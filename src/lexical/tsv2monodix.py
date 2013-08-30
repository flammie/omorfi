#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script converts Finnish TSV-formatted lexicon to apertium format,
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

from format_output import format_monodix_alphabet, format_monodix_sdefs, format_monodix_pardef, format_monodix_entry
from parse_csv_data import parse_from_tsv

# standard UI stuff

def main():
    # defaults
    outfile = None
    # initialise argument parser
    ap = argparse.ArgumentParser(description="Convert Finnish dictionary TSV data into apertium monodix XML")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
            default=False,
            help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
            help="print each step to stdout while processing")
    ap.add_argument("--master", "-m", action="append", required=True, type=open,
            metavar="MFILE", help="read lexical roots from MFILEs")
    ap.add_argument("--stemparts", "-p", action="append", required=True, type=open,
            metavar="SPFILE", help="read lexical roots from SPFILEs")
    ap.add_argument("--inflection", "-i", action="append", required=True, type=open,
            metavar="INFFILE", help="read inflection from INFFILEs")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", action="store", required=True, 
            type=argparse.FileType('w'),
            metavar="OFILE", help="write roots to OFILE")
    args = ap.parse_args()
    # write header to XML file
    print('<?xml version="1.0" encoding="utf-8"?>', file=args.output)
    print('<dictionary>', file=args.output)
    print(format_monodix_alphabet(), file=args.output)
    print(format_monodix_sdefs(), file=args.output)
    # read from csv files
    print('  <pardefs>', file=args.output)
    for tsv_file in args.inflection:
        if args.verbose:
            print("Reading from", tsv_file.name)
        tsv_line = tsv_file.readline()
        linecount = 0
        curr_pardef = ''
        # for each line
        while tsv_line:
            linecount += 1
            tsv_line = tsv_line.strip()
            if tsv_line.startswith("#") or tsv_line.startswith("!") or tsv_line == "":
                # comment line
                tsv_line = tsv_file.readline()
                continue
            tsv_parts = []
            if tsv_line.count('\t') >= 3:
                tsv_parts = tsv_line.split("\t")
            else:
                print("Too few tabs on line", linecount, 
                    "skipping following line completely:", file=stderr)
                print(tsv_line, file=stderr)
                tsv_line = tsv_file.readline()
                continue
            if tsv_parts[-1] == '#<- HEADERS':
                # skip header line
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
    for tsv_file in args.stemparts:
        if args.verbose:
            print("Reading from", tsv_file.name)
        tsv_line = tsv_file.readline()
        linecount = 0
        curr_pardef = ''
        # for each line
        while tsv_line:
            linecount += 1
            tsv_line = tsv_line.strip()
            if tsv_line.startswith("#") or tsv_line.startswith("!") or tsv_line == "":
                # comment line
                tsv_line = tsv_file.readline()
                continue
            tsv_parts = []
            if tsv_line.count('\t') >= 3:
                tsv_parts = tsv_line.split("\t")
            else:
                print("Too few tabs on line", linecount, 
                    "skipping following line completely:", file=stderr)
                print(tsv_line, file=stderr)
                tsv_line = tsv_file.readline()
                continue
            if tsv_parts[-1] == '#<- HEADERS':
                # skip header line
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
    for tsv_file in args.master:
        if args.verbose:
            print("Reading from", tsv_file.name)
        tsv_line = tsv_file.readline()
        linecount = 0
        while tsv_line:
            linecount += 1
            if args.verbose and (linecount % 10000 == 0):
                print(linecount, "...", sep='')
            tsv_line = tsv_line.strip()
            if tsv_line.startswith("#") or tsv_line.startswith("!") or tsv_line == "":
                # comment line
                tsv_line = tsv_file.readline()
                continue
            tsv_parts = []
            if tsv_line.count('\t') >= 18:
                tsv_parts = tsv_line.split("\t")
            else:
                print("Too few tabs on line", linecount, 
                    "skipping following line completely:", file=stderr)
                print(tsv_line, file=stderr)
                tsv_line = tsv_file.readline()
                continue
            if tsv_parts[-1] == '<- HEADERS':
                # skip header line
                tsv_line = tsv_file.readline()
                continue
           # read data from database
            wordmap = dict()
            wordmap = parse_from_tsv(wordmap, tsv_parts)
            # format output
            print(format_monodix_entry(wordmap), file=args.output)
            tsv_line = tsv_file.readline()
    print('  </section>', file=args.output)
    print('</dictionary>', file=args.output)
    exit()


if __name__ == "__main__":
    main()

