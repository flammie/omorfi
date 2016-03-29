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

import argparse
import csv
from sys import exit, stderr

from omorfi.kotus_sanalista_formatter import format_wordmap_kotus_sanalista


# standard UI stuff


def main():
    # initialise argument parser
    ap = argparse.ArgumentParser(
        description="Convert Finnish dictionary TSV data into kotus sanalista XML")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--master", "-m", action="append", required=True,
                    metavar="IFILE", help="read data from IFILEs")
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

    if args.strip == '"' or args.strip == "'":
        quoting = csv.QUOTE_ALL
        quotechar = args.strip
    else:
        quoting = csv.QUOTE_NONE
        quotechar = None

    # write header to XML file
    print('<?xml version="1.0" encoding="utf-8"?>', file=args.output)
    print('<!DOCTYPE kotus-sanalista SYSTEM "kotus-sanalista.dtd">',
          file=args.output)
    print('<!--\nCopyright © Kotimaisten kielten tutkimuskeskus 2006',
          file=args.output)
    print('© Joukahainen, Wiktionary, Finnwordnet, omorfi contributors 2014',
          file=args.output)
    print('Omorfiin koostettu laajennettu nykysuomen sanalista',
          file=args.output)
    print(file=args.output)
    print('Koostettu sanalista julkaistaan GNU GPL -lisenssillä.',
          file=args.output)
    print('Lisenssiteksti luettavissa osoitteessa',
          'http://www.gnu.org/licenses/gpl.html', file=args.output)
    print('-->', file=args.output)
    print(file=args.output)
    print('<kotus-sanalista>', file=args.output)
    # read from csv files
    for tsv_filename in args.master:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        # for each line
        with open(tsv_filename, 'r', newline='') as tsv_file:
            tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                                        quoting=quoting, quotechar=quotechar, escapechar='%', strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 18:
                    print("Too few tabs on line", linecount,
                          "skipping following line completely:", file=stderr)
                    print(tsv_parts, file=stderr)
                    continue
                wordmap = tsv_parts
                # format output
                print(
                    format_wordmap_kotus_sanalista(wordmap), file=args.output)
    print('</kotus-sanalista>', file=args.output)
    exit()


if __name__ == "__main__":
    main()
