#!/bin/bash

echo "## $(date --iso) faithfulness"
echo
for f in *.faithlog; do
    corpus=${f%.faithlog}
    echo "### ${corpus}"
    echo
    tokens=$(wc -l < ${corpus}.conllx)
    types=$(wc -l < ${corpus}.cutted.freqs)
    tokenmisses=$(awk '{SUM+=$2;} END {print SUM;}' < ${f})
    typemisses=$(wc -l < ${f})
    echo "| Feature | Missed | Faithfulness | All |"
    echo "|:--------|-------:|---------:|----:|"
    echo "| Tokens  | $tokenmisses | " \
        $(echo "scale=4; (1 - $tokenmisses / $tokens) * 100" | bc ) \
        "% | $tokens |"
    echo "| Types   | $typemisses |" \
        $(echo "scale=4; (1 - $typemisses / $types) * 100" | bc ) \
        "% | $types |"
    echo
    echo "#### 100 most common mismatches "
    echo
    echo "| Mismatch TYPE | Frequency | Word form | FTB 3.1 | (First reading) |"
    head -n 100 $f |\
        awk -F '\t' '{printf("| %s | %s | %s | %s | %s |\n", $1, $2, $3, $4, $6);}'
    echo
done
