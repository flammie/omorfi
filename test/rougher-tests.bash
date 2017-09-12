#!/bin/sh
if test -z $srcdir ; then
    echo run from make check or set srcdir=.
    exit 1
fi
if test ! -r $srcdir/wordforms-common.list ; then
    echo Missing word list $srcdir/wordforms-common.list
    exit 73
fi
fsa='../src/generated/omorfi.analyse.hfst'
if test -f $fsa ; then
    hfst-lookup -q $fsa < $srcdir/wordforms-common.list > wordforms-common.anals
    if fgrep '+?' wordforms-common.anals -m 1 > /dev/null ; then
        echo "following known wordforms were missing from $fsa"
        fgrep '+?' wordforms-common.anals
        exit 1
    fi
else
    echo "missing automaton $fsa"
    exit 1
fi
