#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Sort a TSV file.
Tries to stabilise sort order of tsv files to make neater change histories.
Because editors and OSes sort differently.
"""

# Author: Tommi A. Pirinen <flammie@iki.fi> 2009, 2011

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

import argparse
import csv
from sys import exit


def main():
    ap = argparse.ArgumentParser(
        description="Sort tsv files")

    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--input", "-i", required=True, dest='infilename',
                    metavar="IFILE", help="read dictionary data from IFILE")
    ap.add_argument("--output", "-o", action="store", required=True,
                    dest='outfilename',
                    metavar="OFILE",
                    help="write resulting data to OFILE")
    ap.add_argument("--fields", "-f", action="store", type=int, default=3,
                    metavar="N", help="read N fields from master")
    ap.add_argument("--separator", "-s", action="store", default="\t",
                    metavar="SEP", help="use SEP as separator")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
                    metavar="COMMENT", help="skip lines starting with COMMENT that"
                    "do not have SEPs")
    ap.add_argument("--strip", "-S", action="store",
                    metavar="STRIP", help="strip STRIP from fields before using")
    ap.add_argument("--ignore-errors", "-I", action="store_true", default=False,
                    help="silently ignore references to entries missing from master file")
    args = ap.parse_args()

    if args.strip == '"' or args.strip == "'":
        quoting = csv.QUOTE_ALL
    else:
        quoting = csv.QUOTE_NONE

    linecount = 0
    lexdata = dict()
    fields = dict()
    with open(args.infilename, 'r', newline='') as tsv_file:
        if args.verbose:
            print("Reading dictionary from", args.infilename)
        tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                                    strict=True)
        for tsv_parts in tsv_reader:
            linecount += 1
            if args.verbose and ((linecount % 10000) == 0 or linecount == 1):
                print(linecount, "...", end='\r')
            if len(tsv_parts) < 2:
                print("Too few tabs on line, skipping:", tsv_parts)
                continue
            lexkey = str(tsv_parts)  # simply use data repr as sort key
            fields = tsv_parts.keys()
            lexdata[lexkey] = tsv_parts
        if args.verbose:
            print("\n", linecount, "entries in database")
    with open(args.outfilename, "w") as output:
        if args.verbose:
            print("Writing master database to", args.outfilename)
            print("Sorting")
        linecount = 0
        tsv_writer = csv.DictWriter(output, fields, delimiter=args.separator,
                                    quoting=quoting, escapechar='\\',
                                    strict=True, lineterminator='\n')
        tsv_writer.writeheader()
        # print("lemma", "homonym", "new_para", "origin", sep='\t', file=output)
        for (line, fields) in sorted(lexdata.items()):
            linecount += 1
            if args.verbose and ((linecount % 10000) == 0 or linecount == 1):
                print(linecount, "...", end='\r')
            if '\\' in fields['lemma']:
                # There's no other way around python's broken TSV escaping
                fields['lemma'] = fields['lemma']\
                    .replace('\\"', '"').replace('\\\\', '\\')
            tsv_writer.writerow(fields)
            # print(fields['lemma'], fields['homonym'], fields['new_para'],
            #        fields['origin'], sep='\t', file=output)
        if args.verbose:
            print()
    exit()


if __name__ == "__main__":
    main()
