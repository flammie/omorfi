#!/bin/sh
if test ! -r $srcdir/wordforms.list ; then
    echo Missing word list $srcdir/wordforms.list
    exit 73
fi
hfst-lookup ../src/morphology.omor.hfst < $srcdir/wordforms.list > wordforms.anals
if grep '+?' wordforms.anals ; then
    echo "following known wordforms were missing from ../src/morphology.omor.hfst:"
    grep '+?' wordforms.anals
    exit 1
fi
