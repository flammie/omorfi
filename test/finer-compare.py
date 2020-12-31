#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compare two finer-data files for matches on NER-annotations.
"""


from argparse import ArgumentParser, FileType
import sys
from sys import stderr


def main():
    a = ArgumentParser()
    a.add_argument('-H', '--hypothesis', metavar="HYPFILE", type=open,
                   required=True, dest="hypfile", help="analysis results")
    a.add_argument('-r', '--reference', metavar="REFFILE", type=open,
                   required=True,
                   dest="reffile", help="reference data")
    a.add_argument('-l', '--log', metavar="LOGFILE", required=True,
                   type=FileType('w'),
                   dest="logfile", help="result file")
    a.add_argument('-v', '--verbose', action="store_true", default=False,
                   help="Print verbosely while processing")
    a.add_argument('-t', '--thresholds', metavar='THOLDS', default=99,
                   type=int, help="require THOLD % for lemma, UPOS and "
                   + "UFEATs or exit 1 (for testing)")
    options = a.parse_args()
    reflines = 0
    hyplines = 0
    lines = 0
    missed_ner = 0
    eoffed = False
    while not eoffed:
        try:
            hypline = next(options.hypfile)
            refline = next(options.reffile)
        except StopIteration:
            eoffed = True
            break
        reflines += 1
        hyplines += 1
        infields = hypline.strip().split('\t')
        reffields = refline.strip().split('\t')
        while len(infields) < 2:
            if hypline.strip() == "" or (
                    hypline.startswith('<') and hypline.strip().endswith('>')):
                pass
            else:
                print("mismatched unknown non-content! HYP:", hypline,
                      "REF:", refline, sep='\n')
                sys.exit(1)
            try:
                hypline = next(options.hypfile)
            except StopIteration:
                eoffed = True
                break
            hyplines += 1
            infields = hypline.strip().split('\t')
        while len(reffields) < 3:
            if refline.strip() == "" or (
                    refline.startswith('<') and refline.strip().endswith('>')):
                pass
            else:
                print("mismatched unknown non-content! REF:", refline,
                      "HYP:", hypline, sep='\n')
                sys.exit(1)
            try:
                refline = next(options.reffile)
            except StopIteration:
                eoffed = True
                break
            reflines += 1
            reffields = refline.strip().split('\t')
        if eoffed:
            break
        if infields[0] != reffields[0]:
            print("misaligned (index)! IN:", infields[0], "REF:",
                  reffields[0], "\n", hypline, refline,
                  "skipping...", file=stderr)
            sys.exit(1)
        if infields[1] != reffields[1]:
            missed_ner += 1
            print("NER", infields[1], reffields[1], file=options.logfile)
            print("NER|SURF", infields[0], reffields[0], infields[1],
                  reffields[1], file=options.logfile)
        lines += 1

    print("Lines", "NER", sep="\t")
    print(lines, lines - missed_ner, sep="\t")
    print(lines / lines * 100,
          (lines - missed_ner) / lines * 100 if lines != 0 else 0,
          sep="\t")
    if lines == 0 or \
            ((lines - missed_ner) / lines * 100 < options.thresholds):
        print("needs to have", options.thresholds,
              "% matches to pass regress test\n",
              file=stderr)
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
