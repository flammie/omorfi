#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script is nothing but a simple ?SV file join. It uses 1 master
database with N fields and joins all matching fields on M files to extra
fields on right.
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
            "Join N field master CSV or TSV file with others having N+1 fields")

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
    ap.add_argument("--fields", "-f", action="store", default=2,
            metavar="N", help="read N fields from master")
    ap.add_argument("--separator", "-s", action="store", default="\t",
            metavar="SEP", help="use SEP as separator")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
            metavar="COMMENT", help="skip lines starting with COMMENT that"
                "do not have SEPs")
    ap.add_argument("--strip", "-S", action="store",
            metavar="STRIP", help="strip STRIP from fields before using")
    args = ap.parse_args()
    try:
        locale.setlocale(locale.LC_ALL, "fi_FI.utf8")
    except locale.Error:
        locale.setlocale(locale.LC_ALL, "fi_FI.UTF-8")
    except locale.Error:
        print("Must have Finnish UTF-8 locale to sort dictionaries")
        exit(1)

    words = dict()
    for csv_file in args.input:
        if args.verbose:
            print("Reading dictionary from", csv_file.name)
        linecount = 0
        entry_count = 0
        for csv_line in csv_file:
            linecount += 1
            csv_line = csv_line.strip("\n")
            if args.verbose and (linecount % 10000) == 0:
                print(linecount, "...", end='\r')
            if csv_line.strip() == "":
                # empties can be skipped
                continue
            for cc in args.comment:
                if csv_line.startswith(cc): 
                    # comment line
                    continue
            csv_parts = []
            if csv_line.count(args.separator) >= (args.fields - 1):
                csv_parts = csv_line.split(args.separator)
            else:
                print("Must have at least N-1 separators on each "
                      "non-comment non-empty line. Skipping:", csv_line,
                      file=stderr)
                continue
            if csv_parts[-1].endswith('<-HEADERS'):
                # skip header line
                csv_line = csv_file.readline()
                continue
            if args.strip:
                csv_parts = [x.strip(args.strip) for x in csv_parts]
            key = args.separator.join(csv_parts[0:args.fields])
            words[key] = csv_parts
            entry_count += 1
        if args.verbose:
            print("\n", entry_count, "entries in database")
    # join all join files (slow but more workable)
    for join_file in args.join:
        if args.verbose:
            print("Reading joins from", join_file.name)
        linecount = 0
        joincount = 0
        for join_line in join_file:
            linecount += 1
            join_line = join_line.strip("\n")
            if args.verbose and (linecount % 10000) == 0:
                print(linecount, "...", end='\r')
            if join_line.strip() == "":
                # empties can be skipped
                continue
            for cc in args.comment:
                if join_line.startswith(cc): 
                    # comment line
                    continue
            join_parts = []
            join_on = ''
            if join_line.count(args.separator) >= args.fields:
                join_parts = join_line.split(args.separator)
            else:
                print("Must have at least N separtors on each",
                    "non-comment non-empty line of join; Skipping:", join_line,
                    file=stderr)
                continue
            if args.strip:
                join_parts = [x.strip(args.strip) for x in join_parts]
            join_on = args.separator.join(join_parts[0:args.fields])
            if join_parts[-1].endswith('<-HEADERS'):
                # skip header line
                continue
            if not join_on in words.keys():
                print("\033[93mMissing!\033[0m "
                      "Could not find the key",
                      join_on, "used by", join_file.name,
                      "line", linecount, "in any of", 
                      [x.name for x in args.input], file=stderr)
            else:
                this_entry = words[join_on]
                this_entry += [join_parts[args.fields]]
                words[join_on] = this_entry
                joincount += 1
            join_line = join_file.readline()
        if args.verbose:
            print("\n", joincount, "joins in that table")
    if args.verbose:
        print("Writing master database to", args.output.name)
        print("Sorting")
    print("# This file was automatically generated from", 
            [x.name for x in args.input],
            "\n# and",
            [x.name for x in args.join],
            "\n# using tsvjoin.py", file=args.output)
    linecount = 0
    for (line,fields) in sorted(words.items()):
        linecount += 1
        if args.verbose and (linecount % 10000) == 0 or linecount == 1:
            print(linecount, "...", end='\r')
        print(args.separator.join(fields), file=args.output)
    if args.verbose:
        print()
    exit()


if __name__ == "__main__":
    main()

