#!/bin/sh
if test -z $srcdir ; then
    echo run from make check or set srcdir=.
    exit 1
fi
if test ! -r $srcdir/wordforms.list ; then
    echo Missing word list $srcdir/wordforms.list
    exit 73
fi
fsa='-'
for f in ../src/generated/omorfi-*.analyse.hfst \
    ../src/generated/fin-automorf.hfst \
    ../src/generated/omorfi.segment.hfst \
    ../src/generated/omorfi.lemmatise.hfst ; do
    hfst-lookup -q $f < $srcdir/wordforms.list > wordforms.anals
    if grep '+?' wordforms.anals -m 1 > /dev/null ; then
        echo "following known wordforms were missing from $f"
        grep '+?' wordforms.anals
        exit 1
    fi
done
