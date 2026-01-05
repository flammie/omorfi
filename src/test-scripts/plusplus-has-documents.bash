#!/bin/bash
LEXFILE=lexemes.tsv
DOCFILE=../docs/lexemes.markdown
WORK=$(mktemp -d -t omorfi-validate-database.XXXXXXXXXX)

echo checking for undocumented for omorfi++ in ${LEXFILE}...
fgrep 'omorfi++' ${LEXFILE} | cut -f 1,2 > ${WORK}/keys
while read w hn ; do
    if ! fgrep -m 1 -- $w $DOCFILE > /dev/null ; then
        echo MISSING $w is found in ${LEXFILE} but is not in $DOCFILE >> ${WORK}/fails.$(basename $DOCFILE)
        fgrep -- "${w}	" $LEXFILE | fgrep 'omorfi++' >> ${WORK}/fails.$(basename $DOCFILE)
        echo ADD $w into ${DOCFILE} >> ${WORK}/fails.$(basename $DOCFILE)
    fi
done < ${WORK}/keys
if test -e ${WORK}/fails.$(basename $DOCFILE) ; then
    echo
    echo there are undocumented ++ lexemes in ${DOCFILE}:
    cat ${WORK}/fails.$(basename $DOCFILE)
    exit 1
fi
rm -rf ${WORK}
