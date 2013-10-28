#!/bin/sh
if test ! -r $srcdir/ftb3.1.conllx ; then
    echo Missing $srcdir/ftb3.1.conllx
    exit 77
fi
if test ! -r ../src/morphology.ftb3.hfst ; then
    echo Missing ../src/morphology.ftb3.hfst
    echo this test only applies to FTB3 version of morphology
    exit 77
fi
PYTHON=python3
if type python3 ; then
    PYTHON=python3
elif type python ; then
    PYTHON=python
else
    echo Missing python3
    exit 77
fi
$PYTHON $srcdir/ftb-test.py -f ../src/morphology.ftb3.hfst -i $srcdir/ftb3.1.conllx -o ftb3.1.log
exit $?
