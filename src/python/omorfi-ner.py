#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A command-line interface for omorfi NER parsing."""

# string munging
from argparse import ArgumentParser, FileType
# CLI stuff
import sys
from sys import stderr, stdin, stdout
# statistics
from time import perf_counter, process_time
# omorfi
import csv
from omorfi import Omorfi
from omorfi.formats.fileformats import next_finer


def propntype2ner(s):
    if s == "Geo":
        return "LOC"
    elif s == "First":
        return "PER"
    elif s == "Last":
        return "PER"
    elif s == "Org":
        return "ORG"
    elif s == "Product":
        return "PRO"
    elif s == "Cultgrp":
        return "ORG"  # XXX
    elif s == "Misc":
        return "ORG"  # XXX
    else:
        print("PropnType missing:", s)
        sys.exit(1)
        return "PRO"  # XXX


def get_ner_b(analysis):
    if "PropnType" in analysis.misc:
        return "B-" + propntype2ner(analysis.misc["PropnType"])
    else:
        return "O"  # XXX


def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-a', '--analyser', metavar='AFILE', required=True,
                   help="read analyser model from AFILE")
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    a.add_argument('-o', '--output', metavar="OUTFILE", dest="outfile",
                   help="print output into OUTFILE", type=FileType('w'))
    a.add_argument('-x', '--statistics', metavar="STATFILE", dest="statfile",
                   help="print statistics to STATFILE", type=FileType('w'))
    a.add_argument('-M', '--mwe', metavar="MWEFILE",
                   help="open mwe master db tsv from MWEFILE")
    a.add_argument('--debug', action='store_true',
                   help="print lots of debug info while processing")
    options = a.parse_args()
    if options.verbose:
        print("Printing verbosely")
    omorfi = Omorfi(options.verbose)
    if options.analyser:
        if options.verbose:
            print("reading analyser model", options.analyser)
        omorfi.load_analyser(options.analyser)
    else:
        print("analyser is needed to mwe", file=stderr)
        sys.exit(4)
    mwedata = dict()
    if options.mwe:
        with open(options.mwe, "r", newline='') as mwefile:
            mwe_reader = csv.DictReader(mwefile, delimiter='\t',
                                        quoting=csv.QUOTE_NONE, escapechar='\\',
                                        quotechar=None, strict=True)
            for mwe_parts in mwe_reader:
                mwedata[mwe_parts['lemma']] = mwe_parts
    if not options.infile:
        print("reading from <stdin>")
        options.infile = stdin
    if options.verbose:
        print("analysing", options.infile.name)
    if not options.outfile:
        options.outfile = stdout
    if options.verbose:
        print("writing to", options.outfile.name)
    if not options.statfile:
        options.statfile = stdout
    # statistics
    realstart = perf_counter()
    cpustart = process_time()
    tokens = 0
    unknowns = 0
    sentences = 0
    eoffed = False
    previous_ner = list()
    previous_anal = list()
    insidemwe = False
    mwefinished = False
    reported_already = list()
    while not eoffed:
        sentplus = next_finer(options.infile)
        if not sentplus:
            eoffed = True
            break
        for token in sentplus:
            if token.nontoken:
                if token.nontoken == 'eof':
                    eoffed = True
                    break
                elif token.nontoken == 'separator':
                    sentences += 1
                    print(file=options.outfile)
                    continue
                elif token.nontoken == 'error':
                    print("Error at line:", token.error, file=stderr)
                    sys.exit(1)
                elif token.nontoken == 'markup?':
                    if token.comment not in reported_already:
                        print("Ignoring markup?", token.comment, file=stderr)
                        reported_already.append(token.comment)
                    print(token.comment, file=options.outfile)
                    continue
                else:
                    print("Error:", token, file=stderr)
                    sys.exit(1)
            elif not token.surf:
                print("No can find surface token in finer?", token, file=stderr)
                sys.exit(1)
            tokens += 1
            omorfi.analyse(token)
            if token.is_oov():
                omorfi.guess(token)
            insidemwe = False
            propnfound = False
            mwefinished = False
            for analysis in token.analyses:
                # check MWE NER
                maybe_mwe = ' '.join(previous_ner) + token.surf
                maybe_mwe2 = ' '.join(previous_ner) + ''.join(analysis.lemmas)
                for k in mwedata.keys():
                    if k.startswith(maybe_mwe + ' '):
                        previous_ner.append(token.surf)
                        previous_anal.append(get_ner_b(analysis))
                        insidemwe = True
                        break
                    elif k in [maybe_mwe, maybe_mwe2]:
                        previous_anal.append(token.surf)
                        insidemwe = False
                        mwefinished = True
                        if 'proper_noun_class' in mwedata[maybe_mwe]:
                            analtype = propntype2ner(
                                mwedata[maybe_mwe]['proper_noun_class'])
                            previous_anal[0] = "B-" + analtype
                            for i in range(1, len(previous_ner)):
                                previous_anal[i] = ["I-" + analtype]
                        break
                if insidemwe or mwefinished:
                    break
                # Check PropnType single-word
                if "PropnType" in analysis.misc:
                    previous_ner.append(token.surf)
                    if get_ner_b(analysis) == 'O':
                        propnfound = False
                    elif previous_anal and previous_anal != 'O':
                        analtype = previous_anal[-1][2:]
                        if analtype and analtype in get_ner_b(analysis):
                            previous_anal.append('I-' + analtype)
                        else:
                            previous_anal.append(get_ner_b(analysis))
                        propnfound = True
                    else:
                        previous_anal.append(get_ner_b(analysis))
                        propnfound = True
                    break
                if token.surf in ["vuonna",
                                  "tammikuussa", "helmikuussa",
                                  "maaliskuussa", "huhtikuussa", "toukokuussa",
                                  "kesäkuussa", "heinäkuussa", "elokuussa",
                                  "syyskuussa", "lokakuussa", "marraskuussa",
                                  "joulukuussa",
                                  "tammikuun", "helmikuun",
                                  "maaliskuun", "huhtikuun", "toukokuun",
                                  "kesäkuun", "heinäkuun", "elokuun",
                                  "syyskuun", "lokakuun", "marraskuun",
                                  "joulukuun"
                                  ]:
                    propnfound = True  # "PROPN" lol
                    previous_ner.append(token.surf)
                    previous_anal.append("B-DATE")
                    break
                if token.surf.isdigit():
                    if len(previous_anal) == 1 and previous_anal[-1] == 'B-DATE':
                        previous_anal.append("I-DATE")
                        previous_ner.append(token.surf)
                        propnfound = True
                        break
                    elif len(previous_anal) == 0 or previous_anal[-1] == 'O':
                        previous_anal.append("B-DATE")
                        previous_ner.append(token.surf)
                        propnfound = True
                        break
            if not propnfound and not insidemwe:
                previous_ner.append(token.surf)
                previous_anal.append("O")
                for i, ner in enumerate(previous_ner):
                    print(ner, previous_anal[i], sep="\t",
                          file=options.outfile)
                previous_ner.clear()
                previous_anal.clear()

    cpuend = process_time()
    realend = perf_counter()
    print("Tokens:", tokens, "Sentences:", sentences,
          file=options.statfile)
    print("Unknowns / OOV:", unknowns, "=",
          unknowns / tokens * 100 if tokens != 0 else 0,
          "%", file=options.statfile)
    print("CPU time:", cpuend - cpustart, "Real time:", realend - realstart,
          file=options.statfile)
    print("Tokens per timeunit:", tokens / (realend - realstart),
          file=options.statfile)
    print("Sentences per timeunit:", sentences / (realend - realstart),
          file=options.statfile)
    sys.exit(0)


if __name__ == "__main__":
    main()
