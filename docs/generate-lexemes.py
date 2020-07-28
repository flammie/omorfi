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
    if s == '1':
        return '₁'
    elif s == '2':
        return '₂'
    elif s == '3':
        return '₃'
    elif s == '4':
        return '₄'
    elif s == '5':
        return '₅'
    elif s == '6':
        return '₆'
    elif s == '7':
        return '₇'
    elif s == '8':
        return '₈'
    elif s == '9':
        return '₉'
    elif s == '10':
        return '₁₀'
    elif s == '11':
        return '₁₁'
    elif s == '12':
        return '₁₂'
    elif s == '13':
        return '₁₃'
    elif s == '14':
        return '₁₄'
    elif s == '15':
        return '₁₅'
    elif s == '16':
        return '₁₆'
    else:
        return s


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
    ap.add_argument("--lexeme-docs", "-L", required=True,
                    metavar="LDFILE", help="read lexeme docs from LDFILE")
    ap.add_argument("--lexemes", "-l", required=True,
                    metavar="LEXENES", help="read lexemes data from LEXEMES")
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
    print('# Lexemes', file=args.output)
    print(file=args.output)
    print("_This is an automatically generated documentation based on omorfi" +
          " lexical database._", file=args.output)
    print(file=args.output)
    print("Lexemes are the word-entries of omorfi, currently we have only " +
          "documented the ones that are commonly problematic, in terms of " +
          "unexpected ambiguity, exceptional spelling or anything otherwise " +
          "worth noting.", file=args.output)
    print(file=args.output)
    print("In attributes column we use following emoji shorthands:",
          file=args.output)
    print("* ☢ for lexemes listed as unlikely for disambiguation purposes",
          file=args.output)
    print("*", stuff2icon("FIRST"), "for first name of a person",
          file=args.output)
    print("*", stuff2icon("MALE"), "for primarily male names",
          file=args.output)
    print("*", stuff2icon("FEMALE"), "for primarily female names",
          file=args.output)
    print("*", stuff2icon("LAST"), "for surname of a person",
          file=args.output)
    print("*", stuff2icon("GEO"), "for geographic location",
          file=args.output)
    print("*", stuff2icon("COUNTRY"), "for a country",
          file=args.output)
    print("*", stuff2icon("CURRENCY"), "for currencies",
          file=args.output)
    print("*", stuff2icon("MEDIA"), "for media",
          file=args.output)
    print("*", stuff2icon("CULTGRP"), "for band or artists",
          file=args.output)
    print("*", stuff2icon("LANGUAGE"), "for languages",
          file=args.output)
    print("*", stuff2icon("ORG"), "for organisations",
          file=args.output)
    print("*", stuff2icon("MEASURE"), "for unit of measurement",
          file=args.output)
    print("*", stuff2icon("MISC"), "for proper noun not suitable for other",
          "categories of proper nouns", file=args.output)
    print(file=args.output)
    print("We link to all original sources for reference.", file=args.output)
    print(file=args.output)
    print("| Lexeme | Short notes | Attributes | Links |", file=args.output)
    print("|:------:|:-----------:|:----------:|:------|", file=args.output)

    lexdata = dict()
    with open(args.lexemes, 'r', newline='') as tsv_file:
        tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                                    strict=True)
        for tsv_parts in tsv_reader:
            if len(tsv_parts) < 2 or tsv_parts['lemma'] is None or \
                    tsv_parts['homonym'] is None:
                print("Too few tabs on line, skipping:", tsv_parts)
                continue
            lexkey = tsv_parts['lemma'] + '\t' + tsv_parts['homonym']
            lexdata[lexkey] = tsv_parts
    with open(args.lexeme_docs, 'r', newline='') as tsv_file:
        tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                                    strict=True)
        prev_lemma = ''
        linecount = 0
        for tsv_parts in tsv_reader:
            linecount += 1
            if len(tsv_parts) < 2 or tsv_parts['doc'] is None:
                print("Too few tabs on line", linecount,
                      "skipping following line completely:", file=stderr)
                print(tsv_parts, file=stderr)
                continue
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
            print(" ", tsv_parts['doc'], end=' | ', file=args.output)
            lexkey = tsv_parts['lemma'] + '\t' + tsv_parts['homonym']
            if lexkey in lexdata:

                if lexdata[lexkey]['proper_noun_class']:
                    print(stuff2icon(lexdata[lexkey]['proper_noun_class']),
                          file=args.output, end='')
                if lexdata[lexkey]['blacklist']:
                    print("☢", file=args.output, end='')
                if lexdata[lexkey]['sem']:
                    print(stuff2icon(lexdata[lexkey]['sem']),
                          file=args.output, end='')
                print(' | ', end='', file=args.output)
                if 'fiwikt' in lexdata[lexkey]['origin']:
                    print("[fiwikt](https://fi.wiktionary.org/wiki/",
                          wiktify(tsv_parts['lemma']), end=') ', sep='',
                          file=args.output)
                if 'enwikt' in lexdata[lexkey]['origin']:
                    print("[enwikt](https://en.wiktionary.org/wiki/",
                          wiktify(tsv_parts['lemma']), end=') ', sep='',
                          file=args.output)
                if 'finnwordnet' in lexdata[lexkey]['origin']:
                    print("[finnwn](https://sanat.csc.fi/w/index.php?search=",
                          wiktify(tsv_parts['lemma']), end=') ', sep='',
                          file=args.output)
            print(" |", file=args.output)
    print('''<!-- vim: set ft=markdown:-->''', file=args.output)
    exit()


if __name__ == "__main__":
    main()
