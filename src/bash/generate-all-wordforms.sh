#!/bin/bash
DEST=wordforms.txt
TSV=src/generated/master.tsv
lines=$(wc -l < $TSV)
echo > ${DEST}
linen=0
cut -f 2 < src/generated/master.tsv | tail -n +4 | while read l; do
    linen=$((linen + 1))
    echo "${l}... $linen / $lines"
    echo -n ${l}: >> ${DEST}
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
        sed -e 's/\\:/@@@/g' |\
        cut -d : -f 1 |\
        sed -e 's/@@@/:/g' |\
        uniq |\
        tr -s '\n' ' ' >> ${DEST}
    echo >> ${DEST}
done

