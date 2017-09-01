#!/bin/bash
if ! ${srcdir}/test-scripts/lemmas-match-regexes.py \
    --regex-file ${srcdir}/paradigms.tsv --input ${srcdir}/lexemes.tsv; then
    exit 1
fi
exit 0
