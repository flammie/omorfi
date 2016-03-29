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

from .error_logging import fail_formatting_missing_for, just_fail
from .formatter import Formatter
from .lexc_formatter import lexc_escape
from .settings import optional_hyphen, weak_boundary, word_boundary


class ApertiumFormatter(Formatter):
    apertium_multichars = {
        "-",
        "",
        "+",
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
        "cm",
        "com",
        "cond",
        "conneg",
        "def",
        "det",
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
        "loc",
        "lpar",
        "lquot",
        "m",
        "mf",
        "n",
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
        "use_dialect",
        "use_archaic",
        "use_nonstd",
        "use_foreign",
        "vaux",
        "vblex"
    }
    stuff2apertium = {
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
        "ADJ": "adj",
        "ADP": "post",
        "ADPOSITION": "post",
        "ADV": "adv",
        "ADVERB": "adv",
        "SCONJ": "cnjsub",
        "ADVERBIAL": "cnjadv",
        "AINF_arg": "vaux",
        "ARTWORK": "",
        "ARROW": "",
        "AUX": "vaux",
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
        "COMMA": "cm",
        "COMPARATIVE": "cnjsub",
        "COMP": "com",
        "CONJUNCTION": "",
        "CONJUNCTIONVERB": "cnjcoo><vblex",
        "CONJ": "cnjcoo",
        "COORDINATING": "cnjcoo",
        "Cpos": "pos",
        "Csup": "sup",
        "CULTGRP": "",
        "Cva": "pprs",
        "DASH": "guio",
        "DECIMAL": "",
        "DERSTI": "",
        "DERTTAIN": "",
        "DET": "det",
        "DEMONSTRATIVE": "dem",
        "DIGIT": "",
        "Din": "+in<n",
        "Ds": "",
        "Du": "+u<n",
        "Dtava": "+tava<adj",
        "Dma": "+ma<n",
        "Dinen": "+inen<n",
        "Dja": "+ja<n",
        "Dmpi": "+mpi<adj",
        "Dmaisilla": "+maisilla<adv",
        "Dminen": "+minen<n",
        "Dnut": "+nut<adj",
        "Dtu": "+tu<adj",
        "Duus": "+uus<adj",
        "Dva": "+va<adj",
        "Dmaton": "+maton<adj",
        "Dttain": "+ttain<adv",
        "Dttaa": "+ttaa<vblex",
        "Dtattaa": "+tattaa<vblex",
        "Dtatuttaa": "+tatuttaa<vblex",
        "Dsti": "+sti<adv",
        "EVENT": "",
        "FEMALE": "f",
        "FINAL-BRACKET": "rpar",
        "FINAL-QUOTE": "rquot",
        "FIRST": "ant",
        "FRACTION": "",
        "GEO": "top",
        "Ia": "infa",
        "Ie": "infe",
        "Ima": "infma",
        "Iminen": "infminen",
        "INDEFINITE": "ind",
        "INITIAL-BRACKET": "lpar",
        "INITIAL-QUOTE": "lquot",
        "INTRANSITIVE_arg": "vblex",
        "INTJ": "ij",
        "INTERROGATIVE": "itg",
        "LAST": "ant",
        "LEMMA-START": "",
        "MALE": "m",
        "MAINF_arg": "vaux",
        "MEDIA": "",
        "MISC": "",
        "MULTIPLICATIVE": "",
        "Ncon": "conneg",
        "N??": "",
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
        "PRON": "prn",
        "PRODUCT": "",
        "PROPN": "np",
        "PROPER": "np",
        "Psg1": "p1><sg",
        "Psg2": "p2><sg",
        "Psg3": "p3><sg",
        "PUNCT": "",
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
        "SUFFIX": "",
        "SUPERL": "sup",
        "SYM": "",
        "Tcond": "cond",
        "Timp": "imp",
        "Topt": "",
        "Tpast": "past",
        "Tpot": "pot",
        "Tpres": "pri",
        "Uarch": "use_archaic",
        "Udial": "use_nonstd",
        "Unonstd": "use_nonstd",
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
        "ADESSIVE": "ade",
        "ABLATIVE": "abl",
        "ALLATIVE": "all",
        "INESSIVE": "ine",
        "ILLATIVE": "ill",
        "LOCATIVE": "loc",
        "FTB3MAN": "",
        "FTB3man": "",
        ".": "",
        "XForeign": "use_foreign",
        "X": "",
        "": ""
    }

    def __init__(self, verbose=True):
        self.verbose = verbose
        for stuff, ape in self.stuff2apertium.items():
            if len(ape) < 2:
                continue
            elif ape.startswith('+'):
                if not ape[ape.find('+'):]:
                    just_fail("There are conflicting formattings in here! " +
                              ape[ape.find('+'):] +
                              " is not a valid apertium multichar_symbol!")
            elif ape not in self.apertium_multichars:
                just_fail("There are conflicting formattings in here! " + ape +
                          " is not a valid apertium multichar_symbol!")

    def stuff2lexc(self, stuff):
        if len(stuff) == 0:
            return ""
        elif stuff in self.stuff2apertium:
            if self.stuff2apertium[stuff] in ['+', '-', '#', '0', '']:
                return self.stuff2apertium[stuff]
            elif self.stuff2apertium[stuff].startswith('+'):
                return (lexc_escape(self.stuff2apertium[stuff]) + '%>')
            else:
                return ('%<' + lexc_escape(self.stuff2apertium[stuff]) + '%>')
        else:
            fail_formatting_missing_for(stuff, "apertium")
            return ""

    def analyses2lexc(self, anals):
        apestring = ''
        for i in anals.split('|'):
            apestring += self.stuff2lexc(i)
        return apestring

    def continuation2lexc(self, anals, surf, cont):
        analstring = self.analyses2lexc(anals)
        # the followings have surface fragments in continuations
        if 'DIGITS_' in cont and not ('BACK' in cont or 'FRONT' in cont):
            analstring = lexc_escape(surf) + analstring
        elif 'PUNCT_NONSTD_EXCL_LOOP' in cont or 'PUNCT_NONSTD_DASH_LOOP' in cont:
            analstring = lexc_escape(surf) + analstring
        surf = lexc_escape(surf)
        return "%s:%s\t%s ;\n" % (analstring, surf, cont)

    def wordmap2lexc(self, wordmap):
        if wordmap['lemma'] == ' ':
            # apertium fails when surf == ' '
            return ''
        wordmap['analysis'] = lexc_escape(wordmap['lemma'])
        wordmap['analysis'] = wordmap['analysis'].replace(
            word_boundary, '+').replace(weak_boundary, '')
        if wordmap['is_suffix']:
            wordmap['analysis'] = "+" + wordmap['analysis']
        elif wordmap['is_prefix']:
            wordmap['analysis'] += "+"
        elif wordmap['upos'] == 'PROPN':
            wordmap['analysis'] += this.stuff2lexc(wordmap['upos'])
            if wordmap['proper_noun_class']:
                wordmap['analysis'] +=\
                        this.stuff2lexc(wordmap['proper_noun_class'])
                if wordmap['sem'] in ['MALE', 'FEMALE']:
                    wordmap['analysis'] += this.stuff2lexc(wordmap['sem'])
        elif wordmap['upos'] == 'VERB':
            if wordmap['argument']:
                wordmap[
                    'analysis'] += self.stuff2lexc(wordmap['argument'] + '_arg')
            else:
                wordmap['analysis'] += this.stuff2lexc(wordmap['upos'])
        elif wordmap['upos'] == 'CONJ|VERB':
            if wordmap['lemma'] == 'eikä':
                wordmap['lemma'] = 'ei'
                wordmap['analysis'] = 'ja' + \
                    self.stuff2lexc('COORDINATING') + \
                    '+ei' + \
                    self.stuff2lexc('Nneg')
            else:
                wordmap['analysis'] = wordmap['lemma'][:-2] +\
                    self.stuff2lexc('ADVERBIAL') + \
                    '+' + wordmap['lemma'][-2:] + \
                    self.stuff2lexc('Nneg')
        elif wordmap['particle']:
            for pclass in wordmap['particle'].split('|'):
                wordmap['analysis'] += self.stuff2lexc(pclass)
        else:
            wordmap['analysis'] += this.stuff2lexc(wordmap['upos'])
        if wordmap['pronoun']:
            for stuff in wordmap['pronoun'].split("|"):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['lex']:
            for stuff in wordmap['lex'].split("|"):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['abbr']:
            for stuff in wordmap['abbr'].split("|"):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['numtype']:
            for stuff in wordmap['numtype'].split("|"):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['symbol']:
            for subcat in wordmap['symbol'].split('|'):
                wordmap['analysis'] += self.stuff2lexc(subcat)
            if wordmap['stub'] in ";:":
                wordmap['analysis'] += self.stuff2lexc("SENTENCE-BOUNDARY")
        # XXX: for now
        if wordmap['lemma'] in "¹²³½¼=≥µ#/%":
            wordmap['analysis'] += self.stuff2lexc("NOUN")
        retvals = ""
        wordmap['stub'] = wordmap['stub'].replace(
            word_boundary, optional_hyphen)
        wordmap['stub'] = lexc_escape(wordmap['stub'])
        retvals += "%s:%s\t%s\t;" % (wordmap['analysis'], wordmap['stub'],
                                       wordmap['new_para'])
        return retvals

    def multichars_lexc(self):
        multichars = "Multichar_Symbols\n!! Apertium standard tags:\n"
        for mcs in sorted(self.apertium_multichars):
            if not '><' in mcs and not mcs in ['', '+', '-', '#', '0']:
                multichars += '%<' + lexc_escape(mcs) + "%>\n"
        multichars += Formatter.multichars_lexc(self)
        return multichars

    def root_lexicon_lexc(self):
        root = Formatter.root_lexicon_lexc(self)
        return root

# self test
if __name__ == '__main__':
    formatter = ApertiumFormatter()
    exit(0)
