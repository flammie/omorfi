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

import argparse
import csv
from sys import exit, stderr

from omorfi.apertium_formatter import ApertiumFormatter
from omorfi.ftb3_formatter import Ftb3Formatter
from omorfi.giella_formatter import GiellaFormatter
from omorfi.omor_formatter import OmorFormatter


# standard UI stuff


def main():
    # initialise argument parser
    ap = argparse.ArgumentParser(
        description="Convert omorfi database to github pages")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--stuff-docs", "-S", action="append", required=True,
                    metavar="SDFILE", help="read stuff docs from SDFILE")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", action="store", required=True,
                    type=argparse.FileType('w'),
                    metavar="OFILE", help="write index page to OFILE")
    ap.add_argument("--outdir", "-O", action="store", required=True,
                    metavar="ODIR", help="write individual stuffs to " +
                    "ODIR/stuff.md")
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

    # write preamble to wiki page
    print('---', file=args.output)
    print('layout: page', file=args.output)
    print('title: Omor stuff–Internal codes', file=args.output)
    print('---', file=args.output)
    print('# omor stuff: some internal short-hand codes in omorfi databases',
            file=args.output)
    print(file=args.output)
    print("_This is an automatically generated documentation based on omorfi" +
          "lexical database._", file=args.output)
    # read from csv files
    print(file=args.output)
    print("Stuff are internal things, but they appear in database a lot, so " +
          "you will want to know what they are if you are gonna modify " +
          "database of affixes.", file=args.output)
    print(file=args.output)
    print("The stuff is typically used by the file format and/or analysis " +
          "generators to either define analysis tags or decide whether or " +
          "not to include the affected string into language model. The " +
          "default renditions for a handful of omorfi tag formats are " +
          "provided (only ones that have trivially mapped formatting are " +
          "included.", file=args.output)
    print(file=args.output)
    # stolen from turku:
    # https://turkunlp.github.io/Finnish_PropBank/
    print("""<p>Stuffs:
{% for page in site.pages %}{% if page.stuff %}
<a href="stuffs/{{page.stuff}}.html">{{page.stuff}}</a>, 
{% endif %}{% endfor %}
</p>

## Stuffs in tabular format

The symbols are default output variants without context-sensitive filtering.


""", file=args.output)
    formatters = [OmorFormatter(args.verbose), ApertiumFormatter(args.verbose),
                  Ftb3Formatter(args.verbose), GiellaFormatter(args.verbose)]
    print("| Stuff | Doc | Omorfi | Apertium | FTB 3.1 | Giella |",
            file=args.output)
    print("|:-----:|:---:|:------:|:--------:|:-------:|:------:|",
            file=args.output)
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
                outfile=open(args.outdir + '/' + 
                             tsv_parts['stuff'].replace('?', '_') +
                             '.markdown', 'w')
                print('---', file=outfile)
                print('layout: stuff', file=outfile)
                print('stuff:', tsv_parts['stuff'].replace('?', '_'),
                        file=outfile)
                print('---', file=outfile)
                print("# `", tsv_parts['stuff'], "`", file=outfile)
                print("| ", tsv_parts['stuff'], " |", file=args.output,
                        end=' ', sep='')
                print(file=outfile)
                print(tsv_parts['doc'], file=outfile)
                print(tsv_parts['doc'], file=args.output, end=' ')
                print(file=outfile)
                print("## Default formats", file=outfile)
                print("| Omorfi | Apertium | FTB 3.1 | Giella |", file=outfile)
                print("|:------:|:--------:|:-------:|:------:|", file=outfile)
                for formatter in formatters:
                    print("| ", formatter.stuff2lexc(tsv_parts['stuff']),
                            file=outfile, end=' ')
                    print("| ", formatter.stuff2lexc(tsv_parts['stuff']),
                            file=args.output, end=' ')
                print(" |", file=outfile)
                print(" |", file=args.output)

    print(file=args.output)
    print('''<!-- vim: set ft=markdown:-->''', file=args.output)
    exit()


if __name__ == "__main__":
    main()
