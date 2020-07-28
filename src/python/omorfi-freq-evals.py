#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test sort | uniq -c | sort -nr'd gold analysis data for faithfulness
"""


from argparse import ArgumentParser, FileType
from sys import stderr, stdout, stdin
from time import perf_counter, process_time

from omorfi import Omorfi, Token


def main():
    """Command-line interface for omorfi's sort | uniq -c tester."""
    a = ArgumentParser()
    a.add_argument('-a', '--analyser', metavar='FSAFILE', required=True,
                   help="load analyser from FSAFILE")
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
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
    a.add_argument('-O', '--no-workaround', default=False, action="store_true",
                   help="do not skip suspicious strings (that may break)")
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    try:
        if options.analyser:
            if options.verbose:
                print("reading analyser from", options.analyser)
            omorfi.load_analyser(options.analyser)
        if not options.infile:
            options.infile = stdin
            print("reading from <stdin>")
        if not options.statfile:
            options.statfile = stdout
        if not options.outfile:
            options.outfile = stdout
    except IOError:
        print("Could not process file", options.analyser, file=stderr)
        exit(2)
    # basic statistics
    covered = 0
    full_matches = 0
    lemma_matches = 0
    anal_matches = 0
    only_permuted = 0
    only_rehashed = 0
    no_matches = 0
    no_results = 0
    lines = 0
    # types
    types_covered = 0
    types_no_results = 0
    types = 0
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
        if len(surf) > 120 and not options.no_workaround:
            print("WARN: Skipping line", fields, file=stderr)
            continue
        lemma = surf
        analysis = surf
        if options.format != 'coverage':
            lemma = fields[2]
            analysis = fields[3]
        lines += freq
        types += 1
        if options.verbose:
            print(lines, '(', freq, ') ...', end='\r')
        token = Token(surf)
        # pos 1 triggers acceptable detitlecasing
        token.pos = 1
        omorfi.analyse(token)
        if token.is_oov():
            omorfi.guess(token)
        if not token.is_oov():
            covered += freq
            types_covered += 1
        else:
            no_results += freq
            types_no_results += 1
            print(freq, "OOV", surf, sep='\t', file=options.outfile)
        found_anals = False
        found_lemma = False
        rehashed = True
        permuted = True
        for anal in token.analyses:
            if options.format == 'ftb3.1':
                anal_ftb3 = ' '.join(anal.get_ftb_feats())
                lemma_ftb3 = '#'.join(anal.get_lemmas())
                # hacks ftb3:
                analysis = analysis.replace(" >>>", "")
                if analysis == anal_ftb3:
                    found_anals = True
                    permuted = False
                elif set(anal_ftb3.split()) == set(analysis.split()):
                    found_anals = True
                    print(freq, "PERMUTAHIT", analysis, anal_ftb3, sep='\t',
                          file=options.outfile)
                else:
                    print(freq, "ANALMISS", analysis, anal_ftb3, sep='\t',
                          file=options.outfile)
                if lemma == lemma_ftb3:
                    found_lemma = True
                    rehashed = False
                elif lemma.replace('#', '') == lemma_ftb3.replace('#', ''):
                    found_lemma = True
                    print(freq, "LEMMARECOMP", lemma, lemma_ftb3, sep='\t',
                          file=options.outfile)
                else:
                    print(freq, "LEMMAMISS", lemma, lemma_ftb3, sep='\t',
                          file=options.outfile)
        if options.format != 'coverage':
            if not found_anals and not found_lemma:
                no_matches += freq
                print(freq, "NOHITS!", surf, sep='\t', file=options.outfile)
            elif found_anals and found_lemma:
                full_matches += freq
            elif not found_anals:
                anal_matches += freq
                print(freq, "LEMMANOANAL", surf, sep='\t',
                      file=options.outfile)
            elif not found_lemma:
                lemma_matches += freq
                print(freq, "ANALNOLEMMA", surf, sep='\t',
                      file=options.outfile)
            else:
                print("Logical error, kill everyone")
                exit(13)
            if rehashed:
                only_rehashed += freq
            if permuted:
                only_permuted += freq
    realend = perf_counter()
    cpuend = process_time()
    print("CPU time:", cpuend - cpustart, "real time:", realend - realstart)
    print("Lines", "Covered", "OOV", sep="\t", file=options.statfile)
    print(lines, covered, lines - covered, sep="\t", file=options.statfile)
    print(lines / lines * 100 if lines != 0 else 0,
          covered / lines * 100 if lines != 0 else 0,
          (lines - covered) / lines * 100 if lines != 0 else 0,
          sep="\t", file=options.statfile)
    print("Types", "Covered", "OOV", sep="\t", file=options.statfile)
    print(types, types_covered, types - types_covered, sep="\t",
          file=options.statfile)
    print(types / types * 100 if types != 0 else 0,
          types_covered / types * 100 if types != 0 else 0,
          (types - types_covered) / types * 100 if types != 0 else 0,
          sep="\t", file=options.statfile)
    if options.format == 'ftb3.1':
        print("Lines", "Matches", "Lemma", "Anals", "Mismatch",
              "No results", sep="\t", file=options.statfile)
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
        print("Of which", "Tag permuations", "Lemma rehashing", sep='\t',
              file=options.statfile)
        print(lines / lines * 100 if lines != 0 else 0,
              only_permuted / lines * 100 if lines != 0 else 0,
              only_rehashed / lines * 100 if lines != 0 else 0, sep='\t',
              file=options.statfile)
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
