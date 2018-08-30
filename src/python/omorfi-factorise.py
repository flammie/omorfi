#!/usr/bin/env python3

import re
from argparse import ArgumentParser
from sys import stdin, stdout, stderr

from omorfi.omorfi import Omorfi


def main():
    """Preprocess text for moses factored modeling."""
    a = ArgumentParser()
    a.add_argument('-a', '--analyser', metavar='AFILE',
                   help="load analyser model from AFILE", required=True)
    a.add_argument('-s', '--segmenter', metavar='SFILE',
                   help="load segmenter model from SFILE", required=True)
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    a.add_argument('-o', '--output', metavar="OUTFILE",
                   help="print factors into OUTFILE")
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    if options.analyser:
        if options.verbose:
            print("Reading analyser model", options.analyser)
        omorfi.load_analyser(options.analyser)
    else:
        print("at least analyser file is needed", file=stderr)
        exit(1)
    if options.segmenter:
        if options.verbose:
            print("Reading segmenter model", options.segmenter)
        omorfi.load_segmenter(options.segmenter)
    else:
        print("at least segmenter file is needed", file=stderr)
        exit(1)
    if options.infile:
        infile = options.infile
    else:
        infile = stdin
    if options.output:
        outfile = open(options.output, 'w')
    else:
        outfile = stdout
    if options.verbose:
        print("reading from", infile.name)
    if options.verbose:
        print("writign to", outfile.name)
    linen = 0
    for line in infile:
        line = line.strip()
        linen += 1
        if options.verbose and linen % 10000 == 0:
            print(linen, '...')
        if not line or line == '':
            continue
        tokens = omorfi.tokenise_sentence(line)
        for token in tokens:
            if not token.surf:
                continue
            anals = omorfi.analyse(token)
            segments = omorfi.segment(token)
            pos = anals[0].get_upos()
            mrds = anals[0].get_last_feats()
            lemmas = anals[0].get_lemmas()
            parts = segments[0].segments
            if '{DB}' in parts:
                suffixes = parts[parts.rfind('{DB}')+4:]
            elif '{WB}' in parts:
                suffixes = parts[parts.rfind('{WB}')+4:]
            elif '{hyph?}' in parts:
                suffixes = parts[parts.rfind('{hyph?}')+6:]
            else:
                suffixes = "0"
            morphs = suffixes[suffixes.find("{"):].replace("{MB}", ".")
            print(token.surf, '+'.join(lemmas), pos, '.'.join(mrds),
                  morphs, sep='|', end=' ', file=outfile)
        print(file=outfile)
    exit(0)


if __name__ == "__main__":
    main()
