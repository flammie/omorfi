#!/bin/bash

echo "= $(date --iso) ="
echo
for f in *.anals; do
    corpus=${f%.anals}
    fgrep '+?' < $f > ${corpus}.misses
    echo "== ${corpus} =="
    echo
    wfs=$(grep -c '^$' < ${f})
    misses=$(wc -l < ${corpus}.misses)
    uniqs=$(cut -f 1 < ${f} | sort | uniq | wc -l)
    uniqmisses=$(sort < ${corpus}.misses | sort | uniq | wc -l)
    echo "=== Coverage ==="
    echo
    echo Tokens: $wfs, misses: $misses
    echo "scale=4; (1 - $misses / $wfs) * 100" | bc |\
        sed -e 's/^/Token Coverage:/' -e 's/$/ %/'
    echo Unique tokens: $uniqs, misses: $uniqmisses
    echo "scale=4; (1 - $uniqmisses / $uniqs) * 100" | bc |\
        sed -e 's/^/Type Coverage:/' -e 's/$/ %/'
    echo
    echo "=== 100 most common missing word forms ==="
    echo
    echo "|| *Frequency* || *Word form* ||"
    sort < ${corpus}.misses | uniq -c | sort -nr |\
        head -n 100 |\
        sed -e 's/^ *//' -e 's/^[[:digit:]]*/ \0 || /' \
            -e 's/[^[:space:]]*+?.*$/ /' \
            -e 's/^/||/' -e 's/$/||/' 
    echo
done

