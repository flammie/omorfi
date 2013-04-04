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

from format_output import format_xml_kotus_sanalista
from parse_csv_data import parse_from_tsv

# standard UI stuff

def main():
    # defaults
    outfile = None
    # initialise argument parser
    ap = argparse.ArgumentParser(description="Convert Finnish dictionary TSV data into kotus sanalista XML")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
            default=False,
            help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
            help="print each step to stdout while processing")
    ap.add_argument("--input", "-i", action="append", required=True, type=open,
            metavar="IFILE", help="read data from IFILEs")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", action="store", required=True, 
            type=argparse.FileType('w'),
            metavar="OFILE", help="write roots to OFILE")
    args = ap.parse_args()
    # write header to XML file
    print('<?xml version="1.0" encoding="utf-8"?>', file=args.output)
    print('<!DOCTYPE kotus-sanalista SYSTEM "kotus-sanalista.dtd">', 
            file=args.output)
    print('<!--\nCopyright © Kotimaisten kielten tutkimuskeskus 2006',
            file=args.output)
    print('© Joukahainen, Wiktionary, Finnwordnet, omorfi contributors 2013',
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
    for csv_file in args.input:
        if args.verbose:
            print("Reading from", csv_file.name)
        csv_line = csv_file.readline()
        linecount = 0
        lexicon_count = 0
        entry_count = 0
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
            # format output
            print(format_xml_kotus_sanalista(wordmap), file=args.output)
            csv_line = csv_file.readline()
    print('</kotus-sanalista>', file=args.output)
    exit()


if __name__ == "__main__":
    main()

