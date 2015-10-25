#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Compare two conllu files for matches on each field.
"""


from argparse import ArgumentParser, FileType

from sys import stderr, stdin, stdout

def main():
    a = ArgumentParser()
    a.add_argument('-H', '--hypothesis', metavar="HYPFILE", type=open, required=True,
            dest="hypfile", help="analysis results")
    a.add_argument('-r', '--reference', metavar="REFFILE", type=open,
            required=True,
            dest="reffile", help="reference data")
    a.add_argument('-l', '--log', metavar="LOGFILE", required=True,
            type=FileType('w'),
            dest="logfile", help="result file")
    a.add_argument('-X', '--realign', action="store_true", default=False,
            help="Allow fuzzy matches if tokenisation differs")
    a.add_argument('-v', '--verbose', action="store_true", default=False,
            help="Print verbosely while processing")
    options = a.parse_args()
    #
    lines = 0
    deplines = 0
    skiplines = 0
    # count this
    missed_lemmas = 0
    missed_uposes = 0
    missed_tdtposes = 0
    missed_feats = 0
    missed_uds = 0
    missed_udlabs = 0
    missed_deps2 = 0
    missed_misc = 0

    for hypline in options.hypfile:
        refline = next(options.reffile)
        lines += 1
        infields = hypline.strip().split('\t')
        reffields = refline.strip().split('\t')
        if len(infields) < 4:
            if 'doc-name' in hypline:
                continue
            elif 'sentence-text' in hypline:
                while hypline != refline:
                    refline = next(options.reffile)
                continue
            elif hypline == refline:
                continue
            else:
                print("mismatched unknown non-content! IN:", hypline, "REF:", refline,
                        sep='\n')
                exit(1)
        if infields[0] != reffields[0]:
            if '-' in reffields[0]:
                refline = next(options.reffile)
                reffields = refline.strip().split('\t')
            else:
                skiplines += 1
                print("misaligned (index)! IN:", infields[0], "REF:", reffields[0],
                        "\n", hypline, refline, "skipping...", file=stderr)
                if options.realign:
                    while hypline != "":
                        skiplines += 1
                        hypline = next(options.hypfile).strip()
                    while refline != "":
                        refline = next(options.reffile).strip()
                    continue
                else:
                    exit(1)
        if infields[1] != reffields[1]:
            skiplines += 1
            print("misaligned (surface)! IN:", infields[1], "REF:", reffields[1],
                    "\n", hypline, "\n", refline, file=stderr)
            if options.realign:
                while hypline != "":
                    skiplines += 1
                    hypline = next(options.hypfile).strip()
                while refline != "":
                    refline = next(options.reffile).strip()
                continue
            else:
                exit(1)
        if infields[2] != reffields[2]:
            missed_lemmas += 1
            print("LEMMA", infields[2], reffields[2], file=options.logfile)
            print("SURFS", infields[1], reffields[1], file=options.logfile)
        if infields[3] != reffields[3]:
            missed_uposes += 1
            print("UPOS", infields[3], reffields[3], file=options.logfile)
            print("SURFS", infields[1], reffields[1], file=options.logfile)
        if infields[4] != reffields[4]:
            missed_tdtposes += 1
            print("TDTPOS", infields[4], reffields[4], file=options.logfile)
            print("SURFS", infields[1], reffields[1], file=options.logfile)
        if infields[5] != reffields[5]:
            missed_feats += 1
            print("UFEAT", infields[5], reffields[5], file=options.logfile)
            print("SURFS", infields[1], reffields[1], file=options.logfile)
        if infields[6] != reffields[6]:
            missed_uds += 1
            print("UD", infields[6], reffields[6], file=options.logfile)
        if infields[7] != reffields[7]:
            missed_udlabs += 1
            print("UDLAB", infields[7], reffields[7], file=options.logfile)
        if infields[8] != reffields[8]:
            missed_deps2 += 1
            print("DEPS2", infields[8], reffields[8], file=options.logfile)
        if infields[9] != reffields[9]:
            missed_misc += 1
            print("MISC", infields[9], reffields[9], file=options.logfile)
        deplines += 1

    print("Lines", "Lemma", "UPOS", "UFEAT", "TDT POS", "UD →", "UD LAB",
            "2^ndDEP", "MISC", sep="\t")
    print(deplines, 
            deplines-missed_lemmas,
            deplines-missed_uposes,
            deplines-missed_feats,
            deplines-missed_tdtposes,
            deplines-missed_uds,
            deplines-missed_udlabs,
            deplines-missed_deps2,
            deplines-missed_misc,
            sep="\t")
    print(deplines / deplines * 100, 
            (deplines-missed_lemmas) / deplines * 100,
            (deplines-missed_uposes) / deplines * 100,
            (deplines-missed_feats) / deplines * 100,
            (deplines-missed_tdtposes) / deplines * 100,
            (deplines-missed_uds) / deplines * 100,
            (deplines-missed_udlabs) / deplines * 100,
            (deplines-missed_deps2) / deplines * 100,
            (deplines-missed_misc) / deplines * 100,
            sep="\t")
    print("Skipped due to tokenisation etc. (no fuzz):", skiplines)
    exit(0)

if __name__ == "__main__":
    main()
