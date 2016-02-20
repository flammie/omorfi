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

from .formatter import Formatter
from .settings import word_boundary, optional_hyphen
from .lexc_formatter import lexc_escape


class NoTagsFormatter(Formatter):

    def __init__(self, verbose=True, **kwargs):
        self.verbose = verbose
        self.segment = False
        self.lemmatise = False
        if 'lemmatise' in kwargs and kwargs['lemmatise']:
            self.lemmatise = True
        elif 'segment' in kwargs and kwargs['segment']:
            self.segment = True

    def stuff2lexc(self, stuff):
        if 'Bc' == stuff:
            return word_boundary
        else:
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
        elif 'PUNCT_NONSTD_EXCL_LOOP' in cont:
            analstring = lexc_escape(surf) + analstring
        elif self.segment:
            analstring = lexc_escape(surf)
        elif self.lemmatise:
            pass
        else:
            analstring = lexc_escape(surf)
        return "%s:%s\t%s ;\n" % (analstring, lexc_escape(surf), cont)

    def wordmap2lexc(self, wordmap):
        if wordmap['lemma'] == ' ':
            return ''
        if self.lemmatise:
            wordmap['analysis'] = lexc_escape(wordmap['lemma'])
        elif self.segment:
            wordmap['analysis'] = lexc_escape(wordmap['stub'])
        else:
            wordmap['analysis'] = lexc_escape(wordmap['stub'])
        retvals = ""
        wordmap['stub'] = wordmap['stub'].replace(
            word_boundary, optional_hyphen)
        wordmap['stub'] = lexc_escape(wordmap['stub'])
        retvals += "%s:%s\t%s\t;\n" % (wordmap['analysis'], wordmap['stub'],
                                       wordmap['new_para'])
        return retvals

    def multichars_lexc(self):
        multichars = "Multichar_Symbols\n"
        multichars += Formatter.multichars_lexc(self)
        return multichars

    def root_lexicon_lexc(self):
        root = Formatter.root_lexicon_lexc(self)
        return root

# self test
if __name__ == '__main__':
    formatter = NoTagsFormatter()
    exit(0)
