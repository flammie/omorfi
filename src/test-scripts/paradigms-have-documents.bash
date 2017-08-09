#!/bin/bash
LEXFILE=lexemes.tsv
DOCFILE=docs/paradigms.tsv
WORK=$(mktemp -d -t omorfi-validate-database.XXXXXXXXXX)

echo checking for missing docs for paradigms in ${LEXFILE}...
cut -f 3 ${LEXFILE} | sort | uniq > ${WORK}/paradigms
cut -f 1 ${DOCFILE} | sort | uniq > ${WORK}/docs.paradigms
comm -23 ${WORK}/paradigms ${WORK}/docs.paradigms > ${WORK}/missing-para-docs
while read k ; do
    echo MISSING $k is found in ${LEXFILE} but is not in $DOCFILE >> ${WORK}/fails.paradigms
    fgrep -m 1 -- "${k}	" $LEXFILE |\
        awk -F '\t' '{printf("%s\tfor example: %s\n", $3, $1);}' \
        >> ${WORK}/fails.paradigms
    echo ADD $k into ${DOCFILE} >> ${WORK}/fails.paradigms
done < ${WORK}/missing-para-docs
comm -13 ${WORK}/paradigms ${WORK}/docs.paradigms > ${WORK}/extra-para-docs
while read k ; do
    echo EXTRA $k is found in ${DOCFILE} but is not in $LEXFILE >> ${WORK}/fails.paradigms
    echo REMOVE $k from ${DOCFILE} >> ${WORK}/fails.paradigms
done < ${WORK}/extra-para-docs
if test -e ${WORK}/fails.paradigms ; then
    echo
    echo there are missing docs in ${DOCFILE}, see ${WORK}/fails.paradigms
    exit 1
fi
rm -rf ${WORK}
