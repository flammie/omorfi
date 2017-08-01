#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test sort | uniq -c | sort -nr'd gold analysis data for faithfulness
"""


from argparse import ArgumentParser, FileType
from sys import stderr, stdout
from time import perf_counter, process_time

import libhfst


def main():
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSAFILE', required=True,
                   help="HFST's optimised lookup binary data for the transducer to be applied")
    a.add_argument('-i', '--input', metavar="INFILE", type=open, required=True,
                   dest="infile", help="source of analysis data")
    a.add_argument('-o', '--output', metavar="OUTFILE", required=True,
                   type=FileType('w'),
                   dest="outfile", help="result file")
    a.add_argument('-X', '--statistics', metavar="STATFILE",
                   type=FileType('w'),
                   dest="statfile", help="statistics")
    a.add_argument('-v', '--verbose', action="store_true", default=False,
                   help="Print verbosely while processing")
    a.add_argument('-C', '--no-casing', action="store_true", default=False,
                   help="Do not try to recase input and output when matching")
    a.add_argument('-a', '--additional-mapping', default="", metavar="MAP",
                   help="Also try using MAP to match analyses and lemmas",
                   choices=["ftb3.1", ""])
    a.add_argument('-c', '--count', metavar="FREQ", default=0,
                   help="test only word-forms with frequency higher than FREQ")
    options = a.parse_args()
    his = libhfst.HfstInputStream(options.fsa)
    omorfi = his.read()
    if not options.statfile:
        options.statfile = stdout
    # basic statistics
    full_matches = 0
    lemma_matches = 0
    anal_matches = 0
    no_matches = 0
    no_results = 0
    lines = 0
    # known bugs by type (FTB 3.1)
    deduct_forgn = 0
    deduct_advposman = 0
    deduct_oliprt = 0
    deduct_abbr_prop = 0
    deduct_unkwn = 0
    # known bugs by statistic to deduct (all)
    deduct_lemma = 0
    deduct_matches = 0
    deduct_results = 0
    # for make check target
    threshold = 90
    realstart = perf_counter()
    cpustart = process_time()
    for line in options.infile:
        fields = line.strip().replace(' ', '\t', 1).split('\t')
        if len(fields) < 4:
            print("ERROR: Skipping line", fields, file=stderr)
            continue
        freq = int(fields[0])
        if freq < int(options.count):
            break
        surf = fields[1]
        lemma = fields[2]
        analysis = fields[3]
        lines += freq
        if options.verbose:
            print(lines, '(', freq, ') ...', end='\r')
        anals = omorfi.lookup(surf)
        if not options.no_casing:
            if surf[0].isupper():
                anals += omorfi.lookup(surf[0].lower() + surf[1:])
            if surf.isupper():
                anals += omorfi.lookup(surf.lower())
            if surf.isupper():
                anals += omorfi.lookup(surf[0] + surf[1:].lower())
        found_anals = False
        found_lemma = False
        print_in = True
        for anal in anals:
            if analysis in anal[0]:
                found_anals = True
            if lemma in anal[0]:
                found_lemma = True
            if not options.no_casing:
                if lemma.lower() in anal[0]:
                    found_lemma = True
                elif lemma.upper() in anal[0]:
                    found_lemma = True
        if len(anals) == 0:
            print_in = False
            no_results += freq
            if options.additional_mapping == "ftb3.1":
                if 'Forgn' in analysis:
                    deduct_forgn += freq
                    deduct_results += freq
                    print_in = False
                elif 'Unkwn' in analysis:
                    deduct_unkwn += freq
                    deduct_results += freq
                    print_in = False
                else:
                    print("NORESULTS:", freq, surf, lemma, anals, sep="\t",
                          file=options.outfile)
                    if options.verbose:
                        print("?", end='', file=stderr)
            else:
                print("NORESULTS:", freq, surf, lemma, anals, sep="\t",
                      file=options.outfile)
                if options.verbose:
                    print("?", end='', file=stderr)
        elif not found_anals and not found_lemma:
            no_matches += freq
            if options.additional_mapping == "ftb3.1":
                if 'Adv Pos Man' in analysis:
                    deduct_advposman += freq
                    deduct_matches += freq
                    print_in = False
                elif 'Unkwn' in analysis:
                    deduct_unkwn += 1
                    deduct_matches += 1
                    print_in = False
                else:
                    print("NOMATCH:", freq, surf, lemma + " " + analysis, sep="\t", end="\t",
                          file=options.outfile)
                    if options.verbose:
                        print("!", end='', file=stderr)
            else:
                print("NOMATCH:", freq, surf, lemma + " " + analysis, sep="\t", end="\t",
                      file=options.outfile)
                if options.verbose:
                    print("!", end='', file=stderr)
        elif not found_anals:
            lemma_matches += freq
            if options.additional_mapping == "ftb3.1":
                if 'Adv Pos Man' in analysis:
                    deduct_advposman += freq
                    deduct_lemma += freq
                    print_in = False
                elif 'V Prt Act' in analysis and surf.startswith('oli'):
                    deduct_oliprt += freq
                    deduct_lemma += freq
                    print_in = False
                elif 'Forgn' in analysis:
                    deduct_forgn += freq
                    deduct_lemma += freq
                    print_in = False
                elif 'Abbr' in analysis:
                    propfail = False
                    for anal in anals:
                        if 'Abbr Prop' in anal[0]:
                            propfail = True
                    if propfail:
                        deduct_abbr_prop += freq
                        deduct_lemma += freq
                        print_in = False
                    else:
                        print("NOANALMATCH:", freq, surf, analysis, sep="\t", end="\t",
                              file=options.outfile)
                    if options.verbose:
                        print("@", end='', file=stderr)
                elif 'Unkwn' in analysis:
                    deduct_unkwn += freq
                    deduct_lemma += freq
                    print_in = False
                else:
                    if options.verbose:
                        print("@", end='', file=stderr)
                    print("NOANALMATCH:", freq, surf, analysis, sep="\t", end="\t",
                          file=options.outfile)
            else:
                if options.verbose:
                    print("@", end='', file=stderr)
                print("NOANALMATCH:", freq, surf, analysis, sep="\t", end="\t",
                      file=options.outfile)
        elif not found_lemma:
            anal_matches += freq
            print("NOLEMMAMATCH:", freq, surf, lemma, sep="\t", end="\t",
                  file=options.outfile)
            if options.verbose:
                print("#", end='', file=stderr)
        else:
            if options.verbose:
                print(".", end='', file=stderr)
            full_matches += freq
            print_in = False
        if print_in:
            print(":IN:", end="\t", file=options.outfile)
            for anal in anals:
                print(anal[0], end='\t', file=options.outfile)
            print(file=options.outfile)
    realend = perf_counter()
    cpuend = process_time()
    print("CPU time:", cpuend - cpustart, "real time:", realend - realstart)
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
    if options.additional_mapping == "ftb3.1":
        print("Deducting known bugs...\n",
              "Forgn:", deduct_forgn,
              "\nAdv Pos Man:", deduct_advposman,
              "\noli V Prt Act:", deduct_oliprt,
              "\nAbbr Prop:", deduct_abbr_prop,
              "\nUnkwn:", deduct_unkwn,
              file=options.statfile)
        lines = lines - deduct_forgn - deduct_advposman - \
            deduct_oliprt - deduct_abbr_prop - deduct_unkwn
        no_results -= deduct_results
        no_matches -= deduct_matches
        lemma_matches -= deduct_lemma
    if options.additional_mapping != '':
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
    if lines == 0 or (full_matches / lines * 100 < threshold):
        print("needs to have", threshold, "% matches to pass regress test\n",
              "please examine", options.outfile.name, "for regressions",
              file=stderr)
        exit(1)
    else:
        exit(0)


if __name__ == "__main__":
    main()
