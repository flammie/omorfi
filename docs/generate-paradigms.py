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
from sys import stderr


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
    ap.add_argument("--paradigm-docs", "-P", action="append", required=True,
                    metavar="PDFILE", help="read paradigm docs from PDFILEs")
    ap.add_argument("--paradigms", "-A", required=True,
                    metavar="PARAFILE",
                    help="read paradigm data from PARAFILE")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", action="store", required=True,
                    type=argparse.FileType('w'),
                    metavar="OFILE", help="write docs OFILE")
    ap.add_argument("--outdir", "-O", action="store", required=True,
                    metavar="ODIR", help="write individual paradigms to " +
                    "ODIR/paradigm.md")
    ap.add_argument("--fields", "-F", action="store", default=2,
                    metavar="N", help="read N fields from master")
    ap.add_argument("--separator", action="store", default="\t",
                    metavar="SEP", help="use SEP as separator")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
                    metavar="COMMENT",
                    help="skip lines starting with COMMENT that"
                    "do not have SEPs")
    ap.add_argument("--strip", action="store",
                    metavar="STRIP",
                    help="strip STRIP from fields before using")

    args = ap.parse_args()

    # write preamble to wiki page
    print('---', file=args.output)
    print('layout: default', file=args.output)
    print('title: Paradigms', file=args.output)
    print('---', file=args.output)
    print('# Paradigms', file=args.output)
    print(file=args.output)
    print("_This is an automatically generated documentation based on omorfi" +
          "lexical database._", file=args.output)
    print(file=args.output)
    print("Paradigms are sub-groups of lexemes that have unique " +
          "morpho-phonological features. " +
          "In omorfi database there is a unique " +
          "paradigm for every possible combination of certain features:",
          file=args.output)
    print(file=args.output)
    print("* Universal Part-of-speech", file=args.output)
    print("* Morphophonology, such as: vowel harmony, gradation pattern, " +
          " stem variations and allomorph selection", file=args.output)
    print("* Other morphotactic limitations, such as: only plurals allowed, " +
          " obligatory possessive suffixes, etc.", file=args.output)
    # read from csv files
    print(file=args.output)
    # stolen from turku:
    # https://turkunlp.github.io/Finnish_PropBank/
    print("| **UPOS** | **Paradigm** | _Notes_ |", file=args.output)
    print("|---------:|:-------------|:--------|", file=args.output)

    paradata = dict()
    with open(args.paradigms) as tsv_file:
        tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                                    strict=True)
        for tsv_parts in tsv_reader:
            paradata[tsv_parts['new_para']] = dict()
            for key in tsv_parts.keys():
                if key != 'new_para':
                    paradata[tsv_parts['new_para']][key] = tsv_parts[key]
    paradigms = set(paradata.keys())
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
                    print("Too few tabs on line", linecount,
                          "skipping following line completely:", file=stderr)
                    print(tsv_parts, file=stderr)
                    continue
                outfilename = args.outdir + '/' + \
                    tsv_parts['new_para'].replace('?', '_')
                outfile = open(outfilename + '.markdown', 'w')
                print('---', file=outfile)
                print('layout: paradigm', file=outfile)
                print('paradigm:', tsv_parts['new_para'], file=outfile)
                print('---', file=outfile)
                print("### `", tsv_parts['new_para'], "`",
                      file=outfile)
                print(file=outfile)
                print(tsv_parts['doc'], file=outfile)
                if tsv_parts['new_para'] in paradata:
                    for key in paradata[tsv_parts['new_para']].keys():
                        print("* ", key, ": ",
                              paradata[tsv_parts['new_para']][key],
                              sep='', file=outfile)
                    paradigms.remove(tsv_parts['new_para'])
                else:
                    print("found in docs but not in data:",
                          tsv_parts['new_para'], file=stderr)
                if not tsv_parts['doc']:
                    print("missing DOC:", tsv_parts['new_para'])
                    exit(1)
                if len(tsv_parts['doc']) > 40:
                    docshort = tsv_parts['doc'][:40] + '...'
                else:
                    docshort = tsv_parts['doc']
                print("| " + paradata[tsv_parts['new_para']]['upos'] +
                      " | [" + tsv_parts['new_para'] + "](" +
                      outfilename + ".html) | " + docshort + " |",
                      file=args.output)
    if paradigms:
        print("Undocumented paradigms left:", ", ".join(paradigms),
              file=stderr)
    print('''<!-- vim: set ft=markdown:-->''', file=args.output)
    exit()


if __name__ == "__main__":
    main()
