#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stderr, stdin, stdout
# statistics
from time import perf_counter, process_time

# omorfi
from omorfi import Omorfi


def try_analyses_ftb(original, wordn, surf, anals, outfile, hacks=None):
    for anal in anals:
        pos = anal.format_xpos_ftb()
        if pos == original[3]:
            feats = anal.format_feats_ftb()
            if feats == original[5]:
                lemmas = "#".join(anal.get_lemmas())
                if lemmas == original[2]:
                    return print_analyses_ftb(wordn, surf, anal, outfile)
    # no exact match found (re-try without lemma)
    for anal in anals:
        upos = anal.format_xpos_ftb()
        if upos == original[3]:
            feats = anal.format_feats_ftb()
            if feats == original[5]:
                return print_analyses_ftb(wordn, surf, anal, outfile)
    # and re-try without feats
    for anal in anals:
        upos = anal.format_xpos_ftb()
        if upos == original[3]:
            return print_analyses_ftb(wordn, surf, anal, outfile)
    return print_analyses_ftb(wordn, surf, anals[0], outfile)


def print_analyses_ftb(wordn, surf, anal, outfile, hacks=None):
    pos = anal.format_xpos_ftb()
    print(wordn, surf, "#".join(anal.get_lemmas()),
          pos,
          pos,
          anal.format_feats_ftb(),
          "_", "_", "_", "_", sep="\t", file=outfile)


def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-a', '--analyser', metavar='AFILE',
                   help="read analyser model from AFILE",
                   required=True)
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    a.add_argument('-o', '--output', metavar="OUTFILE", dest="outfile",
                   help="print output into OUTFILE", type=FileType('w'))
    a.add_argument('-x', '--statistics', metavar="STATFILE", dest="statfile",
                   help="print statistics to STATFILE", type=FileType('w'))
    a.add_argument('-O', '--oracle', action='store_true',
                   help="match to values in input when parsing if possible")
    a.add_argument('-X', '--frequencies', metavar="FREQDIR",
                   help="read frequencies from FREQDIR/*.freqs")
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
        print("analyser is needed to ftb3", file=stderr)
        exit(4)
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

    if options.frequencies:
        with open(options.frequencies + '/lexemes.freqs') as lexfile:
            omorfi.load_lexical_frequencies(lexfile)
        with open(options.frequencies + '/omors.freqs') as omorfile:
            omorfi.load_omortag_frequencies(omorfile)

    # statistics
    realstart = perf_counter()
    cpustart = process_time()
    tokens = 0
    unknowns = 0
    sentences = 0
    for line in options.infile:
        fields = line.strip().split('\t')
        if len(fields) == 10:
            # ftb is 10 field format
            tokens += 1
            try:
                index = int(fields[0])
            except ValueError:
                print("Cannot figure out token index", fields[0], file=stderr)
                exit(1)
            surf = fields[1]
            anals = omorfi.analyse(surf)
            if not anals or len(anals) == 0 or (len(anals) == 1 and
                                                'OOV' in anals[0]):
                unknowns += 1
                anals = omorfi.guess(surf)
            if anals and len(anals) > 0:
                if options.oracle:
                    try_analyses_ftb(fields, index, surf, anals,
                                     options.outfile)
                else:
                    print_analyses_ftb(index, surf, anals[0],
                                       options.outfile)
            else:
                print("Failed:", fields)
                exit(1)
        elif line.startswith('<') and line.rstrip().endswith('>'):
            print(line.strip(), file=options.outfile)
        elif not line or line.strip() == '':
            # retain exactly 1 empty line between sents
            print(file=options.outfile)
            sentences += 1
        else:
            print("Error in ftb3 format: '", line, "'", file=stderr)
            exit(1)
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
    exit(0)


if __name__ == "__main__":
    main()
