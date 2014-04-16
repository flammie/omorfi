#!/bin/bash

LEXFILE=lexemes/lexemes.tsv

if test $# -lt 2 ; then
    echo "Usage: $0 LEMMA CLASS"
    exit 1
fi

cp -v ${LEXFILE} ${LEXFILE}~

case $2 in
    [0-9]*-[A-Z0]) python3 guess_missing.py --lemma=$1 --ktn=${2%-*} --kav=${2#*-} --output=${LEXFILE} --verbose;;
    [0-9]*) python3 guess_missing.py --lemma=$1 --ktn=$2 --output=${LEXFILE} --verbose;;
    [A-Z]*_*) python3 guess_missing.py --lemma=$1 --newpara=$2 --output=${LEXFILE} --verbose;;
esac

sort ${LEXFILE} | uniq > ${LEXFILE}~~
diff -u ${LEXFILE}~ ${LEXFILE}~~
cp ${LEXFILE}~~ ${LEXFILE}
echo Abovementioned addition was made, old version is still in ${LEXFILE}~
echo if all is fine, do commit the result immediately
