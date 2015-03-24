#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to format apertium style analyses from omorfi data."""

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
#
#
# utils to format apertium style data from omorfi database values

from .settings import word_boundary, weak_boundary, \
        optional_hyphen
from .lexc_formatter import lexc_escape
from .error_logging import fail_formatting_missing_for

apertium_multichars =  {
 "-",
 "",
 "+",
 "a→adv",
 "adj",
 "abbr",
 "abe",
 "abl",
 "acc",
 "actv",
 "ade",
 "adv",
 "agent",
 "all",
 "ant",
 "card",
 "cnjcoo",
 "cnjcoo><vblex",
 "cnjsub",
 "cnjadv",
 "com",
 "cond",
 "conneg",
 "def",
 "dem",
 "ela",
 "enc",
 "ess",
 "f",
 "gen",
 "guio",
 "ij",
 "ill", 
 "imp", 
 "impers", 
 "ind",
 "ine",
 "infa",
 "infe",
 "infma",
 "infminen",
 "ins",
 "itg",
 "lat",
 "lpar",
 "lquot",
 "m",
 "mf",
 "n",
 "ND",
 "neg", 
 "nom",
 "np",
 "num",
 "ord",
 "p1", 
 "p2",
 "p3",
 "p1><pl", 
 "p1><sg", 
 "p2><pl",
 "p2><sg",
 "p3><pl",
 "p3><sg",
 "par", 
 "part",
 "past",
 "pasv",
 "pers",
 "pl", 
 "pneg",
 "pos",
 "post",
 "pot", 
 "pp",
 "pprs",
 "pri",
 "prn",
 "pxpl1",
 "pxpl2",
 "pxsg1",
 "pxsg2",
 "pxsp3",
 "qst",
 "qu",
 "rec",
 "reflex",
 "rel",
 "rpar",
 "rquot",
 "sent",
 "sg", 
 "sup",
 "top",
 "tra", 
 "vaux",
 "vblex",
 "v→a",
 "v→adv",
 "v→n"
        }
stuff2apertium =  {
        "ABBREVIATION": "abbr",
        "ACRONYM": "abbr",
        "ADJECTIVE": "adj",
        "ADPOSITION": "post",
        "ADVERB": "adv",
        "ADVERBIAL": "cnjadv",
        "AINF_arg": "vaux",
        "ARTWORK": "",
        "B-": "-",
        "B←": "-",
        "B→": "-",
        "Bc": "+",
        "CARDINAL": "card",
        "Ccmp": "com",
        "CLAUSE-BOUNDARY": "",
        "Cma": "agent",
        "Cmaton": "pneg",
        "Cnut": "pp",
        "COMPARATIVE": "cnjsub",
        "COMP": "com",
        "CONJUNCTION": "",
        "CONJUNCTIONVERB": "cnjcoo><vblex",
        "COORDINATING": "cnjcoo",
        "Cpos": "pos",
        "Csup": "sup",
        "CULTGRP": "",
        "Cva": "pprs",
        "DASH": "guio",
        "DECIMAL": "",
        "DEMONSTRATIVE": "dem",
        "DIGIT": "",
        "Din": "v→n", "Ds": "", "Du": "", "Dtava": "v→a",
        "Dma": "v→a", "Dinen": "", "Dja": "v→n", "Dmpi": "",
        "Dmaisilla": "v→adv",
        "Dminen": "v→n",
        "Dnut": "v→a", "Dtu": "v→a", "Duus": "", "Dva": "v→a", "Dmaton": "v→a",
        "Dttaa": "", "Dtattaa": "", "Dtatuttaa": "", "Dsti": "a→adv",
        "EVENT": "",
        "FINAL-BRACKET": "rpar",
        "FINAL-QUOTE": "rquot",
        "FIRST": "ant",
        "GEO": "top",
        "Ia": "infa",
        "Ie": "infe",
        "Ima": "infma",
        "Iminen": "infminen",
        "INDEFINITE": "ind",
        "INITIAL-BRACKET": "lpar",
        "INITIAL-QUOTE": "lquot",
        "INTRANSITIVE_arg": "vblex",
        "INTERJECTION": "ij",
        "INTERROGATIVE": "itg",
        "LAST": "ant",
        "LEMMA-START": "",
        "MAINF_arg": "vaux",
        "MEDIA": "",
        "MISC": "",
        "Ncon": "conneg",
        "N??": "ND",
        "Nneg": "neg", 
        "NOUN": "n",
        "Npl": "pl", 
        "Nsg": "sg", 
        "NUMERAL": "num",
        "O3": "pxsp3",
        "Opl1": "pxpl1",
        "Opl2": "pxpl2",
        "ORDINAL": "ord",
        "ORG": "",
        "Osg1": "pxsg1",
        "Osg2": "pxsg2",
        "PARTICLE": "part",
        "PERSONAL": "pers",
        "PL1": "p1", 
        "PL2": "p2",
        "PL3": "p3",
        "Ppe4": "impers", 
        "Ppl1": "p1><pl", 
        "Ppl2": "p2><pl",
        "Ppl3": "p3><pl",
        "PRONOUN": "prn",
        "PRODUCT": "",
        "PROPER": "np",
        "Psg1": "p1><sg", 
        "Psg2": "p2><sg",
        "Psg3": "p3><sg",
        "PUNCTUATION": "",
        "Qhan": "+han<enc",
        "Qkaan": "+kaan<enc",
        "Qka": "+ka<enc",
        "Qkin": "+kin<enc",
        "Qko": "+ko<qst",
        "Qpa": "+pa<enc",
        "Qs": "+s<enc",
        "QUALIFIER": "adj",
        "QUANTOR": "qu",
        "RECIPROCAL": "rec",
        "REFLEXIVE": "reflex",
        "RELATIVE": "rel",
        "ROMAN": "",
        ".sent": "",
        "SG1": "p1", 
        "SG2": "p2",
        "SG3": "p3",
        "SENTENCE-BOUNDARY": "sent",
        "SPACE": "",
        "SUPERL": "sup",
        "Tcond": "cond",
        "Timp": "imp", 
        "Topt": "",
        "Tpast": "past",
        "Tpot": "pot", 
        "Tpres": "pri",
        "Uarch": "",
        "Udial": "",
        "Unonstd": "",
        "UNSPECIFIED": "part",
        "Urare": "",
        "Vact": "actv",
        "VERB": "vblex",
        "Vpss": "pasv",
        "X???": "",
        "Xabe": "abe",
        "Xabl": "abl",
        "Xacc": "acc",
        "Xade": "ade",
        "Xall": "all",
        "Xcom": "com",
        "Xela": "ela",
        "Xess": "ess", 
        "Xgen": "gen",
        "Xill": "ill", 
        "Xine": "ine",
        "Xins": "ins",
        "Xlat": "lat",
        "Xnom": "nom",
        "Xpar": "par", 
        "Xtra": "tra", 
        "": ""
        }

def format_stuff_apertium(stuff):
    if len(stuff) == 0:
        return ""
    elif stuff in stuff2apertium:
        if stuff2apertium[stuff] in ['+', '-', '#', '0', '']:
            return stuff2apertium[stuff]
        elif stuff2apertium[stuff].startswith('+'):
            return (lexc_escape(stuff2apertium[stuff]) + '%>')
        else:
            return ('%<' + lexc_escape(stuff2apertium[stuff]) + '%>')
    else:
        fail_formatting_missing_for(stuff, "apertium")
        return ""

def format_analysis_lexc_apertium(anals):
    apestring = ''
    for i in anals.split('|'):
        apestring += format_stuff_apertium(i)
    return apestring

def format_continuation_lexc_apertium(anals, surf, cont):
    analstring = format_analysis_lexc_apertium(anals)
    if 'DIGITS_' in cont and not ('BACK' in cont or 'FRONT' in cont):
        analstring = lexc_escape(surf) + analstring
    surf = lexc_escape(surf)
    return "%s:%s\t%s ;\n" %(analstring, surf, cont)

def format_wordmap_lexc_apertium(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['lemma'])
    wordmap['analysis'] = wordmap['analysis'].replace(word_boundary, '+').replace(weak_boundary, '')
    if wordmap['is_suffix']:
        wordmap['analysis'] = "+" + wordmap['analysis']
    elif wordmap['is_prefix']:
        wordmap['analysis'] += "+"
     
    if wordmap['pos'] == 'NOUN':
        if wordmap['is_proper']:
            wordmap['analysis'] += '%<np%>'
            wordmap['analysis'] += format_stuff_apertium(wordmap['proper_noun_class'])
            if wordmap['sem'] in ['male', 'female']:
                wordmap['analysis'] += format_stuff_apertium(wordmap['sem'])
        else:
            wordmap['analysis'] += '%<n%>'
    elif wordmap['pos'] == 'VERB':
        if wordmap['argument']:
            wordmap['analysis'] += format_stuff_apertium(wordmap['argument'] + '_arg')
        else:
            wordmap['analysis'] += format_stuff_apertium(wordmap['pos'])
    elif wordmap['pos'] == 'CONJUNCTIONVERB':
        if wordmap['lemma'] == 'eikä':
            wordmap['lemma'] = 'ei'
            wordmap['analysis'] = 'ja' + \
                    format_stuff_apertium('COORDINATING') + \
                    '+ei' + \
                    format_stuff_apertium('Nneg')
        else:
            wordmap['analysis'] = wordmap['lemma'][:-2] +\
                    format_stuff_apertium('ADVERBIAL') + \
                    '+' + wordmap['lemma'][-2:] + \
                    format_stuff_apertium('Nneg')
    elif wordmap['particle']:
        for pclass in wordmap['particle'].split('|'):
            wordmap['analysis'] += format_stuff_apertium(pclass)
    else:
        wordmap['analysis'] += format_stuff_apertium(wordmap['pos'])

    if wordmap['pronoun']:
        for stuff in wordmap['pronoun'].split("|"):
            wordmap['analysis'] += format_stuff_apertium(stuff)
    if wordmap['adjective_class']:
        for stuff in wordmap['adjective_class'].split("|"):
            wordmap['analysis'] += format_stuff_apertium(stuff)
    if wordmap['noun_class']:
        for stuff in wordmap['noun_class'].split("|"):
            wordmap['analysis'] += format_stuff_apertium(stuff)
    if wordmap['numeral_class']:
        for stuff in wordmap['numeral_class'].split("|"):
            wordmap['analysis'] += format_stuff_apertium(stuff)
    if wordmap['symbol']:
        for subcat in wordmap['symbol'].split('|'):
            wordmap['analysis'] += format_stuff_apertium(subcat)
    retvals = ""
    wordmap['stub'] = wordmap['stub'].replace(word_boundary, optional_hyphen)
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    retvals += "%s:%s\t%s\t;\n" %(wordmap['analysis'], wordmap['stub'], 
            wordmap['new_para'])
    return retvals

def format_multichars_lexc_apertium():
    multichars = "!! Apertium standard tags:\n"
    for mcs in apertium_multichars:
        if not '><' in mcs and not mcs in ['', '+', '-', '#', '0']:
            multichars += '%<' + lexc_escape(mcs) + "%>\n"
    return multichars

# self test
if __name__ == '__main__':
    fail = False
    for stuff, ape in stuff2apertium.items():
        if len(ape) < 2:
            continue
        elif ape.startswith('+'):
            if not ape[ape.find('+'):]:
                print("There are conflicting formattings in here!", 
                        ape[ape.find('+'):],
                        "is not a valid apertium multichar_symbol!")
                fail = True
        elif not ape in apertium_multichars:
            print("There are conflicting formattings in here!", ape, 
                    "is not a valid apertium multichar_symbol!")
            fail = True
    if fail:
        exit(1)

