#!/bin/bash
# Wiktionary dump is too big to store in version control, here's a script
# to fetch it instead.
ENWIKT_VERSION=20181001
if test $# -eq 1 ; then
    ENWIKT_VERSION=$1
elif test $# -ge 2 ; then
    echo "Usage: $0 [VERSION_ID]"
    echo
    echo "VERSION_ID must be downloadable wiktionary version. If omitted,"
    echo "$ENWIKT_VERSION is used"
    exit 1
fi
EWPREFIX=fiwiktionary-$ENWIKT_VERSION-pages-articles
wget http://dumps.wikimedia.org/fiwiktionary/$ENWIKT_VERSION/$EWPREFIX.xml.bz2
bunzip $EWPREFIX.xml.bz2
bash fiwikt2omorfi.bash $EWPREFIX.articles.xml  > $EWPREFIX.tsv.unsort
python ../python/tsvsort.py -i $EWPREFIX.tsv.unsort -o $EWPREFIX.tsv.noheaders
echo "lemma\thomonym\tnew_para\torigin" | cat - $EWPREFIX.tsv.noheaders \
    > $EWPREFIX.tsv
python ../python/tsvmerge.py -m ../lexemes.tsv -i $EWPREFIX.tsv \
    -o ../lexemes+enwikt.tsv
diff ../lexemes.tsv ../lexemes+enwikt.tsv
echo if nothing broke just cp ../lexemes+enwikt.tsv ../lexemes.tsv and
echo do cd .. and make check
