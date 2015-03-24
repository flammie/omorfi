#!/bin/bash
LEXFILE=lexemes.tsv
echo ${LEXFILE}...
if test -f duplicate-keys ; then
    rm -v duplicate-keys
fi
cut -f 1,2 ${LEXFILE} | LC_ALL=C sort > keys

LC_ALL=C uniq -c < keys |\
    awk '$1 > 1 {print;}' > duplicate-keys
if test -s duplicate-keys ; then
    echo ${LEXFILE} has duplicate keys in duplicate-keys
    exit 1
fi
sort < keys > lc-sort-keys
for f in attributes/*.tsv ; do
    echo $f...
    cut -f 1,2 $f | sort | uniq > keys.$(basename $f)
    if test -f fails.$(basename $f) ; then
        rm -v fails.$(basename $f)
    fi
    if test -f missingkeys.$(basename $f) ; then
        rm -v missingkeys.$(basename $f)
    fi
    comm -23 keys.$(basename $f) lc-sort-keys > missing-keys.$(basename $f)
    while read k ; do
        echo MISSING $k is not found in ${LEXFILE} but is in $f >> fails.$(basename $f)
        egrep -- "^${k/+/\\+}[[:space:]]" $f >> fails.$(basename $f)
        echo LOOK FOR $k in ${LEXEMES} >> fails.$(basename $f)
        egrep -- "^$(echo $k | awk '{print $1}')[[:space:]]" ${LEXFILE} >> fails.$(basename $f)
    done < missing-keys.$(basename $f)
    if test -e fails.$(basename $f) ; then
        echo
        echo there were inconsistencies in ${f}, see fails.$(basename $f)
        exit 1
    fi
done

