#!/usr/bin/env python3

from sys import stdin, stdout
from argparse import ArgumentParser
from omorfi.omorfi import Omorfi
import re

def print_segments(fmt, segments, labelsegments, surf, outfile):
    if fmt == 'labels-moses-factors':
        if labelsegments:
            # öykkärö[UPOS=VERB]i[TRAILS=→][MB=LEFT]dä[TRAILS=→Vpss][?=Tpres][?=Ppe4][?=Ncon][TRAILS=→] 
            analysis = labelsegments[0][0]
            splat = re.split("[]{}[]", analysis)
            skiptag = None
            nextsep = '|'
            moses = ''
            for split in splat:
                if split == '':
                    continue
                elif split in ['STUB', 'hyph?', 'XB']:
                    continue
                elif split in ['SG', 'NOM', 'POS', 'ACTV', 'PRES']:
                    # we actually skip 0 morphs...?
                    continue
                elif split in ['DB', 'MB', 'WB', 'wB']:
                    if skiptag:
                        moses += nextsep + skiptag
                        skiptag = None
                    moses += ' '
                    nextsep = '|'
                elif split in ['NOUN', 'VERB', 'ADJ', 'COMP', 'PROPN', 'SUPER', 'AUX', 'NUM', 'PRON']:
                    skiptag = split
                elif split in ['ADV', 'ADP', 'X', 'PUNCT', 'CONJ',
                        'SCONJ', 'CONJ|VERB', 'INTJ', 'DET']:
                    moses += nextsep + split
                elif split in ['PL', 'INS', 'INE', 'ELA',
                        'ILL', 'ADE', 'ABL', 'ALL', 'ACTV', 'PASV',
                        'IMPV', 'POTN', 'COND', 'SG1', 'SG2', 'SG3', 'PL1',
                        'PL2', 'PL3', 'PAST', 'INFA', 'PAR',
                        'POSSP3', 'POSSG1', 'POSSG2', 'POSPL1', 'POSPL2',
                        'GEN', 'PCPVA', 'INFE', 'PCPMA', 'PCPNUT', 'INFMA',
                        'PE4', 'ABE', 'ESS', 'CONNEG', 'ORD', 'TRA', 'COM',
                        'INFMAISILLA',
                        'HAN', 'KO', 'PA', 'S', 'KAAN', 'KA', 'KIN']:
                    if skiptag:
                        moses += nextsep + skiptag
                        skiptag = None
                        nextsep = '.'
                    moses += nextsep + split
                    nextsep = '.'
                elif split.isupper():
                    print("unhandlend upper string?", split)
                    exit(1)
                else:
                    moses += split
            if skiptag:
                moses += nextsep + skiptag
            # tweaks and hacks
            if " i " in moses or " j " in moses:
                moses = re.sub(r" ([ij]) ([a-zä]*)\|PL.", r" \1|PL \2|", moses)
            moses = re.sub(r" ([a-zåäö]+) ", r" \1|NOUN ", moses)
            moses = re.sub(r"^([a-zåäö]+) ", r"\1|NOUN ", moses)
            moses = re.sub(r"([snrl])\|PCPNUTut", r"\1ut|PCPNUT", moses)
            moses = re.sub(r"([snrl])\|PCPNUTee", r"\1ee|PCPNUT", moses)
            moses = re.sub(r"m\|PCPMA([aä])", r"m\1|PCPMA", moses)
            moses = re.sub(r"v\|PCPVA([aä])", r"v\1|PCPVA", moses)
            moses = re.sub(r"([ei])\|NOUN (n|ssa|ssä)\|INFE.", r"\1|INFE \2|", moses)
            print(moses)

        else:
            print(surf, end='|UNK ', file=outfile)
    elif fmt == 'both-lines':
        if segments and labelsegments:
            print(segments[0][0], labelsegments[0][0], end=' ', file=outfile)
        if segments:
            print(segments[0][0], end=' ', file=outfile)
        if labelsegments:
            print(labelsegments[0][0], end=' ', file=outfile)


def main():
    """Segment text in some formats."""
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSAPATH',
            help="Path to directory of HFST format automata")
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
            dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
            help="print verbosely while processing")
    a.add_argument('-o', '--output', metavar="OUTFILE", 
            help="print segments into OUTFILE")
    a.add_argument('-O', '--output-format', metavar="OFORMAT", 
            help="format output suitable for OFORMAT",
            choices=["labels-tsv", "labels-moses-factors", "segments-arrows"])
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    if options.fsa:
        if options.verbose:
            print("Reading automata dir", options.fsa)
        omorfi.load_from_dir(options.fsa, segment=True, 
                labelsegment=True)
    else:
        if options.verbose:
            print("Searching for automata everywhere...")
        omorfi.load_from_dir(labelsegment=True, segment=True)
    if options.infile:
        infile = options.infile
    else:
        infile = stdin
    if options.output:
        outfile = open(options.output, 'w')
    else:
        outfile = stdout
    if options.verbose:
        print("reading from", options.infile.name)
    if options.verbose:
        print("writign to", options.output)

    linen = 0
    for line in infile:
        line = line.strip()
        linen += 1
        if options.verbose and linen % 10000 == 0:
            print(linen, '...')
        if not line or line == '':
            continue
        surfs = omorfi.tokenise(line)
        for surf in surfs:
            segments = omorfi.segment(surf)
            labelsegments = omorfi.labelsegment(surf)
            print_segments(options.output_format, segments, labelsegments, surf, outfile)
        print(file=outfile)
    exit(0)

if __name__ == "__main__":
    main()

