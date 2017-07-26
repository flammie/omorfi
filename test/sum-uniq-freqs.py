#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classify coveragelogs fast, based on black and white lists.
"""


from argparse import ArgumentParser


def main():
    a = ArgumentParser()
    a.add_argument('-o', '--output', required=True, dest="outfile",
                   metavar="OUTFILE",
                   help="Write combined frequencies to OUTFILE")
    a.add_argument('-t', '--threshold', required=True, type=int,
                   metavar="THOLD",
                   help="Write only tokens with freq >= THOLD")
    a.add_argument('inputs', metavar='INFILE', type=open, nargs='+',
                   help='add frequencies from INFILE')
    options = a.parse_args()
    outfile = open(options.outfile, 'w')
    #
    freqs = dict()
    for infile in options.inputs:
        for inline in infile:
            infields = inline.strip().split(' ')
            if len(infields) < 2:
                print("Not a valid coverage log line", inline.strip())
                continue
            infreq = int(infields[0])
            intoken = infields[1]
            if intoken in freqs:
                freqs[intoken] += infreq
            else:
                freqs[intoken] = infreq
    for token, freq in sorted(freqs.items(), key=lambda x: int(x[1]), reverse=True):
        if int(freq) >= options.threshold:
            print(freq, token, sep='\t', file=outfile)
    exit(0)


if __name__ == "__main__":
    main()
