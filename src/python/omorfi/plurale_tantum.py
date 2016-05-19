#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to guess plurale tantum features from partial lexical data."""

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

from .error_logging import fail_guess_because
from .omorfi.string_manglers import replace_rightmost, replace_rightmosts


def plurale_tantum_get_singular_stem(wordmap):
    '''Guess inflectional singulars for words whose dictionary form is plural.
    '''
    if not wordmap['kotus_tn']:
        return wordmap
    tn = int(wordmap['kotus_tn'])
    if not wordmap['plurale_tantum'] == 'obligatory':
        return wordmap
    if wordmap['kotus_av'] and tn not in [27, 28, 34]:
        if tn in [7, 23, 24, 25, 26, 29, 30]:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'e', 'i')
        # ^^ generic extra tweak
        if (tn in range(1, 7) or tn in range(8, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'A':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'k', 'kk')
        elif (tn in range(1, 7) or tn in range(8, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'B':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'p', 'pp')
        elif (tn in range(1, 7) or tn in range(8, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'C':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 't', 'tt')
        elif tn == 1 and wordmap['kotus_av'] == 'D':
            wordmap['stub'] = replace_rightmosts(
                wordmap['stub'], ['ut', 'yt', 'öt', 'ot'], ['ku', 'ky', 'kö', 'ko'])
        elif tn in [5, 7] and wordmap['kotus_av'] == 'D':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'it', 'ki')
        elif tn in [9, 10] and wordmap['kotus_av'] == 'D':
            wordmap['stub'] = replace_rightmosts(
                wordmap['stub'], ['at', 'ät'], ['ka', 'kä'])
        elif tn == 1007:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'jet', 'i')
        elif tn in [1009, 1010] and wordmap['kotus_av'] == 'D':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'jat', 'ika')
        elif tn == 32 and wordmap['kotus_av'] == 'C':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 'et', ''), 'tt', 't')
        elif tn == 32 and wordmap['kotus_av'] == 'D':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 'et', ''), 'k', '')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'E':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'v', 'p')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'F':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'd', 't')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'G':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'g', 'k')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'H':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'mm', 'mp')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'I':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'll', 'lt')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'J':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'nn', 'nt')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'K':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'rr', 'rt')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'L':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'j', 'k')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'M':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'v', 'k')
        elif (tn in [23, 24, 25, 26, 29, 30]) and wordmap['kotus_av'] == 'G':
            wordmap['stub'] = replace_rightmost(
                replace_rightmost(wordmap['stub'], 't', ''), 'g', 'k')
        elif tn == 16 and wordmap['kotus_av'] == 'H':
            wordmap['stub'] = wordmap['stub'][:-3] + 'pi'
        elif tn == 28 and wordmap['kotus_av'] == 'J':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'nnet', 'nsi')
        elif tn == 33 and wordmap['kotus_av'] in ['A', 'B', 'C', 'D']:
            wordmap['stub'] = wordmap['stub'][:-5] + 'in'
        elif tn == 33 and wordmap['kotus_av'] == 'E':
            wordmap['stub'] = wordmap['stub'][:-5] + 'vin'
        elif tn == 33 and wordmap['kotus_av'] == 'F':
            wordmap['stub'] = wordmap['stub'][:-5] + 'din'
        elif tn == 33 and wordmap['kotus_av'] == 'G':
            wordmap['stub'] = wordmap['stub'][:-5] + 'gin'
        elif tn == 33 and wordmap['kotus_av'] == 'H':
            wordmap['stub'] = wordmap['stub'][:-5] + 'min'
        elif tn == 33 and wordmap['kotus_av'] == 'I':
            wordmap['stub'] = wordmap['stub'][:-5] + 'lin'
        elif tn == 33 and wordmap['kotus_av'] == 'J':
            wordmap['stub'] = wordmap['stub'][:-5] + 'nin'
        elif tn == 33 and wordmap['kotus_av'] == 'K':
            wordmap['stub'] = wordmap['stub'][:-5] + 'rin'
        elif tn == 41 and wordmap['kotus_av'] in ['A', 'B', 'C', 'D']:
            wordmap['stub'] = wordmap['stub'][:-4] + 'as'
        elif tn == 41 and wordmap['kotus_av'] == 'E':
            wordmap['stub'] = wordmap['stub'][:-4] + 'vas'
        elif tn == 41 and wordmap['kotus_av'] == 'F':
            wordmap['stub'] = wordmap['stub'][:-4] + 'das'
        elif tn == 41 and wordmap['kotus_av'] == 'G':
            wordmap['stub'] = wordmap['stub'][:-4] + 'gas'
        elif tn == 41 and wordmap['kotus_av'] == 'H':
            wordmap['stub'] = wordmap['stub'][:-4] + 'mas'
        elif tn == 41 and wordmap['kotus_av'] == 'I':
            wordmap['stub'] = wordmap['stub'][:-4] + 'las'
        elif tn == 41 and wordmap['kotus_av'] == 'J':
            wordmap['stub'] = wordmap['stub'][:-4] + 'nas'
        elif tn == 41 and wordmap['kotus_av'] == 'K':
            wordmap['stub'] = wordmap['stub'][:-4] + 'ras'
        elif tn == 48 and wordmap['kotus_av'] in ['A', 'B', 'C', 'D']:
            wordmap['stub'] = wordmap['stub'][:-4] + 'e'
        elif tn == 48 and wordmap['kotus_av'] == 'E':
            wordmap['stub'] = wordmap['stub'][:-4] + 've'
        elif tn == 48 and wordmap['kotus_av'] == 'F':
            wordmap['stub'] = wordmap['stub'][:-4] + 'de'
        elif tn == 48 and wordmap['kotus_av'] == 'G':
            wordmap['stub'] = wordmap['stub'][:-4] + 'ge'
        elif tn == 48 and wordmap['kotus_av'] == 'H':
            wordmap['stub'] = wordmap['stub'][:-4] + 'me'
        elif tn == 48 and wordmap['kotus_av'] == 'I':
            wordmap['stub'] = wordmap['stub'][:-4] + 'le'
        elif tn == 48 and wordmap['kotus_av'] == 'J':
            wordmap['stub'] = wordmap['stub'][:-4] + 'ne'
        elif tn == 48 and wordmap['kotus_av'] == 'K':
            wordmap['stub'] = wordmap['stub'][:-4] + 're'
        elif tn == 48 and wordmap['kotus_av'] == 'L':
            wordmap['stub'] = wordmap['stub'][:-4] + 'je'
        else:
            fail_guess_because(wordmap, ["av", "!27,28,34"], ["1-48"])
            exit(1)
    else:
        if tn in range(1, 7) or tn in range(8, 16) or tn in range(17, 22):
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', '')
        elif tn in [7, 23, 24, 25, 26, 29, 30]:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'et', 'i')
        elif tn == 16:
            wordmap['stub'] = wordmap['stub'][:-3] + 'pi'
        elif tn == 16:
            wordmap['stub'] = wordmap['stub'][:-2]
        elif tn in [27, 28]:
            wordmap['stub'] = wordmap['stub'][:-3] + 'si'
            wordmap['kotus_av'] = False
        elif tn == 31:
            wordmap['stub'] = wordmap['stub'][:-4] + 'ksi'
        elif tn == 32:
            wordmap['stub'] = wordmap['stub'][:-2]
        elif tn == 33:
            wordmap['stub'] = wordmap['stub'][:-3] + 'n'
        elif tn == 34:
            wordmap['stub'] = wordmap['stub'][:-5] + '{oö}n'
        elif tn == 35:
            wordmap['stub'] = wordmap['stub'][:-5] + 'min'
        elif tn == 36 or tn == 37:
            wordmap['stub'] = wordmap['stub'][:-4] + 'n'
        elif tn == 38:
            wordmap['stub'] = wordmap['stub'][:-3] + 'nen'
        elif tn == 39:
            wordmap['stub'] = wordmap['stub'][:-4] + 's'
        elif tn == 40:
            wordmap['stub'] = wordmap['stub'][:-3] + 's'
        elif tn == 41:
            wordmap['stub'] = wordmap['stub'][:-2] + 's'
        elif tn == 42:
            wordmap['stub'] = wordmap['stub'][:-3] + 's'
        elif tn == 43:
            wordmap['stub'] = wordmap['stub'][:-2] + 't'
        elif tn == 47:
            wordmap['stub'] = wordmap['stub'][:-3] + '{uy}t'
        elif tn == 48:
            wordmap['stub'] = wordmap['stub'][:-3] + 'e'
        elif tn == 49:
            wordmap['stub'] = wordmap['stub'][:-3]
        else:
            fail_guess_because(wordmap, ["!av"], ["1-49"])
            exit(1)

    if wordmap['harmony'] == 'front':
        wordmap['stub'] = wordmap['stub'].replace('{uy}', 'y')
        wordmap['stub'] = wordmap['stub'].replace('{oö}', 'ö')
    elif wordmap['harmony'] == 'back':
        wordmap['stub'] = wordmap['stub'].replace('{uy}', 'u')
        wordmap['stub'] = wordmap['stub'].replace('{oö}', 'o')

    wordmap['gradestem'] = wordmap['stub']
    return wordmap
