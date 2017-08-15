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
from sys import exit, stderr


def filenamify(s):
    repls = {'!': 'EXCL', '?': 'QQ', '"': 'DQUO', "'": 'SQUO', '/': 'SLASH',
            '\\': 'BACKSLASH', '<': 'LEFT', '>': 'RIGHT', ':': 'COLON',
            ' ': 'SPACE', '|': 'PIPE', '.': 'STOP', ',': 'COMMA', 
            ';': 'SC', '(': 'LBR', ')': 'RBR', '[': 'LSQ',
            ']': 'RSQ', '{': 'LCURL', '}': 'RCURL', '$': 'DORA',
            '\t': 'TAB'}
    for needl, subst in repls.items():
        s = s.replace(needl, subst)
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
    ap.add_argument("--lexeme-docs", "-L", action="append", required=True,
                    metavar="PDFILE", help="read paradigm docs from LDFILEs")
    ap.add_argument("--lexemes", "-l", required=True,
                    metavar="LEXENES", help="read lexemes data from LEXEMES")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--output", "-o", action="store", required=True,
                    type=argparse.FileType('w'),
                    metavar="OFILE", help="write docs OFILE")
    ap.add_argument("--outdir", "-O", action="store", required=True,
                    metavar="ODIR", help="write individual paradigms to " +
                    "ODIR/paradigm.md")
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
    print('---', file=args.output)
    print('layout: page', file=args.output)
    print('title: Lexemes', file=args.output)
    print('---', file=args.output)
    print('# Lexemes', file=args.output)
    print(file=args.output)
    print("_This is an automatically generated documentation based on omorfi" +
          "lexical database._", file=args.output)
    print(file=args.output)
    print("Lexemes are the word-entries of omorfi, currently we have only " +
            "documented the ones that are commonly problematic, in terms of " +
            "unexpected ambiguity, exceptional spelling or anything otherwise " +
            "worth noting. Full dictionary can be found for the time being " +
            "in wiktionary, or other such services.", file=args.output)
    print(file=args.output)
    # read from csv files
    print(file=args.output)
    # stolen from turku:
    # https://turkunlp.github.io/Finnish_PropBank/
    print("""<table id="lexemetable" class="display">
<thead>
<tr>
<th>Lexeme</th>
</tr>
</thead>
<tbody>
{% for page in site.pages %}
{% if page.lexeme %}
<tr><td><a href="lexemes/{{page.lexeme}}.html">{{page.lexeme}}</a></td></tr>
{% endif %}
{% endfor %}
</tbody>
</table>

""", file=args.output)

    lexdata = dict()
    #with open(args.lexemes) as tsv_file:
    #    tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
    #                                strict=True)
    #    # probably could just read whole thing in one sweep
    #    for tsv_parts in tsv_reader:
    #        lexkey = tsv_parts['lemma'] + '_' + tsv_parts['homonym']
    #        lexdata[lexkey] = dict()
    #        for key in tsv_parts.keys():
    #            if key != 'new_para':
    #                lexdata[lexkey][key] = tsv_parts[key]
    for tsv_filename in args.lexeme_docs:
        if args.verbose:
            print("Reading from", tsv_filename)
        linecount = 0
        # for each line
        with open(tsv_filename, 'r', newline='') as tsv_file:
            tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                                        strict=True)
            prev_lemma = ''
            for tsv_parts in tsv_reader:
                linecount += 1
                if len(tsv_parts) < 2 or tsv_parts['doc'] == None:
                    print("Too few tabs on line", linecount,
                          "skipping following line completely:", file=stderr)
                    print(tsv_parts, file=stderr)
                    continue
                if '\t' in tsv_parts['lemma']:
                    print("ARGH python tsv fail on line:",
                            tsv_parts, file=stderr)
                    continue
                if tsv_parts['lemma'] != prev_lemma:
                    outfile=open(args.outdir + '/' +
                             filenamify(tsv_parts['lemma']) +
                             '.markdown', 'w')
                    prev_lemma = tsv_parts['lemma']
                    print('---', file=outfile)
                    print('layout: lexeme', file=outfile)
                    print('lexeme:', tsv_parts['lemma'], file=outfile)
                    print('---', file=outfile)
                print(file=outfile)
                print("### ", tsv_parts['lemma'], "",
                      file=outfile, end='')
                if tsv_parts['homonym'] != '1':
                    print(" (alternate reading", tsv_parts['homonym'],
                          ")", file=outfile)
                print(file=outfile)
                print(tsv_parts['doc'], file=outfile)
                print(file=outfile)
    print('''<!-- vim: set ft=markdown:-->''', file=args.output)
    exit()


if __name__ == "__main__":
    main()
