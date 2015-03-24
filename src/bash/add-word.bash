#!/bin/bash

LEXFILE=lexemes.tsv

if test $# -lt 2 ; then
    echo "Usage: $0 LEMMA CLASS [SOURCE=omorfi]"
    exit 1
fi

LEMMA=$1
PARA=$2
SOURCE=omorfi
if test $# -ge 3 ; then
    SOURCE=$3
fi

cp -v ${LEXFILE} ${LEXFILE}~

# OBS! kots tn guessing was lost in github migration??

HN=1
if egrep "^$1" ${LEXFILE} | fgrep $2 ; then
    HN=$(egrep "^$1" ${LEXFILE} | fgrep $2 | tail -n 1 | cut -f 2)
    HN=$(($HN + 1))
fi
printf "%s\t%s\t%s\t%s\n" $LEMMA $HN $PARA $SOURCE >> ${LEXFILE}
head -n 1 < ${LEXFILE} > ${LEXFILE}~~
tail -n +2 < ${LEXFILE} | sort -k1,1  | LC_ALL=C uniq >> ${LEXFILE}~~
diff -u ${LEXFILE}~ ${LEXFILE}~~
mv ${LEXFILE}~~ ${LEXFILE}
echo Abovementioned addition was made, old version is still in ${LEXFILE}~
echo if all is fine, do commit the result immediately:
echo $'\t'git commit lexemes.tsv
echo to roll back changes:
echo $'\t'mv lexemes.tsv~ lexemes.tsv
