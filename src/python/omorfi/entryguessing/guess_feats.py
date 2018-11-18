#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to guess omorfi features from partial lexical data."""

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

from ..error_logging import fail_guess_because


def guess_pos_from_newpara(wordmap):
    if wordmap['pos']:
        return wordmap
    new_para = wordmap['new_para']
    wordmap['pos'] = new_para[:new_para.find('_')]


def guess_grade_dir_from_ktn(wordmap):
    '''Record gradation direction based on kotus class or stem syllable.'''
    if not wordmap['kotus_tn']:
        return wordmap
    if wordmap['grade_dir']:
        return wordmap
    tn = int(wordmap['kotus_tn'])
    if tn in range(1, 32) or tn in range(52, 62) or tn in range(76, 79):
        wordmap['grade_dir'] = 'weaken'
    elif tn in range(32, 50) or tn in range(62, 76):
        wordmap['grade_dir'] = 'strengthen'
    elif tn in [0, 99, 101, 999]:
        wordmap['grade_dir'] = False
    elif tn in [1007, 1008, 1009, 1010, 1024, 1026, 1067, 1099, 1101]:
        wordmap['grade_dir'] = 'weaken'
    else:
        fail_guess_because(wordmap, [], ["0-78", 99, 101, 1007, 1008, 1009,
                                         1010, 1024, 1026, 1067, 1099, 1101])
    return wordmap


def guess_stem_features_ktn(wordmap):
    '''Record guessable features based on kotus classification, such as stem
    variants, harmony etc. This is especially for those features kotus
    classification has collapsed that are hard for us.
    '''
    if not wordmap['kotus_tn']:
        return wordmap
    tn = int(wordmap['kotus_tn'])
    if tn in [5, 6]:
        if wordmap['lemma'].endswith('i'):
            wordmap['extra_i'] = True
    elif tn in range(9, 16) or tn in [1009, 1010]:
        if wordmap['lemma'].endswith('a'):
            wordmap['stem_vowel'] = 'a'
        elif wordmap['lemma'].endswith('ä'):
            wordmap['stem_vowel'] = 'ä'
    elif tn in range(17, 19) or tn == 20:
        if wordmap['lemma'].endswith('a'):
            wordmap['stem_vowel'] = 'a'
        elif wordmap['lemma'].endswith('e'):
            wordmap['stem_vowel'] = 'e'
        elif wordmap['lemma'].endswith('i'):
            wordmap['stem_vowel'] = 'i'
        elif wordmap['lemma'].endswith('o'):
            wordmap['stem_vowel'] = 'o'
        elif wordmap['lemma'].endswith('u'):
            wordmap['stem_vowel'] = 'u'
        elif wordmap['lemma'].endswith('y'):
            wordmap['stem_vowel'] = 'y'
        elif wordmap['lemma'].endswith('ä'):
            wordmap['stem_vowel'] = 'ä'
        elif wordmap['lemma'].endswith('ö'):
            wordmap['stem_vowel'] = 'ö'
    elif tn == 19:
        if wordmap['lemma'].endswith('uo'):
            wordmap['stem_diphthong'] = 'uo'
        elif wordmap['lemma'].endswith('yö'):
            wordmap['stem_diphthong'] = 'yö'
        elif wordmap['lemma'].endswith('ie'):
            wordmap['stem_diphthong'] = 'ie'
    elif tn == 47:
        if wordmap['lemma'].endswith('ut'):
            wordmap['stem_vowel'] = 'u'
        elif wordmap['lemma'].endswith('yt'):
            wordmap['stem_vowel'] = 'y'
    elif tn == 64:
        if wordmap['lemma'].endswith('uoda'):
            wordmap['stem_diphthong'] = 'uo'
        elif wordmap['lemma'].endswith('yödä'):
            wordmap['stem_diphthong'] = 'yö'
        elif wordmap['lemma'].endswith('iedä'):
            wordmap['stem_diphthong'] = 'ie'
    return wordmap


def guess_harmony(wordmap):
    '''Guess word's harmony based on lemma, using trivial last harmony vowel
    or front algorithm.
    '''
    if wordmap['harmony']:
        return wordmap
    if not wordmap['kotus_tn']:
        tn = 0
    else:
        tn = int(wordmap['kotus_tn'])
    if tn in range(52, 79) or wordmap['pos'] == 'VERB':
        if wordmap['lemma'].endswith('ä'):
            wordmap['harmony'] = 'front'
        elif wordmap['lemma'].endswith('a'):
            wordmap['harmony'] = 'back'
        elif wordmap['lemma'].endswith('ei') and tn == 1099:
            wordmap['harmony'] = 'front'
        else:
            fail_guess_because(wordmap, ["VERB"], ["a", "ä", "ei"])
            exit(1)
    elif wordmap['pronunciation']:
        lastbound = -1
        for bound in ['{WB}', '{XB}', '_', '#', ' ', '-']:
            b = wordmap['pronunciation'].rfind(bound)
            if b > lastbound:
                lastbound = b
        lastback = lastbound
        for back in ['a', 'o', 'u', 'A', 'O', 'U', 'á', 'à', 'ą', 'ô', 'û']:
            b = wordmap['pronunciation'].rfind(back)
            if b > lastback:
                lastback = b
        lastfront = lastbound
        for front in ['ä', 'ö', 'y', 'Ä', 'Ö', 'Y', 'ü']:
            f = wordmap['pronunciation'].rfind(front)
            if f > lastfront:
                lastfront = f
        if lastfront == lastbound and lastback == lastbound:
            wordmap['harmony'] = 'front'
        elif lastfront > lastback:
            wordmap['harmony'] = 'front'
        elif lastback > lastfront:
            wordmap['harmony'] = 'back'
    else:
        fail_guess_because(wordmap, [""], ["pronunciation"])
        exit(1)
    return wordmap


def guess_pronunciation(wordmap):
    if wordmap['pronunciation']:
        return wordmap
    wordmap['pronunciation'] = wordmap['stub']
    if wordmap['stem_vowel']:
        wordmap['pronunciation'] += wordmap['stem_vowel']
    elif wordmap['stem_diphthong']:
        wordmap['pronunciation'] += wordmap['stem_diphthong']
    return wordmap


def guess_gradestem(wordmap):
    if wordmap['stem_vowel']:
        wordmap['gradestem'] += '{^' + wordmap['stem_vowel'] + '}'
    if wordmap['harmony']:
        wordmap['gradestem'] += '{^' + wordmap['harmony'] + '}'
    if wordmap['kotus_av']:
        wordmap['gradestem'] += '{' + wordmap['kotus_av'] + '}'
    if wordmap['plurale_tantum'] == 'obligatory':
        wordmap['gradestem'] += '@U.PLURALE.TANTUM@'
    elif wordmap['plurale_tantum'] == 'common':
        wordmap['gradestem'] += '{PLT?}'
    return wordmap


def guess_bound_morphs(wordmap):
    if wordmap['stub'] in ['-', '--']:
        return wordmap
    if wordmap['stub'].endswith('-'):
        wordmap['is_prefix'] = True
        wordmap['stub'] = wordmap['stub'][:-1]
    elif wordmap['stub'].startswith('-'):
        wordmap['is_suffix'] = True
        wordmap['stub'] = wordmap['stub'][1:]
    return wordmap
