#!/bin/bash
DEST=wordforms.txt
TSV=src/lexical/master.tsv
echo > ${DEST}
cut -f 1 < src/lexical/master.tsv | tail -n +4 | while read l; do
    echo ${l}...
    echo -n ${l}: >> ${DEST}
    echo ${l} |\
        sed -e 's/./\0 /g' |\
        sed -e 's/^/%[WORD%_ID%= /' -e 's/$/%] \\%[WORD%_ID%=* ;/' |\
        hfst-regexp2fst -o temporary.wordform.hfst
    hfst-compose -v -F src/temporary.ftb3.hfst temporary.wordform.hfst -o temporary.wordgen.hfst
    hfst-fst2strings temporary.wordgen.hfst | cut -d : -f 1 | tr -s '\n' ' ' >> ${DEST}
    echo >> ${DEST}
done

