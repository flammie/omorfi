#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FTB test
"""


from omorfi import Omorfi
from convert_tag_format import convert_omor_string
from argparse import ArgumentParser, FileType

from sys import stderr, stdin, stdout

import re

def main():
    print("""Please note that the licence of FTC does not allow you to do much
    with the results or anything, other than including approximate numbers of
    recall for scientific purposes. Please do not look at the differences or
    do any processing with any of the data since it will automatically make
    your versions of all your future work on this or any other analysers of
    the Finnish language illegal and other bad things.""", file=stderr)
    password = "YES I HAVE READ THE TEXT ABOVE AND UNDERSTAND IT"
    userpass = input("Write '%s': " % ( password ))
    if userpass != password:
        print("You have chosen not to use badly licenced FTC data", file=stderr)
        exit(2)
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSADIR', required=True,
            help="Location of omorfi automata")
    a.add_argument('-i', '--input', metavar="INFILE", type=open, required=True,
            dest="infile", help="source of analysis data")
    a.add_argument('-o', '--output', metavar="OUTFILE", required=True,
            type=FileType('w'),
            dest="outfile", help="result file")
    a.add_argument('-X', '--statistics', metavar="STATFILE",
            type=FileType('w'),
            dest="statfile", help="statistics")
    options = a.parse_args()
    omorfi = Omorfi()
    omorfi.load_from_dir(options.fsa)
    if not options.statfile:
        options.statfile = stdout
    # basic statistics
    full_matches = 0
    lemma_matches = 0
    anal_matches = 0
    no_matches = 0
    no_results = 0
    lines = 0
    # known bugs by type
    deduct_forgn = 0
    deduct_advposman = 0
    deduct_oliprt = 0
    # known bugs by statistic to deduct
    deduct_lemma = 0
    deduct_anal = 0
    deduct_matches = 0
    deduct_results = 0
    # for make check target
    threshold = 0
    for line in options.infile:
        if not '<w lemma' in line or not 'msd=' in line:
            continue
        matches = re.search('<w.*lemma="([^"]*).*msd="([^"]*)".*>([^<]*)</w>',
                line)
        if not matches:
            print("ERROR: Skipping line", line, file=stderr)
            continue
        lines += 1
        if lines % 100000 == 0:
            print(lines, "...", file=stderr)
        ftcsurf = matches.group(3)
        ftclemma = matches.group(1)
        ftcanals = matches.group(2)
        omors = omorfi.analyse(ftcsurf)
        anals = []
        for omor in omors:
            anals.append(convert_omor_string(omor.output, 'ftc'))
        found_anals = False
        found_lemma = False
        print_in = True
        for anal in anals:
            if ftcanals in anal:
                found_anals = True
            if ftclemma in anal:
                found_lemma = True
        if len(anals) == 0:
            print_in = False
            no_results += 1
            print("NORESULTS:", ftcsurf, ftclemma, ftcanals, sep="\t",
                    file=options.outfile)
        elif not found_anals and not found_lemma:
            no_matches += 1
            print("NOMATCH:", ftcsurf, ftclemma, ftcanals, sep="\t", end="\t",
                    file=options.outfile)
        elif not found_anals:
            lemma_matches += 1
            print("NOANALMATCH:", ftcsurf, ftcanals, sep="\t", end="\t",
                    file=options.outfile)
        elif not found_lemma:
            anal_matches += 1
            print("NOLEMMAMATCH:", ftcsurf, ftclemma, sep="\t", end="\t",
                    file=options.outfile)
        else:
            full_matches += 1
            print_in = False
        if print_in:
            print(":IN:", end="\t", file=options.outfile)
            for anal in anals:
                print(anal, end='\t', file=options.outfile)
            print(file=options.outfile)
    print("Lines", "Matches", "Lemma", "Anals", "Mismatch", "No results", sep="\t",
            file=options.statfile)
    print(lines, full_matches, lemma_matches, anal_matches, no_matches,
            no_results,
            sep="\t", file=options.statfile)
    print(lines / lines * 100, full_matches / lines * 100,
            lemma_matches / lines * 100, anal_matches / lines * 100,
            no_matches / lines * 100, no_results / lines * 100,
            sep="\t", file=options.statfile)
    if (full_matches / lines * 100 < threshold):
        print("needs to have", threshold, "% matches to pass regress test\n",
                "please examine", options.outfile.name, "for regressions",
                file=stderr)
        exit(1)
    else:
        exit(0)

if __name__ == "__main__":
    main()
