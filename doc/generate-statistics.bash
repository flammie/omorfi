#!/bin/bash
set -x
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
echo >> $INDEX
echo "## Lexical database" >> $INDEX
echo >> $INDEX
echo "The numbers are counted from the database, unique lexical items.
Depending on your definitions there may be ±1 % difference, e.g. with homonyms,
defective and doubled paradigms, etc." >> $INDEX
echo >> "There are total of \*$(wc -l < src/lexemes.tsv)\* in the database" \
    >> $INDEX
echo "### Per universal POS" >> $INDEX
echo >> $INDEX
echo "The universal parts-of-speech are described in [Universal dependencies 
UPOS documentation](http://universaldependencies.org/u/pos/index.html) and its
[Finnish UPOS 
definitions](http://universaldependencies.org/fi/pos/index.html)." >> $INDEX
echo >> $INDEX
echo "| Frequency | UPOS |" >> $INDEX
echo "|----------:|:-----|" >> $INDEX
cut -f 1 src/generated/master.tsv | sort | uniq -c | sort -nr | fgrep -v upos |\
    tr '|' ',' | sed -e 's/,/, /g' |\
    sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]$//' |\
    sed -e 's/ / | /' -e 's/^/| /' -e 's/$/ |/' >> $INDEX
echo >> $INDEX
echo "### Per sources of origin" >> $INDEX
echo >> $INDEX
echo "Sources of origin are:" >> $INDEX
echo "* *kotus*: [Nykysuomen sanalista]()" >> $INDEX
echo "* *joukahainen*: [Joukahainen]()" >> $INDEX
echo "* *omorfi*: curated by omorfi project itself" >> $INDEX
echo "* *omorfi++*: ...and documented in detail" >> $INDEX
echo "* *ftb3*: collected in [FinnTreeBank project]()" >> $INDEX
echo "* *finnwordnet*: collected in [FinnWordNet project]()" >> $INDEX
echo "* *unihu*: collected in University of Helsinki outside abovementioned
projects" >> $INDEX
echo >> $INDEX
echo "| Frequency | origin |" >> $INDEX
echo "|----------:|:-----|" >> $INDEX
cut -f 4 src/lexemes.tsv | sort | uniq -c | sort -nr | fgrep -v origin |\
    tr '|' ',' | sed -e 's/,/, /g' |\
    sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]$//' |\
    sed -e 's/ / | /' -e 's/^/| /' -e 's/$/ |/' >> $INDEX
echo >> $INDEX
echo "### Paradigms" >> $INDEX
echo >> $INDEX
echo "[Paradigms](paradigms.html) are the classes you need to separate the
lexemes into for inflection and some of the lexical features, such as UPOS.
You can see the [Paradigms](paradigms.html) generated documentation for some
automatically gathered details about each paradigm." >> $INDEX
echo >> $INDEX
echo "| Frequency | origin |" >> $INDEX
echo "|----------:|:-----|" >> $INDEX
cut -f 3 src/lexemes.tsv |\
    fgrep -v 'new_para' |\
    cut -f 1 -d _ | sort | uniq -c | sort -nr |\
    sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]$//' |\
    sed -e 's/ / | /' -e 's/^/| /' -e 's/$/ |/' >> $INDEX
echo >> $INDEX


function convert_coveragelog {
    echo "### $2"
    echo
    tokens=$(awk '{SUM+=$1;} END {print SUM;}' < ${3})
    types=$(wc -l < ${3})
    tokenmisses=$(awk '{SUM+=$1;} END {print SUM;}' < ${1})
    typemisses=$(wc -l < ${1})
    echo "| Feature | Coverage # | Coverage % | All |"
    echo "|:--------|-------:|---------:|----:|"
    echo "| Tokens  | $(($tokens - $tokenmisses)) | " \
        $(echo "scale=4; (1 - $tokenmisses / $tokens) * 100" | bc ) \
        "% | $tokens |"
    echo "| Types   | $(($types - $typemisses)) |" \
        $(echo "scale=4; (1 - $typemisses / $types) * 100" | bc ) \
        "% | $types |"
    echo
}

echo "## Naïve coverages" >> $INDEX
echo >> $INDEX
echo "Naïve coverage is number of tokens (types) that receive one or more
non-heuristic readings divided by total number of tokens, i.e. how many words
are part of the lexical database." >> $INDEX

echo >> $INDEX

convert_coveragelog $1/coverage-short.log "Combined coverages" \
    $1/coverage-fast-alls.freqs >> $INDEX

echo "The coverages were measured with full lexicon, if you use the [smaller
lexicon coverages are slightly worse](#Smaller-lexicon-coverage)." >> $INDEX

convert_coveragelog $1/coverage-blort.log "Smaller lexicon coverage" \
    $1/coverage-fast-alls.freqs>> $INDEX


for f in $1/*.coveragelog ; do
    convert_coveragelog $f "$(echo $f |\
        sed -e 's:test/::' -e 's/.coveragelog//')" \
        ${f%.coveragelog}.uniq.freqs >> $INDEX
done

echo "For list of common tokens not covered by the lexicon, see [the
most frequent missing tokens per
corpus](#Most-frequent-missing-tokens-per-corpus)." >> ${INDEX}

echo >> $INDEX


# generate list of most common missing words
echo "## Most frequent missing tokens per corpus " >> ${INDEX}
echo >> $INDEX
echo "These are the most common tokens still left unrecognised by the
lexicon. Most of them should be foreign languages, codes and rubbish. These
are used from time to time improve the lexical coverage." >> $INDEX
echo >> $INDEX
for f in $1/*coveragelog ; do
    corpus=${f%.coveragelog}
    echo "### ${corpus}" >> ${INDEX}
    echo >> ${INDEX}
    echo "| Frequency | Word-form |" >> ${INDEX}
    head -n 100 $f |\
        awk '{printf("| %s | %s |\n", $1, $2);}' >> ${INDEX}
    echo >> ${INDEX}
done
