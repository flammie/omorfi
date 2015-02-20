#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test sort | uniq -c | sort -nr'd FTB data against omorfi's FTB automaton
"""


import libhfst
from argparse import ArgumentParser, FileType

from sys import stderr, stdin, stdout

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
    a.add_argument('-c', '--count', metavar="FREQ", default=0,
            help="test only word-forms with frequency higher than FREQ")
    options = a.parse_args()
    omorfi = libhfst.HfstTransducer(libhfst.HfstInputStream(options.fsa))
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
    deduct_abbr_prop = 0
    deduct_unkwn = 0
    # known bugs by statistic to deduct
    deduct_lemma = 0
    deduct_anal = 0
    deduct_matches = 0
    deduct_results = 0
    # for make check target
    threshold = 90
    for line in options.infile:
        fields = line.strip().replace(' ', '\t', 1).split('\t')
        if len(fields) < 4:
            print("ERROR: Skipping line", fields, file=stderr)
            continue
        freq = int(fields[0])
        if freq < int(options.count):
            break
        ftbsurf = fields[1]
        ftblemma = fields[2]
        ftbanals = fields[3]
        lines += freq
        if options.verbose:
            print(freq, '...', end='\r')
        anals = libhfst.detokenize_paths(omorfi.lookup_fd(ftbsurf))
        if ftbsurf[0].isupper():
            anals += libhfst.detokenize_paths(omorfi.lookup_fd(ftbsurf[0].lower() + ftbsurf[1:]))
        if ftbsurf.isupper():
            anals += libhfst.detokenize_paths(omorfi.lookup_fd(ftbsurf.lower()))
        if ftbsurf.isupper():
            anals += libhfst.detokenize_paths(omorfi.lookup_fd(ftbsurf[0] + ftbsurf[1:].lower()))
        found_anals = False
        found_lemma = False
        print_in = True
        for anal in anals:
            if ftbanals in anal.output:
                found_anals = True
            if ftblemma in anal.output:
                found_lemma = True
        if len(anals) == 0:
            print_in = False
            no_results += freq
            if 'Forgn' in ftbanals:
                deduct_forgn += freq
                deduct_results += freq
                print_in = False
            elif 'Unkwn' in ftbanals:
                deduct_unkwn += freq
                deduct_results += freq
                print_in = False
            else:
                print("NORESULTS:", freq, ftbsurf, ftblemma, ftbanals, sep="\t",
                    file=options.outfile)
                if options.verbose:
                    print("?", end='', file=stderr)
        elif not found_anals and not found_lemma:
            no_matches += freq
            if 'Adv Pos Man' in ftbanals:
                deduct_advposman += freq
                deduct_matches += freq
                print_in = False
            elif 'Unkwn' in ftbanals:
                deduct_unkwn += 1
                deduct_matches += 1
                print_in = False
            else:
                print("NOMATCH:", freq, ftbsurf, ftblemma, ftbanals, sep="\t", end="\t",
                    file=options.outfile)
                if options.verbose:
                    print("!", end='', file=stderr)
        elif not found_anals:
            lemma_matches += freq
            if 'Adv Pos Man' in ftbanals:
                deduct_advposman += freq
                deduct_lemma += freq
                print_in = False
            elif 'V Prt Act' in ftbanals and ftbsurf.startswith('oli'):
                deduct_oliprt += freq
                deduct_lemma += freq
                print_in = False
            elif 'Forgn' in ftbanals:
                deduct_forgn += freq
                deduct_lemma += freq
                print_in = False
            elif 'Abbr' in ftbanals:
                propfail = False
                for anal in anals:
                    if 'Abbr Prop' in anal.output:
                        propfail = True
                if propfail:
                    deduct_abbr_prop += freq
                    deduct_lemma += freq
                    print_in = False
                else:
                    print("NOANALMATCH:", freq, ftbsurf, ftbanals, sep="\t", end="\t",
                        file=options.outfile)
                if options.verbose:
                    print("@", end='', file=stderr)
            elif 'Unkwn' in ftbanals:
                deduct_unkwn += freq
                deduct_lemma += freq
                print_in = False
            else:
                if options.verbose:
                    print("@", end='', file=stderr)
                print("NOANALMATCH:", freq, ftbsurf, ftbanals, sep="\t", end="\t",
                    file=options.outfile)
        elif not found_lemma:
            anal_matches += freq
            print("NOLEMMAMATCH:", freq, ftbsurf, ftblemma, sep="\t", end="\t",
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
                print(anal.output, end='\t', file=options.outfile)
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
    print("Deducting known bugs...\n",
            "Forgn:", deduct_forgn,
            "\nAdv Pos Man:", deduct_advposman,
            "\noli V Prt Act:", deduct_oliprt,
            "\nAbbr Prop:", deduct_abbr_prop,
            "\nUnkwn:", deduct_unkwn,
            file=options.statfile)
    lines = lines - deduct_forgn - deduct_advposman - deduct_oliprt - deduct_abbr_prop - deduct_unkwn
    no_results -= deduct_results
    no_matches -= deduct_matches
    lemma_matches -= deduct_lemma
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
