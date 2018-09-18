#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A command-line interface for omorfi with CONLL-U I/O formats."""

# string munging
from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stderr, stdin, stdout
# statistics
from time import perf_counter, process_time

# omorfi
from omorfi import Omorfi
from omorfi.fileformats import next_conllu


def get_reference_conllu_list(token):
    if not token.gold:
        print("Oracle data missing from", token, file=stderr)
        exit(2)
    else:
        return token.gold.split("\t")


def try_analyses_conllu(token, outfile, hacks=None):
    anals = token.analyses
    original = get_reference_conllu_list(token)
    best = None
    highest = -1
    for i, anal in enumerate(anals):
        upos = anal.get_upos()
        feats = anal.printable_ud_feats()
        lemmas = anal.get_lemmas()
        if lemmas:
            lemma = '#'.join(anal.get_lemmas())
        else:
            lemma = '_'
        score = 0
        if upos == original[3]:
            score += 10
        if lemma == original[2]:
            score += 10
        elif lemma.strip('#') == original[2].strip('#'):
            score += 5
        elif lemma.lower() == original[2].lower():
            score += 5
        if feats == original[5]:
            score += 10
        else:
            featset = set(feats.split("|"))
            refset = set(original[5].split("|"))
            score += len(featset.intersection(refset))
        if score > highest:
            best = i
            highest = score
    return print_analyses_conllu(token, outfile, hacks, best)


def debug_analyses_conllu(token, outfile, hacks=None):
    anals = token.analyses
    print("# REFERENCE(python):", get_reference_conllu_list(token),
          file=outfile)
    for anal in anals:
        print_analyses_conllu(anal, outfile, hacks)


def print_analyses_conllu(token, outfile, hacks=None, best=0):
    anal = token.analyses[best]
    if anal.rawtype != 'omor':
        print("Trying to omorprint non-omor analysis", anal, file=stderr)
        exit(1)
    upos = anal.get_upos()
    if not upos or upos == "":
        upos = 'X'
    if hacks == 'ftb':
        third = anal.get_xpos_ftb()
    else:
        third = anal.get_xpos_tdt()
    lemmas = anal.get_lemmas()
    if not lemmas:
        lemma = '_'
    else:
        lemma = '#'.join(anal.get_lemmas())
    print(token.pos, token.surf, lemma, upos, third,
          anal.printable_ud_feats(hacks),
          "_", "_", "_", anal.printable_ud_misc(), sep="\t", file=outfile)


def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-a', '--analyser', metavar='AFILE',
                   help="read analyser model from AFILE")
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
    a.add_argument('-u', '--udpipe', metavar="UDPIPE",
                   help='use UDPIPE for additional guesses (experi-mental)')
    a.add_argument('--hacks', metavar='HACKS',
                   help="mangle analyses to match HACKS version of UD",
                   choices=['ftb'])
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
        print("analyser is needed to conllu", file=stderr)
        exit(4)
    if options.udpipe:
        if options.verbose:
            print("Loading udpipe", options.udpipe)
        omorfi.load_udpipe(options.udpipe)
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
    eoffed = False
    while not eoffed:
        sentplus = next_conllu(options.infile)
        if not sentplus:
            eoffed = True
            break
        for token in sentplus:
            if token.nontoken:
                if token.nontoken == 'comment':
                    print(token.comment, file=options.outfile)
                elif token.nontoken == 'eof':
                    eoffed = True
                    break
                elif token.nontoken == 'separator':
                    sentences += 1
                    print(file=options.outfile)
                elif token.nontoken == 'error':
                    print("Unrecognisable line:", token.error, file=stderr)
                    exit(1)
                else:
                    print("Error:", token, file=stderr)
                    exit(1)
                continue
            elif not token.surf:
                print("No surface in CONLL-U?", token, file=stderr)
                exit(1)
            tokens += 1
            omorfi.analyse(token)
            if token.is_oov():
                unknowns += 1
                omorfi.guess(token)
            if options.debug:
                debug_analyses_conllu(token, options.outfile, options.hacks)
            elif options.oracle:
                try_analyses_conllu(token, options.outfile, options.hacks)
            else:
                print_analyses_conllu(token, options.outfile, options.hacks)
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
