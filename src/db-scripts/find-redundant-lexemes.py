#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Analyse lexical data from input and print out those definitions which
seem redundant since there is another identical lexeme with a paradigm
class which is an extension of the given paradigm.
"""

# Author: Juha Kuokkala <juha.kuokkala@helsinki.fi> 2014

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
from collections import defaultdict
from sys import exit, stderr, stdin, stdout

# Supersets of paradigm classes
# (the list might be lacking something, e.g. adjectives & verbs)
superpara = defaultdict(lambda: "", {
    "['N_TALO']": "['N_RUIPELO']",   # KTN 1: 2
    "['N_ASU']": "['N_SEIKKAILU']",
    "['N_KÄRRY']": "['N_VEHKEILY']",
    "['N_MÖMMÖ']": "['N_JÄÄTELÖ']",
    "['N_NALLE']": "['N_EUGENE']",   # KTN 8: 2
    "['N_NISSE']": "['N_SELENE']",
    "['N_UKKO']": "['N_LEPAKKO']",   # KTN 1: 4
    "['N_YÖKKÖ']": "['N_YKSIKKÖ']",
    "['N_PUNK']": "['N_STADION']",   # KTN 5: 6
    "['N_ZEN']": "['N_BESSERWISSER']",
    "['N_RUUVI']": "['N_KANAALI']",
    "['N_TYYLI']": "['N_KEHVELI']",
    "['N_KIRJA']": "['N_KITARA']",   # KTN 9: 13
    "['N_YMPÄRYSTÄ']": "['N_HÄKKYRÄ']",
    "['N_MAKKARA']": "['N_KITARA']",   # KTN 12: 13
    "['N_SIIVILÄ']": "['N_HÄKKYRÄ']",
    "['N_VOIMA']": "['N_PROBLEEMA']",   # KTN 10: 11
    "['N_HÖPÖTTÄJÄ']": "['N_KÄPÄLÄ']",
    # "['N_MAKKARA']": "['N_PROBLEEMA']",   # KTN 12: 11
    #  "['N_SIIVILÄ']": "['N_KÄPÄLÄ']",
    "['N_POLITIIKKA']": "['N_LUSIKKA']",   # KTN 9: 14
    "['N_TIPPA']": "['N_ULAPPA']",
    "['N_MITTA']": "['N_POHATTA']",
    "['N_VAINAA']": "['N_NUGAA']",      # KTN 17: 20
    "['N_TOKEE']": "['N_PATEE']",
    "['N_LENTTEE']": "['N_BIDEE']",
    "['N_TIENOO']": "['N_TRIKOO']",
    "['N_LEIKKUU']": "['N_RAGUU']",
    "['N_HYÖTYY']": "['N_FONDYY']",
    "['N_YLÖÖ']": "['N_MILJÖÖ']",
    "['N_MAA']": "['N_NUGAA']",      # KTN 18: 20
    "['N_MATEE']": "['N_PATEE']",
    "['N_TEE']": "['N_BIDEE']",
    "['N_OOKOO']": "['N_TRIKOO']",
    "['N_PUU']": "['N_RAGUU']",
    "['N_PYY']": "['N_FONDYY']",
    "['N_KÖÖ']": "['N_MILJÖÖ']"
})


def main():
    ap = argparse.ArgumentParser(
        description="Find redundant definitions in Omorfi's lexical data")

    ap.add_argument("--input", "-i", metavar="INFILE",
                    help="read data from INFILE")
    ap.add_argument('--output', '-o', metavar="OUTFILE",
                    help="write output to OUTFILE")
    ap.add_argument('--verbose', '-v', action="store_true",
                    help="Print verbosely while processing")
    ap.add_argument("--version", "-V", action="version")
    args = ap.parse_args()

    if args.input:
        input = open(args.input, 'r', newline='')
    else:
        input = stdin

    paralist = defaultdict(list)
    for line in input:
        fields = line.strip('\n').split('\t')
        if len(fields) < 2:
            if len(fields > 0):
                if args.verbose:
                    print("Skipping too short line:", line, file=stderr)
            continue
        paralist[fields[0]].append(fields[1])
    input.close()

    redulist = list()
    for lemma, paras in paralist.items():
        for para in paras:
            if superpara[para] in paras:
                redulist.append([lemma, para])

    if args.output:
        output = open(args.output, 'w', newline='')
    else:
        output = stdout

    for lex in redulist:
        print('\t'.join(lex), file=output)

    output.close()
    exit()


if __name__ == "__main__":
    main()
