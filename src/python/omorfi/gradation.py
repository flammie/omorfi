#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to guess gradation from partial lexical data."""

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

from .omorfi.error_logging import fail_guess_because
from .omorfi.string_mangling import replace_rightmost, replace_rightmosts


def gradation_make_morphophonemes(wordmap):
    '''mark up gradating stop for morphophonological handling'''
    if not wordmap['kotus_tn']:
        return wordmap
    tn = wordmap['kotus_tn']
    av = wordmap['kotus_av']
    if not wordmap['kotus_av']:
        return wordmap
    if tn in range(1, 28) or tn in range(29, 32) or tn in range(52, 66) or tn == 76 or tn in [1009, 1010]:
        # strong root stem
        if av == 'A':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'k', '{k~~}')
        elif av == 'B':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'p', '{p~~}')
        elif av == 'C':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 't', '{t~~}')
        elif av == 'D':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'k', '{k~~}')
        elif av == 'E':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'p', '{p~~}')
        elif av == 'F':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 't', '{t~~}')
        elif av == 'G':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'k', '{k~~}')
        elif av == 'H':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'p', '{p~~}')
        elif av == 'I':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 't', '{t~~}')
        elif av == 'J':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 't', '{t~~}')
        elif av == 'K':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 't', '{t~~}')
        elif av == 'L':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'k', '{k~~}')
        elif av == 'M':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'k', '{k~~}')
        elif av == 'O':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'g', '{g~~}')
        elif av == 'P':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'b', '{b~~}')
        elif av == 'N':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'd', '{d~~}')
        else:
            fail_guess_because(wordmap, ["1-27", "29-32", "52-66", "76"],
                               ["A-P"])
            exit(1)
        return wordmap
    elif tn == 28:
        # gah gradation in stemparts
        return wordmap
    elif tn == 1007:
        # not gradation
        return wordmap
    else:
        # weak root stem
        if av == 'A':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'k', 'k{k~~}')
        elif av == 'B':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'p', 'p{p~~}')
        elif av == 'C' and tn in range(72, 76):
            # TVtA verbs
            wordmap['gradestem'] = wordmap['gradestem'][:wordmap['gradestem'].rfind(
                't') - 2] + 't{t~~}' + wordmap['gradestem'][wordmap['gradestem'].rfind('t') - 1:]
        elif av == 'C':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 't', 't{t~~}')
        elif av == 'D':
            # danger ahead! (it appears from middle of nowhere)
            if tn == 32:
                wordmap['gradestem'] = replace_rightmost(
                    wordmap['gradestem'], 'e', '{k~~}e')
            elif tn == 33:
                wordmap['gradestem'] = replace_rightmost(
                    wordmap['gradestem'], 'i', '{k~~}i')
            elif tn == 41:
                wordmap['gradestem'] = replace_rightmosts(wordmap['gradestem'], [
                                                          'as', 'es', 'is', '{aä}s'], ['{k~~}as', '{k~0}es', '{k~0}is', '{k~~}{aä}s'])
            elif tn == 43:
                wordmap['gradestem'] = replace_rightmosts(
                    wordmap['gradestem'], ['ut', 'yt'], ['{k~~}ut', '{k~~}yt'])
            elif tn == 44:
                wordmap['gradestem'] = replace_rightmost(
                    wordmap['gradestem'], 'e', '{k~~}e')
            elif tn == 48:
                wordmap['gradestem'] = replace_rightmost(
                    wordmap['gradestem'], 'e', '{k~~}e')
            elif tn == 49:
                wordmap['gradestem'] = replace_rightmost(
                    wordmap['gradestem'], 'en', '{k~~}en')
            elif tn == 67:
                wordmap['gradestem'] = replace_rightmost(
                    wordmap['gradestem'], 'ell', '{k~~}ell')
            elif tn == 72:
                wordmap['gradestem'] = replace_rightmosts(
                    wordmap['gradestem'], ['at', 'et', 'ot'], ['{k~~}at', '{k~~}et', '{k~0}ot'])
            elif tn == 73:
                wordmap['gradestem'] = replace_rightmosts(
                    wordmap['gradestem'], ['ata', 'ätä'], ['{k~~}ata', '{k~0}ätä'])
            elif tn == 74:
                wordmap['gradestem'] = replace_rightmosts(wordmap['gradestem'], [
                                                          'ota', 'eta', 'ötä', 'etä'], ['{k~~}ota', '{k~0}eta', '{k~0}ötä', '{k~0}etä'])
            elif tn == 75:
                wordmap['gradestem'] = replace_rightmosts(
                    wordmap['gradestem'], ['ita', 'itä'], ['{k~~}ita', '{k~0}itä'])
            elif tn == 99:
                pass
            else:
                fail_guess_because(wordmap, ["1-99"], ["A-C", "E-P"])
                exit(1)
        elif av == 'E':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'v', '{p~~}')
        elif av == 'F':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'd', '{t~~}')
        elif av == 'G':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'g', '{k~~}')
        elif av == 'H':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'm', '{p~~}')
        elif av == 'I' and tn != 67:
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'l', '{t~~}')
        elif av == 'I' and tn == 67:
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'lell', '{t~~}ell')
        elif av == 'J' and tn != 33:
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'n', '{t~~}')
        elif av == 'J' and tn == 33:
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'nin', '{t~~}in')
        elif av == 'K':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'r', '{t~~}')
        elif av == 'L':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'j', '{k~~}')
        elif av == 'N':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'd', 'd{d~~}')
        elif av == 'O':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'g', 'g{g~~}')
        elif av == 'P':
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'b', 'b{b~~}')
        elif av == 'T' and tn == 49:
            wordmap['gradestem'] = replace_rightmost(
                wordmap['gradestem'], 'e', '{t~~}e')
        else:
            fail_guess_because(wordmap, [""], ["1-99", "A-P"])
            exit(1)
        return wordmap
    return None
