#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script expands Finnish TSV-formatted lexicon with a lot of data by
automatic guessing. The
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
# q
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from sys import stderr, exit
import argparse
import csv

from omorfi.wordmap import init_wordmap, get_wordmap_fieldnames
from omorfi.parse_csv_data import parse_defaults_from_tsv, parse_extras_from_tsv
from omorfi.stub import stub_all_new_para
# from guess_feats import guess_grade_dir_from_ktn, guess_harmony,
# guess_stem_features_ktn, guess_pronunciation,
from omorfi.guess_feats import guess_bound_morphs
# from guess_new_class import guess_new_class


# standard UI stuff

def main():
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
    ap.add_argument("--output", "-o", action="store", required=True,
                    metavar="OFILE", help="write data to OFILE")
    ap.add_argument("--fields", "-f", action="store", default=2,
                    metavar="N", help="read N fields from master")
    ap.add_argument("--join", "-j", action="store", required=True,
                    metavar="JFILE", help="read join fields from JFILE")
    ap.add_argument("--stub", "-c", action="store", required=True,
                    metavar="SFILE", help="read stub expressions from SFILE")
    ap.add_argument("--separator", "-s", action="store", default="\t",
                    metavar="SEP", help="use SEP as separator")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
                    metavar="COMMENT", help="skip lines starting with COMMENT that"
                    "do not have SEPs")
    ap.add_argument("--strip", "-S", action="store",
                    metavar="STRIP", help="strip STRIP characters")
    args = ap.parse_args()

    if args.strip == '"' or args.strip == "'":
        quoting = csv.QUOTE_ALL
        quotechar = args.strip
    else:
        quoting = csv.QUOTE_NONE
        quotechar = None

    errors = False
    joinmap = dict()
    # read joins from file if any
    with open(args.join, 'r', newline='') as joins:
        join_reader = csv.DictReader(joins, delimiter=args.separator,
                                     quoting=quoting, escapechar='\\', strict=True)
        for join_parts in join_reader:
            if len(join_parts) < 3:
                print("Must have at leas N separators in joins; skipping",
                      join_parts)
                continue
            key = join_parts['new_para']
            joinmap[key] = join_parts
    stubmap = dict()
    with open(args.stub, 'r', newline='') as stubs:
        stub_reader = csv.DictReader(stubs, delimiter=args.separator,
                                     quoting=quoting, escapechar='\\', strict=True)
        for stub_parts in stub_reader:
            if len(stub_parts) < 2:
                print("Must have at least N separators in stubbings; skipping",
                      stub_parts)
                continue
            key = stub_parts['new_para']
            stubmap[key] = stub_parts['deletion']

    # read from csv files
    with open(args.output, 'w', newline='') as output:
        tsv_writer = csv.DictWriter(output,
                                    fieldnames=get_wordmap_fieldnames(),
                                    delimiter=args.separator, quoting=quoting,
                                    escapechar='%', quotechar=quotechar, strict=True)
        tsv_writer.writeheader()
        with open(args.input, 'r', newline='') as infile:
            tsv_reader = csv.reader(infile, delimiter=args.separator,
                                    quoting=quoting, escapechar='\\', strict=True)
            linecount = 0
            for tsv_parts in tsv_reader:
                linecount += 1
                if args.verbose and (linecount % 10000 == 0):
                    print(linecount, "...", sep='', end='\r')
                if len(tsv_parts) < args.fields:
                    print("Must have at least N separators on each",
                          "non-comment non-empty line; skipping:",
                          tsv_parts, file=stderr)
                    continue
                # here starts the guessworks
                # the aim is to fill dict wordmap with data necessary to
                # generate a lexc line
                wordmap = init_wordmap()
                wordmap = parse_defaults_from_tsv(wordmap, tsv_parts)
                wordmap = parse_extras_from_tsv(wordmap, tsv_parts)
                # Extend from known new paras
                joinkey = wordmap['new_para']
                if joinkey in joinmap:
                    for k, v in joinmap[joinkey].items():
                        if k != 'new_para':
                            if v == "False":
                                wordmap[k] = False
                            elif v == "None":
                                wordmap[k] = None
                            elif k == 'kotus_tn':
                                try:
                                    wordmap[k] = int(v)
                                except:
                                    print("FAIL", k, v, tsv_parts)
                                    exit(2)
                            else:
                                wordmap[k] = v
                else:
                    print("\033[93mMissing!\033[0m",
                          "new para not in join data:", joinkey,
                          "\n\033[92mExplanation:\033[0m"
                          "add paradigm to morphophonology.tsv and carry on")
                    errors = True
                    continue

                # Guess-works in order
                # wordmap = guess_stem_features_ktn(wordmap)
                # wordmap = guess_pronunciation(wordmap)
                # wordmap = guess_grade_dir_from_ktn(wordmap)
                # wordmap = guess_harmony(wordmap)
                # wordmap = guess_new_class(wordmap)
                wordmap = stub_all_new_para(wordmap, stubmap)
                if not wordmap:
                    errors = True
                    continue
                # suffixes can be id'd by the - in beginning. They need an own
                # lexicon
                wordmap = guess_bound_morphs(wordmap)
                if wordmap['is_suffix']:
                    wordmap['real_pos'] = wordmap['pos']
                    wordmap['pos'] = 'SUFFIX'
                if "PCLE_HAH" == wordmap['new_para']:
                    wordmap['real_pos'] = wordmap['pos']
                    wordmap['pos'] = 'INTERJECTION'
                wordmaps = [wordmap]
                for wordmap in wordmaps:
                    tsv_writer.writerow(wordmap)
    if errors:
        print("you must fix database integrity or hack the scripts",
              "before continuing")
        exit(1)

    exit()


if __name__ == "__main__":
    main()
