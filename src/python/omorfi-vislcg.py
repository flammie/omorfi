#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# string munging
import re
from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stdin, stdout, stderr
# statistics
from time import perf_counter, process_time

# omorfi
from omorfi.omorfi import Omorfi
from omorfi.token import get_lemmas, \
        get_vislcg_feats, get_line_tokens, get_line_tokens_vislcg, \
        get_line_tokens_conllu


def print_analyses_vislcg3(surf, anals, outfile):
    print('"<', surf['surf'], '>"', sep='', file=outfile)
    re_mrd = re.compile("\[([^=]*)=([^]]*)]")
    for anal in anals:
        lemmas = get_lemmas(anal)
        mrds = get_vislcg_feats(anal)
        print('\t"', '#'.join(lemmas), '" ',
              ' '.join(mrds), ' <CMP=' + str(len(lemmas)) + '>',
              sep='', file=outfile)

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
    tokens = 0
    unknowns = 0
    last = None
    for line in options.infile:
        surfs = []
        if options.format == 'vislcg':
            surfs = get_line_tokens_vislcg(line, last)
        elif options.format == 'text':
            surfs = get_line_tokens(line, omorfi)
        elif options.format == 'conllu':
            surfs = get_line_tokens_conllu(line, last)
        else:
            print("input format missing implementation", options.format,
                  file=stderr)
            exit(2)
        for surf in surfs:
            if 'conllu_form' in surf:
                # skip conllu special forms in input for now:
                # (ellipsis and MWE magics)
                continue
            elif 'surf' in surf:
                tokens += 1
                anals = omorfi.analyse(surf)
                if len(anals) == 0 or (len(anals) == 1 and
                                       'UNKNOWN' in anals[0]['anal']):
                    unknowns += 1
                    anals = omorfi.guess(surf)
                print_analyses_vislcg3(surf, anals, options.outfile)
            elif 'comment' in surf:
                if surf['comment'].startswith(';') or \
                       surf['comment'].startswith('\t'):
                    continue
                else:
                    print(surf['comment'], file=options.outfile)
            elif 'error' in surf:
                print(surf['error'], file=stderr)
                exit(2)
            last = surf
    cpuend = process_time()
    realend = perf_counter()
    print("# Tokens:", tokens, "\n# Unknown:", unknowns,
          unknowns / tokens * 100, "%", file=options.statfile)
    print("# CPU time:", cpuend - cpustart,
          "\n# Real time:", realend - realstart,
          file=options.statfile)
    print("# Tokens per timeunit:", tokens / (realend - realstart),
          file=options.statfile)
    exit(0)


if __name__ == "__main__":
    main()
