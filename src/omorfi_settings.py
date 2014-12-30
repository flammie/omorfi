#!/bin/python3



# common symbols for all
version_id_easter_egg='OMORFI_VERSION_≥_14_©_GNU_GPL_V3'
word_boundary="{WB}"
newword_boundary="{wB}"
weak_boundary="{XB}"
deriv_boundary="{DB}"
morph_boundary="{MB}"
stub_boundary="{STUB}"
optional_hyphen="{hyph?}"
common_multichars={
        version_id_easter_egg,
        word_boundary,
        newword_boundary,
        weak_boundary,
        deriv_boundary,
        morph_boundary,
        stub_boundary,
        optional_hyphen
        }
# some duplicates for symmetry:
fin_lowercase = "abcdefghijklmnopqrsštuvwxyzžåäö" + \
    "áàâãāăąçćĉċčđðďéèêëēĕęėěƒĝğġģȟħíìîïĩīĭįıĳĵķĸĺļľŀłñńņňŋ" + \
    "óòôōŏŕŗřśŝşſţťŧßþúùûüũūŭůųŵýŷÿűźżʒæøœőə"
fin_uppercase = "ABCDEFGHIJKLMNOPQRSŠTUVWXYZŽÅÄÖ" \
    "ÁÀÂÃĀĂĄÇĆĈĊČÐÐĎÉÈÊËĒĔĘĖĚƑĜĞĠĢȞĦÍÌÎÏĨĪĬĮİĲĴĶĸĹĻĽĿŁÑŃŅŇŊ" + \
    "ÓÒÔŌŎŔŖŘŚŜŞSŢŤŦßÞÚÙÛÜŨŪŬŮŲŴÝŶŸŰŹŻƷÆØŒŐƏ"
# asymmetric sets:
fin_lower_vowels = "aeiouyåäö" + \
    "áàâãāăąéèêëēĕęėěíìîïĩīĭįıóòôōŏúùûüũūŭůųýŷÿűæøœőə"
fin_upper_vowels = "AEIOUYÅÄÖ" \
    "ÁÀÂÃĀĂĄÉÈÊËĒĔĘĖĚÍÌÎÏĨĪĬĮİÓÒÔŌŎÚÙÛÜŨŪŬŮŲÝŶŰÆØŒŐƏ"
fin_vowels = fin_lower_vowels + fin_upper_vowels
fin_lower_consonants = "bcdfghjklmnpqrsštvwxzž" + \
    "çćĉċčđðďƒĝğġģȟħĵķĸĺļľŀłñńņňŉŋŕŗřśŝşſţťŧßþŵźżʒ"
fin_upper_consonants = "BCDFGHJKLMNPQRSŠTVWXZŽ" \
    "ÇĆĈĊČÐĎĜĞĠĢȞĦĴĶĹĻĽĿŁÑŃŅŇŊŔŖŘŚŜŞŢŤŦÞŴŹŻƷ"
fin_consonants = fin_lower_consonants + fin_upper_consonants
# the words containing symbols are likely weird / props etc.
fin_symbols = "1234567890§!\"#¤%&/()=?½@£$‚{[]}<>*"
# known variants and old orthographies 1:1
# (a conservative listing for sure)
fin_orth_pairs = [("’", "'"), ("’", "´"), ("’", "′"), ("-", "‐"),
        ("-", "‑"), ("-", "‑")]

# stuff is the tag format in database or lexical data, a lot of things
stuffs = {
        "",
        "ABBREVIATION",
        "ACRONYM",
        "ADJECTIVE",
        "ADPOSITION",
        "ADVERB",
        "ADVERBIAL",
        "Bc",
        "B-",
        "B←",
        "B→",
        "CARDINAL",
        "Ccmp",
        "CLAUSE-BOUNDARY",
        "Cma",
        "Cmaisilla",
        "Cmaton",
        "Cnut",
        "COMPARATIVE",
        "COMP",
        "CONJUNCTION",
        "COORDINATING",
        "Cpos",
        "Csup",
        "Cva",
        "DASH",
        "DECIMAL",
        "DEMONSTRATIVE",
        "DIGIT",
        "Din",
        "Dinen",
        "Dja",
        "Dma",
        "Dmaisilla",
        "Dmaton",
        "Dminen",
        "Dmpi",
        "Dnut",
        "Ds",
        "Dsti",
        "Dtattaa",
        "Dtatuttaa",
        "Dtava",
        "Dttaa",
        "Dtu",
        "Du",
        "Duus",
        "Dva",
        "FINAL-BRACKET",
        "FINAL-QUOTE",
        "FTB3man",
        "Ia",
        "Ie",
        "Ima",
        "Iminen",
        "INDEFINITE",
        "INITIAL-BRACKET",
        "INITIAL-QUOTE",
        "INTERJECTION",
        "INTERROGATIVE",
        "LEMMA-START",
        "Ncon",
        "Nneg", 
        "NOUN",
        "Npl", 
        "N??",
        "Nsg", 
        "NUMERAL",
        "O3",
        "Opl1",
        "Opl2",
        "ORDINAL",
        "Osg1",
        "Osg2",
        "PE4",
        "PERSONAL",
        "PL1", 
        "PL2",
        "PL3",
        "Ppe4", 
        "Ppl1", 
        "Ppl2",
        "Ppl3",
        "PREPOSITION",
        "PRONOUN",
        "PROPER",
        "Psg1", 
        "Psg2",
        "Psg3",
        "PUNCTUATION",
        "Qhan",
        "Qkaan",
        "Qka",
        "Qkin",
        "Qko",
        "Qpa",
        "Qs",
        "QUALIFIER",
        "QUANTOR",
        "RECIPROCAL",
        "REFLEXIVE",
        "RELATIVE",
        "ROMAN",
        ".sent",
        "SENTENCE-BOUNDARY",
        "SG1", 
        "SG2",
        "SG3",
        "SPACE",
        "SUPERL",
        "Tcond",
        "Timp", 
        "Topt",
        "Tpast",
        "Tpot", 
        "Tpres",
        "Uarch",
        "Udial",
        "Unonstd",
        "UNSPECIFIED",
        "Urare",
        "Vact",
        "VERB",
        "Vpss",
        "Xabe",
        "Xabl",
        "Xacc",
        "Xade",
        "Xall",
        "Xcom",
        "Xela",
        "Xess", 
        "Xgen",
        "Xill", 
        "Xine",
        "Xins",
        "Xlat",
        "X???",
        "Xnom",
        "Xpar", 
        "Xtra", 
        }

