#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Validates databases
"""


# Author: Tommi A Pirinen <flammie@iki.fi> 2015

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#q
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from sys import stderr, stdout, exit, argv
from time import strftime
import argparse
import csv
import re

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
            metavar="IFILE", help="read data from IFILE")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--fields", "-f", action="store", default=2,
            metavar="N", help="read N fields from master")
    ap.add_argument("--regex-file", "-r", action="store", required=True,
            metavar="SFILE", help="read stem regexes from SFILE")
    ap.add_argument("--separator", "-s", action="store", default="\t",
            metavar="SEP", help="use SEP as separator")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
            metavar="COMMENT", help="skip lines starting with COMMENT that"
                "do not have SEPs")
    ap.add_argument("--strip", "-S", action="store",
            metavar="STRIP", help="strip STRIP characters")
    args = ap.parse_args()

    if args.strip == '"' or args.strip == "'":
        quoting = csv.QUOTE_ALL
        quotechar = args.strip
    else:
        quoting = csv.QUOTE_NONE
        quotechar = None

    errors = False
    # read joins from file if any
    regexmap = dict()
    with open(args.regex_file, 'r', newline='') as regexes:
        re_reader = csv.DictReader(regexes, delimiter=args.separator,
                quoting=quoting, escapechar='\\', strict=True)
        for re_parts in re_reader:
            if len(re_parts) < 2:
                print("Must have at least N separators in stubbings; skipping",
                        re_parts)
                continue
            key = re_parts['new_para']
            regexmap[key] = re_parts['suffix_regex']

    # read from csv files
    with open(args.input, 'r', newline='') as infile:
        tsv_reader = csv.DictReader(infile, delimiter=args.separator,
                quoting=quoting, escapechar='\\', strict=True)
        linecount = 0
        for tsv_parts in tsv_reader:
            linecount += 1
            if args.verbose and (linecount % 10000 == 0):
                print(linecount, "...", sep='', end='\r')
            if len(tsv_parts) < args.fields:
                print("Must have at least N separators on each",
                        "non-comment non-empty line; skipping:",
                        tsv_parts, file=stderr)
                continue
            if tsv_parts['new_para'] in regexmap:
                if not re.match('^.*' + regexmap[tsv_parts['new_para']] +
                        '$', tsv_parts['lemma']):
                    print(tsv_parts['lemma'], '!~ /^.*', 
                            regexmap[tsv_parts['new_para']], '$/',
                            sep='', file=stderr)
                    errors = True
    if errors:
        print("you must fix database integrity or hack the scripts",
              "before continuing")
        exit(1)

    exit()


if __name__ == "__main__":
    main()

