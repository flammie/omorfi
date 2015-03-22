#!/bin/bash
LEXFILE=lexemes.tsv
for f in attributes/*.tsv ; do
    echo $f...
    cut -f 1,2,3 $f | sort | uniq > keys.$(basename $f)
    if test -f fails.$(basename $f) ; then
        rm -v fails.$(basename $f)
    fi
    while read k ; do
        if ! fgrep -m 1 -- "$k" ${LEXFILE} > /dev/null ; then
            echo $k in $f is not valid, try >> fails.$(basename $f)
            egrep -m 80 -- "^"$(echo $k | awk '{print $1}') ${LEXFILE} >> fails.$(basename $f)
            echo -n '!'
        fi
    done < keys.$(basename $f)
    if test -e fails.$(basename $f) ; then
        echo there were inconsistencies in ${f}
        echo once fixed, delete fails.$(basename $f)
        exit 1
    fi
done

