#!/bin/bash
# Wiktionary dump is too big to store in version control, here's a script
# to fetch it instead.
ENWIKT_VERSION=latest
if test $# -eq 1 ; then
    ENWIKT_VERSION=$1
elif test $# -ge 2 ; then
    echo "Usage: $0 [VERSION_ID]"
    echo
    echo "VERSION_ID must be downloadable wiktionary version. If omitted,"
    echo "$ENWIKT_VERSION is used"
    exit 1
fi
EWPREFIX=enwiktionary-$ENWIKT_VERSION-pages-articles
if test -f "$EWPREFIX.xml.bz2" ; then
    echo "NB! using existing $EWPREFIX.xml.bz2"
elif ! wget "https://dumps.wikimedia.org/enwiktionary/$ENWIKT_VERSION/$EWPREFIX.xml.bz2" ; then
    echo Download failed
fi
if test -f "$EWPREFIX.xml" ; then
    echo "Using exitsing $EWPREFIX.xml"
else
    bunzip2 -k -p "$EWPREFIX.xml.bz2"
fi
bash enwikt2omorfi.bash "$EWPREFIX.xml"  > "$EWPREFIX.tsv.noheaders"
printf "lemma\thomonym\tnew_para\torigin\n" | cat - "$EWPREFIX.tsv.noheaders" \
    > "$EWPREFIX.tsv.unsort"
python ../python/tsvsort.py -i "$EWPREFIX.tsv.unsort" \
    -o "$EWPREFIX.tsv"
python ../python/tsvmerge.py -i ../lexemes.tsv -m "$EWPREFIX.tsv" \
    -o ../lexemes+enwikt.tsv
diff -u ../lexemes.tsv ../lexemes+enwikt.tsv
echo if nothing broke just cp ../lexemes+enwikt.tsv ../lexemes.tsv and
echo "do cd .. and make check"
