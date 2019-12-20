#!/bin/bash
if test $# -lt 2 ; then
    echo Usage $0 LEMMAFILE OUTFILE
    exit 1
fi
cat $1 | while read l; do
    echo ${l}...
    echo -n \"${l}\"  >> $2
    echo ${l} |\
        sed -e 's/./\0 /g' |\
        sed -e 's/[$_]/%\0/g' |\
        sed -e 's/   / %  /g' |\
        sed -e 's/^/%[WORD%_ID%= /' -e 's/$/%] \\%[WORD%_ID%=* ;/' |\
        hfst-regexp2fst -o src/generated/temporary.wordform.hfst
        hfst-compose -v -F src/generated/temporary.describe.hfst \
            src/generated/temporary.wordform.hfst \
            -o src/generated/temporary.wordgen.hfst
    hfst-fst2strings src/generated/temporary.wordgen.hfst |\
        uniq |\
        tr -s '\n' ' ' >> $2
    echo >> $2
done

