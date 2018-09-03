#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# string munging
from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stdin, stdout, stderr
# statistics
from time import perf_counter, process_time

# omorfi
from omorfi import Omorfi
from omorfi.token import is_tokenlist_oov


def print_analyses_vislcg3(surf, anals, outfile):
    print('"<%s>"' % (anals[0].surf), file=outfile)
    for anal in anals:
        print(anal.printable_vislcg(), file=outfile)


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
                   choices=['text', 'vislcg', 'conllu'])
    a.add_argument('-x', '--statistics', metavar="STATFILE", dest="statfile",
                   help="print statistics to STATFILE", type=FileType('w'))
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    if options.analyser:
        if options.verbose:
            print("reading analyser model", options.analyser)
        omorfi.load_analyser(options.analyser)
    else:
        print("analyser is required to vislcg", file=stderr)
        exit(4)
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
            tokens = omorfi.tokenise_vislcg(options.infile)
        elif options.format == 'text':
            tokens = omorfi.tokenise_plaintext(options.infile)
        elif options.format == 'conllu':
            tokens = omorfi.tokenise_conllu(options.infile)
        else:
            print("input format missing implementation", options.format,
                  file=stderr)
            exit(2)
        if not tokens:
            break
        for token in tokens:
            if token.error:
                print(token.error, file=stderr)
                exit(2)
            elif token.nontoken:
                if token.nontoken == 'comment':
                    print(token.comment, file=options.outfile)
                elif token.nontoken == 'separator':
                    print(file=options.outfile)
                elif token.nontoken == 'eof':
                    eoffed = True
                    break
                else:
                    print("Unrecognised", token, file=stderr)
                    exit(2)
            elif token.surf:
                tokencount += 1
                anals = omorfi.analyse(token)
                if is_tokenlist_oov(anals):
                    unknowns += 1
                    anals = omorfi.guess(token)
                print_analyses_vislcg3(token, anals, options.outfile)
            else:
                print("Unrecognised", token, file=stderr)
                exit(2)
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
