#!/bin/bash
# This script takes an English wiktionary xml dump and converts it to omorfi
# it was at c/p from fiwikt2omorfi.bash

SED="sed"

print_usage() {
    echo "Usage: $0 [enwikt-pages-articles.xml]"
    echo
    echo "enwikt-pages-articles.xml must point to unzipped en.wiktionary dump."
    echo "If omitted, stdin is uSED"
}

if test $# -ge 2 ; then
    print_usage
    exit 1
fi
# Define word class
wc='(Noun|Adjective|Pronoun|Numeral|Preposition|Adverb|Interjection|Conjunction|Particle|Verb|Proper [Nn]oun|Letter|Prefix)'

# enwikt is too big
# split
split -n l/20 "$@"
for f in x?? ; do
# Fetchs  only relevant lines from the xml dump (NOTE: This assumes relevant
# lines are between <page> & </page> tags)
cat "$f" | $SED -ne '/<page>/,/<\/page>/p' |\
# Remove all line-initial whitespaces
    $SED -e 's/^[ \t]*//g' |\
# Remove unwanted xml tags
    $SED -ne '/\(<page>\|<title>\)/p' -ne '/<text/,/<\/page>/p' |\
# Remove unwanted xml tag (NOTE: The </revision> tag is found between </text>
# & </page>)
    $SED '/<\/revision>/d' |\
# Remove linebreaks
    tr -d '\n' |\
# Place linebreak infront of each <page>
    $SED -re "s/<page>/\n\0/g" |\
# Retain only those lines which contain relevant content (in this case ==Suomi== which is the heading of Finnish words)
    grep -F "==Finnish==" |\
# Remove certain MediaWiki pages
    $SED -r "/<title>(Class:)|(Template:)|(Wiktionary:)/d" |\
# Remove word forms
    grep -F -v '{{fi-form' | grep -F -v 'possessive form' |\
    grep -F -v 'proper noun form' |\
# Remove some MWEs
    grep '<title>[^ ]*</title>' |\
# Place tags and content on separate lines
    $SED -re "s/(<\/page>)/\n\1/g" \
    -e "s/(<title>)/\n\1/g" \
    -e "s/(<\/title>)/\1\n/g" \
    -e "s/(<text [^>]*>)/\1\n/g" \
    -e "s/(<\/text>)/\n\1/g" |\
# Place relevant content markup characters on seperate lines
    $SED -re "s/(==*[[:alpha:] ]+==)/\n\1/g" \
    -e "s/((\(\{\{)|(\{\{fi))/\n\1/g" |\
# Parse lines and tag word classes in headings (example: ===Substantiivi===)
    $SED -re "s/===$wc===/<wordclass>\1<\/wordclass>/g" |\
# {{fi-decl-nalle|nonsens|||a}}
    $SED -re 's/\{\{fi-(decl|conj)-([a-z]*).*\}\}/<paradigm>\2<\/paradigm>/' |\
# definitions in enwikt are like transatlations usually
#    $SED -re "s/^\{\{fi-noun.*# (.*)$/<definition>\1<\/definition>/g" |\
# Place tags on separate lines
    $SED -re \
    "s/(<(wordclass|paradigm|definition|example)>.*<\/(wordclass|paradigm|definition|example)>)/\n\1\n/g" |\
# recodr languages
     $SED -e 's/^==\([A-Z].*\)==/<lang>\1<\/lang>/' |\
# Remove all  non-tagged lines
    $SED -rn "/^<.*>$/p" |\
# Remove linebreaks
    tr -d '\n' |\
# Split per word again
    $SED -e 's/<page>/\n/g' |\
# Remve non-finnish parts
    $SED -e 's:<text.*<lang>Finnish</lang>::' \
        -e 's:<lang>.*$::' \
        -e 's:</text>.*::' \
        -e 's:<text.*::' |\
# replace space in propn for easy
    $SED -e 's/Proper noun/Proper-noun/g' |\
# Place entries in alphabetical order (due to uniform xml strucuture sort
# command works normally) and write as .xml file
    sort |\
# make csv
    $SED -re \
    's/^.*<title>([^<]*).*<wordclass>([^<]*).*<paradigm>([^<]*).*$/\1,\2,\3/' |\
# remove missing lemmas or classes shown as leftover tags from ^^
    tr '|' ',' |\
    gawk -F , 'NF == 3 {printf("%s\t1\t%s_%s\tenwikt\n", $1, $2, $3);}' |\
    $SED -e 's/Adverb_99/ADV_NOPEASTI/' \
        -e 's/Interjection_[^	]*/INTJ_HAH/' \
        -e 's/\(kko	1	\)Proper-noun_valo	/\1PROPN_UKKO	/' \
        -e 's/\(kko	1	\)Noun_valo	/\1NOUN_UKKO	/' \
        -e 's/\(kku	1	\)Noun_valo	/\1NOUN_TIKKU	/' \
        -e 's/\(kku	1	\)Proper-noun_valo	/\1PROPN_TIKKU	/' \
        -e 's/\(ppu	1	\)Noun_valo	/\1NOUN_LIPPU	/' \
        -e 's/\(ppo	1	\)Proper-noun_valo	/\1PROPN_HAPPO	/' \
        -e 's/\(ppo	1	\)Noun_valo	/\1NOUN_HAPPO	/' \
        -e 's/\(tto	1	\)Noun_valo	/\1NOUN_HIRTTO	/' \
        -e 's/\(tto	1	\)Proper-noun_valo	/\1PROPN_HIRTTO	/' \
        -e 's/\(ttu	1	\)Adjective_valo	/\1ADJ_VIMMATTU	/' \
        -e 's/\(tty	1	\)Adjective_valo	/\1ADJ_YLENNETTY	/' \
        -e 's/\(ttu	1	\)Proper-noun_valo	/\1PROPN_TORTTU	/' \
        -e 's/\(ttu	1	\)Noun_valo	/\1NOUN_TORTTU	/' \
        -e 's/\(tty	1	\)Proper-noun_valo	/\1PROPN_PYTTY	/' \
        -e 's/\(ttö	1	\)Proper-noun_valo	/\1PROPN_PÖNTTÖ	/' \
        -e 's/\(ku	1	\)Proper-noun_valo	/\1PROPN_ALKU	/' \
        -e 's/\([st]ko	1	\)Noun_valo	/\1NOUN_TALO	/' \
        -e 's/\(nko	1	\)Noun_valo	/\1NOUN_RUNKO	/' \
        -e 's/\(oko	1	\)Noun_valo	/\1NOUN_RUOKO	/' \
        -e 's/\(oko	1	\)Proper-noun_valo	/\1PROPN_RUOKO	/' \
        -e 's/\(to	1	\)Proper-noun_valo	/\1PROPN_VETO	/' \
        -e 's/\(lto	1	\)Noun_valo	/\1NOUN_KIELTO	/' \
        -e 's/\(rto	1	\)Noun_valo	/\1NOUN_SIIRTO	/' \
        -e 's/\(nto	1	\)Noun_valo	/\1NOUN_TUNTO	/' \
        -e 's/\([^s]to	1	\)Noun_valo	/\1NOUN_VETO	/' \
        -e 's/\(ttu	1	\)Noun_valo	/\1NOUN_TORTTU	/' \
        -e 's/\(ntu	1	\)Noun_valo	/\1NOUN_LINTU	/' \
        -e 's/\(tu	1	\)Noun_valo	/\1NOUN_KUITU	/' \
        -e 's/\(tu	1	\)Proper-noun_valo	/\1PROPN_KUITU	/' \
        -e 's/\([^s]to	1	\)Proper-noun_valo	/\1PROPN_VETO	/' \
        -e 's/\(nko	1	\)Proper-noun_valo	/\1PROPN_RUNKO	/' \
        -e 's/\(mpo	1	\)Noun_valo	/\1NOUN_SAMPO	/' \
        -e 's/\(mpu	1	\)Proper-noun_valo	/\1PROPN_RUMPU	/' \
        -e 's/\(lto	1	\)Noun_valo	/\1NOUN_KIELTO	/' \
        -e 's/\(lto	1	\)Proper-noun_valo	/\1PROPN_KIELTO	/' \
        -e 's/\(nto	1	\)Proper-noun_valo	/\1PROPN_TUNTO	/' \
        -e 's/\(rto	1	\)Proper-noun_valo	/\1PROPN_SIIRTO	/' \
        -e 's/\(nky	1	\)Noun_valo	/\1NOUN_SÄNKY	/' \
        -e 's/\(ky	1	\)Noun_valo	/\1NOUN_NÄKY	/' \
        -e 's/\(ko	1	\)Noun_valo	/\1NOUN_TEKO	/' \
        -e 's/\(uku	1	\)Noun_valo	/\1NOUN_LUKU	/' \
        -e 's/\(o	1	\)Noun_valo	/\1NOUN_TALO	/' \
        -e 's/\(ot	1	\)Noun_valo	/\1NOUN_AIVOT	/' \
        -e 's/\(o	1	\)Adjective_valo	/\1ADJ_TUMMAHKO	/' \
        -e 's/\(o	1	\)Proper-noun_valo	/\1PROPN_TALO	/' \
        -e 's/\(pu	1	\)Noun_valo	/\1NOUN_APU	/' \
        -e 's/\(ku	1	\)Noun_valo	/\1NOUN_ALKU	/' \
        -e 's/\(u	1	\)Noun_valo	/\1NOUN_ASU	/' \
        -e 's/\(u	1	\)Verb_valo	/\1ADJ_VALKAISTU	/' \
        -e 's/\(u	1	\)Adjective_valo	/\1ADJ_VALKAISTU	/' \
        -e 's/\(ut	1	\)Noun_valo	/\1NOUN_HOUSUT	/' \
        -e 's/\(ut	1	\)Proper-noun_valo	/\1PROPN_HOUSUT	/' \
        -e 's/\(u	1	\)Proper-noun_valo	/\1PROPN_ASU	/' \
        -e 's/\(y	1	\)Proper-noun_valo	/\1PROPN_KÄRRY	/' \
        -e 's/\(y	1	\)Noun_valo	/\1NOUN_KÄRRY	/' \
        -e 's/\(yt	1	\)Noun_valo	/\1NOUN_PÖKSYT	/' \
        -e 's/\(ntö	1	\)Noun_valo	/\1NOUN_KÄÄNTÖ	/' \
        -e 's/\(mpö	1	\)Noun_valo	/\1NOUN_LÄMPÖ	/' \
        -e 's/\(kkö	1	\)Noun_valo	/\1NOUN_YÖKKÖ	/' \
        -e 's/\(ttö	1	\)Noun_valo	/\1NOUN_PÖNTTÖ	/' \
        -e 's/\(ö	1	\)Noun_valo	/\1NOUN_MÖMMÖ	/' \
        -e 's/\(öt	1	\)Noun_valo	/\1NOUN_TYTÖT	/' \
        -e 's/\(ö	1	\)Adjective_valo	/\1ADJ_HÖLÖ	/' \
        -e 's/\(y	1	\)Adjective_valo	/\1ADJ_HÄPÄISTY	/' \
        -e 's/\(y	1	\)Verb_valo	/\1ADJ_HÄPÄISTY	/' \
        -e 's/\(ö	1	\)Proper-noun_valo	/\1PROPN_MÖMMÖ	/' \
        -e 's/\(o	1	\)Noun_palvelu	/\1NOUN_RUIPELO	/' \
        -e 's/\(ot	1	\)Noun_palvelu	/\1NOUN_PIPPALOT	/' \
        -e 's/\(u	1	\)Noun_palvelu	/\1NOUN_SEIKKAILU	/' \
        -e 's/\(ut	1	\)Noun_palvelu	/\1NOUN_HOUSUT	/' \
        -e 's/\(y	1	\)Noun_palvelu	/\1NOUN_VEHKEILY	/' \
        -e 's/\(ö	1	\)Noun_palvelu	/\1NOUN_JÄÄTELÖ	/' \
        -e 's/\(o	1	\)Adjective_palvelu	/\1ADJ_TUMMAHKO	/' \
        -e 's/\(ö	1	\)Adjective_palvelu	/\1ADJ_LÖPERÖ	/' \
        -e 's/\(y	1	\)Proper-noun_2	/\1PROPN_KÄRRY	/' \
        -e 's/\(ttu	1	\)Proper-noun_palvelu	/\1PROPN_TORTTU	/' \
        -e 's/\(o	1	\)Proper-noun_palvelu	/\1PROPN_RUIPELO	/' \
        -e 's/\(y	1	\)Proper-noun_palvelu	/\1PROPN_KÄRRY	/' \
        -e 's/\(ö	1	\)Proper-noun_palvelu	/\1PROPN_JÄÄTELÖ	/' \
        -e 's/\(o	1	\)Adjective_valtio	/\1ADJ_AUTIO	/' \
        -e 's/\(o	1	\)Noun_valtio	/\1NOUN_TUOMIO	/' \
        -e 's/\(ot	1	\)Noun_valtio	/\1NOUN_RAUNIOT	/' \
        -e 's/\(e	1	\)Noun_valtio	/\1NOUN_ZOMBIE	/' \
        -e 's/\(ö	1	\)Noun_valtio	/\1NOUN_HÄIRIÖ	/' \
        -e 's/\(o	1	\)Proper-noun_valtio	/\1PROPN_TUOMIO	/' \
        -e 's/\(ot	1	\)Proper-noun_valtio	/\1PROPN_RAUNIOT	/' \
        -e 's/\(e	1	\)Proper-noun_valtio	/\1PROPN_ZOMBIE	/' \
        -e 's/\(ö	1	\)Proper-noun_valtio	/\1PROPN_HÄIRIÖ	/' \
        -e 's/\(ä	1	\)Proper-noun_valtio	/\1PROPN_HÄKKYRÄ	/' \
        -e 's/\(o	1	\)Noun_laatikko	/\1NOUN_LEPAKKO	/' \
        -e 's/\(ö	1	\)Noun_laatikko	/\1NOUN_YKSIKKÖ	/' \
        -e 's/\(o	1	\)Proper-noun_laatikko	/\1PROPN_LEPAKKO	/' \
        -e 's/\(ö	1	\)Proper-noun_laatikko	/\1PROPN_YKSIKKÖ	/' \
        -e 's/\(o	1	\)Noun_4C	/\1NOUN_HIRTTO	/' \
        -e 's/\([aouAOU].*nki	1	\)Noun_risti	/\1NOUN_VANKI	/' \
        -e 's/\([aouAOU].*nti	1	\)Noun_risti	/\1NOUN_SOINTI	/' \
        -e 's/\([äöyÄÖY].*nti	1	\)Noun_risti	/\1NOUN_VIENTI	/' \
        -e 's/\([aouAOU].*ti	1	\)Noun_risti	/\1NOUN_TAUTI	/' \
        -e 's/\([aouAOU].*kki	1	\)Noun_risti	/\1NOUN_LOKKI	/' \
        -e 's/\([äöyÄÖY].*kki	1	\)Noun_risti	/\1NOUN_HÄKKI	/' \
        -e 's/\([aouAOU].*i	1	\)Proper-noun_risti	/\1PROPN_RUUVI	/' \
        -e 's/\([aouAOU].*i	1	\)Noun_risti	/\1NOUN_RUUVI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Proper-noun_risti	/\1PROPN_TYYLI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Noun_risti	/\1NOUN_TYYLI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Pronoun_risti	/\1NOUN_TYYLI	/' \
        -e 's/\(i	1	\)Proper-noun_risti	/\1PROPN_TYYLI	/' \
        -e 's/\(i	1	\)Noun_risti	/\1NOUN_TYYLI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Adjective_risti	/\1ADJ_STYDI	/' \
        -e 's/\([äöyÄÖY].*[mnhcflrktbvpsšžxzgwdMNHFLRKTPBSXGD]	1	\)Noun_risti/\1NOUN_ZEN	/' \
        -e 's/\([mnhcflrktbvpsšžxzgwdMNHFLRKTPBSXGD]	1	\)Noun_risti	/\1NOUN_PUNK	/' \
        -e 's/\([mnhcflrktbpvsšžgdxwz]	1	\)Proper-noun_risti	/\1PROPN_PUNK	/' \
        -e 's/\([mnhcflrktbvpsšžxzgwdMNHFLRKTPBSXGD]	1	\)Adjective_risti/\1ADJ_CHIC	/' \
        -e 's/\(i	1	\)Numeral_risti	/\1NUM_MILJARDI	/' \
        -e 's/\(i	1	\)Adjective_risti	/\1ADJ_ABNORMI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Proper-noun_5A	/\1PROPN_HÄKKI	/' \
        -e 's/\(i	1	\)Proper-noun_5A	/\1PROPN_LOKKI	/' \
        -e 's/\(i	1	\)Proper-noun_5B	/\1PROPN_KUPPI	/' \
        -e 's/\(i	1	\)Noun_5B	/\1NOUN_KUPPI	/' \
        -e 's/\(it	1	\)Noun_5B	/\1NOUN_KLUMPIT	/' \
        -e 's/\(i	1	\)Proper-noun_5C	/\1PROPN_KORTTI	/' \
        -e 's/\(i	1	\)Noun_5C	/\1NOUN_KORTTI	/' \
        -e 's/\(i	1	\)Noun_5G	/\1NOUN_VANKI	/' \
        -e 's/\(i	1	\)Proper-noun_5G	/\1PROPN_VANKI	/' \
        -e 's/\(i	1	\)Noun_5F	/\1NOUN_LEHTI	/' \
        -e 's/\(i	1	\)Proper-noun_5F	/\1PROPN_TAUTI	/' \
        -e 's/\(i	1	\)Proper-noun_5J	/\1PROPN_SOINTI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Proper-noun_6	/\1PROPN_KEHVELI	/' \
        -e 's/\(.*i	1	\)Proper-noun_paperi	/\1PROPN_KANAALI	/' \
        -e 's/\([aouAOU].*i	1	\)Noun_paperi	/\1NOUN_KANAALI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Noun_paperi	/\1NOUN_KEHVELI	/' \
        -e 's/\(i	1	\)Noun_paperi	/\1NOUN_KEHVELI	/' \
        -e 's/\(.*i	1	\)Adjective_paperi	/\1ADJ_ABNORMAALI	/' \
        -e 's/\([mnlhfkrtpdbgsv]	1	\)Noun_paperi	/\1NOUN_STADION	/' \
        -e 's/\([mnlhfkrtpdbgsv]	1	\)Proper-noun_paperi	/\1PROPN_STADION	/' \
        -e 's/\(i	1	\)Proper-noun_6C	/\1PROPN_SKEITTI	/' \
        -e 's/\(i	1	\)Proper-noun_7	/\1PROPN_ONNI	/' \
        -e 's/\(i	1	\)Noun_7	/\1NOUN_ONNI	/' \
        -e 's/\(e	1	\)Numeraali_7	/\1NUM_KOLME	/' \
        -e 's/\(i	1	\)Proper-noun_7D	/\1PROPN_NOKI	/' \
        -e 's/\(i	1	\)Proper-noun_7E	/\1PROPN_LAHTI	/' \
        -e 's/\(i	1	\)Proper-noun_7F	/\1PROPN_KORPI	/' \
        -e 's/\([äöy].*i	1	\)Proper-noun_7D	/\1PROPN_KÄKI	/' \
        -e 's/\(i	1	\)Proper-noun_7H	/\1PROPN_SAMPI	/' \
        -e 's/\(i	1	\)Noun_7J	/\1NOUN_SOINTI	/' \
        -e 's/\(i	1	\)Proper-noun_7L	/\1PROPN_ARKI	/' \
        -e 's/\(e	1	\)Proper-noun_8	/\1PROPN_NALLE	/' \
        -e 's/\(e	1	\)Noun_valo	/\1NOUN_NALLE	/' \
        -e 's/\(e	1	\)Proper-noun_valo	/\1PROPN_NALLE	/' \
        -e 's/\(e	1	\)Noun_nalle	/\1NOUN_NALLE	/' \
        -e 's/\(e	1	\)Adjective_nalle	/\1ADJ_TERVE	/' \
        -e 's/\(ke	1	\)Proper-noun_nalle	/\1PROPN_EKKE	/' \
        -e 's/\(e	1	\)Proper-noun_nalle	/\1PROPN_NALLE	/' \
        -e 's/\(ntä	1	\)Noun_kala	/\1NOUN_KYSYNTÄ	/' \
        -e 's/\(ppa	1	\)Noun_kala	/\1NOUN_TIPPA	/' \
        -e 's/\(ppä	1	\)Noun_kala	/\1NOUN_SEPPÄ	/' \
        -e 's/\(kka	1	\)Noun_kala	/\1NOUN_LUOKKA	/' \
        -e 's/\(tta	1	\)Noun_kala	/\1NOUN_MITTA	/' \
        -e 's/\(nta	1	\)Noun_kala	/\1NOUN_KUTSUNTA	/' \
        -e 's/\(ntä	1	\)Noun_kala	/\1NOUN_HÄNTÄ	/' \
        -e 's/\(lta	1	\)Noun_kala	/\1NOUN_VALTA	/' \
        -e 's/\(tä	1	\)Noun_kala	/\1NOUN_PÖYTÄ	/' \
        -e 's/\(ta	1	\)Noun_kala	/\1NOUN_PATA	/' \
        -e 's/\(ka	1	\)Noun_kala	/\1NOUN_VIKA	/' \
        -e 's/\(a	1	\)Noun_kala	/\1NOUN_KIRJA	/' \
        -e 's/\(ä	1	\)Noun_kala	/\1NOUN_HÖPÖTTÄJÄ	/' \
        -e 's/\(at	1	\)Noun_kala	/\1NOUN_VARAT	/' \
        -e 's/\(a	1	\)Numeral_kala	/\1NUM_MILJOONA	/' \
        -e 's/\(n	1	\)Numeral_kala	/\1NUM_KYMMENEN	/' \
        -e 's/\(a	1	\)Adjective_kala	/\1ADJ_RUMA	/' \
        -e 's/\(llat	1	\)Proper-noun_kala	/\1PROPN_VALLAT	/' \
        -e 's/\(at	1	\)Proper-noun_kala	/\1PROPN_VARAT	/' \
        -e 's/\(lta	1	\)Proper-noun_kala	/\1PROPN_VALTA	/' \
        -e 's/\(nta	1	\)Proper-noun_kala	/\1PROPN_KUTSUNTA	/' \
        -e 's/\(rta	1	\)Proper-noun_kala	/\1PROPN_KERTA	/' \
        -e 's/\(rka	1	\)Adjective_kala	/\1ADJ_ARKA	/' \
        -e 's/\(ka	1	\)Proper-noun_kala	/\1PROPN_POLITIIKKA	/' \
        -e 's/\(pa	1	\)Noun_kala	/\1NOUN_TIPPA	/' \
        -e 's/\(ta	1	\)Proper-noun_kala	/\1PROPN_MITTA	/' \
        -e 's/\(ka	1	\)Proper-noun_kala	/\1PROPN_VAAKA	/' \
        -e 's/\(ta	1	\)Noun_kala	/\1NOUN_PATA	/' \
        -e 's/\(ta	1	\)Proper-noun_kala	/\1PROPN_PATA	/' \
        -e 's/\(a	1	\)Proper-noun_kala	/\1PROPN_KIRJA	/' \
        -e 's/\(a	1	\)Adjective_koira	/\1ADJ_RUMA	/' \
        -e 's/\(ä	1	\)Adjective_koira	/\1ADJ_TYHMÄ	/' \
        -e 's/\(ruoka	1	\)Verb_koira	/\1NOUN_RUOKA	/' \
        -e 's/\(tta	1	\)Noun_koira	/\1NOUN_ROTTA	/' \
        -e 's/\(kka	1	\)Noun_koira	/\1NOUN_LUOKKA	/' \
        -e 's/\(nta	1	\)Noun_koira	/\1NOUN_KUNTA	/' \
        -e 's/\(pa	1	\)Noun_koira	/\1NOUN_LUPA	/' \
        -e 's/\(ta	1	\)Noun_koira	/\1NOUN_SOTA	/' \
        -e 's/\(a	1	\)Verb_koira	/\1NOUN_VOIMA	/' \
        -e 's/\(a	1	\)Noun_koira	/\1NOUN_VOIMA	/' \
        -e 's/\(at	1	\)Noun_koira	/\1NOUN_JUHLAT	/' \
        -e 's/\(tä	1	\)Noun_koira	/\1NOUN_PÖYTÄ	/' \
        -e 's/\(ä	1	\)Noun_koira	/\1NOUN_HÖPÖTTÄJÄ	/' \
        -e 's/\(ät	1	\)Noun_koira	/\1NOUN_KÄRÄJÄT	/' \
        -e 's/\(a	1	\)Numeral_koira	/\1NUM_MILJOONA	/' \
        -e 's/\(ä	1	\)Numeral_koira	/\1NOUN_HÖPÖTTÄJÄ	/' \
        -e 's/\(a	1	\)Noun_omena	/\1NOUN_PROBLEEMA	/' \
        -e 's/\(at	1	\)Noun_omena	/\1NOUN_KASTILJAT	/' \
        -e 's/\(a	1	\)Adjective_omena	/\1ADJ_MATALA	/' \
        -e 's/\(ä	1	\)Adjective_omena	/\1ADJ_SÄKKÄRÄ	/' \
        -e 's/\(a	1	\)Proper-noun_koira	/\1PROPN_VOIMA	/' \
        -e 's/\(at	1	\)Proper-noun_koira	/\1PROPN_JUHLAT	/' \
        -e 's/\(a	1	\)Proper-noun_omena	/\1PROPN_PROBLEEMA	/' \
        -e 's/\(ä	1	\)Proper-noun_koira	/\1PROPN_HÖPÖTTÄJÄ	/' \
        -e 's/\(ä	1	\)Verb_koira	/\1NOUN_HÖPÖTTÄJÄ	/' \
        -e 's/\(ä	1	\)Noun_omena	/\1NOUN_HÖPÖTTÄJÄ	/' \
        -e 's/\(a	1	\)Numeraali_10	/\1NUM_MILJOONA	/' \
        -e 's/\(än	1	\)Numeraali_10	/\1NUM_YHDEKSÄN	/' \
        -e 's/\(ä	1	\)Proper-noun_koira	/\1PROPN_HÖPÖTTÄJÄ	/' \
        -e 's/\(ä	1	\)Proper-noun_omena	/\1PROPN_HÖPÖTTÄJÄ	/' \
        -e 's/\(a	1	\)Proper-noun_10A	/\1PROPN_KUKKA	/' \
        -e 's/\(ä	1	\)Proper-noun_10A	/\1PROPN_HÖLKKÄ	/' \
        -e 's/\(ä	1	\)Proper-noun_10B	/\1PROPN_SEPPÄ	/' \
        -e 's/\(a	1	\)Proper-noun_10B	/\1PROPN_KUOPPA	/' \
        -e 's/\(ä	1	\)Proper-noun_10C	/\1PROPN_KENTTÄ	/' \
        -e 's/\(a	1	\)Noun_10L	/\1NOUN_OLKA	/' \
        -e 's/\([Pp]oika	1	\)Noun_10D	/\1NOUN_POIKA	/' \
        -e 's/\([Pp]oika	1	\)Proper-noun_10D	/\1PROPN_POIKA	/' \
        -e 's/\(ä	1	\)Noun_10D	/\1NOUN_NÄLKÄ	/' \
        -e 's/\(ä	1	\)Proper-noun_10D	/\1PROPN_NÄLKÄ	/' \
        -e 's/\(a	1	\)Proper-noun_10E	/\1PROPN_LUPA	/' \
        -e 's/\(a	1	\)Noun_10F	/\1NOUN_SOTA	/' \
        -e 's/\(ä	1	\)Noun_10F	/\1NOUN_PÖYTÄ	/' \
        -e 's/\(a	1	\)Proper-noun_10F	/\1PROPN_SOTA	/' \
        -e 's/\(a	1	\)Proper-noun_10G	/\1PROPN_HONKA	/' \
        -e 's/\(ä	1	\)Proper-noun_10G	/\1PROPN_KENKÄ	/' \
        -e 's/\(a	1	\)Noun_10H	/\1NOUN_RAMPA	/' \
        -e 's/\(a	1	\)Proper-noun_10J	/\1PROPN_KUNTA	/' \
        -e 's/\(a	1	\)Adjective_10J	/\1ADJ_VIHANTA	/' \
        -e 's/\(ä	1	\)Noun_10L	/\1NOUN_NÄLKÄ	/' \
        -e 's/\(ä	1	\)Proper-noun_11	/\1PROPN_HÄKKYRÄ	/' \
        -e 's/\(a	1	\)Adjective_katiska	/\1ADJ_RUMA	/' \
        -e 's/\(a	1	\)Noun_katiska	/\1NOUN_MAKKARA	/' \
        -e 's/\(at	1	\)Noun_katiska	/\1NOUN_VARAT	/' \
        -e 's/\(ä	1	\)Noun_katiska	/\1NOUN_SIIVILÄ	/' \
        -e 's/\(a	1	\)Proper-noun_katiska	/\1PROPN_KITARA	/' \
        -e 's/\(a	1	\)Noun_kulkija	/\1NOUN_KITARA	/' \
        -e 's/\(at	1	\)Noun_kulkija	/\1NOUN_MARKKINAT	/' \
        -e 's/\(a	1	\)Adjective_kulkija	/\1ADJ_HARMAJA	/' \
        -e 's/\(ä	1	\)Noun_kulkija	/\1NOUN_HÄKKYRÄ	/' \
        -e 's/\(a	1	\)Proper-noun_kulkija	/\1PROPN_KITARA	/' \
        -e 's/\(ä	1	\)Proper-noun_kulkija	/\1PROPN_HÄKKYRÄ	/' \
        -e 's/\(a	1	\)Noun_13	/\1NOUN_KIRJA	/' \
        -e 's/\(o	1	\)Proper-noun_laatikko	/\1PROPN_LEPAKKO	/' \
        -e 's/\(ö	1	\)Proper-noun_laatikko	/\1PROPN_YKSIKKÖ	/' \
        -e 's/\(a	1	\)Proper-noun_13	/\1PROPN_KIRJA	/' \
        -e 's/\(ka	1	\)Proper-noun_solakka	/\1PROPN_LUSIKKA	/' \
        -e 's/\(ta	1	\)Noun_solakka	/\1NOUN_MITTA	/' \
        -e 's/\(ka	1	\)Noun_solakka	/\1NOUN_LUSIKKA	/' \
        -e 's/\(kat	1	\)Noun_solakka	/\1NOUN_SILAKAT	/' \
        -e 's/\(pa	1	\)Noun_solakka	/\1NOUN_ULAPPA	/' \
        -e 's/\(kä	1	\)Noun_solakka	/\1NOUN_KÄMMEKKÄ	/' \
        -e 's/\(kä	1	\)Adjective_solakka	/\1ADJ_RÄVÄKKÄ	/' \
        -e 's/\(ka	1	\)Adjective_solakka	/\1ADJ_HAILAKKA	/' \
        -e 's/\(ka	1	\)Proper-noun_solakka	/\1PROPN_LUSIKKA	/' \
        -e 's/\(kä	1	\)Proper-noun_solakka	/\1PROPN_HÖLKKÄ	/' \
        -e 's/\(ta	1	\)Proper-noun_solakka	/\1PROPN_MITTA	/' \
        -e 's/\(a	1	\)Noun_14G	/\1NOUN_HONKA	/' \
        -e 's/\(a	1	\)Proper-noun_korkea	/\1PROPN_MAKKARA	/' \
        -e 's/\(a	1	\)Noun_korkea	/\1NOUN_SOKEA	/' \
        -e 's/\(at	1	\)Noun_korkea	/\1NOUN_HOPEAT	/' \
        -e 's/\(ä	1	\)Noun_korkea	/\1NOUN_LIPEÄ	/' \
        -e 's/\(ä	1	\)Proper-noun_korkea	/\1PROPN_LIPEÄ	/' \
        -e 's/\(a	1	\)Adjective_korkea	/\1ADJ_KORKEA	/' \
        -e 's/\(ä	1	\)Adjective_korkea	/\1ADJ_JÄREÄ	/' \
        -e 's/\(a	1	\)Pronomini_15	/\1PRON_USEA	/' \
        -e 's/\(i	1	\)Noun_vanhempi	/\1NOUN_VANHEMPI	/' \
        -e 's/\(i	1	\)Pronoun_vanhempi	/\1PRON_MOLEMPI	/' \
        -e 's/\(mat	1	\)Noun_vanhempi	/\1NOUN_VANHEMMAT	/' \
        -e 's/\(mat	1	\)Pronoun_vanhempi	/\1PRON_MOLEMMAT	/' \
        -e 's/\(i	1	\)Adjective_vanhempi	/\1ADJ_LÄHEMPI	/' \
        -e 's/\(i	1	\)Pronomini_16	/\1PRON_KUMPI	/' \
        -e 's/\(ikin	1	\)Pronomini_16	/\1PRON_KUMPIKIN	/' \
        -e 's/\([aA]	1	\)Noun_maa	/\1NOUN_MAA	/' \
        -e 's/\([aA]	1	\)Adjective_maa	/\1NOUN_PEEAA	/' \
        -e 's/\(i	1	\)Noun_maa	/\1NOUN_HAI	/' \
        -e 's/\(e	1	\)Noun_maa	/\1NOUN_TEE	/' \
        -e 's/\(o	1	\)Noun_maa	/\1NOUN_OOKOO	/' \
        -e 's/\(u	1	\)Noun_maa	/\1NOUN_PUU	/' \
        -e 's/\(ut	1	\)Noun_maa	/\1NOUN_PUUT	/' \
        -e 's/\(y	1	\)Noun_maa	/\1NOUN_PYY	/' \
        -e 's/\(ä	1	\)Noun_maa	/\1NOUN_PÄÄ	/' \
        -e 's/\(ät	1	\)Noun_maa	/\1NOUN_HÄÄT	/' \
        -e 's/\(ö	1	\)Noun_maa	/\1NOUN_KÖÖ	/' \
        -e 's/\(a	1	\)Proper-noun_maa	/\1PROPN_MAA	/' \
        -e 's/\(at	1	\)Proper-noun_maa	/\1PROPN_MAAT	/' \
        -e 's/\([uU]	1	\)Proper-noun_maa	/\1PROPN_PUU	/' \
        -e 's/\(u	1	\)Pronomini_maa	/\1PRON_MUU	/' \
        -e 's/\(i	1	\)Proper-noun_maa	/\1PROPN_HAI	/' \
        -e 's/\(o	1	\)Proper-noun_maa	/\1PROPN_OOKOO	/' \
        -e 's/\(y	1	\)Proper-noun_maa	/\1PROPN_PYY	/' \
        -e 's/\(ä	1	\)Proper-noun_maa	/\1PROPN_PÄÄ	/' \
        -e 's/\(ie	1	\)Noun_suo	/\1NOUN_TIE	/' \
        -e 's/\(uo	1	\)Noun_suo	/\1NOUN_VUO	/' \
        -e 's/\(yö	1	\)Noun_suo	/\1NOUN_TYÖ	/' \
        -e 's/\(yöt	1	\)Noun_suo	/\1NOUN_TYÖT	/' \
        -e 's/\(ie	1	\)Proper-noun_suo	/\1PROPN_TIE	/' \
        -e 's/\(uo	1	\)Proper-noun_suo	/\1PROPN_VUO	/' \
        -e 's/\(uu	1	\)Noun_vapaa	/\1NOUN_LEIKKUU	/' \
        -e 's/\(oo	1	\)Noun_vapaa	/\1NOUN_TIENOO	/' \
        -e 's/\(oot	1	\)Noun_vapaa	/\1NOUN_TALKOOT	/' \
        -e 's/\(yyt	1	\)Noun_vapaa	/\1NOUN_RYNTTYYT	/' \
        -e 's/\(e	1	\)Noun_vapaa	/\1NOUN_PATEE	/' \
        -e 's/\(a	1	\)Noun_vapaa	/\1NOUN_VAINAA	/' \
        -e 's/\(a	1	\)Adjective_vapaa	/\1ADJ_VAPAA	/' \
        -e 's/\(e	1	\)Adjective_filee	/\1NOUN_MAKEE	/' \
        -e 's/\(e	1	\)Noun_filee	/\1NOUN_PATEE	/' \
        -e 's/\(eet	1	\)Noun_filee	/\1NOUN_RÄMEET	/' \
        -e 's/\(a	1	\)Noun_filee	/\1NOUN_VAINAA	/' \
        -e 's/\(oi	1	\)Proper-noun_filee	/\1PROPN_HAI	/' \
        -e 's/\(a	1	\)Proper-noun_filee	/\1PROPN_NUGAA	/' \
        -e 's/\(eet	1	\)Proper-noun_filee	/\1PROPN_RÄMEET	/' \
        -e 's/\(kee	1	\)Proper-noun_filee	/\1PROPN_TOKEE	/' \
        -e 's/\(e	1	\)Proper-noun_filee	/\1PROPN_BIDEE	/' \
        -e 's/\(o	1	\)Noun_filee	/\1NOUN_TIENOO	/' \
        -e 's/\(u	1	\)Noun_filee	/\1NOUN_RAGUU	/' \
        -e 's/\(y	1	\)Noun_filee	/\1NOUN_FONDYY	/' \
        -e 's/\(ö	1	\)Noun_filee	/\1NOUN_MILJÖÖ	/' \
        -e 's/\(ö	1	\)Proper-noun_filee	/\1PROPN_MILJÖÖ	/' \
        -e 's/\(t	1	\)Noun_parfait	/\1NOUN_PARFAIT	/' \
        -e 's/\([xw]	1	\)Noun_parfait	/\1NOUN_SHOW	/' \
        -e 's/\(ee	1	\)Proper-noun_vapaa	/\1PROPN_TOKEE	/' \
        -e 's/\(a	1	\)Proper-noun_vapaa	/\1PROPN_VAINAA	/' \
        -e 's/\(o	1	\)Proper-noun_vapaa	/\1PROPN_TIENOO	/' \
        -e 's/\(u	1	\)Proper-noun_vapaa	/\1PROPN_LEIKKUU	/' \
        -e 's/\(ä	1	\)Proper-noun_vapaa	/\1PROPN_HYVINKÄÄ	/' \
        -e 's/\(	1	\)Noun_rosé	/\1NOUN_ROSÉ	/' \
        -e 's/\(	1	\)Noun_ros	/\1NOUN_ROSÉ	/' \
        -e 's/\(ie	1	\)Pronomini_21	/\1PRON_MIE	/' \
        -e 's/\(	1	\)Proper-noun_rosé	/\1PROPN_ROSÉ	/' \
        -e 's/\(w	1	\)Proper-noun_show	/\1PROPN_SHOW	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Adjective_ovi	/\1ADJ_LÄHEMPI	/' \
        -e 's/\(i	1	\)Adjective_ovi	/\1ADJ_AIEMPI	/' \
        -e 's/\([aouAOU].*nki	1	\)Noun_ovi	/\1NOUN_ONKI	/' \
        -e 's/\([aouAOU].*ppi	1	\)Noun_ovi	/\1NOUN_HAPPI	/' \
        -e 's/\([aouAOU].*lehti	1	\)Noun_ovi	/\1NOUN_LEHTI	/' \
        -e 's/\([äöyÄÖY].*[lr]ki	1	\)Noun_ovi	/\1NOUN_JÄRKI	/' \
        -e 's/\([äöyÄÖY].*ki	1	\)Noun_ovi	/\1NOUN_KÄKI	/' \
        -e 's/\([aouAOU].*ki	1	\)Noun_ovi	/\1NOUN_NOKI	/' \
        -e 's/\([aouAOU].*pi	1	\)Noun_ovi	/\1NOUN_KILPI	/' \
        -e 's/\([aouAOU].*i	1	\)Noun_ovi	/\1NOUN_RUUHI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Noun_ovi	/\1NOUN_KIVI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Noun_pieni	/\1NOUN_HIIRI	/' \
        -e 's/\i	1	\)Noun_ovi	/\1NOUN_KIVI	/' \
        -e 's/\(et	1	\)Noun_ovi	/\1NOUN_RIPSET	/' \
        -e 's/\(i	1	\)Noun_pieni	/\1NOUN_RUUHI	/' \
        -e 's/\(i	1	\)Adjective_pieni	/\1ADJ_SUURI	/' \
        -e 's/\(i	1	\)Proper-noun_ovi	/\1PROPN_RUUHI	/' \
        -e 's/\(meri	1	\)Noun_ovi	/\1NOUN_MERI	/' \
        -e 's/\(meri	1	\)Noun_uni	/\1NOUN_MERI	/' \
        -e 's/\(meri	1	\)Proper-noun_uni	/\1PROPN_MERI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Noun_tiili	/\1NOUN_SYLI	/' \
        -e 's/\(i	1	\)Proper-noun_uni	/\1PROPN_TULI	/' \
        -e 's/\(i	1	\)Noun_tiili	/\1NOUN_TULI	/' \
        -e 's/\(i	1	\)Noun_uni	/\1NOUN_HIIRI	/' \
        -e 's/\(et	1	\)Noun_uni	/\1NOUN_ONNET	/' \
        -e 's/\(i	1	\)Noun_nuori	/\1NOUN_HIIRI	/' \
        -e 's/\(i	1	\)Noun_toimi	/\1NOUN_TAIMI	/' \
        -e 's/\(i	1	\)Proper-noun_toimi	/\1PROPN_TAIMI	/' \
        -e 's/\(i	1	\)Proper-noun_ovi	/\1PROPN_RUUHI	/' \
        -e 's/\(i	1	\)Proper-noun_pieni	/\1PROPN_RUUHI	/' \
        -e 's/\(et	1	\)Proper-noun_ovi	/\1PROPN_SAARET	/' \
        -e 's/\(et	1	\)Proper-noun_pieni	/\1PROPN_SAARET	/' \
        -e 's/\(et	1	\)Noun_pieni	/\1NOUN_SAARET	/' \
        -e 's/\(i	1	\)Proper-noun_27	/\1PROPN_KÖYSI	/' \
        -e 's/\(i	1	\)Proper-noun_28	/\1PROPN_VARSI	/' \
        -e 's/\(tsi	1	\)Noun_veitsi	/\1NOUN_VEITSI	/' \
        -e 's/\(i	1	\)Noun_29	/\1NOUN_UKSI	/' \
        -e 's/\(i	1	\)Noun_kaksi	/\1NOUN_HAAKSI	/' \
        -e 's/\(i	1	\)Noun_31	/\1NOUN_HAAKSI	/' \
        -e 's/\(i	1	\)Noun_kynsi	/\1NOUN_LÄNSI	/' \
        -e 's/\(arsi	1	\)Proper-noun_kynsi	/\1PROPN_VARSI	/' \
        -e 's/\(rret	1	\)Proper-noun_kynsi	/\1PROPN_VIIRRET	/' \
        -e 's/\(nnet	1	\)Noun_kynsi	/\1NOUN_KANNET	/' \
        -e 's/\(i	1	\)Noun_lapsi	/\1NOUN_LAPSI	/' \
        -e 's/\([rnl]	1	\)Adjective_sisar	/\1ADJ_TYVEN	/' \
        -e 's/\([rnl]	1	\)Noun_sisar	/\1NOUN_JOUTSEN	/' \
        -e 's/\([rnl]et	1	\)Noun_sisar	/\1NOUN_HÖYHENET	/' \
        -e 's/\([rnl]	1	\)Proper-noun_sisar	/\1PROPN_JOUTSEN	/' \
        -e 's/\(din	1	\)Noun_kytkin	/\1NOUN_SÄÄDIN	/' \
        -e 's/\(ttimet	1	\)Noun_kytkin	/\1NOUN_HOKSOTTIMET	/' \
        -e 's/\(timet	1	\)Noun_kytkin	/\1NOUN_ROHTIMET	/' \
        -e 's/\(imet	1	\)Noun_kytkin	/\1NOUN_KERITSIMET	/' \
        -e 's/\(n	1	\)Noun_koira	/\1NOUN_AAMUKAHDEKSAN	/' \
        -e 's/\([aouAOU].*tin	1	\)Noun_kytkin	/\1NOUN_SUODATIN	/' \
        -e 's/\([aouAOU].*dun	1	\)Noun_kytkin	/\1NOUN_LAIDUN	/' \
        -e 's/\([aouAOU].*n	1	\)Noun_kytkin	/\1NOUN_PUHELIN	/' \
        -e 's/\([äöyÄÖY].*n	1	\)Noun_kytkin	/\1NOUN_ELIN	/' \
        -e 's/\(n	1	\)Noun_kytkin	/\1NOUN_ELIN	/' \
        -e 's/\(n	1	\)Proper-noun_kytkin	/\1PROPN_ELIN	/' \
        -e 's/\(n	1	\)Adjective_kytkin	/\1NOUN_AVOIN	/' \
        -e 's/\(n	1	\)Proper-noun_33	/\1PROPN_SIEMEN	/' \
        -e 's/\(n	1	\)Proper-noun_33A	/\1PROPN_HÄRKIN	/' \
        -e 's/\(kevät	1	\)Noun_kev	/\1NOUN_KEVÄT	/' \
        -e 's/\(venät	1	\)Noun_kev	/\1NOUN_KEVÄT	/' \
        -e 's/\(ton	1	\)Noun_onneton	/\1NOUN_OSATON	/' \
        -e 's/\(tön	1	\)Noun_onneton	/\1NOUN_NIMETÖN	/' \
        -e 's/\(ton	1	\)Adjective_onneton	/\1ADJ_VIATON	/' \
        -e 's/\(tön	1	\)Adjective_onneton	/\1ADJ_KYVYTÖN	/' \
        -e 's/\(ton	1	\)Verb_onneton	/\1ADJ_VIATON	/' \
        -e 's/\(tön	1	\)Verb_onneton	/\1ADJ_KYVYTÖN	/' \
        -e 's/\(pan	1	\)Adjective_vasen	/\1ADJ_HAPAN	/' \
        -e 's/\(n	1	\)Adjective_vasen	/\1ADJ_VASEN	/' \
        -e 's/\(n	1	\)Noun_sisin	/\1NOUN_KYLÄNVANHIN	/' \
        -e 's/\(n	1	\)Adjective_sisin	/\1ADJ_SISIN	/' \
        -e 's/\(n	1	\)Proper-noun_sisin	/\1PROPN_KYLÄNVANHIN	/' \
        -e 's/\([aouAOU].*nen	1	\)Noun_nainen	/\1NOUN_AAKKOSTAMINEN	/' \
        -e 's/\([aouAOU].*nen	1	\)Verb_nainen	/\1NOUN_AAKKOSTAMINEN	/' \
        -e 's/\([äöyÄÖY].*nen	1	\)Proper-noun_38	/\1PROPN_KYLKIÄINEN	/' \
        -e 's/\([äöyÄÖY].*nen	1	\)Noun_nainen	/\1NOUN_KYLKIÄINEN	/' \
        -e 's/\(nen	1	\)Noun_nainen	/\1NOUN_KYLKIÄINEN	/' \
        -e 's/\([äöyÄÖY].*]set	1	\)Noun_nainen	/\1NOUN_RAPPUSET	/' \
        -e 's/\(set	1	\)Noun_nainen	/\1NOUN_RAPPUSET	/' \
        -e 's/\(nen	1	\)Pronomini_38	/\1PRON_JOKAINEN	/' \
        -e 's/\(set	1	\)Proper-noun_nainen	/\1PROPN_RAPPUSET	/' \
        -e 's/\(nen	1	\)Proper-noun_nainen	/\1PROPN_AAKKOSTAMINEN	/' \
        -e 's/\([aouAOU].*nen	1	\)Adjective_nainen	/\1ADJ_AAKKOSELLINEN	/' \
        -e 's/\([äöyÄÖY].*nen	1	\)Adjective_nainen	/\1ADJ_KYLMÄJÄRKINEN	/' \
        -e 's/\(nen	1	\)Pronoun_nainen	/\1ADJ_KYLMÄJÄRKINEN	/' \
        -e 's/\(äs	1	\)Adjective_kahdeksas	/\1NUM_NELJÄS	/' \
        -e 's/\(as	1	\)Numeral_kahdeksas	/\1NUM_KOLMAS	/' \
        -e 's/\(s	1	\)Numeral_kahdeksas	/\1NUM_NELJÄS	/' \
        -e 's/\(s	1	\)Pronoun_kahdeksas	/\1PRON_MONES	/' \
        -e 's/\(sko	1	\)Pronoun_kahdeksas	/\1PRON_MONES	/' \
        -e 's/\(as	1	\)Adjective_kahdeksas	/\1NUM_KOLMAS	/' \
        -e 's/\(s	1	\)Adjective_kahdeksas	/\1NUM_KOLMAS	/' \
        -e 's/\(s	1	\)Proper-noun_vastaus	/\1PROPN_VAKUUTUS	/' \
        -e 's/\(š	1	\)Noun_vastaus	/\1NOUN_HAŠIŠ	/' \
        -e 's/\([äöyÄÖY].*s	1	\)Noun_vastaus	/\1NOUN_RÄJÄYTYS	/' \
        -e 's/\([äöyÄÖY].*s	1	\)Verb_vastaus	/\1NOUN_RÄJÄYTYS	/' \
        -e 's/\(s	1	\)Noun_vastaus	/\1NOUN_VAKUUTUS	/' \
        -e 's/\(s	1	\)Verb_vastaus	/\1NOUN_VAKUUTUS	/' \
        -e 's/\(kset	1	\)Noun_vastaus	/\1NOUN_SERKUKSET	/' \
        -e 's/\(s	1	\)Adjective_vastaus	/\1ADJ_SYMPPIS	/' \
        -e 's/\(us	1	\)Noun_kalleus	/\1NOUN_AAKKOSELLISUUS	/' \
        -e 's/\(udet	1	\)Noun_kalleus	/\1NOUN_OIKEUDET	/' \
        -e 's/\(us	1	\)Proper-noun_kalleus	/\1PROPN_AAKKOSELLISUUS	/' \
        -e 's/\(ys	1	\)Noun_kauneus	/\1NOUN_KÖYHYYS	/' \
        -e 's/\(ys	1	\)Noun_kalleus	/\1NOUN_KÖYHYYS	/' \
        -e 's/\(ys	1	\)Adjective_kalleus	/\1ADJ_LÄHTEISYYS	/' \
        -e 's/\(us	1	\)Adjective_kalleus	/\1ADJ_LÄHTEISYYS	/' \
        -e 's/\(kas	1	\)Proper-noun_vieras	/\1PROPN_ASUKAS	/' \
        -e 's/\(tas	1	\)Proper-noun_vieras	/\1PROPN_RATAS	/' \
        -e 's/\(tis	1	\)Proper-noun_vieras	/\1PROPN_ALTIS	/' \
        -e 's/\(is	1	\)Proper-noun_vieras	/\1PROPN_RUUMIS	/' \
        -e 's/\(is	1	\)Noun_vieras	/\1NOUN_RUUMIS	/' \
        -e 's/\(es	1	\)Noun_vieras	/\1NOUN_KIRVES	/' \
        -e 's/\(tus	1	\)Noun_vieras	/\1NOUN_VANTUS	/' \
        -e 's/\(tuut	1	\)Noun_vieras	/\1NOUN_VANTTUUT	/' \
        -e 's/\(ras	1	\)Noun_vieras	/\1NOUN_VARAS	/' \
        -e 's/\(aat	1	\)Noun_vieras	/\1NOUN_VALJAAT	/' \
        -e 's/\(ies	1	\)Noun_vieras	/\1NOUN_IES	/' \
        -e 's/\(äes	1	\)Noun_vieras	/\1NOUN_IES	/' \
        -e 's/\(is	1	\)Adjective_vieras	/\1ADJ_VALMIS	/' \
        -e 's/\(äs	1	\)Adjective_vieras	/\1ADJ_TYÖLÄS	/' \
        -e 's/\(ngäs	1	\)Proper-noun_vieras	/\1PROPN_KÖNGÄS	/' \
        -e 's/\(ngas	1	\)Proper-noun_vieras	/\1PROPN_KANGAS	/' \
        -e 's/\(mmas	1	\)Noun_vieras	/\1NOUN_HAMMAS	/' \
        -e 's/\(rras	1	\)Proper-noun_vieras	/\1PROPN_PORRAS	/' \
        -e 's/\(das	1	\)Noun_vieras	/\1NOUN_TEHDAS	/' \
        -e 's/\(kas	1	\)Noun_vieras	/\1NOUN_ASUKAS	/' \
        -e 's/\(käs	1	\)Noun_vieras	/\1NOUN_KÄRSÄKÄS	/' \
        -e 's/\(as	1	\)Noun_vieras	/\1NOUN_PATSAS	/' \
        -e 's/\(äs	1	\)Noun_vieras	/\1NOUN_ÄYRÄS	/' \
        -e 's/\(eräs	1	\)Pronoun_vieras	/\1PRON_ERÄS	/' \
        -e 's/\(os	1	\)Noun_vieras	/\1NOUN_UROS	/' \
        -e 's/\(kas	1	\)Adjective_vieras	/\1ADJ_VOIMAKAS	/' \
        -e 's/\(käs	1	\)Adjective_vieras	/\1ADJ_TYYLIKÄS	/' \
        -e 's/\(as	1	\)Adjective_vieras	/\1ADJ_AUTUAS	/' \
        -e 's/\(as	1	\)Proper-noun_vieras	/\1PROPN_PATSAS	/' \
        -e 's/\(es	1	\)Proper-noun_vieras	/\1PROPN_ARISTOTELES	/' \
        -e 's/\(äs	1	\)Proper-noun_vieras	/\1PROPN_ÄYRÄS	/' \
        -e 's/\(ut	1	\)Proper-noun_ohut	/\1PROPN_PUNK	/' \
        -e 's/\(ut	1	\)Noun_ohut	/\1NOUN_OLUT	/' \
        -e 's/\(yt	1	\)Noun_ohut	/\1NOUN_NEITSYT	/' \
        -e 's/\(yt	1	\)Proper-noun_ohut	/\1PROPN_NEITSYT	/' \
        -e 's/\(ut	1	\)Adjective_ohut	/\1ADJ_OLUT	/' \
        -e 's/\(yt	1	\)Adjective_ohut	/\1ADJ_EHYT	/' \
        -e 's/\(es	1	\)Noun_mies	/\1NOUN_MIES	/' \
        -e 's/\(es	1	\)Proper-noun_mies	/\1PROPN_MIES	/' \
        -e 's/\(et	1	\)Proper-noun_44	/\1PROPN_HÄMET	/' \
        -e 's/\(et	1	\)Proper-noun_44C	/\1PROPN_KORTET	/' \
        -e 's/\(et	1	\)Proper-noun_44F	/\1PROPN_AHDET	/' \
        -e 's/\(et	1	\)Proper-noun_44K	/\1PROPN_VIIRRET	/' \
        -e 's/\(et	1	\)Proper-noun_44I	/\1PROPN_VUOLLET	/' \
        -e 's/\(et	1	\)Proper-noun_44J	/\1PROPN_RINNET	/' \
        -e 's/\(äs	1	\)Noun_kahdeksas	/\1ADJ_NELJAS	/' \
        -e 's/\(es	1	\)Noun_kahdeksas	/\1ADJ_NELJAS	/' \
        -e 's/\(as	1	\)Numeral_45	/\1ADJ_KOLMAS	/' \
        -e 's/\(äs	1	\)Numeral_45	/\1ADJ_NELJÄS	/' \
        -e 's/\(tuhat	1	\)Noun_tuhat	/\1NOUN_VUOSITUHAT	/' \
        -e 's/\(ut	1	\)Noun_kuollut	/\1NOUN_AIVOKUOLLUT	/' \
        -e 's/\(eet	1	\)Noun_kuollut	/\1NOUN_LIITTOUTUNEET	/' \
        -e 's/\(yt	1	\)Noun_kuollut	/\1NOUN_SIVISTYNYT	/' \
        -e 's/\(yt	1	\)Adjective_kuollut	/\1ADJ_ÄLLISTYNYT	/' \
        -e 's/\(yt	1	\)Verb_kuollut	/\1ADJ_ÄLLISTYNYT	/' \
        -e 's/\(ut	1	\)Adjective_kuollut	/\1ADJ_KULUNUT	/' \
        -e 's/\(ut	1	\)Verb_kuollut	/\1ADJ_KULUNUT	/' \
        -e 's/\(e	1	\)Proper-noun_hame	/\1PROPN_ASTE	/' \
        -e 's/\(ke	1	\)Noun_hame	/\1NOUN_LÄÄKE	/' \
        -e 's/\(teet	1	\)Noun_hame	/\1NOUN_VAATTEET	/' \
        -e 's/\(eet	1	\)Noun_hame	/\1NOUN_RÄMEET	/' \
        -e 's/\(ke	1	\)Proper-noun_hame	/\1PROPN_LÄÄKE	/' \
        -e 's/\(oe	1	\)Noun_hame	/\1NOUN_KOE	/' \
        -e 's/\(tet	1	\)Proper-noun_hame	/\1PROPN_KORTET	/' \
        -e 's/\(eet	1	\)Proper-noun_hame	/\1PROPN_HIUTALET	/' \
        -e 's/\(de	1	\)Proper-noun_hame	/\1PROPN_LUODE	/' \
        -e 's/\(nne	1	\)Proper-noun_hame	/\1PROPN_RAKENNE	/' \
        -e 's/\(rre	1	\)Proper-noun_hame	/\1PROPN_KIERRE	/' \
        -e 's/\(i	1	\)Noun_hame	/\1NOUN_ORI	/' \
        -e 's/\(keet	1	\)Noun_hame	/\1NOUN_ALKEET	/' \
        -e 's/\(ylje	1	\)Noun_hame	/\1NOUN_HYLJE	/' \
        -e 's/\([aouAOU].*de	1	\)Noun_hame	/\1NOUN_LUODE	/' \
        -e 's/\([aouAOU].*nne	1	\)Noun_hame	/\1NOUN_RAKENNE	/' \
        -e 's/\([aouAOU].*te	1	\)Noun_hame	/\1NOUN_OSOITE	/' \
        -e 's/\([äöyÄÖY].*de	1	\)Noun_hame	/\1NOUN_KIDE	/' \
        -e 's/\([äöyÄÖY].*nne	1	\)Noun_hame	/\1NOUN_KIINNE	/' \
        -e 's/\([aouAOU].*e	1	\)Noun_hame	/\1NOUN_ASTE	/' \
        -e 's/\([äöyÄÖY].*e	1	\)Noun_hame	/\1NOUN_PISTE	/' \
        -e 's/\(e	1	\)Noun_hame	/\1NOUN_PISTE	/' \
        -e 's/\(e	1	\)Adjective_hame	/\1ADJ_TERVE	/' \
        -e 's/\(e	1	\)Proper-noun_hame	/\1PROPN_ASTE	/' \
        -e 's/\(säen	1	\)Noun_askel	/\1NOUN_SÄEN	/' \
        -e 's/\([lrn]	1	\)Noun_askel	/\1NOUN_SIEMEN	/' \
        -e 's/\([nrl]e	1	\)Noun_askel	/\1NOUN_ASTE	/' \
        -e 's/\(nner	1	\)Proper-noun_askel	/\1PROPN_MANNER	/' \
        -e 's/\(l	1	\)Proper-noun_askel	/\1PROPN_TAIVAL	/' \
        -e 's/\([nrl]e	1	\)Proper-noun_askel	/\1PROPN_ASTE	/' \
        -e 's/\(.	1	\)Noun_51	/\1NOUN_51XXX	/' \
        -e 's/\(.	1	\)Numeral_51	/\1NUM_51XXX	/' \
        -e 's/\(.	1	\)Pronoun_51	/\1PRON_51XXX	/' \
        -e 's/\(.	1	\)Proper-noun_51	/\1PROPN_51XXX	/' |\
    $SED -e 's/\(ttaa	1	\)Noun_muistaa	/\1VERB_VIEROITTAA	/' \
        -e 's/\(ttaa	1	\)Verb_muistaa	/\1VERB_VIEROITTAA	/' \
        -e 's/\(a	1	\)Verb_kaivaa	/\1VERB_KASVAA	/' \
        -e 's/\(tää	1	\)Verb_huutaa	/\1VERB_PYYTÄÄ	/' \
        -e 's/\(ntää	1	\)Verb_muistaa	/\1VERB_HIVENTÄÄ	/' \
        -e 's/\(tää	1	\)Verb_muistaa	/\1VERB_YSKÄHTÄÄ	/' \
        -e 's/\(tää	1	\)Noun_muistaa	/\1VERB_YSKÄHTÄÄ	/' \
        -e 's/\(ttua	1	\)Verb_sanoa	/\1VERB_HERMOTTUA	/' \
        -e 's/\(pyä	1	\)Verb_sanoa	/\1VERB_SYÖPYÄ	/' \
        -e 's/\(rtyä	1	\)Noun_sanoa	/\1VERB_KIERTYÄ	/' \
        -e 's/\(rtyä	1	\)Verb_sanoa	/\1VERB_KIERTYÄ	/' \
        -e 's/\(ntyä	1	\)Verb_sanoa	/\1VERB_TYHJENTYÄ	/' \
        -e 's/\(oa	1	\)Verb_sanoa	/\1VERB_PUNOA	/' \
        -e 's/\(ua	1	\)Noun_sanoa	/\1VERB_KAUNISTUA	/' \
        -e 's/\(ua	1	\)Verb_sanoa	/\1VERB_KAUNISTUA	/' \
        -e 's/\(yä	1	\)Verb_sanoa	/\1VERB_ÄLLISTYÄ	/' \
        -e 's/\(ata	1	\)Noun_salata	/\1VERB_ARVATA	/' \
        -e 's/\(aa	1	\)Verb_salata	/\1VERB_ARVATA	/' \
        -e 's/\(ata	1	\)Verb_salata	/\1VERB_ARVATA	/' \
        -e 's/\(ätä	1	\)Verb_salata	/\1VERB_YNNÄTÄ	/' \
        -e 's/\(ltaa	1	\)Verb_huutaa	/\1VERB_SIVALTAA	/' \
        -e 's/\(rtää	1	\)Verb_huutaa	/\1VERB_NÄPERTÄÄ	/' \
        -e 's/\(rtaa	1	\)Verb_huutaa	/\1VERB_KUHERTAA	/' \
        -e 's/\(ntää	1	\)Verb_huutaa	/\1VERB_HIVENTÄÄ	/' \
        -e 's/\(ntaa	1	\)Verb_huutaa	/\1VERB_HUONONTAA	/' \
        -e 's/\(ntaa	1	\)Verb_muistaa	/\1VERB_HUONONTAA	/' \
        -e 's/\(a	1	\)Verb_muistaa	/\1VERB_MUTRISTAA	/' \
        -e 's/\(ä	1	\)Verb_muistaa	/\1VERB_KIVISTÄÄ	/' \
        -e 's/\(a	1	\)Noun_tulla	/\1VERB_ETUILLA	/' \
        -e 's/\(a	1	\)Verb_tulla	/\1VERB_ETUILLA	/' \
        -e 's/\(ä	1	\)Verb_tulla	/\1VERB_ÄKSYILLÄ	/' \
        -e 's/\(a	1	\)Verb_juoda	/\1VERB_TUODA	/' \
        -e 's/\(ä	1	\)Verb_juoda	/\1VERB_SYÖDÄ	/' \
        -e 's/\(a	1	\)Verb_rohkaista	/\1VERB_MARISTA	/' \
        -e 's/\(ä	1	\)Verb_rohkaista	/\1VERB_ÄRISTÄ	/' \
        -e 's/\(a	1	\)Verb_valita	/\1VERB_PALKITA	/' \
        -e 's/\(ä	1	\)Verb_valita	/\1VERB_MERKITÄ/' \
        -e 's/\(a	1	\)Verb_saada	/\1VERB_SAADA	/' \
        -e 's/\(a	1	\)Verb_voida	/\1VERB_KOPIOIDA	/' \
        -e 's/\(ä	1	\)Verb_voida	/\1VERB_ÖYKKÄRÖIDÄ	/' \
        -e 's/\(ä	1	\)Verb_saada	/\1VERB_MYYDÄ	/' \
        -e 's/\(a	1	\)Verb_juosta	/\1VERB_JUOSTA	/' \
        -e 's/\(ä	1	\)Verb_juosta	/\1VERB_PIESTÄ	/' \
        -e 's/\(pia	1	\)Verb_sallia	/\1VERB_RAAPIA	/' \
        -e 's/\(ä	1	\)Verb_sallia	/\1VERB_RYSKIÄ	/' \
        -e 's/\(a	1	\)Verb_sallia	/\1VERB_KOSIA	/' \
        -e 's/\(a	1	\)Verb_tupakoida	/\1VERB_MELLAKOIDA	/' \
        -e 's/\(ä	1	\)Verb_tupakoida	/\1VERB_ISÄNNÖIDÄ	/' \
        -e 's/\(a	1	\)Verb_katketa	/\1VERB_KARHUTA	/' \
        -e 's/\(detä	1	\)Verb_katketa	/\1VERB_VYYHDETÄ	/' \
        -e 's/\(jetä	1	\)Verb_katketa	/\1VERB_ILJETÄ	/' \
        -e 's/\(ä	1	\)Verb_katketa	/\1VERB_TÄHYTÄ	/' \
        -e 's/\(ä	1	\)Verb_selvit	/\1VERB_SELVITÄ	/' \
        -e 's/\(a	1	\)Verb_selvit	/\1VERB_KARHUTA	/' \
        -e 's/\(a	1	\)Adjective_selvit	/\1VERB_KARHUTA	/' \
        -e 's/\(ä	1	\)Verb_vanheta	/\1VERB_LÄMMETÄ	/' \
        -e 's/\(a	1	\)Verb_vanheta	/\1VERB_POIKETA	/' \
        -e 's/\(rkeä	1	\)Verb_laskea	/\1VERB_SÄRKEÄ	/' \
        -e 's/\(keä	1	\)Verb_laskea	/\1VERB_KYTKEÄ	/' \
        -e 's/\(peä	1	\)Verb_laskea	/\1VERB_RYPEÄ	/' \
        -e 's/\(eä	1	\)Verb_laskea	/\1VERB_KYTKEÄ	/' \
        -e 's/\(ea	1	\)Verb_laskea	/\1VERB_SOTKEA	/' \
        -e 's/\(tää	1	\)Verb_soutaa	/\1VERB_KIITÄÄ	/' \
        -e 's/\(taa	1	\)Verb_soutaa	/\1VERB_MOJAHTAA	/' \
        -e 's/\(taa	1	\)Verb_taitaa	/\1VERB_TAITAA	/' \
        -e 's/\(taa	1	\)Verb_saartaa	/\1VERB_SAARTAA	/' \
        -e 's/\(taa	1	\)Verb_huutaa	/\1VERB_HUUTAA	/' \
        -e 's/\(ää	1	\)Verb_kaikaa	/\1VERB_ÄHKÄÄ	/' \
        -e 's/\(aa	1	\)Verb_kaikaa	/\1VERB_RAIKAA	/' \
        -e 's/\(aa	1	\)Verb_kumajaa	/\1VERB_VIPAJAA	/' \
        -e 's/\(ää	1	\)Verb_kumajaa	/\1VERB_HELÄJÄÄ	/' \
        -e 's/\(	1	\)Verb_ei	/\1X_IGNORE	/' \
        -e 's/\(	1	\)Adjective_pron	/\1ADJ_XXX	/' \
        -e 's/\(	1	\)Adverb_pron	/\1ADV_XXX	/' \
        -e 's/\(	1	\)Adverb_pred	/\1ADV_NOPEASTI	/' \
        -e 's/\(	1	\)Adverb_kala	/\1ADV_NOPEASTI	/' \
        -e 's/\(	1	\)Adverb_koira	/\1ADV_NOPEASTI	/' \
        -e 's/\(	1	\)Noun_pron	/\1NOUN_XXX	/' \
        -e 's/\(	1	\)Numeral_pron	/\1NUM_XXX	/' \
        -e 's/\(	1	\)Pronoun_pron	/\1PRON_XXX	/' \
        -e 's/\(	1	\)Prefix_pron	/\1NOUN_YLEIS-	/' \
        -e 's/\(	1	\)Preposition_pron	/\1ADP_MUKAISESTI	/' \
        -e 's/\(	1	\)Adjective_l	/\1ADJ_XXX	/' \
        -e 's/\(	1	\)Adjective_k	/\1ADJ_XXX	/' \
        -e 's/\(	1	\)Verb_l	/\1VERB_XXX	/' \
        -e 's/\(	1	\)Verb_k	/\1VERB_XXX	/' \
        -e 's/\(	1	\)Noun_k	/\1NOUN_XXX	/' \
        -e 's/\(	1	\)Proper-noun_k	/\1PROPN_XXX	/' \
        -e 's/\([[:upper:]]	1	\)Proper-noun_[a-z]*	/\1PROPN_ACRO_XXX	/' \
        -e 's/\([[:upper:]]	1	\)Noun_[a-z]*	/\1NOUN_ACRO_XXX	/' |\
    $SED -e 's/1	NOUN/NOUN	NOUN/' \
        -e 's/1	PROPN/PROPN	PROPN/' \
        -e 's/1	VERB/VERB	VERB/' \
        -e 's/1	ADJ/ADJ	ADJ/' \
        -e 's/1	NUM/NUM	NUM/' \
        -e 's/1	PRON/PRON	PRON/' \
        -e 's/1	ADP/ADP	ADP/' \
        -e 's/1	ADV/ADV	ADV/' |\
    $SED -e 's/		/	/' \
        -e "s/'/’/g" \
        -e 's/[[:space:]]*$//'
done
# see what else we can
#cat fiwikt.tempxml |\
# pick all classified for now
#    fgrep -v '<kotus' |\
#    egrep 'Interjektio|Adverbi|Konjunktion|Prepositio' |\
#    egrep -v 'Verbi|Substantiivi|Adjektiivi|Pronomini|Numeraali' |\
#    fgrep -v 'lemma>-' |\
# make csv
#    $SED -re 's/^.*<lemma>([^<]*).*<wordclass>([^<]*).*$/\1,\2/' |\
# remove missing lemmas or classes shown as leftover tags from ^^
#    fgrep -v '<entry>' |\
#    tr '|' ',' |\
#    $SED -re 's/([[:digit:]]+)-([[:upper:]])/\1,\2/' |\
#    gawk -F , 'NF == 2 {printf("%s\t1\t%s\tfiwikt\n", $1, $2);}' |\
#    $SED -e 's/Adverbi_99/ADV_NOPEASTI/' \
#        -e 's/Adverbi/ADV_NOPEASTI/' \
#        -e 's/Prepositio/ADP_MUKAISESTI/' \
#        -e 's/Interjektio/INTJ_HAH/' \
#        -e 's/Konjunktio/SCONJ_ETTÄ/'
