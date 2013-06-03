#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script expands Finnish TSV-formatted lexicon with a lot of data by
automatic guessing. The
"""


# Author: Tommi A Pirinen <tommi.pirinen@helsinki.fi> 2009, 2011

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
#

from sys import stderr, stdout, exit, argv
from time import strftime
import argparse

from wordmap import init_wordmap
from gradation import gradation_make_morphophonemes
from parse_csv_data import parse_defaults_from_csv, parse_extras_from_csv, parse_conts, finetune_conts, add_extras
from plurale_tantum import plurale_tantum_get_singular_stem
from stub import stub_all
from guess_feats import guess_grade_dir, guess_harmony
from guess_new_class import guess_new_class

# standard UI stuff

def main():
    # defaults
    outfiles = None
    # initialise argument parser
    ap = argparse.ArgumentParser(description="Guess more data for Finnish TSV databases")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
            default=False,
            help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
            help="print each step to stdout while processing")
    ap.add_argument("--input", "-i", action="store", required=True, type=open,
            metavar="IFILE", help="read data from IFILE")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", action="store", required=True, 
            type=argparse.FileType('w'),
            metavar="OFILE", help="write data to OFILE")
    args = ap.parse_args()
    # read from csv files
    print("# This file has been guessed using", argv[0], "from", args.input,
            "to", args.output, file=args.output)
    print("# DO NOT MODIFY manually since it will be OVERWRITTEN anyways",
            file=args.output)
    print("lemma", "new_para", "pos", "kotus_tn", "kotus_av", "plurale_tantum", 
        "stub", "twolstem", "possessive", "clitics", "is_proper",
        "proper_noun_class", "style", "stub", "gradestem", "twolstem",
        "grade_dir", "harmony", "is_suffix", "is_prefix", "stem_vowel",
        "stem_diphthong", "subcat", "sem", "particle", "#", "<- HEADERS", sep="\t", file=args.output)
    linecount = 0
    for csv_line in args.input:
        linecount += 1
        csv_line = csv_line.strip()
        if csv_line.startswith("#") or csv_line.startswith("!") or csv_line == "":
            # comment line
            csv_line = csv_file.readline()
            continue
        csv_parts = []
        if csv_line.count('\t') >= 2:
            csv_parts = csv_line.split("\t")
        elif csv_line.count(',') >= 2:
            csv_parts = csv_line.split(",")
        else:
            print("Too few commas or tabs on line", linecount, 
                "skipping following line completely:", file=stderr)
            print(csv_line, file=stderr)
            csv_line = csv_file.readline()
            continue
        if csv_parts[-1] == '<-HEADERS':
            # skip header line
            csv_line = csv_file.readline()
            continue
        # here starts the guessworks
        # the aim is to fill dict wordmap with data necessary to
        # generate a lexc line
        wordmap = init_wordmap()
        wordmap = parse_defaults_from_csv(wordmap, csv_parts)
        wordmap = parse_extras_from_csv(wordmap, csv_parts)
        # Guess works in order
        wordmap = guess_grade_dir(wordmap)
        wordmap = guess_harmony(wordmap)
        wordmap = guess_new_class(wordmap)
        # here is actual python code doing the pre-processing
        wordmap = plurale_tantum_get_singular_stem(wordmap)
        wordmap = gradation_make_morphophonemes(wordmap)
        wordmap = stub_all(wordmap)
        # suffixes can be id'd by the - in beginning
        if wordmap['lemma'].startswith('-'):
            wordmap['is_suffix'] = True
        else:
            wordmap['is_suffix'] = False
        if wordmap['lemma'].endswith('-'):
            wordmap['is_prefix'] = True
        else:
            wordmap['is_prefix'] = False
        # ...
        wordmap = add_extras(wordmap)
        # print result
        print(wordmap['lemma'], wordmap['new_para'], wordmap['pos'],
                wordmap['kotus_tn'], wordmap['kotus_av'],
                wordmap['plurale_tantum'],
                wordmap['possessive'], wordmap['clitics'], wordmap['is_proper'],
                wordmap['proper_noun_class'], wordmap['style'], wordmap['stub'],
                wordmap['gradestem'], wordmap['twolstem'], wordmap['grade_dir'],
                wordmap['harmony'], wordmap['is_suffix'], wordmap['is_prefix'],
                wordmap['stem_vowel'], wordmap['stem_diphthong'],
                wordmap['subcat'], wordmap['sem'], wordmap['particle'], 
                sep='\t', file=args.output)
    exit()


if __name__ == "__main__":
    main()

