#!/bin/sh
if test ! -r $srcdir/wordforms.list ; then
    echo Missing word list $srcdir/wordforms.list
    exit 73
fi
fsa='-'
for tf in apertium omor ftb3 ; do
    if test -f ../src/morphology.$tf.hfst ; then
        fsa="../src/morphology.$tf.hfst"
    fi
done
hfst-lookup $fsa < $srcdir/wordforms.list > wordforms.anals
if grep '+?' wordforms.anals -m 1 > /dev/null ; then
    echo "following known wordforms were missing from $fsa"
    grep '+?' wordforms.anals
    exit 1
fi
