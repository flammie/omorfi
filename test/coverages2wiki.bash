#!/bin/bash

echo "## $(date --iso) coverages"
echo
for f in *.coveragelog; do
    corpus=${f%.coveragelog}
    echo "### ${corpus}"
    echo
    tokens=$(wc -l < ${corpus}.tokens)
    types=$(wc -l < ${corpus}.uniq.freqs)
    tokenmisses=$(awk '{SUM+=$1;} END {print SUM;}' < ${f})
    typemisses=$(wc -l < ${f})
    echo "| Feature | Missed | Coverage | All |"
    echo "|:--------|-------:|---------:|----:|"
    echo "| Tokens  | $tokenmisses | " \
        $(echo "scale=4; (1 - $tokenmisses / $tokens) * 100" | bc ) \
        "% | $tokens |"
    echo "| Types   | $typemisses |" \
        $(echo "scale=4; (1 - $typemisses / $types) * 100" | bc ) \
        "% | $types |"
    echo
    echo "#### 100 most common missing word-forms "
    echo
    echo "| Frequency | Word-form |"
    head -n 100 $f |\
        awk '{printf("| %s | %s |\n", $1, $2);}'
    echo
done
