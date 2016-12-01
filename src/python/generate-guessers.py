#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script generates Finnish omorfi morphotactics into a lexc format guesser.
It is assumed that the database contains at least following information for each
paradigm:
    * the word lemma pattern as regular expression
    * the word stub deletion as fixed string matching the regex's suffix
"""


# Author: Omorfi contributors, 2016

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

import argparse
import csv
from sys import argv, exit, stderr
from time import strftime

from omorfi.apertium_formatter import ApertiumFormatter
from omorfi.ftb3_formatter import Ftb3Formatter
from omorfi.giella_formatter import GiellaFormatter
from omorfi.labeled_segments_formatter import LabeledSegmentsFormatter
from omorfi.no_tags_formatter import NoTagsFormatter
from omorfi.omor_formatter import OmorFormatter


# standard UI stuff


def main():
    # defaults
    curr_lexicon = dict()
    # initialise argument parser
    ap = argparse.ArgumentParser(
        description="Convert Finnish dictionary TSV data into xerox/HFST lexc format")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--stemparts", "-p", action="append", required=True,
                    dest='spfilenames',
                    metavar="SPFILE", help="read lexical roots from SPFILEs")
    ap.add_argument("--inflection", "-i", action="append", required=True,
                    dest='inffilenames',
                    metavar="INFFILE", help="read inflection from INFFILEs")
    ap.add_argument("--suffix-regexes", "-r", action="append", required=True,
                    dest='refilenames',
                    metavar="REFILE", help="read suffix regexes from REFILEs")
    ap.add_argument("--stub-deletions", "-d", action="append", required=True,
                    dest='sdfilenames',
                    metavar="SDFILE", help="read stub deletions from SDFILEs")
    ap.add_argument("--exclude-pos", "-x", action="append",
                    metavar="XPOS",
                    help="exclude all XPOS parts of speech from generation")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", "--one-file", "-1",
                    type=argparse.FileType("w"), required=True,
                    metavar="OFILE", help="write output to OFILE")
    ap.add_argument("--fields", "-F", action="store", default=1,
                    metavar="N", help="require N fields for tables")
    ap.add_argument("--separator", action="store", default="\t",
                    metavar="SEP", help="use SEP as separator")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
                    metavar="COMMENT", help="skip lines starting with COMMENT that"
                    "do not have SEPs")
    ap.add_argument("--strip", action="store",
                    metavar="STRIP", help="strip STRIP from fields before using")
    ap.add_argument("--format", "-f", action="store", default="omor",
                    help="use specific output format for lexc data",
                    choices=["omor", "giella", "ftb3", "ftb1", "none", "apertium",
                             "labelsegments"])
    args = ap.parse_args()

    formatter = None
    if args.format == 'omor':
        formatter = OmorFormatter(args.verbose, new_para=False,
                allo=False, props=False, sem=False)
    elif args.format == 'ftb3':
        formatter = Ftb3Formatter(args.verbose)
    elif args.format == 'apertium':
        formatter = ApertiumFormatter(args.verbose)
    elif args.format == 'giella':
        formatter = GiellaFormatter(args.verbose)
    elif args.format == 'none':
        formatter = NoTagsFormatter(args.verbose,
                                    lemmatise=args.none_lemmas, segment=args.none_segments)
    elif args.format == 'labelsegments':
        formatter = LabeledSegmentsFormatter(args.verbose)
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
    # print stem parts
    for tsv_filename in args.refilenames:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        print("! Omorfi guessers generated from", tsv_filename,
              "! date:", strftime("%Y-%m-%d %H:%M:%S+%Z"),
              "! params: ", ' '.join(argv), file=args.output)
        print(formatter.copyright_lexc(), file=args.output)
        curr_lexicon = ""
        print("LEXICON GUESSERS", file=args.output)
        with open(tsv_filename, 'r', newline='') as tsv_file:
            tsv_reader = csv.reader(tsv_file, delimiter=args.separator,
                                    strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 1:
                    print(tsv_filename, linecount,
                          "Too few tabs on line",
                          "skipping following fields:",
                          tsv_parts, file=stderr)
                    continue
                pos = tsv_parts[0].split("_")[0]
                if pos not in ["ADJ", "NOUN", "VERB", "PROPN", "NUM",
                               "PRON", "ADP", "ADV", "SYM", "PUNCT", "INTJ", "X",
                               "DIGITS", "CONJ", "SCONJ", "AUX", "DET"]:
                    print("Cannot deduce pos from incoming cont:",
                          tsv_parts[0], "Skipping")
                    continue
                # format output
                if len(tsv_parts) == 2:
                    print(formatter.guesser2lexc(
                        tsv_parts[1], tsv_parts[0]),
                        file=args.output)
                else:
                    print(formatter.guesser2lexc(
                        None, tsv_parts[0]),
                        file=args.output)
    # FOLLOWING IS SHARED WITH generate-lexcies
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
                if pos not in ["ADJ", "NOUN", "VERB", "PROPN", "NUM",
                               "PRON", "ADP", "ADV", "SYM", "PUNCT", "INTJ",
                               "X", "DIGITS", "CONJ", "SCONJ"]:
                    print("Cannot deduce pos from incoming cont:",
                          tsv_parts[0], "Skipping")
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
