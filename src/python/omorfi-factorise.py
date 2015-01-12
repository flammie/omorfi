#!/usr/bin/env python3

from sys import stdin
from argparse import ArgumentParser
from omorfi.omorfi import Omorfi
import re

def main():
    """Preprocess text for moses factored modeling."""
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSAPATH',
            help="Path to directory of HFST format automata")
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
            dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
            help="print verbosely while processing")
    a.add_argument('-o', '--output', metavar="OUTFILE", required=True,
            help="print factors into OUTFILE")
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    if options.fsa:
        if options.verbose:
            print("Reading automata dir", options.fsa)
        omorfi.load_from_dir(options.fsa)
    else:
        if options.verbose:
            print("Searching for automata everywhere...")
        omorfi.load_from_dir()
    if not options.infile:
        options.infile = stdin
    if options.verbose:
        print("reading from", options.infile.name)
    if options.verbose:
        print("writign to", options.output)

    re_lemma = re.compile("\[WORD_ID=([^]]*)\]")
    re_pos = re.compile("\[POS=([^]]*)\]")
    re_mrd = re.compile("\[([^=]*)=([^]]*)]")
    with open(options.output, 'w') as outfile:
        for line in options.infile:
            line = line.strip()
            if not line or line == '':
                continue
            surfs = line.split()
            for surf in surfs:
                anals = omorfi.analyse(surf)
                segments = omorfi.segment(surf)
                pos_matches = re_pos.finditer(anals[0].output)
                pos = "UNK"
                mrds = []
                lemmas = []
                for pm in pos_matches:
                    pos = pm.group(1)
                lemma_matches = re_lemma.finditer(anals[0].output)
                for lm in lemma_matches:
                    lemmas += [lm.group(1)]
                mrd_matches = re_mrd.finditer(anals[0].output)
                for mm in mrd_matches:
                    if mm.group(1) == 'WORD_ID':
                        mrds = []
                    elif mm.group(1) == 'WEIGHT':
                        pass
                    else:
                        mrds += [mm.group(2)]
                stemfixes = segments[0].output[segments[0].output.rfind("{STUB}"):].replace("{STUB}", "")
                if '{' in stemfixes:
                    morphs = stemfixes[stemfixes.find("{"):].replace("{MB}", ".")
                else:
                    morphs = '0'
                print(surf, '+'.join(lemmas), pos, '.'.join(mrds),
                        morphs, sep='|', end=' ', file=outfile)
            print(file=outfile)
    exit(0)

if __name__ == "__main__":
    main()

