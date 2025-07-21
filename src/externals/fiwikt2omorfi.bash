#!/bin/bash
# This script takes a Finnish wiktionary xml dump and converts it to omorfi
# Originally from end assignment of CLT 131 in Uni. Helsinki by ...
# Bit of coding style fixes and updates by <flammie@iki.fi>

SED=sed
print_usage() {
    echo "Usage: $0 [fiwikt-pages-articles.xml]"
    echo
    echo "fiwikt-pages-articles.xml must point to unzipped fi.wiktionary dump."
    echo "If omitted, stdin is uSED"
}

if test $# -ge 2 ; then
    print_usage
    exit 1
fi

# Define word class
wc='(Substantiivi|Adjektiivi|Pronomini|Numeraali|Prepositio|Adverbi|Interjektio|Konjunktio|Partikkeli|Verbi|Erisnimi)'
# Fetch only relevant lines from the xml dump (NOTE: This assumes relevant
# lines are between <page> & </page> tags)
cat $@ | $SED -ne '/<page>/,/<\/page>/p' |\
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
    fgrep "==Suomi==" |\
# Remove certain MediaWiki pages
    $SED -r "/<title>(Luokka:)|(Malline:)|(Wikisanakirja:)/d" |\
# Place tags and content on separate lines
    $SED -re "s/(<\/page>)/\n\1/g" \
    -e "s/(<title>)/\n\1/g" \
    -e "s/(<\/title>)/\1\n/g" \
    -e "s/(<text [^>]*>)/\1\n/g" \
    -e "s/(<\/text>)/\n\1/g" |\
# Place relevant content markup characters on seperate lines
    $SED -re "s/(==*[[:alpha:]]+==)/\n\1/g" \
    -e "s/((\(\{\{)|(\{\{fi))/\n\1/g" \
    -e "s/(#)/\n\1/g" |\
# Parse lines and tag word classes in headings (example: ===Substantiivi===)
    $SED -re "s/=$wc=/<wordclass>\1<\/wordclass>/g" |\
# Parse lines and tag with KOTUS numbering (this script only allows
# {{taivutustyyppi|99(alt: 99-A), {{fi-taivitus|99 & {{fi-subs-99 formats)
# {{fi-subs|14|A}}
    $SED -re "s/\{\{taivutustyyppi\|([[:alnum:]]+-?[[:alnum:]]?)\}\}/<kotus>\1<\/kotus>/" \
    -e "s/\{\{fi-taivutus\|([[:digit:]]+(\|?[[:upper:]])*)/<kotus>\1<\/kotus>/" \
    -e "s/\{\{fi-[[:alpha:]]*-([[:digit:]]+)\}\}/<kotus>\1<\/kotus>/" \
    -e "s/\{\{fi-[[:alpha:]]*\|([[:digit:]]+)\|([A-Z])\}\}/<kotus>\1-\2<\/kotus>/" \
    -e "s/\{\{fi-[[:alpha:]]*\|([[:digit:]]+)\}\}/<kotus>\1<\/kotus>/" |\
# Parse lines that begin with # but not #: and tag with definition
    $SED -re "s/^#([^#:].*)$/<definition>\1<\/definition>/g" |\
# Parse lines that begin with #: and tag with example
    $SED -re "s/^#:(.*)$/<example>\1<\/example>/g" |\
# Place tags on separate lines
    $SED -re "s/(<(wordclass|kotus|definition|example)>.*<\/(wordclass|kotus|definition|example)>)/\n\1\n/g" |\
# Remove all  non-tagged lines
    $SED -rn "/^<.*>$/p" |\
# Remove definitions that are for conjugated words, i.e. retain only
# definitions of unconjugated words
    $SED -r "/(\{\{taivm)|(-taivm\|)|(\(taivutusmuoto)|(\(taivutusmuodot)|(taivutusmuoto'')|(\(taivus)/d" | egrep -v "\[\[Luokka:Suomen ([[:alpha:]]+) taivutusmuodot\]\]" |\
# remover text element ??
    $SED -re 's/<text bytes[^>]*>//' |\
# Parse remove wikimedia links, formatting and other tuff
    $SED -r "s/\[\[[[:alpha:]]+\|([[:alpha:]]+)\]\]/\1/g" |\
# Parse and remove other wikimedia markup "garbage"
    $SED -re "/\[\[[[:alpha:]]+:[[:alpha:]]+.*\]\]/d" -e "/\{.*\}/d" |\
    $SED -re "s/\[|\]//g" -e "s/'|#|#://g" |\
# Remove unescessary <text> & </text> tags
    $SED -re "/^<text |<\/text>/d" |\
# Rename remaining wiktionary xml tags: page to entry, title to lemma
    $SED -re "s/page>$/entry>/g" -e "s/title>/lemma>/g" |
# Remove linebreaks
    tr -d '\n' |\
# Place each <entry> on a separate line
    $SED -re "s/(<entry>)/\n\1/g" |\
# Remove some MWEs
    egrep '<lemma>[^ ]*<\/lemma>' |\
# Place entries in alphabetical order (due to uniform xml strucuture sort
# command works normally) and write as .xml file
    sort | tee fiwikt.tempxml |\
# pick all classified for now
    fgrep '<kotus' |\
    fgrep -v 'lemma>-' |\
# make csv
    $SED -re 's/^.*<lemma>([^<]*).*<wordclass>([^<]*).*<kotus>([^<]*).*$/\1,\3,\2/' |\
# remove missing lemmas or classes shown as leftover tags from ^^
    fgrep -v '<entry>' |\
    tr '|' ',' |\
    $SED -re 's/([[:digit:]]+)-([[:upper:]])/\1,\2/' |\
    gawk -F , 'NF == 3 {printf("%s\t1\t%s_%s\tfiwikt\n", $1, $3, $2);}
        NF == 4 {printf("%s\t1\t%s_%s%s\tfiwikt\n", $1, $4, $2, $3);}' |\
    $SED -e 's/Substantiivi\(_5[2-9]\|_[67][0-9]\)/Verbi\1/' |\
    $SED -e 's/Adverbi_99/ADV_NOPEASTI/' \
        -e 's/Interjektio_[^	]*/INTJ_HAH/' \
        -e 's/\(o	1	\)Adjektiivi_1	/\1ADJ_KOHELO	/' \
        -e 's/\(u	1	\)Adjektiivi_1	/\1ADJ_VALKAISTU	/' \
        -e 's/\(y	1	\)Adjektiivi_1	/\1ADJ_HÄPÄISTY	/' \
        -e 's/\(ö	1	\)Adjektiivi_1	/\1ADJ_HÖLÖ	/' \
        -e 's/\(o	1	\)Substantiivi_1	/\1NOUN_TALO	/' \
        -e 's/\(ot	1	\)Substantiivi_1	/\1NOUN_AIVOT	/' \
        -e 's/\(o	1	\)Erisnimi_1	/\1PROPN_TALO	/' \
        -e 's/\(u	1	\)Substantiivi_1	/\1NOUN_ASU	/' \
        -e 's/\(ut	1	\)Substantiivi_1	/\1NOUN_HOUSUT	/' \
        -e 's/\(yt	1	\)Substantiivi_1	/\1NOUN_PÖKSYT	/' \
        -e 's/\(y	1	\)Substantiivi_1	/\1NOUN_KÄRRY	/' \
        -e 's/\(ö	1	\)Substantiivi_1	/\1NOUN_MÖMMÖ	/' \
        -e 's/\(öt	1	\)Substantiivi_1	/\1NOUN_PÖLLÖT	/' \
        -e 's/\(i	1	\)Substantiivi_1	/\1NOUN_XXXFAIL	/' \
        -e 's/\(e	1	\)Substantiivi_1	/\1NOUN_XXXFAIL	/' \
        -e 's/\(y	1	\)Erisnimi_1	/\1PROPN_KÄRRY	/' \
        -e 's/\(u	1	\)Erisnimi_1	/\1PROPN_ASU	/' \
        -e 's/\(ö	1	\)Erisnimi_1	/\1PROPN_MÖMMÖ	/' \
        -e 's/\(o	1	\)Erisnimi_1A	/\1PROPN_UKKO	/' \
        -e 's/\(o	1	\)Adjektiivi_1A	/\1ADJ_KOLKKO	/' \
        -e 's/\(ö	1	\)Adjektiivi_1A	/\1ADJ_KÖKKÖ	/' \
        -e 's/\(o	1	\)Substantiivi_1A	/\1NOUN_UKKO	/' \
        -e 's/\(ot	1	\)Substantiivi_1A	/\1NOUN_JOUKOT	/' \
        -e 's/\(u	1	\)Substantiivi_1A	/\1NOUN_TIKKU	/' \
        -e 's/\(ut	1	\)Substantiivi_1A	/\1NOUN_FARKUT	/' \
        -e 's/\(y	1	\)Substantiivi_1A	/\1NOUN_MYRKKY	/' \
        -e 's/\(ö	1	\)Substantiivi_1A	/\1NOUN_YÖKKÖ	/' \
        -e 's/\(u	1	\)Erisnimi_1A	/\1PROPN_TIKKU	/' \
        -e 's/\(u	1	\)Adjektiivi_1B	/\1ADJ_IKÄLOPPU	/' \
        -e 's/\(ut	1	\)Substantiivi_1B	/\1NOUN_RAPUT	/' \
        -e 's/\(ot	1	\)Substantiivi_1B	/\1NOUN_PEIPOT	/' \
        -e 's/\(o	1	\)Substantiivi_1B	/\1NOUN_HAPPO	/' \
        -e 's/\(u	1	\)Substantiivi_1B	/\1NOUN_LIPPU	/' \
        -e 's/\(y	1	\)Substantiivi_1B	/\1NOUN_RYYPPY	/' \
        -e 's/\(ö	1	\)Substantiivi_1B	/\1NOUN_TÖRPPÖ	/' \
        -e 's/\(o	1	\)Erisnimi_1B	/\1PROPN_HAPPO	/' \
        -e 's/\(y	1	\)Erisnimi_1B	/\1PROPN_RYYPPY	/' \
        -e 's/\(ut	1	\)Substantiivi_1C	/\1NOUN_HOUSUT	/' \
        -e 's/\(o	1	\)Substantiivi_1C	/\1NOUN_HIRTTO	/' \
        -e 's/\(o	1	\)Erisnimi_1C	/\1PROPN_HIRTTO	/' \
        -e 's/\(u	1	\)Adjektiivi_1C	/\1ADJ_VIMMATTU	/' \
        -e 's/\(y	1	\)Adjektiivi_1C	/\1ADJ_YLENNETTY	/' \
        -e 's/\(u	1	\)Verbi_1C	/\1ADJ_VIMMATTU	/' \
        -e 's/\(y	1	\)Verbi_1C	/\1ADJ_YLENNETTY	/' \
        -e 's/\(u	1	\)Substantiivi_1C	/\1NOUN_TORTTU	/' \
        -e 's/\(y	1	\)Substantiivi_1C	/\1NOUN_PYTTY	/' \
        -e 's/\(ö	1	\)Substantiivi_1C	/\1NOUN_PÖNTTÖ	/' \
        -e 's/\(u	1	\)Erisnimi_1C	/\1PROPN_TORTTU	/' \
        -e 's/\(y	1	\)Erisnimi_1C	/\1PROPN_PYTTY	/' \
        -e 's/\(ö	1	\)Erisnimi_1C	/\1PROPN_PÖNTTÖ	/' \
        -e 's/\(u	1	\)Substantiivi_1D	/\1NOUN_ALKU	/' \
        -e 's/\(y	1	\)Substantiivi_1D	/\1NOUN_NÄKY	/' \
        -e 's/\(u	1	\)Erisnimi_1D	/\1PROPN_ALKU	/' \
        -e 's/\(o	1	\)Substantiivi_1D	/\1NOUN_RUOKO	/' \
        -e 's/\(o	1	\)Erisnimi_1D	/\1PROPN_RUOKO	/' \
        -e 's/\(ö	1	\)Substantiivi_1D	/\1NOUN_NÄKÖ	/' \
        -e 's/\(o	1	\)Substantiivi_1E	/\1NOUN_HEPO	/' \
        -e 's/\(u	1	\)Substantiivi_1E	/\1NOUN_APU	/' \
        -e 's/\(y	1	\)Substantiivi_1E	/\1NOUN_KÄPY	/' \
        -e 's/\(o	1	\)Erisnimi_1E	/\1PROPN_VETO	/' \
        -e 's/\(u	1	\)Erisnimi_1E	/\1PROPN_APU	/' \
        -e 's/\(u	1	\)Adjektiivi_1F	/\1ADJ_VIIPALOITU	/' \
        -e 's/\(o	1	\)Adjektiivi_1F	/\1NOUN_MIETO	/' \
        -e 's/\(y	1	\)Adjektiivi_1F	/\1ADJ_YKSILÖITY	/' \
        -e 's/\(o	1	\)Substantiivi_1F	/\1NOUN_VETO	/' \
        -e 's/\(u	1	\)Substantiivi_1F	/\1NOUN_KUITU	/' \
        -e 's/\(y	1	\)Substantiivi_1F	/\1NOUN_VETY	/' \
        -e 's/\(ö	1	\)Substantiivi_1F	/\1NOUN_HÄÄTÖ	/' \
        -e 's/\(ot	1	\)Substantiivi_1F	/\1NOUN_PIDOT	/' \
        -e 's/\(o	1	\)Erisnimi_1F	/\1PROPN_VETO	/' \
        -e 's/\(u	1	\)Erisnimi_1F	/\1PROPN_KUITU	/' \
        -e 's/\(o	1	\)Substantiivi_1G	/\1NOUN_RUNKO	/' \
        -e 's/\(u	1	\)Substantiivi_1G	/\1NOUN_VINKU	/' \
        -e 's/\(y	1	\)Substantiivi_1G	/\1NOUN_SÄNKY	/' \
        -e 's/\(ö	1	\)Substantiivi_1G	/\1NOUN_YLÄNKÖ	/' \
        -e 's/\(o	1	\)Erisnimi_1G	/\1PROPN_RUNKO	/' \
        -e 's/\(ö	1	\)Erisnimi_1G	/\1PROPN_YLÄNKÖ	/' \
        -e 's/\(o	1	\)Substantiivi_1H	/\1NOUN_SAMPO	/' \
        -e 's/\(u	1	\)Substantiivi_1H	/\1NOUN_RUMPU	/' \
        -e 's/\(ö	1	\)Substantiivi_1H	/\1NOUN_LÄMPÖ	/' \
        -e 's/\(u	1	\)Erisnimi_1H	/\1PROPN_RUMPU	/' \
        -e 's/\(o	1	\)Substantiivi_1I	/\1NOUN_KIELTO	/' \
        -e 's/\(ö	1	\)Substantiivi_1I	/\1NOUN_SISÄLTÖ§	/' \
        -e 's/\(o	1	\)Erisnimi_1I	/\1PROPN_KIELTO	/' \
        -e 's/\(ut	1	\)Substantiivi_1J	/\1NOUN_LINNUT	/' \
        -e 's/\(o	1	\)Substantiivi_1J	/\1NOUN_TUNTO	/' \
        -e 's/\(u	1	\)Substantiivi_1J	/\1NOUN_LINTU	/' \
        -e 's/\(y	1	\)Substantiivi_1J	/\1NOUN_MÄNTY	/' \
        -e 's/\(ö	1	\)Substantiivi_1J	/\1NOUN_KÄÄNTÖ	/' \
        -e 's/\(o	1	\)Erisnimi_1J	/\1PROPN_TUNTO	/' \
        -e 's/\(o	1	\)Substantiivi_1K	/\1NOUN_SIIRTO	/' \
        -e 's/\(o	1	\)Erisnimi_1K	/\1PROPN_SIIRTO	/' \
        -e 's/\(y	1	\)Substantiivi_1L	/\1NOUN_NÄKY	/' \
        -e 's/\(o	1	\)Substantiivi_1M	/\1NOUN_RUOKO	/' \
        -e 's/\(u	1	\)Substantiivi_1M	/\1NOUN_SUKU	/' \
        -e 's/\(y	1	\)Substantiivi_1M	/\1NOUN_KYKY	/' \
        -e 's/\(ö	1	\)Adjektiivi_2	/\1ADJ_HÖLÖ	/' \
        -e 's/\(ot	1	\)Substantiivi_2	/\1NOUN_AIVOT	/' \
        -e 's/\(o	1	\)Substantiivi_2	/\1NOUN_RUIPELO	/' \
        -e 's/\(u	1	\)Substantiivi_2	/\1NOUN_SEIKKAILU	/' \
        -e 's/\(y	1	\)Substantiivi_2	/\1NOUN_VEHKEILY	/' \
        -e 's/\(ö	1	\)Substantiivi_2	/\1NOUN_JÄÄTELÖ	/' \
        -e 's/\(i	1	\)Substantiivi_2	/\1NOUN_XXXFAIL	/' \
        -e 's/\(y	1	\)Erisnimi_2	/\1PROPN_VEHKEILY	/' \
        -e 's/\(o	1	\)Erisnimi_2	/\1PROPN_RUIPELO	/' \
        -e 's/\(u	1	\)Erisnimi_2	/\1PROPN_SEIKKAILU	/' \
        -e 's/\(öt	1	\)Substantiivi_3	/\1NOUN_YHTIÖT	/' \
        -e 's/\(o	1	\)Substantiivi_3	/\1NOUN_TUOMIO	/' \
        -e 's/\(u	1	\)Substantiivi_3	/\1NOUN_SEIKKAILU	/' \
        -e 's/\(ö	1	\)Substantiivi_3	/\1NOUN_HÄIRIÖ	/' \
        -e 's/\(e	1	\)Substantiivi_3	/\1NOUN_ZOMBIE	/' \
        -e 's/\(ot	1	\)Substantiivi_3	/\1NOUN_RAUNIOT	/' \
        -e 's/\(o	1	\)Erisnimi_3	/\1PROPN_TUOMIO	/' \
        -e 's/\(e	1	\)Erisnimi_3	/\1PROPN_ZOMBIE	/' \
        -e 's/\(ö	1	\)Erisnimi_3	/\1PROPN_HÄIRIÖ	/' \
        -e 's/\(ö	1	\)Adjektiivi_4A	/\1ADJ_KÖKKÖ	/' \
        -e 's/\(o	1	\)Substantiivi_4	/\1NOUN_LEPAKKO	/' \
        -e 's/\(ö	1	\)Substantiivi_4	/\1NOUN_YKSIKKÖ	/' \
        -e 's/\(ot	1	\)Substantiivi_4A	/\1NOUN_LUOLIKOT	/' \
        -e 's/\(o	1	\)Substantiivi_4A	/\1NOUN_LEPAKKO	/' \
        -e 's/\(ö	1	\)Substantiivi_4A	/\1NOUN_YKSIKKÖ	/' \
        -e 's/\(o	1	\)Substantiivi_4D	/\1NOUN_LEPAKKO	/' \
        -e 's/\(ö	1	\)Substantiivi_4D	/\1NOUN_YKSIKKÖ	/' \
        -e 's/\(a	1	\)Substantiivi_4	/\1NOUN_XXXFAIL	/' \
        -e 's/\(o	1	\)Erisnimi_4A	/\1PROPN_LEPAKKO	/' \
        -e 's/\(ö	1	\)Erisnimi_4A	/\1PROPN_YKSIKKÖ	/' \
        -e 's/\(o	1	\)Substantiivi_4C	/\1NOUN_HIRTTO	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Adjektiivi_5	/\1ADJ_STYDI	/' \
        -e 's/\(i	1	\)Adjektiivi_5	/\1ADJ_ABNORMI	/' \
        -e 's/\([äöyÄÖY].*[kptsvdx]	1	\)Adjektiivi_5	/\1ADJ_CHIC	/' \
        -e 's/\([kptsvdxr]	1	\)Adjektiivi_5	/\1ADJ_COOL	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Erisnimi_5	/\1PROPN_TYYLI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Substantiivi_5	/\1NOUN_TYYLI	/' \
        -e 's/\(kasvit	1	\)Substantiivi_5	/\1NOUN_LASIT	/' \
        -e 's/\([äöyÄÖY].*[cmnrhflrktbpvsxgdšzž]	1	\)Substantiivi_5	/\1NOUN_ZEN	/' \
        -e 's/\([äöyÄÖY].*[cmrnhflrktbpsvxgdšzž]	1	\)Erisnimi_5	/\1PROPN_ZEN	/' \
        -e 's/\([cmnhflrktvbrpsxšgdzž]	1	\)Substantiivi_5	/\1NOUN_PUNK	/' \
        -e 's/\([cmnhflrktvbrpsxšgdzž]	1	\)Substantiivi_5A	/\1NOUN_PUNK	/' \
        -e 's/\([cmnhflrktbvprsxšgdzž]	1	\)Erisnimi_5	/\1PROPN_PUNK	/' \
        -e 's/\(i	1	\)Erisnimi_5	/\1PROPN_RUUVI	/' \
        -e 's/\(i	1	\)Substantiivi_5	/\1NOUN_RUUVI	/' \
        -e 's/\(e	1	\)Substantiivi_5	/\1NOUN_XXXFAIL	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Substantiivi_5A	/\1NOUN_HÄKKI	/' \
        -e 's/\(i	1	\)Substantiivi_5A	/\1NOUN_LOKKI	/' \
        -e 's/\(it	1	\)Substantiivi_5A	/\1NOUN_PANKIT	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Erisnimi_5A	/\1PROPN_HÄKKI	/' \
        -e 's/\(i	1	\)Erisnimi_5A	/\1PROPN_LOKKI	/' \
        -e 's/\([aou].*i	1	\)Erisnimi_5B	/\1PROPN_KUPPI	/' \
        -e 's/\(i	1	\)Erisnimi_5B	/\1PROPN_TYYPPI	/' \
        -e 's/\([aou].*i	1	\)Substantiivi_5B	/\1NOUN_KUPPI	/' \
        -e 's/\(i	1	\)Substantiivi_5B	/\1NOUN_TYYPPI	/' \
        -e 's/\(it	1	\)Substantiivi_5B	/\1NOUN_KLUMPIT§	/' \
        -e 's/\(it	1	\)Erisnimi_5C	/\1PROPN_KASTANJETIT	/' \
        -e 's/\(i	1	\)Erisnimi_5C	/\1PROPN_KORTTI	/' \
        -e 's/\(i	1	\)Adjektiivi_5C	/\1ADJ_HURTTI	/' \
        -e 's/\(i	1	\)Substantiivi_5C	/\1NOUN_KORTTI	/' \
        -e 's/\(it	1	\)Substantiivi_5C	/\1NOUN_KASTANJETIT	/' \
        -e 's/\(i	1	\)Substantiivi_5D	/\1NOUN_LAKI	/' \
        -e 's/\(i	1	\)Substantiivi_5E	/\1NOUN_KUPPI	/' \
        -e 's/\(i	1	\)Adjektiivi_5F	/\1NOUN_TUHTI	/' \
        -e 's/\(i	1	\)Substantiivi_5G	/\1NOUN_VANKI	/' \
        -e 's/\(it	1	\)Substantiivi_5G	/\1NOUN_TONGIT	/' \
        -e 's/\(i	1	\)Erisnimi_5G	/\1PROPN_VANKI	/' \
        -e 's/\(i	1	\)Substantiivi_5H	/\1NOUN_SOINTI	/' \
        -e 's/\(i	1	\)Substantiivi_5F	/\1NOUN_LEHTI	/' \
        -e 's/\(i	1	\)Erisnimi_5F	/\1PROPN_TAUTI	/' \
        -e 's/\(i	1	\)Substantiivi_5I	/\1NOUN_PELTI	/' \
        -e 's/\(i	1	\)Substantiivi_5J	/\1NOUN_SOINTI	/' \
        -e 's/\(i	1	\)Erisnimi_5J	/\1PROPN_SOINTI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Erisnimi_6	/\1PROPN_KEHVELI	/' \
        -e 's/\([lx]	1	\)Numeraali_5	/\1NUM_GOOGOL	/' \
        -e 's/\(i	1	\)Numeraali_6	/\1NUM_MILJARDI	/' \
        -e 's/\(.*i	1	\)Erisnimi_6	/\1PROPN_KANAALI	/' \
        -e 's/\(.*i	1	\)Adjektiivi_6	/\1ADJ_ABNORMI	/' \
        -e 's/\(.*i	1	\)Substantiivi_6	/\1NOUN_KANAALI	/' \
        -e 's/\([mnlhfkrtpdbgszx]	1	\)Substantiivi_6	/\1NOUN_STADION	/' \
        -e 's/\(a	1	\)Substantiivi_6	/\1NOUN_XXXFAIL	/' \
        -e 's/\([mnlhfkrtpdbgszx]	1	\)Erisnimi_6	/\1PROPN_STADION	/' \
        -e 's/\(.*it	1	\)Substantiivi_6A	/\1NOUN_LOKIT	/' \
        -e 's/\(.*i	1	\)Substantiivi_6A	/\1NOUN_LOKKI	/' \
        -e 's/\(.*i	1	\)Substantiivi_6C	/\1NOUN_KORTTI	/' \
        -e 's/\(.*i	1	\)Substantiivi_6G	/\1NOUN_VANKI	/' \
        -e 's/\(i	1	\)Erisnimi_6C	/\1PROPN_SKEITTI	/' \
        -e 's/\([aou].*i	1	\)Erisnimi_7	/\1PROPN_ONNI	/' \
        -e 's/\(i	1	\)Erisnimi_7	/\1PROPN_KIVI	/' \
        -e 's/\([aou].*i	1	\)Substantiivi_7	/\1NOUN_ONNI	/' \
        -e 's/\(i	1	\)Substantiivi_7	/\1NOUN_KIVI	/' \
        -e 's/\(et	1	\)Substantiivi_7	/\1NOUN_SAKSET	/' \
        -e 's/\(a	1	\)Substantiivi_7	/\1NOUN_KIRJA	/' \
        -e 's/\(et	1	\)Substantiivi_7B	/\1NOUN_HAPET	/' \
        -e 's/\(i	1	\)Substantiivi_7B	/\1NOUN_HAPPI	/' \
        -e 's/\([äöy].*i	1	\)Erisnimi_7D	/\1PROPN_KÄKI	/' \
        -e 's/\(et	1	\)Substantiivi_7D	/\1NOUN_MÄET	/' \
        -e 's/\(i	1	\)Substantiivi_7D	/\1NOUN_NOKI	/' \
        -e 's/\(i	1	\)Erisnimi_7D	/\1PROPN_NOKI	/' \
        -e 's/\(i	1	\)Substantiivi_7E	/\1NOUN_KORPI	/' \
        -e 's/\(i	1	\)Erisnimi_7E	/\1PROPN_KORPI	/' \
        -e 's/\(et	1	\)Substantiivi_7F	/\1NOUN_TÄHDET	/' \
        -e 's/\(i	1	\)Substantiivi_7F	/\1NOUN_LEHTI	/' \
        -e 's/\(i	1	\)Erisnimi_7F	/\1PROPN_LEHTI	/' \
        -e 's/\(e	1	\)Numeraali_7	/\1NUM_KOLME	/' \
        -e 's/\(i	1	\)Substantiivi_7G	/\1NOUN_ONKI	/' \
        -e 's/\(i	1	\)Substantiivi_7H	/\1NOUN_RIMPI	/' \
        -e 's/\(i	1	\)Erisnimi_7H	/\1PROPN_SAMPI	/' \
        -e 's/\(i	1	\)Substantiivi_7J	/\1NOUN_SOINTI	/' \
        -e 's/\(i	1	\)Substantiivi_7L	/\1NOUN_ARKI	/' \
        -e 's/\(i	1	\)Erisnimi_7L	/\1PROPN_ARKI	/' \
        -e 's/\(e	1	\)Erisnimi_8	/\1PROPN_NALLE	/' \
        -e 's/\(e	1	\)Erisnimi_6	/\1PROPN_NALLE	/' \
        -e 's/\(e	1	\)Substantiivi_2	/\1NOUN_NALLE	/' \
        -e 's/\(e	1	\)Adjektiivi_8	/\1ADJ_TERVE	/' \
        -e 's/\(e	1	\)Substantiivi_8	/\1NOUN_NALLE	/' \
        -e 's/\(e	1	\)Substantiivi_8A	/\1NOUN_HIKKE	/' \
        -e 's/\(e	1	\)Erisnimi_8A	/\1PROPN_EKKE	/' \
        -e 's/\(e	1	\)Substantiivi_8B	/\1NOUN_JEPPE	/' \
        -e 's/\(e	1	\)Substantiivi_8C	/\1NOUN_RINGETTE	/' \
        -e 's/\(a	1	\)Adjektiivi_9	/\1NOUN_AAVA	/' \
        -e 's/\(a	1	\)Substantiivi_9	/\1NOUN_KIRJA	/' \
        -e 's/\(ä	1	\)Substantiivi_9	/\1NOUN_HÖPÖTTÄJÄ	/' \
        -e 's/\(at	1	\)Substantiivi_9	/\1NOUN_VARAT	/' \
        -e 's/\(e	1	\)Substantiivi_9	/\1NOUN_XXXFAIL	/' \
        -e 's/\(ä	1	\)Substantiivi_9	/\1NOUN_HÖPÖTTÄJÄ	/' \
        -e 's/\(a	1	\)Adjektiivi_9A	/\1ADJ_TARKKA	/' \
        -e 's/\(at	1	\)Substantiivi_9A	/\1NOUN_SUKAT	/' \
        -e 's/\(a	1	\)Substantiivi_9A	/\1NOUN_POLITIIKKA	/' \
        -e 's/\(a	1	\)Pronomini_9	/\1PRON_SAMA	/' \
        -e 's/\(a	1	\)Erisnimi_9	/\1PROPN_KIRJA	/' \
        -e 's/\(a	1	\)Erisnimi_9A	/\1PROPN_POLITIIKKA	/' \
        -e 's/\(a	1	\)Substantiivi_9B	/\1NOUN_TIPPA	/' \
        -e 's/\(a	1	\)Substantiivi_9C	/\1NOUN_MITTA	/' \
        -e 's/\(a	1	\)Erisnimi_9C	/\1PROPN_MITTA	/' \
        -e 's/\(at	1	\)Substantiivi_9D	/\1NOUN_PAIKAT	/' \
        -e 's/\(a	1	\)Substantiivi_9D	/\1NOUN_VIKA	/' \
        -e 's/\(a	1	\)Erisnimi_9D	/\1PROPN_VIKA	/' \
        -e 's/\(a	1	\)Substantiivi_9E	/\1NOUN_SALPA	/' \
        -e 's/\(a	1	\)Adjektiivi_9F	/\1ADJ_EHTA	/' \
        -e 's/\(a	1	\)Substantiivi_9F	/\1NOUN_PATA	/' \
        -e 's/\(at	1	\)Substantiivi_9F	/\1NOUN_RAUDAT	/' \
        -e 's/\(a	1	\)Erisnimi_9F	/\1PROPN_PATA	/' \
        -e 's/\(a	1	\)Substantiivi_9G	/\1NOUN_LANKA	/' \
        -e 's/\(at	1	\)Substantiivi_9G	/\1NOUN_VARAT	/' \
        -e 's/\(a	1	\)Substantiivi_9H	/\1NOUN_RAMPA	/' \
        -e 's/\(a	1	\)Substantiivi_9I	/\1NOUN_VALTA	/' \
        -e 's/\(a	1	\)Erisnimi_9I	/\1PROPN_VALTA	/' \
        -e 's/\(a	1	\)Adjektiivi_9J	/\1ADJ_VIHANTA	/' \
        -e 's/\(at	1	\)Substantiivi_9J	/\1NOUN_RANNAT	/' \
        -e 's/\(a	1	\)Substantiivi_9J	/\1NOUN_KUTSUNTA	/' \
        -e 's/\(ä	1	\)Substantiivi_9J	/\1NOUN_KYSYNTÄ	/' \
        -e 's/\(a	1	\)Erisnimi_9J	/\1PROPN_KUTSUNTA	/' \
        -e 's/\(a	1	\)Substantiivi_9K	/\1NOUN_KERTA	/' \
        -e 's/\(a	1	\)Erisnimi_9K	/\1PROPN_KERTA	/' \
        -e 's/\(a	1	\)Adjektiivi_9L	/\1ADJ_ARKA	/' \
        -e 's/\(a	1	\)Adjektiivi_10	/\1ADJ_RUMA	/' \
        -e 's/\(ä	1	\)Adjektiivi_10	/\1ADJ_TYHMÄ	/' \
        -e 's/\(ä	1	\)Adjektiivi_10E	/\1ADJ_KÄYPÄ	/' \
        -e 's/\(a	1	\)Substantiivi_10	/\1NOUN_VOIMA	/' \
        -e 's/\(at	1	\)Substantiivi_10	/\1NOUN_JUHLAT	/' \
        -e 's/\(a	1	\)Erisnimi_10	/\1PROPN_VOIMA	/' \
        -e 's/\(a	1	\)Verbi_10	/\1NOUN_VOIMA	/' \
        -e 's/\(ä	1	\)Erisnimi_10	/\1PROPN_HÖPÖTTÄJÄ	/' \
        -e 's/\(ä	1	\)Substantiivi_10	/\1NOUN_HÖPÖTTÄJÄ	/' \
        -e 's/\(ät	1	\)Substantiivi_10	/\1NOUN_KÄRÄJÄT	/' \
        -e 's/\(a	1	\)Numeraali_10	/\1NUM_MILJOONA	/' \
        -e 's/\(än	1	\)Numeraali_10	/\1NUM_YHDEKSÄN	/' \
        -e 's/\(ä	1	\)Erisnimi_10	/\1PROPN_HÖPÖTTÄJÄ	/' \
        -e 's/\(a	1	\)Adjektiivi_10A	/\1ADJ_TARKKA	/' \
        -e 's/\(ä	1	\)Adjektiivi_10A	/\1ADJ_MYKKÄ	/' \
        -e 's/\(at	1	\)Substantiivi_10A	/\1NOUN_SUKAT	/' \
        -e 's/\(a	1	\)Substantiivi_10A	/\1NOUN_KUKKA	/' \
        -e 's/\(ä	1	\)Substantiivi_10A	/\1NOUN_HÖLKKÄ	/' \
        -e 's/\(a	1	\)Erisnimi_10A	/\1PROPN_KUKKA	/' \
        -e 's/\(ä	1	\)Erisnimi_10A	/\1PROPN_HÖLKKÄ	/' \
        -e 's/\(a	1	\)Adjektiivi_10B	/\1ADJ_POPPA	/' \
        -e 's/\(a	1	\)Substantiivi_10B	/\1NOUN_KUOPPA	/' \
        -e 's/\(ä	1	\)Substantiivi_10B	/\1NOUN_SEPPÄ	/' \
        -e 's/\(ä	1	\)Erisnimi_10B	/\1PROPN_SEPPÄ	/' \
        -e 's/\(a	1	\)Erisnimi_10B	/\1PROPN_KUOPPA	/' \
        -e 's/\(at	1	\)Substantiivi_10C	/\1NOUN_RIUTAT	/' \
        -e 's/\(a	1	\)Substantiivi_10C	/\1NOUN_MITTA	/' \
        -e 's/\(ä	1	\)Substantiivi_10C	/\1NOUN_KENTTÄ	/' \
        -e 's/\(ä	1	\)Erisnimi_10C	/\1PROPN_KENTTÄ	/' \
        -e 's/\([Pp]oika	1	\)Substantiivi_10D	/\1NOUN_POIKA	/' \
        -e 's/\([Pp]oika	1	\)Erisnimi_10D	/\1PROPN_POIKA	/' \
        -e 's/\(ä	1	\)Adjektiivi_10D	/\1ADJ_MÄRKÄ	/' \
        -e 's/\(a	1	\)Substantiivi_10D	/\1NOUN_RUOKA	/' \
        -e 's/\(ä	1	\)Substantiivi_10D	/\1NOUN_NÄLKÄ	/' \
        -e 's/\(ä	1	\)Erisnimi_10D	/\1PROPN_NÄLKÄ	/' \
        -e 's/\(a	1	\)Adjektiivi_10E	/\1ADJ_VOIPA	/' \
        -e 's/\(at	1	\)Substantiivi_10E	/\1NOUN_TURVAT	/' \
        -e 's/\(a	1	\)Substantiivi_10E	/\1NOUN_LUPA	/' \
        -e 's/\(ä	1	\)Substantiivi_10E	/\1NOUN_LEIPÄ	/' \
        -e 's/\(a	1	\)Erisnimi_10E	/\1PROPN_LUPA	/' \
        -e 's/\(ä	1	\)Adjektiivi_10F	/\1ADJ_MÄTÄ	/' \
        -e 's/\(a	1	\)Substantiivi_10F	/\1NOUN_SOTA	/' \
        -e 's/\(ä	1	\)Substantiivi_10F	/\1NOUN_PÖYTÄ	/' \
        -e 's/\(a	1	\)Substantiivi_10G	/\1NOUN_HONKA	/' \
        -e 's/\(ä	1	\)Substantiivi_10G	/\1NOUN_KENKÄ	/' \
        -e 's/\(ät	1	\)Substantiivi_10G	/\1NOUN_KENGÄT	/' \
        -e 's/\(a	1	\)Erisnimi_10F	/\1PROPN_SOTA	/' \
        -e 's/\(a	1	\)Erisnimi_10G	/\1PROPN_HONKA	/' \
        -e 's/\(ä	1	\)Erisnimi_10G	/\1PROPN_KENKÄ	/' \
        -e 's/\(a	1	\)Substantiivi_10H	/\1NOUN_RAMPA	/' \
        -e 's/\(a	1	\)Substantiivi_10I	/\1NOUN_MULTA	/' \
        -e 's/\(ä	1	\)Adjektiivi_10J	/\1ADJ_LÄNTÄ	/' \
        -e 's/\(a	1	\)Substantiivi_10J	/\1NOUN_KUNTA	/' \
        -e 's/\(ä	1	\)Substantiivi_10J	/\1NOUN_HÄNTÄ	/' \
        -e 's/\(a	1	\)Erisnimi_10J	/\1PROPN_KUNTA	/' \
        -e 's/\(a	1	\)Adjektiivi_10J	/\1ADJ_VIHANTA	/' \
        -e 's/\(a	1	\)Substantiivi_10L	/\1NOUN_OLKA	/' \
        -e 's/\(ä	1	\)Substantiivi_10L	/\1NOUN_NÄLKÄ	/' \
        -e 's/\(a	1	\)Adjektiivi_11	/\1ADJ_AAVA	/' \
        -e 's/\(ä	1	\)Adjektiivi_11	/\1ADJ_SÄKKÄRÄ	/' \
        -e 's/\(a	1	\)Substantiivi_5	/\1NOUN_MAKKARA	/' \
        -e 's/\(a	1	\)Substantiivi_11	/\1NOUN_MAKKARA	/' \
        -e 's/\(ä	1	\)Substantiivi_11	/\1NOUN_KÄPÄLÄ	/' \
        -e 's/\(at	1	\)Substantiivi_11	/\1NOUN_MARKKINAT	/' \
        -e 's/\(a	1	\)Erisnimi_11	/\1PROPN_MAKKARA	/' \
        -e 's/\(ä	1	\)Erisnimi_11	/\1PROPN_HÄKKYRÄ	/' \
        -e 's/\(a	1	\)Substantiivi_11A	/\1NOUN_LUSIKKA	/' \
        -e 's/\(a	1	\)Substantiivi_11F	/\1NOUN_SOTA	/' \
        -e 's/\(a	1	\)Adjektiivi_12	/\1ADJ_HARMAJA	/' \
        -e 's/\(ä	1	\)Adjektiivi_12	/\1ADJ_VIHERIÄ	/' \
        -e 's/\(ät	1	\)Substantiivi_12	/\1NOUN_KÄRÄJÄT	/' \
        -e 's/\(a	1	\)Substantiivi_12	/\1NOUN_KITARA	/' \
        -e 's/\(ä	1	\)Substantiivi_12	/\1NOUN_HÄKKYRÄ	/' \
        -e 's/\(at	1	\)Substantiivi_12	/\1NOUN_VARAT	/' \
        -e 's/\(a	1	\)Erisnimi_12	/\1PROPN_KITARA	/' \
        -e 's/\(ä	1	\)Erisnimi_12	/\1PROPN_HÄKKYRÄ	/' \
        -e 's/\(at	1	\)Substantiivi_13	/\1NOUN_JUHLAT	/' \
        -e 's/\(a	1	\)Substantiivi_13	/\1NOUN_KIRJA	/' \
        -e 's/\(ä	1	\)Substantiivi_13	/\1NOUN_SIIVILÄ	/' \
        -e 's/\(a	1	\)Adjektiivi_13	/\1NOUN_MATALA	/' \
        -e 's/\(a	1	\)Erisnimi_13	/\1PROPN_KIRJA	/' \
        -e 's/\(a	1	\)Erisnimi_14	/\1PROPN_LUSIKKA	/' \
        -e 's/\(a	1	\)Adjektiivi_14A	/\1NOUN_HAILAKKA	/' \
        -e 's/\(a	1	\)Substantiivi_14	/\1NOUN_LUSIKKA	/' \
        -e 's/\(ä	1	\)Substantiivi_14	/\1NOUN_KÄMMEKKÄ	/' \
        -e 's/\(at	1	\)Substantiivi_14A	/\1NOUN_PAIKAT	/' \
        -e 's/\(a	1	\)Substantiivi_14A	/\1NOUN_LUSIKKA	/' \
        -e 's/\(ät	1	\)Substantiivi_14A	/\1NOUN_SÄRKÄT	/' \
        -e 's/\(ä	1	\)Substantiivi_14A	/\1NOUN_KÄMMEKKÄ	/' \
        -e 's/\(a	1	\)Verbi_14A	/\1NOUN_LUSIKKA	/' \
        -e 's/\(ä	1	\)Adjektiivi_14A	/\1ADJ_MYKKÄ	/' \
        -e 's/\(a	1	\)Erisnimi_14	/\1PROPN_LUSIKKA	/' \
        -e 's/\(a	1	\)Erisnimi_14A	/\1PROPN_LUSIKKA	/' \
        -e 's/\(ä	1	\)Erisnimi_14A	/\1PROPN_HÖLKKÄ	/' \
        -e 's/\(a	1	\)Substantiivi_14B	/\1NOUN_ULAPPA	/' \
        -e 's/\(a	1	\)Substantiivi_14C	/\1NOUN_MITTA	/' \
        -e 's/\(a	1	\)Erisnimi_14C	/\1PROPN_MITTA	/' \
        -e 's/\(a	1	\)Substantiivi_14G	/\1NOUN_HONKA	/' \
        -e 's/\(a	1	\)Substantiivi_15	/\1NOUN_SOKEA	/' \
        -e 's/\(ä	1	\)Substantiivi_15	/\1NOUN_LIPEÄ	/' \
        -e 's/\(ä	1	\)Adjektiivi_15	/\1ADJ_JÄREÄ	/' \
        -e 's/\(a	1	\)Adjektiivi_15	/\1ADJ_KORKEA	/' \
        -e 's/\(a	1	\)Pronomini_15	/\1PRON_USEA	/' \
        -e 's/\(i	1	\)Adjektiivi_16H	/\1ADJ_AIEMPI	/' \
        -e 's/\(at	1	\)Substantiivi_16	/\1NOUN_VANHEMMAT	/' \
        -e 's/\(i	1	\)Substantiivi_16	/\1NOUN_VANHEMPI	/' \
        -e 's/\(i	1	\)Substantiivi_16H	/\1NOUN_VANHEMPI	/' \
        -e 's/\(i	1	\)Pronomini_16	/\1PRON_KUMPI	/' \
        -e 's/\(ikin	1	\)Pronomini_16	/\1PRON_KUMPIKIN	/' \
        -e 's/\(a	1	\)Adjektiivi_17	/\1ADJ_VAPAA	/' \
        -e 's/\(a	1	\)Substantiivi_17	/\1NOUN_VAINAA	/' \
        -e 's/\(o	1	\)Substantiivi_17	/\1NOUN_TIENOO	/' \
        -e 's/\(e	1	\)Substantiivi_17	/\1NOUN_PATEE	/' \
        -e 's/\(u	1	\)Substantiivi_17	/\1NOUN_LEIKKUU	/' \
        -e 's/\(ö	1	\)Substantiivi_17	/\1NOUN_MILJÖÖ	/' \
        -e 's/\(aa	1	\)Erisnimi_17	/\1PROPN_VAINAA	/' \
        -e 's/\(uu	1	\)Erisnimi_17	/\1PROPN_LEIKKUU	/' \
        -e 's/\(a	1	\)Adjekiivi_18	/\1ADJ_PEEAA	/' \
        -e 's/\(a	1	\)Substantiivi_18	/\1NOUN_MAA	/' \
        -e 's/\(e	1	\)Substantiivi_18	/\1NOUN_TEE	/' \
        -e 's/\(ait	1	\)Substantiivi_18	/\1NOUN_HAIT	/' \
        -e 's/\(i	1	\)Substantiivi_18	/\1NOUN_HAI	/' \
        -e 's/\(ai	1	\)Erisnimi_1	/\1PROPN_HAI	/' \
        -e 's/\(ot	1	\)Substantiivi_18	/\1NOUN_TALKOOT	/' \
        -e 's/\(o	1	\)Substantiivi_18	/\1NOUN_OOKOO	/' \
        -e 's/\(u	1	\)Substantiivi_18	/\1NOUN_PUU	/' \
        -e 's/\(ut	1	\)Substantiivi_18	/\1NOUN_PUUT	/' \
        -e 's/\(y	1	\)Substantiivi_18	/\1NOUN_PYY	/' \
        -e 's/\(ät	1	\)Substantiivi_18	/\1NOUN_PÄÄT	/' \
        -e 's/\(ä	1	\)Substantiivi_18	/\1NOUN_PÄÄ	/' \
        -e 's/\(ö	1	\)Substantiivi_18	/\1NOUN_KÖÖ	/' \
        -e 's/\(nen	1	\)Substantiivi_18	/\1NOUN_XXXFAIL	/' \
        -e 's/\(a	1	\)Erisnimi_18	/\1PROPN_MAA	/' \
        -e 's/\(u	1	\)Erisnimi_18	/\1PROPN_PUU	/' \
        -e 's/\(ai	1	\)Erisnimi_18	/\1PROPN_HAI	/' \
        -e 's/\(ei	1	\)Erisnimi_18	/\1PROPN_HAI	/' \
        -e 's/\(ee	1	\)Erisnimi_18	/\1PROPN_TOKEE	/' \
        -e 's/\(u	1	\)Pronomini_18	/\1PRON_MUU	/' \
        -e 's/\(o	1	\)Erisnimi_18	/\1PROPN_OOKOO	/' \
        -e 's/\(ä	1	\)Erisnimi_18	/\1PROPN_PÄÄ	/' \
        -e 's/\(ie	1	\)Substantiivi_19	/\1NOUN_TIE	/' \
        -e 's/\(uo	1	\)Substantiivi_19	/\1NOUN_VUO	/' \
        -e 's/\(yö	1	\)Substantiivi_19	/\1NOUN_TYÖ	/' \
        -e 's/\(ie	1	\)Erisnimi_19	/\1PROPN_TIE	/' \
        -e 's/\(uo	1	\)Erisnimi_19	/\1PROPN_VUO	/' \
        -e 's/\(a	1	\)Substantiivi_20	/\1NOUN_NUGAA	/' \
        -e 's/\(e	1	\)Substantiivi_20	/\1NOUN_PATEE	/' \
        -e 's/\(o	1	\)Substantiivi_20	/\1NOUN_TRIKOO	/' \
        -e 's/\(u	1	\)Substantiivi_20	/\1NOUN_RAGUU	/' \
        -e 's/\(y	1	\)Substantiivi_20	/\1NOUN_FONDYY	/' \
        -e 's/\(ö	1	\)Substantiivi_20	/\1NOUN_MILJÖÖ	/' \
        -e 's/\(ä	1	\)Erisnimi_20	/\1PROPN_HYVINKÄÄ	/' \
        -e 's/\(	1	\)Substantiivi_21	/\1NOUN_ROSÉ	/' \
        -e 's/\(ie	1	\)Pronomini_21	/\1PRON_MIE	/' \
        -e 's/\(	1	\)Erisnimi_21	/\1PROPN_ROSÉ	/' \
        -e 's/\(w	1	\)Erisnimi_22	/\1PROPN_SHOW	/' \
        -e 's/\(s	1	\)Erisnimi_22	/\1PROPN_BORDEAUX	/' \
        -e 's/\(t	1	\)Substantiivi_22	/\1NOUN_BEIGNET	/' \
        -e 's/\(	1	\)Substantiivi_22	/\1NOUN_SHOW	/' \
        -e 's/\(i	1	\)Substantiivi_23	/\1NOUN_TULI	/' \
        -e 's/\(et	1	\)Substantiivi_24	/\1NOUN_RIPSET	/' \
        -e 's/\(i	1	\)Substantiivi_24	/\1NOUN_RUUHI	/' \
        -e 's/\(i	1	\)Erisnimi_24	/\1PROPN_RUUHI	/' \
        -e 's/\(meri	1	\)Substantiivi_24	/\1NOUN_MERI	/' \
        -e 's/\([aou].*i	1	\)Substantiivi_25	/\1NOUN_TAIMI	/' \
        -e 's/\(i	1	\)Substantiivi_25	/\1NOUN_LIEMI	/' \
        -e 's/\([aou].*i	1	\)Erisnimi_25	/\1PROPN_TAIMI	/' \
        -e 's/\(i	1	\)Erisnimi_25	/\1PROPN_LIEMI	/' \
        -e 's/\(i	1	\)Adjektiivi_26	/\1ADJ_SUURI	/' \
        -e 's/\(et	1	\)Substantiivi_26	/\1NOUN_RIPSET	/' \
        -e 's/\(i	1	\)Substantiivi_26	/\1NOUN_RUUHI	/' \
        -e 's/\(i	1	\)Erisnimi_26	/\1PROPN_RUUHI	/' \
        -e 's/\(et	1	\)Erisnimi_26	/\1PROPN_SAARET	/' \
        -e 's/\(i	1	\)Adjektiivi_27	/\1ADJ_UUSI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Substantiivi_27	/\1NOUN_KÖYSI	/' \
        -e 's/\(i	1	\)Substantiivi_27	/\1NOUN_KAUSI	/' \
        -e 's/\(i	1	\)Substantiivi_27F	/\1NOUN_KAUSI	/' \
        -e 's/\(i	1	\)Erisnimi_27	/\1PROPN_KÖYSI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Substantiivi_28	/\1NOUN_HIRSI	/' \
        -e 's/\(i	1	\)Substantiivi_28	/\1NOUN_VARSI	/' \
        -e 's/\(i	1	\)Substantiivi_28K	/\1NOUN_VARSI	/' \
        -e 's/\(i	1	\)Substantiivi_28I	/\1NOUN_TALSI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Erisnimi_28	/\1PROPN_HIRSI	/' \
        -e 's/\(i	1	\)Erisnimi_28	/\1PROPN_VARSI	/' \
        -e 's/\(i	1	\)Substantiivi_29	/\1NOUN_UKSI	/' \
        -e 's/\(et	1	\)Substantiivi_30	/\1NOUN_SUITSET	/' \
        -e 's/\(i	1	\)Substantiivi_30	/\1NOUN_VEITSI	/' \
        -e 's/\(i	1	\)Substantiivi_31	/\1NOUN_HAAKSI	/' \
        -e 's/\([äöyÄÖY].*[ln]	1	\)Substantiivi_32	/\1NOUN_SIEMEN	/' \
        -e 's/\([lnr]	1	\)Substantiivi_32	/\1NOUN_JOUTSEN	/' \
        -e 's/\(n	1	\)Erisnimi_32	/\1PROPN_SIEMEN	/' \
        -e 's/\(tar	1	\)Substantiivi_32C	/\1NOUN_AJATAR	/' \
        -e 's/\(tär	1	\)Substantiivi_32C	/\1NOUN_TYTÄR	/' \
        -e 's/\(en	1	\)Substantiivi_32D	/\1NOUN_IEN	/' \
        -e 's/\([äöyÄÖY].*n	1	\)Substantiivi_33	/\1NOUN_ELIN	/' \
        -e 's/\(n	1	\)Adjektiivi_33	/\1NOUN_AVOIN	/' \
        -e 's/\(n	1	\)Substantiivi_33	/\1NOUN_PUHELIN	/' \
        -e 's/\([äöyÄÖY].*met	1	\)Substantiivi_33	/\1NOUN_KERITSIMET	/' \
        -e 's/\([aouAOU].*met	1	\)Substantiivi_33	/\1NOUN_ATERIMET	/' \
        -e 's/\(met	1	\)Substantiivi_33	/\1NOUN_KERITSIMET	/' \
        -e 's/\([äöyÄÖY].*n	1	\)Erisnimi_33	/\1PROPN_ELIN	/' \
        -e 's/\(n	1	\)Erisnimi_33	/\1PROPN_PUHELIN	/' \
        -e 's/\(n	1	\)Erisnimi_33A	/\1PROPN_HÄRKIN	/' \
        -e 's/\(n	1	\)Substantiivi_33A	/\1NOUN_HÄRKIN	/' \
        -e 's/\(n	1	\)Substantiivi_33C	/\1NOUN_SUODATIN	/' \
        -e 's/\(met	1	\)Substantiivi_33C	/\1NOUN_HOKSOTTIMET	/' \
        -e 's/\([äöyÄÖY].*n	1	\)Erisnimi_33C	/\1PROPN_HEITIN	/' \
        -e 's/\(n	1	\)Substantiivi_33D	/\1NOUN_PUIN	/' \
        -e 's/\(n	1	\)Substantiivi_33E	/\1NOUN_RAAVIN	/' \
        -e 's/\(n	1	\)Substantiivi_33F	/\1NOUN_JOHDIN	/' \
        -e 's/\(n	1	\)Substantiivi_33I	/\1NOUN_ASKELLIN	/' \
        -e 's/\(n	1	\)Substantiivi_33K	/\1NOUN_KIHARRIN	/' \
        -e 's/\(n	1	\)Substantiivi_33L	/\1NOUN_POLJIN	/' \
        -e 's/\([äöyÄÖY]*n	1	\)Substantiivi_33J	/\1NOUN_KÄÄNNIN	/' \
        -e 's/\(n	1	\)Substantiivi_33J	/\1NOUN_MUUNNIN	/' \
        -e 's/\(ton	1	\)Substantiivi_34	/\1NOUN_ALASTON	/' \
        -e 's/\(ton	1	\)Substantiivi_34C	/\1NOUN_OSATON	/' \
        -e 's/\(tön	1	\)Substantiivi_34C	/\1NOUN_NIMETÖN	/' \
        -e 's/\(nen	1	\)Substantiivi_34	/\1NOUN_XXXFAIL	/' \
        -e 's/\(tön	1	\)Adjektiivi_34	/\1ADJ_KYVYTÖN	/' \
        -e 's/\(ton	1	\)Adjektiivi_34	/\1ADJ_VIATON	/' \
        -e 's/\(tön	1	\)Adjektiivi_34C	/\1ADJ_KYVYTÖN	/' \
        -e 's/\(ton	1	\)Adjektiivi_34C	/\1ADJ_VIATON	/' \
        -e 's/\(ton	1	\)Verbi_34C	/\1ADJ_VIATON	/' \
        -e 's/\(tön	1	\)Verbi_34C	/\1ADJ_KYVYTÖN	/' \
        -e 's/\(n	1	\)Adjektiivi_33B	/\1ADJ_HAPAN	/' \
        -e 's/\(n	1	\)Substantiivi_35H	/\1NOUN_LÄMMIN	/' \
        -e 's/\(n	1	\)Substantiivi_36	/\1NOUN_LÄHIN	/' \
        -e 's/\(n	1	\)Adjektiivi_36	/\1ADJ_SISIN	/' \
        -e 's/\([aou].*nen	1	\)Erisnimi_38	/\1PROPN_AAKKOSTAMINEN	/' \
        -e 's/\([äöyÄÖY].*nen	1	\)Erisnimi_38	/\1PROPN_KYLKIÄINEN	/' \
        -e 's/\([äöyÄÖY].*nen	1	\)Substantiivi_38	/\1NOUN_KYLKIÄINEN	/' \
        -e 's/\([äöyÄÖY].*nen	1	\)Verbi_38	/\1NOUN_KYLKIÄINEN	/' \
        -e 's/\([aouAOU].*nen	1	\)Verbi_38	/\1NOUN_AAKKOSTAMINEN	/' \
        -e 's/\(nen	1	\)Substantiivi_38	/\1NOUN_AAKKOSTAMINEN	/' \
        -e 's/\(set	1	\)Substantiivi_38	/\1NOUN_RAPPUSET	/' \
        -e 's/\(nen	1	\)Pronomini_38	/\1PRON_JOKAINEN	/' \
        -e 's/\(nen	1	\)Erisnimi_38	/\1PROPN_AAKKOSTAMINEN	/' \
        -e 's/\(nen	1	\)Adjektiivi_38	/\1ADJ_AAKKOSELLINEN	/' \
        -e 's/\(nen	1	\)Adjektiivi_18	/\1ADJ_AAKKOSELLINEN	/' \
        -e 's/\(tty	1	\)Adjektiivi_38	/\1ADJ_YLENNETTY	/' \
        -e 's/\(s	1	\)Numeraali_38	/\1NUM_NELJÄS	/' \
        -e 's/\([AOUaou].*s	1	\)Substantiivi_38	/\1NOUN_VAKUUTUS	/' \
        -e 's/\([ÄÖYäöy].*s	1	\)Substantiivi_38	/\1NOUN_RÄJÄYTYS	/' \
        -e 's/\(s	1	\)Substantiivi_38	/\1NOUN_RÄJÄYTYS	/' \
        -e 's/\(s	1	\)Erisnimi_39	/\1PROPN_VAKUUTUS	/' \
        -e 's/\(s	1	\)Adjektiivi_39	/\1ADJ_SYMPPIS	/' \
        -e 's/\(s	1	\)Substantiivi_39	/\1NOUN_VAKUUTUS	/' \
        -e 's/\(s	1	\)Substantiivi_39F	/\1NOUN_VAKUUTUS	/' \
        -e 's/\(s	1	\)Verbi_39	/\1NOUN_VAKUUTUS	/' \
        -e 's/\(kset	1	\)Substantiivi_39	/\1NOUN_SERKUKSET	/' \
        -e 's/\(a	1	\)Substantiivi_40	/\1NOUN_XXXFAIL	/' \
        -e 's/\(us	1	\)Substantiivi_40	/\1NOUN_AAKKOSELLISUUS	/' \
        -e 's/\(us	1	\)Substantiivi_40A	/\1NOUN_AAKKOSELLISUUS	/' \
        -e 's/\(ys	1	\)Substantiivi_40	/\1NOUN_KÖYHYYS	/' \
        -e 's/\(us	1	\)Erisnimi_40	/\1PROPN_AAKKOSELLISUUS	/' \
        -e 's/\(as	1	\)Adjektiivi_41	/\1ADJ_AUTUAS	/' \
        -e 's/\(is	1	\)Adjektiivi_41	/\1ADJ_VALMIS	/' \
        -e 's/\(käs	1	\)Adjektiivi_41	/\1ADJ_TYYLIKÄS	/' \
        -e 's/\(us	1	\)Substantiivi_41	/\1NOUN_KIIRUS	/' \
        -e 's/\(os	1	\)Substantiivi_41	/\1NOUN_UROS	/' \
        -e 's/\(as	1	\)Substantiivi_41	/\1NOUN_PATSAS	/' \
        -e 's/\(is	1	\)Substantiivi_41	/\1NOUN_RUUMIS	/' \
        -e 's/\(es	1	\)Substantiivi_41	/\1NOUN_KIRVES	/' \
        -e 's/\(äs	1	\)Substantiivi_41	/\1NOUN_ÄYRÄS	/' \
        -e 's/\(aat	1	\)Substantiivi_41	/\1NOUN_VALJAAT	/' \
        -e 's/\(as	1	\)Erisnimi_41	/\1PROPN_PATSAS	/' \
        -e 's/\(es	1	\)Erisnimi_41	/\1PROPN_ARISTOTELES	/' \
        -e 's/\(is	1	\)Erisnimi_41	/\1PROPN_RUUMIS	/' \
        -e 's/\(äs	1	\)Erisnimi_41	/\1PROPN_ÄYRÄS	/' \
        -e 's/\(as	1	\)Adjektiivi_41A	/\1ADJ_VOIMAKAS	/' \
        -e 's/\(äs	1	\)Adjektiivi_41A	/\1ADJ_TYYLIKÄS	/' \
        -e 's/\(äät	1	\)Substantiivi_41A	/\1NOUN_KILPIKKÄÄT	/' \
        -e 's/\(as	1	\)Substantiivi_41A	/\1NOUN_ASUKAS	/' \
        -e 's/\(äs	1	\)Substantiivi_41A	/\1NOUN_KÄRSÄKÄS	/' \
        -e 's/\(as	1	\)Erisnimi_41A	/\1PROPN_ASUKAS	/' \
        -e 's/\(as	1	\)Substantiivi_41B	/\1NOUN_SAAPAS	/' \
        -e 's/\(äs	1	\)Substantiivi_41B	/\1NOUN_RYPÄS	/' \
        -e 's/\(aat	1	\)Substantiivi_41C	/\1NOUN_RATTAAT	/' \
        -e 's/\(as	1	\)Substantiivi_41C	/\1NOUN_RATAS	/' \
        -e 's/\(us	1	\)Substantiivi_41C	/\1NOUN_VANTUS	/' \
        -e 's/\(as	1	\)Erisnimi_41C	/\1PROPN_RATAS	/' \
        -e 's/\(is	1	\)Erisnimi_41C	/\1PROPN_ALTIS	/' \
        -e 's/\(as	1	\)Substantiivi_41D	/\1NOUN_VARAS	/' \
        -e 's/\(es	1	\)Substantiivi_41D	/\1NOUN_IES	/' \
        -e 's/\(is	1	\)Substantiivi_41D	/\1NOUN_RUIS	/' \
        -e 's/\(äs	1	\)Substantiivi_41D	/\1NOUN_KÄRSÄKÄS	/' \
        -e 's/\(as	1	\)Adjektiivi_41F	/\1ADJ_HIDAS	/' \
        -e 's/\(as	1	\)Substantiivi_41E	/\1NOUN_VARVAS	/' \
        -e 's/\(äs	1	\)Substantiivi_41E	/\1NOUN_SEIVÄS	/' \
        -e 's/\(as	1	\)Substantiivi_41F	/\1NOUN_TEHDAS	/' \
        -e 's/\(aat	1	\)Substantiivi_41G	/\1NOUN_KANKAAT	/' \
        -e 's/\(as	1	\)Substantiivi_41G	/\1NOUN_KANGAS	/' \
        -e 's/\(äs	1	\)Substantiivi_41G	/\1NOUN_KÖNGÄS	/' \
        -e 's/\(äs	1	\)Erisnimi_41G	/\1PROPN_KÖNGÄS	/' \
        -e 's/\(as	1	\)Erisnimi_41G	/\1PROPN_KANGAS	/' \
        -e 's/\(at	1	\)Substantiivi_41H	/\1NOUN_ROMPAAT	/' \
        -e 's/\(as	1	\)Substantiivi_41H	/\1NOUN_HAMMAS	/' \
        -e 's/\(as	1	\)Substantiivi_41I	/\1NOUN_ALLAS	/' \
        -e 's/\(äät	1	\)Substantiivi_41J	/\1NOUN_RYNTÄÄT	/' \
        -e 's/\(as	1	\)Substantiivi_41J	/\1NOUN_KINNAS	/' \
        -e 's/\(äs	1	\)Substantiivi_41J	/\1NOUN_RYNNÄS	/' \
        -e 's/\(as	1	\)Substantiivi_41K	/\1NOUN_PORRAS	/' \
        -e 's/\(at	1	\)Substantiivi_41K	/\1NOUN_PORTAAT	/' \
        -e 's/\(as	1	\)Erisnimi_41K	/\1PROPN_PORRAS	/' \
        -e 's/\(es	1	\)Substantiivi_42	/\1NOUN_MIES	/' \
        -e 's/\(es	1	\)Erisnimi_42	/\1PROPN_MIES	/' \
        -e 's/\(yt	1	\)Adjektiivi_43	/\1ADJ_EHYT	/' \
        -e 's/\(ut	1	\)Adjektiivi_43	/\1ADJ_OHUT	/' \
        -e 's/\(ut	1	\)Substantiivi_43	/\1NOUN_OLUT	/' \
        -e 's/\(yt	1	\)Substantiivi_43	/\1NOUN_IMMYT	/' \
        -e 's/\(yt	1	\)Substantiivi_43H	/\1NOUN_IMMYT	/' \
        -e 's/\(ät	1	\)Substantiivi_44	/\1NOUN_KEVÄT	/' \
        -e 's/\(et	1	\)Erisnimi_44	/\1PROPN_HÄMET	/' \
        -e 's/\(et	1	\)Erisnimi_44C	/\1PROPN_KORTET	/' \
        -e 's/\(et	1	\)Erisnimi_44F	/\1PROPN_AHDET	/' \
        -e 's/\(et	1	\)Erisnimi_44K	/\1PROPN_VIIRRET	/' \
        -e 's/\(et	1	\)Erisnimi_44I	/\1PROPN_VUOLLET	/' \
        -e 's/\(et	1	\)Erisnimi_44J	/\1PROPN_RINNET	/' \
        -e 's/\(as	1	\)Numeraali_45	/\1ADJ_KOLMAS	/' \
        -e 's/\(äs	1	\)Numeraali_45	/\1ADJ_NELJÄS	/' \
        -e 's/\(at	1	\)Substantiivi_46	/\1NOUN_VUOSITUHAT	/' \
        -e 's/\(at	1	\)Substantiivi_47	/\1NOUN_VUOSITUHAT	/' \
        -e 's/\(ut	1	\)Substantiivi_47	/\1NOUN_AIVOKUOLLUT	/' \
        -e 's/\(yt	1	\)Substantiivi_47	/\1NOUN_SIVISTYNYT	/' \
        -e 's/\(ut	1	\)Adjektiivi_47	/\1ADJ_KULUNUT	/' \
        -e 's/\(yt	1	\)Adjektiivi_47	/\1ADJ_ÄLLISTYNYT	/' \
        -e 's/\(et	1	\)Substantiivi_48	/\1NOUN_HIUTALEET	/' \
        -e 's/\(i	1	\)Substantiivi_48	/\1NOUN_ORI	/' \
        -e 's/\(e	1	\)Substantiivi_48	/\1NOUN_ASTE	/' \
        -e 's/\(e	1	\)Adjektiivi_48	/\1ADJ_TERVE	/' \
        -e 's/\(e	1	\)Erisnimi_48	/\1PROPN_ASTE	/' \
        -e 's/\(eet	1	\)Substantiivi_48A	/\1NOUN_SILMÄKKEET	/' \
        -e 's/\(e	1	\)Substantiivi_48A	/\1NOUN_LÄÄKE	/' \
        -e 's/\(e	1	\)Erisnimi_48A	/\1PROPN_LÄÄKE	/' \
        -e 's/\(e	1	\)Substantiivi_48B	/\1NOUN_APE	/' \
        -e 's/\(e	1	\)Substantiivi_48C	/\1NOUN_OSOITE	/' \
        -e 's/\(e	1	\)Substantiivi_48D	/\1NOUN_KOE	/' \
        -e 's/\(eet	1	\)Substantiivi_48E	/\1NOUN_TARPEET	/' \
        -e 's/\(e	1	\)Substantiivi_48E	/\1NOUN_TARVE	/' \
        -e 's/\([aou].*e	1	\)Substantiivi_48F	/\1NOUN_LUODE	/' \
        -e 's/\(e	1	\)Substantiivi_48F	/\1NOUN_KIDE	/' \
        -e 's/\(e	1	\)Substantiivi_48G	/\1NOUN_UNGE	/' \
        -e 's/\(et	1	\)Substantiivi_48F	/\1NOUN_SUHTEET	/' \
        -e 's/\(e	1	\)Substantiivi_48H	/\1NOUN_LUMME	/' \
        -e 's/\([aou].*e	1	\)Erisnimi_48F	/\1PROPN_LUODE	/' \
        -e 's/\(e	1	\)Erisnimi_48F	/\1PROPN_KIDE	/' \
        -e 's/\(e	1	\)Erisnimi_48H	/\1PROPN_LUMME	/' \
        -e 's/\([äöyÄÖY].*e	1	\)Substantiivi_48I	/\1NOUN_MIELLE	/' \
        -e 's/\(e	1	\)Substantiivi_48I	/\1NOUN_MIELLE	/' \
        -e 's/\([äöyÄÖY].*e	1	\)Substantiivi_48J	/\1NOUN_KIINNE	/' \
        -e 's/\([äöyÄÖY].*e	1	\)Substantiivi_48K	/\1NOUN_KIERRE	/' \
        -e 's/\(.*e	1	\)Substantiivi_48K	/\1NOUN_KIERRE	/' \
        -e 's/\(e	1	\)Substantiivi_48J	/\1NOUN_RAKENNE	/' \
        -e 's/\(e	1	\)Erisnimi_48J	/\1PROPN_RAKENNE	/' \
        -e 's/\([aou].*e	1	\)Substantiivi_48K	/\1NOUN_AARRE	/' \
        -e 's/\([aou].*e	1	\)Erisnimi_48K	/\1PROPN_AARRE	/' \
        -e 's/\(e	1	\)Erisnimi_48K	/\1PROPN_KIERRE	/' \
        -e 's/\(e	1	\)Substantiivi_48L	/\1NOUN_HYLJE	/' \
        -e 's/\(e	1	\)Erisnimi_49	/\1PROPN_ASTE	/' \
        -e 's/\(e	1	\)Substantiivi_49	/\1NOUN_ASTE	/' \
        -e 's/\(e	1	\)Substantiivi_49E	/\1NOUN_ASTE	/' \
        -e 's/\(e	1	\)Substantiivi_49.	/\1NOUN_ASTE	/' \
        -e 's/\(l	1	\)Substantiivi_49	/\1NOUN_SIEMEN	/' \
        -e 's/\(r	1	\)Substantiivi_49	/\1NOUN_SIEMEN	/' \
        -e 's/\(n	1	\)Substantiivi_49	/\1NOUN_SIEMEN	/' \
        -e 's/\(n	1	\)Substantiivi_49D	/\1NOUN_SÄEN	/' \
        -e 's/\(l	1	\)Substantiivi_49E	/\1NOUN_TAIVAL	/' \
        -e 's/\(n	1	\)Substantiivi_49E	/\1NOUN_HEVEN	/' \
        -e 's/\(r	1	\)Substantiivi_49E	/\1NOUN_ÄVÄR	/' \
        -e 's/\(r	1	\)Substantiivi_49F	/\1NOUN_UDAR	/' \
        -e 's/\(r	1	\)Substantiivi_49G	/\1NOUN_PENGER	/' \
        -e 's/\(l	1	\)Substantiivi_49H	/\1NOUN_VEMMEL	/' \
        -e 's/\(l	1	\)Substantiivi_49J	/\1NOUN_KANNEL	/' \
        -e 's/\(r	1	\)Substantiivi_49J	/\1NOUN_MANNER	/' \
        -e 's/\(l	1	\)Erisnimi_49E	/\1PROPN_TAIVAL	/' \
        -e 's/\(.	1	\)Substantiivi_50	/\1NOUN_50XXX	/' \
        -e 's/\(.	1	\)Substantiivi_51	/\1NOUN_51XXX	/' \
        -e 's/\(.	1	\)Substantiivi_51.	/\1NOUN_51XXX	/' \
        -e 's/\(.	1	\)Numeraali_51	/\1NUM_51XXX	/' \
        -e 's/\(.	1	\)Pronomini_51	/\1PRON_51XXX	/' \
        -e 's/\(.	1	\)Erisnimi_51	/\1PROPN_51XXX	/' |\
    $SED -e 's/\(a	1	\)Verbi_53	/\1VERB_KASVAA	/' \
        -e 's/\(a	1	\)Verbi_52	/\1VERB_KAUNISTUA	/' \
        -e 's/\(ä	1	\)Verbi_52	/\1VERB_ÄLLISTYÄ	/' \
        -e 's/\(a	1	\)Verbi_52A	/\1VERB_HAUKKOA	/' \
        -e 's/\(ä	1	\)Verbi_52A	/\1VERB_KÄRKKYÄ	/' \
        -e 's/\(a	1	\)Verbi_52B	/\1VERB_HARPPOA	/' \
        -e 's/\(ä	1	\)Verbi_52B	/\1VERB_LEPPYÄ	/' \
        -e 's/\(a	1	\)Verbi_52C	/\1VERB_HERMOTTUA	/' \
        -e 's/\(ä	1	\)Verbi_52C	/\1VERB_KIVETTYÄ	/' \
        -e 's/\(a	1	\)Verbi_52D	/\1VERB_TAKOA	/' \
        -e 's/\(ä	1	\)Verbi_52D	/\1VERB_MÄIKYÄ	/' \
        -e 's/\(a	1	\)Verbi_52E	/\1VERB_SILPOA	/' \
        -e 's/\(ä	1	\)Verbi_52E	/\1VERB_SYÖPYÄ	/' \
        -e 's/\(a	1	\)Verbi_52F	/\1VERB_ROHTUA	/' \
        -e 's/\(ä	1	\)Verbi_52F	/\1VERB_SILIYTYÄ	/' \
        -e 's/\(a	1	\)Verbi_52G	/\1VERB_HINKUA	/' \
        -e 's/\(a	1	\)Verbi_52H	/\1VERB_AMPUA	/' \
        -e 's/\(a	1	\)Verbi_52I	/\1VERB_HUMALTUA	/' \
        -e 's/\(ä	1	\)Verbi_52I	/\1VERB_MIELTYÄ	/' \
        -e 's/\(a	1	\)Verbi_52J	/\1VERB_VAKAANTUA	/' \
        -e 's/\(ä	1	\)Verbi_52J	/\1VERB_TYHJENTYÄ	/' \
        -e 's/\(a	1	\)Verbi_52K	/\1VERB_HAPERTUA	/' \
        -e 's/\(ä	1	\)Verbi_52K	/\1VERB_HAPERTUA	/' \
        -e 's/\(ä	1	\)Verbi_53	/\1VERB_KIVISTÄÄ	/' \
        -e 's/\(ä	1	\)Verbi_53A	/\1VERB_ÄHKÄÄ	/' \
        -e 's/\(ä	1	\)Verbi_53C	/\1VERB_RÄPSYTTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_53C	/\1VERB_VIEROITTAA	/' \
        -e 's/\(a	1	\)Verbi_53D	/\1VERB_PURKAA	/' \
        -e 's/\(a	1	\)Verbi_53F	/\1VERB_MOJAHTAA	/' \
        -e 's/\(ä	1	\)Verbi_53F	/\1VERB_YSKÄHTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_54F	/\1VERB_HUUTAA	/' \
        -e 's/\(ä	1	\)Verbi_54F	/\1VERB_PYYTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_53J	/\1VERB_HUONONTAA	/' \
        -e 's/\(ä	1	\)Verbi_53J	/\1VERB_HIVENTÄÄ	/' \
        -e 's/\(ä	1	\)Verbi_54	/\1VERB_HIVENTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_54K	/\1VERB_KUHERTAA	/' \
        -e 's/\(ä	1	\)Verbi_54K	/\1VERB_NÄPERTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_54I	/\1VERB_SIVALTAA	/' \
        -e 's/\(ä	1	\)Verbi_54I	/\1VERB_VIHELTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_54J	/\1VERB_HUONONTAA	/' \
        -e 's/\(ä	1	\)Verbi_54J	/\1VERB_HIVENTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_55F	/\1VERB_KAATAA	/' \
        -e 's/\(ä	1	\)Verbi_55	/\1VERB_PYYTÄÄ	/' \
        -e 's/\(ä	1	\)Verbi_55F	/\1VERB_YSKÄHTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_55K	/\1VERB_SORTAA	/' \
        -e 's/\(ä	1	\)Verbi_55I	/\1VERB_YLTÄÄ	/' \
        -e 's/\(ä	1	\)Verbi_55J	/\1VERB_ENTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_56	/\1VERB_KASVAA	/' \
        -e 's/\(a	1	\)Verbi_56A	/\1VERB_VIRKKAA	/' \
        -e 's/\(a	1	\)Verbi_56B	/\1VERB_TAPPAA	/' \
        -e 's/\(a	1	\)Verbi_56C	/\1VERB_AUTTAA	/' \
        -e 's/\(ä	1	\)Verbi_56C	/\1VERB_XXXTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_56D	/\1VERB_VIRKKAA	/' \
        -e 's/\(a	1	\)Verbi_56F	/\1VERB_SATAA	/' \
        -e 's/\(ä	1	\)Verbi_56F	/\1VERB_RÄPSYTTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_56J	/\1VERB_KANTAA	/' \
        -e 's/\(a	1	\)Verbi_57F	/\1VERB_KAATAA	/' \
        -e 's/\(a	1	\)Verbi_57K	/\1VERB_SAARTAA	/' \
        -e 's/\(a	1	\)Verbi_57J	/\1VERB_HUONONTAA	/' \
        -e 's/\(a	1	\)Verbi_58	/\1VERB_SOTKEA	/' \
        -e 's/\(ä	1	\)Verbi_58	/\1VERB_KYTKEÄ	/' \
        -e 's/\(a	1	\)Verbi_58D	/\1VERB_PUKEA	/' \
        -e 's/\(ä	1	\)Verbi_58D	/\1VERB_RYPEÄ	/' \
        -e 's/\(ä	1	\)Verbi_58E	/\1VERB_RYPEÄ	/' \
        -e 's/\(a	1	\)Verbi_58F	/\1VERB_KUTEA	/' \
        -e 's/\(a	1	\)Verbi_58G	/\1VERB_TUNKEA	/' \
        -e 's/\(ä	1	\)Verbi_58G	/\1VERB_ÄNKEÄ	/' \
        -e 's/\(ä	1	\)Verbi_58F	/\1VERB_PÄTEÄ	/' \
        -e 's/\(a	1	\)Verbi_58L	/\1VERB_POLKEA	/' \
        -e 's/\(ä	1	\)Verbi_58L	/\1VERB_SÄRKEÄ	/' \
        -e 's/\(a	1	\)Verbi_59J	/\1VERB_TUNTEA	/' \
        -e 's/\(ä	1	\)Verbi_60F	/\1VERB_LÄHTEÄ	/' \
        -e 's/\(a	1	\)Verbi_61	/\1VERB_KOSIA	/' \
        -e 's/\(ä	1	\)Verbi_61	/\1VERB_RYSKIÄ	/' \
        -e 's/\(a	1	\)Verbi_61A	/\1VERB_KUKKIA	/' \
        -e 's/\(ä	1	\)Verbi_61A	/\1VERB_SÖRKKIÄ	/' \
        -e 's/\(a	1	\)Verbi_61B	/\1VERB_KALPPIA	/' \
        -e 's/\(ä	1	\)Verbi_61B	/\1VERB_HYPPIÄ	/' \
        -e 's/\(a	1	\)Verbi_61C	/\1VERB_MOITTIA	/' \
        -e 's/\(ä	1	\)Verbi_61C	/\1VERB_MIETTIÄ	/' \
        -e 's/\(a	1	\)Verbi_61D	/\1VERB_KUKKIA	/' \
        -e 's/\(ä	1	\)Verbi_61D	/\1VERB_SÖRKKIÄ	/' \
        -e 's/\(ä	1	\)Verbi_61E	/\1VERB_RIIPIÄ	/' \
        -e 's/\(a	1	\)Verbi_61E	/\1VERB_RAAPIA	/' \
        -e 's/\(a	1	\)Verbi_61F	/\1VERB_AHNEHTIA	/' \
        -e 's/\(ä	1	\)Verbi_61F	/\1VERB_EHTIÄ	/' \
        -e 's/\(a	1	\)Verbi_61G	/\1VERB_ONKIA	/' \
        -e 's/\(ä	1	\)Verbi_61G	/\1VERB_MÖNKIÄ	/' \
        -e 's/\(ä	1	\)Verbi_61H	/\1VERB_TYMPIÄ	/' \
        -e 's/\(a	1	\)Verbi_61J	/\1VERB_KONTIA	/' \
        -e 's/\(ä	1	\)Verbi_61L	/\1VERB_HYLKIÄ	/' \
        -e 's/\(a	1	\)Verbi_62	/\1VERB_KOPIOIDA	/' \
        -e 's/\(ä	1	\)Verbi_62	/\1VERB_ÖYKKÄRÖIDÄ	/' \
        -e 's/\(a	1	\)Verbi_62F	/\1VERB_KOPIOIDA	/' \
        -e 's/\(a	1	\)Verbi_63	/\1VERB_SAADA	/' \
        -e 's/\(ä	1	\)Verbi_63	/\1VERB_JÄÄDÄ	/' \
        -e 's/\(a	1	\)Verbi_64	/\1VERB_TUODA	/' \
        -e 's/\(ä	1	\)Verbi_64	/\1VERB_KÄYDÄ	/' \
        -e 's/\(ä	1	\)Verbi_64	/\1VERB_SYÖDÄ	/' \
        -e 's/\(ä	1	\)Verbi_65	/\1VERB_KÄYDÄ	/' \
        -e 's/\(a	1	\)Verbi_66	/\1VERB_MARISTA	/' \
        -e 's/\(ä	1	\)Verbi_66	/\1VERB_ÄRISTÄ	/' \
        -e 's/\(a	1	\)Verbi_66E	/\1VERB_HÄVÄISTÄ	/' \
        -e 's/\(ä	1	\)Verbi_66E	/\1VERB_HÄVÄISTÄ	/' \
        -e 's/\(a	1	\)Verbi_66G	/\1VERB_RANGAISTA	/' \
        -e 's/\(a	1	\)Verbi_67	/\1VERB_ARVAILLA	/' \
        -e 's/\(ä	1	\)Verbi_67	/\1VERB_ÄKSYILLÄ	/' \
        -e 's/\(a	1	\)Verbi_67A	/\1VERB_NAKELLA	/' \
        -e 's/\(ä	1	\)Verbi_67A	/\1VERB_LEIKELLÄ	/' \
        -e 's/\(a	1	\)Verbi_67B	/\1VERB_TAPELLA	/' \
        -e 's/\(a	1	\)Verbi_67C	/\1VERB_SULATELLA	/' \
        -e 's/\(ä	1	\)Verbi_67C	/\1VERB_HERÄTELLÄ	/' \
        -e 's/\(a	1	\)Verbi_67F	/\1VERB_TIPAHDELLA	/' \
        -e 's/\(ä	1	\)Verbi_67F	/\1VERB_SÄPSÄHDELLÄ	/' \
        -e 's/\(a	1	\)Verbi_67H	/\1VERB_OMMELLA	/' \
        -e 's/\(a	1	\)Verbi_67I	/\1VERB_VAELLELLA	/' \
        -e 's/\(ä	1	\)Verbi_67I	/\1VERB_KIILLELLÄ	/' \
        -e 's/\(a	1	\)Verbi_67J	/\1VERB_KOMENNELLA	/' \
        -e 's/\(ä	1	\)Verbi_67J	/\1VERB_KÄÄNNELLÄ	/' \
        -e 's/\(a	1	\)Verbi_67K	/\1VERB_NAKERRELLA	/' \
        -e 's/\(ä	1	\)Verbi_67K	/\1VERB_KIHERRELLÄ	/' \
        -e 's/\(a	1	\)Verbi_68	/\1VERB_KOPIOIDA	/' \
        -e 's/\(ä	1	\)Verbi_68	/\1VERB_ISÄNNÖIDÄ	/' \
        -e 's/\(a	1	\)Verbi_69	/\1VERB_PALKITA	/' \
        -e 's/\(ä	1	\)Verbi_69	/\1VERB_MERKITÄ	/' \
        -e 's/\(a	1	\)Verbi_70	/\1VERB_JUOSTA	/' \
        -e 's/\(ä	1	\)Verbi_70	/\1VERB_PIESTÄ	/' \
        -e 's/\(ä	1	\)Verbi_71	/\1VERB_NÄHDÄ	/' \
        -e 's/\(a	1	\)Verbi_72	/\1VERB_KARHETA	/' \
        -e 's/\(ä	1	\)Verbi_72	/\1VERB_VÄHETÄ	/' \
        -e 's/\(a	1	\)Verbi_72A	/\1VERB_XXXKETA	/' \
        -e 's/\(ä	1	\)Verbi_72A	/\1VERB_JYRKETÄ	/' \
        -e 's/\(a	1	\)Verbi_72B	/\1VERB_HAPATA	/' \
        -e 's/\(a	1	\)Verbi_72C	/\1VERB_LOITOTA	/' \
        -e 's/\(a	1	\)Verbi_72D	/\1VERB_POIKETA	/' \
        -e 's/\(ä	1	\)Verbi_72D	/\1VERB_JYRKETÄ	/' \
        -e 's/\(a	1	\)Verbi_72E	/\1VERB_KAVETA	/' \
        -e 's/\(ä	1	\)Verbi_72F	/\1VERB_PIDETÄ	/' \
        -e 's/\(ä	1	\)Verbi_72H	/\1VERB_LÄMMETÄ	/' \
        -e 's/\(a	1	\)Verbi_72L	/\1VERB_ROHJETA	/' \
        -e 's/\(ä	1	\)Verbi_72L	/\1VERB_ILJETÄ	/' \
        -e 's/\(a	1	\)Verbi_72J	/\1VERB_INNOTA	/' \
        -e 's/\(a	1	\)Verbi_73	/\1VERB_ARVATA	/' \
        -e 's/\(ä	1	\)Verbi_73	/\1VERB_YNNÄTÄ	/' \
        -e 's/\(a	1	\)Verbi_73A	/\1VERB_MORKATA	/' \
        -e 's/\(ä	1	\)Verbi_73A	/\1VERB_YÖKÄTÄ	/' \
        -e 's/\(a	1	\)Verbi_73B	/\1VERB_SIEPATA	/' \
        -e 's/\(ä	1	\)Verbi_73B	/\1VERB_VÄLPÄTÄ	/' \
        -e 's/\(a	1	\)Verbi_73C	/\1VERB_LUNTATA	/' \
        -e 's/\(ä	1	\)Verbi_73C	/\1VERB_LÄNTÄTÄ	/' \
        -e 's/\(a	1	\)Verbi_73D	/\1VERB_MORKATA	/' \
        -e 's/\(ä	1	\)Verbi_73D	/\1VERB_YÖKÄTÄ	/' \
        -e 's/\(a	1	\)Verbi_73E	/\1VERB_KAIVATA	/' \
        -e 's/\(ä	1	\)Verbi_73E	/\1VERB_LEVÄTÄ	/' \
        -e 's/\(a	1	\)Verbi_73F	/\1VERB_JAHDATA	/' \
        -e 's/\(ä	1	\)Verbi_73F	/\1VERB_TÄHDÄTÄ	/' \
        -e 's/\(a	1	\)Verbi_73G	/\1VERB_VONGATA	/' \
        -e 's/\(ä	1	\)Verbi_73G	/\1VERB_VÄNGÄTÄ	/' \
        -e 's/\(a	1	\)Verbi_73H	/\1VERB_TEMMATA	/' \
        -e 's/\(a	1	\)Verbi_73I	/\1VERB_MULLATA	/' \
        -e 's/\(a	1	\)Verbi_73J	/\1VERB_SUUNNATA	/' \
        -e 's/\(ä	1	\)Verbi_73J	/\1VERB_RYNNÄTÄ	/' \
        -e 's/\(a	1	\)Verbi_73K	/\1VERB_VERRATA	/' \
        -e 's/\(ä	1	\)Verbi_73L	/\1VERB_HYLJÄTÄ	/' \
        -e 's/\(a	1	\)Verbi_74	/\1VERB_KARHUTA	/' \
        -e 's/\(ä	1	\)Verbi_74	/\1VERB_TÄHYTÄ	/' \
        -e 's/\(a	1	\)Verbi_74A	/\1VERB_KAIKOTA	/' \
        -e 's/\(a	1	\)Verbi_74B	/\1VERB_UPOTA	/' \
        -e 's/\(a	1	\)Verbi_74C	/\1VERB_PEITOTA	/' \
        -e 's/\(a	1	\)Verbi_74D	/\1VERB_POIKETA	/' \
        -e 's/\(ä	1	\)Verbi_74D	/\1VERB_KERETÄ	/' \
        -e 's/\(a	1	\)Verbi_74E	/\1VERB_KIVUTA	/' \
        -e 's/\(ä	1	\)Verbi_74E	/\1VERB_REVETÄ	/' \
        -e 's/\(a	1	\)Verbi_74F	/\1VERB_VAAHDOTA	/' \
        -e 's/\(a	1	\)Verbi_74G	/\1VERB_PINGOTA	/' \
        -e 's/\(ä	1	\)Verbi_74G	/\1VERB_ÄNGETÄ	/' \
        -e 's/\(a	1	\)Verbi_74H	/\1VERB_KAMMETA	/' \
        -e 's/\(a	1	\)Verbi_74J	/\1VERB_KANNETA	/' \
        -e 's/\(a	1	\)Verbi_74K	/\1VERB_IRROTA	/' \
        -e 's/\(a	1	\)Verbi_74L	/\1VERB_HALJETA	/' \
        -e 's/\(ä	1	\)Verbi_74L	/\1VERB_ILJETÄ	/' \
        -e 's/\(a	1	\)Verbi_75	/\1VERB_HALUTA	/' \
        -e 's/\(ä	1	\)Verbi_75	/\1VERB_SELVITÄ	/' \
        -e 's/\(ä	1	\)Verbi_75B	/\1VERB_RYÖPYTÄ	/' \
        -e 's/\(a	1	\)Verbi_75C	/\1VERB_PEITOTA	/' \
        -e 's/\(ä	1	\)Verbi_75D	/\1VERB_KERITÄ	/' \
        -e 's/\(ä	1	\)Verbi_75H	/\1VERB_LÄMMITÄ	/' \
        -e 's/\(a	1	\)Verbi_75I	/\1VERB_AALLOTA	/' \
        -e 's/\(a	1	\)Verbi_75I	/\1VERB_AALLOTA	/' \
        -e 's/\(ä	1	\)Verbi_75I	/\1VERB_HELLITÄ	/' \
        -e 's/\(ä	1	\)Verbi_75J	/\1VERB_LENNITÄ	/' \
        -e 's/\(a	1	\)Verbi_76F	/\1VERB_TAITAA	/' \
        -e 's/\(ä	1	\)Verbi_76F	/\1VERB_TIETÄÄ	/' \
        -e 's/\(a	1	\)Verbi_77	/\1VERB_VIPAJAA	/' \
        -e 's/\(ä	1	\)Verbi_77	/\1VERB_HELÄJÄÄ	/' \
        -e 's/\(a	1	\)Verbi_78	/\1VERB_RAIKAA	/' \
        -e 's/\(ä	1	\)Verbi_78	/\1VERB_ÄHKÄÄ	/' \
        -e 's/\(a	1	\)Verbi_78A	/\1VERB_RAIKAA	/' |\
    $SED -e 's/\(	1	\)Substantiivi_[^[:space:]]*	/\1NOUN_XXXFAIL	/' \
        -e 's/\(	1	\)Adjektiivi_[^[:space:]]*	/\1ADJ_XXXFAIL	/' \
        -e 's/\(	1	\)Verbi_[^[:space:]]*	/\1VERB_XXXFAIL	/' |\
    $SED -e 's/1	NOUN/NOUN	NOUN/' \
        -e 's/1	PROPN/PROPN	PROPN/' \
        -e 's/1	VERB/VERB	VERB/' \
        -e 's/1	ADJ/ADJ	ADJ/' \
        -e 's/1	NUM/NUM	NUM/' \
        -e 's/1	PRON/PRON	PRON/' \
        -e 's/1	ADP/ADP	ADP/' \
        -e 's/1	INTJ/INTJ	INTJ/' \
        -e 's/1	ADV/ADV	ADV/'
# see what else we can
cat fiwikt.tempxml |\
# pick all classified for now
    fgrep -v '<kotus' |\
    egrep 'Interjektio|Adverbi|Konjunktion|Prepositio' |\
    egrep -v 'Verbi|Substantiivi|Adjektiivi|Pronomini|Numeraali' |\
    fgrep -v 'lemma>-' |\
# make csv
    $SED -re 's/^.*<lemma>([^<]*).*<wordclass>([^<]*).*$/\1,\2/' |\
# remove missing lemmas or classes shown as leftover tags from ^^
    fgrep -v '<entry>' |\
    tr '|' ',' |\
    $SED -re 's/([[:digit:]]+)-([[:upper:]])/\1,\2/' |\
    gawk -F , 'NF == 2 {printf("%s\t1\t%s\tfiwikt\n", $1, $2);}' |\
    $SED -e 's/Adverbi_99/ADV_NOPEASTI/' \
        -e 's/Adverbi/ADV_NOPEASTI/' \
        -e 's/Prepositio/ADP_MUKAISESTI/' \
        -e 's/Interjektio/INTJ_HAH/' \
        -e 's/Konjunktio/SCONJ_ETTÄ/' |\
    $SED -e 's/1	NOUN/NOUN	NOUN/' \
        -e 's/1	ADP/ADP	ADP/' \
        -e 's/1	ADV/ADV	ADV/' \
        -e 's/1	INTJ/INTJ	INTJ/' \
        -e 's/1	SCONJ/SCONJ	SCONJ/'
