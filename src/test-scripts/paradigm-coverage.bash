#!/bin/bash
LEXFILE=lexemes.tsv
MWEFILE=mwe.tsv
PARAFILE=paradigms.tsv

WORK=$(mktemp -d -t omorfi-validate-database.XXXXXXXXXX)

LEXEMES="${WORK}/lexemes"
LPARADIGMS="${WORK}/lexemes.paradigms"
RPARADIGMS="${WORK}/paradigms.paradigms"
MISSPARAS="${WORK}/missing.paradigms"
EXTRAPARAS="${WORK}/extra.paradigms"
FAILS="{WORK}/fails.paradigms"
cat ${LEXFILE} ${MWEFILE} > "${LEXEMES}"
echo checking for missing paradigms of ${LEXFILE} and ${MWEFILE} \
    in $PARAFILE...
cut -f 3 ${LEXEMES} | sort | uniq > "${LPARADIGMS}"
cut -f 1 ${PARAFILE} | sort | uniq > "${RPARADIGMS}"
comm -23 "${LPARADIGMS}" "${RPARADIGMS}" > "${MISSPARAS}"
while read -r k ; do
    echo MISSING "$k" is found in databases but is not in $PARAFILE >> \
        "${FAILS}"
    grep -F -m 1 -- "${k}	" "${LEXEMES}" |\
        awk -F '\t' '{printf("%s\tfor example: %s\n", $3, $1);}' \
        >> "${FAILS}"
    echo ADD "$k" into ${PARAFILE} >> "${FAILS}"
done < "${MISSPARAS}"
comm -13 "${LPARADIGMS}" "${RPARADIGMS}" > "${EXTRAPARAS}"
while read -r k ; do
    echo EXTRA "$k" is found in ${PARAFILE} but is not in databases >> \
        "${FAILS}"
    echo REMOVE "$k" from ${PARAFILE} >> "${FAILS}"
done < "${EXTRAPARAS}"
if test -e "${FAILS}" ; then
    echo
    echo there are missing or extra paradigms:
    cat "${FAILS}"
    exit 1
fi
rm -rf "${WORK}"
