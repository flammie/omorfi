#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compare two conllu files for matches on each field.
"""

import sys
from argparse import ArgumentParser, FileType
from sys import stderr


def main():
    a = ArgumentParser()
    a.add_argument("-H", "--hypothesis", metavar="HYPFILE", type=open,
                   required=True, dest="hypfile", help="analysis results")
    a.add_argument("-r", "--reference", metavar="REFFILE", type=open,
                   required=True,
                   dest="reffile", help="reference data")
    a.add_argument("-l", "--log", metavar="LOGFILE", required=True,
                   type=FileType("w"),
                   dest="logfile", help="result file")
    a.add_argument("-X", "--realign", action="store_true", default=False,
                   help="Allow fuzzy matches if tokenisation differs")
    a.add_argument("-v", "--verbose", action="store_true", default=False,
                   help="Print verbosely while processing")
    a.add_argument("-t", "--thresholds", metavar="THOLDS", default=99,
                   type=int, help="require THOLD % for lemma, UPOS and " +
                   "UFEATs or exit 1 (for testing)")
    options = a.parse_args()
    #
    reflines = 0
    hyplines = 0
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
        infields = hypline.strip().split("\t")
        reffields = refline.strip().split("\t")
        while len(infields) < 4:
            if hypline.startswith("#") or hypline.strip() == "":
                pass
            else:
                print("mismatched unknown non-content! HYP:", hypline,
                      "REF:", refline, sep="\n")
                sys.exit(1)
            try:
                hypline = next(options.hypfile)
            except StopIteration:
                eoffed = True
                break
            hyplines += 1
            infields = hypline.strip().split("\t")
        while len(reffields) < 4:
            if refline.startswith("#") or refline.strip() == "":
                pass
            else:
                print("mismatched unknown non-content! REF:", refline,
                      "HYP:", hypline, sep="\n")
                exit(1)
            try:
                refline = next(options.reffile)
            except StopIteration:
                eoffed = True
                break
            reflines += 1
            reffields = refline.strip().split("\t")
        if eoffed:
            break
        if infields[0] != reffields[0]:
            if "-" in reffields[0]:
                refline = next(options.reffile)
                reffields = refline.strip().split("\t")
            elif "." in reffields[0]:
                refline = next(options.reffile)
                reffields = refline.strip().split("\t")
            else:
                skiplines += 1
                print("misaligned (index)! IN:", infields[0], "REF:",
                      reffields[0], "\n", hypline, refline,
                      "skipping...", file=stderr)
                if options.realign:
                    while hypline != "":
                        skiplines += 1
                        hypline = next(options.hypfile).strip()
                    while refline != "":
                        refline = next(options.reffile).strip()
                    continue
                else:
                    sys.exit(1)
        if infields[1] != reffields[1]:
            skiplines += 1
            print("misaligned (surface)! IN:", infields[1], "REF:",
                  reffields[1], "\n", hypline, "\n", refline, file=stderr)
            if options.realign:
                while hypline != "":
                    skiplines += 1
                    hypline = next(options.hypfile).strip()
                while refline != "":
                    refline = next(options.reffile).strip()
                continue
            else:
                sys.exit(1)
        if infields[2] != reffields[2]:
            missed_lemmas += 1
            print("LEMMA", infields[2], reffields[2], file=options.logfile)
            print("^^|SURF", infields[1], reffields[1], infields[2],
                  reffields[2], file=options.logfile)
        if infields[3] != reffields[3]:
            missed_uposes += 1
            print("UPOS", infields[3], reffields[3], file=options.logfile)
            print("^^|SURF", infields[1], reffields[1], infields[3],
                  reffields[3], file=options.logfile)
        if infields[4] != reffields[4]:
            missed_tdtposes += 1
            print("TDTPOS", infields[4], reffields[4], file=options.logfile)
            print("^^|SURF", infields[1], reffields[1], infields[4],
                  reffields[4], file=options.logfile)
        if infields[5] != reffields[5]:
            missed_feats += 1
            print("UFEAT", infields[5], reffields[5], file=options.logfile)
            print("^^|SURF", infields[1], reffields[1], infields[5],
                  reffields[5], file=options.logfile)
            infeats = set(infields[5].split("|"))
            reffeats = set(reffields[5].split("|"))
            missfeats = reffeats - infeats
            for misfit in missfeats:
                print("MISFIT", misfit, file=options.logfile)
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
          deplines - missed_lemmas,
          deplines - missed_uposes,
          deplines - missed_feats,
          deplines - missed_tdtposes,
          deplines - missed_uds,
          deplines - missed_udlabs,
          deplines - missed_deps2,
          deplines - missed_misc,
          sep="\t")
    print(deplines / deplines * 100,
          (deplines - missed_lemmas) / deplines * 100 if deplines != 0 else 0,
          (deplines - missed_uposes) / deplines * 100 if deplines != 0 else 0,
          (deplines - missed_feats) / deplines * 100 if deplines != 0 else 0,
          (deplines - missed_tdtposes) / deplines * 100 if deplines != 0 else 0,
          (deplines - missed_uds) / deplines * 100 if deplines != 0 else 0,
          (deplines - missed_udlabs) / deplines * 100 if deplines != 0 else 0,
          (deplines - missed_deps2) / deplines * 100 if deplines != 0 else 0,
          (deplines - missed_misc) / deplines * 100 if deplines != 0 else 0,
          sep="\t")
    print("Skipped due to tokenisation etc. (no fuzz):", skiplines)
    if deplines == 0 or \
            ((deplines - missed_lemmas) / deplines * 100 < options.thresholds)\
            or\
            ((deplines - missed_uposes) / deplines * 100 < options.thresholds)\
            or\
            ((deplines - missed_feats) / deplines * 100 < options.thresholds):
        print("needs to have", options.thresholds,
              "% matches to pass regress test\n",
              file=stderr)
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
