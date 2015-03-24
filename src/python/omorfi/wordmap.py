#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python data format for one lexeme in omorfi database."""

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




def init_wordmap():
    wordmap = {"pos": None, "lemma": None, "new_para": None, "kotus_tn": None,
               "kotus_av": None, "plurale_tantum": None,
               "possessive": None, "clitics": None,
               "is_proper": None, "proper_noun_class": list(), "style": None,
               "stub": None, "gradestem": None, "twolstem": None, 
               "grade_dir": None, "harmony": None, "is_suffix": None,
               "is_prefix": None, "stem_vowel": None, "stem_diphthong": None,
               "sem": list(), "particle": None, "pronunciation": None,
               "boundaries": None, "bracketstub": None, "origin": None,
               "extra_i": False, "extra_e": False, "real_pos": None,
               "symbol": None, "argument": None , "pronoun": None,
               "noun_class": None, "adjective_class": None,
               "numeral_class": None,
               "homonym": 0}
    return wordmap

def get_wordmap_fieldnames():
    return ["pos", "lemma", "new_para", "kotus_tn", "kotus_av",
            "plurale_tantum", "possessive", "clitics", "is_proper",
            "proper_noun_class", "style", "stub", "gradestem", "twolstem",
            "grade_dir", "harmony", "is_suffix", "is_prefix", "stem_vowel",
            "stem_diphthong", "sem", "particle", "pronunciation", 
            "boundaries", "bracketstub", "origin", "extra_i", "extra_e",
            "real_pos", "symbol", "argument", "pronoun", "noun_class",
            "adjective_class", "numeral_class", "homonym"]

# Split a wordmap into a list of wordmaps each having a different item of original
# <field> list in their respective <field>, or only '' if <field> list was empty.
def split_wordmap_by_field(wordmap, field):
    if not wordmap[field]:
        wordmap[field] = ['']
    wordmaps = []
    for value in wordmap[field]:
        wm_copy = dict(wordmap)
        wm_copy[field] = value
        wordmaps.append(wm_copy)
    return wordmaps
