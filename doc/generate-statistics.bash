#!/bin/bash
set -x
INDEX=statistics.markdown

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
head -n 8 config.log | tail -n 6 >> $INDEX
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
echo "| Paradigms per | UPOS |" >> $INDEX
echo "|----------:|:-----|" >> $INDEX
cut -f 3 src/lexemes.tsv |\
    fgrep -v 'new_para' |\
    fgrep -v '51' |\
    sort | uniq | cut -f 1 -d _ |\
    sort | uniq -c | sort -nr |\
    sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]$//' |\
    sed -e 's/ / | /' -e 's/^/| /' -e 's/$/ |/' >> $INDEX
echo >> $INDEX


function convert_coveragelog {
    if ! test -f $1 -o -f $3 ; then
        echo Cannot read from $1 or $3 >&2
        return 1
    fi
    HAPAX=1
    case $3 in
        *5grams*)
            HAPAX=8;;
        *jrc-fi*)
            HAPAX=2;;
        *OpenSubtitles2016.fi*)
            HAPAX=2;;
        *fiwiki*)
            HAPAX=2;;
    esac
    echo "### $2"
    echo
    tokens=$(awk "\$1 >= $HAPAX"' {SUM+=$1;} END {print SUM;}' < ${3})
    types=$(wc -l < ${3})
    tokenmisses=$(awk '{SUM+=$1;} END {print SUM;}' < ${1})
    typemisses=$(wc -l < ${1})
    echo "| Feature | Coverage # | Coverage % | All |"
    echo "|:--------|-----------:|-----------:|----:|"
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
echo "For list of common tokens not covered by the lexicon, see [the
most frequent missing tokens per
corpus](#Most-frequent-missing-tokens-per-corpus)." >> ${INDEX}
echo >> $INDEX
convert_coveragelog test/coverage-short.log "Combined coverages" \
    test/coverage-fast-alls.freqs >> $INDEX
echo "The coverages were measured with full lexicon, if you use the [smaller
lexicon coverages are slightly worse](#Smaller-lexicon-coverage)." >> $INDEX
echo >> $INDEX
convert_coveragelog test/coverage-blort.log "Smaller lexicon coverage" \
    test/coverage-fast-alls.freqs >> $INDEX
for f in test/*.coveragelog ; do
    convert_coveragelog $f "$(echo $f |\
        sed -e 's:test/::' -e 's/.coveragelog//')" \
        ${f%.coveragelog}.uniq.freqs >> $INDEX
done
echo >> $INDEX

# generate list of most common missing words
echo "## Most frequent missing tokens per corpus " >> ${INDEX}
echo >> $INDEX
echo "These are the most common tokens still left unrecognised by the
lexicon. Most of them should be foreign languages, codes and rubbish. These
are used from time to time improve the lexical coverage." >> $INDEX
echo >> $INDEX
for f in test/*coveragelog ; do
    corpus=${f%.coveragelog}
    echo "### ${corpus}" >> ${INDEX}
    echo >> ${INDEX}
    echo "| Frequency | Word-form |" >> ${INDEX}
    echo "|----------:|:----------|"
    head -n 100 $f |\
        awk '{printf("| %s | %s |\n", $1, $2);}' >> ${INDEX}
    echo >> ${INDEX}
done
echo >> $INDEX

echo "## Automata statistics" >> $INDEX
echo >> $INDEX
echo "The underlying language models are mostly represented by
[finite-state automata (FSAs)](https://en.wikipedia.org/wiki/Finite-state
automaton). The figures may give some indication of the speed and size of the
models in practical applications." >> $INDEX
echo >> $INDEX
for f in src/generated/omorfi.*.hfst ; do
    purpose=$(echo $f | sed -e 's:^.*omorfi\.::' -e 's/\.hfst$//')
    echo "### $purpose" >> $INDEX
    echo >> $INDEX
    echo "| Feature | Measure |" >> $INDEX
    echo "|:--------|--------:|" >> $INDEX
    ls -lh $f | cut -d ' ' -f 5 |\
        sed -e 's/^/| On-disk size | /' -e 's/$/ |/' >> $INDEX
    hfst-summarize $f | fgrep '# of' | fgrep -v '???' |\
        sed -e 's/^# of/| /' -e 's/:/ |/' -e 's/$/ |/' >> $INDEX
    echo >> $INDEX
done
