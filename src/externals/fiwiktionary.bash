#!/bin/bash
# Wiktionary dump is too big to store in version control, here's a script
# to fetch it instead.
FIWIKT_VERSION=latest
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
if ! test -f "$FWPREFIX.xml.bz2" ; then
    if ! wget "http://dumps.wikimedia.org/fiwiktionary/$FIWIKT_VERSION/$FWPREFIX.xml.bz2" ; then
        echo failed to dl
        exit 1
    fi
else
    echo "using existing $FWPREFIX.xml.bz2"
fi
if ! test -f "$FWPREFIX.xml" ; then
    bunzip2 -k -p "$FWPREFIX.xml.bz2"
else
    echo "using existing $FWPREFIX.xml"
fi
bash fiwikt2omorfi.bash "$FWPREFIX.xml"  > "$FWPREFIX.tsv.noheaders"
printf "lemma\thomonym\tnew_para\torigin\n" | cat - "$FWPREFIX.tsv.noheaders" \
    > "$FWPREFIX.tsv.unsort"
python ../python/tsvsort.py -i "$FWPREFIX.tsv.unsort" -o "$FWPREFIX.tsv"
python ../python/tsvmerge.py -i ../lexemes.tsv -m "$FWPREFIX.tsv" \
    -o ../lexemes+fiwikt.tsv
diff ../lexemes.tsv ../lexemes+fiwikt.tsv
echo if nothing broke just cp ../lexemes+fiwikt.tsv ../lexemes.tsv and
echo "do cd .. and make check"
