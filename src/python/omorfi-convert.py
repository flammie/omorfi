#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# string munging
from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stdin, stdout, stderr
# statistics
from time import perf_counter, process_time

# omorfi
from omorfi.token import is_tokenlist_oov
from omorfi.doc import Doc
from omorfi.fileformats import next_vislcg, next_conllu, next_plaintext


def main():
    """Convert from non-omorfi format back to omorfi."""
    a = ArgumentParser()
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    a.add_argument('-o', '--output', metavar="OUTFILE", dest="outfile",
                   help="print output into OUTFILE", type=FileType('w'))
    a.add_argument('-I', '--informat', metavar="INFORMAT", required=True,
                   help="read input using INFORMAT tokenisation",
                   choices=['tokens', 'vislcg', 'conllu'])
    a.add_argument('-O', '--outformat', metavar='OUTFORMAT', default="json",
                   choices=['json'])
    options = a.parse_args()
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
    doc = Doc()
    while not eoffed:
        if options.format == 'vislcg':
            tokens = next_(options.infile)
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
        doc.add(tokens)
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
