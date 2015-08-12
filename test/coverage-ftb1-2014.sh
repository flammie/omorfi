#!/bin/bash
# coverage for FTB 3.1
if test -z $srcdir ; then
    echo invoke from make check or define srcdir=.
    exit 1
fi
fsa="../src/generated/omorfi-ftb1.analyse.hfst"
cuf="ftb1-2014.uniq.freqs"
cs="get-covered.bash"
if ! test -r  $fsa ; then
    echo Unable to find built fsa for tests: $fsa
    exit 77
fi
if ! test -f "$cuf" ; then
    echo missing corpus data $cuf, run $cs and re-try
    exit 77
fi
if ! test -x /usr/bin/python ; then
    echo python missing, cannot run tests
    exit 77
fi
echo Looking up ftb1-2014.uniq.freqs
if ! /usr/bin/python $srcdir/coverage.py -f $fsa -i $cuf -c 2 -o ftb1-2014.coveragelog -t 96 ; then
    exit 1
fi

