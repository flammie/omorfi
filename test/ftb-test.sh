#!/bin/bash
if test -z $srcdir ; then
    echo Use make check or define srcdir
    exit 1
fi
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
split -n l/100 $srcdir/ftb3.1.conllx ftb3.1.parts.
fail=0
for f in ftb3.1.parts.* ; do
    echo ${f}...
    if ! $PYTHON $srcdir/ftb-test.py -f ../src/morphology.ftb3.hfst -i $f -o ${f/parts/logs} ; then
        echo $f failed
        fail=1
    fi
done
cat ftb3.1.logs.* > ftb3.1.log
rm ftb3.1.parts* ftb3.1.logs*
exit $fail
