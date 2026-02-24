#!/bin/bash
if test -z $srcdir ; then
    echo Use make check or define srcdir
    exit 1
fi
fsa="../src/generated/omorfi.describe.hfst"
cuf="tokenisation-test-set.text"
if test ! -r "$fsa" ; then
    echo Missing $fsa
    exit 77
fi
if ! test -x /usr/bin/python ; then
    echo Missing python
    exit 77
fi
if test ! -r $cuf ; then
    echo missing $cuf? Should be in git / tarballs, report issue plz
    exit 77
fi
if ! /usr/bin/python ../src/python/omorfi-tokenise.py -a $fsa -i $cuf \
        -o tokenisation-test-set.hyps; then
    echo Tokenisation failed from unknown reasons
    exit 1
fi
if ! diff -u tokenisation-test-set.hyps tokenisation-test-set.ref ; then
    echo Unexpected tokenisations see above
    exit 1
fi
exit 0
