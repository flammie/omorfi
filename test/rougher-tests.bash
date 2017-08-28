#!/bin/sh
if test -z $srcdir ; then
    echo run from make check or set srcdir=.
    exit 1
fi
if test ! -r $srcdir/wordforms-common.list ; then
    echo Missing word list $srcdir/wordforms-common.list
    exit 73
fi
fsa='-'
for f in ../src/generated/omorfi-*.analyse.hfst \
    ../src/generated/fin-automorf.hfst \
    ../src/generated/omorfi.segment.hfst \
    ../src/generated/omorfi.lemmatise.hfst ; do
    if ! hfst-lookup -q $f < $srcdir/wordforms-common.list \
            > wordforms-common.anals ; then
        echo lookup failed for $f
        exit 1
    fi
    if fgrep '+?' wordforms-common.anals -m 1 > /dev/null ; then
        echo "following known wordforms were missing from $f"
        fgrep '+?' wordforms-common.anals
        exit 1
    fi
done
