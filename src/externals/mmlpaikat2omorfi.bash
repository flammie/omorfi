#!/bin/bash

MMLZIP=Maanmittauslaitos_Tiedostopalvelu_REST-20231219T172033410205562.zip
if ! test -f "$MMLZIP" ; then
    echo you need to download $MMLZIP from avoindata.fi
    exit 1
fi
if ! test -d nimisto_oapif ; then
    unzip "$MMLZIP"
fi
bash maanmittauslaitos-gml.bash > paikat.tsv.noheaders
printf "lemma\thomonym\tnew_para\torigin\n" | cat - paikat.tsv.noheaders > paikat.tsv.unsort
../python/tsvsort.py -i paikat.tsv.unsort -o paikat.tsv
../python/tsvmerge.py -i ../lexemes.tsv -m paikat.tsv -o ../lexemes+paikat.tsv
echo you can diff -u ../lexemes.tsv ../lexemes+paikat.tsv and update now
