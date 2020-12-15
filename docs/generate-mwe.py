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


def filenamify(s):
    repls = {'!': 'EXCL', '?': 'QQ', '"': 'DQUO', "'": 'SQUO', '/': 'SLASH',
             '\\': 'BACKSLASH', '<': 'LEFT', '>': 'RIGHT', ':': 'COLON',
             ' ': 'SPACE', '|': 'PIPE', '.': 'STOP', ',': 'COMMA',
             ';': 'SC', '(': 'LBR', ')': 'RBR', '[': 'LSQ',
             ']': 'RSQ', '{': 'LCURL', '}': 'RCURL', '$': 'DORA',
             '\t': 'TAB'}
    for needl, subst in repls.items():
        s = s.replace(needl, subst)
    if s[0].upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖŠŽ':
        s = s[0].upper() + '/' + s
    return s


def markdownify(s):
    repls = {']': '(right square bracket)', '|': '(pipe symbol)',
             '[': '(left square bracket)'}
    for needl, subst in repls.items():
        s = s.replace(needl, subst)
    return s


def wiktify(s):
    repls = {']': '(right square bracket)', '|': '(pipe symbol)',
             '[': '(left square bracket)'}
    for needl, subst in repls.items():
        s = s.replace(needl, subst)
    return s


def homonymify(s):
    # ₀₁₂₃₄₅₆₇₈₉
    if '2' in s:
        return '₂'
    elif '3' in s:
        return '₃'
    elif '4' in s:
        return '₄'
    elif '5' in s:
        return '₅'
    elif '6' in s:
        return '₆'
    elif '7' in s:
        return '₇'
    elif '8' in s:
        return '₈'
    elif '9' in s:
        return '₉'
    else:
        return '₁'


def stuff2icon(s):
    if s == 'ORG':
        return 'org'
    elif s == 'GEO':
        return '🌍'
    elif s == 'FIRST':
        return '🧑¹'
    elif s == 'LAST':
        return '🧑²'
    elif s == 'FEMALE':
        return '♀'
    elif s == 'MALE':
        return '♂'
    elif s == 'CURRENCY':
        return '💱'
    elif s == 'MEDIA':
        return '📺'
    elif s == 'MISC':
        return '⁈'
    elif s == 'CULTGRP':
        return '🎶'
    elif s == 'LANGUAGE':
        return '🗪'
    elif s == 'COUNTRY':
        return '⚐'
    elif s == 'MEASURE':
        return '📏'
    else:
        return s

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
    ap.add_argument("--mwes", "-m", required=True,
                    metavar="MWEs", help="read mwe data from MWEs")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", action="store", required=True,
                    type=argparse.FileType('w'),
                    metavar="OFILE", help="write docs OFILE")
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

    # write preamble to wiki page
    print('# Multi-word entities (MWEs)', file=args.output)
    print(file=args.output)
    print("_This is an automatically generated documentation based on omorfi " +
          " lexical database._", file=args.output)
    print(file=args.output)
    print("Multi-word entities are *words* in dictionary that contain space," +
          " omorfi and many other systems generally treat space-separated " +
          "tokens, this list contains entries in dictionary that could be " +
          "processed as single unit.", file=args.output)
    print(file=args.output)
    print("We link to all original sources for reference.", file=args.output)
    print(file=args.output)
    print("| Lexeme | Short notes | Attributes | Links |", file=args.output)
    print("|:------:|:-----------:|:----------:|:------|", file=args.output)

    lexdata = dict()
    with open(args.mwes, 'r', newline='') as tsv_file:
        tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                                    strict=True)
        prev_lemma = ''
        linecount = 0
        for tsv_parts in tsv_reader:
            if len(tsv_parts) < 2 or tsv_parts['lemma'] is None or \
                    tsv_parts['homonym'] is None:
                print("Too few tabs on line, skipping:", tsv_parts)
                continue
            lexkey = tsv_parts['lemma'] + '\t' + tsv_parts['homonym']
            lexdata[lexkey] = tsv_parts
            linecount += 1
            if '\t' in tsv_parts['lemma']:
                print("ARGH python tsv fail on line:",
                      tsv_parts, file=stderr)
                continue
            print("| %s |" %
                  (markdownify(tsv_parts['lemma']) +
                   homonymify(tsv_parts['homonym'])),
                   end='', file=args.output)
            if tsv_parts['lemma'] != prev_lemma:
                prev_lemma = tsv_parts['lemma']
            print(" ...", end=' | ', file=args.output)
            print(" ...", end=' | ', file=args.output)
            lexkey = tsv_parts['lemma'] + '\t' + tsv_parts['homonym']
            if 'fiwikt' in tsv_parts['origin']:
                print("[fiwikt](https://fi.wiktionary.org/wiki/",
                      wiktify(tsv_parts['lemma']), end=') ', sep='',
                      file=args.output)
            if 'enwikt' in tsv_parts['origin']:
                print("[enwikt](https://en.wiktionary.org/wiki/",
                      wiktify(tsv_parts['lemma']), end=') ', sep='',
                      file=args.output)
            if 'finnwordnet' in tsv_parts['origin']:
                print("[finnwn](https://sanat.csc.fi/w/index.php?search=",
                      wiktify(tsv_parts['lemma']), end=') ', sep='',
                      file=args.output)
            print(" |", file=args.output)
    print('''<!-- vim: set ft=markdown:-->''', file=args.output)
    exit()


if __name__ == "__main__":
    main()
