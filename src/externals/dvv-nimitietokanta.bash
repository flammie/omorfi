#!/bin/bash

# use gnused if mac os x sed causes problems
SED="sed"
FNURL=http://www.avoindata.fi/data/dataset/57282ad6-3ab1-48fb-983a-8aba5ff8d29a/resource/08c89936-a230-42e9-a9fc-288632e234f5/download/
FORNAMES=etunimitilasto-2022-02-07-dvv
SNURL=http://www.avoindata.fi/data/dataset/57282ad6-3ab1-48fb-983a-8aba5ff8d29a/resource/957d19a5-b87a-4c4d-8595-49c22d9d3c58/download/
SURNAMES=sukunimitilasto-2022-02-07-dvv

# download name database from Finnish gov
if ! test -f $FORNAMES.xlsx ; then
    wget ${FNURL}${FORNAMES}.xlsx
fi
if ! test -f $SURNAMES.xlsx ; then
    wget ${SNURL}${SURNAMES}.xlsx
fi

# ssconvert from gnumeric can do xlsx to tsv
if ! test -f $FORNAMES.txt.0 ; then
    ssconvert -S ${FORNAMES}.xlsx -O 'separator="    "' ${FORNAMES}.txt
fi
if ! test -f $SURNAMES.txt.0 ; then
    ssconvert -S ${SURNAMES}.xlsx -O 'separator="    "' ${SURNAMES}.txt
fi

cut -f 1 < ${SURNAMES}.txt.0 |\
    tail -n +2 | sort | uniq > sukunimet
cat ${FORNAMES}.txt.[012345] |\
    grep -E -v '^Etunimi	' | cut -f 1 | sort | uniq > etunimet

FRONT="[äæöøyÄÆÖØY][^åaoóuÅAOÓU]*"
BACK="[åaoóuÅAOÓU][^äæöøyÄÆÖØY]*"
cat sukunimet etunimet |\
    grep -F -v ' ' |\
    $SED -e "s/'/’/g" |\
    $SED \
    -e "s/oo$/\0	PROPN	PROPN_OOKOO	dvvfi_/" \
    -e "s/io$/\0	PROPN	PROPN_TUOMIO	dvvfi_/" \
    -e "s/tto$/\0	PROPN	PROPN_HIRTTO	dvvfi_/" \
    -e "s/ppo$/\0	PROPN	PROPN_HAPPO	dvvfi_/" \
    -e "s/kko$/\0	PROPN	PROPN_UKKO	dvvfi_/" \
    -e "s/lto$/\0	PROPN	PROPN_KIELTO	dvvfi_/" \
    -e "s/nto$/\0	PROPN	PROPN_TUNTO	dvvfi_/" \
    -e "s/uo$/\0	PROPN	PROPN_VUO	dvvfi_/" \
    -e "s/rto$/\0	PROPN	PROPN_SIIRTO	dvvfi_/" \
    -e "s/nko$/\0	PROPN	PROPN_RUNKO	dvvfi_/" \
    -e "s/o$/\0	PROPN	PROPN_TALO	dvvfi_/" \
    -e "s/kku$/\0	PROPN	PROPN_TIKKU	dvvfi_/" \
    -e "s/u$/\0	PROPN	PROPN_ASU	dvvfi_/" \
    -e "s/ey$/\0	PROPN	PROPN_JOCKEY	dvvfi_/" \
    -e "s/[ao]y$/\0	PROPN	PROPN_COWBOY	dvvfi_/" \
    -e "s/y$/\0	PROPN	PROPN_KÄRRY	dvvfi_/" \
    -e "s/${FRONT}nen$/\0	PROPN	PROPN_KYLKIÄINEN	dvvfi_/" \
    -e "s/${BACK}nen$/\0	PROPN	PROPN_AAKKOSTAMINEN	dvvfi_/" \
    -e "s/äme$/\0	PROPN	PROPN_PISTE	dvvfi_/" \
    -e "s/[Aa]hde$/\0	PROPN	PROPN_LUODE	dvvfi_/" \
    -e "s/ee$/\0	PROPN	PROPN_TEE	dvvfi_/" \
    -e "s/ie$/\0	PROPN	PROPN_BRASSERIE	dvvfi_/" \
    -e "s/${BACK}ppe$/\0	PROPN	PROPN_RAPPE	dvvfi_/" \
    -e "s/${BACK}kke$/\0	PROPN	PROPN_EKKE	dvvfi_/" \
    -e "s/${FRONT}tte$/\0	PROPN	PROPN_METTE	dvvfi_/" \
    -e "s/${BACK}tte$/\0	PROPN	PROPN_LOTTE	dvvfi_/" \
    -e "s/tte$/\0	PROPN	PROPN_METTE	dvvfi_/" \
    -e "s/${FRONT}e$/\0	PROPN	PROPN_NISSE	dvvfi_/" \
    -e "s/${BACK}e$/\0	PROPN	PROPN_NALLE	dvvfi_/" \
    -e "s/e$/\0	PROPN	PROPN_NISSE	dvvfi_/" \
    -e "s/${BACK}rpi$/\0	PROPN	PROPN_KORPI	dvvfi_/" \
    -e "s/${BACK}mpi$/\0	PROPN	PROPN_SAMPI	dvvfi_/" \
    -e "s/mäki$/\0	PROPN	PROPN_KÄKI	dvvfi_/" \
    -e "s/niemi$/\0	PROPN	PROPN_LIEMI	dvvfi_/" \
    -e "s/lahti$/\0	PROPN	PROPN_LAHTI	dvvfi_/" \
    -e "s/järvi$/\0	PROPN	PROPN_KIVI	dvvfi_/" \
    -e "s/ai$/\0	PROPN	PROPN_HAI	dvvfi_/" \
    -e "s/oi$/\0	PROPN	PROPN_HAI	dvvfi_/" \
    -e "s/${BACK}ei$/\0	PROPN	PROPN_HAI	dvvfi_/" \
    -e "s/ei$/\0	PROPN	PROPN_PII	dvvfi_/" \
    -e "s/${BACK}kki$/\0	PROPN	PROPN_LOKKI	dvvfi_/" \
    -e "s/${FRONT}kki$/\0	PROPN	PROPN_HÄKKI	dvvfi_/" \
    -e "s/kki$/\0	PROPN	PROPN_HÄKKI	dvvfi_/" \
    -e "s/${BACK}tti$/\0	PROPN	PROPN_KORTTI	dvvfi_/" \
    -e "s/${FRONT}i$/\0	PROPN	PROPN_TYYLI	dvvfi_/" \
    -e "s/${BACK}i$/\0	PROPN	PROPN_RUUVI	dvvfi_/" \
    -e "s/i$/\0	PROPN	PROPN_TYYLI	dvvfi_/" \
    -e "s/tär$/\0	PROPN	PROPN_TYTÄR	dvvfi_/" \
    -e "s/tar$/\0	PROPN	PROPN_AJATAR	dvvfi_/" \
    -e "s/uomas$/\0	PROPN	PROPN_PATSAS	dvvfi_/" \
    -e "s/ngas$/\0	PROPN	PROPN_KANGAS	dvvfi_/" \
    -e "s/nnas$/\0	PROPN	PROPN_VAKUUTUS	dvvfi_/" \
    -e "s/os$/\0	PROPN	PROPN_VAKUUTUS	dvvfi_/" \
    -e "s/ius$/\0	PROPN	PROPN_VAKUUTUS	dvvfi_/" \
    -e "s/${FRONT}[bcçdfghjklmnpqrstvwxz]$/\0	PROPN	PROPN_ZEN	dvvfi_/"  \
    -e "s/${BACK}[bcçdfghjklmnpqrstvwxz]$/\0	PROPN	PROPN_PUNK	dvvfi_/" \
    -e "s/[bcçdfghjklmnpqrstvwxz]$/\0	PROPN	PROPN_ZEN	dvvfi_/"  \
    -e "s/poika$/\0	PROPN	PROPN_POIKA	dvvfi_/" \
    -e "s/kka$/\0	PROPN	PROPN_LUSIKKA	dvvfi_/" \
    -e "s/tta$/\0	PROPN	PROPN_MITTA	dvvfi_/" \
    -e "s/rta$/\0	PROPN	PROPN_KERTA	dvvfi_/" \
    -e "s/lta$/\0	PROPN	PROPN_VALTA	dvvfi_/" \
    -e "s/nta$/\0	PROPN	PROPN_KUTSUNTA	dvvfi_/" \
    -e "s/upa$/\0	PROPN	PROPN_LUPA	dvvfi_/" \
    -e "s/[oeé]a$/\0	PROPN	PROPN_PIIROA	dvvfi_/" \
    -e "s/ia$/\0	PROPN	PROPN_MAKKARA	dvvfi_/" \
    -e "s/aa$/\0	PROPN	PROPN_MAA	dvvfi_/" \
    -e "s/a$/\0	PROPN	PROPN_KIRJA	dvvfi_/" \
    -e "s/ää$/\0	PROPN	PROPN_PÄÄ	dvvfi_/" \
    -e "s/ä$/\0	PROPN	PROPN_HÖPÖTTÄJÄ	dvvfi_/" \
    -e "s/ö$/\0	PROPN	PROPN_MALMÖ	dvvfi_/" \
    -e "s/[áà]$/\0	PROPN	PROPN_CHACHACHA	dvvfi_/" \
    -e "s/[óòå]$/\0	PROPN	PROPN_TALO	dvvfi_/" \
    -e "s/[êéèë]$/\0	PROPN	PROPN_ROSÉ	dvvfi_/" \
    -e "s/\.$/\0	PROPN	PROPN_A.	dvvfi_/" \
    -e "s/[^_]$/\0	PROPN	PROPN_???	dvvfi_/" |\
    $SED -e 's/dvvfi_/dvvfi/' > dvv.fi.tsv.noheaders.unsort
printf "lemma\thomonym\tnew_para\torigin\n" |\
    cat - dvv.fi.tsv.noheaders.unsort > dvv.fi.tsv.unsort
python ../python/tsvsort.py -i dvv.fi.tsv.unsort -o dvv.fi.tsv
python ../python/tsvmerge.py -i ../lexemes.tsv -m dvv.fi.tsv \
    -o lexemes+dvv.fi.tsv.unsort
python ../python/tsvsort.py -i lexemes+dvv.fi.tsv.unsort -o lexemes+dvv.fi.tsv

