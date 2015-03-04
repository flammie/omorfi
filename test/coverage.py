#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test sort | uniq -c | sort -nr'd corpus
"""


import libhfst
from argparse import ArgumentParser, FileType

from sys import stderr, stdin, stdout

from time import perf_counter, process_time

def main():
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSAFILE', required=True,
            help="HFST's optimised lookup binary data for the transducer to be applied")
    a.add_argument('-i', '--input', metavar="INFILE", type=open, required=True,
            dest="infile", help="source of analysis data")
    a.add_argument('-o', '--output', metavar="outFILE", type=FileType('w'),
            required=True,
            dest="outfile", help="log file name")
    a.add_argument('-v', '--verbose', action="store_true", default=False,
            help="Print verbosely while processing")
    a.add_argument('-c', '--count', metavar="FREQ", default=0,
            help="test only word-forms with frequency higher than FREQ")
    a.add_argument('-t', '--threshold', metavar='THOLD', default=99, type=int,
            help="require THOLD % coverage or exit 1 (for testing)")
    options = a.parse_args()
    omorfi = libhfst.HfstTransducer(libhfst.HfstInputStream(options.fsa))
    # statistics
    tokens = 0
    uniqs = 0
    found_tokens = 0
    found_uniqs = 0
    missed_tokens = 0
    missed_uniqs = 0
    # for make check target
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
        tokens += freq
        uniqs += 1
        if options.verbose:
            print(tokens, "(", freq, ')...', end='\r')
        anals = libhfst.detokenize_paths(omorfi.lookup_fd(surf))
        if surf[0].isupper():
            anals += libhfst.detokenize_paths(omorfi.lookup_fd(surf[0].lower() + surf[1:]))
        if surf.isupper():
            anals += libhfst.detokenize_paths(omorfi.lookup_fd(surf.lower()))
        if surf.isupper():
            anals += libhfst.detokenize_paths(omorfi.lookup_fd(surf[0] + surf[1:].lower()))
        if len(anals) > 0:
            found_tokens += freq
            found_uniqs += 1
        else:
            missed_tokens += freq
            missed_uniqs += 1
            print(freq, surf, "? (missed)", sep="\t", file=options.outfile)
    if options.verbose:
        print()
    cpuend = process_time()
    realend = perf_counter()
    print("cpu time: ", cpuend - cpustart,
            "real time:", realend - realstart)
    print("Tokens", "Matches", "Misses", "%", sep="\t")
    print(tokens, found_tokens, missed_tokens, found_tokens / tokens * 100,
            sep="\t")
    print("Uniqs", "Matches", "Misses", "%", sep="\t")
    print(uniqs, found_uniqs, missed_uniqs, found_uniqs / uniqs * 100,
            sep="\t")
    if (found_tokens / tokens * 100 < options.threshold):
        print("needs to have", options.threshold,
                "% non-unique matches to pass regress test\n",
                file=stderr)
        exit(1)
    else:
        exit(0)

if __name__ == "__main__":
    main()
