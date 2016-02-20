#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script generates twolc files from database data.
"""


# Author: Omorfi contributors, 2014

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

from sys import exit
import argparse

from omorfi.twolc_formatter import format_alphabet_twolc, \
    format_sets_twolc, format_definitions_twolc, format_rules_twolc, \
    format_copyright_twolc

# standard UI stuff


def main():
    # initialise argument parser
    ap = argparse.ArgumentParser(
        description="Generate Xerox twolcs for Finnish")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--output", "-o", type=argparse.FileType("w"),
                    required=True, metavar="OFILE", help="write output to OFILE")
    ap.add_argument("--ruleset", "-r", required=True, action="store",
                    metavar="RULES", help="compile RULES ruleset")

    def format_arg_type(v):
        baseformats = ["omor", "apertium",
                       "giellatekno", "ftb3", "segments", "google"]
        extras = ["propers", "semantics", "ktnkav", "newparas", "taggerhacks"]
        parts = v.split('+')
        if parts[0] not in baseformats:
            raise argparse.ArgumentTypeError(
                "Format must be one of: " + " ".join(baseformats))
        for ex in parts[1:]:
            if ex not in extras:
                raise argparse.ArgumentTypeError(
                    "Format extension must be one of: " + " ".join(extras))
        return v
    ap.add_argument("--format", "-f", action="store", default="omor",
                    help="use specific output format for twolc data",
                    type=format_arg_type)
    args = ap.parse_args()
    # check args
    # setup files
    if args.verbose:
        print("Writing everything to", args.output.name)
    print(format_copyright_twolc(), file=args.output)
    # print definitions to rootfile
    if args.verbose:
        print("Creating Alphabet")
    print(format_alphabet_twolc(args.format, args.ruleset), file=args.output)
    if args.verbose:
        print("Creating Sets")
    print(format_sets_twolc(args.format, args.ruleset), file=args.output)
    if args.verbose:
        print("Creating Definitions")
    print(format_definitions_twolc(
        args.format, args.ruleset), file=args.output)
    if args.verbose:
        print("Creating Rules")
    print(format_rules_twolc(args.format, args.ruleset), file=args.output)
    exit(0)


if __name__ == "__main__":
    main()
