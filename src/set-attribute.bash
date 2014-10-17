#!/bin/bash

LEXFILE=lexemes/lexemes.tsv

if test $# -lt 4 ; then
    echo "Usage: $0 LEMMA CLASS ATTRIBUTE=VALUE CATEGORY"
    exit 1
fi

ATTRIBUTEFILE=attributes/$4.tsv
if ! test -f ${ATTRIBUTEFILE} ; then
    echo "cannot find attribute category db for $2 in ${ATTRIBUTEFILE}"
    exit 2
fi

cp -v ${ATTRIBUTEFILE} ${ATTRIBUTEFILE}~

fgrep "$1	$2" ${LEXFILE} | sed -e "s/\$/	$3/" >> ${ATTRIBUTEFILE}

sort -k1,1 ${ATTRIBUTEFILE} | LC_ALL=C uniq > ${ATTRIBUTEFILE}~~
diff -u ${ATTRIBUTEFILE}~ ${ATTRIBUTEFILE}~~
cp ${ATTRIBUTEFILE}~~ ${ATTRIBUTEFILE}
echo Abovementioned addition was made, old version is still in ${LEXFILE}~
echo if all is fine, do commit the result immediately
