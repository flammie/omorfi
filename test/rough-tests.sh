#!/bin/sh
if test -z $srcdir ; then
    echo run from make check or set srcdir=.
    exit 1
fi
if test ! -r $srcdir/wordforms.list ; then
    echo Missing word list $srcdir/wordforms.list
    exit 73
fi
fsa='../src/generated/omorfi.analyse.hfst'
if test -f $fsa ; then
    hfst-lookup -q $fsa < $srcdir/wordforms.list > wordforms.anals
    if grep '+?' wordforms.anals -m 1 > /dev/null ; then
        echo "following known wordforms were missing from $fsa"
        grep '+?' wordforms.anals
        exit 1
    fi
else
    echo "missing $fsa"
fi
