#!/usr/bin/env python3

from sys import stdin, stdout
from argparse import ArgumentParser
from omorfi.omorfi import Omorfi
import re

def print_segments(fmt, segments, labelsegments, surf):
    if fmt == 'labels-moses-factors':
        if labelsegments:
            # öykkärö[UPOS=VERB]i[TRAILS=→][MB=LEFT]dä[TRAILS=→Vpss][?=Tpres][?=Ppe4][?=Ncon][TRAILS=→] 
            analysis = labelsegments[0].input
            analysis = analysis.replace("{STUB}", "")
            # lets do it state-machine way
            intag = False
            stacktag = []
            currtag = ''
            currmorph = ''
            carryovertag = None
            outs = ''
            for c in analysis:
                if not intag and c != '[':
                    currmorph += c
                elif not intag and c == '[':
                    intag = True
                elif intag and c != ']':
                    currtag += c
                elif intag and c == ']':
                    if currtag.startswith('UPOS'):
                        carryovertag = currtag
                    elif currmorph != '' and carryovertag:
                        outs += currmorph + '|' +  carryovertag + ' '
                        carryovertag = None
                        currmorph = ''
                    elif currmorph != '':
                        outs += currmorph + '|' +  currtag + ' '
                        currmorph = ''
                    elif currmorph == '':
                        outs += '.' + currtag + ' '
                    currtag = ''
                    intag = False
            print(outs.replace("TRAILS=→", "",).replace("UPOS=", "").replace(" .", ".").replace("?=", "").replace("MB=LEFT", "").replace("..", ".").replace(". ", " "))
        else:
            print(surf, end='|UNK')
    elif fmt == 'both-lines':
        if segments and labelsegments:
            print(segments[0].input, labelsegments[0].input, end=' ', file=outfile)
        if segments:
            print(segments[0].input, end=' ', file=outfile)
        if labelsegments:
            print(labelsegments[0].input, end=' ', file=outfile)


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
            print_segments(options.output_format, segments, labelsegments, surf)
        print(file=outfile)
    exit(0)

if __name__ == "__main__":
    main()

