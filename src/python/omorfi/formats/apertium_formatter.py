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

from ..error_logging import fail_formatting_missing_for, just_fail
from .formatter import Formatter
from ..settings import weak_boundary, word_boundary
from ..string_manglers import lexc_escape


class ApertiumFormatter(Formatter):
    """Formatter that handles conversions for apertium's conventions."""

    ## All apertium multichar symbols
    apertium_multichars = {
        "-",
        "",
        "+",
        "adj",
        "abbr",
        "abe",
        "abl",
        "acc",
        "acr",
        "actv",
        "ade",
        "adv",
        "agent",
        "al",
        "all",
        "ant",
        "card",
        "cnjcoo",
        "cnjcoo><vblex",
        "cnjsub",
        "cnjadv",
        "cog",
        "com",
        "comp",
        "cni",
        "conneg",
        "cmp",
        "cmp-split",
        "compound-only-L",
        "compound-R",
        "def",
        "det",
        "dem",
        "ela",
        "enc",
        "ess",
        "f",
        "gen",
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
        "m",
        "mf",
        "n",
        "neg",
        "nom",
        "np",
        "num",
        "ord",
        "org",
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
        "pst",
        "post",
        "pot",
        "pp",
        "pprs",
        "pri",
        "prn",
        "punct",
        "px1pl",
        "px2pl",
        "px1sg",
        "px2sg",
        "px3sp",
        "qst",
        "qu",
        "rec",
        "reflex",
        "rel",
        "sg",
        "sp",
        "sup",
        "sym",
        "top",
        "tra",
        "use_dialect",
        "use_archaic",
        "use_nonstd",
        "use_foreign",
        "use_blacklist",
        "vaux",
        "vblex"
    }
    ## a mapping from omorfi stuff to apertium symbols
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
        "ACRONYM": "acr",
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
        "B-": "cmp-split",
        "Bxxx": "compound-only-L",
        "B←": "compound-only-L",
        "B→": "compound-R",
        "Bc": "cmp>+",
        "BLACKLISTED": "use_blacklist",
        "CARDINAL": "card",
        "Ccmp": "comp",
        "CLAUSE-BOUNDARY": "",
        "Cma": "agent",
        "Cmaton": "pneg",
        "Cnut": "pp",
        "COMMA": "",
        "COMPARATIVE": "cnjsub",
        "COMP": "",
        "CONJUNCTION": "",
        "CONJUNCTIONVERB": "cnjcoo><vblex",
        "CONJ": "cnjcoo",
        "CCONJ": "cnjcoo",
        "COORDINATING": "cnjcoo",
        "Cpos": "pst",
        "Csup": "sup",
        "CULTGRP": "al",
        "Cva": "pprs",
        "DASH": "",
        "DECIMAL": "",
        "DERSTI": "",
        "DERTTAIN": "",
        "DET": "det",
        "DEMONSTRATIVE": "dem",
        "DIGIT": "",
        "Din": "+in<n",
        "Din²": "",
        "Ds": "+s<n",
        "Dhko": "+hko<adj",
        "Disa": "+isa<adj",
        "Dllinen": "+llinen<n",
        "Dlainen": "+lainen<n",
        "Dla": "+la<n",
        "Dnen": "+nen<n",
        "Dtar": "+tar<n",
        "Dton": "+ton<adj",
        "Dmainen": "+mainen<adj",
        "Du": "+u<n",
        "Dtava": "+tava<adj",
        "Dma": "+ma<n",
        "Dinen": "+inen<n",
        "Dja": "+ja<n",
        "Dmpi": "",
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
        "Dtuttaa": "+tuttaa<vblex",
        "Dsti": "+sti<adv",
        "EVENT": "",
        "FEMALE": "f",
        "FINAL-BRACKET": "",
        "FINAL-QUOTE": "",
        "FIRST": "ant",
        "FRACTION": "",
        "GEO": "top",
        "Ia": "infa",
        "Ie": "infe",
        "Ima": "infma",
        "Iminen": "infminen",
        "INDEFINITE": "ind",
        "INITIAL-BRACKET": "",
        "INITIAL-QUOTE": "",
        "INTRANSITIVE_arg": "vblex",
        "INTJ": "ij",
        "INTERROGATIVE": "itg",
        "LAST": "cog",
        "LEMMA-START": "",
        "LEMMA-END": "",
        "MALE": "m",
        "MAINF_arg": "vaux",
        "MEDIA": "al",
        "MISC": "al",
        "MULTIPLICATIVE": "",
        "Ncon": "conneg",
        "N??": "sp",
        "Nneg": "neg",
        "NOUN": "n",
        "Npl": "pl",
        "Nsg": "sg",
        "NUM": "num",
        "NUMERAL": "num",
        "O3": "px3sp",
        "Opl1": "px1pl",
        "Opl2": "px2pl",
        "ORDINAL": "ord",
        "ORD": "ord",
        "ORG": "org",
        "UNKNOWNPROPN": "al",
        "Osg1": "px1sg",
        "Osg2": "px2sg",
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
        "PRODUCT": "al",
        "PROPN": "np",
        "PROPER": "np",
        "Psg1": "p1><sg",
        "Psg2": "p2><sg",
        "Psg3": "p3><sg",
        "Psg0": "p3><sg",
        "PUNCT": "punct",
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
        "SG0": "p3",
        "SENTENCE-BOUNDARY": "",
        "SPACE": "",
        "SUFFIX": "",
        "SUPERL": "sup",
        "SYM": "sym",
        "Tcond": "cni",
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
        "X": "x",
        "": ""
    }

    def __init__(self, verbose=True):
        """Create an apertium formatter with given verbosity.

        @param verbose  set to false to disable stdout logging
        """
        ## verbosity, i.e. print while translating
        super().__init__(verbose)
        self.verbose = verbose
        for _, ape in self.stuff2apertium.items():
            if len(ape) < 2:
                continue
            elif ape.startswith('+'):
                if not ape[ape.find('+'):]:
                    just_fail("There are conflicting formattings in here! " +
                              ape[ape.find('+'):] +
                              " is not a valid apertium multichar_symbol!")
            elif ape.endswith('+'):
                if not ape[:ape.find('+')]:
                    just_fail("There are conflicting formattings in here! " +
                              ape[ape.find('+'):] +
                              " is not a valid apertium multichar_symbol!")
            elif ape not in self.apertium_multichars:
                just_fail("There are conflicting formattings in here! " + ape +
                          " is not a valid apertium multichar_symbol!")

    def stuff2lexc(self, stuff):
        """Get apertium analyses in lexc format corresponding omorfi stuff.

        @return str containing lexc formatted analysis tag(s)
        """
        if not stuff:
            return ""
        elif stuff in self.stuff2apertium:
            if self.stuff2apertium[stuff] in ['+', '-', '#', '0', '']:
                return self.stuff2apertium[stuff]
            elif self.stuff2apertium[stuff].startswith('+'):
                return lexc_escape(self.stuff2apertium[stuff]) + '%>'
            elif self.stuff2apertium[stuff].endswith('+'):
                return '%<' + lexc_escape(self.stuff2apertium[stuff])
            else:
                return '%<' + lexc_escape(self.stuff2apertium[stuff]) + '%>'
        else:
            fail_formatting_missing_for(stuff, "apertium")
            return "%<error%>"

    def analyses2lexc(self, anals, surf):
        """Get full analysis string in lexc for omorfi analyses.

        @return str containing lexc-formatted analysi tags and potential lemma
                fragments
        """
        apestring = ''
        for i in anals.split('|'):
            if i == '@@COPY-STEM@@':
                apestring += lexc_escape(surf)
            elif i.startswith('@@LITERAL') and i.endswith('@@'):
                apestring += lexc_escape(i[len('@@LITERAL'):-len('@@')])
            else:
                apestring += self.stuff2lexc(i)
        return apestring

    def continuation2lexc(self, anals, surf, cont):
        """Get lexc representation for omorfi continuation lexicon."""
        analstring = self.analyses2lexc(anals, surf)
        surf = lexc_escape(surf)
        return "%s:%s\t%s ;\n" % (analstring, surf, cont)

    def wordmap2lexc(self, wordmap):
        """Get lexc representation of omorfi lexeme in a wordmap.

        @return lexc-formatted entries for the word
        """
        if wordmap['lemma'] == ' ':
            # apertium fails when surf == ' '
            return ''
        wordmap['analysis'] = lexc_escape(wordmap['lemma'])
        wordmap['analysis'] = wordmap['analysis'].replace(
            word_boundary, '+').replace(weak_boundary, '')
        if wordmap['is_prefix']:
            wordmap['analysis'] += "+"
        elif wordmap['upos'] == 'PROPN':
            wordmap['analysis'] += self.stuff2lexc(wordmap['upos'])
            if wordmap['proper_noun_class']:
                wordmap['analysis'] +=\
                    self.stuff2lexc(wordmap['proper_noun_class'])
                if wordmap['sem'] in ['MALE', 'FEMALE']:
                    wordmap['analysis'] += self.stuff2lexc(wordmap['sem'])
            else:
                wordmap['analysis'] += self.stuff2lexc('UNKNOWNPROPN')
        elif wordmap['upos'] == 'VERB':
            if wordmap['argument']:
                wordmap[
                    'analysis'] += self.stuff2lexc(wordmap['argument'] +
                                                   '_arg')
            else:
                wordmap['analysis'] += self.stuff2lexc(wordmap['upos'])
        elif wordmap['upos'] == 'CCONJ|VERB':
            if wordmap['lemma'] == 'eikä':
                wordmap['lemma'] = 'ei'
                wordmap['analysis'] = 'ja' + \
                    self.stuff2lexc('COORDINATING') + \
                    '+ei' + \
                    self.stuff2lexc('Nneg')
            else:
                wordmap['analysis'] = wordmap['lemma'][:-2] + \
                    self.stuff2lexc('ADVERBIAL') + \
                    '+' + wordmap['lemma'][-2:] + \
                    self.stuff2lexc('Nneg')
        elif wordmap['particle']:
            for pclass in wordmap['particle'].split(','):
                wordmap['analysis'] += self.stuff2lexc(pclass)
        else:
            wordmap['analysis'] += self.stuff2lexc(wordmap['upos'])
        if wordmap['blacklist']:
            if wordmap['blacklist'] != "TOOSHORTFORCOMPOUND":
                wordmap['analysis'] += self.stuff2lexc('BLACKLISTED')

        if wordmap['pronoun']:
            for stuff in wordmap['pronoun'].split(","):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['lex']:
            for stuff in wordmap['lex'].split(","):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['abbr']:
            for stuff in wordmap['abbr'].split(","):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['numtype']:
            for stuff in wordmap['numtype'].split(","):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['symbol']:
            for subcat in wordmap['symbol'].split(','):
                wordmap['analysis'] += self.stuff2lexc(subcat)
            if wordmap['stub'] in ";:":
                wordmap['analysis'] += self.stuff2lexc("SENTENCE-BOUNDARY")
        # XXX: for now
        if wordmap['lemma'] in "¹²³½¼=≥µ#/%":
            wordmap['analysis'] += self.stuff2lexc("NOUN")
        wordmap['stub'] = wordmap['stub']
        wordmap['stub'] = lexc_escape(wordmap['stub'])
        if 'BLACKLIST' in wordmap['new_para']:
            return "!%s:%s\t%s\t;" % (wordmap['analysis'], wordmap['stub'],
                                      wordmap['new_para'])
        else:
            return "%s:%s\t%s\t;" % (wordmap['analysis'], wordmap['stub'],
                                     wordmap['new_para'])

    def multichars_lexc(self):
        """Get apertium compatible lexc multichars.

        @return str containing lexc multichar_symbols block for apertium tags
        """
        multichars = "Multichar_Symbols\n!! Apertium standard tags:\n"
        for mcs in sorted(self.apertium_multichars):
            if '><' not in mcs and mcs not in ['', '+', '-', '#', '0']:
                multichars += '%<' + lexc_escape(mcs) + "%>\n"
        multichars += Formatter.multichars_lexc(self)
        return multichars

    def root_lexicon_lexc(self):
        """Get apertium compatible lexc root.

        @return str containing lexc Root lexicon for apertium"""
        root = Formatter.root_lexicon_lexc(self)
        root += '\t'.join(['-', 'SUFFIX', ';']) + '\n'
        root += '\t'.join(['-', 'NOUN', ';']) + '\n'
        root += '\t'.join(['-', 'ADJ', ';']) + '\n'
        return root


# self test
if __name__ == '__main__':
    formatter = ApertiumFormatter()
    exit(0)
