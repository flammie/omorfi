#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convert between file and tagging formats."""
# string munging
from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stdin, stdout, stderr

# omorfi
from omorfi.formats.fileformats import (next_vislcg, next_conllu,
                                        next_plaintext, next_omorfi)


def main():
    """Command-line interface to omorfi conversions."""
    a = ArgumentParser()
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    a.add_argument('-o', '--output', metavar="OUTFILE", dest="outfile",
                   help="print output into OUTFILE", type=FileType('w'))
    a.add_argument('-I', '--informat', metavar="INFORMAT", required=True,
                   help="read input using INFORMAT tokenisation",
                   choices=['tokens', 'vislcg', 'conllu', 'omorfi'])
    a.add_argument('-O', '--outformat', metavar='OUTFORMAT', default="omorfi",
                   choices=['omorfi', 'json', 'vislcg', 'conllu'])
    options = a.parse_args()
    if not options.infile:
        options.infile = stdin
    if options.verbose:
        print("reading", options.infile.name)
    if not options.outfile:
        options.outfile = stdout
    if options.verbose:
        print("converting to", options.outfile.name)
    eoffed = False
    while not eoffed:
        if options.informat == 'vislcg':
            tokens = next_vislcg(options.infile, False)
        elif options.informat == 'tokens':
            tokens = next_plaintext(options.infile)
        elif options.informat == 'conllu':
            tokens = next_conllu(options.infile)
        elif options.informat == 'omorfi':
            tokens = next_omorfi(options.infile)
        else:
            print("input format missing implementation", options.informat,
                  file=stderr)
            exit(2)
        if not tokens:
            eoffed = True
            break
        for token in tokens:
            if token.nontoken == 'eof':
                eoffed = True
                break
            if options.outformat == 'vislcg':
                print(token.printable_vislcg(), file=options.outfile)
            elif options.outformat == 'conllu':
                print(token.printable_conllu(), file=options.outfile)
            elif options.outformat == 'omorfi':
                print(token, file=options.outfile)
            else:
                print("Format implementation misisng", options.outformat,
                      file=stderr)
                exit(1)
    exit(0)


if __name__ == "__main__":
    main()
