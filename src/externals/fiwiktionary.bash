#!/bin/bash
# Wiktionary dump is too big to store in version control, here's a script
# to fetch it instead.
FIWIKT_VERSION=20201120
if test $# -eq 1 ; then
    FIWIKT_VERSION=$1
elif test $# -ge 2 ; then
    echo "Usage: $0 [VERSION_ID]"
    echo
    echo "VERSION_ID must be downloadable wiktionary version. If omitted,"
    echo "$FIWIKT_VERSION is used"
    exit 1
fi
FWPREFIX=fiwiktionary-$FIWIKT_VERSION-pages-articles
wget http://dumps.wikimedia.org/fiwiktionary/$FIWIKT_VERSION/$FWPREFIX.xml.bz2
bunzip $FWPREFIX.xml.bz2
bash fiwikt2omorfi.bash $FWPREFIX.articles.xml  > $FWPREFIX.tsv.unsort
python ../python/tsvsort.py -i $FWPREFIX.tsv.unsort -o $FWPREFIX.tsv.noheaders
echo "lemma\thomonym\tnew_para\torigin" | cat - $FWPREFIX.tsv.noheaders \
    > $FWPREFIX.tsv
python ../python/tsvmerge.py -m ../lexemes.tsv -i $FWPREFIX.tsv \
    -o ../lexemes+fiwikt.tsv
diff ../lexemes.tsv ../lexemes+fiwikt.tsv
echo if nothing broke just cp ../lexemes+fiwikt.tsv ../lexemes.tsv and
echo do cd .. and make check
