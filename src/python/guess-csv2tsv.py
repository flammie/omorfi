#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Converts Omorfi's lexeme & attribute file data from old kotus-csv format to newpara-tsv.
New paradigms are simply guessed here; possible checks against existing
lexical data should be done separately.
"""

# Authors: Juha Kuokkala, Tommi A. Pirinen  2014

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
import csv
from collections import defaultdict

from omorfi.wordmap import init_wordmap, get_wordmap_fieldnames
from omorfi.guess_new_class import guess_new_class
from omorfi.guess_feats import guess_grade_dir_from_ktn, guess_harmony, guess_stem_features_ktn, guess_pronunciation


def expand_pos(wordmap):
    if wordmap['pos'] == 'A':
        wordmap['pos'] = 'ADJECTIVE'
    elif wordmap['pos'] == 'N':
        wordmap['pos'] = 'NOUN'
    elif wordmap['pos'] == 'V':
        wordmap['pos'] = 'VERB'
    elif wordmap['pos'] == 'P':
        wordmap['pos'] = 'PARTICLE'
    elif wordmap['pos'] == 'Prop':
        wordmap['pos'] = 'NOUN'
        wordmap['is_proper'] = True
    elif wordmap['pos'] == 'Adv':
        wordmap['pos'] = 'ADVERB'
    elif wordmap['pos'] == 'Adp':
        wordmap['pos'] = 'ADPOSITION'
    elif wordmap['pos'] == 'Intj':
        wordmap['pos'] = 'INTERJECTION'
    elif wordmap['pos'] == 'Conj':
        wordmap['pos'] = 'CONJUNCTION'
    elif wordmap['pos'] == 'Pre':
        wordmap['pos'] = 'NOUN'
        wordmap['is_prefix'] = True
    elif wordmap['pos'] == 'Abbr':
        wordmap['pos'] = 'ABBREVIATION'
    elif wordmap['pos'] == 'Acro':
        wordmap['pos'] = 'ACRONYM'
    elif wordmap['pos'] == 'Num':
        wordmap['pos'] = 'NUMERAL'
    elif wordmap['pos'] == 'Pron':
        wordmap['pos'] = 'PRONOUN'
    else:
        print("Unrecognised POS", wordmap['pos'], file=stderr)
    return wordmap


def main():
    ap = argparse.ArgumentParser(description="Converts Omorfi's lexical data from old kotus-csv format to newpara-tsv "
                                 "with possible attribute fields")

    ap.add_argument("--input", "-i", metavar="INFILE",
                    help="read data from INFILE")
    ap.add_argument('--output', '-o', metavar="OUTFILE",
                    help="write converted stuff to OUTFILE")
    ap.add_argument('--plt-file', '-p', metavar="PLTFILE",
                    help="read plurale tantum info (csv) from PLTFILE")
    ap.add_argument('--verbose', '-v', action="store_true",
                    help="Print verbosely while processing")
    ap.add_argument("--version", "-V", action="version")
    args = ap.parse_args()

    plt_info = defaultdict(lambda: False)
    if args.plt_file:
        if args.verbose:
            print("Reading plurale tantum data from",
                  args.plt_file, file=stderr)
        with open(args.plt_file, 'r', newline='') as plt_in:
            headers_skipped = False
            for line in plt_in:
                if headers_skipped:
                    lex, plt = line.rsplit(',', 1)
                    plt_info[lex] = plt.strip('"')
                elif line.find('HEADERS') >= 0:
                    headers_skipped = True

    if args.input:
        input = open(args.input, 'r', newline='')
    else:
        input = stdin
    if args.output:
        output = open(args.output, 'w', newline='')
    else:
        output = stdout

    for line in input:
        if line.startswith('#') or line.find('<-HEADERS') >= 0:
            continue
        fields = line.strip('"\n').split('","')
        if len(fields) < 4:
            if len(fields) > 0:
                if args.verbose:
                    print("Skipping too short line:", line, file=stderr)
            continue
        wordmap = init_wordmap()
        wordmap['stub'] = wordmap['lemma'] = fields[0]
        if args.verbose:
            print(wordmap['lemma'])
        wordmap['kotus_tn'] = int(fields[1])
        wordmap['kotus_av'] = fields[2]
        if wordmap['kotus_av'] == '0':
            wordmap['kotus_av'] = False
        wordmap['pos'] = fields[3]
        wordmap = expand_pos(wordmap)
        if plt_info:
            wordmap['plurale_tantum'] = plt_info[
                '"' + '","'.join(fields[0:4]) + '"']
        for i in range(4, len(fields)):
            if fields[i].startswith('plt='):
                wordmap['plurale_tantum'] = fields[i]
            elif fields[i].startswith('boundaries='):
                fields[i] = fields[i].replace('|', '{WB}')
                wordmap['stub'] = wordmap['boundaries'] = fields[i]
        wordmap = guess_stem_features_ktn(wordmap)
        wordmap = guess_pronunciation(wordmap)
        wordmap = guess_grade_dir_from_ktn(wordmap)
        wordmap = guess_harmony(wordmap)
        wordmap = guess_new_class(wordmap)

        wordmap['extras'] = '\t'.join(fields[4:])
        if wordmap['extras']:
            wordmap['extras'] = '\t' + wordmap['extras']

        if args.verbose:
            print("Guessed new para: %(new_para)r" % (wordmap))
        print("%(lemma)s\t%(new_para)r%(extras)s" % (wordmap), file=output)

    input.close()
    output.close()
    exit()


if __name__ == "__main__":
    main()
