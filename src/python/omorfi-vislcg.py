#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# string munging
import re
from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stdin, stdout
# statistics
from time import perf_counter, process_time

# omorfi
from omorfi.omorfi import Omorfi


def get_lemmas(anal):
    re_lemma = re.compile("\[WORD_ID=([^]]*)\]")
    lemmas = re_lemma.finditer(anal['anal'])
    rv = []
    for lemma in lemmas:
        rv += [lemma.group(1)]
    return rv


def get_last_feat(feat, anal):
    re_feat = re.compile("\[" + feat + "=([^]]*)\]")
    feats = re_feat.finditer(anal[0])
    rv = ""
    for feat in feats:
        rv = feat.group(1)
    return rv


def get_last_feats(anal):
    re_feats = re.compile("\[[^]]*\]")
    rvs = list()
    feats = re_feats.finditer(anal[0][0])
    for feat in feats:
        if 'BOUNDARY=' in feat.group(0) or 'WORD_ID=' in feat.group(0):
            rvs = list()
        else:
            rvs.append(feat.group(0))
    return rvs


def print_analyses_vislcg3(surf, anals, outfile):
    print('"<', surf['surf'], '>"', sep='', file=outfile)
    re_mrd = re.compile("\[([^=]*)=([^]]*)]")
    for anal in anals:
        mrds = []
        lemmas = get_lemmas(anal)
        mrd_matches = re_mrd.finditer(anal['anal'])
        for mm in mrd_matches:
            if mm.group(1) == 'WORD_ID':
                mrds = []
            elif mm.group(1) == 'CASECHANGE' and mm.group(2) != 'NONE':
                mrds = ['<' + mm.group(2) + '>'] + mrds
            elif mm.group(1) == 'ALLO':
                mrds = ['<' + mm.group(2) + '>'] + mrds
            elif mm.group(1) == 'WEIGHT' and mm.group(2) != 'inf':
                mrds += ['<W=' + str(int(float(mm.group(2)) * 100)) + '>']
            elif mm.group(1) == 'WEIGHT' and mm.group(2) == 'inf':
                mrds += ['<W=65536>']
            elif mm.group(1) in ['STYLE']:
                mrds += ['<' + mm.group(2) + '>']
            else:
                mrds += [mm.group(2)]
        print('\t"', ''.join(lemmas).replace('"', '\\"'), '" ',
              ' '.join(mrds), sep='', file=outfile)
    print(file=outfile)


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
    for line in options.infile:
        line = line
        if not line or line == '':
            continue
        surfs = omorfi.tokenise(line)
        for surf in surfs:
            tokens += 1
            anals = omorfi.analyse(surf)
            if len(anals) == 0 or (len(anals) == 1 and
                                   'UNKNOWN' in anals[0]['anal']):
                unknowns += 1
                anals = omorfi.guess(surf)
            print_analyses_vislcg3(surf, anals, options.outfile)
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
