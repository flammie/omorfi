#!/bin/python3
# -*- coding: utf-8 -*-
"""Global settings for omorfi.

Includes special symbols, definitions of alphabets and their subsets,
and alphabet pairs as well as internal keywords.
"""

# Author: Omorfi contributors <omorfi-devel@groups.google.com> 2015

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


# common symbols for all
version_id_easter_egg = 'OMORFI_VERSION_≥_15_©_GNU_GPL_V3'
word_boundary = "{WB}"
newword_boundary = "{wB}"
weak_boundary = "{XB}"
deriv_boundary = "{DB}"
morph_boundary = "{MB}"
stub_boundary = "{STUB}"
optional_hyphen = "{hyph?}"
common_multichars = {
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
# punctuation characters one may optionally split without space after the word
fin_punct_trailing = "\"'.,?!)]}’”–:;»>"
# punctuations chopped of at the beginning of the word
fin_punct_leading = "\"'<([{’”-–»>"
# known variants and old orthographies 1:1
# (a conservative listing for sure)
fin_orth_pairs = [("’", "'"), ("’", "´"), ("’", "′"), ("-", "‐"),
                  ("-", "‑"), ("-", "‑")]
# weights by rules
stuff_weights = {'Bc': '+1.0',
                 'Duus': '+16.0', 'Dttaa': '+16.0',
                 'Dtattaa': '+16.0', 'Dtatuttaa': '+32.0', 'Dinen': '+1.0',
                 'Dja': '+2.0', 'Du': '+16.0',
                 'Uarch': '+16.0',
                 'Udial': '+2.0', 'Urare': '+4.0', 'Unonstd': '+4.0',
                 'Xabe': '+0.1', 'Xcom': '+1.0', 'Xins': '+2.0',
                 'Qhan': '+1.0', 'Qpa': '+1.0', 'Qkin': '+1.0',
                 'Qkaan': '+1.0'
                 }
boundary_weights = {word_boundary: '+0.1', morph_boundary: '+0.1',
                    newword_boundary: '+1.0', deriv_boundary: '+2.0',
                    weak_boundary: '+0.1', stub_boundary: '+0.1'}

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
