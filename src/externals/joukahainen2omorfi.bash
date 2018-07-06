#!/bin/bash

awk '/<wordlist/,/<\/wordlist/ {print;}' < joukahainen.xml |\
    fgrep -v wordlist |\
    tr -d '\n' |\
    # XML to TSV
    sed -e 's/<word /\n/g' |\
    fgrep -v prefix |\
    sed -e 's/>[[:space:]]*</></g' |\
    sed -e 's/^id=.*<forms>//' \
        -e 's:<form>::' \
        -e 's:</form><form>:||:g' \
        -e 's:</form>::' |\
    sed -e 's:</forms>.*<classes>:\t:' \
        -e 's:<wclass>::' \
        -e 's:</wclass><wclass>:||:g' \
        -e 's:</wclass>::' |\
    sed -e 's:</classes>.*<inflection>:_:' \
        -e 's:<infclass>::' \
        -e 's:</infclass><infclass[^>]*>:||:g' \
        -e 's:</infclass>::' |\
    sed -e 's:</classes></word>::' \
        -e 's:</classes>::' |\
    sed -e 's:<vtype>:__:' \
        -e 's:</vtype>::' \
        -e 's:</style>::' \
        -e 's:</application>::' \
        -e 's:<flag>.*</flag>::' |\
    sed -e 's:</inflection>.*</word>::'\
        -e 's:<style>.*</word>::' \
        -e 's:</word>::' |\
    # JOU to new paras
    sed -e 's/pnoun_\(misc\|lastname\|firstname\|place\)/PROPN/g' \
        -e 's/noun/NOUN/g' \
        -e 's/verb/VERB/g' \
        -e 's/adjective/ADJ/g' \
        -e 's/interjection/INTJ_HAH/' \
        -e 's/abbreviation/NOUN_ACRO/' \
        -e 's/conjunction/SCONJ_ETTÄ/' |\
    sed -e 's/poikkeava$/XXX/' \
        -e 's/risti-av1$/KORTTI/' \
        -e 's/kalsium$/PUNK/' \
        -e 's/kalsium__aä$/PUNK/' \
        -e 's/kalsium||edam__a$/PUNK/' \
        -e 's/kalsium||edam__aä$/PUNK/' \
        -e 's/risti$/RUUVI/' \
        -e 's/risti__a$/RUUVI/' \
        -e 's/kala||asema$/VOIMA/' \
        -e 's/asema$/VOIMA/' \
        -e 's/kulkija||karahka$/KIRJA/' \
        -e 's/kala||karahka$/KIRJA/' \
        -e 's/loppu$/ASU/' \
        -e 's/vastaus$/VAKUUTUS/' \
        -e 's/valo$/TALO/' \
        -e 's/valo__aä$/TALO/' \
        -e 's/kala||kulkija$/VOIMA/' \
        -e 's/karahka||kulkija$/VOIMA/' \
        -e 's/kulkija$/VOIMA/' \
        -e 's/kala$/KIRJA/' \
        -e 's/vieras$/PATSAS/' \
        -e 's/edam$/STADION/' \
        -e 's/nalle$/NALLE/' \
        -e 's/karahka||pasuuna$/KITARA/' \
        -e 's/karahka$/KITARA/' \
        -e 's/peruna||pasuuna$/KITARA/' \
        -e 's/kulkija||pasuuna$/VOIMA/' \
        -e 's/karahka||koira$/VOIMA/' \
        -e 's/koira$/VOIMA/' \
        -e 's/kamee$/BIDEE/' \
        -e 's/suurempi$/LÄHEMPI/' \
        -e 's/pii$/HAI/' \
        -e 's/hame-av2$/OSOITE/' \
        -e 's/paperi||banaali$/KANAALI/' \
        -e 's/risti||banaali$/KANAALI/' \
        -e 's/risti||paperi$/KANAALI/' \
        -e 's/paperi$/KANAALI/' \
        -e 's/sisar-av2$/AJATAR/' \
        -e 's/karahka-av1$/LUSIKKA/' \
        -e 's/arvelu$/RUIPELO/' \
        -e 's/risti-av1||paperi-av1$/KORTTI/' \
        -e 's/paperi-av1$/LOKKI/' \
        -e 's/valo-av1$/UKKO/' \
        -e 's/valo-av1||arvelu-av1$/UKKO/' \
        -e 's/arvelu-av1$/LEPAKKO/' \
        -e 's/rosé__a$/ROSÉ/' \
        -e 's/hame$/ASTE/' \
        -e 's/risti__aä$/RUUVI/' \
        -e 's/nalle__a$/NALLE/' \
        -e 's/kala-av1$/TIPPA/' \
        -e 's/lovi-av1$/KUPPI/' \
        -e 's/lovi-av3$/ARKI/' \
        -e 's/vapaa$/PUU/' \
        -e 's/askel$/ASKAR/' \
        -e 's/autio$/TUOMIO/' \
        -e 's/sisar||ahven$/JOUTSEN/' \
        -e 's/kalleus$/AAKKOSELLISUUS/' \
        -e 's/kiiski$/KIVI/' \
        -e 's/asema||matala$/VOIMA/' \
        -e 's/apaja||kantaja$/PROBLEEMA/' \
        -e 's/matala$/PROBLEEMA/' \
        -e 's/ohut$/OLUT/' \
        -e 's/mies$/MIES/' \
        -e 's/koira-av1$/LUOKKA/' \
        -e 's/vieras-av2$/HIDAS/' \
        -e 's/uistin-av2$/VAADIN/' \
        -e 's/iäkäs-av2$/ASUKAS/' \
        -e 's/uistin$/PUHELIN/' \
        -e 's/onneton$/VIATON/' \
        -e 's/onneton-av2$/VIATON/' \
        -e 's/kuollut$/AIVOKUOLLUT/' \
        -e 's/kala-av3$/AIKA/' \
        -e 's/rosé||bébé$/ROSÉ/' \
        -e 's/nainen__aä$/AAKKOSELLINEN/' \
        -e 's/nainen$/AAKKOSELLINEN/' |\
    sed -e 's/hidastaa$/MUTRISTAA/' \
        -e 's/aaltoilla$/ARVAILLA/'\
        -e 's/katsella-av2$/SULATELLA/'\
        -e 's/kanavoida-av2||haravoida-av2$/KOPIOIDA/'\
        -e 's/voida-av2||kanavoida-av2$/KOPIOIDA/'\
        -e 's/kanavoida-av2$/KOPIOIDA/'\
        -e 's/voida-av2||haravoida-av2$/KOPIOIDA/'\
        -e 's/haravoida-av2$/KOPIOIDA/'\
        -e 's/sulaa-av1$/VIEROITTAA/'\
        -e 's/punoa-av1$/ROHTUA/'\
        -e 's/punoa-av1||antautua$/ROHTUA/'\
        -e 's/punoa-av5$/TAKOA/'\
        -e 's/salata-av2$/JAHDATA/'\
        -e 's/sukeltaa-av2$/KUHERTAA/'\
        -e 's/sukeltaa-av1$/KUHERTAA/'\
        -e 's/aavistaa$/MUTRISTAA/'\
        -e 's/sallia$/KOSIA/'\
        -e 's/kaivaa$/KASVAA/'\
        -e 's/kaivaa-av1$/SATAA/'\
        -e 's/pahentaa-av1$/HUONONTAA/'\
        -e 's/kirjoittaa-av1$/VIEROITTAA/' \
        -e 's/aavistaa-av1$/VIEROITTAA/' \
        -e 's/aiheuttaa-av1$/VIEROITTAA/' \
        -e 's/sallia-av1$/AHNEHTIA/'\
        -e 's/katketa-av6$/POIKETA/'\
        -e 's/aleta-av6$/NIUKETA/'\
        -e 's/nuolaista$/MARISTA/'\
        -e 's/punoa$/PUNOA/'\
        -e 's/salata||palata$/ARVATA/'\
        -e 's/saneerata$/ARVATA/'\
        -e 's/valita$/PALKITA/'\
        -e 's/salata$/ARVATA/'\
        -e 's/saada$/SAADA/'\
        -e 's/kohota$/KARHUTA/'\
        -e 's/haluta$/HALUTA/'\
        -e 's/katsella$/ETUILLA/'
