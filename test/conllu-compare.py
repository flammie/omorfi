#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test sort | uniq -c | sort -nr'd gold analysis data for faithfulness
"""


from argparse import ArgumentParser, FileType

from sys import stderr, stdin, stdout

def main():
    a = ArgumentParser()
    a.add_argument('-i', '--input', metavar="INFILE", type=open, required=True,
            dest="infile", help="analysis results")
    a.add_argument('-r', '--reference', metavar="INFILE", type=open,
            required=True,
            dest="reffile", help="reference data")
    a.add_argument('-o', '--output', metavar="OUTFILE", required=True,
            type=FileType('w'),
            dest="outfile", help="result file")
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

    for inline in options.infile:
        refline = next(options.reffile)
        lines += 1
        infields = inline.strip().split('\t')
        reffields = refline.strip().split('\t')
        if len(infields) < 4:
            if 'doc-name' in inline:
                continue
            elif 'sentence-text' in inline:
                while inline != refline:
                    refline = next(options.reffile)
                continue
            elif inline == refline:
                continue
            else:
                print("mismatched unknown non-content! IN:", inline, "REF:", refline,
                        sep='\n')
                exit(1)
        if infields[0] != reffields[0]:
            skiplines += 1
            print("misaligned (index)! IN:", infields[0], "REF:", reffields[0],
                    "\n", inline, refline, "skipping...", file=stderr)
            while inline != "":
                skiplines += 1
                inline = next(options.infile).strip()
            while refline != "":
                refline = next(options.reffile).strip()
            continue
        if infields[1] != reffields[1]:
            skiplines += 1
            print("misaligned (surface)! IN:", infields[1], "REF:", reffields[1],
                    "\n", inline, "\n", refline, file=stderr)
            while inline != "":
                skiplines += 1
                inline = next(options.infile).strip()
            while refline != "":
                refline = next(options.reffile).strip()
            continue

        if infields[2] != reffields[2]:
            missed_lemmas += 1
            print("LEMMA", infields[2], reffields[2], file=options.outfile)
        if infields[3] != reffields[3]:
            missed_uposes += 1
            print("UPOS", infields[3], reffields[3], file=options.outfile)
        if infields[4] != reffields[4]:
            missed_tdtposes += 1
            print("TDTPOS", infields[4], reffields[4], file=options.outfile)
        if infields[5] != reffields[5]:
            missed_feats += 1
            print("UFEAT", infields[5], reffields[5], file=options.outfile)
        if infields[6] != reffields[6]:
            missed_uds += 1
            print("UD", infields[6], reffields[6], file=options.outfile)
        if infields[7] != reffields[7]:
            missed_udlabs += 1
            print("UDLAB", infields[7], reffields[7], file=options.outfile)
        if infields[8] != reffields[8]:
            missed_deps2 += 1
            print("DEPS2", infields[8], reffields[8], file=options.outfile)
        if infields[9] != reffields[9]:
            missed_misc += 1
            print("MISC", infields[9], reffields[9], file=options.outfile)
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
