#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to format lexc from omorfi data."""

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

# functions for formatting the database data to lexc

from .settings import common_multichars, version_id_easter_egg, \
        optional_hyphen, word_boundary, stub_boundary, newword_boundary, \
        morph_boundary, deriv_boundary

def lexc_escape(s):
    '''Escape symbols that have special meaning in lexc.'''
    s = s.replace("%", "__PERCENT__")
    s = s.replace(" ", "% ")
    s = s.replace("<", "%<")
    s = s.replace(">", "%>")
    s = s.replace("0", "%0")
    s = s.replace("!", "%!")
    s = s.replace(":", "%:")
    s = s.replace('"', '%"')
    s = s.replace(";", "%;")
    s = s.replace("__PERCENT__", "%%")
    return s


def format_copyright_lexc():
    return """
! This automatically generated lexc data is originated from 
! omorfi database.
! Copyright (c) 2014 Omorfi contributors

! This program is free software: you can redistribute it and/or modify
! it under the terms of the GNU General Public License as published by
! the Free Software Foundation, version 3 of the License

! This program is distributed in the hope that it will be useful,
! but WITHOUT ANY WARRANTY; without even the implied warranty of
! MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
! GNU General Public License for more details.

! You should have received a copy of the GNU General Public License
! along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""




# generics
def format_continuation_lexc_generic(anals, surf, cont):
    surf = lexc_escape(surf)
    return "%s:%s\t%s ; \n" %(surf.replace(optional_hyphen, newword_boundary),
            surf, cont)


def format_wordmap_lexc_generic(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['stub']) + stub_boundary
    retvals = []
    lex_stub = lexc_escape(wordmap['stub'])
    retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, wordmap['new_para'])]
    return "\n".join(retvals)

def format_wordmap_lexc_labeled_segments(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['stub']) + "[" + wordmap['upos'] + ']'
    retvals = []
    lex_stub = lexc_escape(wordmap['stub'])
    retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, wordmap['new_para'])]
    return "\n".join(retvals)

def format_continuation_lexc_labeled_segments(anals, surf, cont):
    surf = lexc_escape(surf)
    # mostly suffixes: e.g.
    # >i>ssa Pl|Ine -> |i|PL|ssa|INE
    # >i -> |i|ACT|PAST|SG3
    foo = surf
    foo = foo.replace(morph_boundary, "", 1)
    foo = foo.replace(deriv_boundary, "")
    foo = foo.replace(newword_boundary, "##")
    foo = foo.replace(word_boundary, "#")
    restanals = []
    for anal in anals.split('|'):
        if "{MB}" in foo:
            foo = foo.replace(morph_boundary, "["  + anal+ "]", 1)
        else:
            restanals.append(anal)
    if len(restanals) > 0:
        foo += "|" + "|".join(restanals)

    return "%s:%s\t%s ; \n" %(foo.replace(optional_hyphen, newword_boundary),
            surf, cont)


def format_wordmap_lexc_generic(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['stub']) + stub_boundary
    retvals = []
    lex_stub = lexc_escape(wordmap['stub'])
    retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, wordmap['new_para'])]
    return "\n".join(retvals)

