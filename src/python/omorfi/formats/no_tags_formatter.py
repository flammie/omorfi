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
from ..settings import optional_hyphen, word_boundary
from ..string_manglers import lexc_escape


class NoTagsFormatter(Formatter):
    """A formatter that can create tagless analysers. This is used for e.g.,
    lemmatisers, acceptors, and morph segmenters."""

    def __init__(self, verbose=True, **kwargs):
        """Create omorfi tag converter for tagless automata with given
        verbosity and options.

        @param verbose set to false to disable printing
        @param segment set to true to create segmenter
        @param lemmatise set to true to create lemmatiser
        """
        ## verbosity
        self.verbose = verbose
        ## if we are creating a segmenter
        self.segment = False
        ## if we are creating a lemmatiser
        self.lemmatise = False
        if 'lemmatise' in kwargs and kwargs['lemmatise']:
            self.lemmatise = True
        elif 'segment' in kwargs and kwargs['segment']:
            self.segment = True

    def stuff2lexc(self, stuff):
        """Convert omorfi analyses to nothing

        @return empty string unless relevant for lemmatiser or segmenter
        """
        if stuff == 'Bc':
            return word_boundary
        else:
            return ""

    def analyses2lexc(self, anals):
        """Convert omorfi analyses to nothing

        @return empty string unless relevant for lemmatiser or segmenter
        """
        apestring = ''
        for i in anals.split('|'):
            apestring += self.stuff2lexc(i)
        return apestring

    def continuation2lexc(self, anals, surf, cont):
        """Create lexc content for omorfi continuation class data

        @return lexc-formatted continuation class entry
        """
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
        """Format omorfi lexical item for tagless analysis

        @return lexc-format entry for lemma/stub analysis
        """
        if wordmap['lemma'] == ' ':
            return ''
        if self.lemmatise:
            wordmap['analysis'] = lexc_escape(wordmap['lemma'])
        elif self.segment:
            wordmap['analysis'] = lexc_escape(wordmap['stub'])
        else:
            wordmap['analysis'] = lexc_escape(wordmap['stub'])
        wordmap['stub'] = wordmap['stub'].replace(
            word_boundary, optional_hyphen)
        wordmap['stub'] = lexc_escape(wordmap['stub'])
        lexc_line = "%s:%s\t%s\t;\n" % (wordmap['analysis'], wordmap['stub'],
                                        wordmap['new_para'])
        if 'BLACKLISTED' in wordmap['new_para']:
            return "! ! !" + lexc_line
        else:
            return lexc_line

    def multichars_lexc(self):
        """Create analysis tags for lemmas and segments

        @return lexc-formatted string for Multichar_symbols block without
                analyses
        """
        multichars = "Multichar_Symbols\n"
        multichars += Formatter.multichars_lexc(self)
        return multichars

    def root_lexicon_lexc(self):
        """Create lexc root lexicon for lemmatisers and segmenters

        @return lexc-format string for Root lexicon of lemmatiser
        """
        root = Formatter.root_lexicon_lexc(self)
        return root


# self test
if __name__ == '__main__':
    formatter = NoTagsFormatter()
    exit(0)
