#!/bin/bash
LEXFILE=lexemes.tsv
WORK=$(mktemp -d -t omorfi-validate-database.XXXXXXXXXX)
if test -f ${WORK}/invalid-datatype ; then
    rm -v ${WORK}/invalid-datatype
fi

tail -n +2 < $LEXFILE | awk -F '\t' '$2 !~ /[[:digit:]]+/ {print;}' >> \
    ${WORK}/invalid-datatype
if test -s ${WORK}/invalid-datatype ; then
    echo The data in $LEXFILE does not match the database description
    echo see ${WORK}/invalid-datatype
fi
