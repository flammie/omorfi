#!/bin/bash

INDEX=statistics.markdown
if test $# -ne 1 ; then
    echo Usage: $0 TESTDIR
    exit 1
fi


# build index page
echo "---" > $INDEX
echo "layout: page" >> $INDEX
echo "title: Statistics" >> $INDEX
echo "---" >> $INDEX
echo >> $INDEX
echo "# Statistics" >> $INDEX
echo >> $INDEX
echo "_These are semi-automatically generated statistics from omorfi
database._ The statistics are based on the actual data in the database tables
and the versions of whole analysed corpora and tools on this date." >> $INDEX
echo >> $INDEX
echo "Generation time was \`$(date --iso=hours)\`" >> $INDEX

echo "## Naïve coverages" >> $INDEX
echo >> $INDEX
echo "Naïve coverage is number of tokens (types) that receive one or more
non-heuristic readings divided by total number of tokens, i.e. how many words
are part of the lexical database." >> $INDEX

echo >> $INDEX

for f in $1/*.coveragelog ; do
    corpus=${f%.coveragelog}
    echo "### ${corpus}" >> $INDEX
    echo >> $INDEX
    tokens=$(wc -l < ${corpus}.tokens)
    types=$(wc -l < ${corpus}.uniq.freqs)
    tokenmisses=$(awk '{SUM+=$1;} END {print SUM;}' < ${f})
    typemisses=$(wc -l < ${f})
    echo "| Feature | Coverage # | Coverage % | All |" >> $INDEX
    echo "|:--------|-------:|---------:|----:|" >> $INDEX
    echo "| Tokens  | $(($tokens - $tokenmisses)) | " \
        $(echo "scale=4; (1 - $tokenmisses / $tokens) * 100" | bc ) \
        "% | $tokens |" >> $INDEX
    echo "| Types   | $(($types - $typemisses)) |" \
        $(echo "scale=4; (1 - $typemisses / $types) * 100" | bc ) \
        "% | $types |" >> $INDEX
    echo >> $INDEX
done

# generate list of most common missing words
echo "## $(date --iso) " >> ${INDEX}
for f in $1/*coveragelog ; do
    corpus=${f%.coveragelog}
    echo "### ${corpus}" >> ${INDEX}
    echo "#### 100 most common missing word-forms " >> ${INDEX}
    echo >> ${INDEX}
    echo "| Frequency | Word-form |" >> ${INDEX}
    head -n 100 $f |\
        awk '{printf("| %s | %s |\n", $1, $2);}' >> ${INDEX}
    echo >> ${INDEX}
done
