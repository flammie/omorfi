#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script converts Finnish TSV-formatted lexicon to hunspell format,
"""


# Author: Tommi A Pirinen <flammie@iki.fi> 2009, 2011, 2018

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
import re
from sys import exit, stderr



# standard UI stuff


def main():
    # initialise argument parser
    ap = argparse.ArgumentParser(
        description="Convert Finnish dictionary TSV data into hunspell")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--master", "-m", action="append", required=True,
                    metavar="MFILE", help="read lexical roots from MFILEs")
    ap.add_argument("--continuations", "-c", action="append", required=True,
                    metavar="CONTFILE", help="read inflection from CONTFILEs")
    ap.add_argument("--paradigms", "-P", action="append", required=True,
                    metavar="PFILE", help="read paradigms from PFILEs")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--dic", "-d", action="store", required=True,
                    type=argparse.FileType('w'),
                    metavar="DFILE", help="write roots to DFILE")
    ap.add_argument("--aff", "-a", action="store", required=True,
                    type=argparse.FileType('w'),
                    metavar="OFILE", help="write affixes to AFILE")
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

    quoting = csv.QUOTE_NONE
    quotechar = None
    # map continuation to affixes
    affixmap = {'SUFFIX': 1, 'NOUN': 2, 'ADJ': 3, 'VERB': 4, 'INTJ': 5,
            'ACRONYM': 6, 'NUM': 7, 'PROPN': 8}
    conts = 0
    for tsv_filename in args.continuations:
        if args.verbose:
            print("Reading from", tsv_filename)
        with open(tsv_filename, "r", newline='') as tsv_file:
            tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                    strict=True)
            for tsv_parts in tsv_reader:
                if not tsv_parts['continuation'] in affixmap:
                    affixmap[tsv_parts['continuation']] = conts + 100
                    conts += 1
    # map paradigms to memory in dict
    paradigms = dict()
    for tsv_filename in args.paradigms:
        if args.verbose:
            print("Reading from", tsv_filename)
        with open(tsv_filename, "r", newline='') as tsv_file:
            tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                    strict=True)
            for tsv_parts in tsv_reader:
                paradigms[tsv_parts['new_para']] = tsv_parts
    # write header to AFF file
    if args.verbose:
        print("Writing affixes to", args.aff.file_name)
    print('SET UTF-8', file=args.aff)
    print('FLAG num', file=args.aff)
    #          abcdefghijklmnopqrstuvwxyzåäöšžABCDEFGHIJKLMNOPQRESTUVWXYZÅÄÖŠŽ-.
    print('TRY aintesloukämrvjhpydögbcfwzxqåšžAINTESLOUKÄMRVJHPYDÖGBCXFWZXQÅŠŽ-.',
            file=args.aff)
    for tsv_filename in args.continuations:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        prev_pardef = ''
        pardef_data = ''
        # for each line
        with open(tsv_filename, "r", newline='') as tsv_file:
            tsv_reader = csv.reader(tsv_file, delimiter=args.separator,
                                    strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 3:
                    print("Too few tabs on line", linecount,
                          "skipping following line completely:", file=stderr)
                    print(tsv_parts, file=stderr)
                    continue
                elif 'HEADERS' in tsv_parts[3]:
                    continue
                # format output
                if prev_pardef != '' and prev_pardef != tsv_parts[0]:
                    # AFFIX PARADIGM CROSS COUNT
                    pardef_data = 'SFX %d Y %d' % (affixmap[prev_pardef],
                            pardef_data.count('\n')) + pardef_data
                    print(pardef_data, file=args.aff)
                    pardef_data = ''
                # AFFIX PARADIGM DELETE ADD MATCH
                if tsv_parts[0] in paradigms:
                    deletion = paradigms[tsv_parts[0]]['deletion']
                    suffix_match = paradigms[tsv_parts[0]]['suffix_regex']
                else:
                    deletion = "0"
                    suffix_match = "."
                if deletion == None or deletion == "None":
                    deletion = "0"
                contlist = list()
                for cont in tsv_parts[3:]:
                    if cont == '#':
                        continue
                    contlist += [str(affixmap[cont])]
                conts = ','.join(contlist)
                affix = tsv_parts[2].replace('{MB}', '').replace('{DB}', '').replace('{STUB}', '')
                pardef_data += '\nSFX %d\t%s\t%s/%s\t%s' % (affixmap[tsv_parts[0]],
                        deletion, affix, conts, suffix_match)
                prev_pardef = tsv_parts[0]

    print(155883, file=args.dic)
    for tsv_filename in args.master:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        with open(tsv_filename, 'r', newline='') as tsv_file:
            tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                                        quoting=quoting, quotechar=quotechar,
                                        escapechar='%', strict=True)
            for tsv_parts in tsv_reader:
                linecount += 1
                if args.verbose and (linecount % 10000 == 0):
                    print(linecount, "...", sep='', end='\r')
                if len(tsv_parts) < 18:
                    print("Too few tabs on line", linecount,
                          "skipping following line completely:", file=stderr)
                    print(tsv_line, file=stderr)
                    tsv_line = tsv_file.readline()
                    continue
                wordmap = tsv_parts
                # XXX: format output
                if 'PROPN' in wordmap['new_para'] or 'IGNORE' in wordmap['new_para']:
                    pass
                elif wordmap['new_para'] in affixmap:
                    print(wordmap['lemma'], affixmap[wordmap['new_para']],
                            sep='/', file=args.dic)
                else:
                    print(wordmap['lemma'], file=args.dic)
                    print("Missing para", wordmap['new_para'], file=stderr)
    exit()


if __name__ == "__main__":
    main()
