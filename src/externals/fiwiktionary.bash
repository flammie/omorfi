#!/bin/bash
# Wiktionary dump is too big to store in version control, here's a script
# to fetch it instead.
FIWIKT_VERSION=20121220
if test $# -eq 1 ; then
    FIWIKT_VERSION=$1
elif test $# -ge 2 ; then
    echo "Usage: $0 [VERSION_ID]"
    echo
    echo "VERSION_ID must be downloadable wiktionary version. If omitted,"
    echo "$FIWIKT_VERSION is used"
    exit 1
fi
wget http://dumps.wikimedia.org/fiwiktionary/$FIWIKT_VERSION/fiwiktionary-$FIWIKT_VERSION-pages-articles.xml.bz2
bunzip fiwiktionary-$FIWIKT_VERSION-pages-articles.xml.bz2
