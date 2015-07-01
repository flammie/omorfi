#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""This script creates a reweighting rulesets that match the current tag format.
"""


# Author: Tommi A Pirinen <flammie@iki.fi> 2014

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

from omorfi.formatters import format_stuff
from omorfi.settings import stuff_weights, boundary_weights

# standard UI stuff

def main():
    # initialise argument parser
    ap = argparse.ArgumentParser(description="Create FST reweighter for tags")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
            default=False,
            help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
            help="print each step to stdout while processing")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o",
            type=argparse.FileType("w"), required=True,
            metavar="OFILE", help="write output to OFILE")
    ap.add_argument("--fields", "-F", action="store", default=2,
            metavar="N", help="read N fields from master")
    ap.add_argument("--separator", action="store", default="\t",
            metavar="SEP", help="use SEP as separator")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
            metavar="COMMENT", help="skip lines starting with COMMENT that"
                "do not have SEPs")
    ap.add_argument("--strip", action="store",
            metavar="STRIP", help="strip STRIP from fields before using")

    def FormatArgType(v):
        baseformats = ["omor", "apertium",
                "giellatekno", "ftb3", "segments", "google", "boundary"]
        extras = ["propers", "semantics", "ktnkav", "newparas", "taggerhacks"]
        parts = v.split('+')
        if parts[0] not in baseformats:
            raise argparse.ArgumentTypeError("Format must be one of: " + " ".join(baseformats))
        for ex in parts[1:]:
            if ex not in extras:
                raise argparse.ArgumentTypeError("Format extension must be one of: " + " ".join(extras))
        return v
    ap.add_argument("--format", "-f", action="store", default="omor",
            help="use specific output format for lexc data",
            type=FormatArgType)
    args = ap.parse_args()
    # setup files
    if args.verbose: 
        print("Writing some weights to", args.output.name)
    if args.format == 'boundary':
        for tag, weight in boundary_weights.items():
            print(tag, weight, sep='\t', file=args.output)
    else:
        for stuff, weight in stuff_weights.items():
            if format_stuff(stuff, args.format) and format_stuff(stuff, args.format) != '0':
                print(format_stuff(stuff, args.format), weight,
                        sep='\t', file=args.output)
    exit(0)


if __name__ == "__main__":
    main()

