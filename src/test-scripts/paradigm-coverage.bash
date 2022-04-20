#!/bin/bash
LEXFILE=lexemes.tsv
PARAFILE=paradigms.tsv

WORK=$(mktemp -d -t omorfi-validate-database.XXXXXXXXXX)

echo checking for missing paradigms of ${LEXFILE} in $PARAFILE...
cut -f 3 ${LEXFILE} | sort | uniq > "${WORK}"/paradigms
cut -f 1 $PARAFILE | sort | uniq > "${WORK}/$(basename $PARAFILE).paradigms"
comm -23 "${WORK}"/paradigms "${WORK}/$(basename $PARAFILE).paradigms" > \
    "${WORK}/missing-para-$(basename $PARAFILE)"
while read -r k ; do
    echo MISSING "$k" is found in ${LEXFILE} but is not in $PARAFILE >> \
        "${WORK}"/fails.paradigms
    grep -F -m 1 -- "${k}	" $LEXFILE |\
        awk -F '\t' '{printf("%s\tfor example: %s\n", $3, $1);}' \
        >> "${WORK}"/fails.paradigms
    echo ADD "$k" into ${PARAFILE} >> "${WORK}"/fails.paradigms
done < "${WORK}/missing-para-$(basename $PARAFILE)"
comm -13 "${WORK}/paradigms" "${WORK}/$(basename $PARAFILE).paradigms" > \
    "${WORK}/extra-para-$(basename $PARAFILE)"
while read -r k ; do
    echo EXTRA "$k" is found in ${PARAFILE} but is not in $LEXFILE >> \
        "${WORK}"/fails.paradigms
    echo REMOVE "$k" from ${PARAFILE} >> \
        "${WORK}"/fails.paradigms
done < "${WORK}/extra-para-$(basename $PARAFILE)"
if test -e "${WORK}"/fails.paradigms ; then
    echo
    echo there are missing paradigms:
    cat "${WORK}"/fails.paradigms
    exit 1
fi
rm -rf "${WORK}"
