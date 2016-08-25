#!/bin/bash
LEXFILE=lexemes.tsv
WORK=$(mktemp -d -t omorfi-validate-database.XXXXXXXXXX)
if test -f ${WORK}/duplicate-keys ; then
    rm -v duplicate-keys
fi

echo "checking for duplicate unique keys in lexemes (word_id, homonym)"
echo ${LEXFILE}...
cut -f 1,2 ${LEXFILE} | LC_ALL=C sort > ${WORK}/keys
LC_ALL=C uniq -c < ${WORK}/keys |\
    awk '$1 > 1 {print;}' > ${WORK}/duplicate-keys
if test -s ${WORK}/duplicate-keys ; then
    echo ${LEXFILE} has duplicate keys in ${WORK}/duplicate-keys
    exit 1
fi
rm -rf ${WORK}
