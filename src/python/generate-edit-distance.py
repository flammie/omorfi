#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script generates edit distance.
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

from omorfi.settings import fin_lowercase, fin_uppercase, fin_symbols

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
    ap.add_argument("--deletion", "-d", type=float, default=1.0,
                    metavar="DW", help="weight each deletion DW")
    ap.add_argument("--addition", "-a", type=float, default=1.0,
                    metavar="AW", help="weight each addition AW")
    ap.add_argument("--swap", "-s", type=float, default=1.0, metavar="SW",
                    help="weight each swap SW")
    ap.add_argument("--change", "-c", type=float, default=1.0, metavar="CW",
                    help="weight each change CW")
    ap.add_argument("--output", "-o", type=argparse.FileType("w"),
                    required=True, metavar="OFILE", help="write output to OFILE")

    args = ap.parse_args()
    # check args
    # setup files
    if args.verbose:
        print("Writing everything to", args.output.name)
    # print definitions to rootfile
    if args.verbose:
        print("Creating EDs")
    print(0, 0.0, sep="\t", file=args.output)
    for c in fin_lowercase + fin_uppercase + fin_symbols:
        print(0, 0, c, c, 0.0, sep="\t", file=args.output)
        print(0, 1, c, "@_EPSILON_SYMBOL_@", args.deletion, sep="\t",
              file=args.output)
        print(0, 1, "@_EPSILON_SYMBOL_@", c, args.addition, sep="\t",
              file=args.output)
        print(1, 1, c, c, 0.0, sep="\t", file=args.output)
    print("%d\t%f\n", 0, 0.0, sep="\t", file=args.output)
    # generate swaps
    i = 2
    for c in fin_lowercase:
        for g in fin_lowercase:
            print(0, i, c, g, 0.0, sep="\t", file=args.output)
            print(i, 1, g, c, args.swap, sep="\t", file=args.output)
            print(i, args.change, sep="\t", file=args.output)
            i += 1

    exit(0)


if __name__ == "__main__":
    main()
