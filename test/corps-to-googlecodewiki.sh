#!/bin/bash

echo "= $(date --iso) ="
echo
for f in *.anals; do
    echo "== ${f%.anals} =="
    echo
    wfs=$(grep -c '^$' < ${f})
    misses=$(wc -l < ${f%anals}misses)
    uniqs=$(cut -f 1 < ${f} | sort | uniq | wc -l)
    uniqmisses=$(sort < ${f%anals}misses | uniq | wc -l)
    echo "=== Coverage ==="
    echo
    echo Total:
    echo "scale=4; (1 - $misses / $wfs) * 100" | bc
    echo Unique:
    echo "scale=4; (1 - $uniqmisses / $uniqs) * 100" | bc
    echo
    echo "=== Missing word forms ==="
    echo
    echo "|| *Frequency* || *Word form* ||"
    head -n 100 ${f%anals}misses |\
        sed -e 's/^ *//' -e 's/^[[:digit:]]*/ \0 || /' \
            -e 's/[^[:space:]]*+?.*$/ /' \
            -e 's/^/||/' -e 's/$/||/' 
    echo
done

