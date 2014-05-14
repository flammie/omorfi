#!/bin/bash
# requires an installation of <>.
# analyse and rank the common open source corpora
fsa='-'

usage() {
    echo "$0 [OPTIONS...]"
    echo
    echo "  -t, --text=TFILE     read raw text from TFILE"
    echo "  -c, --conllx=CFILE   read connlx data from CFILE"
    echo
    echo If no files are specified we will glob them
}

for tf in apertium omor ftb3 ; do
    if test -r ../src/morphology.$tf.hfst ; then
        fsa="../src/morphology.$tf.hfst"
    fi
done
while test $# -gt 0 ; do
    case $1 in
        -t|--text)
            TEXTS="$TEXTS $2"
            shift ;;
        -c|--conllx)
            CONLLXS="$CONLLXS $2"
            shift ;;
        *)
            usage
            exit 1
            ;;
    esac
    shift 
done
if test -z $TEXTS ; then
    TEXTS=*.text
    CONLLXS=*.conllx
fi

function _preproc() {
    cat $@ | sed -e 's/[[:punct:]][[:space:][:punct:]]/ \0/g' \
        -e 's/[[:punct:]]\r\?$/ \0/' -e 's/^[[:punct:]]/\0 /' \
        -e 's/[[:space:]][[:punct:]]/\0 /g' -e 's/[[:space:]]/ /g' |\
        tr -s ' ' '\n'
}
preprocess=_preproc
if ! test -f "fi-gutenberg.text" ; then
    echo "Fetching and unpacking gutenberg corpus, this may take a while..."
    fetch-gutenberg.bash "fi" "txt"
    unpack-gutenbergs.bash > "fi-gutenberg.text"
fi
if ! test -f "fiwiki.text" ; then
    echo "Fetching and unpacking fiwiki, this will take quite a while..."
    fetch-wikimedia.bash fiwiki
    unpack-wikimedia.bash fiwiki > fiwiki.text
fi
if ! test -f "fi-europarl.text" ; then
    echo "Fetching and unpacking europarl fi, this may take a while..."
    fetch-europarl.bash "fi" en
    unpack-europarl.bash "fi" "fi" en > "fi-europarl.text"
fi
if ! test -f "fi-jrc-acquis.text" ; then
    echo "Fetching and unpacking JRC acquis fi, this may take a while..."
    fetch-jrc-acquis.bash "fi"
    unpack-jrc-acquis.bash "fi" > "fi-jrc-acquis.text"
fi
if ! test -f ftb3.1.conllx ; then
    echo "Fetching and unpacking ftb3.1, this may take a while..."
    wget "http://www.ling.helsinki.fi/kieliteknologia/tutkimus/treebank/sources/ftb3.1.conllx.gz"
    gunzip ftb3.1.conllx.gz
fi
for f in $TEXTS ; do
    echo Testing $f
    $preprocess $f | hfst-lookup -q $fsa > ${f%text}anals
done
for f in $CONLLXS ; do
    echo Testing $f
    tail -n +2 < $f | egrep -v '^</?s' | cut -f 2 | hfst-lookup -q $fsa > ${f%conllx}anals
done
