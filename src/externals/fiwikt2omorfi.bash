#!/bin/bash
# This script takes a Finnish wiktionary xml dump and converts it to omorfi
# Originally from end assignment of CLT 131 in Uni. Helsinki by ...
# Bit of coding style fixes and updates by <flammie@iki.fi>

print_usage() {
    echo "Usage: $0 [fiwikt-pages-articles.xml]"
    echo
    echo "fiwikt-pages-articles.xml must point to unzipped fi.wiktionary dump."
    echo "If omitted, stdin is used"
}

if test $# -ge 2 ; then
    print_usage
    exit 1
fi

# Define word class
wc='(Substantiivi|Adjektiivi|Pronomini|Numeraali|Prepositio|Adverbi|Interjektio|Konjunktio|Partikkeli|Verbi|Erisnimi)'
# Fetch only relevant lines from the xml dump (NOTE: This assumes relevant
# lines are between <page> & </page> tags)
cat $@ | sed -ne '/<page>/,/<\/page>/p' |\
# Remove all line-initial whitespaces
    sed -e 's/^[ \t]*//g' |\
# Remove unwanted xml tags
    sed -ne '/\(<page>\|<title>\)/p' -ne '/<text/,/<\/page>/p' |\
# Remove unwanted xml tag (NOTE: The </revision> tag is found between </text>
# & </page>)
    sed '/<\/revision>/d' |\
# Remove linebreaks
    tr -d '\n' |\
# Place linebreak infront of each <page>
    sed -re "s/<page>/\n\0/g" |\
# Retain only those lines which contain relevant content (in this case ==Suomi== which is the heading of Finnish words)
    fgrep "==Suomi==" |\
# Remove certain MediaWiki pages
    sed -r "/<title>(Luokka:)|(Malline:)|(Wikisanakirja:)/d" |\
# Place tags and content on separate lines
    sed -re "s/(<\/page>)/\n\1/g" \
    -e "s/(<title>)/\n\1/g" \
    -e "s/(<\/title>)/\1\n/g" \
    -e "s/(<text [^>]*>)/\1\n/g" \
    -e "s/(<\/text>)/\n\1/g" |\
# Place relevant content markup characters on seperate lines
    sed -re "s/(==*[[:alpha:]]+==)/\n\1/g" \
    -e "s/((\(\{\{)|(\{\{fi))/\n\1/g" \
    -e "s/(#)/\n\1/g" |\
# Parse lines and tag word classes in headings (example: ===Substantiivi===)
    sed -re "s/=$wc=/<wordclass>\1<\/wordclass>/g" |\
# Parse lines and tag with KOTUS numbering (this script only allows
# {{taivutustyyppi|99(alt: 99-A), {{fi-taivitus|99 & {{fi-subs-99 formats)
    sed -re "s/\{\{taivutustyyppi\|([[:alnum:]]+-?[[:alnum:]]?)\}\}/<kotus>\1<\/kotus>/" \
    -e "s/\{\{fi-taivutus\|([[:digit:]]+(\|?[[:upper:]])*)/<kotus>\1<\/kotus>/" \
    -e "s/\{\{fi-[[:alpha:]]*-([[:digit:]]+)\}\}/<kotus>\1<\/kotus>/" |\
# Parse lines that begin with # but not #: and tag with definition
    sed -re "s/^(#[^#:].*)$/<definition>\1<\/definition>/g" |\
# Parse lines that begin with #: and tag with example
    sed -re "s/^(#:.*)$/<example>\1<\/example>/g" |\
# Place tags on separate lines
    sed -re "s/(<(wordclass|kotus|definition|example)>.*<\/(wordclass|kotus|definition|example)>)/\n\1\n/g" |\
# Remove all  non-tagged lines
    sed -rn "/^<.*>$/p" |\
# Remove definitions that are for conjugated words, i.e. retain only
# definitions of unconjugated words
    sed -r "/(\{\{taivm)|(-taivm\|)|(\(taivutusmuoto)|(\(taivutusmuodot)|(taivutusmuoto'')|(\(taivus)/d" | egrep -v "\[\[Luokka:Suomen ([[:alpha:]]+) taivutusmuodot\]\]" |\
# Parse remove wikimedia links, formatting and other tuff
    sed -r "s/\[\[[[:alpha:]]+\|([[:alpha:]]+)\]\]/\1/g" |\
# Parse and remove other wikimedia markup "garbage"
    sed -re "/\[\[[[:alpha:]]+:[[:alpha:]]+.*\]\]/d" -e "/\{.*\}/d" | sed -re "s/\[|\]//g" -e "s/'|#|#://g" |\
# Remove unescessary <text> & </text> tags
    sed -re "/^<text |<\/text>/d" |\
# Rename remaining wiktionary xml tags: page to entry, title to lemma
    sed -re "s/page>$/entry>/g" -e "s/title>/lemma>/g" |
# Remove linebreaks
    tr -d '\n' |\
# Place each <entry> on a separate line
    sed -re "s/(<entry>)/\n\1/g" |\
# Place entries in alphabetical order (due to uniform xml strucuture sort
# command works normally) and write as .xml file
    sort | tee fiwikt.tempxml |\
# pick all classified for now
    fgrep '<kotus' |\
    fgrep -v 'lemma>-' |\
# make csv
    sed -re 's/^.*<lemma>([^<]*).*<wordclass>([^<]*).*<kotus>([^<]*).*$/\1,\3,\2/' |\
# remove missing lemmas or classes shown as leftover tags from ^^
    fgrep -v '<entry>' |\
    tr '|' ',' |\
    sed -re 's/([[:digit:]]+)-([[:upper:]])/\1,\2/' |\
    gawk -F , 'NF == 3 {printf("%s\t1\t%s_%s\tfiwikt\n", $1, $3, $2);}
        NF == 4 {printf("%s\t1\t%s_%s%s\tfiwikt\n", $1, $4, $2, $3);}' |\
    sed -e 's/Adverbi_99/ADV_NOPEASTI/' \
        -e 's/Interjektio_[^	]*/INTJ_HAH/' \
        -e 's/\(o	1	\)Substantiivi_1	/\1NOUN_TALO	/' \
        -e 's/\(o	1	\)Erisnimi_1	/\1PROPN_TALO	/' \
        -e 's/\(u	1	\)Substantiivi_1	/\1NOUN_ASU	/' \
        -e 's/\(u	1	\)Erisnimi_1	/\1PROPN_ASU	/' \
        -e 's/\(ö	1	\)Erisnimi_1	/\1PROPN_MÖMMÖ	/' \
        -e 's/\(o	1	\)Erisnimi_1A	/\1PROPN_UKKO	/' \
        -e 's/\(o	1	\)Substantiivi_1A	/\1NOUN_UKKO	/' \
        -e 's/\(u	1	\)Substantiivi_1A	/\1NOUN_TIKKU	/' \
        -e 's/\(u	1	\)Erisnimi_1A	/\1PROPN_TIKKU	/' \
        -e 's/\(u	1	\)Substantiivi_1B	/\1NOUN_LIPPU	/' \
        -e 's/\(o	1	\)Erisnimi_1B	/\1PROPN_HAPPO	/' \
        -e 's/\(o	1	\)Substantiivi_1C	/\1NOUN_HIRTTO	/' \
        -e 's/\(o	1	\)Erisnimi_1C	/\1PROPN_HIRTTO	/' \
        -e 's/\(u	1	\)Adjektiivi_1C	/\1ADJ_TORTTU	/' \
        -e 's/\(y	1	\)Adjektiivi_1C	/\1ADJ_YLENNETTY	/' \
        -e 's/\(u	1	\)Substantiivi_1C	/\1NOUN_TORTTU	/' \
        -e 's/\(u	1	\)Erisnimi_1C	/\1PROPN_TORTTU	/' \
        -e 's/\(y	1	\)Erisnimi_1C	/\1PROPN_PYTTY	/' \
        -e 's/\(ö	1	\)Erisnimi_1C	/\1PROPN_PÖNTTÖ	/' \
        -e 's/\(u	1	\)Erisnimi_1D	/\1PROPN_ALKU	/' \
        -e 's/\(o	1	\)Substantiivi_1D	/\1NOUN_RUOKO	/' \
        -e 's/\(o	1	\)Erisnimi_1D	/\1PROPN_RUOKO	/' \
        -e 's/\(o	1	\)Erisnimi_1E	/\1PROPN_VETO	/' \
        -e 's/\(o	1	\)Substantiivi_1F	/\1NOUN_VETO	/' \
        -e 's/\(u	1	\)Substantiivi_1F	/\1NOUN_KUITU	/' \
        -e 's/\(o	1	\)Erisnimi_1F	/\1PROPN_VETO	/' \
        -e 's/\(o	1	\)Erisnimi_1G	/\1PROPN_RUNKO	/' \
        -e 's/\(o	1	\)Substantiivi_1H	/\1NOUN_SAMPO	/' \
        -e 's/\(u	1	\)Erisnimi_1H	/\1PROPN_RUMPU	/' \
        -e 's/\(o	1	\)Substantiivi_1I	/\1NOUN_KIELTO	/' \
        -e 's/\(o	1	\)Erisnimi_1I	/\1PROPN_KIELTO	/' \
        -e 's/\(o	1	\)Erisnimi_1J	/\1PROPN_TUNTO	/' \
        -e 's/\(o	1	\)Erisnimi_1K	/\1PROPN_SIIRTO	/' \
        -e 's/\(y	1	\)Substantiivi_1L	/\1NOUN_NÄKY	/' \
        -e 's/\(o	1	\)Substantiivi_1M	/\1NOUN_RUOKO	/' \
        -e 's/\(u	1	\)Substantiivi_1M	/\1NOUN_SUKU	/' \
        -e 's/\(y	1	\)Erisnimi_2	/\1PROPN_KÄRRY	/' \
        -e 's/\(o	1	\)Erisnimi_2	/\1PROPN_RUIPELO	/' \
        -e 's/\(o	1	\)Substantiivi_3	/\1NOUN_TUOMIO	/' \
        -e 's/\(o	1	\)Erisnimi_3	/\1PROPN_TUOMIO	/' \
        -e 's/\(e	1	\)Erisnimi_3	/\1PROPN_ZOMBIE	/' \
        -e 's/\(ö	1	\)Erisnimi_3	/\1PROPN_HÄIRIÖ	/' \
        -e 's/\(o	1	\)Erisnimi_4A	/\1PROPN_LEPAKKO	/' \
        -e 's/\(ö	1	\)Erisnimi_4A	/\1PROPN_YKSIKKÖ	/' \
        -e 's/\(o	1	\)Substantiivi_4C	/\1NOUN_HIRTTO	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Erisnimi_5	/\1PROPN_TYYLI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Substantiivi_5	/\1NOUN_TYYLI	/' \
        -e 's/\([mnhflrktbpsxgd]	1	\)Substantiivi_5	/\1NOUN_PUNK	/' \
        -e 's/\([mnhflrktbpsgd]	1	\)Erisnimi_5	/\1PROPN_PUNK	/' \
        -e 's/\(i	1	\)Erisnimi_5	/\1PROPN_RUUVI	/' \
        -e 's/\(i	1	\)Substantiivi_5	/\1NOUN_RUUVI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Erisnimi_5A	/\1PROPN_HÄKKI	/' \
        -e 's/\(i	1	\)Erisnimi_5A	/\1PROPN_LOKKI	/' \
        -e 's/\(i	1	\)Erisnimi_5B	/\1PROPN_KUPPI	/' \
        -e 's/\(i	1	\)Substantiivi_5B	/\1NOUN_KUPPI	/' \
        -e 's/\(it	1	\)Substantiivi_5B	/\1NOUN_KLUMPIT§	/' \
        -e 's/\(i	1	\)Erisnimi_5C	/\1PROPN_KORTTI	/' \
        -e 's/\(i	1	\)Substantiivi_5C	/\1NOUN_KORTTI	/' \
        -e 's/\(i	1	\)Substantiivi_5G	/\1NOUN_VANKI	/' \
        -e 's/\(i	1	\)Erisnimi_5G	/\1PROPN_VANKI	/' \
        -e 's/\(i	1	\)Substantiivi_5F	/\1NOUN_LEHTI	/' \
        -e 's/\(i	1	\)Erisnimi_5F	/\1PROPN_TAUTI	/' \
        -e 's/\(i	1	\)Erisnimi_5J	/\1PROPN_SOINTI	/' \
        -e 's/\([äöyÄÖY].*i	1	\)Erisnimi_6	/\1PROPN_KÄNÄÄLI	/' \
        -e 's/\(.*i	1	\)Erisnimi_6	/\1PROPN_KANAALI	/' \
        -e 's/\(.*i	1	\)Substantiivi_6	/\1NOUN_KANAALI	/' \
        -e 's/\([mnlhfkrtpdbgs]	1	\)Substantiivi_6	/\1NOUN_STADION	/' \
        -e 's/\([mnlhfkrtpdbgs]	1	\)Erisnimi_6	/\1PROPN_STADION	/' \
        -e 's/\(i	1	\)Erisnimi_6C	/\1PROPN_SKEITTI	/' \
        -e 's/\(i	1	\)Erisnimi_7	/\1PROPN_ONNI	/' \
        -e 's/\(i	1	\)Substantiivi_7	/\1NOUN_ONNI	/' \
        -e 's/\(e	1	\)Numeraali_7	/\1NUM_KOLME	/' \
        -e 's/\(i	1	\)Erisnimi_7D	/\1PROPN_NOKI	/' \
        -e 's/\(i	1	\)Erisnimi_7E	/\1PROPN_LAHTI	/' \
        -e 's/\(i	1	\)Erisnimi_7F	/\1PROPN_KORPI	/' \
        -e 's/\([äöy].*i	1	\)Erisnimi_7D	/\1PROPN_KÄKI	/' \
        -e 's/\(i	1	\)Erisnimi_7H	/\1PROPN_SAMPI	/' \
        -e 's/\(i	1	\)Substantiivi_7J	/\1NOUN_SOINTI	/' \
        -e 's/\(i	1	\)Erisnimi_7L	/\1PROPN_ARKI	/' \
        -e 's/\(e	1	\)Erisnimi_8	/\1PROPN_NALLE	/' \
        -e 's/\(e	1	\)Substantiivi_8	/\1NOUN_NALLE	/' \
        -e 's/\(e	1	\)Erisnimi_8A	/\1PROPN_EKKE	/' \
        -e 's/\(a	1	\)Substantiivi_9	/\1NOUN_KIRJA	/' \
        -e 's/\(a	1	\)Substantiivi_9A	/\1NOUN_POLITIIKKA	/' \
        -e 's/\(a	1	\)Pronomini_9	/\1PRON_SAMA	/' \
        -e 's/\(a	1	\)Erisnimi_9	/\1PROPN_KIRJA	/' \
        -e 's/\(a	1	\)Erisnimi_9A	/\1PROPN_POLITIIKKA	/' \
        -e 's/\(a	1	\)Substantiivi_9B	/\1NOUN_TIPPA	/' \
        -e 's/\(a	1	\)Erisnimi_9C	/\1PROPN_MITTA	/' \
        -e 's/\(a	1	\)Erisnimi_9D	/\1PROPN_VAAKA	/' \
        -e 's/\(a	1	\)Substantiivi_9F	/\1NOUN_PATA	/' \
        -e 's/\(a	1	\)Erisnimi_9F	/\1PROPN_PATA	/' \
        -e 's/\(a	1	\)Erisnimi_9I	/\1PROPN_VALTA	/' \
        -e 's/\(a	1	\)Substantiivi_9J	/\1NOUN_KUTSUNTA	/' \
        -e 's/\(a	1	\)Erisnimi_9J	/\1PROPN_KUTSUNTA	/' \
        -e 's/\(a	1	\)Erisnimi_9K	/\1PROPN_KERTA	/' \
        -e 's/\(a	1	\)Adjektiivi_9L	/\1ADJ_ARKA	/' \
        -e 's/\(a	1	\)Adjektiivi_10	/\1ADJ_RUMA	/' \
        -e 's/\(a	1	\)Substantiivi_10	/\1NOUN_VOIMA	/' \
        -e 's/\(a	1	\)Erisnimi_10	/\1PROPN_VOIMA	/' \
        -e 's/\(a	1	\)Verbi_10	/\1NOUN_VOIMA	/' \
        -e 's/\(ä	1	\)Erisnimi_10	/\1PROPN_HÖPÖTTÄJÄ	/' \
        -e 's/\(ä	1	\)Substantiivi_10	/\1NOUN_HÖPÖTTÄJÄ	/' \
        -e 's/\(a	1	\)Numeraali_10	/\1NUM_MILJOONA	/' \
        -e 's/\(än	1	\)Numeraali_10	/\1NUM_YHDEKSÄN	/' \
        -e 's/\(ä	1	\)Erisnimi_10	/\1PROPN_HÖPÖTTÄJÄ	/' \
        -e 's/\(a	1	\)Substantiivi_10A	/\1NOUN_KUKKA	/' \
        -e 's/\(ä	1	\)Substantiivi_10A	/\1NOUN_HÖLKKÄ	/' \
        -e 's/\(a	1	\)Erisnimi_10A	/\1PROPN_KUKKA	/' \
        -e 's/\(ä	1	\)Erisnimi_10A	/\1PROPN_HÖLKKÄ	/' \
        -e 's/\(ä	1	\)Erisnimi_10B	/\1PROPN_SEPPÄ	/' \
        -e 's/\(a	1	\)Erisnimi_10B	/\1PROPN_KUOPPA	/' \
        -e 's/\(ä	1	\)Erisnimi_10C	/\1PROPN_KENTTÄ	/' \
        -e 's/\(a	1	\)Substantiivi_10L	/\1NOUN_OLKA	/' \
        -e 's/\([Pp]oika	1	\)Substantiivi_10D	/\1NOUN_POIKA	/' \
        -e 's/\([Pp]oika	1	\)Erisnimi_10D	/\1PROPN_POIKA	/' \
        -e 's/\(ä	1	\)Substantiivi_10D	/\1NOUN_NÄLKÄ	/' \
        -e 's/\(ä	1	\)Erisnimi_10D	/\1PROPN_NÄLKÄ	/' \
        -e 's/\(a	1	\)Erisnimi_10E	/\1PROPN_LUPA	/' \
        -e 's/\(a	1	\)Substantiivi_10F	/\1NOUN_SOTA	/' \
        -e 's/\(ä	1	\)Substantiivi_10F	/\1NOUN_PÖYTÄ	/' \
        -e 's/\(ä	1	\)Substantiivi_10G	/\1NOUN_KENKÄ	/' \
        -e 's/\(a	1	\)Erisnimi_10F	/\1PROPN_SOTA	/' \
        -e 's/\(a	1	\)Erisnimi_10G	/\1PROPN_HONKA	/' \
        -e 's/\(ä	1	\)Erisnimi_10G	/\1PROPN_KENKÄ	/' \
        -e 's/\(a	1	\)Substantiivi_10H	/\1NOUN_RAMPA	/' \
        -e 's/\(a	1	\)Erisnimi_10J	/\1PROPN_KUNTA	/' \
        -e 's/\(a	1	\)Adjektiivi_10J	/\1ADJ_VIHANTA	/' \
        -e 's/\(ä	1	\)Substantiivi_10L	/\1NOUN_NÄLKÄ	/' \
        -e 's/\(a	1	\)Erisnimi_11	/\1PROPN_MAKKARA	/' \
        -e 's/\(ä	1	\)Erisnimi_11	/\1PROPN_HÄKKYRÄ	/' \
        -e 's/\(a	1	\)Substantiivi_12	/\1NOUN_KITARA	/' \
        -e 's/\(ä	1	\)Substantiivi_12	/\1NOUN_HÄKKYRÄ	/' \
        -e 's/\(a	1	\)Erisnimi_12	/\1PROPN_KITARA	/' \
        -e 's/\(a	1	\)Substantiivi_13	/\1NOUN_KIRJA	/' \
        -e 's/\(a	1	\)Erisnimi_13	/\1PROPN_KIRJA	/' \
        -e 's/\(a	1	\)Erisnimi_14	/\1PROPN_LUSIKKA	/' \
        -e 's/\(a	1	\)Substantiivi_14A	/\1NOUN_LUSIKKA	/' \
        -e 's/\(a	1	\)Erisnimi_14A	/\1PROPN_LUSIKKA	/' \
        -e 's/\(ä	1	\)Erisnimi_14A	/\1PROPN_HÖLKKÄ	/' \
        -e 's/\(a	1	\)Erisnimi_14C	/\1PROPN_MITTA	/' \
        -e 's/\(a	1	\)Substantiivi_14G	/\1NOUN_HONKA	/' \
        -e 's/\(a	1	\)Pronomini_15	/\1PRON_USEA	/' \
        -e 's/\(i	1	\)Pronomini_16	/\1PRON_KUMPI	/' \
        -e 's/\(ikin	1	\)Pronomini_16	/\1PRON_KUMPIKIN	/' \
        -e 's/\(a	1	\)Erisnimi_18	/\1PROPN_MAA	/' \
        -e 's/\(u	1	\)Erisnimi_18	/\1PROPN_PUU	/' \
        -e 's/\(u	1	\)Pronomini_18	/\1PRON_MUU	/' \
        -e 's/\(o	1	\)Erisnimi_18	/\1PROPN_OOKOO	/' \
        -e 's/\(ä	1	\)Erisnimi_18	/\1PROPN_PÄÄ	/' \
        -e 's/\(ie	1	\)Erisnimi_19	/\1PROPN_TIE	/' \
        -e 's/\(uo	1	\)Erisnimi_19	/\1PROPN_VUO	/' \
        -e 's/\(e	1	\)Substantiivi_20	/\1NOUN_PATEE	/' \
        -e 's/\(ä	1	\)Erisnimi_20	/\1PROPN_HYVINKÄÄ	/' \
        -e 's/\(	1	\)Substantiivi_21	/\1NOUN_ROSÉ	/' \
        -e 's/\(ie	1	\)Pronomini_21	/\1PRON_MIE	/' \
        -e 's/\(	1	\)Erisnimi_21	/\1PROPN_ROSÉ	/' \
        -e 's/\(w	1	\)Erisnimi_22	/\1PROPN_SHOW	/' \
        -e 's/\(i	1	\)Substantiivi_24	/\1NOUN_RUUHI	/' \
        -e 's/\(i	1	\)Erisnimi_24	/\1PROPN_RUUHI	/' \
        -e 's/\(meri	1	\)Substantiivi_24	/\1NOUN_MERI	/' \
        -e 's/\(i	1	\)Erisnimi_25	/\1PROPN_TAIMI	/' \
        -e 's/\(i	1	\)Erisnimi_26	/\1PROPN_RUUHI	/' \
        -e 's/\(et	1	\)Erisnimi_26	/\1PROPN_SAARET	/' \
        -e 's/\(i	1	\)Erisnimi_27	/\1PROPN_KÖYSI	/' \
        -e 's/\(i	1	\)Erisnimi_28	/\1PROPN_VARSI	/' \
        -e 's/\(i	1	\)Substantiivi_29	/\1NOUN_UKSI	/' \
        -e 's/\(i	1	\)Substantiivi_31	/\1NOUN_HAAKSI	/' \
        -e 's/\(n	1	\)Erisnimi_32	/\1PROPN_SIEMEN	/' \
        -e 's/\(n	1	\)Erisnimi_33A	/\1PROPN_HÄRKIN	/' \
        -e 's/\(ton	1	\)Verbi_34C	/\1ADJ_VIATON	/' \
        -e 's/\(tön	1	\)Verbi_34C	/\1ADJ_KYVYTÖN	/' \
        -e 's/\(n	1	\)Adjektiivi_33B	/\1ADJ_HAPAN	/' \
        -e 's/\([äöyÄÖY].*nen	1	\)Erisnimi_38	/\1PROPN_KYLKIÄINEN	/' \
        -e 's/\([äöyÄÖY].*nen	1	\)Substantiivi_38	/\1NOUN_KYLKIÄINEN	/' \
        -e 's/\([äöyÄÖY].*nen	1	\)Verbi_38	/\1NOUN_KYLKIÄINEN	/' \
        -e 's/\(nen	1	\)Substantiivi_38	/\1NOUN_AAKKOSTAMINEN	/' \
        -e 's/\(set	1	\)Substantiivi_38	/\1NOUN_RAPPUSET	/' \
        -e 's/\(nen	1	\)Pronomini_38	/\1PRON_JOKAINEN	/' \
        -e 's/\(nen	1	\)Erisnimi_38	/\1PROPN_AAKKOSTAMINEN	/' \
        -e 's/\(nen	1	\)Adjektiivi_38	/\1ADJ_AAKKOSELLINEN	/' \
        -e 's/\(s	1	\)Numeraali_38	/\1NUM_NELJÄS	/' \
        -e 's/\(s	1	\)Erisnimi_39	/\1PROPN_VAKUUTUS	/' \
        -e 's/\(s	1	\)Substantiivi_39	/\1NOUN_VAKUUTUS	/' \
        -e 's/\(uus	1	\)Substantiivi_40	/\1NOUN_AAKKOSELLISUUS	/' \
        -e 's/\(os	1	\)Substantiivi_41	/\1NOUN_UROS	/' \
        -e 's/\(as	1	\)Substantiivi_41	/\1NOUN_PATSAS	/' \
        -e 's/\(as	1	\)Erisnimi_41	/\1PROPN_PATSAS	/' \
        -e 's/\(es	1	\)Erisnimi_41	/\1PROPN_ARISTOTELES	/' \
        -e 's/\(äs	1	\)Erisnimi_41	/\1PROPN_ÄYRÄS	/' \
        -e 's/\(as	1	\)Erisnimi_41A	/\1PROPN_ASUKAS	/' \
        -e 's/\(as	1	\)Erisnimi_41C	/\1PROPN_RATAS	/' \
        -e 's/\(is	1	\)Erisnimi_41C	/\1PROPN_ALTIS	/' \
        -e 's/\(as	1	\)Substantiivi_41D	/\1NOUN_VARAS	/' \
        -e 's/\(as	1	\)Substantiivi_41G	/\1NOUN_KANGAS	/' \
        -e 's/\(äs	1	\)Erisnimi_41G	/\1PROPN_KÖNGÄS	/' \
        -e 's/\(as	1	\)Erisnimi_41G	/\1PROPN_KANGAS	/' \
        -e 's/\(as	1	\)Substantiivi_41H	/\1NOUN_HAMMAS	/' \
        -e 's/\(as	1	\)Erisnimi_41K	/\1PROPN_PORRAS	/' \
        -e 's/\(es	1	\)Substantiivi_42	/\1NOUN_MIES	/' \
        -e 's/\(es	1	\)Erisnimi_42	/\1PROPN_MIES	/' \
        -e 's/\(et	1	\)Erisnimi_44	/\1PROPN_HÄMET	/' \
        -e 's/\(et	1	\)Erisnimi_44C	/\1PROPN_KORTET	/' \
        -e 's/\(et	1	\)Erisnimi_44F	/\1PROPN_AHDET	/' \
        -e 's/\(et	1	\)Erisnimi_44K	/\1PROPN_VIIRRET	/' \
        -e 's/\(et	1	\)Erisnimi_44I	/\1PROPN_VUOLLET	/' \
        -e 's/\(et	1	\)Erisnimi_44J	/\1PROPN_RINNET	/' \
        -e 's/\(as	1	\)Numeraali_45	/\1ADJ_KOLMAS	/' \
        -e 's/\(äs	1	\)Numeraali_45	/\1ADJ_NELJÄS	/' \
        -e 's/\(yt	1	\)Adjektiivi_47	/\1ADJ_ÄLLISTYNYT	/' \
        -e 's/\(i	1	\)Substantiivi_48	/\1NOUN_ORI	/' \
        -e 's/\(e	1	\)Substantiivi_48	/\1NOUN_ASTE	/' \
        -e 's/\(e	1	\)Erisnimi_48	/\1PROPN_ASTE	/' \
        -e 's/\(e	1	\)Substantiivi_48A	/\1NOUN_LÄÄKE	/' \
        -e 's/\(e	1	\)Erisnimi_48A	/\1PROPN_LÄÄKE	/' \
        -e 's/\(e	1	\)Substantiivi_48D	/\1NOUN_KOE	/' \
        -e 's/\(e	1	\)Substantiivi_48F	/\1NOUN_LUODE	/' \
        -e 's/\(e	1	\)Erisnimi_48F	/\1PROPN_LUODE	/' \
        -e 's/\(e	1	\)Erisnimi_48J	/\1PROPN_RAKENNE	/' \
        -e 's/\(e	1	\)Erisnimi_48K	/\1PROPN_KIERRE	/' \
        -e 's/\(e	1	\)Erisnimi_49	/\1PROPN_ASTE	/' \
        -e 's/\(l	1	\)Substantiivi_49	/\1NOUN_SIEMEN	/' \
        -e 's/\(l	1	\)Erisnimi_49E	/\1PROPN_TAIVAL	/' \
        -e 's/\(.	1	\)Substantiivi_51	/\1NOUN_51XXX	/' \
        -e 's/\(.	1	\)Numeraali_51	/\1NUM_51XXX	/' \
        -e 's/\(.	1	\)Pronomini_51	/\1PRON_51XXX	/' \
        -e 's/\(.	1	\)Erisnimi_51	/\1PROPN_51XXX	/' |\
    sed -e 's/\(a	1	\)Verbi_53	/\1VERB_KASVAA	/' \
        -e 's/\(ä	1	\)Verbi_52F	/\1VERB_SILIYTYÄ	/' \
        -e 's/\(a	1	\)Verbi_53C	/\1VERB_VIEROITTAA	/' \
        -e 's/\(a	1	\)Verbi_53F	/\1VERB_MOJAHTAA	/' \
        -e 's/\(ä	1	\)Verbi_53F	/\1VERB_YSKÄHTÄÄ	/' \
        -e 's/\(ä	1	\)Verbi_54J	/\1VERB_HIVENTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_55F	/\1VERB_KAATAA	/' \
        -e 's/\(ä	1	\)Verbi_55	/\1VERB_PYYTÄÄ	/' \
        -e 's/\(a	1	\)Verbi_56C	/\1VERB_AUTTAA	/' \
        -e 's/\(a	1	\)Verbi_56F	/\1VERB_SATAA	/' \
        -e 's/\(ä	1	\)Verbi_67C	/\1VERB_HERÄTELLÄ	/' \
        -e 's/\(a	1	\)Verbi_72D	/\1VERB_POIKETA	/' \
        -e 's/\(a	1	\)Verbi_73	/\1VERB_ARVATA	/' \
        -e 's/\(a	1	\)Verbi_74D	/\1VERB_POIKETA	/'
# see what else we can
cat fiwikt.tempxml |\
# pick all classified for now
    fgrep -v '<kotus' |\
    egrep 'Interjektio|Adverbi|Konjunktion|Prepositio' |\
    egrep -v 'Verbi|Substantiivi|Adjektiivi|Pronomini|Numeraali' |\
    fgrep -v 'lemma>-' |\
# make csv
    sed -re 's/^.*<lemma>([^<]*).*<wordclass>([^<]*).*$/\1,\2/' |\
# remove missing lemmas or classes shown as leftover tags from ^^
    fgrep -v '<entry>' |\
    tr '|' ',' |\
    sed -re 's/([[:digit:]]+)-([[:upper:]])/\1,\2/' |\
    gawk -F , 'NF == 2 {printf("%s\t1\t%s\tfiwikt\n", $1, $2);}' |\
    sed -e 's/Adverbi_99/ADV_NOPEASTI/' \
        -e 's/Adverbi/ADV_NOPEASTI/' \
        -e 's/Prepositio/ADP_MUKAISESTI/' \
        -e 's/Interjektio/INTJ_HAH/' \
        -e 's/Konjunktio/SCONJ_ETTÄ/'
