#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) Omorfi contributors <omorfi-devel@groups.google.com> 2015
# see AUTHORS file in top-level dir of this project, or
# <https://github.com/flammie/omorfi/wiki/AUTHORS>

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

"""
An interface for formatting, deformatting etc. tags and stuff.
"""

from abc import ABCMeta, abstractmethod

from ..settings import common_multichars, version_id_easter_egg


class Formatter(metaclass=ABCMeta):

    """
    An abstract base class for omorfi objects doing format conversions and
    such string mangling. The implememting classes are mainly tag-set
    variants, for conversions between different syntaxes there are helper
    functions. The better the conversions between stuffs are, the better the
    raw and python-based analysers are.

    The formats to convert include:

    * from omorfi's stuff strings
    * to lexc
    * to monodix
    * from wordmap
    * from continuation record (a tsv row)
    """

    def __init__(self, verbosity=False, **kwargs):
        """Construct formatter with given verbosity.
        
        @param verbosity whether to print messages while processing
        @param kwargs keyword map to determine what automata to load
        """
        self._verbosity = verbosity

    def copyright_lexc(self):
        """Return copyright declaration in lexc format.
        
        @return string holding current copyright declaration in lexc comment.
        """
        return "! Copyright 2015 Omorfi Contributors, GNU GPLv3"

    @abstractmethod
    def multichars_lexc(self):
        """Return multichar declaration in lexc format"""
        multichars = "!! Following specials exist in all versions of omorfi\n"
        for mcs in sorted(common_multichars):
            multichars += mcs + "\n"
        return multichars

    @abstractmethod
    def root_lexicon_lexc(self):
        """Return root lexicon in lexc format"""
        root = "LEXICON Root\n"
        root += """!! LEXICONS per class
    0   NOUN ;
    0   ADJ ;
    0   VERB    ;
    0   NUM ;
    0   DIGITS ;
    0   PRON    ;
    0   ADP    ;
    0   ADV    ;
    0   INTJ ;
    0   PUNCT ;
    0   SYM ;
    0   CCONJ ;
    0   SCONJ ;
    0   CCONJ|VERB ;
    0   PROPN ;
    0   ACRONYM ;
    0   ABBREVIATION    ;
    0   AUX    ;
    0   DET    ;
    0   X    ;
    """
        root += version_id_easter_egg + ':__omorfi # ;\n'
        return root

    @abstractmethod
    def wordmap2lexc(self, wordmap):
        """Turn wordmap into lexc string valid for insides of LEXICON"""
        pass

    @abstractmethod
    def continuation2lexc(self, fields):
        """Turn continuation into lexc string valid for insides of LEXICON."""
        pass


def main():
    """Self test exmaple"""
    exit(0)


if __name__ == "__main__":
    main()
