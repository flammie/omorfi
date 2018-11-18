#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to parse omorfi intermediate lexical databases."""

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

from ..error_logging import just_fail


def parse_defaults_from_tsv(wordmap, tsv_parts):
    '''Parse default data from 2+ field tsv with new para and lemma.'''
    # first field is lemma; start all deep, shallow and surface forms from that
    wordmap['lemma'] = tsv_parts[0]
    wordmap['stub'] = wordmap['lemma']
    wordmap['bracketstub'] = wordmap['lemma']
    wordmap['gradestem'] = wordmap['lemma']
    # second field is new paradigm class set
    wordmap['new_para'] = tsv_parts[2]
    wordmap['homonym'] = tsv_parts[1]
    wordmap['origin'] = tsv_parts[3]
    return wordmap


def parse_extras_from_tsv(wordmap, tsv_parts):
    '''Parse extra fields form >3 fields of 2+ field tsv.'''
    if len(tsv_parts) == 4:
        # no extras
        pass
    elif len(tsv_parts) >= 5:
        tsv_extras = tsv_parts[4:]
        for tsv_extra in tsv_extras:
            extra_fields = tsv_extra.split("=")
            if extra_fields[0] == 'plurale_tantum':
                wordmap['plurale_tantum'] = extra_fields[1]
            elif extra_fields[0] == 'proper_noun_class':
                wordmap['proper_noun_class'] = extra_fields[1].upper()
                wordmap['is_proper'] = True
            elif extra_fields[0] == 'adjective_class':
                wordmap['adjective_class'] = extra_fields[1].upper()
            elif extra_fields[0] == 'noun_class':
                wordmap['noun_class'] = extra_fields[1].upper()
            elif extra_fields[0] == 'numtype':
                wordmap['numtype'] = extra_fields[1].upper()
            elif extra_fields[0] == 'possessive':
                wordmap['possessive'] = extra_fields[1]
            elif extra_fields[0] == 'clitics':
                wordmap['clitics'] = extra_fields[1]
            elif extra_fields[0] == 'stem-vowel':
                wordmap['stem_vowel'] = extra_fields[1]
            elif extra_fields[0] == 'style':
                wordmap['style'] = extra_fields[1].upper()
            elif extra_fields[0] == 'boundaries':
                wordmap['stub'] = extra_fields[1]
                wordmap['boundaries'] = extra_fields[1]
            elif extra_fields[0] == 'subcat':
                wordmap['subcat'] = extra_fields[1].upper()
            elif extra_fields[0] == 'sem':
                wordmap['sem'] = extra_fields[1].upper()
            elif extra_fields[0] == 'particle':
                wordmap['particle'] = extra_fields[1].upper()
            elif extra_fields[0] == 'pronunciation':
                wordmap['pronunciation'] = extra_fields[1]
            elif extra_fields[0] == 'origin':
                wordmap['origin'] = extra_fields[1]
            elif extra_fields[0] == 'symbol':
                wordmap['symbol'] = extra_fields[1].upper()
            elif extra_fields[0] == 'argument':
                wordmap['argument'] = extra_fields[1].upper()
            elif extra_fields[0] == 'pronoun':
                wordmap['pronoun'] = extra_fields[1].upper()
            elif extra_fields[0] == 'homonym':
                wordmap['homonym'] = int(extra_fields[1])
            elif extra_fields[0] == 'original-ktn':
                wordmap['kotus_tn'] = int(extra_fields[1])
            elif extra_fields[0] == 'prontype':
                wordmap['prontype'] = extra_fields[1].upper()
            elif extra_fields[0] == 'abbr':
                wordmap['abbr'] = extra_fields[1].upper()
            elif extra_fields[0] == 'lex':
                wordmap['lex'] = extra_fields[1].upper()
            elif extra_fields[0] == 'adptype':
                wordmap['adptype'] = extra_fields[1].upper()
            elif extra_fields[0] == 'blacklist':
                wordmap['blacklist'] = extra_fields[1].upper()
            else:
                just_fail("Unrecognised extra field " + tsv_extra + " in TSV")
                return None
    return wordmap
