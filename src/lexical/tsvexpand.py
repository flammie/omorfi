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
import csv

from wordmap import init_wordmap, get_wordmap_fieldnames
from gradation import gradation_make_morphophonemes
from parse_csv_data import parse_defaults_from_csv, parse_extras_from_csv, parse_conts, finetune_conts, add_extras
from plurale_tantum import plurale_tantum_get_singular_stem
from stub import stub_all
from guess_feats import guess_grade_dir, guess_harmony, guess_stem_features_ktn, guess_pronunciation
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
    ap.add_argument("--input", "-i", action="store", required=True,
            dest='inputfilename',
            metavar="IFILE", help="read data from IFILE")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", action="store", required=True, 
            dest='outputfilename',
            metavar="OFILE", help="write data to OFILE")
    ap.add_argument("--fields", "-f", action="store", default=2,
            metavar="N", help="read N fields from master")
    ap.add_argument("--separator", "-s", action="store", default="\t",
            metavar="SEP", help="use SEP as separator")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
            metavar="COMMENT", help="skip lines starting with COMMENT that"
                "do not have SEPs")
    ap.add_argument("--strip", "-S", action="store",
            metavar="STRIP", help="strip STRIP from fields before using")

    args = ap.parse_args()

    output = open(outputfilename, 'w', newline='')

    # header comments
    print("# This file has been guessed using", argv[0], "from", args.inputname,
            "to", args.outputname, file=output)
    print("# DO NOT MODIFY manually since it will be OVERWRITTEN anyways",
            file=output)
    fieldnames = get_wordmap_fieldnames()
    tsv_writer = csv.DictWriter(output, fieldnames, restval='None', 
            delimeter=args.separator)
    tsv_writer.writeheader()
    # read from csv files
    linecount = 0
    with open(args.inputfilename, 'r', newline='') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter=args.separator,
                strict=True)
        for tsv_parts in tsv_reader:
            linecount += 1
            if len(tsv_parts) < 2:
                print("Too few commas or tabs on line", linecount, 
                    "skipping following line completely:", file=stderr)
                print(tsv_parts, file=stderr)
                continue
            if tsv_parts[-1] == '<-HEADERS':
                # skip header line
                continue
            # here starts the guessworks
            # the aim is to fill dict wordmap with data necessary to
            # generate a lexc line
            wordmap = init_wordmap()
            wordmap = parse_defaults_from_tsv(wordmap, tsv_parts)
            wordmap = parse_extras_from_tsv(wordmap, tsv_parts)
            # Guess works in order
            wordmap = guess_pos_from_newpara(wordmap)
            wordmap = guess_ktn_from_newpara(wordmap)
            wordmap = guess_stem_features_ktn(wordmap)
            wordmap = guess_pronunciation(wordmap)
            wordmap = guess_grade_dir_from_ktn(wordmap)
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
            tsv_writer.writerow(wordmap)
            print(wordmap['lemma'], wordmap['new_paras'], wordmap['pos'],
                    wordmap['kotus_tn'], wordmap['kotus_av'],
                    wordmap['plurale_tantum'],
                    wordmap['possessive'], wordmap['clitics'], wordmap['is_proper'],
                    wordmap['proper_noun_class'], wordmap['style'], wordmap['stub'],
                    wordmap['gradestem'], wordmap['twolstem'], wordmap['grade_dir'],
                    wordmap['harmony'], wordmap['is_suffix'], wordmap['is_prefix'],
                    wordmap['stem_vowel'], wordmap['stem_diphthong'],
                    wordmap['subcat'], wordmap['sem'], wordmap['particle'],
                    wordmap['boundaries'], wordmap['bracketstub'],
                    wordmap['origin'],
                    sep='\t', file=args.output)
    exit()


if __name__ == "__main__":
    main()

