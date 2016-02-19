#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to format apertium monodix from omorfi data."""

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
# utils to format apertium style data from omorfi database values

from .settings import word_boundary, weak_boundary, \
    optional_hyphen
from .error_logging import fail_formatting_missing_for

monodix_sdefs = {
    'abbr',
    'abe',
    'abl',
    'acc',
    'actv',
    'ade',
    'adj',
    'agent',
    'all',
    'ant',
    'card',
    'cmp',
    'cnjcoo',
    'cnjsub',
    'com',
    'comp',
    'cond',
    'conneg',
    'dem',
    'ela',
    'enc',
    'ess',
    'f',
    'gen',
    'ij',
    'ill',
    'imp',
    'impers',
    'ind',
    'indv',
    'ine',
    'infa',
    'infe',
    'infma',
    'infminen',
    'ins',
    'itg',
    'lat',
    'm',
    'mf',
    'n',
    'neg',
    'nom',
    'np',
    'nt',
    'num',
    'ord',
    'p1',
    'p2',
    'p3',
    'par',
    'part',
    'past',
    'pasv',
    'pl',
    'pneg',
    'pos',
    'post',
    'pot',
    'pp',
    'pprs',
    'pr',
    'pres',
    'prn',
    'pxpl1',
    'pxpl2',
    'pxsg1',
    'pxsg2',
    'pxsp3',
    'qst',
    'rec',
    'reflex',
    'rel',
    'sg',
    'sup',
    'top',
    'tra',
    'vblex',
    'ND'}

stuff2monodix = {
    "Aiden": "",
    "Aien": "",
    "Aiin": "",
    "Ain": "",
    "Ayn": "",
    "Aän": "",
    "Aön": "",
    "Aisiin": "",
    "Aseen": "",
    "Aä": "",
    "Ajä": "",
    "Atä": "",
    "Ajen": "",
    "Aten": "",
    "Ahin": "",
    "Ahen": "",
    "Ahyn": "",
    "Aihin": "",
    "Aiä": "",
    "Ana": "",
    "Asa": "",
    "Aitten": "",
    "Aan": "",
    "Aen": "",
    "Ahan": "",
    "Ahon": "",
    "Ahun": "",
    "Aon": "",
    "Aun": "",
    "Aa": "",
    "Aia": "",
    "Aita": "",
    "Aja": "",
    "Ahän": "",
    "Ahön": "",
    "Aitä": "",
    "Ata": "",
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
    "Dinen": "+inen<adj>",
    "Din": "+in<n>",
    "Dja": "+ja<n>",
    "Dmaisilla": "+maisilla<adv>",
    "Dma": "+ma<n>",
    "Dmaton": "+maton<adj>",
    "Dminen": "+minen<n>",
    "Dmpi": "+mpi<adj>",
    "Dnut": "+nut<adj>",
    "Ds": "+s<n>",
    "Dsti": "+sti<adv>",
    "Dtattaa": "+tattaa<vblex>",
    "Dtatuttaa": "+tatuttaa<vblex>",
    "Dtava": "+tava<adj>",
    "Dttaa": "+ttaa<vblex>",
    "Dttain": "+ttain<adv>",
    "Dtu": "+tu<adj>",
    "Du": "+u<n>",
    "Duus": "+uus<n>",
    "Dva": "+va<a>",
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
    "NUM": "num",
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
    ".": "",
    "": ""
}


def format_monodix_licence():
    return """<!--
  Copyright (c) 2014 Omorfi contributors

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, version 3 of the License

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
-->"""


def format_monodix_alphabet():
    """Finnish alphabet as in CLDR 24"""
    return ("<alphabet>abcdefghijklmnopqrsštuvwxyzžåäö"
            "ABCDEFGHIJKLMNOPQRSŠTUVWXYZŽ"
            "áàâãčçđéèêëǧǥȟíîïǩńñŋôõœřßŧúùûÿüʒǯæø"
            "ÁÀÂÃČÇÐÉÈÊËǦÍÎÏĸŃÑŊÔÕŘÚÙÛŸÜƷǮÆØ"
            "</alphabet>")


def format_monodix_sdefs():
    sdefs = '  <sdefs>\n'
    for sdef in monodix_sdefs:
        sdefs += '    <sdef n="' + sdef + '"/>\n'
    sdefs += '  </sdefs>\n'
    return sdefs


def format_monodix_l(s):
    if s != '0':
        return s.replace(' ', '<b/>').replace(word_boundary, '')
    else:
        return ''


def format_monodix_r(anals):
    r = ''
    if anals != '0':
        for anal in anals.split('|'):
            r += format_monodix_s(anal)
    return r


def format_monodix_s(stuff):
    s = ''
    if stuff in stuff2monodix:
        s += '<s n="' + stuff2monodix[stuff] + '"/>'
    else:
        fail_formatting_missing_for(stuff, "monodix")
    if '><' in s:
        s = s.replace('><', '"/><s n="')
    elif '"+"' in s:
        s = '+'
    elif '""' in s:
        s = ''
    elif '"-"' in s:
        s = '-'
    return s


def format_monodix_par(cont):
    return '<par n="' + cont.lower().replace('_', '__') + '"/>'


def format_monodix_pardef(fields):
    pardef = ''
    for cont in fields[3:]:
        pardef += '      <e>'
        if fields[1] == fields[2]:
            pardef += '<i>' + format_monodix_l(fields[2]) + '</i>'
        else:
            pardef += '<p><l>' + format_monodix_l(fields[2]) + '</l>'
            pardef += '<r>' + format_monodix_r(fields[1]) + '</r></p>'
        if cont != '#':
            pardef += format_monodix_par(cont)
        pardef += '</e>\n'
    return pardef


def format_monodix_entry(wordmap):
    e = '<e lm="' + wordmap['lemma'].replace('&', '&amp;') + '">'
    e += '<p><l>' + \
        wordmap['stub'].replace(word_boundary, '').replace(
            '&', '&amp;') + '</l>'
    e += '<r>'
    e += wordmap['lemma'].replace('&', '&amp;')
    e += format_monodix_s(wordmap['real_pos'] or wordmap['pos'])
    e += '</r></p>'
    e += format_monodix_par(wordmap['new_para'])
    e += '</e>'
    return e

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
