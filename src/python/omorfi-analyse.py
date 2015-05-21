#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stderr, stdin, stdout
from argparse import ArgumentParser, FileType
from omorfi.omorfi import Omorfi

import re

def print_analyses(surf, anals, format, outfile):
    if format == 'xerox':
        print_analyses_xerox(surf, anals, outfile)
    elif format == 'apertium':
        print_analyses_apertium(surf, anals, outfile)
    elif format == 'vislcg3':
        print_analyses_vislcg3(surf, anals, outfile)
    elif format == 'conllx':
        print_analyses_conllx(surf, anals, outfile)
    elif format == 'conllu':
        print_analyses_conllu(surf, anals, outfile)
    else:
        print("format unknown:", format, file=stderr)
        exit(2)

def print_analyses_xerox(surf, anals, outfile):
    for anal in anals:
        print(surf, anal.output, sep='\t', file=outfile)
    print

def print_analyses_apertium(surf, anals, outfile):
    print("^", surf, sep='')
    for anal in anals:
        print("/", anal.output, sep='', file=outfile)
    print("$")

def print_analyses_vislcg3(surf, anals, outfile):
    print('"<', surf, '>"', sep='', file=outfile)
    re_lemma = re.compile("\[WORD_ID=([^]]*)\]")
    re_pos = re.compile("\[POS=([^]]*)\]")
    re_mrd = re.compile("\[([^=]*)=([^]]*)]")
    for anal in anals:
        pos_matches = re_pos.finditer(anal.output)
        pos = "UNK"
        mrds = []
        lemmas = []
        for pm in pos_matches:
            pos = pm.group(1)
        lemma_matches = re_lemma.finditer(anal.output)
        for lm in lemma_matches:
            lemmas += [lm.group(1)]
        mrd_matches = re_mrd.finditer(anal.output)
        for mm in mrd_matches:
            if mm.group(1) == 'WORD_ID':
                mrds = []
            elif mm.group(1) == 'CASECHANGE' and mm.group(2) != 'NONE':
                mrds = ['<*>'] + mrds
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

def print_analyses_conllx(surf, anals, outfile):
    print(1, surf, surf, anals[0].output[0], anals[0].output[0], anals[0].output,
            "-", "-", "-", "-", sep="\t", file=outfile)

def print_analyses_conllu(surf, anals, outfile):
    print(1, surf, surf, anals[0].output[0], anals[0].output[0], anals[0].output,
            "-", "-", "-", "-", sep="\t", file=outfile)

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
    a.add_argument('-F', '--format', metavar='FORMAT', required=True,
            help="Output in format compatible with FORMAT",
            choices=['xerox', 'apertium', 'vislcg3', 'conllx', 'conllu'])
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
    for line in options.infile:
        line = line
        if not line or line == '':
            continue
        surfs = omorfi.tokenise(line)
        for surf in surfs:
            anals = omorfi.analyse(surf)
            print_analyses(surf, anals, options.format, options.outfile)
    exit(0)

if __name__ == "__main__":
    main()
