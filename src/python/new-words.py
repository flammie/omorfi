#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Insert list of words to TSV database with guessing of paradigms.
"""

# Author: Tommi A. Pirinen <flammie@iki.fi> 2009, 2011

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

import argparse
import csv
from sys import exit, stderr


def choose_from(options):
    print("x", "none of the below")
    for i, opt in enumerate(options):
        print(i, opt)
    a = input("x or " + str(range(len(options))) + ": ")
    while True:
        try:
            return options[int(a)]
        except:
            if a == 'x':
                return None
            else:
                print(a, "did not work")
        a = input("once more: ")

def is_back(s):
    if 'a' in s or 'o' in s or 'u' in s:
        return True
    else:
        return False

def guess_new_para_interactive(wordmap):
    print("What is:", wordmap)
    if not wordmap['lemma']:
        print("No guessing paras without lemmas yet")
        return 'X_IGNORE'
    s = wordmap['lemma']
    para = None
    if s.endswith('kko'):
        para = choose_from(['NOUN_UKKO', 'NOUN_LEPAKKO', 'PROPN_UKKO',
                            'PROPN_LEPAKKO', 'ADJ_KOLKKO', 'ADJ_HUPAKKO'])
    elif s.endswith('nko'):
        para = choose_from(['NOUN_RUNKO', 'PROPN_RUNKO', 'ADJ_LENKO'])
    elif s.endswith('oko'):
        para = choose_from(['NOUN_RUOKO', 'PROPN_RUOKO', 'NOUN_KOKO',
                            'PROPN_KOKO'])
    elif s.endswith('tto'):
        para = choose_from(['NOUN_HIRTTO', 'PROPN_HIRTTO'])
    if para:
        return para
    if s.endswith('ko'):
        para = choose_from(['NOUN_PELKO', 'NOUN_VIHKO', 'NOUN_TEKO',
                            'PROPN_PELKO', 'PROPN_VIHKO', 'PROPN_TEKO',
                            'ADJ_LAKO'])
    if para:
        return para
    if s.endswith('o'):
        para = choose_from(['NOUN_TALO', 'PROPN_TALO', 'ADJ_TUMMAHKO'])
    if para:
        return para
    if s.endswith('u'):
        para = choose_from(['NOUN_ASU', 'NOUN_SEIKKAILU', 'NOUN_KUNGFU',
                            'PROPN_ASU', 'PROPN_SEIKKAILU', 'PROPN_KUNGFU',
                            'ADJ_VALKAISTU'])
    if para:
        return para
    if s.endswith('y'):
        para = choose_from(['NOUN_KÄRRY', 'NOUN_VEHKEILY', 'NOUN_GAY',
                            'PROPN_KÄRRY', 'PROPN_SPOTIFY', 'PROPN_GAY',
                            'PROPN_JOCKEY', 'ADJ_HÄPÄISTY'])
    if para:
        return para
    if s.endswith('ö'):
        para = choose_from(['NOUN_MÖMMÖ', 'NOUN_HÄIRIÖ', 'NOUN_JÄÄTELÖ',
                            'PROPN_MÖMMÖ', 'PROPN_HÄIRIÖ', 'PROPN_JÄÄTELÖ'])
    if para:
        return para
    if s.endswith('aa'):
        para = choose_from(['NOUN_MAA', 'NOUN_VAINAA', 'NOUN_NUGAA',
                            'PROPN_MAA', 'PROPN_VAINAA', 'PROPN_VAINAA'])
    if para:
        return para
    if s.endswith('a'):
        para = choose_from(['NOUN_ASEMA', 'NOUN_KIRJA', 'NOUN_KITARA',
                            'NOUN_MAKKARA', 'NOUN_PROBLEEMA', 'NOUN_VOIMA',
                            'PROPN_ASEMA', 'PROPN_KIRJA',
                            'PROPN_MINERVA', 'PROPN_KITARA', 'PROPN_BOTSWANA',
                            'PROPN_LAHELMA', 'PROPN_MAKKARA', 'PROPN_PROBLEEMA'
                            'PROPN_VOIMA', 'PROPN_WADA', 'PROPN_FIFA'])
    if para:
        return para
    if s.endswith('i'):
        if is_back(s):
            para = choose_from(['NOUN_RUUVI', 'NOUN_KANAALI', 'NOUN_ONNI',
                                'NOUN_PROTOLYYSI', 'NOUN_PYRAMIDI', 'NOUN_ORI'
                                'NOUN_RUUHI', 'NOUN_TULI', 'NOUN_SAVI',
                                'NOUN_SANKARI', 'NOUN_AAMUKAKSI',
                                'PROPN_RUUVI', 'PROPN_KANAALI', 'PROPN_ONNI',
                                'PROPN_HKI', 'PROPN_RUUHI', 'PROPN_TULI',
                                'PROPN_SAVI'])
    if para:
        return para
    if s.endswith('ee'):
        if is_back(s):
            para = choose_from(['NOUN_MATEE', 'NOUN_PATEE', 'NOUN_TOKEE',
                                'PROPN_PATEE', 'PROPN_TOKEE'])
        else:
            para = choose_from(['NOUN_TEE',
                                'PROPN_TEE', 'PROPN_LENTTEE'])
    if para:
        return para
    if s.endswith('e'):
        if is_back(s):
            para = choose_from(['NOUN_NALLE', 'NOUN_ASTE', 'NOUN_ZOMBIE',
                                'NOUN_BRASSERIE', 'NOUN_REGGAE', 'ADJ_AHNE'
                                'ADJ_OIKEE', 'ADJ_TOOPE', 'PROPN_ASTE',
                                'PROPN_NALLE', 'PROPN_EUGENE',
                                'PROPN_ZOMBIE', 'PROPN_BRASSERIE',
                                'PROPN_FONDUE'])
        else:
            para = choose_from(['NOUN_NISSE', 'NOUN_PISTE', 'PROPN_BERNIE',
                                'PROPN_BRIE', 'PROPN_NISSE',
                                'PROPN_PISTE', 'PROPN_SELENE',
                                'PROPN_BRIE'])
    if para:
        return para
    consonants = "bcdfghjklmnpqrstvwxz"
    for c in consonants:
        if s.endswith(c):
            if is_back(s):
                para = choose_from(['NOUN_PUNK', 'NOUN_STADION', 'PROPN_PUNK',
                                    'PROPN_STADION'])
            else:
                para = choose_from(['NOUN_ZEN', 'NOUN_BESSERWISSER',
                                    'PROPN_ZEN', 'PROPN_BESSERWISSER'])
    if para:
        return para
    else:
        print("conclusion: not-a-word (new para??)")
        para = choose_from(['X_IGNORE'])
        if para:
            return 'X_IGNORE'
        else:
            return None

def main():
    ap = argparse.ArgumentParser(
        description="Prepare list of words into TSV format for merge")

    ap.add_argument("--quiet", "-q", action="store_false", dest="verbose",
                    default=False,
                    help="do not print output to stdout while processing")
    ap.add_argument("--verbose", "-v", action="store_true", default=False,
                    help="print each step to stdout while processing")
    ap.add_argument("--version", "-V", action="version")
    ap.add_argument("--input", "-i", required=True,dest='infilename',
                    metavar="IFILE", help="read dictionary data from IFILE")
    ap.add_argument("--output", "-o", action="store", required=True,
                    dest='outfilename',
                    metavar="OFILE",
                    help="write resulting data to OFILE")
    ap.add_argument("--fields", "-f", action="store", type=int, default=3,
                    metavar="N", help="read N fields from master")
    ap.add_argument("--separator", "-s", action="store", default="\t",
                    metavar="SEP", help="use SEP as separator")
    ap.add_argument("--comment", "-C", action="append", default=["#"],
                    metavar="COMMENT", help="skip lines starting with COMMENT that"
                    "do not have SEPs")
    ap.add_argument("--strip", "-S", action="store",
                    metavar="STRIP", help="strip STRIP from fields before using")
    ap.add_argument("--ignore-errors", "-I", action="store_true", default=False,
                    help="silently ignore references to entries missing from master file")
    args = ap.parse_args()

    if args.strip == '"' or args.strip == "'":
        quoting = csv.QUOTE_ALL
    else:
        quoting = csv.QUOTE_NONE
    output = open(args.outfilename, 'w')
    linecount = 0
    entry_count = 0
    lexdata = dict()
    print("lemma", "homonym", "new_para", "origin", sep='\t', file=output)
    with open(args.infilename, 'r', newline='') as tsv_file:
        if args.verbose:
            print("Reading dictionary from", args.infilename)
        tsv_reader = csv.DictReader(tsv_file, delimiter=args.separator,
                                    strict=True)
        for tsv_parts in tsv_reader:
            if 'lemma' not in tsv_parts:
                print("Need at least a lemma column...:", tsv_parts)
                exit(1)
            if 'new_para' not in tsv_parts:
                tsv_parts['new_para'] = guess_new_para_interactive(tsv_parts)
                if not tsv_parts['new_para']:
                    continue
            if 'homonym' not in tsv_parts:
                tsv_parts['homonym'] = tsv_parts['new_para'].split("_")[0]
            if 'origin' not in tsv_parts:
                tsv_parts['origin'] = 'omorfi'
            entry_count += 1
            print(tsv_parts['lemma'], tsv_parts['homonym'],
                  tsv_parts['new_para'], tsv_parts['origin'],
                  sep='\t', file=output)
        if args.verbose:
            print("\n", entry_count, "entries in database")
    exit()


if __name__ == "__main__":
    main()
