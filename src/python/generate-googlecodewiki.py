#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script converts Finnish TSV-formatted lexicon to googlecodewiki
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

# standard UI stuff

def main():
    # defaults
    outfile = None
    # initialise argument parser
    ap = argparse.ArgumentParser(description="Convert Finnish dictionary TSV data into googlecodewiki")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
            default=False,
            help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
            help="print each step to stdout while processing")
    ap.add_argument("--paradigm-docs", "-P", action="append", required=True,
            metavar="PDFILE", help="read paradigm docs from PDFILEs")
    ap.add_argument("--stuff-docs", "-S", action="append", required=True,
            metavar="SDFILE", help="read stuff docs from SDFILE")
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
    # write header to XML file
    print('#Summary Generated documentation of database keys and values', file=args.output)
    print('= Introduction =', file=args.output)
    print("This document was automatically generated from the omorfi " + \
            "database. It describes some of the internal codes used in the " + \
            "database keys and values \"_stuff_\", and the _paradigms_ that " + \
            "define inflection patterns", file=args.output)
    # read from csv files
    print('== Stuff ==', file=args.output)
    for tsv_filename in args.stuff_docs:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        # for each line
        with open(tsv_filename, "r", newline='') as tsv_file:
            tsv_reader = csv.reader(tsv_file, delimiter=args.separator,
                    strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 2:
                    if tsv_parts[0][0] not in args.comment:
                        print("Too few tabs on line", linecount, 
                            "skipping following line completely:", file=stderr)
                        print(tsv_parts, file=stderr)
                    continue
                print("  * `", tsv_parts[0], "`: ", tsv_parts[1], sep='',
                        file=args.output)
    print('== Paradigms ==', file=args.output)
    for tsv_filename in args.paradigm_docs:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        # for each line
        with open(tsv_filename, 'r', newline='') as tsv_file:
            tsv_reader = csv.reader(tsv_file, delimiter=args.separator,
                    strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 2:
                    if tsv_parts[0][0] not in args.comment:
                        print("Too few tabs on line", linecount, 
                            "skipping following line completely:", file=stderr)
                        print(tsv_parts, file=stderr)
                    tsv_line = tsv_file.readline()
                    continue
                print("  * `", tsv_parts[0], "`: ", tsv_parts[1], sep='',
                        file=args.output)
    print('''<wiki:comment>
vim: set ft=googlecodewiki:
</wiki:comment>''', file=args.output)
    exit()


if __name__ == "__main__":
    main()

