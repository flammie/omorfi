#!/bin/bash
LEXFILE=lexemes.tsv
DOCFILE=docs/paradigms.tsv
REFILE=paradigms/suffix-regexes.tsv
MFILE=paradigms/morphophonology.tsv
DELFILE=paradigms/stub-deletions.tsv

WORK=$(mktemp -d -t omorfi-validate-database.XXXXXXXXXX)

echo checking for missing docs for paradigms in ${LEXFILE}...
cut -f 3 ${LEXFILE} | sort | uniq > ${WORK}/paradigms
for d in $MFILE $REFILE $DELFILE $DOCFILE ; do
    cut -f 1 ${d} | sort | uniq > ${WORK}/$(basename $d).paradigms
    comm -23 ${WORK}/paradigms ${WORK}/$(basename $d).paradigms > ${WORK}/missing-para-$(basename $d)
    while read k ; do
        echo MISSING $k is found in ${LEXFILE} but is not in $d >> ${WORK}/fails.paradigms
        fgrep -m 1 -- "${k}	" $LEXFILE |\
            awk -F '\t' '{printf("%s\tfor example: %s\n", $3, $1);}' \
            >> ${WORK}/fails.paradigms
        echo ADD $k into ${d} >> ${WORK}/fails.paradigms
    done < ${WORK}/missing-para-$(basename $d)
    comm -13 ${WORK}/paradigms ${WORK}/$(basename $d).paradigms > ${WORK}/extra-para-$(basename $d)
    while read k ; do
        echo EXTRA $k is found in ${d} but is not in $LEXFILE >> ${WORK}/fails.paradigms
        echo REMOVE $k from ${d} >> ${WORK}/fails.paradigms
    done < ${WORK}/extra-para-$(basename $d)
done
if test -e ${WORK}/fails.paradigms ; then
    echo
    echo there are missing paradigms, see ${WORK}/fails.paradigms
    exit 1
fi
rm -rf ${WORK}
