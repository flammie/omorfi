#!/bin/bash
# joukahainen is too big to store in version control, here's a script
# to fetch it instead.
wget https://joukahainen.puimula.org/sanastot/joukahainen.xml.gz
gunzip joukahainen.xml.gz
bash joukahainen2omorfi.bash joukahainen.xml  > joukahainen.tsv.noheaders
printf "lemma\thomonym\tnew_para\torigin\n" | cat - joukahainen.tsv.noheaders\
    > joukahainen.tsv.unsort
python ../python/tsvsort.py -i joukahainen.tsv.unsort -o joukahainen.tsv
python ../python/tsvmerge.py -i ../lexemes.tsv -m joukahainen.tsv \
    -o ../lexemes+joukahainen.tsv
diff -u ../lexemes.tsv ../lexemes+joukahainen.tsv
echo if nothing broke just cp ../lexemes+joukahainen.tsv ../lexemes.tsv and
echo "do cd .. and make check"
