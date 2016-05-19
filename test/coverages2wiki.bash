#!/bin/bash

toplist=top-100-log
echo "## $(date --iso) coverages"
echo "## $(date --iso) " > ${toplist}
echo
for f in *.coveragelog; do
    corpus=${f%.coveragelog}
    echo "### ${corpus}"
    echo
    tokens=$(wc -l < ${corpus}.tokens)
    types=$(wc -l < ${corpus}.uniq.freqs)
    tokenmisses=$(awk '{SUM+=$1;} END {print SUM;}' < ${f})
    typemisses=$(wc -l < ${f})
    echo "| Feature | Coverage # | Coverage % | All |"
    echo "|:--------|-------:|---------:|----:|"
    echo "| Tokens  | $(($tokens - $tokenmisses)) | " \
        $(echo "scale=4; (1 - $tokenmisses / $tokens) * 100" | bc ) \
        "% | $tokens |"
    echo "| Types   | $(($types - $typemisses)) |" \
        $(echo "scale=4; (1 - $typemisses / $types) * 100" | bc ) \
        "% | $types |"
    echo
    echo "### ${corpus}" >> ${toplist}
    echo "#### 100 most common missing word-forms " >> ${toplist}
    echo >> ${toplist}
    echo "| Frequency | Word-form |" >> ${toplist}
    head -n 100 $f |\
        awk '{printf("| %s | %s |\n", $1, $2);}' >> ${toplist}
    echo >> ${toplist}
done
