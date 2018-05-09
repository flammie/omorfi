#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test sort | uniq -c | sort -nr'd gold analysis data for faithfulness
"""


from argparse import ArgumentParser, FileType
from sys import stderr, stdout
from time import perf_counter, process_time

from omorfi.omorfi import Omorfi
from omorfi.token import is_tokenlist_oov, format_feats_ftb, get_lemmas

def main():
    a = ArgumentParser()
    a.add_argument('-a', '--analyser', metavar='FSAFILE', required=True,
                   help="load analyser from FSAFILE")
    a.add_argument('-i', '--input', metavar="INFILE", type=open, required=True,
                   dest="infile", help="source of analysis data")
    a.add_argument('-o', '--output', metavar="OUTFILE",
                   type=FileType('w'),
                   dest="outfile", help="log outputs to OUTFILE")
    a.add_argument('-X', '--statistics', metavar="STATFILE",
                   type=FileType('w'),
                   dest="statfile", help="statistics")
    a.add_argument('-v', '--verbose', action="store_true", default=False,
                   help="Print verbosely while processing")
    a.add_argument('-C', '--no-casing', action="store_true", default=False,
                   help="Do not try to recase input and output when matching")
    a.add_argument('-f', '--format', metavar="FORMAT",
                   help="use FORMAT formatter to compare analyses",
                   choices=["coverage", "ftb3.1"], default="coverage")
    a.add_argument('-c', '--count', metavar="FREQ", default=0,
                   help="test only word-forms with frequency higher than FREQ")
    a.add_argument('-t', '--threshold', metavar="THOLD", default=99,
                   help="if coverage is less than THOLD exit with error")
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    try:
        if options.analyser:
            if options.verbose:
                print("reading analyser from", options.analyser)
            omorfi.load_analyser(options.analyser)
        if not options.statfile:
            options.statfile = stdout
    except IOError:
        print("Could not process file", options.analyser, file=stderr)
        exit(2)
    # basic statistics
    covered = 0
    full_matches = 0
    lemma_matches = 0
    anal_matches = 0
    no_matches = 0
    no_results = 0
    lines = 0
    # for make check target
    threshold = options.threshold
    realstart = perf_counter()
    cpustart = process_time()
    for line in options.infile:
        fields = line.strip().replace(' ', '\t', 1).split('\t')
        if len(fields) < 2:
            print("ERROR: Skipping line", fields, file=stderr)
            continue
        freq = int(fields[0])
        if freq < int(options.count):
            break
        surf = fields[1]
        lemma = surf
        analysis = surf
        if options.format != 'coverage':
            lemma = fields[2]
            analysis = fields[3]
        lines += freq
        if options.verbose:
            print(lines, '(', freq, ') ...', end='\r')
        anals = omorfi.analyse(surf)
        if not is_tokenlist_oov(anals):
            covered += freq
        else:
            no_results += freq
            print("OOV", surf, sep='\t', file=options.outfile)
        found_anals = False
        found_lemma = False
        for anal in anals:
            if options.format == 'ftb3.1':
                anal_ftb3 = format_feats_ftb(anal)
                lemma_ftb3 = '#'.join(get_lemmas(anal))
                if analysis == anal_ftb3:
                    found_anals = True
                    print("ANALHIT", analysis, anal_ftb3, file=options.outfile)
                elif set(anal_ftb3.split()) == set(analysis.split()):
                    found_anals = True
                    print("PERMUTAHIT", analysis, anal_ftb3, file=options.outfile)
                else:
                    print("ANALMISS", analysis, anal_ftb3, file=options.outfile)
                if lemma == lemma_ftb3:
                    found_lemma = True
                    print("LEMMAHIT", lemma, lemma_ftb3, file=options.outfile)
                else:
                    print("LEMMAMISS", lemma, lemma_ftb3, file=options.outfile)
        if options.format != 'coverage':
            if not found_anals and not found_lemma:
                no_matches += freq
                print("MISS", surf, sep='\t', file=options.outfile)
            elif found_anals and found_lemma:
                print("HIT", surf, sep='\t', file=options.outfile)
                full_matches += freq
            elif not found_anals:
                anal_matches += freq
                print("LEMMANOANAL", surf, sep='\t', file=options.outfile)
            elif not found_lemma:
                lemma_matches += freq
                print("ANALNOLEMMA", surf, sep='\t', file=options.outfile)
            else:
                print("Logical error, kill everyone")
                exit(13)
    realend = perf_counter()
    cpuend = process_time()
    print("CPU time:", cpuend - cpustart, "real time:", realend - realstart)
    print("Lines", "Covered", "OOV", sep="\t", file=options.statfile)
    print(lines, covered, lines-covered, sep="\t", file=options.statfile)
    print(lines / lines * 100 if lines != 0 else 0,
          covered / lines * 100 if lines != 0 else 0,
          (lines-covered) / lines * 100 if lines != 0 else 0,
          sep="\t", file=options.statfile)
    if options.format == 'ftb3.1':
        print("Lines", "Matches", "Lemma", "Anals", "Mismatch", "No results", sep="\t",
              file=options.statfile)
        print(lines, full_matches, lemma_matches, anal_matches, no_matches,
              no_results,
              sep="\t", file=options.statfile)
        print(lines / lines * 100 if lines != 0 else 0,
              full_matches / lines * 100 if lines != 0 else 0,
              lemma_matches / lines * 100 if lines != 0 else 0,
              anal_matches / lines * 100 if lines != 0 else 0,
              no_matches / lines * 100 if lines != 0 else 0,
              no_results / lines * 100 if lines != 0 else 0,
              sep="\t", file=options.statfile)
    if lines == 0:
        print("Needs more than 0 lines to determine something",
              file=stderr)
        exit(2)
    elif options.format == 'ftb3.1' and \
            (full_matches / lines * 100 <= int(options.threshold)):
        print("needs to have", threshold, "% matches to pass regress test\n",
              "please examine", options.outfile.name, "for regressions",
              file=stderr)
        exit(1)
    elif options.format == 'coverage' and \
            (covered / lines * 100 <= int(options.threshold)):
        print("needs to have", threshold, "% coverage to pass regress test\n",
              "please examine", options.outfile.name, "for regressions",
              file=stderr)
        exit(1)
    else:
        exit(0)


if __name__ == "__main__":
    main()
