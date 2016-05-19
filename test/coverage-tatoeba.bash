#!/bin/bash
# coverage for fiwiki-latest
if test -z $srcdir ; then
    echo invoke from make check or define srcdir=.
    exit 1
fi
fsa="../src/generated/"
cuf="tatoeba-fi.uniq.freqs"
cs="get-covered.bash"
if ! test -r $fsa ; then
    echo Unable to find built fsa for tests: $fsa
fi
if ! test -f $cuf ; then
    echo missing corpus data $cuf, run $cs and retry
    exit 77
fi
if ! test -x /usr/bin/python3 ; then
    echo python missing, cannot run tests
    exit 77
fi
echo Looking up gutenberg-fi.tokens
if ! PYTHONPATH=$PYTHONPATH:../src/python /usr/bin/python3 coverage.py -f $fsa -i $cuf -c 2 -o tatoeba-fi.coveragelog -t 96 ; then
    exit 1
fi
