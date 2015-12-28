#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script generates Finnish omorfi database to lexc format, given that
they contain at least following information for each word:
    * the word lemma or the dictionary form
    * the word inflection classification in one of the known format.
Additional data may be available in the database and can be deduced from the
lemma or classification as needed. The current database reader is based
on the python's csv module, but may change in the future.
"""


# Author: Omorfi contributors, 2014 

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

from ast import literal_eval
from sys import stderr, stdout, exit, argv
from time import strftime
import argparse
import csv

from omorfi.omor_formatter import OmorFormatter
from omorfi.ftb3_formatter import Ftb3Formatter
from omorfi.apertium_formatter import ApertiumFormatter

from omorfi.parse_csv_data import parse_defaults_from_tsv

# standard UI stuff

def main():
    # defaults
    stubfiles = dict()
    stempartfiles = dict()
    inflectfiles = dict()
    curr_lexicon = dict()
    # initialise argument parser
    ap = argparse.ArgumentParser(description="Convert Finnish dictionary TSV data into xerox/HFST lexc format")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
            default=False,
            help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
            help="print each step to stdout while processing")
    ap.add_argument("--master", "-m", action="append", required=True,
            dest="masterfilenames",
            metavar="MFILE", help="read lexical roots from MFILEs")
    ap.add_argument("--stemparts", "-p", action="append", required=True,
            dest='spfilenames',
            metavar="SPFILE", help="read lexical roots from SPFILEs")
    ap.add_argument("--inflection", "-i", action="append", required=True,
            dest='inffilenames',
            metavar="INFFILE", help="read inflection from INFFILEs")
    ap.add_argument("--exclude-pos", "-x", action="append",
            metavar="XPOS",
            help="exclude all XPOS parts of speech from generation")
    ap.add_argument("--include-lemmas", "-I", action="append", type=open,
            metavar="ILFILE", help="read lemmas to include from ILFILE")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", "--one-file", "-1",
            type=argparse.FileType("w"), required=True,
            metavar="OFILE", help="write output to OFILE")
    ap.add_argument("--fields", "-F", action="store", default=2,
            metavar="N", help="read N fields from master")
    ap.add_argument("--separator", action="store", default="\t",
            metavar="SEP", help="use SEP as separator")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
            metavar="COMMENT", help="skip lines starting with COMMENT that"
                "do not have SEPs")
    ap.add_argument("--strip", action="store",
            metavar="STRIP", help="strip STRIP from fields before using")
    ap.add_argument("--format", "-f", action="store", default="omor",
            help="use specific output format for lexc data",
            choices=["omor", "giella", "ftb3", "ftb1", "generic", "apertium"])
    ap.add_argument("--omor-new-para", action="store_true", default=False,
            help="include NEW_PARA= in raw analyses")
    ap.add_argument("--omor-allo", action="store_true", default=False,
            help="include ALLO= in raw analyses")
    ap.add_argument("--omor-props", action="store_true", default=False,
            help="include PROPER= in raw analyses")
    ap.add_argument("--omor-sem", action="store_true", default=False,
            help="include SEM= in raw analyses")
    args = ap.parse_args()

    formatter = None
    if args.format == 'omor':
        formatter = OmorFormatter(args.verbose, new_para=args.omor_new_para,
                allo=args.omor_allo, props=args.omor_props, sem=args.omor_sem)
    elif args.format == 'ftb3':
        formatter = Ftb3Formatter(args.verbose)
    elif args.format == 'apertium':
        formatter = ApertiumFormatter(args.verbose)
    else:
        print("DIDNT CONVERT FORMATTER YET", args.format)
        exit(1)
    # check args
    if args.strip == '"' or args.strip == "'":
        quoting = csv.QUOTE_ALL
        quotechar = args.strip
    else:
        quoting = csv.QUOTE_NONE
        quotechar = None
    lemmas = []
    if args.include_lemmas:
        for lemma_file in args.include_lemmas:
            if args.verbose:
                print("including only lemmas from", lemma_file.name);
            for line in lemma_file:
                lemmas.append(line.rstrip('\n'))
            lemma_file.close()
    if not args.exclude_pos:
        args.exclude_pos = []
    # setup files
    if args.verbose: 
        print("Writing everything to", args.output.name)
        if args.exclude_pos:
            print("Not writing closed parts-of-speech data in", 
                    ",".join(args.exclude_pos))
    # print definitions to rootfile
    print(formatter.copyright_lexc(), file=args.output)
    if args.verbose:
        print("Creating Multichar_Symbols and Root")
    print(formatter.multichars_lexc(), file=args.output)
    print(formatter.root_lexicon_lexc(), file=args.output)
    # read from csv files
    for tsv_filename in args.masterfilenames:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        lexicon_count = 0
        entry_count = 0
        print("! Omorfi stubs generated from", tsv_filename,
              "\n! date:", strftime("%Y-%m-%d %H:%M:%S+%Z"), 
              "\n! params: ", ' '.join(argv), file=args.output)
        print(formatter.copyright_lexc(), file=args.output)
        curr_lexicon = ""
        # for each line
        with open(tsv_filename, "r", newline='') as tsv_file:
            tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator, 
                    quoting=quoting, escapechar='%', quotechar=quotechar, strict=True)
            postponed_suffixes = list()
            postponed_abbrs = {'ABBREVIATION': list(), 'ACRONYM': list()}
            for tsv_parts in tsv_reader:
                linecount += 1
                if args.verbose and (linecount % 10000 == 0):
                    print(linecount, "...", sep='', end='\r')
                if len(tsv_parts) < 18:
                    print("Too few tabs on line", linecount, 
                        "skipping following line completely:", file=stderr)
                    print(tsv_parts, file=stderr)
                    continue
                # read data from database
                wordmap = tsv_parts
                # exclusions
                if args.exclude_pos:
                    if wordmap['pos'] in args.exclude_pos:
                        continue
                if args.include_lemmas:
                    if wordmap['lemma'] not in lemmas:
                        continue
                # choose correct lexicon
                incoming_lexicon = tsv_parts['upos']
                if tsv_parts['is_suffix']:
                    postponed_suffixes.append(tsv_parts)
                    continue
                elif tsv_parts['abbr']:
                    postponed_abbrs[tsv_parts['abbr']].append(tsv_parts)
                    continue
                if curr_lexicon != incoming_lexicon:
                    print("\nLEXICON", incoming_lexicon, end="\n\n",
                            file=args.output)
                    curr_lexicon = incoming_lexicon
                # switch back to real POS when possible suffix lexicon has been selected
                if wordmap['real_pos']:
                    wordmap['pos'] = wordmap['real_pos']
                # format output
                print(formatter.wordmap2lexc(wordmap), 
                      file=args.output)
            if len(postponed_suffixes) > 0:
                print("\nLEXICON SUFFIX\n\n", file=args.output)
                for suffix in postponed_suffixes:
                    print(formatter.wordmap2lexc(suffix),
                            file=args.output)
            for key, words in postponed_abbrs.items():
                print("\nLEXICON", key, "\n\n", file=args.output)
                for word in words:
                    print(formatter.wordmap2lexc(word),
                            file=args.output)
        if args.verbose:
            print("\n", linecount, " entries in master db")
    # print stem parts
    for tsv_filename in args.spfilenames:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        print("! Omorfi stemparts generated from", tsv_file.name,
                      "! date:", strftime("%Y-%m-%d %H:%M:%S+%Z"), 
                      "! params: ", ' '.join(argv), file=args.output)
        print(formatter.copyright_lexc(), file=args.output)
        curr_lexicon = ""
        with open(tsv_filename, 'r', newline='') as tsv_file:
            tsv_reader = csv.reader(tsv_file, delimiter=args.separator,
                    strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 3:
                    print(tsv_filename, linecount, 
                            "Too few tabs on line",
                            "skipping following fields:",
                            tsv_parts, file=stderr)
                    continue
                pos = tsv_parts[0].split("_")[0]
                if not pos in ["ADJ", "NOUN", "VERB", "PROPN", "NUM",
                        "PRON", "ADP", "ADV", "SYM", "PUNCT", "INTJ", "X",
                        "DIGITS", "CONJ", "SCONJ", "AUX", "DET"]:
                    print("Cannot deduce pos from incoming cont:", 
                            tsv_parts[0], "Skipping")
                    continue
                if pos in args.exclude_pos:
                    continue
                # format output
                if curr_lexicon != tsv_parts[0]:
                    print("\nLEXICON", tsv_parts[0], end="\n\n",
                            file=args.output)
                    curr_lexicon = tsv_parts[0]
                for cont in tsv_parts[3:]:
                    print(formatter.continuation2lexc(
                        tsv_parts[1], tsv_parts[2], cont), 
                        file=args.output)
    # print inflections
    for tsv_filename in args.inffilenames:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        print("! Omorfi inflects generated from", tsv_file.name,
                      "! date:", strftime("%Y-%m-%d %H:%M:%S+%Z"), 
                      "! params: ", ' '.join(argv), file=args.output)
        print(formatter.copyright_lexc(), file=args.output)
        curr_lexicon = ""
        # for each line
        with open(tsv_filename, 'r', newline='') as tsv_file:
            tsv_reader = csv.reader(tsv_file, delimiter=args.separator,
                    strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 3:
                    print(tsv_filename, linecount,
                            "Too few tabs on line", 
                            "skipping following fields:", tsv_parts,
                            file=stderr)
                    continue
                pos = tsv_parts[0].split("_")[0]
                if not pos in ["ADJ", "NOUN", "VERB", "PROPN", "NUM",
                        "PRON", "ADP", "ADV", "SYM", "PUNCT", "INTJ",
                        "X", "DIGITS", "CONJ", "SCONJ"]:
                    print("Cannot deduce pos from incoming cont:", 
                            tsv_parts[0], "Skipping")
                    continue
                if pos in args.exclude_pos:
                    continue
                # format output
                if curr_lexicon != tsv_parts[0]:
                    print("\nLEXICON", tsv_parts[0], end="\n\n",
                            file=args.output)
                    curr_lexicon = tsv_parts[0]
                for cont in tsv_parts[3:]:
                    print(formatter.continuation2lexc(
                        tsv_parts[1], tsv_parts[2], cont), 
                        file=args.output)
    exit(0)


if __name__ == "__main__":
    main()

