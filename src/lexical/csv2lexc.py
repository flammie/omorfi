#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
This script converts Finnish TSV-formatted lexicon to lexc format, given that
they contain at least following information for each word (i.e. at least two
fields per line):
    * the word lemma or the dictionary form
    * the word inflection classification in one of the known formats
The TSV-formatted data can be joined with arbitrary amount of extra fields to
store additional data. The additional data needs to be in name=value format.
"""


# Author: Tommi A Pirinen <tommi.pirinen@helsinki.fi> 2009, 2011

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

from format_output import format_lexc, format_multichars_lexc, \
        format_root_lexicon, format_continuation_lexc
from parse_csv_data import parse_from_tsv

# standard UI stuff

def main():
    # defaults
    pos_files = {"ADJECTIVE": 'adjectives.lexc', 
            "NOUN": 'nouns.lexc',
            "VERB": 'verbs.lexc',
            "PARTICLE": 'particles.lexc',
            "ACRONYM": 'acronyms.lexc',
            "PRONOUN": 'pronouns.lexc',
            "NUMERAL": 'numerals.lexc'}
    stubfiles = dict()
    stempartfiles = dict()
    inflectfiles = dict()
    curr_lexicon = dict()
    # initialise argument parser
    ap = argparse.ArgumentParser(description="Convert Finnish dictionary TSV data into xerox/HFST lexc format")
    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
            default=False,
            help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
            help="print each step to stdout while processing")
    ap.add_argument("--master", "-m", action="append", required=True, type=open,
            metavar="MFILE", help="read lexical roots from MFILEs")
    ap.add_argument("--stemparts", "-p", action="append", required=True,
            type=open,
            metavar="SPFILE", help="read lexical roots from SPFILEs")
    ap.add_argument("--inflection", "-i", action="append", required=True,
            type=open,
            metavar="INFFILE", help="read inflection from INFFILEs")
    ap.add_argument("--exclude-pos", "-x", action="append",
            metavar="XPOS",
            help="exclude all XPOS parts of speech from generation")
    ap.add_argument("--include-lemmas", "-I", action="append", type=open,
            metavar="ILFILE", help="read lemmas to include from ILFILE")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--stubdir", "-s", action="store", required=True, type=str,
            metavar="SDIR", help="write stubs to SDIR")
    ap.add_argument("--stempartdir", "-S", action="store", required=True,
            type=str, metavar="SPDIR", help="write stemparts to SPDIR")
    ap.add_argument("--inflectiondir", "-X", action="store", required=True,
            type=str, metavar="IXDIR", help="write inflections to IXDIR")
    ap.add_argument("--root", "-R", type=argparse.FileType("w"),
            metavar="ROOTFILE",
            help="write multichars and roto lexicon to ROOTFILE")
    ap.add_argument("--one-file", "-1", type=argparse.FileType("w"),
            metavar="ONEFILE")
    def FormatArgType(v):
        baseformats = ["omor", "omor-short", "ktnkav", "apertium", "giellatekno", "ftb3"]
        extras = ["propers", "semantics", "taggerhacks", "no-segments"]
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
    # check args
    lemmas = []
    if args.include_lemmas:
        for lemma_file in args.include_lemmas:
            if args.verbose:
                print("including only lemmas from", lemma_file.name);
            lemmas += lemma_file.readlines()
            lemma_file.close()
    if not args.exclude_pos:
        args.exclude_pos = []
    # setup files
    if args.one_file:
        if args.verbose: 
            print("Writing everything to", args.one_file)
        args.root = args.one_file
    for (pos, pos_filename) in pos_files.items():
        if not pos in args.exclude_pos:
            if args.one_file:
                stubfiles[pos] = args.one_file
            else:
                if args.verbose: 
                    print("Writing", pos, "stubs to", args.stubdir + "/"
                            + pos_filename)
                stubfiles[pos] = open(args.stubdir + "/" + pos_filename, "w")
    for (pos, pos_filename) in pos_files.items():
        if not pos in args.exclude_pos:
            if args.one_file:
                stempartfiles[pos] = args.one_file
            else:
                if args.verbose: 
                    print("Writing", pos, "stemparts to", args.stempartdir + "/"
                            + pos_filename)
                stempartfiles[pos] = open(args.stempartdir + "/" + pos_filename,
                        "w")
    for (pos, pos_filename) in pos_files.items():
        if not pos in args.exclude_pos:
            if args.one_file:
                inflectfiles[pos] = args.one_file
            else:
                if args.verbose: 
                    print("Writing", pos, "inflects to", args.inflectiondir +
                            "/" + pos_filename)
                inflectfiles[pos] = open(args.inflectiondir + "/" +
                        pos_filename, "w")
    if args.exclude_pos:
        if args.verbose:
            print("Not writing closed parts-of-speech data in", 
                    ",".join(args.exclude_pos))
    # print definitions to rootfile
    if args.verbose:
        print("Creating Multichar_Symbols and Root")
    print(format_multichars_lexc(args.format), file=args.root)
    print(format_root_lexicon(args.format), file=args.root)
    # read from csv files
    for tsv_file in args.master:
        if args.verbose:
            print("Reading from", tsv_file.name)
        tsv_line = tsv_file.readline()
        linecount = 0
        lexicon_count = 0
        entry_count = 0
        for (pos, pos_filename) in pos_files.items():
            if not pos in args.exclude_pos:
                print("! Omorfi stubs", pos, "generated from", tsv_file.name,
                      file=stubfiles[pos])
                print("! date:", strftime("%Y-%m-%d %H:%M:%S+%Z"), 
                    file=stubfiles[pos])
                print("! params: ", ' '.join(argv), file=stubfiles[pos])
                curr_lexicon[pos] = ""
                print("\nLEXICON ", pos, end="\n\n", file=stubfiles[pos])
        # for each line
        while tsv_line:
            linecount += 1
            if args.verbose and (linecount % 10000 == 0):
                print(linecount, "...", sep='')
            tsv_line = tsv_line.strip()
            if tsv_line.startswith("#") or tsv_line.startswith("!") or tsv_line == "":
                # comment line
                tsv_line = tsv_file.readline()
                continue
            tsv_parts = []
            if tsv_line.count('\t') >= 18:
                tsv_parts = tsv_line.split("\t")
            else:
                print("Too few tabs on line", linecount, 
                    "skipping following line completely:", file=stderr)
                print(tsv_line, file=stderr)
                tsv_line = tsv_file.readline()
                continue
            if tsv_parts[-1] == '<- HEADERS':
                # skip header line
                tsv_line = tsv_file.readline()
                continue
            # read data from database
            wordmap = dict()
            wordmap = parse_from_tsv(wordmap, tsv_parts)
            # exclusions
            if args.exclude_pos:
                if wordmap['pos'] in args.exclude_pos:
                    tsv_line = tsv_file.readline()
                    continue
            if args.include_lemmas:
                if wordmap['lemma'] not in lemmas:
                    tsv_line = tsv_file.readline()
                    continue
            # format output
            print(format_lexc(wordmap, args.format), 
                  file=stubfiles[wordmap['pos']])
            tsv_line = tsv_file.readline()
    # print stem parts
    for tsv_file in args.stemparts:
        if args.verbose:
            print("Reading from", tsv_file.name)
        tsv_line = tsv_file.readline()
        linecount = 0
        for (pos, pos_filename) in pos_files.items():
            if not pos in args.exclude_pos:
                print("! Omorfi stemparts", pos, "generated from", tsv_file.name,
                      file=stempartfiles[pos])
                print("! date:", strftime("%Y-%m-%d %H:%M:%S+%Z"), 
                    file=stempartfiles[pos])
                print("! params: ", ' '.join(argv), file=stempartfiles[pos])
                curr_lexicon[pos] = ""
        # for each line
        while tsv_line:
            linecount += 1
            tsv_line = tsv_line.strip()
            if tsv_line.startswith("#") or tsv_line.startswith("!") or tsv_line == "":
                # comment line
                tsv_line = tsv_file.readline()
                continue
            tsv_parts = []
            if tsv_line.count('\t') >= 3:
                tsv_parts = tsv_line.split("\t")
            else:
                print("Too few tabs on line", linecount, 
                    "skipping following line completely:", file=stderr)
                print(tsv_line, file=stderr)
                tsv_line = tsv_file.readline()
                continue
            if tsv_parts[-1] == '#<- HEADERS':
                # skip header line
                tsv_line = tsv_file.readline()
                continue
            if tsv_parts[0].startswith('A_'):
                pos = 'ADJECTIVE'
            elif tsv_parts[0].startswith('N_'):
                pos = 'NOUN'
            elif tsv_parts[0].startswith('V_'):
                pos = 'VERB'
            elif tsv_parts[0].startswith('ACRO_'):
                pos = 'ACRONYM'
            elif tsv_parts[0].startswith('NUM_'):
                pos = 'NUMERAL'
            elif tsv_parts[0].startswith('DIGITS_'):
                pos = 'NUMERAL'
            elif tsv_parts[0].startswith('ADV_'):
                pos = 'PARTICLE'
            elif tsv_parts[0].startswith('PRON_'):
                pos = 'PRONOUN'
            else:
                print("Cannot deduce pos from incoming cont:", tsv_parts[0])
                pos = 'PARTICLE'
            if pos in args.exclude_pos:
                tsv_line = tsv_file.readline()
                continue
            # format output
            if curr_lexicon[pos] != tsv_parts[0]:
                print("\nLEXICON", tsv_parts[0], end="\n\n",
                        file=stempartfiles[pos])
                curr_lexicon[pos] = tsv_parts[0]
            print(format_continuation_lexc(tsv_parts, args.format), 
                  file=stempartfiles[pos])
            tsv_line = tsv_file.readline()
    # print inflections
    for tsv_file in args.inflection:
        if args.verbose:
            print("Reading from", tsv_file.name)
        tsv_line = tsv_file.readline()
        linecount = 0
        for (pos, pos_filename) in pos_files.items():
            if not pos in args.exclude_pos:
                print("! Omorfi inflects", pos, "generated from", tsv_file.name,
                      file=inflectfiles[pos])
                print("! date:", strftime("%Y-%m-%d %H:%M:%S+%Z"), 
                    file=inflectfiles[pos])
                print("! params: ", ' '.join(argv), file=inflectfiles[pos])
                curr_lexicon[pos] = ""
        # for each line
        while tsv_line:
            linecount += 1
            tsv_line = tsv_line.strip()
            if tsv_line.startswith("#") or tsv_line.startswith("!") or tsv_line == "":
                # comment line
                tsv_line = tsv_file.readline()
                continue
            tsv_parts = []
            if tsv_line.count('\t') >= 3:
                tsv_parts = tsv_line.split("\t")
            else:
                print("Too few tabs on line", linecount, 
                    "skipping following line completely:", file=stderr)
                print(tsv_line, file=stderr)
                tsv_line = tsv_file.readline()
                continue
            if tsv_parts[-1] == '#<- HEADERS':
                # skip header line
                tsv_line = tsv_file.readline()
                continue
            if tsv_parts[0].startswith('A_'):
                pos = 'ADJECTIVE'
            elif tsv_parts[0].startswith('N_'):
                pos = 'NOUN'
            elif tsv_parts[0].startswith('V_'):
                pos = 'VERB'
            elif tsv_parts[0].startswith('ACRO_'):
                pos = 'ACRONYM'
            elif tsv_parts[0].startswith('NUM_'):
                pos = 'NUMERAL'
            elif tsv_parts[0].startswith('DIGITS_'):
                pos = 'NUMERAL'
            elif tsv_parts[0].startswith('ADV_'):
                pos = 'PARTICLE'
            elif tsv_parts[0].startswith('ADP_'):
                pos = 'PARTICLE'
            elif tsv_parts[0].startswith('PCLE_'):
                pos = 'PARTICLE'
            elif tsv_parts[0].startswith('PRON_'):
                pos = 'PRONOUN'
            else:
                print("Cannot deduce pos from incoming cont:", tsv_parts[0])
                pos = 'PARTICLE'
            if pos in args.exclude_pos:
                tsv_line = tsv_file.readline()
                continue
            # format output
            if curr_lexicon[pos] != tsv_parts[0]:
                print("\nLEXICON", tsv_parts[0], end="\n\n",
                        file=inflectfiles[pos])
                curr_lexicon[pos] = tsv_parts[0]
            print(format_continuation_lexc(tsv_parts, args.format), 
                  file=inflectfiles[pos])
            tsv_line = tsv_file.readline()
    exit(0)


if __name__ == "__main__":
    main()

