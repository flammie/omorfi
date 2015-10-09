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

from omorfi.formatters import format_wordmap_lexc, format_multichars_lexc, \
        format_root_lexicon_lexc, format_continuation_lexc
from omorfi.lexc_formatter import format_copyright_lexc
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

    def FormatArgType(v):
        baseformats = ["omor", "apertium",
                "giella", "ftb3", "generic", "google"]
        extras = ["propers", "semantics", "ktnkav", "newparas", "taggerhacks"]
        parts = v.split('+')
        if parts[0] not in baseformats:
            raise argparse.ArgumentTypeError("Format must be one of: " + " ".join(baseformats))
        for ex in parts[1:]:
            if ex not in extras:
                raise argparse.ArgumentTypeError("Format extension must be one of: " + " ".join(extras))
        return v
    ap.add_argument("--format", "-f", action="store", default="omor",
            help="use specific output format for lexc data",
            type=FormatArgType)
    args = ap.parse_args()
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
    print(format_copyright_lexc(), file=args.output)
    if args.verbose:
        print("Creating Multichar_Symbols and Root")
    print(format_multichars_lexc(args.format), file=args.output)
    print(format_root_lexicon_lexc(args.format), file=args.output)
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
        print(format_copyright_lexc(), file=args.output)
        curr_lexicon = ""
        # for each line
        with open(tsv_filename, "r", newline='') as tsv_file:
            tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator, 
                    quoting=quoting, escapechar='%', quotechar=quotechar, strict=True)
            postponed_suffixes = list()
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
                if curr_lexicon != incoming_lexicon:
                    print("\nLEXICON", incoming_lexicon, end="\n\n",
                            file=args.output)
                    curr_lexicon = incoming_lexicon
                # switch back to real POS when possible suffix lexicon has been selected
                if wordmap['real_pos']:
                    wordmap['pos'] = wordmap['real_pos']
                # format output
                print(format_wordmap_lexc(wordmap, args.format), 
                      file=args.output)
            if len(postponed_suffixes) > 0:
                print("\nLEXICON SUFFIX\n\n", file=args.output)
            for suffix in postponed_suffixes:
                print(format_wordmap_lexc(suffix, args.format),
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
        print(format_copyright_lexc(), file=args.output)
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
                        "DIGITS", "CONJ", "SCONJ"]:
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
                print(format_continuation_lexc(tsv_parts, args.format), 
                      file=args.output)
    # print inflections
    for tsv_filename in args.inffilenames:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        print("! Omorfi inflects generated from", tsv_file.name,
                      "! date:", strftime("%Y-%m-%d %H:%M:%S+%Z"), 
                      "! params: ", ' '.join(argv), file=args.output)
        print(format_copyright_lexc(), file=args.output)
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
                print(format_continuation_lexc(tsv_parts, args.format), 
                      file=args.output)
    exit(0)


if __name__ == "__main__":
    main()

