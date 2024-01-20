#!/bin/bash
# fetch omorfi coverage corpus data
nc=16
function preprocess() {
    cat $@ > .tokenise
    split -l 500000 .tokenise
    for f in x?? ; do
        ../../src/python/omorfi-tokenise.py -i "$f" -a\
            ../../src/generated/omorfi.describe.hfst |\
        tr -s ' ' '\n'
    done
    rm -f .tokenise x??
}

function frequency_list() {
    cat $@ | sort | uniq -c | sort -nr
}

if ! which fetch-europarl.bash ; then
    echo missing bash-corpora, get:
    echo git clone git@github.com:flammie/bash-corpora.git
    echo make and install.
    exit 1
fi
if ! test -d corpora ; then
    mkdir -v corpora
fi
pushd corpora || exit 1
# europarl
echo europarl... corpus 1/$nc
if ! test -f "europarl-v7.fi-en.fi.uniq.freqs" ; then
    if ! test -f "europarl-v7.fi-en.fi.tokens" ; then
        if ! test -f europarl-v7.fi-en.fi.text ; then
            if ! test -f "fi-en.tgz" ; then
                echo fetch
                fetch-europarl.bash "fi" en
            fi
            echo unpack
            unpack-europarl.bash "fi" "fi" en> europarl-v7.fi-en.fi.text
        fi
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
        if ! test -f "fiwiki-latest-pages-articles.text" ; then
            if ! test -f "fiwiki-latest-pages-articles.xml.bz2" ; then
                echo fetch
                fetch-wikimedia.bash fiwiki
            fi
            echo unpack
            unpack-wikimedia.bash fiwiki > fiwiki-latest-pages-articles.text
        fi
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
        if ! test -f ftb3.1.conllx.gz ; then
            echo fetch
            wget "https://korp.csc.fi/download/finntreebank/finntreebank3-src/finntreebank3-src.zip"
        fi
        echo unpack
        unzip finntreebank3-src.zip
        mv finntreebank3-src/ftb3.1.conllx .
    fi
    echo tokenise
    grep -E -v '^<' < ftb3.1.conllx |\
        cut -f 2 > ftb3.1.tokens
    echo count
    frequency_list ftb3.1.tokens > ftb3.1.uniq.freqs
fi
if ! test -f ftb3.1.cutted.freqs ; then
    grep -E -v '^<' < ftb3.1.conllx | cut -f 2,3,6 | sort | uniq -c |\
        sort -nr > ftb3.1.cutted.freqs
fi

# gutenberg
echo gutenberg... corpus 4/$nc
echo "disabled since gutenberg has blocked their download access :-("
## if ! test -f "gutenberg-fi.uniq.freqs" ; then
##     if ! test -f "gutenberg-fi.tokens" ; then
##         if ! test -f "gutenberg-fi.text" ; the
##             echo fetch
##             fetch-gutenberg.bash "fi" txt
##             echo unpack
##             unpack-gutenbergs.bash  > "gutenberg-fi.text"
##         fi
##         echo tokenise
##         preprocess  "gutenberg-fi.text" > "gutenberg-fi.tokens"
##     fi
##     echo count
##     frequency_list gutenberg-fi.tokens > gutenberg-fi.uniq.freqs
##
## fi
# JRC acquis
echo JRC acquis... corpus 5/$nc
if ! test -f "jrc-fi.uniq.freqs" ; then
    if ! test -f "jrc-fi.tokens" ; then
        if ! test -f jrc-fi.text ; then
            if ! test -f "jrc-fi.tgz" ; then
                echo fetch
                fetch-jrc-acquis.bash "fi"
            fi
            echo unpack
            unpack-jrc-acquis.bash "fi" > "jrc-fi.text"
        fi
        echo tokenise
        preprocess < "jrc-fi.text" > "jrc-fi.tokens"
    fi
    echo count
    frequency_list jrc-fi.tokens > jrc-fi.uniq.freqs
fi

# FTB 1
echo FTB-1  ... corpus 6/$nc
if ! test -f "ftb1.uniq.freqs" ; then
    if ! test -f visk-sent_tab.txt ; then
        echo fetch
        wget "https://korp.csc.fi/download/finntreebank/finntreebank1-src/finntreebank1-src.zip"
        echo unpack
        unzip finntreebank1-src.zip
        cp finntreebank1-src/visk-sent_tab.txt .
    fi
    echo tokenise
    grep -E -v '^#' < visk-sent_tab.txt |\
        tr -s '\n' |\
        cut -f 2 > ftb1.tokens
    echo count
    frequency_list ftb1.tokens > ftb1.uniq.freqs
fi
if ! test -f ftb1.cutted.freqs ; then
    grep -E -v '^#' < visk-sent_tab.txt | tr -s '\n' |\
        cut -f 2,3,6 | sort | uniq -c | sort -nr > ftb1.cutted.freqs
fi

# UD-finnish
echo UD Finnish ... 7/$nc
if ! test -f "fi_tdt-ud.uniq.freqs" ; then
    if ! test -f "fi_tdt-ud-train.conllu" ; then
        if ! test -d UD_Finnish-TDT ; then
            git clone git@github.com:UniversalDependencies/UD_Finnish-TDT.git
        else
            pushd UD_Finnish-TDT || exit 1
            git pull
            popd || exit 1
        fi
        cp UD_Finnish-TDT/fi_tdt-ud-{train,dev,test}.conllu .
    fi
    echo tokenise
    cat fi_tdt-ud-{train,dev}.conllu | grep -E -v '^#' | tr -s '\n' |\
        cut -f 2 > "fi_tdt-ud.tokens"
    echo count
    frequency_list "fi_tdt-ud.tokens" > "fi_tdt-ud.uniq.freqs"
fi
echo UD Finnish-FTB ... 8/$nc
if ! test -f "fi_ftb-ud.uniq.freqs" ; then
    if ! test -f "fi_ftb-ud-train.conllu" ; then
        if ! test -d UD_Finnish-ftb ; then
            git clone git@github.com:UniversalDependencies/UD_Finnish-ftb.git
        else
            pushd UD_Finnish-ftb || exit 1
            git pull
            popd || exit 1
        fi
        cp UD_Finnish-ftb/fi_ftb-ud-{train,dev,test}.conllu .
    fi
    echo tokenise
    cat fi_ftb-ud-{train,dev}.conllu | grep -E -v '^#' | tr -s '\n' |\
        cut -f 2 > "fi_ftb-ud.tokens"
    echo count
    frequency_list "fi_ftb-ud.tokens" > "fi_ftb-ud.uniq.freqs"
fi

# Open subtitles
echo Open Subtitle 2018... corpus 9/$nc
if ! test -f "OpenSubtitles2018.fi.uniq.freqs" ; then
    if ! test -f "OpenSubtitles2018.fi.tokens" ; then
        if ! test -f "OpenSubtitles2018.fi.text" ; then
            if ! test -f "OpenSubtitles2018.raw.fi.gz" ; then
                echo fetch
                fetch-opensubtitles.bash "fi"
            fi
            echo unpack
            unpack-opensubtitles.bash "fi" > "OpenSubtitles2018.fi.text"
        fi
        echo tokenise
        preprocess < "OpenSubtitles2018.fi.text" > "OpenSubtitles2018.fi.tokens"
    fi
    echo count
    frequency_list OpenSubtitles2018.fi.tokens > OpenSubtitles2018.fi.uniq.freqs
fi
# tatoeba
echo Tatoeba fi... corpus 10/$nc
if ! test -f "tatoeba-fi.uniq.freqs" ; then
    if ! test -f "tatoeba-fi.tokens" ; then
        if ! test -f tatoeba-fi.text ; then
            if ! test -f sentences.tar.bz2 ; then
                echo fetch
                fetch-tatoeba.bash
            fi
            echo unpack
            unpack-tatoeba.bash "fin" > tatoeba-fi.text
        fi
        echo tokenise
        preprocess < tatoeba-fi.text > tatoeba-fi.tokens
    fi
    echo count
    frequency_list tatoeba-fi.tokens > tatoeba-fi.uniq.freqs
fi

# Turku Internet Parse Bank
echo Internet parse bank... corpus 11/$nc
echo "disabled since UTU has just removed internet parsebank"
## if ! test -f "5grams.uniq.freqs" ; then
##     if ! test -f "5grams.tokens" ; then
##         if ! test -f 5grams.text ; then
##             if ! test -f 5grams.01.txt.gz ; then
##                 echo fetch 1/4
##                 wget http://bionlp-www.utu.fi/fin-ngrams/fin-flat-ngrams/5grams.01.txt.gz
##             fi
##             if ! test -f 5grams.02.txt.gz ; then
##                 echo fetch 2/4
##                 wget http://bionlp-www.utu.fi/fin-ngrams/fin-flat-ngrams/5grams.02.txt.gz
##             fi
##             if ! test -f 5grams.03.txt.gz ; then
##                 echo fetch 3/4
##                 wget http://bionlp-www.utu.fi/fin-ngrams/fin-flat-ngrams/5grams.03.txt.gz
##             fi
##             if ! test -f 5grams.04.txt.gz ; then
##                 echo fetch 4/4
##                 wget http://bionlp-www.utu.fi/fin-ngrams/fin-flat-ngrams/5grams.04.txt.gz
##             fi
##             echo unpack
##             zcat 5grams.0{1,2,3,4}.txt.gz > 5grams.text
##         fi
##         echo tokenise
##         cat 5grams.text | tr ' ' '\n' | cut -d/ -f1 > 5grams.tokens
##     fi
##     echo count
##     frequency_list 5grams.tokens > 5grams.uniq.freqs
## fi

# Old language frequency lists
echo Vanhan kirjasuomen sanojen taajuuksia... corpus 12/$nc
echo Varhaisnykysuomen sanojen taajuuksia... corpus 13/$nc
echo "gone?"

# Unimorph-fin
echo Unimorph fin ... 14/$nc
if ! test -f "unimorph-fin.uniq.freqs" ; then
    if ! test -d fin ; then
        git clone git@github.com:unimorph/fin.git
    fi
    cat fin/fin.? > unimorph-fin.unimorphs
    cat unimorph-fin.unimorphs | cut -f 2 |\
        grep -F -v ' ' > "unimorph-fin.tokens"
    echo count
    frequency_list "unimorph-fin.tokens" > "unimorph-fin.uniq.freqs"
fi
# finer
echo finer ... 15/$nc
if ! test -f "finer.uniq.freqs" ; then
    if ! test -d finer-data ; then
        git clone git@github.com:mpsilfve/finer-data.git
    fi
    cut -f 1 finer-data/data/*.csv > finer.tokens
    echo count
    frequency_list "finer.tokens" > "finer.uniq.freqs"
    cp -v finer-data/data/*csv .
fi

# Turku ONE
echo turku ner corpse ... 16/$nc
if ! test -f "turku-ner.freqs" ; then
    if ! test -d turku-ner-corpus ; then
        git clone git@github.com:TurkuNLP/turku-ner-corpus
    fi
    cut -f 1 turku-ner-corpus/data/conll/train.tsv > turku-ner.tokens
    echo count
    frequency_list turku-ner.tokens > turku-ner.uniq.freqs
    cp -v turku-ner-corpus/data/conll/*.tsv .
fi
popd || exit 1

