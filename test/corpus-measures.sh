#!/bin/bash
# requires an installation of <>.
# analyse and rank the common open source corpora
if ! test -f "fi-gutenberg.text" ; then
    echo "Fetching and unpacking gutenberg corpus, this may take a while..."
    fetch-gutenberg.bash "fi"
    unpack-gutenbergs.bash > "fi-gutenberg.text"
fi
if ! test -f "fiwiki.text" ; then
    echo "Fetching and unpacking fiwiki, this will take quite a while..."
    fetch-wikimedia.bash fiwiki
    unpack-wikimedia.bash fiwiki > fiwiki.text
fi
if ! test -f "fi-europarl.text" ; then
    echo "Fetching and unpacking europarl fi, this may take a while..."
    fetch-europarl.bash "fi"
    unpack-europarl.bash "fi" > "fi-europarl.text"
fi
for f in "fi-gutenberg.text" "fi-europarl.text" fiwiki.text ; do
    echo Testing $f
    apertium-destxt $f |\
        hfst-proc --xerox ../src/morphology.omor.hfst > ${f%text}anals
    fgrep '+?' ${f%text}anals | sort | uniq -c | sort -nr > ${f%text}misses
done

