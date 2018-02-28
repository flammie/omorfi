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
from omorfi.token import get_lemmas, get_last_feat, get_last_feats, \
        get_vislcg_feats


def print_analyses_vislcg3(surf, anals, outfile):
    print('"<', surf['surf'], '>"', sep='', file=outfile)
    re_mrd = re.compile("\[([^=]*)=([^]]*)]")
    for anal in anals:
        lemmas = get_lemmas(anal)
        mrds = get_vislcg_feats(anal)
        print('\t"', '#'.join(lemmas).replace('"', '\\"'), '" ',
              ' '.join(mrds), ' <CMP=' + str(len(lemmas)) + '>',
              sep='', file=outfile)

def get_surfs(line, omorfi):
    if not line or line == '':
        return [{'comment': ''}]
    surfs = omorfi.tokenise(line)
    first_in_sent = True
    for surf in surfs:
        if first_in_sent and surf["surf"][0].isupper():
            if "analsurf" not in surf or surf['analsurf'][0].isupper():
                surf['analsurf_override'] = surf['surf'][0].lower() + \
                        surf['surf'][1:]
                first_in_sent = False
    return surfs

def get_vislcg_surfs(line, prev):
    line = line.rstrip()
    if not line or line == '':
        return [{'comment': ''}]
    elif line.startswith("#") or line.startswith("<"):
        return [{'comment': line.strip()}]
    elif line.startswith('"<') and line.endswith('>"'):
        surf = {'surf': line[2:-2]}
        if prev and 'comment' in prev and (prev['comment'] == '' or \
                prev['comment'].startswith('#') or \
                prev['comment'].startswith('<')) and \
                surf['surf'][0].isupper():
            surf['analsurf_override'] = surf['surf'][0].lower() + \
                    surf['surf'][1:]
        return [surf]
    elif line.startswith('\t"') or line.startswith(';\t"'):
        # gold?
        return [{'comment': line}]
    else:
        return [{'error': 'vislcg parsing: ' + line}]

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
    a.add_argument('-F', '--format', metavar="INFORMAT", default='text',
                   help="read input using INFORMAT tokenisation",
                   choices=['text', 'vislcg'])
    a.add_argument('-x', '--statistics', metavar="STATFILE", dest="statfile",
                   help="print statistics to STATFILE", type=FileType('w'))
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
    unknowns = 0
    last = None
    for line in options.infile:
        surfs = []
        if options.format == 'vislcg':
            surfs = get_vislcg_surfs(line, last)
        elif options.format == 'text':
            surfs = get_surfs(line, omorfi)
        else:
            print("input format missing implementation", options.format,
                file=stderr)
            exit(2)
        for surf in surfs:
            if 'surf' in surf:
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
    print("Tokens:", tokens, "Unknown:", unknowns, unknowns / tokens * 100,
          "%", file=options.statfile)
    print("CPU time:", cpuend - cpustart, "Real time:", realend - realstart,
          file=options.statfile)
    print("Tokens per timeunit:", tokens / (realend - realstart),
          file=options.statfile)
    exit(0)


if __name__ == "__main__":
    main()
