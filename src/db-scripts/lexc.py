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
some snippets.
"""

from settings import common_multichars, version_id_easter_egg


def copyright_lexc():
    """Return copyright declaration in lexc format.

    @return string holding current copyright declaration in lexc comment.
    """
    return "! Copyright 2015 Omorfi Contributors, GNU GPLv3"

def multichars_lexc():
    """Return multichar declaration in lexc format"""
    multichars = "!! Following specials exist in all versions of omorfi\n"
    for mcs in sorted(common_multichars):
        multichars += mcs + "\n"
    return multichars

def root_lexicon_lexc():
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
    root += version_id_easter_egg + ":__omorfi # ;\n"
    return root


def main():
    """Self test exmaple"""
    sys.exit(0)


if __name__ == "__main__":
    main()
