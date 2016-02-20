#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CLI stuff
from sys import stdin, stdout
from argparse import ArgumentParser, FileType
# omorfi
from omorfi.omorfi import Omorfi
# statistics
from time import perf_counter, process_time


def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSAPATH',
                   help="Path to directory of HFST format automata")
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
                   help="format output for OUTFORMAT", choices=['moses', 'conllu'])
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    if options.fsa:
        if options.verbose:
            print("reading language models in", options.fsa)
        omorfi.load_from_dir(options.fsa, analyse=True, accept=True)
    else:
        if options.verbose:
            print("reading language models in default dirs")
        omorfi.load_from_dir()
    if not options.infile:
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
    lines = 0
    if options.output_format == 'conllu':
        print("# doc-name:", options.infile.name, file=options.outfile)
    for line in options.infile:
        line = line
        lines += 1
        if not line or line.rstrip('\n') == '':
            continue
        surfs = omorfi.tokenise(line)
        tokens += len(surfs)
        if options.output_format == 'moses':
            print(' '.join([surf[0] for surf in surfs]), file=options.outfile)
        else:
            print("# sentence-text:", line.rstrip("\n"), file=options.outfile)
            i = 1
            for surf in surfs:
                print(i, surf[0], "_", "_", "_", "_", "_", "_", "_",
                      surf[1],
                      sep="\t", file=options.outfile)
                i += 1
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
