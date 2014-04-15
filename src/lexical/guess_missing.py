#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Example script for simple interface for adding new words to omorfi
"""

# Author: Tommi A. Pirinen <tommi.pirinen@helsinki.fi> 2014

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from sys import stdin, stdout, stderr, exit, argv
import argparse
import locale
import readline
import re

from wordmap import init_wordmap
from guess_new_class import guess_new_class
from guess_feats import guess_harmony, guess_pronunciation

def main():
    ap = argparse.ArgumentParser(description=
            "Helper script to guess missing data for new word entry")

    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--lemma", "-l", required=False,
            metavar="LEMMA", help="guess attributes for LEMMA")
    ap.add_argument("--pos", "-p", metavar="POS",
            help="use POS as hint for guesssing")
    ap.add_argument("--ktn", "-k", metavar="KTN",
            help="Use KTN as hint for guessing")
    ap.add_argument("--kav", "-a", metavar="KAV",
            help="Use KAV as hint for guessing")
    ap.add_argument('--newpara', '-n', metavar='NEWPARA',
            help="Use NEWPARA as hint for guessing")
    ap.add_argument("--plt", "-t", action="store_true",
            help="Plurale tantum (plt) word")
    ap.add_argument('--input', '-i', metavar="INFILE",
            help="Read (multiple) lemma and paradigm values from INFILE (space separated: LEMMA (NEWPARA | KTN(-KAV)) )")
    ap.add_argument('--output', '-o', metavar="OUTFILE",
            help="Append guessed stuff to OUTFILE")
    ap.add_argument('--verbose', '-v', action="store_true",
            help="Print verbosely while processing")
    args = ap.parse_args()
   
    if not args.lemma and not args.input:
        print(argv[0], ': error: argument --lemma/-l or --input/-i is required', file=stderr)
        exit(1)
    
    if args.input:
        input = open(args.input, 'r', newline='')
        if args.verbose:
            print('Reading lexical data from', args.input, file=stderr)
        for line in input:
            fields = line.strip('\n').split()
            if len(fields) > 1:
                para = fields[1]
                if re.match(r'[A-Z]+_', para):
                    args.newpara = para
                    args.ktn = None
                    args.kav = None
                elif re.match(r'[0-9]+-[A-Z0]$', para):
                    args.newpara = None
                    args.ktn, args.kav = para.split('-')
                elif re.match(r'[0-9]+$', para):
                    args.newpara = None
                    args.ktn = para
                    args.kav = None
                else:
                    print('Invalid paradigm:', para, ', skipping', args.lemma, file=stderr)
                    continue
            if len(fields) > 0:
                args.lemma = fields[0]
                do_guessing(args)
    else:
        do_guessing(args)
    
    exit()

    
def do_guessing(args):

    if args.verbose:
        print("Initialising wordmap from args...", file=stderr)
    word = init_wordmap()
    word['lemma'] = args.lemma
    word['stub'] = args.lemma
    if args.verbose:
        print(word['lemma'], file=stderr)
    
    if args.pos:
        word['pos'] = args.pos
        if args.verbose:
            print(word['pos'], file=stderr)
    if args.ktn:
        word['kotus_tn'] = int(args.ktn)
        if args.verbose:
            print(word['kotus_tn'], file=stderr)
        if args.kav != '0':
            word['kotus_av'] = args.kav
        elif args.kav == '0':
            word['kotus_av'] = False
        else:
            word['kotus_av'] = False
        if args.verbose:
            print(word['kotus_av'], file=stderr)
    if args.newpara:
        word['new_paras'].append(args.newpara)
        if args.verbose:
            print(word['new_paras'], file=stderr)
    if args.plt:
        word['plurale_tantum'] = True
        if args.verbose:
            print('plurale_tantum = True', file=stderr)
    
    # this we can guess
    if args.verbose:
        print("Guessing pronunciation from lemma", word['lemma'], "...", file=stderr)
    word = guess_pronunciation(word)
    if args.verbose:
        print("Resolved to", word['pronunciation'], file=stderr)
        print("Guessing harmony from that...", file=stderr)
    word = guess_harmony(word)
    if args.verbose:
        print("Resolved to", word['harmony'], file=stderr)
    if not word['pos']:
        if word['kotus_tn']:
            if args.verbose:
                print("Guessing pos from ktn...", file=stderr)
            if word['kotus_tn'] < 52:
                word['pos'] = 'NOUN'
            elif word['kotus_tn'] < 79:
                word['pos'] = 'VERB'
            else:
                word['pos'] = 'PARTICLE'
        else:
            if args.verbose:
                print("Guessing pos from lemma...", file=stderr)
            if word['lemma'].endswith('aa') or word['lemma'].endswith('ää'):
                word['pos'] = 'VERB'
            elif word['lemma'].endswith('sti'):
                word['pos'] = 'PARTICLE'
            else:
                word['pos'] = 'NOUN'
    if not word['new_paras']:
        if args.verbose:
            print("Guessing new para from ktn...", file=stderr)
        word = guess_new_class(word)

    if not args.output:
        if args.verbose:
            print("Following is for lexemes.tsv:")
        print("%(lemma)s\t%(new_paras)r" % (word))
    else:
        with open(args.output, 'a') as output:
            print("%(lemma)s\t%(new_paras)r" % (word), file=output)



if __name__ == "__main__":
    main()

