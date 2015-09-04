#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script converts Finnish TSV-formatted lexicon to github wiki
"""


# Author: Tommi A Pirinen <flammie@iki.fi> 2009, 2011

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

from omorfi.omor_formatter import format_stuff_omor
from omorfi.ftb3_formatter import format_stuff_ftb3
from omorfi.giella_formatter import format_stuff_giella
from omorfi.apertium_formatter import format_stuff_apertium

# standard UI stuff

def main():
    # defaults
    outfile = None
    # initialise argument parser
    ap = argparse.ArgumentParser(description="Convert omorfi database to github pages")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
            default=False,
            help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
            help="print each step to stdout while processing")
    ap.add_argument("--paradigm-docs", "-P", action="append", required=True,
            metavar="PDFILE", help="read paradigm docs from PDFILEs")
    ap.add_argument("--stuff-docs", "-S", action="append", required=True,
            metavar="SDFILE", help="read stuff docs from SDFILE")
    ap.add_argument("--paradigms", "-A", required=True,
            metavar="PARADIR", help="read paradigm data from PARADIR/")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", action="store", required=True, 
            type=argparse.FileType('w'),
            metavar="OFILE", help="write docs OFILE")
    ap.add_argument("--fields", "-F", action="store", default=2,
            metavar="N", help="read N fields from master")
    ap.add_argument("--separator", action="store", default="\t",
            metavar="SEP", help="use SEP as separator")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
            metavar="COMMENT", help="skip lines starting with COMMENT that"
                "do not have SEPs")
    ap.add_argument("--strip", action="store",
            metavar="STRIP", help="strip STRIP from fields before using")

    args = ap.parse_args()

    quoting = csv.QUOTE_NONE
    quotechar = None
    #
    # write preamble to wiki page
    print('# Introduction', file=args.output)
    print("""This document was automatically generated from the omorfi 
            database. It describes some of the internal codes used in the
            database. Keys and values "_stuff_", and the _paradigms_ that
            define inflection patterns or so.""", file=args.output)
    # read from csv files
    print('## Stuff ', file=args.output)
    print("""Stuff are internal things, but they appear in database a lot, so
            you will want to know what they are if you are gonna modify database
            of affixes.""", file=args.output)
    print("""The stuff is typically used by the file format and/or analysis
        generators to either define analysis tags or decide whether or not to
        include the affected string into language model. The default renditions
        for a handful of omorfi tag formats are provided (only ones that have
        trivially0 mapped formatting are included.""", file=args.output)
    for tsv_filename in args.stuff_docs:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        # for each line
        with open(tsv_filename, "r", newline='') as tsv_file:
            tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                    strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 2:
                    print("Too few tabs on line", linecount, 
                            "skipping following line completely:", file=stderr)
                    print(tsv_parts, file=stderr)
                    continue
                print("### `", tsv_parts['stuff'], "` ", file=args.output)
                print(tsv_parts['doc'], file=args.output)
                print("* omor: ", format_stuff_omor(tsv_parts['stuff'],
                                                    'omor'), 
                        file=args.output)
                print("* ftb3: ", format_stuff_ftb3(tsv_parts['stuff']),
                        file=args.output)
                print("* apertium-fin: ", format_stuff_apertium(tsv_parts['stuff']),
                        file=args.output)
                print("* giella: ", format_stuff_giella(tsv_parts['stuff']),
                        file=args.output)
    
    paradata = dict()
    with open(args.paradigms + "/morphophonology.tsv") as tsv_file:
        tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                strict=True)
        for tsv_parts in tsv_reader:
            paradata[tsv_parts['new_para']] = dict()
            for key in tsv_parts.keys():
                if key != 'new_para':
                    paradata[tsv_parts['new_para']][key] = tsv_parts[key]
    print('\n## Paradigms', file=args.output)
    for tsv_filename in args.paradigm_docs:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        # for each line
        with open(tsv_filename, 'r', newline='') as tsv_file:
            tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                    strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 2:
                    tsv_line = tsv_file.readline()
                    continue
                print("### `", tsv_parts['new_para'], "`", 
                        file=args.output)
                print(tsv_parts['doc'], file=args.output)
                if tsv_parts['new_para'] in paradata:
                    for key in paradata[tsv_parts['new_para']].keys():
                        print("* ", key, ": ", paradata[tsv_parts['new_para']][key],
                                sep='', file=args.output)
                else:
                    if not tsv_parts['doc']:
                        print("UNDOCUMENTED", tsv_parts['new_para'])
                        exit(1)
    print('''<!-- vim: set ft=markdown:-->''', file=args.output)
    exit()


if __name__ == "__main__":
    main()

