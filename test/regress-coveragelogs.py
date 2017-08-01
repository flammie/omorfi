#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compare two directories full of coveragelogs for regressions.
"""


from argparse import ArgumentParser, FileType
from glob import glob
from sys import stderr


def main():
    a = ArgumentParser()
    a.add_argument('-c', '--current', metavar="CURRDIR", required=True,
                   dest="currdir", help="analysis results")
    a.add_argument('-r', '--reference', metavar="REFDIR", required=True,
                   dest="refdir", help="previous results")
    a.add_argument('-l', '--log', metavar="LOGFILE", required=True,
                   type=FileType('w'),
                   dest="logfile", help="result file")
    a.add_argument(
        '-t', '--thresholds', metavar='THOLDS', default=99, type=int,
        help="require THOLD % regressions or exit 1 (for testing)")
    options = a.parse_args()
    # count this
    currlines = 0
    reflines = 0
    regressioncount = 0
    regressions = dict()
    devcount = 0
    developments = dict()

    reffiles = glob(options.refdir + "/*.coveragelog")
    currfiles = glob(options.currdir + "/*.coveragelog")
    for reffile in reffiles:
        reffn = reffile[reffile.rfind("/"):]
        currfn = None
        for currfile in currfiles:
            currfn = currfile[currfile.rfind("/"):]
            if currfn == reffn:
                break
            else:
                currfn = None
        if not currfn:
            print("Could not find", reffn, "from", options.currdir, "skipping")
            continue
        ref = open(reffile)
        curr = open(options.currdir + "/" + currfn)
        currcount = 1000000000
        refcount = 1000000000
        try:
            currline = next(curr)
            refline = next(ref)
            currlines += 1
            reflines += 1
        except StopIteration:
            print("Cannot read first line of file?!")
            exit(2)
        try:
            while curr and ref:
                reffields = refline.strip().split()
                currfields = currline.strip().split()
                currcount = int(currfields[0])
                refcount = int(reffields[0])
                currword = reffields[1]
                refword = reffields[1]
                if currcount > refcount:
                    # reference needs to catch up from regressed terms
                    if currword not in regressions:
                        regressions[currword] = 0
                    regressions[currword] += currcount
                    regressioncount += currcount
                    currline = next(curr)
                    currlines += 1
                elif refcount > currcount:
                    # new words found
                    if refword not in developments:
                        developments[refword] = 0
                    developments[refword] += refcount
                    devcount += refcount
                    refline = next(ref)
                    reflines += 1
                elif currword < refword:
                    # current earlier in alphabets, same count: regression
                    if currword not in regressions:
                        regressions[currword] = 0
                    regressions[currword] += currcount
                    regressioncount += currcount
                    currline = next(curr)
                    currlines += 1
                elif refword < currword:
                    # reference earlier in alphabets: new addition
                    if refword not in developments:
                        developments[refword] = 0
                    developments += refcount
                    devcount += refcount
                    refline = next(ref)
                    reflines += 1
                else:
                    # both are same, great
                    refline = next(ref)
                    currline = next(curr)
                    currlines += 1
                    reflines += 1
        except StopIteration:
            # normal: one of the streams can end earlier
            pass

    print("REGRESSED:", file=options.logfile)
    for reg in sorted(regressions, key=regressions.get, reverse=True):
        print(regressions[reg], reg, sep="\t", file=options.logfile)
    print("\n\n\nDEVELOPED:", file=options.logfile)
    for dev in sorted(developments, key=developments.get, reverse=True):
        print(developments[dev], dev, sep="\t", file=options.logfile)
    if currlines == 0 or reflines == 0:
        print("needs to have lines or", options.thresholds,
              "% matches to pass regress test\n",
              file=stderr)
        exit(1)
    else:
        exit(0)


if __name__ == "__main__":
    main()
