#!/bin/bash

echo "= $(date --iso) ="
echo
for f in *.text; do
    echo "== ${f%.text} =="
    echo
    wfs=$(grep -c '^$' < ${f%text}anals)
    misses=$(wc -l < ${f%text}misses)
    echo "=== Coverage ==="
    echo
    echo "scale=4; (1 - $misses / $wfs) * 100" | bc
    echo
    echo "=== Missing word forms ==="
    echo
    echo "|| *Frequency* || *Word form* ||"
    head -n 100 ${f%text}misses |\
        sed -e 's/^ *//' -e 's/^[[:digit:]]*/ \0 || /' \
            -e 's/^/||/' -e 's/$/||/' -e 's/[[:space:]]*+?/ /'
    echo
done

