#!/bin/bash
# fetch omorfi coverage corpus data
nc=9
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
    egrep -v '^<' < ftb3.1.conllx | cut -f 2,3,6 | sort | uniq -c | sort -nr > ftb3.1.cutted.freqs
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

# FTB 1
echo FTB-1 2014 ... corpus 6/$nc
if ! test -f "ftb1-2014.uniq.freqs" ; then
    if ! test -f ftb1-2014.tsv ; then
        echo fetch
        wget "http://www.ling.helsinki.fi/kieliteknologia/tutkimus/treebank/sources/ftb1-2014-beta.zip"
        echo unpack
        unzip ftb1-2014-beta.zip
        cp ftb1-2014-beta/ftb1-2014.tsv .
    fi
    echo tokenise
    egrep -v '^#' < ftb1-2014.tsv |\
        tr -s '\n' |\
        cut -f 2 > ftb1-2014.tokens
    echo count
    frequency_list ftb1-2014.tokens > ftb1-2014.uniq.freqs
fi
if ! test -f ftb1-2014.cutted.freqs ; then
    egrep -v '^#' < ftb1-2014.tsv | tr -s '\n' |\
        cut -f 2,3,6 | sort | uniq -c | sort -nr > ftb1-2014.cutted.freqs
fi

# UD-finnish
echo UD Finnish ... 7/$nc
if ! test -f "fi-ud-all.uniq.freqs" ; then
    if ! test -f "fi-ud-all.conllu" ; then
        git clone git@github.com:UniversalDependencies/UD_Finnish.git
        cat UD_Finnish/fi-ud-*.conllu > "fi-ud-all.conllu"
    fi
    echo tokenise
    egrep -v '^#' < "fi-ud-all.conllu" | tr -s '\n' |\
        cut -f 2 > "fi-ud-all.tokens"
    echo count
    frequency_list "fi-ud-all.tokens" > "fi-ud-all.uniq.freqs"
fi
echo UD Finnish-FTB ... 8/$nc
if ! test -f "fi_ftb-ud-all.uniq.freqs" ; then
    if ! test -f "fi_ftb-ud-all.conllu" ; then
        git clone git@github.com:UniversalDependencies/UD_Finnish-FTB.git
        cat UD_Finnish-FTB/fi_ftb-ud-*.conllu > "fi_ftb-ud-all.conllu"
    fi
    echo tokenise
    egrep -v '^#' < "fi_ftb-ud-all.conllu" | tr -s '\n' |\
        cut -f 2 > "fi_ftb-ud-all.tokens"
    echo count
    frequency_list "fi_ftb-ud-all.tokens" > "fi_ftb-ud-all.uniq.freqs"
fi

# Open subtitles
echo Open Subtitle 2016... corpus 9/$nc
if ! test -f "OpenSubtitles2016.fi.uniq.freqs" ; then
    if ! test -f "OpenSubtitles2016.fi.tokens" ; then
        if ! test -f "OpenSubtitles2016.raw.fi.gz" ; then
            echo fetch
            fetch-opensubtitles.bash "fi"
        fi
        echo unpack
        unpack-opensubtitles.bash "fi" > "OpenSubtitles2016.fi.text"
        echo tokenise
        preprocess < "OpenSubtitles2016.fi.text" > "OpenSubtitles2016.fi.tokens"
    fi
    echo count
    frequency_list OpenSubtitles2016.fi.tokens > OpenSubtitles2016.fi.uniq.freqs
fi

