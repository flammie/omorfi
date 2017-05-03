#!/bin/bash
LEXFILE=lexemes.tsv
DOCFILE=docs/lexemes.tsv
WORK=$(mktemp -d -t omorfi-validate-database.XXXXXXXXXX)

echo checking for missing docs for omorfi++ in ${LEXFILE}...
fgrep 'omorfi++' ${LEXFILE} | cut -f 1,2 > ${WORK}/keys
sort < ${WORK}/keys > ${WORK}/lc-sort-keys
cut -f 1,2 ${DOCFILE} | sort | uniq > ${WORK}/keys.$(basename $DOCFILE)
comm -13 ${WORK}/keys.$(basename $DOCFILE) ${WORK}/lc-sort-keys > ${WORK}/missing-keys.$(basename $DOCFILE)
while read k ; do
    echo MISSING $k is found in ${LEXFILE} but is not in $DOCFILE >> ${WORK}/fails.$(basename $DOCFILE)
    fgrep -- "${k}	" $LEXFILE | fgrep 'omorfi++' >> ${WORK}/fails.$(basename $DOCFILE)
    echo ADD $k into ${DOCFILE} >> ${WORK}/fails.$(basename $DOCFILE)
done < ${WORK}/missing-keys.$(basename $DOCFILE)
if test -e ${WORK}/fails.$(basename $DOCFILE) ; then
    echo
    echo there are missing docs in ${DOCFILE}, see ${WORK}/fails.$(basename $DOCFILE)
    exit 1
fi
rm -rf ${WORK}
