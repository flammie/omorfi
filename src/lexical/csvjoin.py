#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script simply joins 2-field ?SV data of omorfi two extra fields on
auxiliary files by matching the first 4 fields and adding the fifth.
"""

# Author: Tommi A. Pirinen <tommi.pirinen@helsinki.fi> 2009, 2011

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

from sys import stdin, stdout, stderr, exit, argv
import argparse
import locale

def main():
    ap = argparse.ArgumentParser(description=
            "Join 4-field CSV or TSV over fifth fields")

    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
            default=False,
            help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
            help="print each step to stdout while processing")
    ap.add_argument("--input", "-i", action="append", required=True, type=open,
            metavar="IFILE", help="read dictionary data from IFILEs")
    ap.add_argument("--join", "-j", action="append", required=True, type=open,
            metavar="JFILE",
            help="read auxiliary data from JFILEs")
    ap.add_argument("--output", "-o", action="store", required=True, 
            type=argparse.FileType('w'),
            metavar="OFILE",
            help="write resulting data to OFILE")
    ap.add_argument("--version", "-V", action="version")

    args = ap.parse_args()
    try:
        locale.setlocale(locale.LC_ALL, "fi_FI.utf8")
    except locale.Error:
        locale.setlocale(locale.LC_ALL, "fi_FI.UTF-8")
    except locale.Error:
        print("Must have Finnish UTF-8 locale to sort dictionaries")
        exit(1)

    # read from csv files
    words = dict()
    # read all csv files
    for csv_file in args.input:
        if args.verbose:
            print("Reading dictionary from", csv_file.name)
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
            if csv_line.count(',') >= 2:
                csv_parts = csv_line.split(',')
            elif csv_line.count('\t') >= 2:
                csv_parts = csv_line.split('\t')
            else:
                print("Must have at least 2 commas or tabs on each non-comment non-empty line of dictionary data; Skipping:", file=stderr)
                print(csv_line, file=stderr)
                csv_line = csv_file.readline()
                continue
            if csv_parts[-1] == '<-HEADERS':
                # skip header line
                csv_line = csv_file.readline()
                continue

            words[csv_line] = csv_parts
            csv_line = csv_file.readline()
    # join all join files (slow but more workable)
    for join_file in args.join:
        if args.verbose:
            print("Reading joins from", join_file.name)
        join_line = join_file.readline()
        linecount = 0
        while join_line:
            linecount += 1
            join_line = join_line.strip()
            if join_line.startswith("#") or join_line.startswith("!") or join_line == "":
                # comment line
                join_line = join_file.readline()
                continue
            join_parts = []
            join_on = ''
            if join_line.count(',') >= 3:
                join_parts = join_line.split(',')
                join_on = ','.join(join_parts[0:4])
            elif join_line.count('\t') >= 3:
                join_parts = join_line.split('\t')
                join_on = '\t'.join(join_parts[0:4])
            else:
                print("Must have at least 3 commas or tabs on each non-comment non-empty line of dictionary data; Skipping:", file=stderr)
                print(join_line, file=stderr)
                join_line = join_file.readline()
                continue
            if join_parts[-1] == '<-HEADERS':
                # skip header line
                join_line = join_file.readline()
                continue
            if not join_on in words.keys():
                print("Could not find the key", join_on, "of", join_file,
                "line", linecount, "from any of", args.input, file=stderr)
            else:
                this_entry = words[join_on]
                this_entry += [join_parts[4]]
                words[join_on] = this_entry
            join_line = join_file.readline()
    if args.verbose:
        print("Writing master database to", args.output.name)
    for (line,fields) in words.items():
        print("\t".join(fields), file=args.output)
    exit()


if __name__ == "__main__":
    main()

