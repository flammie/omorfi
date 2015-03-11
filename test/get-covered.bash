#!/bin/bash
# fetch omorfi coverage corpus data
nc=5
function preprocess() {
    cat $@ | sed -e 's/[[:punct:]][[:space:][:punct:]]/ \0/g' \
        -e 's/[[:punct:]]\r\?$/ \0/' -e 's/^[[:punct:]]/\0 /' \
        -e 's/[[:space:]][[:punct:]]/\0 /g' -e 's/[[:space:]]/ /g' |\
        tr -s ' ' '\n'
}

function frequency_list() {
    cat $@ | sort | uniq -c | sort -nr
}

# europarl
echo europarl... corpus 1/$nc
if ! test -f "europarl-v7.fi-en.fi.uniq.freqs" ; then
    if ! test -f "europarl-v7.fi-en.fi.tokens" ; then
        if ! test -f "fi-en.tgz" ; then
            echo fetch
            fetch-europarl.bash "fi" en
        fi
        echo unpack
        unpack-europarl.bash "fi" "fi" en> europarl-v7.fi-en.fi.text
        echo tokenise
        preprocess europarl-v7.fi-en.fi.text > europarl-v7.fi-en.fi.tokens
    fi
    echo count
    frequency_list europarl-v7.fi-en.fi.tokens > europarl-v7.fi-en.fi.uniq.freqs
fi
# fiwiki
echo fiwiki... corpus 2/$nc
if ! test -f "fiwiki-latest-pages-articles.uniq.freqs" ; then
    if ! test -f "fiwiki-latest-pages-articles.tokens" ; then
        if ! test -f "fiwiki-latest-pages-articles.xml.bz2" ; then
            echo fetch
            fetch-wikimedia.bash fiwiki
        fi
        echo unpack
        unpack-wikimedia.bash fiwiki > fiwiki-latest-pages-articles.text
        echo tokenise
        preprocess fiwiki-latest-pages-articles.text > fiwiki-latest-pages-articles.tokens
    fi
    echo count
    frequency_list fiwiki-latest-pages-articles.tokens > fiwiki-latest-pages-articles.uniq.freqs
fi
# FTB 3.1
echo ftb3.1... corpus 3/$nc
if ! test -f ftb3.1.uniq.freqs ; then
    if ! test -f ftb3.1.conllx ; then
        echo fetch
        wget "http://www.ling.helsinki.fi/kieliteknologia/tutkimus/treebank/sources/ftb3.1.conllx.gz"
        echo unpack
        gunzip ftb3.1.conllx.gz
    fi
    echo tokenise
    egrep -v '^<' < ftb3.1.conllx |\
        cut -f 2 > ftb3.1.tokens
    echo count
    frequency_list ftb3.1.tokens > ftb3.1.uniq.freqs
fi
if ! test -f ftb3.1.cutted.freqs ; then
    egrep -v '^<' < ftb3.1.conllx | cut -f 2,3,6 | sort | uniq -c | sort > ftb3.1.cutted.freqs
fi

# gutenberg
echo gutenberg... corpus 4/$nc
if ! test -f "gutenberg-fi.uniq.freqs" ; then
    if ! test -f "gutenberg-fi.tokens" ; then
        echo fetch
        fetch-gutenberg.bash "fi" txt
        echo unpack
        unpack-gutenbergs.bash  > "gutenberg-fi.text"
        echo tokenise
        preprocess  "gutenberg-fi.text" > "gutenberg-fi.tokens"
    fi
    echo count
    frequency_list gutenberg-fi.tokens > gutenberg-fi.uniq.freqs

fi
# JRC acquis
echo JRC acquis... corpus 5/$nc
if ! test -f "jrc-fi.uniq.freqs" ; then
    if ! test -f "jrc-fi.tokens" ; then
        if ! test -f "jrc-fi.tgz" ; then
            echo fetch
            fetch-jrc-acquis.bash "fi"
        fi
        echo unpack
        unpack-jrc-acquis.bash "fi" > "jrc-fi.text"
        echo tokenise
        preprocess < "jrc-fi.text" > "jrc-fi.tokens"
    fi
    echo count
    frequency_list jrc-fi.tokens > jrc-fi.uniq.freqs
fi

