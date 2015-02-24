#!/bin/bash
if test -z $srcdir ; then
    echo Use make check or define srcdir
    exit 1
fi
if test ! -r $srcdir/ftb3.1.conllx ; then
    echo Missing $srcdir/ftb3.1.conllx
    exit 77
fi
if test ! -r ../src/generated/omorfi-ftb3.analyse.hfst ; then
    echo Missing ../src/geerated/omorfi-ftb3.analyse.hfst
    echo this test only applies to FTB3 version of morphology
    exit 77
fi
PYTHON=python3
if type python3 ; then
    PYTHON=python3
elif type python ; then
    if python -V | fgrep 3. ; then
        PYTHON=python
    else
        echo $(which python) not python3
        exit 77
    fi
else
    echo Missing python3
    exit 77
fi
if test ! -r ftb3.1.conllx.cutted.freqs ; then
    echo counting freqs for ftb3.1
    egrep -v '^<' < $srcdir/ftb3.1.conllx | cut -f 2,3,6 | sort | uniq -c | sort -nr > ftb3.1.conllx.cutted.freqs
fi
if ! $PYTHON $srcdir/faithfulness.py -f ../src/generated/omorfi-ftb3.analyse.hfst -i ftb3.1.conllx.cutted.freqs -c 1000 -o ftb3.1-short.log -a ftb3.1 ; then
    echo We missed the target of 90 % faithfulness
    exit 1
fi
exit 0
