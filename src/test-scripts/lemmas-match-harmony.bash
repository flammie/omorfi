#!/bin/bash
if ! ${srcdir}/test-scripts/lemmas-match-harmony.py \
        --input generated/master.tsv; then
    exit 1
fi
exit 0
