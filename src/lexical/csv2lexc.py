#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script converts Finnish TSV-formatted lexicon to lexc format, given that
they contain at least following information for each word (i.e. at least two
fields per line):
    * the word lemma or the dictionary form
    * the word inflection classification in one of the known formats
The TSV-formatted data can be joined with arbitrary amount of extra fields to
store additional data. The additional data needs to be in name=value format.
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

from format_output import format_lexc
from parse_csv_data import parse_from_tsv

# standard UI stuff

def main():
    # defaults
    pos_files = {"ADJECTIVE": 'adjectives.lexc', 
            "NOUN": 'nouns.lexc',
            "VERB": 'verbs.lexc',
            "PROPER": 'proper-nouns.lexc',
            "ADVERB": 'adverbs.lexc',
            "PARTICLE": 'particles.lexc',
            "CONJUNCTION": 'conjunctions.lexc',
            "ADPOSITION": 'adpositions.lexc',
            "SUFFIX": 'suffixes.lexc',
            "PREFIX": 'prefixes.lexc',
            "INTERJECTION": 'interjections.lexc',
            "ABBREVIATION": 'abbreviations.lexc',
            "ACRONYM": 'acronyms.lexc',
            "PRONOUN": 'pronoubs.lexc',
            "NUMERAL": 'numerals.lexc'}
    outfiles = dict()
    curr_lexicon = dict()
    # initialise argument parser
    ap = argparse.ArgumentParser(description="Convert Finnish dictionary TSV data into xerox/HFST lexc format")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
            default=False,
            help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
            help="print each step to stdout while processing")
    ap.add_argument("--input", "-i", action="append", required=True, type=open,
            metavar="IFILE", help="read data from IFILEs")
    ap.add_argument("--exclude-pos", "-x", action="append",
            metavar="XPOS",
            help="exclude all XPOS parts of speech from generation")
    ap.add_argument("--include-lemmas", "-I", action="append", type=open,
            metavar="IFILE", help="read lemmas to include from IFILE")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", action="store", required=True, type=str,
            metavar="ODIR", help="write roots to ODIR")
    ap.add_argument("--format", "-f", action="store", default="omor",
            help="use specific output format for lexc data",
            choices=["omor", "ktnkav", "apertium", "giellatekno"])
    args = ap.parse_args()
    # check args
    lemmas = []
    if args.include_lemmas:
        for lemma_file in args.include_lemmas:
            if args.verbose:
                print("including only lemmas from", lemma_file.name);
            lemmas += lemma_file.readlines()
            lemma_file.close()
    # write headers to lexcies
    for (pos, pos_filename) in pos_files.items():
        if not pos in args.exclude_pos:
            if args.verbose: 
                print("Writing", pos, "to", args.output + "/" + pos_filename)
            outfiles[pos] = open(args.output + "/" + pos_filename, "w")
            
            print("! Omorfi stubs", pos, "generated from", args.input,
                    file=outfiles[pos])
            print("! date:", strftime("%Y-%m-%d %H:%M:%S+%Z"), 
                file=outfiles[pos])
            print("! params: ", ' '.join(argv), file=outfiles[pos])
            curr_lexicon[pos] = ""
    if args.exclude_pos:
        if args.verbose:
            print("Not writing closed parts-of-speech data in", 
                    ",".join(args.exclude_pos))
    # read from csv files
    for csv_file in args.input:
        if args.verbose:
            print("Reading from", csv_file.name)
        csv_line = csv_file.readline()
        linecount = 0
        lexicon_count = 0
        entry_count = 0
        for (pos, pos_filename) in pos_files.items():
            if not pos in args.exclude_pos:
                print("! Entries from ", csv_file.name, file=outfiles[pos])
                print("LEXICON ", pos, file=outfiles[pos])
        # for each line
        while csv_line:
            linecount += 1
            csv_line = csv_line.strip()
            if csv_line.startswith("#") or csv_line.startswith("!") or csv_line == "":
                # comment line
                csv_line = csv_file.readline()
                continue
            csv_parts = []
            if csv_line.count('\t') >= 18:
                csv_parts = csv_line.split("\t")
            else:
                print("Too few tabs on line", linecount, 
                    "skipping following line completely:", file=stderr)
                print(csv_line, file=stderr)
                csv_line = csv_file.readline()
                continue
            if csv_parts[-1] == '<- HEADERS':
                # skip header line
                csv_line = csv_file.readline()
                continue
            # here starts the guessworks
            # the aim is to fill dict wordmap with data necessary to
            # generate a lexc line
            wordmap = dict()
            wordmap = parse_from_tsv(wordmap, csv_parts)
            if args.exclude_pos:
                if wordmap['pos'] in args.exclude_pos:
                    csv_line = csv_file.readline()
                    continue
            if args.include_lemmas:
                if wordmap['lemma'] not in lemmas:
                    csv_line = csv_file.readline()
                    continue
            # format output
            print(format_lexc(wordmap, args.format), 
                  file=outfiles[wordmap['pos']])
            csv_line = csv_file.readline()
    exit()


if __name__ == "__main__":
    main()

