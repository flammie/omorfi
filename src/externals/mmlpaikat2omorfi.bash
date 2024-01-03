#!/bin/bash

MMLZIP=Maanmittauslaitos_Tiedostopalvelu_REST-20231219T1234567890.zip
if ! test -f "$MMLZIP" ; then
    echo you need to download $MMLZIP from avoindata.fi
    exit 1
fi
unzip "$MMLZIP"
bash maanmittauslaitos-gml.bash > paikat.tsv.noheaders
printf "lemma\thomonym\tnew_para\torigin\n" | cat - paikat.tsv.noheaders > paikat.tsv.unsort
../python/tsvsort.py -i paikat.tsv.unsort -o paikat.tsv
../python/tsvmerge.py -i ../lexemes.tsv -m paikat.tsv -o ../lexemes+paikat.tsv
echo you can diff -u ../lexemes.tsv ../lexemes+paikat.tsv and update now
 2013  ls
 2014  man unzip
 2015  for f in nimisto_oapif/places/etrs89/gml/places_202*; do mkdir $(basename $f) ; unzip -d $(basename $f) $f; done
 2016  less places_2023_01.zip/places.xml
 2017  xmllint -format places_2023_01.zip/places.xml | less
 2018  egrep -o '<language>...<' places_2023_01.zip/places.xml | sort | uniq
 2019  xmllint -format places_2023_01.zip/places.xml | less
 2020* egrep -o '<spelling>.*</language>' places_2023_01.zip/places.xml | sed
 2021  cp ~/github/flammie/apevis-xslt/monodix2html.xslt gml2omorfi.xslt
 2022  xmllint -format places_2023_01.zip/places.xml | less
 2023  less ~/github/flammie/apevis-xslt/monodix2html.xslt
 2024  xmllint -format places_2023_01.zip/places.xml | less
 2025  less ~/github/flammie/apevis-xslt/monodix2md.xslt
 2026  xsltproc
 2027  xsltproc gml2omorfi.xslt places_2023_01.zip/places.xml
 2028  less ~/github/flammie/apevis-xslt/monodix2md.xslt
 2029  xmllint -format places_2023_01.zip/places.xml | less
 2030  saxon9-transform
 2031  saxon9-transform -s:places_2023_01.zip/places.xml gml2omorfi.xslt
 2032  saxon9-transform -s:places_2023_01.zip/places.xml gml2omorfi.xslt | head
 2033  ls
 2034  rm *.xsd
 2035  ls
 2036  less enwiktionary-20221220-pages-articles.tsv
 2037  less enwiktionary-20221220-pages-articles.tsv.unsort
 2038  less enwiktionary-latest-pages-articles.tsv.unsort
 2039  less enwikt2omorfi.bash
 2040  less enwiktionary-latest-pages-articles.tsv.unsort
 2041  mupdf Nimiston_GML-tiedostotuotteet_OAPIF-skeema.pdf
 2042  for d in places_* ; do saxon9-transform -s:"$d/places.xml" gml2omorfi.xslt ; done | tee places.list
 2043  less enwikt2omorfi.bash
 2044  less ../lexemes.tsv
 2045  less enwikt2omorfi.bash
 2046  less ../lexemes.tsv
 2047  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/'
 2048  less ../lexemes.tsv
 2049  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/'
 2050  less ../lexemes.tsv
 2051  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/'
 2052  less ../lexemes.tsv
 2053  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/metsä_fin/metsä	PROPN	PROPN_HÖPÖTTÄJÄ/'
 2054  less ../lexemes.tsv
 2055  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/'
 2056  less ../lexemes.tsv
 2057  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/'
 2058  less ../lexemes.tsv
 2059  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/'
 2060  less ../lexemes.tsv
 2061  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/'
 2062  less ../lexemes.tsv
 2063  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/'
 2064  less ../lexemes.tsv
 2065  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/'
 2066  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/'
 2067  less ../lexemes.tsv
 2068  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/'
 2069  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/'
 2070  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*)i/\1i	PROPN	PROPN_RUUHI/'
 2071  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i/\1i	PROPN	PROPN_RUUHI/'
 2072  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/'
 2073  less ../lexemes.tsv
 2074  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/'
 2075  less ../lexemes.tsv
 2076  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/
 2077  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/'
 2078  less ../lexemes.tsv
 2079  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/'
 2080  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/'
 2081  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/'
 2082  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/'
 2083  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/'
 2084  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' | fgrep -v PROPN_
 2085  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN_ZEN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' | fgrep -v PROPN_
 2086  less ../lexemes.tsv
 2087  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN_ZEN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' -e 's/uo_fin/uo	PROPN	PROPN_VUO/' | fgrep -v PROPN_
 2088  less ../lexemes.tsv
 2089  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN_ZEN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' -e 's/uo_fin/uo	PROPN	PROPN_VUO/' -e 's/maa_fin/maa	PROPN	PROPN_MAA/' -e 's/park_fin/park	PROPN	PROPN_PUNK/' | fgrep -v PROPN_
 2090  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN_ZEN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' -e 's/uo_fin/uo	PROPN	PROPN_VUO/' -e 's/maa_fin/maa	PROPN	PROPN_MAA/' -e 's/park_fin/park	PROPN	PROPN_PUNK/' -e 's/eo_fin/eo	PROPN	PROPN_TUOMIO/' | fgrep -v PROPN_
 2091  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN_ZEN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' -e 's/uo_fin/uo	PROPN	PROPN_VUO/' -e 's/maa_fin/maa	PROPN	PROPN_MAA/' -e 's/park_fin/park	PROPN	PROPN_PUNK/' -e 's/eo_fin/eo	PROPN	PROPN_TUOMIO/' -e 's/museet_swe/museet	PROPN	PROPN_PUNK/' -e 's/landet_swe/lander	PROPN	PROPN_PUNK/' | fgrep -v PROPN_
 2092  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN_ZEN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' -e 's/uo_fin/uo	PROPN	PROPN_VUO/' -e 's/maa_fin/maa	PROPN	PROPN_MAA/' -e 's/park_fin/park	PROPN	PROPN_PUNK/' -e 's/eo_fin/eo	PROPN	PROPN_TUOMIO/' -e 's/museet_swe/museet	PROPN	PROPN_PUNK/' -e 's/landet_swe/lander	PROPN	PROPN_PUNK/' -e 's/and_swe/and	PROPN	PROPN_PUNK/'  | fgrep -v PROPN_
 2093  less ../lexemes.tsv
 2094  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN_ZEN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' -e 's/uo_fin/uo	PROPN	PROPN_VUO/' -e 's/maa_fin/maa	PROPN	PROPN_MAA/' -e 's/park_fin/park	PROPN	PROPN_PUNK/' -e 's/eo_fin/eo	PROPN	PROPN_TUOMIO/' -e 's/museet_swe/museet	PROPN	PROPN_PUNK/' -e 's/landet_swe/lander	PROPN	PROPN_PUNK/' -e 's/and_swe/and	PROPN	PROPN_PUNK/'  -e s'/ohi_fin/ohi	PROPN	PROPN_TULI/' | fgrep -v PROPN_
 2095  less ../lexemes.tsv
 2096  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN_ZEN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' -e 's/uo_fin/uo	PROPN	PROPN_VUO/' -e 's/maa_fin/maa	PROPN	PROPN_MAA/' -e 's/park_fin/park	PROPN	PROPN_PUNK/' -e 's/eo_fin/eo	PROPN	PROPN_TUOMIO/' -e 's/museet_swe/museet	PROPN	PROPN_PUNK/' -e 's/landet_swe/lander	PROPN	PROPN_PUNK/' -e 's/and_swe/and	PROPN	PROPN_PUNK/'  -e s'/ohi_fin/ohi	PROPN	PROPN_TULI/' -e 's/ale_fin/ale	PROPN	PROPN_NALLE/' | fgrep -v PROPN_
 2097  less ../lexemes.tsv
 2098  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN_ZEN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' -e 's/uo_fin/uo	PROPN	PROPN_VUO/' -e 's/maa_fin/maa	PROPN	PROPN_MAA/' -e 's/park_fin/park	PROPN	PROPN_PUNK/' -e 's/eo_fin/eo	PROPN	PROPN_TUOMIO/' -e 's/museet_swe/museet	PROPN	PROPN_PUNK/' -e 's/landet_swe/lander	PROPN	PROPN_PUNK/' -e 's/and_swe/and	PROPN	PROPN_PUNK/'  -e s'/ohi_fin/ohi	PROPN	PROPN_TULI/' -e 's/ale_fin/ale	PROPN	PROPN_NALLE/' -e 's/skär_swe/skär	PROPN	PROPN_ZEN/' | fgrep -v PROPN_
 2099  less ../lexemes.tsv
 2100  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN_ZEN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' -e 's/uo_fin/uo	PROPN	PROPN_VUO/' -e 's/maa_fin/maa	PROPN	PROPN_MAA/' -e 's/park_fin/park	PROPN	PROPN_PUNK/' -e 's/eo_fin/eo	PROPN	PROPN_TUOMIO/' -e 's/museet_swe/museet	PROPN	PROPN_PUNK/' -e 's/landet_swe/lander	PROPN	PROPN_PUNK/' -e 's/and_swe/and	PROPN	PROPN_PUNK/'  -e s'/ohi_fin/ohi	PROPN	PROPN_TULI/' -e 's/ale_fin/ale	PROPN	PROPN_NALLE/' -e 's/skär_swe/skär	PROPN	PROPN_ZEN/' -e 's/lma_fin/lma	PROPN	PROPN_VOIMA/' | fgrep -v PROPN_
 2101  less ../lexemes.tsv
 2102  cat places.list | grep -v ' '| sed -e 's/kko_fin/kko	PROPN	PROPN_UKKO/' -e 's/koski_fin/koski	PROPN	PROPN_ONNI/' -e 's/niemi_fin/niemi	PROPN	PROPN_TAIMI/' -e 's/lampi_fin/lampi	PROPN	PROPN_SAMPI/' -e 's/järvi_fin/järvi	PROPN	PROPN_KIVI/' -e 's/mäki_fin/mäki	PROPN	PROPN_KÄKI/' -e 's/vuori_fin/vuori	PROPN	PROPN_RUUHI/' -e 's/lahti_fin/lahti	PROPN	PROPN_LAHTI/' -e 's/sto_fin/sto	PROPN	PROPN_TALO/' -e 's/ä_fin/ä	PROPN	PROPN_HÖPÖTTÄJÄ/' -e 's/\(a.*\)en_swe/\1en	PROPN	PROPN_PUNK/' -e 's/en_swe/en	PROPN	PROPN_ZEN/' -e 's/saari_fin/saari	PROPN	PROPN_RUUHI/' -e 's/tuuli_fin/tuuli	PROPN	PROPN_RUUHI/' -e 's/io_fin/io	PROPN	PROPN_TUOMIO/' -e 's/nta_fin/nta	PROPN	PROPN_KUTSUNTA/' -e 's/\(.*a\)nen_fin/\1nen	PROPN	PROPN_AAKKOSTAMINEN/' -e 's/nen_fin/nen	PROPN	PROPN_KYLKIÄINEN/' -e 's/tty_fin/tty	PROPN	PROPN_PYTTY/' -e 's/y_fin/y	PROPN	PROPN_KÄRRY/' -e 's/\(a.*\)i_fin/\1i	PROPN	PROPN_RUUHI/' -e 's/u_fin/u	PROPN	PROPN_ASU/' -e 's/la_fin/la	PROPN	PROPN_KITARA/' -e 's/berg_swe/berg	PROPN	PROPN_ZEN/' -e 's/vik_swe/vik	PROPN	PROPN_ZEN/' -e 's/berget_swe/berget	PROPN	PROPN_ZEN/' -e 's/byn_swe/byn	PROPN	PROPN_ZEN/' -e 's/by_swe/by	PROPN	PROPN_KÄRRY/' -e 's/berga_swe/berga	PROPN	PROPN_KITARA/' -e 's/lto_fin/lto	PROPN	PROPN_KIELTO/' -e 's/gård_swe/gård	PROPN	PROPN_PUNK/' -e 's/uo_fin/uo	PROPN	PROPN_VUO/' -e 's/maa_fin/maa	PROPN	PROPN_MAA/' -e 's/park_fin/park	PROPN	PROPN_PUNK/' -e 's/eo_fin/eo	PROPN	PROPN_TUOMIO/' -e 's/museet_swe/museet	PROPN	PROPN_PUNK/' -e 's/landet_swe/lander	PROPN	PROPN_PUNK/' -e 's/and_swe/and	PROPN	PROPN_PUNK/'  -e s'/ohi_fin/ohi	PROPN	PROPN_TULI/' -e 's/ale_fin/ale	PROPN	PROPN_NALLE/' -e 's/skär_swe/skär	PROPN	PROPN_ZEN/' -e 's/lma_fin/lma	PROPN	PROPN_VOIMA/' -e 's/notko_fin/notko	PROPN	PROPN_TALO/' | fgrep -v PROPN_
 2103  bash maanmittauslaitos-gml.bash
 2104  less ../lexemes.tsv
 2105  bash maanmittauslaitos-gml.bash
 2106  less ../lexemes.tsv
 2107  bash maanmittauslaitos-gml.bash
 2108  less ../lexemes.tsv
 2109  bash maanmittauslaitos-gml.bash
 2110  less ../lexemes.tsv
 2111  bash maanmittauslaitos-gml.bash
 2112  less ../lexemes.tsv
 2113  bash maanmittauslaitos-gml.bash
 2114  less ../lexemes.tsv
 2115  bash maanmittauslaitos-gml.bash
 2116  less ../lexemes.tsv
 2117  bash maanmittauslaitos-gml.bash
 2118  less ../lexemes.tsv
 2119  bash maanmittauslaitos-gml.bash
 2120  less ../lexemes.tsv
 2121  bash maanmittauslaitos-gml.bash
 2122  less ../lexemes.tsv
 2123  bash maanmittauslaitos-gml.bash
 2124  less ../lexemes.tsv
 2125  bash maanmittauslaitos-gml.bash
 2126  less ../lexemes.tsv
 2127  bash maanmittauslaitos-gml.bash
 2128  less ../lexemes.tsv
 2129  bash maanmittauslaitos-gml.bash
 2130  less ../lexemes.tsv
 2131  bash maanmittauslaitos-gml.bash
 2132  less ../lexemes.tsv
 2133  bash maanmittauslaitos-gml.bash
 2134  less ../lexemes.tsv
 2135  bash maanmittauslaitos-gml.bash
 2136  less ../lexemes.tsv
 2137  bash maanmittauslaitos-gml.bash
 2138  less ../lexemes.tsv
 2139  bash maanmittauslaitos-gml.bash
 2140  less ../lexemes.tsv
 2141  bash maanmittauslaitos-gml.bash
 2142  less ../lexemes.tsv
 2143  bash maanmittauslaitos-gml.bash
 2144  less ../lexemes.tsv
 2145  bash maanmittauslaitos-gml.bash
 2146  less ../lexemes.tsv
 2147  bash maanmittauslaitos-gml.bash
 2148  less ../lexemes.tsv
 2149  bash maanmittauslaitos-gml.bash
 2150  less ../lexemes.tsv
 2151  bash maanmittauslaitos-gml.bash
 2152  less ../lexemes.tsv
 2153  bash maanmittauslaitos-gml.bash
 2154  less ../lexemes.tsv
 2155  bash maanmittauslaitos-gml.bash
 2156  less ../lexemes.tsv
 2157  bash maanmittauslaitos-gml.bash
 2158  less ../lexemes.tsv
 2159  bash maanmittauslaitos-gml.bash
 2160  less ../lexemes.tsv
 2161  bash maanmittauslaitos-gml.bash
 2162  less ../lexemes.tsv
 2163  bash maanmittauslaitos-gml.bash
 2164  less ../lexemes.tsv
 2165  bash maanmittauslaitos-gml.bash
 2166  less ../lexemes.tsv
 2167  bash maanmittauslaitos-gml.bash
 2168  less ../lexemes.tsv
 2169  bash maanmittauslaitos-gml.bash
 2170  less ../lexemes.tsv
 2171  bash maanmittauslaitos-gml.bash
 2172  less ../lexemes.tsv
 2173  bash maanmittauslaitos-gml.bash
 2174  less ../lexemes.tsv
 2175  bash maanmittauslaitos-gml.bash
 2176  less ../lexemes.tsv
 2177  bash maanmittauslaitos-gml.bash
 2178  less ../lexemes.tsv
 2179  bash maanmittauslaitos-gml.bash
 2180  less ../lexemes.tsv
 2181  bash maanmittauslaitos-gml.bash
 2182  less ../lexemes.tsv
 2183  bash maanmittauslaitos-gml.bash
 2184  less ../lexemes.tsv
 2185  bash maanmittauslaitos-gml.bash
 2186  less ../lexemes.tsv
 2187  bash maanmittauslaitos-gml.bash
 2188  less ../lexemes.tsv
 2189  bash maanmittauslaitos-gml.bash
 2190  less ../lexemes.tsv
 2191  bash maanmittauslaitos-gml.bash
 2192  less ../paradigms.tsv
 2193  bash maanmittauslaitos-gml.bash
 2194  less ../paradigms.tsv
 2195  less ../lexemes.tsv
 2196  bash maanmittauslaitos-gml.bash
 2197  less ../lexemes.tsv
 2198  bash maanmittauslaitos-gml.bash
 2199  less ../lexemes.tsv
 2200  bash maanmittauslaitos-gml.bash
 2201  less ../lexemes.tsv
 2202  bash maanmittauslaitos-gml.bash
 2203  less ../lexemes.tsv
 2204  bash maanmittauslaitos-gml.bash
 2205  less ../lexemes.tsv
 2206  bash maanmittauslaitos-gml.bash
 2207  less ../lexemes.tsv
 2208  bash maanmittauslaitos-gml.bash
 2209  less ../lexemes.tsv
 2210  bash maanmittauslaitos-gml.bash
 2211  less ../lexemes.tsv
 2212  bash maanmittauslaitos-gml.bash
 2213  less ../lexemes.tsv
 2214  bash maanmittauslaitos-gml.bash
 2215  less ../lexemes.tsv
 2216  bash maanmittauslaitos-gml.bash
 2217  less ../lexemes.tsv
 2218  bash maanmittauslaitos-gml.bash
 2219  less ../lexemes.tsv
 2220  bash maanmittauslaitos-gml.bash
 2221  less ../lexemes.tsv
 2222  bash maanmittauslaitos-gml.bash
 2223  less ../lexemes.tsv
 2224  bash maanmittauslaitos-gml.bash
 2225  less ../lexemes.tsv
 2226  bash maanmittauslaitos-gml.bash
 2227  less ../lexemes.tsv
 2228  bash maanmittauslaitos-gml.bash
 2229  less ../lexemes.tsv
 2230  bash maanmittauslaitos-gml.bash
 2231  less ../lexemes.tsv
 2232  bash maanmittauslaitos-gml.bash
 2233  less ../lexemes.tsv
 2234  bash maanmittauslaitos-gml.bash
 2235  less ../lexemes.tsv
 2236  bash maanmittauslaitos-gml.bash
 2237  less ../lexemes.tsv
 2238  bash maanmittauslaitos-gml.bash
 2239  less ../lexemes.tsv
 2240  bash maanmittauslaitos-gml.bash
 2241  less ../lexemes.tsv
 2242  bash maanmittauslaitos-gml.bash
 2243  less ../lexemes.tsv
 2244  bash maanmittauslaitos-gml.bash
 2245  less ../lexemes.tsv
 2246  bash maanmittauslaitos-gml.bash
 2247  less ../lexemes.tsv
 2248  bash maanmittauslaitos-gml.bash
 2249  less ../lexemes.tsv
 2250  bash maanmittauslaitos-gml.bash
 2251  less ../lexemes.tsv
 2252  gvim maanmittauslaitos-gml.bash
 2253  less ../lexemes.tsv
 2254  gvim maanmittauslaitos-gml.bash
 2255  bash maanmittauslaitos-gml.bash
 2256  less ../lexemes.tsv
 2257  bash maanmittauslaitos-gml.bash
 2258  less ../lexemes.tsv
 2259  bash maanmittauslaitos-gml.bash
 2260  less ../lexemes.tsv
 2261  bash maanmittauslaitos-gml.bash
 2262  less ../lexemes.tsv
 2263  bash maanmittauslaitos-gml.bash
 2264  less ../lexemes.tsv
 2265  bash maanmittauslaitos-gml.bash
 2266  less ../lexemes.tsv
 2267  bash maanmittauslaitos-gml.bash
 2268  less ../lexemes.tsv
 2269  bash maanmittauslaitos-gml.bash
 2270  less ../lexemes.tsv
 2271  bash maanmittauslaitos-gml.bash
 2272  less ../lexemes.tsv
 2273  bash maanmittauslaitos-gml.bash
 2274  less enwiktionary.bash
 2275  less enwikt2omorfi.bash
 2276  bash maanmittauslaitos-gml.bash > paikat.tsv.unsort
 2277  printf "lemma\thomonym\tnew_para\torigin\n" | cat - paikat.tsv.unsort > paikat.tsv.headers
 2278  ../python/tsvsort.py -i paikat.tsv.headers -o paikat.tsv
 2279  ../python/tsvmerge.py -i ../lexemes.tsv -m paikat.tsv -o ../lexemes+paikat.tsv
 2280  diff -u ../lexemes.tsv ../lexemes+paikat.tsv
 2281  diff -u ../lexemes.tsv ../lexemes+paikat.tsv | less
 2282  less paikat.tsv
 2283  less paikat.tsv.headers
 2284  less paikat.tsv.unsort
 2285  bash maanmittauslaitos-gml.bash
 2286  bash maanmittauslaitos-gml.bash > paikat.tsv.unsort
 2287  printf "lemma\thomonym\tnew_para\torigin\n" | cat - paikat.tsv.unsort > paikat.tsv.headers
 2288  cat paikat.tsv.headers
 2289  ../python/tsvsort.py -i paikat.tsv.headers -o paikat.tsv
 2290  ../python/tsvmerge.py -i ../lexemes.tsv -m paikat.tsv -o ../lexemes+paikat.tsv
 2291  diff -u ../lexemes.tsv ../lexemes+paikat.tsv | less
 2292  less ../lexemes.tsv
 2293  bash maanmittauslaitos-gml.bash > paikat.tsv.unsort
 2294  printf "lemma\thomonym\tnew_para\torigin\n" | cat - paikat.tsv.unsort > paikat.tsv.headers
 2295  ../python/tsvsort.py -i paikat.tsv.headers -o paikat.tsv
 2296  ../python/tsvmerge.py -i ../lexemes.tsv -m paikat.tsv -o ../lexemes+paikat.tsv
 2297  bash maanmittauslaitos-gml.bash > paikat.tsv.unsort
 2298  printf "lemma\thomonym\tnew_para\torigin\n" | cat - paikat.tsv.unsort > paikat.tsv.headers
 2299  ../python/tsvsort.py -i paikat.tsv.headers -o paikat.tsv
 2300  ../python/tsvmerge.py -i ../lexemes.tsv -m paikat.tsv -o ../lexemes+paikat.tsv
 2301  cd ..
 2302  cp lexemes+paikat.tsv lexemes.tsv
 2303  cd ..
 2304  make
 2305  less src/lexemes.tsv
 2306  vim src/attributes/blacklisted.tsv
 2307  make
 2308  less src/lexemes.tsv
 2309  less src/paradigms.tsv
 2310  vim src/lexemes.tsv
 2311  sed -i -e 's/PROPN_VUO /PROPN_VUO/' src/lexemes.tsv
 2312  make
 2313  cd src/externals/
 2314  history
 2315  bash mmlpaikat2omorfi.bash
 2316  cd ..
 2317  cp lexemes+paikat.tsv lexemes.tsv
 2318  cd ..
 2319  make
 2320  cd src/externals/
 2321  bash mmlpaikat2omorfi.bash
 2322  cd ..
 2323  cp lexemes+paikat.tsv lexemes.tsv
 2324  make
 2325  fgrep Airâskurrâ externals/places.list
 2326  fgrep Airâškurrâ externals/places.list
 2327  cd externals/
 2328  ls -l
 2329  ls ../
 2330  ls ../ -l
 2331  nano ../lexemes.tsv
 2332  make
 2333  cd .
 2334  cd ../../
 2335  make
 2336  cd src/externals/
 2337  bash mmlpaikat2omorfi.bash
 2338  cd ..
 2339  cd externals/
 2340  cat mmlpaikat2omorfi.bash
 2341  cd ..
 2342  cp lexemes+paikat.tsv lexemes.tsv
 2343  git diff
 2344  cd ..
 2345  make
 2346  git restore lexemes.tsv
 2347  git restore src/lexemes.tsv
 2348  cd src/ex
 2349  cd src/externals/
 2350  ls
 2351  bash mmlpaikat2omorfi.bash
 2352  cd ..
 2353  cp lexemes+paikat.tsv lexemes.tsv
 2354  git diff
 2355  cd ..
 2356  make
 2357  cd src
 2358  less lexemes
 2359  less lexemes.tsv
 2360  vim paradigms.tsv
 2361  vim continuations.tsv
 2362  cd ..
 2363  make
 2364  make check
 2365  cat src/test-suite.log
 2366  cd src/
 2367  git restore lexemes.tsv
 2368  cd externals/
 2369  vim mmlpaikat2omorfi.bash
 2370  git restore ../lexemes.tsv
 2371  bash mmlpaikat2omorfi.bash
 2372  cp ../lexemes+paikat.tsv ../lexemes.tsv
 2373  cd ../../
 2374  make
 2375  make check
 2376  cat src/test-suite.log
 2377  less src/lexemes.tsv
 2378  git restore src/lexemes.tsv
 2379  cd src/externals/
 2380  bash mmlpaikat2omorfi.bash
 2381  cd ../../
 2382  cp src/lexemes+paikat.tsv src/lexemes.tsv
 2383  make
 2384  make check
 2385  cat src/test-suite.log
 2386  less src/lexemes.tsv
 2387  less src/paradigms.tsv
 2388  make
 2389  cd src/externals/
 2390  bash mmlpaikat2omorfi.bash
 2391  git restore ../lexemes.tsv
 2392  bash mmlpaikat2omorfi.bash
 2393  cp ../lexemes+paikat.tsv ../lexemes.tsv
 2394  cd ../../
 2395  make
 2396  make check
 2397  cat src/test-suite.log
 2398  less src/lexemes.tsv
 2399  less src/externals/places.list
 2400  less src/lexemes.tsv
 2401  less src/externals/places.list
 2402  cd src/externals/
 2403  git restore ../lexemes.tsv
 2404  bash mmlpaikat2omorfi.bash
 2405  git restore ../lexemes.tsv
 2406  bash mmlpaikat2omorfi.bash
 2407  cp ../lexemes+paikat.tsv ../lexemes.tsv
 2408  cd ../../
 2409  make
 2410  make check
 2411  cat src/test-suite.log
 2412  less src/lexemes.tsv
 2413  less src/externals/places.list
 2414  cd src/externals/
 2415  less ../lexemes.tsv
 2416  bash mmlpaikat2omorfi.bash
 2417  git restore ../lexemes.tsv
 2418  bash mmlpaikat2omorfi.bash
 2419  cp ../lexemes+paikat.tsv ../lexemes.tsv
 2420  cd ../../
 2421  make
 2422  make check
 2423  cat te
 2424  cat src/test-suite.log
 2425  less src/lexemes.tsv
 2426  less src/paradigms.tsv
 2427  cd src/externals/
 2428  git restore ../lexemes.tsv
 2429  bash mmlpaikat2omorfi.bash
 2430  cp ../lexemes+paikat.tsv ../lexemes.tsv
 2431  cd ../../
 2432  make
 2433  git diff
 2434  cd src/externals/
 2435  git restore ../lexemes.tsv
 2436  bash maanmittauslaitos-gml.bash
 2437  bash mmlpaikat2omorfi.bash
 2438  cd ..
 2439  make
 2440  make check
 2441  history >> src/externals/mmlpaikat2omorfi.bash
