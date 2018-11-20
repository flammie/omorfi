#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command-line interface for omorfi analysis in VISL CG-3 formats."""

# string munging
from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stdin, stdout, stderr
# statistics
from time import perf_counter, process_time

# omorfi
from omorfi import Omorfi
from omorfi.formats.fileformats import next_conllu, next_vislcg, next_plaintext
from omorfi.disamparsulate import Disamparsulator


def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-a', '--analyser', metavar='AFILE',
                   help="load analyser model from AFILE")
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    a.add_argument('-o', '--output', metavar="OUTFILE", dest="outfile",
                   help="print output into OUTFILE", type=FileType('w'))
    a.add_argument('-F', '--format', metavar="INFORMAT", default='text',
                   help="read input using INFORMAT tokenisation",
                   choices=['text', 'vislcg', 'conllu', 'sentences'])
    a.add_argument('-x', '--statistics', metavar="STATFILE", dest="statfile",
                   help="print statistics to STATFILE", type=FileType('w'))
    a.add_argument('--not-rules', metavar="RULEFILE", type=open,
                   help="read non-rules from RULEFILE")
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    if options.analyser:
        if options.verbose:
            print("reading analyser model", options.analyser)
        omorfi.load_analyser(options.analyser)
    else:
        print("analyser is required to vislcg", file=stderr)
        exit(4)
    disamparsulator = None
    if options.not_rules:
        if options.verbose:
            print("Reading rulestuff", options.not_rules.name)
        disamparsulator = Disamparsulator()
        disamparsulator.frobblesnizz(options.not_rules)
    if not options.infile:
        options.infile = stdin
    if options.verbose:
        print("analysing", options.infile.name)
    if not options.outfile:
        options.outfile = stdout
    if options.verbose:
        print("writing to", options.outfile.name)
    if not options.statfile:
        if options.outfile == stdout:
            options.statfile = stdout
        else:
            options.statfile = stderr
    # statistics
    realstart = perf_counter()
    cpustart = process_time()
    tokencount = 0
    unknowns = 0
    eoffed = False
    while not eoffed:
        if options.format == 'vislcg':
            tokens = next_vislcg(options.infile)
        elif options.format == 'text':
            tokens = next_plaintext(options.infile)
        elif options.format == 'conllu':
            tokens = next_conllu(options.infile)
        else:
            print("input format missing implementation", options.format,
                  file=stderr)
            exit(2)
        if not tokens:
            break
        for token in tokens:
            if token.surf:
                tokencount += 1
                omorfi.analyse(token)
                if token.is_oov():
                    unknowns += 1
                    omorfi.guess(token)
            elif token.error or token.nontoken:
                pass
            else:
                print("Unrecognised", token, file=stderr)
                exit(2)
        if disamparsulator:
            disamparsulator.linguisticate(tokens)
        for token in tokens:
            if token.nontoken and token.nontoken == "eof":
                eoffed = True
                break
            print(token.printable_vislcg(), file=options.outfile)
    cpuend = process_time()
    realend = perf_counter()
    print("# Tokens:", tokencount, "\n# Unknown:", unknowns,
          unknowns / tokencount * 100 if tokencount > 0 else 0, "%",
          file=options.statfile)
    print("# CPU time:", cpuend - cpustart,
          "\n# Real time:", realend - realstart,
          file=options.statfile)
    print("# Tokens per timeunit:", tokencount / (realend - realstart),
          file=options.statfile)
    exit(0)


if __name__ == "__main__":
    main()
