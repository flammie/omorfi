#!/bin/bash
# joukahainen is too big to store in version control, here's a script
# to fetch it instead.
wget https://joukahainen.puimula.org/sanastot/joukahainen.xml.gz
gunzip joukahainen.xml.gz
bash joukahainen2omorfi.bash joukahainen.xml  > joukahainen.tsv.unsort
python ../python/tsvsort.py -i joukahainen.tsv.unsort -o joukahainen.tsv
python ../python/tsvmerge.py -m ../lexemes.tsv -i joukahainene.tsv \
    -o ../lexemes+joukahainen.tsv
diff ../lexemes.tsv ../lexemes+joukahainen.tsv
echo if nothing broke just cp ../lexemes+joukahainen.tsv ../lexemes.tsv and
echo do cd .. and make check
