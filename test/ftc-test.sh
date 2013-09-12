#!/bin/sh
if test ! -r $srcdir/ftc-u8.xmls ; then
    echo Missing $srcdir/ftc.xmls
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
$PYTHON $srcdir/ftc-test.py -f ../src/ -i $srcdir/ftc-u8.xmls -o ftc.log
exit $?
