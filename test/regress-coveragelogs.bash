#!/bin/bash

if test $# != 2 ; then
    echo Usage: $0 OLDTESTDIR NAME
    exit 1
fi

echo > $2.regressions
echo > $2.developments
echo > $2.stable

for f in *.coveragelog ; do
    if test ! -f $1/$f ; then
        echo Skipping $f missing $1/$f
        continue
    fi
    sort $f > $f.sorted
    sort $1/$f > $f.$2.sorted
    comm -23 $f.sorted $f.$2.sorted >> $2.regressions
    comm -13 $f.sorted $f.$2.sorted >> $2.developments
    comm -12 $f.sorted $f.$2.sorted >> $2.stable
done
sort -nr $2.regressions > $2.regressions.sorted
sort -k 2 $2.regressions > $2.regressions.sortedk2
sort -nr $2.developments > $2.developments.sorted
sort -k 2 $2.developments > $2.developments.sortedk2
sort -nr $2.stable > $2.stable.sorted
sort -k 2 $2.stable > $2.stable.sortedk2

