#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test omorfi - unimorph compatibility
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
    a.add_argument('-t', '--threshold', metavar="THOLD", default=99,
                   help="if coverage is less than THOLD exit with error")
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
    no_matches = 0
    no_results = 0
    only_permuted = 0
    accfails = 0
    lines = 0
    # for make check target
    threshold = options.threshold
    realstart = perf_counter()
    cpustart = process_time()
    for line in options.infile:
        fields = line.strip().split('\t')
        if len(fields) < 3:
            print("ERROR: Skipping line", fields, file=stderr)
            continue
        if ' ' in fields[1] or ' ' in fields[0]:
            continue
        lines += 1
        if options.verbose and lines % 1000 == 0:
            print(lines, '...')
        lemma = fields[0]
        surf = fields[1]
        unimorph = fields[2].replace('ACC', 'NOM').replace('GEADJ', 'GEN')
        token = Token(surf)
        omorfi.analyse(token)
        if not token.is_oov():
            covered += 1
        else:
            no_results += 1
            print(1, "OOV", surf, sep='\t', file=options.outfile)
        found_anals = False
        found_lemma = False
        permuted = True
        accfail = False
        for anal in token.analyses:
            analhyp = anal.printable_unimorph()
            lemmahyp = ''.join(anal.get_lemmas())
            if analhyp == unimorph:
                found_anals = True
                permuted = False
            elif set(analhyp.split(';')) == set(unimorph.split(';')):
                found_anals = True
                # print("PERMUTAHIT", analhyp, unimorph, sep='\t',
                #      file=options.outfile)
            else:
                pass
                # print("ANALMISS", analhyp, unimorph, sep='\t',
                #      file=options.outfile)
            if lemma == lemmahyp:
                found_lemma = True
            else:
                pass
                # print("LEMMAMISS", lemmahyp, lemma, sep='\t',
                #      file=options.outfile)
        if not found_anals and not found_lemma:
            no_matches += 1
            print("NOHITS!", surf, lemma, unimorph,
                  [a.printable_unimorph() for a in token.analyses], sep='\t',
                  file=options.outfile)
        elif found_anals and found_lemma:
            full_matches += 1
        elif not found_anals:
            anal_matches += 1
            print("LEMMANOANAL", surf, unimorph,
                  [a.printable_unimorph() for a in token.analyses], sep='\t',
                  file=options.outfile)
        elif not found_lemma:
            lemma_matches += 1
            print("ANALNOLEMMA", surf, lemma,
                  [a.get_lemmas() for a in token.analyses], sep='\t',
                  file=options.outfile)
        else:
            print("Logical error, kill everyone")
            exit(13)
        if permuted:
            only_permuted += 1
        if accfail:
            accfails += 1
    realend = perf_counter()
    cpuend = process_time()
    print("CPU time:", cpuend - cpustart, "real time:", realend - realstart)
    if lines == 0:
        print("Needs more than 0 lines to determine something",
              file=stderr)
        exit(2)
    print("Lines", "Covered", "OOV", sep="\t", file=options.statfile)
    print(lines, covered, lines - covered, sep="\t", file=options.statfile)
    print(lines / lines * 100 if lines != 0 else 0,
          covered / lines * 100 if lines != 0 else 0,
          (lines - covered) / lines * 100 if lines != 0 else 0,
          sep="\t", file=options.statfile)
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
          sep="% \t", file=options.statfile)
    print("Of which", "Tag permuations", sep='\t',
          file=options.statfile)
    print(lines / lines * 100 if lines != 0 else 0,
          only_permuted / lines * 100 if lines != 0 else 0, sep='\t',
          file=options.statfile)
    if full_matches / lines * 100 <= int(options.threshold):
        print("needs to have", threshold, "% matches to pass regress test\n",
              "please examine", options.outfile.name, "for regressions",
              file=stderr)
        exit(1)
    elif covered / lines * 100 <= int(options.threshold):
        print("needs to have", threshold, "% coverage to pass regress test\n",
              "please examine", options.outfile.name, "for regressions",
              file=stderr)
        exit(1)
    else:
        exit(0)


if __name__ == "__main__":
    main()
