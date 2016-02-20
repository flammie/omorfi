#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script converts Finnish TSV-formatted lexicon to apertium format,
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

from sys import stderr, exit
import argparse
import csv

from omorfi.monodix_formatter import format_monodix_alphabet, format_monodix_sdefs, format_monodix_pardef, format_monodix_entry, format_monodix_licence

# standard UI stuff


def main():
    # initialise argument parser
    ap = argparse.ArgumentParser(
        description="Convert Finnish dictionary TSV data into apertium monodix XML")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--master", "-m", action="append", required=True,
                    metavar="MFILE", help="read lexical roots from MFILEs")
    ap.add_argument("--stemparts", "-p", action="append", required=True,
                    metavar="SPFILE", help="read lexical roots from SPFILEs")
    ap.add_argument("--inflection", "-i", action="append", required=True,
                    metavar="INFFILE", help="read inflection from INFFILEs")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", action="store", required=True,
                    type=argparse.FileType('w'),
                    metavar="OFILE", help="write roots to OFILE")
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
    print('<?xml version="1.0" encoding="utf-8"?>', file=args.output)
    print(format_monodix_licence(), file=args.output)
    print('<dictionary>', file=args.output)
    print(format_monodix_alphabet(), file=args.output)
    print(format_monodix_sdefs(), file=args.output)
    # read from csv files
    print('  <pardefs>', file=args.output)
    for tsv_filename in args.inflection:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        curr_pardef = ''
        # for each line
        with open(tsv_filename, "r", newline='') as tsv_file:
            tsv_reader = csv.reader(tsv_file, delimiter=args.separator,
                                    strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 3:
                    print("Too few tabs on line", linecount,
                          "skipping following line completely:", file=stderr)
                    print(tsv_parts, file=stderr)
                    continue
                # format output
                if curr_pardef != tsv_parts[0]:
                    if curr_pardef != '':
                        print('  </pardef>', file=args.output)
                    print('  <pardef n="' +
                          tsv_parts[0].lower().replace('_', '__') +
                          '">', file=args.output)
                    curr_pardef = tsv_parts[0]
                print(format_monodix_pardef(tsv_parts), file=args.output)
    print('  </pardef>', file=args.output)
    for tsv_filename in args.stemparts:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        curr_pardef = ''
        # for each line
        with open(tsv_filename, 'r', newline='') as tsv_file:
            tsv_reader = csv.reader(tsv_file, delimiter=args.separator,
                                    strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 3:
                    print("Too few tabs on line", linecount,
                          "skipping following line completely:", file=stderr)
                    print(tsv_parts, file=stderr)
                    tsv_line = tsv_file.readline()
                    continue
                # format output
                if curr_pardef != tsv_parts[0]:
                    if curr_pardef != '':
                        print('  </pardef>', file=args.output)
                    print('  <pardef n="' +
                          tsv_parts[0].lower().replace('_', '__') +
                          '">', file=args.output)
                    curr_pardef = tsv_parts[0]
                print(format_monodix_pardef(tsv_parts), file=args.output)
                tsv_line = tsv_file.readline()
    print('  </pardef>', file=args.output)
    print('  </pardefs>', file=args.output)
    print('  <section id="main" type="standard">', file=args.output)
    for tsv_filename in args.master:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        with open(tsv_filename, 'r', newline='') as tsv_file:
            tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                                        quoting=quoting, quotechar=quotechar, escapechar='%', strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if args.verbose and (linecount % 10000 == 0):
                    print(linecount, "...", sep='', end='\r')
                if len(tsv_parts) < 18:
                    print("Too few tabs on line", linecount,
                          "skipping following line completely:", file=stderr)
                    print(tsv_line, file=stderr)
                    tsv_line = tsv_file.readline()
                    continue
                wordmap = tsv_parts
                # format output
                print(format_monodix_entry(wordmap), file=args.output)
    print('  </section>', file=args.output)
    print('</dictionary>', file=args.output)
    exit()


if __name__ == "__main__":
    main()
