#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to format giellatekno style analyses from omorfi data."""

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

from ..error_logging import fail_formatting_missing_for, just_fail
from .formatter import Formatter
from ..settings import (deriv_boundary, morph_boundary, stub_boundary,
                        weak_boundary, word_boundary)
from ..string_manglers import lexc_escape


class GiellaFormatter(Formatter):
    """Formatter that handles conversions to giellatekno.uit.no conventions."""

    ## Giellatekno style analysis tags
    giella_multichars = {
        '+A',
        '+ABBR',
        '+Abe',
        '+Abl',
        '+Acc',
        '+Act',
        '+ACR',
        '+Ade',
        '+Adp',
        '+Adp+Po',
        '+Adp+Pr',
        '+Adv',
        '+AgPrc',
        '+All',
        '+Card',
        '+CC',
        '+Com',
        '+Comp',
        '+Cmp',
        '+Cond',
        '+ConNeg',
        '+CS',
        '+Dash',
        '+Dem',
        "+Dem",
        '+Der/inint',
        '+Der/nen',
        '+Der/inen',
        '+Der/hko',
        '+Der/ja',
        '+Der/lainen',
        '+Der/llinen',
        '+Der/maisilla',
        '+Der/minen',
        '+Der/nti',
        '+Der/sti',
        "+Der/sti",
        '+Der/tar',
        '+Der/tattaa',
        '+Der/tatuttaa',
        '+Der/tuttaa',
        '+Der/mainen',
        '+Der/isa',
        '+Der/ton',
        '+Der/tse',
        '+Der/ttaa',
        '+Der/ttain',
        '+Der/u',
        '+Der/uus',
        '+Der/vs',
        '+Dial/Finland',
        '+Dial/East',
        '+Dial/Eteläpohjalaiset',
        '+Dial/Häme',
        '+Dial/Keskipohjalaiset',
        '+Dial/North',
        '+Dial/Peräpohjalaiset',
        '+Dial/Savo',
        '+Dial/Southeast',
        '+Dial/Southwest',
        '+Dial/Standard',
        '+Dial/West',
        '+Digit',
        '+Ela',
        '+Err/Orth',
        '+Err/Sub',
        '+Ess',
        '+Foc/han',
        '+Foc/ka',
        '+Foc/kaan',
        '+Foc/kin',
        '+Foc/ko',
        '+Foc/pa',
        '+Foc/s',
        '+Gen',
        '+Ill',
        '+Impv',
        "+Indef",
        '+Ine',
        '+InfA',
        '+InfE',
        '+InfMA',
        '+Inf1',
        '+Inf2',
        '+Inf3',
        '+Ins',
        '+Interj',
        '+Interr',
        "+Interr",
        '+Lat',
        '+Man',
        '+N',
        '+N+Abbr',
        '+Neg',
        '+NegPrc',
        '+Nom',
        '+Num',
        '+OLang/eng',
        '+Opt',
        '+Ord',
        '+Par',
        '+Pass',
        '+Pcle',
        '+Pe4',
        '+Pers',
        "+Pers",
        '+Pl',
        '+Pl1',
        '+Pl2',
        '+Pl3',
        '+Po',
        '+Pos',
        '+Pot',
        '+Pr',
        '+Pref',
        '+PrfPrc',
        '+PrfPrc+Act',
        '+PrfPrc+Pass',
        '+Pron',
        '+Prop',
        '+Prs',
        '+PrsPrc',
        '+PrsPrc+Act',
        '+PrsPrc+Pass',
        '+Prt',
        '+Pst',
        '+Punct',
        '+PxPl1',
        '+PxPl2',
        '+PxPl3',
        '+PxSg1',
        '+PxSg2',
        '+PxSg3',
        '+Px3',
        "+Qnt",
        '+Qst',
        '+Qu',
        '+Quote',
        '+Refl',
        "+Refl",
        '+Rel',
        "+Rel",
        '+Roman',
        '+Sem/Geo',
        '+Sem/Human',
        '+Sem/Org',
        '+Sg',
        '+Sg1',
        '+Sg2',
        '+Sg3',
        '+Suff',
        '+Superl',
        '+Tra',
        '+Trunc',
        '+TruncPrefix',
        'TruncSuffix+',
        '+Use/Arch',
        '+Use/Circ',
        '+Use/Marg',
        '+Use/Rare',
        '+V'
    }

    ## Omorfi to giellatekno tag mapping
    stuff2giella = {"Bc": "#",
                    ".": "",
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
                    "ABBREVIATION": "+ABBR",
                    "ABLATIVE": "+Abl",
                    "ACRONYM": "+ACR",
                    "ADESSIVE": "+Ade",
                    "ADJECTIVE": "+A",
                    "ADPOSITION": "+Adp+Po",
                    "ADVERB": "+Adv",
                    "ADVERBIAL": "+CS",
                    "ALLATIVE": "+All",
                    "ARROW": "",
                    "ARTWORK": "",
                    "B-": "+Trunc",
                    "B←": "+TruncPrefix",
                    "B→": "TruncSuffix+",
                    "CARDINAL": "",
                    "Ccmp": "+Comp",
                    "CLAUSE-BOUNDARY": "",
                    "Cma": "+AgPrc",
                    "Cmaisilla": "+Der/maisilla",
                    "Cmaton": "+NegPrc",
                    "Cnut": "+PrfPrc",
                    "COMMA": "",
                    "COMPARATIVE": "+CS",
                    "COMP": "+Comp",
                    "CONJUNCTION": "",
                    "COORDINATING": "+CC",
                    "Cpos": "+Pos",
                    "Csup": "+Superl",
                    "CULTGRP": "+Sem/Human",
                    "Cva": "+PrsPrc",
                    "DASH": "+Dash",
                    "DECIMAL": "",
                    "DEMONSTRATIVE": "+Dem",
                    "DERSTI": "+Der/sti",
                    "DERTTAIN": "+Der/ttain",
                    "DIGIT": "+Digit",
                    "Dinen": "+Der/inint",
                    "Din": "+Superl",
                    "Dja": "+Der/ja",
                    "Dma": "+AgPrc",
                    "Dmaisilla": "+Der/maisilla",
                    "Dmaton": "+NegPrc",
                    "Dminen": "+N",
                    "Dmpi": "+Comp",
                    "Dnut": "+PrfPrc+Act",
                    "Ds": "+Cmp",
                    "Dsti": "+Der/sti",
                    "Dtattaa": "+Der/tattaa",
                    "Dtatuttaa": "+Der/tatuttaa",
                    "Dtava": "+PrsPrc+Pass",
                    "Dttaa": "+Der/ttaa",
                    "Dtar": "+Der/tar",
                    "Dmainen": "+Der/mainen",
                    "Dton": "+Der/ton",
                    "Dllinen": "+Der/llinen",
                    "Dhko": "+Der/hko",
                    "Disa": "+Der/isa",
                    "Dnen": "+Der/nen",
                    "Dtuttaa": "+Der/tuttaa",
                    "Dlainen": "+Der/lainen",
                    "Dttain": "+Der/ttain",
                    "Dtu": "+PrfPrc+Pass",
                    "Du": "+Der/u",
                    "Duus": "+Der/uus",
                    "Dva": "+PrsPrc+Act",
                    "EVENT": "",
                    "FINAL-BRACKET": "",
                    "FINAL-QUOTE": "+Quote",
                    "FIRST": "+Sem/Human",
                    "FTB3MAN": "+Ins",
                    "FTB3man": "+Man",
                    "GEO": "+Sem/Geo",
                    "Ia": "+Inf1",
                    "Ie": "+Inf2",
                    "ILLATIVE": "+Ill",
                    "Ima": "+Inf3",
                    "Iminen": "+N",
                    "INDEFINITE": "+Indef",
                    "INESSIVE": "+Ine",
                    "INITIAL-BRACKET": "",
                    "INITIAL-QUOTE": "+Quote",
                    "INTERJECTION": "+Interj",
                    "INTERROGATIVE": "+Interr",
                    "LAST": "+Sem/Human",
                    "LEMMA-END": "",
                    "LEMMA-START": "",
                    "LOCATIVE": "",
                    "MEDIA": "",
                    "MISC": "",
                    "Ncon": "+ConNeg",
                    "Nneg": "+Neg",
                    "NOUN": "+N",
                    "Npl": "+Pl",
                    "N??": "+Sg",
                    "Nsg": "+Sg",
                    "NUMERAL": "+Num",
                    "NUM": "+Num",
                    "O3": "+Px3",
                    "Opl1": "+PxPl1",
                    "Opl2": "+PxPl2",
                    "ORDINAL": "+Ord",
                    "ORG": "+Sem/Org",
                    "Osg1": "+PxSg1",
                    "Osg2": "+PxSg2",
                    "PARTICLE": "+Pcle",
                    "PE4": "+Pe4",
                    "PERSONAL": "+Pers",
                    "PL1": "+Pl1",
                    "PL2": "+Pl2",
                    "PL3": "+Pl3",
                    "Ppe4": "+Pe4",
                    "Ppl1": "+Pl1",
                    "Ppl2": "+Pl2",
                    "Ppl3": "+Pl3",
                    "PREPOSITION": "+Adp+Pr",
                    "PRODUCT": "",
                    "PRONOUN": "+Pron",
                    "PROPER": "+Prop",
                    "PROPN": "+Prop",
                    "Psg1": "+Sg1",
                    "Psg2": "+Sg2",
                    "Psg3": "+Sg3",
                    "PUNCTUATION": "+Punct",
                    "Qhan": "+Foc/han",
                    "Qkaan": "+Foc/kaan",
                    "Qka": "+Foc/ka",
                    "Qkin": "+Foc/kin",
                    "Qko": "+Foc/ko",
                    "Qpa": "+Foc/pa",
                    "Qs": "+Foc/s",
                    "QUALIFIER": "+A",
                    "QUANTOR": "+Qnt",
                    "RECIPROCAL": "",
                    "REFLEXIVE": "+Refl",
                    "RELATIVE": "+Rel",
                    "ROMAN": "+Roman",
                    ".sent": "",
                    "SENTENCE-BOUNDARY": "",
                    "SG1": "+Sg1",
                    "SG2": "+Sg2",
                    "SG3": "+Sg3",
                    "SPACE": "",
                    "SUPERL": "+Superl",
                    "SUFFIX": "",
                    "Tcond": "+Cond",
                    "Timp": "+Impv",
                    "Topt": "+Opt",
                    "Tpast": "+Pst",
                    "Tpot": "+Pot",
                    "Tpres": "+Prs",
                    "Uarch": "+Use/Arch",
                    "Udial": "+Dial/Finland",
                    "Unonstd": "+Err/Orth",
                    "UNSPECIFIED": "+Pcle",
                    "Urare": "+Use/Marg",
                    "Vact": "+Act",
                    "VERB": "+V",
                    "Vpss": "+Pass",
                    "Xabe": "+Abe",
                    "Xabl": "+Abl",
                    "Xacc": "+Acc",
                    "Xade": "+Ade",
                    "Xall": "+All",
                    "Xcom": "+Com",
                    "Xela": "+Ela",
                    "Xess": "+Ess",
                    "Xgen": "+Gen",
                    "Xill": "+Ill",
                    "Xine": "+Ine",
                    "Xins": "+Ins",
                    "Xlat": "+Lat",
                    "X???": "+Nom",
                    "Xnom": "+Nom",
                    "Xpar": "+Par",
                    "Xtra": "+Tra",
                    "XForeign": "+OLang/eng",
                    "X": "",
                    "": ""
                    }

    def __init__(self, verbosity=False):
        """Create a giellatekno tag formatter with given verbosity.

        @param verbosity set to true to disable output printng
        """
        ## Verbosity
        self.verbosity = verbosity
        fail = False
        for _, giella in self.stuff2giella.items():
            if len(giella) < 2:
                continue
            elif giella not in self.giella_multichars:
                just_fail("There are conflicting formattings in here!\n" +
                          giella +
                          " is not a valid defined giella multichar_symbol!")
                fail = True
        if fail:
            ## Whether tags match reality
            self.tainted = True

    def stuff2lexc(self, stuff):
        """Convert omorfi analysis to giellatekno's lexc.

        @return lexc-formatted string containing giellatekno tag(s)
        """
        if stuff == '0':
            return "0"
        elif stuff in self.stuff2giella:
            return self.stuff2giella[stuff]
        else:
            fail_formatting_missing_for(stuff, "giella.1")
            return ""

    def analyses2lexc(self, anals, surf):
        """Convert omorfi analyses and lexeme into giellatekno format.

        @return lexc-formatted string containing giellatekno tags and lemma
        """
        giellastring = ""
        for anal in anals.split('|'):
            if anal == '@@COPY-STEM@@':
                giellastring += lexc_escape(surf)
            elif anal.startswith('@@LITERAL:') and anal.endswith('@@'):
                giellastring += lexc_escape(anal[len('@@LITERAL:'):-len('@@')])
            else:
                giellastring += self.stuff2lexc(anal)
        return giellastring

    def continuation2lexc(self, anals, surf, cont):
        """Create lexical entry for omorfi continuation class data

        @return lexc-date for omorfi continuation class
        """
        giellastring = self.analyses2lexc(anals, surf)
        if 'DIGITS_' in cont and not ('BACK' in cont or 'FRONT' in cont):
            giellastring = lexc_escape(surf) + giellastring
        surf = lexc_escape(surf.replace(morph_boundary, ">")
                           .replace(deriv_boundary, "»")
                           .replace(word_boundary, "")
                           .replace(stub_boundary, ""))
        return "%s:%s\t%s ;\n" % (giellastring, surf, cont)

    def wordmap2lexc(self, wordmap):
        '''
        format string for canonical giella format for morphological analysis

        @return lexc-formatted lexical entry for a giellatekno word.
        '''
        wordmap['analysis'] = lexc_escape(
            wordmap['lemma'].replace(word_boundary, '#'))
        if wordmap['pos'] == 'CONJUNCTIONVERB':
            if wordmap['lemma'] == 'eikä':
                wordmap['lemma'] = 'ei'
                wordmap['analysis'] = self.stuff2lexc('COORDINATING') + \
                    self.stuff2lexc('Nneg')
            else:
                wordmap['analysis'] = self.stuff2lexc('ADVERBIAL') + \
                    self.stuff2lexc('Nneg')
        else:
            wordmap['analysis'] += self.stuff2lexc(wordmap['pos'])
        if wordmap['is_proper']:
            wordmap['analysis'] += self.stuff2lexc('PROPER')
            if wordmap['proper_noun_class']:
                wordmap['analysis'] +=\
                    self.stuff2lexc(wordmap['proper_noun_class'])
        if wordmap['particle']:
            for pclass in wordmap['particle'].split('|'):
                wordmap['analysis'] += self.stuff2lexc(pclass)
        if wordmap['symbol']:
            for subcat in wordmap['symbol'].split('|'):
                wordmap['analysis'] += self.stuff2lexc(subcat)
        lex_stub = lexc_escape(wordmap['stub'].replace(word_boundary, "")
                               .replace(weak_boundary, "")
                               .replace(deriv_boundary, "»")
                               .replace(morph_boundary, ">"))
        lexc_line = "%s:%s\t%s\t;" % (wordmap['analysis'], lex_stub,
                                      wordmap['new_para'])
        if 'BLACKLISTED' in wordmap['new_para']:
            return "! ! !" + lexc_line
        else:
            return lexc_line

    def multichars_lexc(self):
        """Create lexc analysis tags declaration in giellatekno format.

        @return lexc-formatted string of giellatekno Mutlichar_symbols block.
        """
        multichars = "Multichar_Symbols\n!! giellatekno multichar set:\n"
        for mcs in self.giella_multichars:
            multichars += mcs + "\n"
        multichars += Formatter.multichars_lexc(self)
        return multichars

    def root_lexicon_lexc(self):
        """Create root lexicon for giellatekno lexc.

        @return lexc-formatted string of giellatekno Root lexicon
        """
        root = Formatter.root_lexicon_lexc(self)
        if True:
            # want co-ordinated hyphens left
            root += "!! LEXICONS that can be co-ordinated hyphen -compounds\n"
            root += self.stuff2lexc('B→') + ':-   NOUN ;\n'
            root += self.stuff2lexc('B→') + ':-   ADJ ;\n'
            root += self.stuff2lexc('B→') + ':-   SUFFIX ;\n'
        return root


# self test
if __name__ == '__main__':
    formatter = GiellaFormatter()
    exit(0)
