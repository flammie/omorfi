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

from wordmap import init_wordmap
from guess_new_class import guess_new_class
from guess_feats import guess_harmony, guess_pronunciation

def main():
    ap = argparse.ArgumentParser(description=
            "Helper script to guess missing data for new word entry")

    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--lemma", "-l", required=True,
            metavar="LEMMA", help="guess attributes for LEMMA")
    ap.add_argument("--pos", "-p", metavar="POS",
            help="use POS as hint for guesssing")
    ap.add_argument("--ktn", "-k", metavar="KTN",
            help="Use KTN as hint for guessing")
    ap.add_argument("--kav", "-a", metavar="KAV",
            help="Use KAV as hint for guessing")
    ap.add_argument('--newpara', '-n', metavar='NEWPARA',
            help="Use NEWPARA as hint for guessing")
    ap.add_argument('--output', '-o', metavar="OUTFILE",
            help="Append guessed stuff to OUTFILE")
    ap.add_argument('--verbose', '-v', action="store_true",
            help="Print verbosely while processing")
    args = ap.parse_args()
   
    if args.verbose:
        print("Initialising wordmap from args...")
    word = init_wordmap()
    word['lemma'] = args.lemma
    word['stub'] = args.lemma
    if args.verbose:
        print(word['lemma'])
    
    if args.pos:
        word['pos'] = args.pos
        if args.verbose:
            print(word['pos'])
    if args.ktn:
        word['kotus_tn'] = int(args.ktn)
        if args.verbose:
            print(word['kotus_tn'])
        if args.kav != '0':
            word['kotus_av'] = args.kav
        elif args.kav == '0':
            word['kotus_av'] = False
        else:
            word['kotus_av'] = False
        if args.verbose:
            print(word['kotus_av'])
    
    # this we can guess
    if args.verbose:
        print("Guessing pronunciation from lemma", word['lemma'], "...")
    word = guess_pronunciation(word)
    if args.verbose:
        print("Resolved to", word['pronunciation'])
        print("Guessing harmony from that...")
    word = guess_harmony(word)
    if args.verbose:
        print("Resolved to", word['harmony'])
    if not word['pos']:
        if args.verbose:
            print("Guessing pos from ktn...")
        if int(args.ktn) < 52:
            word['pos'] = 'NOUN'
        elif int(args.ktn) < 79:
            word['pos'] = 'VERB'
        else:
            word['pos'] = 'PARTICLE'
    else:
        if args.verbose:
            print("Guessing pos from lemma...")
        if word['lemma'].endswith('aa') or word['lemma'].endswith('ää'):
            word['pos'] = 'VERB'
        elif word['lemma'].endswith('sti'):
            word['pos'] = 'PARTICLE'
        else:
            word['pos'] = 'NOUN'
    if not word['new_paras']:
        if args.verbose:
            print("Guessing new para from ktn...")
        word = guess_new_class(word)

    if not args.output:
        if args.verbose:
            print("Following is for lexemes.tsv:")
        print("%(lemma)s\t%(new_paras)r" % (word))
    else:
        with open(args.output, 'a') as output:
            print("%(lemma)s\t%(new_paras)r" % (word), file=output)

    
    exit()


if __name__ == "__main__":
    main()

