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

from ..error_logging import fail_formatting_missing_for
from .formatter import Formatter
from .no_tags_formatter import NoTagsFormatter
from ..settings import optional_hyphen, word_boundary
from ..string_manglers import lexc_escape


class LabeledSegmentsFormatter(Formatter):
    """Handles conversions for morph segmenter with morph labels.
    Experimental.
    """

    ## labels for segments
    multichars = {
        '[ADJ]',
        '[VERB]',
        '[NOUN]',
        '[PART]',
        '[PRON]',
        '[NUM]',
        '[PROPN]',
        '[INTJ]',
        '[CCONJ]',
        '[SCONJ]',
        '[ADV]',
        '[ADP]',
        '[POST]',
        '[PREP]',
        '[PUNCT]',
        '[NOM]',
        '[PAR]',
        '[GEN]',
        '[INE]',
        '[ELA]',
        '[ILL]',
        '[ADE]',
        '[ABL]',
        '[ALL]',
        '[ESS]',
        '[INS]',
        '[ABE]',
        '[TRA]',
        '[COM]',
        '[LAT]',
        '[ACC]',
        '[SG]',
        '[PL]',
        '[POSSG1]',
        '[POSSG2]',
        '[POSPL1]',
        '[POSPL2]',
        '[POSSP3]',
        '[TRUNC]',
        '[PRES]',
        '[PAST]',
        '[COND]',
        '[POTN]',
        '[IMPV]',
        '[SG1]',
        '[SG2]',
        '[SG3]',
        '[PL1]',
        '[PL2]',
        '[PL3]',
        '[PE4]',
        '[CONNEG]',
        '[NEG]',
        '[ACTV]',
        '[PASV]',
        '[INFA]',
        '[INFE]',
        '[INFMA]',
        '[INFMAISILLA]',
        '[PCPNUT]',
        '[PCPVA]',
        '[PCPMA]',
        '[PCPMATON]',
        '[POS]',
        '[COMP]',
        '[SUPER]',
        '[hAn]',
        '[kAAn]',
        '[kin]',
        '[kO]',
        '[pA]',
        '[s]',
        '[kA]',
        '[FORGN]'}

    ## convert omorfi analyses to segment labels
    stuff2labels = {"Bc": "{wB}",
                    ".sent": "",
                    ".": ".",
                    "Aa": "",
                    "Aan": "",
                    "ABBREVIATION": "",
                    "ABESSIVE": "[ABE]",
                    "ABLATIVE": "[ABL]",
                    "ACRONYM": "",
                    "ADESSIVE": "[ADE]",
                    "ADJ": "[ADJ]",
                    "ADJECTIVE": "[ADJ]",
                    "ADP": "[ADP]",
                    "ADV": "[ADV]",
                    "ADVERBIAL": "",
                    "Aen": "",
                    "Ahan": "",
                    "Ahen": "",
                    "Ahin": "",
                    "Ahon": "",
                    "Ahun": "",
                    "Ahyn": "",
                    "Ahän": "",
                    "Ahön": "",
                    "Aia": "",
                    "Aiden": "",
                    "Aien": "",
                    "Aihin": "",
                    "Aiin": "",
                    "Ain": "",
                    "Aisiin": "",
                    "Aita": "",
                    "Aitten": "",
                    "Aitä": "",
                    "Aiä": "",
                    "Aja": "",
                    "Ajen": "",
                    "Ajä": "",
                    "ALLATIVE": "[ALL]",
                    "Ana": "",
                    "Aon": "",
                    "ARROW": "",
                    "Asa": "",
                    "Aseen": "",
                    "Ata": "",
                    "Aten": "",
                    "Atä": "",
                    "Aun": "",
                    "Ayn": "",
                    "Aä": "",
                    "Aän": "",
                    "Aön": "",
                    "B-": "[TRUNC]",
                    "B←": "[TRUNC]",
                    "B→": "[TRUNC]",
                    "CARDINAL": "",
                    "ORDINAL": "[ORD]",
                    "Ccmp": "[COMP]",
                    "CLAUSE-BOUNDARY": "",
                    "Cma": "[PCPMA]",
                    "Cmaisilla": "",
                    "Cmaton": "[PCPMATON]",
                    "Cnut": "[PCPNUT]",
                    "COMMA": "",
                    "COMPARATIVE": "",
                    "COMP": "[COMP]",
                    "CCONJ": "[CCONJ]",
                    "COORDINATING": "",
                    "Cpos": "[POS]",
                    "Csup": "[SUPER]",
                    "Cva": "[PCPVA]",
                    "DASH": "",
                    "DECIMAL": "",
                    "DEMONSTRATIVE": "",
                    "DERSTI": "",
                    "DERTTAIN": "",
                    "DIGIT": "",
                    "Din": "",
                    "Dinen": "",
                    "Dja": "",
                    "Dma": "[PCPMA]",
                    "Dmaisilla": "[INFMAISILLA]",
                    "Dmaton": "[PCPMATON]",
                    "Dminen": "",
                    "Dmpi": "",
                    "Dnut": "[PCPNUT]",
                    "Ds": "",
                    "Dsti": "",
                    "Dtattaa": "",
                    "Dtatuttaa": "",
                    "Dtava": "[PCPVA]",
                    "Dttaa": "",
                    "Dttain": "",
                    "Dtu": "[PCPNUT]",
                    "Du": "",
                    "Duus": "",
                    "Dva": "[PCPVA]",
                    "ELATIVE": "[ELA]",
                    "FINAL-BRACKET": "",
                    "FINAL-QUOTE": "",
                    "FTB3man": "",
                    "FTB3MAN": "",
                    "GENITIVE": "[GEN]",
                    "Ia": "[INFA]",
                    "Ie": "[INFE]",
                    "ILLATIVE": "[ILL]",
                    "Ima": "[INFMA]",
                    "Iminen": "",
                    "INDEFINITE": "",
                    "INESSIVE": "[INE]",
                    "INITIAL-BRACKET": "",
                    "INITIAL-QUOTE": "",
                    "INSTRUCTIVE": "",
                    "INTERROGATIVE": "",
                    "INTJ": "[INTJ]",
                    "LATIVE": "",
                    "LEMMA-END": "",
                    "LEMMA-START": "",
                    "LOCATIVE": "",
                    "Ncon": "[CONNEG]",
                    "Nneg": "",
                    "NOUN": "[NOUN]",
                    "Npl": "[PL]",
                    "N??": "",
                    "Nsg": "[SG]",
                    "NUMERAL": "[NUM]",
                    "NUM": "[NUM]",
                    "O3": "[POSSP3]",
                    "Opl1": "[POSPL1]",
                    "Opl2": "[POSPL2]",
                    "Osg1": "[POSSG1]",
                    "Osg2": "[POSSG2]",
                    "PARTICLE": "",
                    "PARTITIVE": "[PAR]",
                    "PE4": "[PE4]",
                    "PERSONAL": "[PERS]",
                    "PL1": "[PL1]",
                    "PL2": "[PL2]",
                    "PL3": "[PL3]",
                    "Ppe4": "[PE4]",
                    "Ppl1": "[PL1]",
                    "Ppl2": "[PL2]",
                    "Ppl3": "[PL3]",
                    "PREPOSITION": "[PREP]",
                    "PRONOUN": "[PRON]",
                    "PRON": "[PRON]",
                    "PROPER": "[PROPN]",
                    "Psg1": "[SG1]",
                    "Psg2": "[SG2]",
                    "Psg3": "[SG3]",
                    "PUNCTUATION": "[PUNCT]",
                    "Qhan": "[HAN]",
                    "Qkaan": "[KAAN]",
                    "Qka": "[KA]",
                    "Qkin": "[KIN]",
                    "Qko": "[KO]",
                    "Qpa": "[PA]",
                    "Qs": "[S]",
                    "QUALIFIER": "",
                    "QUANTIFIER": "",
                    "QUANTOR": "",
                    "RECIPROCAL": "",
                    "REFLEXIVE": "",
                    "RELATIVE": "",
                    "ROMAN": "",
                    "SCONJ": "[SCONJ]",
                    "SENTENCE-BOUNDARY": "",
                    "SEPARATIVE": "",
                    "SG1": "[SG1]",
                    "SG2": "[SG2]",
                    "SG3": "[SG3]",
                    "SPACE": "",
                    "SUFFIX": "",
                    "SUPERL": "[SUPER]",
                    "Tcond": "[COND]",
                    "Timp": "[IMPV]",
                    "Topt": "",
                    "Tpast": "[PAST]",
                    "Tpot": "[POTN]",
                    "Tpres": "[PRES]",
                    "Uarch": "",
                    "Udial": "",
                    "Unonstd": "",
                    "UNSPECIFIED": "",
                    "Urare": "",
                    "Vact": "[ACTV]",
                    "VERB": "[VERB]",
                    "Vpss": "[PASV]",
                    "X": "",
                    "Xabe": "[ABE]",
                    "Xabl": "[ABL]",
                    "Xacc": "[ACC]",
                    "Xade": "[ADE]",
                    "Xall": "[ALL]",
                    "Xcom": "[COM",
                    "Xela": "[ELA]",
                    "Xess": "[ESS]",
                    "XForeign": "",
                    "Xgen": "[GEN]",
                    "Xill": "[ILL]",
                    "Xine": "[INE]",
                    "Xins": "[INS]",
                    "Xlat": "",
                    "X???": "",
                    "Xnom": "[NOM]",
                    "Xpar": "[PAR]",
                    "Xtra": "[TRA]",
                    "": ""
                    }

    def __init__(self, verbose=True, **kwargs):
        """Create a segment label formatter with given verbosity and options.

        @param verbose set to false to disable output logging
        """
        ## verbosity
        self.verbose = verbose

    def stuff2lexc(self, stuff, _):
        """Convert omorfi analysis into segment labels

        @return lexc-formatted string of labeled segments
        """
        if stuff == '@@COPY-STEM@@':
            # we already copy stem
            return ''
        elif stuff.startswith('@@LITERAL:') and stuff.endswith('@@'):
            # we already copy stem
            return ''
        elif stuff in self.stuff2labels:
            return self.stuff2labels[stuff]
        else:
            if self.verbose:
                fail_formatting_missing_for(stuff, "labeled segements")
            return "ERRORMACRO"

    def analyses2lexc(self, anals, stem):
        """Convert omorfi analysis string and stem into labeled segments.

        @return lexc-formatted string of labeled segments
        """
        apestring = ''
        for i in anals.split('|'):
            apestring += self.stuff2lexc(i, stem)
        return apestring

    def continuation2lexc(self, anals, surf, cont):
        """Create lexc continuation class for omorfi morphology informations.

        @return lexc-formatted entry for continuation class data
        """
        # interleave tags and segments
        analstring = lexc_escape(surf)
        analstring += self.analyses2lexc(anals, surf)
        return "%s:%s\t%s ;\n" % (analstring, lexc_escape(surf), cont)

    def wordmap2lexc(self, wordmap):
        """Format omorfi lexical data into labeled stem segments in lexc.

        @return lexc-formatted lexical entry
        """
        if wordmap['lemma'] == ' ':
            return ''
        wordmap['analysis'] = lexc_escape(wordmap['stub'])
        wordmap['analysis'] += "{STUB}" + "[" + wordmap['upos'] + "]"
        retvals = ""
        wordmap['stub'] = wordmap['stub'].replace(
            word_boundary, optional_hyphen)
        wordmap['stub'] = lexc_escape(wordmap['stub'])
        if 'BLACKLIST' in wordmap['new_para']:
            return "! ! %s:%s\t%s\t;\n" % (wordmap['analysis'],
                                           wordmap['stub'],
                                           wordmap['new_para'])
        else:
            return "%s:%s\t%s\t;\n" % (wordmap['analysis'], wordmap['stub'],
                                       wordmap['new_para'])

        return retvals

    def multichars_lexc(self):
        """Format labels as lexc block

        @return lexc-format multichar symbols definition for segment labels
        """
        multichars = "Multichar_Symbols\n"
        for mc in self.multichars:
            multichars += lexc_escape(mc) + "\n"
        multichars += Formatter.multichars_lexc(self)
        return multichars

    def root_lexicon_lexc(self):
        """Create root lexicon for labeled segments

        @return lexc-format Root lexicon for labeled morph segments
        """
        root = Formatter.root_lexicon_lexc(self)
        return root


# self test
if __name__ == '__main__':
    formatter = NoTagsFormatter()
    exit(0)
