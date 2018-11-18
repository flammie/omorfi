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
wget http://dumps.wikimedia.org/enwiktionary/$ENWIKT_VERSION/enwiktionary-$ENWIKT_VERSION-pages-articles.xml.bz2
bunzip enwiktionary-$ENWIKT_VERSION-pages-articles.xml.bz2
