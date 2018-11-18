#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stdin, stdout, stderr
# statistics
from time import perf_counter, process_time

import json

# omorfi
from omorfi import Omorfi


def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-a', '--analyser', metavar='AFILE',
                   help="load tokeniser model from (analyser) AFILE",
                   required=True)
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    a.add_argument('-o', '--output', metavar="OUTFILE", dest="outfile",
                   help="print output into OUTFILE", type=FileType('w'))
    a.add_argument('-x', '--statistics', metavar="STATFILE", dest="statfile",
                   help="print statistics to STATFILE", type=FileType('w'))
    a.add_argument('-O', '--output-format', metavar="OUTFORMAT",
                   default="moses",
                   help="format output for OUTFORMAT", choices=['moses',
                                                                'conllu',
                                                                'json',
                                                                'ftb3'])
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    if options.analyser:
        if options.verbose:
            print("reading language model", options.analyser)
        omorfi.load_analyser(options.analyser)
    else:
        print("analyser is needed for tokenisation", file=stderr)
        exit(1)
    if not options.infile:
        options.infile = stdin
    if options.verbose:
        print("analysing", options.infile.name)
    if not options.outfile:
        options.outfile = stdout
    if options.verbose:
        print("writing to", options.outfile.name)
    if not options.statfile:
        options.statfile = stderr
    # statistics
    realstart = perf_counter()
    cpustart = process_time()
    tokens = 0
    lines = 0
    if options.output_format == 'conllu':
        print("# new doc id=", options.infile.name, file=options.outfile)
    for line in options.infile:
        line = line
        lines += 1
        if options.verbose and lines % 10000 == 0:
            print(lines, "...")
        if not line or line.rstrip('\n') == '':
            continue
        surfs = omorfi.tokenise(line)
        tokens += len(surfs)
        if options.output_format == 'moses':
            print(' '.join([surf.surf for surf in surfs]),
                  file=options.outfile)
        elif options.output_format == 'json':
            print(json.encode(surfs))
        elif options.output_format == 'conllu':
            print("# sent_id =", lines, file=options.outfile)
            print("# text =", line.rstrip("\n"), file=options.outfile)
            i = 1
            for surf in surfs:
                print(i, surf['surf'], "_", "_", "_", "_", "_", "_", "_", "_",
                      sep="\t", file=options.outfile)
                i += 1
        elif options.output_format == 'ftb3':
            print("<s><loc file=\"", options.infile.name, "\" line=\"",
                  lines, "\" />", file=options.outfile, sep="")
            i = 1
            for surf in surfs:
                print(i, surf['surf'], "_", "_", "_", "_", "_", "_", "_", "_",
                      sep="\t", file=options.outfile)
                i += 1
            print("</s>", file=options.outfile)
        if options.output_format == 'conllu':
            print(file=options.outfile)
    cpuend = process_time()
    realend = perf_counter()
    print("Lines:", lines, "Tokens:", tokens, "Ratio:", tokens / lines,
          "tokens/line", file=options.statfile)
    print("CPU time:", cpuend - cpustart, "Real time:", realend - realstart,
          file=options.statfile)
    print("Tokens per timeunit:", tokens / (realend - realstart),
          "Lines per timeunit:", lines / (realend - realstart),
          file=options.statfile)
    exit(0)


if __name__ == "__main__":
    main()
