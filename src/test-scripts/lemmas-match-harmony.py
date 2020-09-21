#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Validates databases
"""


# Author: Tommi A Pirinen <flammie@iki.fi> 2020

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
# q
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import argparse
import csv
import re
from sys import stderr


# standard UI stuff


def main():
    """Command-line interface for regex checking."""
    # initialise argument parser
    ap = argparse.ArgumentParser(
        description="Guess more data for Finnish TSV databases")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--input", "-i", action="store", required=True,
                    metavar="IFILE", help="read data from IFILE")
    ap.add_argument("--version", "-V", action="version")
    args = ap.parse_args()
    errors = False
    # read lemmas from lexemes file
    with open(args.input, 'r', newline='') as infile:
        tsv_reader = csv.DictReader(infile, delimiter='\t',
                                    quoting=csv.QUOTE_NONE, escapechar='\\',
                                    strict=True)
        linecount = 0
        for tsv_parts in tsv_reader:
            linecount += 1
            if args.verbose and (linecount % 10000 == 0):
                print(linecount, "...", sep='', end='\r')
            if len(tsv_parts) < 4 or None in tsv_parts.values():
                print("Must have at least 4 separators on each",
                      "non-comment non-empty line; skipping:",
                      tsv_parts, file=stderr)
                continue
            if not tsv_parts['harmony']:
                continue
            if tsv_parts['harmony'] == 'both':
                continue
            if tsv_parts['harmony'] == 'back':
                harmony_regex = '[AOUŌÓÅaouůåôąáăâāóōúūû][^äöy]*'
            elif tsv_parts['harmony'] == 'front':
                harmony_regex = '[ÄÖYIEĒÉÍäöyieíüýéőèěęøæõ][^aou]*'
            else:
                print("Unknown harmony:", tsv_parts['harmony'], file=stderr)
                errors=True
            if not re.match('^.*' + harmony_regex + '$',
                            tsv_parts['lemma']):
                if tsv_parts['boundaries']:
                    if not re.match('^.*' + harmony_regex + '$',
                                    tsv_parts['boundaries']):
                        print(tsv_parts['boundaries'],  tsv_parts['homonym'],
                              ' !~ /^.*', harmony_regex, sep='', file=stderr)
                        errors = True
                    else:
                        pass
                else:
                    print(tsv_parts['lemma'], tsv_parts['homonym'], ' !~ /^.*',
                          harmony_regex, '$/',
                          sep='', file=stderr)
                    errors = True
    if errors:
        print("you must fix database integrity or hack the scripts",
              "before continuing")
        exit(1)

    exit()


if __name__ == "__main__":
    main()
