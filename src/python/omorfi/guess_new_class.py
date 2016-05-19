#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to guess omorfi paradigm from other omorfi data."""

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
from .string_manglers import three_syllable


def guess_new_class(wordmap):
    '''Guess more exact classification now
    '''
    if wordmap['new_para']:
        return wordmap
    if wordmap['kotus_tn'] is None or wordmap['kotus_tn'] == '':
        return wordmap
    if not wordmap['pos']:
        wordmap['pos'] = 'PARTICLE'
        wordmap['new_para'] = '#'
    if wordmap['is_prefix']:
        wordmap['new_para'] = 'N_COMPOUND'
    elif wordmap['pos'] in ['PROPER', 'NOUN']:
        wordmap = guess_new_noun(wordmap)
    elif wordmap['pos'] == 'ADJECTIVE':
        wordmap = guess_new_adjective(wordmap)
    elif wordmap['pos'] == 'VERB':
        wordmap = guess_new_verb(wordmap)
    elif wordmap['pos'] == 'PRONOUN':
        wordmap = guess_new_pronoun(wordmap)
    elif wordmap['pos'] == 'ACRONYM':
        wordmap = guess_new_acro(wordmap)
    elif wordmap['pos'] == 'NUMERAL':
        wordmap = guess_new_numeral(wordmap)
    elif wordmap['pos'] == 'PARTICLE':
        wordmap = guess_new_particle(wordmap)
    else:
        fail_guess_because(wordmap, ["POS"], [
                           '!POS', 'PARTICLE', 'N', 'PROP', 'A', 'V', 'ACRO', 'NUM', 'INTJ', 'CONJ', 'ABBR'])
    if not wordmap['new_para']:
        fail_guess_because(wordmap, ["???"], ["???"],
                           "shouldn't reach this point (missing case somewhere)\n"
                           "Temporarily recovering by setting new_para to #!")
        wordmap['new_para'] = '#'
    return wordmap


def guess_new_noun(wordmap):
    '''Guessing new noun class based on kotus class.'''
    tn = int(wordmap['kotus_tn'])
    if not wordmap['plurale_tantum'] or wordmap['plurale_tantum'] == 'common':
        if tn == 1:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('o') or wordmap['lemma'].endswith('O'):
                    wordmap['new_para'] = 'N_TALO'
                elif wordmap['lemma'].endswith('u') or wordmap['lemma'].endswith('U'):
                    wordmap['new_para'] = 'N_ASU'
                elif wordmap['lemma'].endswith('ú'):
                    wordmap['new_para'] = 'N_ASU'
                elif wordmap['lemma'].endswith('y') or wordmap['lemma'].endswith('Y'):
                    wordmap['new_para'] = 'N_KÄRRY'
                elif wordmap['lemma'].endswith('ÿ'):
                    wordmap['new_para'] = 'N_KÄRRY'
                elif wordmap['lemma'].endswith('ö'):
                    wordmap['new_para'] = 'N_MÖMMÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, False],
                                       ['o O', 'u ú', 'y ÿ Y', 'ö'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('ko'):
                    wordmap['new_para'] = 'N_UKKO'
                elif wordmap['lemma'].endswith('ku'):
                    wordmap['new_para'] = 'N_TIKKU'
                elif wordmap['lemma'].endswith('ky'):
                    wordmap['new_para'] = 'N_MYRKKY'
                elif wordmap['lemma'].endswith('kö'):
                    wordmap['new_para'] = 'N_YÖKKÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'A'],
                                       ['ko', 'ku', 'ky', 'kö'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppo'):
                    wordmap['new_para'] = 'N_HAPPO'
                elif wordmap['lemma'].endswith('ppu'):
                    wordmap['new_para'] = 'N_LIPPU'
                elif wordmap['lemma'].endswith('ppy'):
                    wordmap['new_para'] = 'N_RYYPPY'
                elif wordmap['lemma'].endswith('ppö'):
                    wordmap['new_para'] = 'N_TÖRPPÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'B'],
                                       ['ppo', 'ppu', 'ppy', 'ppö'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tto'):
                    wordmap['new_para'] = 'N_HIRTTO'
                elif wordmap['lemma'].endswith('ttu'):
                    wordmap['new_para'] = 'N_TORTTU'
                elif wordmap['lemma'].endswith('tty'):
                    wordmap['new_para'] = 'N_PYTTY'
                elif wordmap['lemma'].endswith('ttö'):
                    wordmap['new_para'] = 'N_PÖNTTÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'C'],
                                       ['tto', 'ttu', 'tty', 'ttö'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('uoko'):
                    wordmap['new_para'] = 'N_RUOKO'
                elif wordmap['lemma'].endswith('iuku'):
                    wordmap['new_para'] = 'N_LIUKU'
                elif wordmap['lemma'].endswith('oko'):
                    wordmap['new_para'] = 'N_KOKO'
                elif wordmap['lemma'].endswith('hko') or \
                        wordmap['lemma'].endswith('lko') or \
                        wordmap['lemma'].endswith('rko'):
                    wordmap['new_para'] = 'N_PELKO'
                elif wordmap['lemma'].endswith('hku') or \
                        wordmap['lemma'].endswith('lku') or \
                        wordmap['lemma'].endswith('rku'):
                    wordmap['new_para'] = 'N_ALKU'
                elif wordmap['lemma'].endswith('hky') or \
                        wordmap['lemma'].endswith('lky') or \
                        wordmap['lemma'].endswith('rky'):
                    wordmap['new_para'] = 'N_HYLKY'
                elif wordmap['lemma'].endswith('hkö') or \
                        wordmap['lemma'].endswith('lkö') or \
                        wordmap['lemma'].endswith('rkö'):
                    wordmap['new_para'] = 'N_MÖRKÖ'
                elif wordmap['lemma'].endswith('ko'):
                    wordmap['new_para'] = 'N_TEKO'
                elif wordmap['lemma'].endswith('ku'):
                    wordmap['new_para'] = 'N_MAKU'
                elif wordmap['lemma'].endswith('ky'):
                    wordmap['new_para'] = 'N_NÄKY'
                elif wordmap['lemma'].endswith('kö'):
                    wordmap['new_para'] = 'N_NÄKÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'D'],
                                       ['ko', 'ku', 'ky', 'kö'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('po'):
                    wordmap['new_para'] = 'N_HEPO'
                elif wordmap['lemma'].endswith('pu'):
                    wordmap['new_para'] = 'N_APU'
                elif wordmap['lemma'].endswith('py'):
                    wordmap['new_para'] = 'N_KÄPY'
                elif wordmap['lemma'].endswith('pö'):
                    wordmap['new_para'] = 'N_LÖPÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'E'],
                                       ['po', 'pu', 'py', 'pö'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('to'):
                    wordmap['new_para'] = 'N_VETO'
                elif wordmap['lemma'].endswith('tu'):
                    wordmap['new_para'] = 'N_KUITU'
                elif wordmap['lemma'].endswith('ty'):
                    wordmap['new_para'] = 'N_VETY'
                elif wordmap['lemma'].endswith('tö'):
                    wordmap['new_para'] = 'N_HÄÄTÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'F'],
                                       ['to', 'tu', 'ty', 'tö'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nko'):
                    wordmap['new_para'] = 'N_RUNKO'
                elif wordmap['lemma'].endswith('nku'):
                    wordmap['new_para'] = 'N_VINKU'
                elif wordmap['lemma'].endswith('nky'):
                    wordmap['new_para'] = 'N_SÄNKY'
                elif wordmap['lemma'].endswith('nkö'):
                    wordmap['new_para'] = 'N_YLÄNKÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'G'],
                                       ['nko', 'nku', 'nky', 'nkö'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mpo'):
                    wordmap['new_para'] = 'N_SAMPO'
                elif wordmap['lemma'].endswith('mpu'):
                    wordmap['new_para'] = 'N_RUMPU'
                elif wordmap['lemma'].endswith('mpö'):
                    wordmap['new_para'] = 'N_LÄMPÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'H'],
                                       ['mpo', 'mpu', 'mpö'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('lto'):
                    wordmap['new_para'] = 'N_KIELTO'
                elif wordmap['lemma'].endswith('ltu'):
                    wordmap['new_para'] = 'N_HUOLITELTU'
                elif wordmap['lemma'].endswith('lty'):
                    wordmap['new_para'] = 'N_EPÄILTY'
                elif wordmap['lemma'].endswith('ltö'):
                    wordmap['new_para'] = 'N_SISÄLTÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'I'],
                                       ['lto', 'ltu', 'lty', 'ltö'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nto'):
                    wordmap['new_para'] = 'N_TUNTO'
                elif wordmap['lemma'].endswith('ntu'):
                    wordmap['new_para'] = 'N_LINTU'
                elif wordmap['lemma'].endswith('nty'):
                    wordmap['new_para'] = 'N_MÄNTY'
                elif wordmap['lemma'].endswith('ntö'):
                    wordmap['new_para'] = 'N_KÄÄNTÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'J'],
                                       ['nto', 'ntu', 'nty', 'ntö'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rto'):
                    wordmap['new_para'] = 'N_SIIRTO'
                elif wordmap['lemma'].endswith('rtu'):
                    wordmap['new_para'] = 'N_MERTU'
                elif wordmap['lemma'].endswith('rtö'):
                    wordmap['new_para'] = 'N_VÄRTÖ'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'K'],
                                       ['rto'])
            elif wordmap['kotus_av'] == 'M':
                if wordmap['lemma'].endswith('ko'):
                    wordmap['new_para'] = 'N_MALKO'
                elif wordmap['lemma'].endswith('ku'):
                    wordmap['new_para'] = 'N_LUKU'
                elif wordmap['lemma'].endswith('ky'):
                    wordmap['new_para'] = 'N_KYKY'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'M'],
                                       ['ko', 'ku', 'ky'])
            else:
                fail_guess_because(wordmap, ['N', 1], ['A–K', 'M'])
        elif tn == 2:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('o'):
                    wordmap['new_para'] = 'N_RUIPELO'
                elif wordmap['lemma'].endswith('u'):
                    wordmap['new_para'] = 'N_SEIKKAILU'
                elif wordmap['lemma'].endswith('y'):
                    wordmap['new_para'] = 'N_VEHKEILY'
                elif wordmap['lemma'].endswith('ö'):
                    wordmap['new_para'] = 'N_JÄÄTELÖ'
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_EUGENE'
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SELENE'
                else:
                    fail_guess_because(wordmap, ['N', 2, False],
                                       ['o', 'u', 'y', 'ö', 'e'])
            else:
                fail_guess_because(wordmap, ['N', 2], [False])
        elif tn == 3:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ao'):
                    wordmap['new_para'] = 'N_TUOMIO'
                elif wordmap['lemma'].endswith('ão'):
                    wordmap['new_para'] = 'N_TUOMIO'
                elif wordmap['lemma'].endswith('ae'):
                    wordmap['new_para'] = 'N_ZOMBIE'
                elif wordmap['lemma'].endswith('eo'):
                    wordmap['new_para'] = 'N_TUOMIO'
                elif wordmap['lemma'].endswith('io'):
                    wordmap['new_para'] = 'N_TUOMIO'
                elif wordmap['lemma'].endswith('iö'):
                    wordmap['new_para'] = 'N_HÄIRIÖ'
                elif wordmap['lemma'].endswith('ie') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ZOMBIE'
                elif wordmap['lemma'].endswith('ie') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_BERNIE'
                elif wordmap['lemma'].endswith('ye') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_BERNIE'
                elif wordmap['lemma'].endswith('oe'):
                    wordmap['new_para'] = 'N_ZOMBIE'
                elif wordmap['lemma'].endswith('ue'):
                    wordmap['new_para'] = 'N_ZOMBIE'
                elif wordmap['lemma'].endswith('yo'):
                    wordmap['new_para'] = 'N_TUOMIO'
                elif wordmap['lemma'].endswith('yö'):
                    wordmap['new_para'] = 'N_HÄIRIÖ'
                elif wordmap['lemma'].endswith('kolme'):
                    wordmap['new_para'] = 'N_AAMUKOLME'
                else:
                    fail_guess_because(wordmap, ['N', 3, False],
                                       ['ae', 'ao ão', 'eo', 'io', 'ie', 'iö', 'oe', 'ue', '*yo ye'])
            else:
                fail_guess_because(wordmap, ['N', 3], [False])
        elif tn == 4:
            if wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kko'):
                    wordmap['new_para'] = 'N_LEPAKKO'
                elif wordmap['lemma'].endswith('kkö'):
                    wordmap['new_para'] = 'N_YKSIKKÖ'
                else:
                    fail_guess_because(wordmap, ['N', 4, 'A'],
                                       ['kko', 'kkö'])
            else:
                fail_guess_because(wordmap, ['N', 4], ['A'])
        elif tn == 5:
            if not wordmap['lemma'].endswith('i'):
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_PUNK'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_ZEN'
                else:
                    fail_guess_because(wordmap, ['N', 5, False, '!i'],
                                       ['front', 'back'])
            elif not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_RUUVI'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_TYYLI'
                else:
                    fail_guess_because(wordmap, ['N', 5, False, 'i'],
                                       ['front', 'back'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LOKKI'
                elif wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_HÄKKI'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'A'],
                                       ['ki', 'front', 'back'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppi') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KUPPI'
                elif wordmap['lemma'].endswith('ppi') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_TYYPPI'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'B'],
                                       ['ppi', 'front', 'back'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tti') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KORTTI'
                elif wordmap['lemma'].endswith('tti') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SKEITTI'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'C'],
                                       ['tti', 'front', 'back'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LAKI'
                elif wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_HÄKKI'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'D'],
                                       ['ki', 'front', 'back'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('pi') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_HUPI'
                elif wordmap['lemma'].endswith('pi') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_RIIPI'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'E'],
                                       ['pi', 'back', 'front'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_TAUTI'
                elif wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_NIHTI'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'F'],
                                       ['ti', 'front', 'back'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nki') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_VANKI'
                elif wordmap['lemma'].endswith('nki') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_HÄMMINKI'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'F'],
                                       ['nki', 'front', 'back'])
            elif wordmap['kotus_av'] == 'H':
                # obs! lampi och rimpi kan vara 5 eller 7
                if wordmap['lemma'].endswith('mpi') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LAMMI'
                elif wordmap['lemma'].endswith('mpi') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_RIMMI'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'H'],
                                       ['mpi', 'front', 'back'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('lti') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_PELTI'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'I'],
                                       ['lti', 'back'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nti') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_SOINTI'
                elif wordmap['lemma'].endswith('nti') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_VIENTI'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'J'],
                                       ['nti', 'front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 5],
                                   ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'J'])
        elif tn == 6:
            if not wordmap['lemma'].endswith('i'):
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_STADION'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_BESSERWISSER'
                else:
                    fail_guess_because(wordmap, ['N', 6, False, '!i'],
                                       ['front', 'back'])
            elif not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KANAALI'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KEHVELI'
                else:
                    fail_guess_because(wordmap, ['N', 6, False, 'i'],
                                       ['front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 6],
                                   [False])
        elif tn == 7:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ONNI'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KIVI'
                else:
                    fail_guess_because(wordmap, ['N', 7, False],
                                       ['front', 'back'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppi') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_HAPPI'
                elif wordmap['lemma'].endswith('ppi') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_TYPPI'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'B'],
                                       ['ppi', 'front', 'back'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_NOKI'
                elif wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KÄKI'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'D'],
                                       ['ki', 'front', 'back'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('pi') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KORPI'
                elif wordmap['lemma'].endswith('pi') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KILPI'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'E'],
                                       ['pi', 'front', 'back'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LAHTI'
                elif wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_LEHTI'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'F'],
                                       ['hti', 'front', 'back'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nki') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ONKI'
                elif wordmap['lemma'].endswith('nki') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_HENKI'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'G'],
                                       ['nki', 'front', 'back'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mpi') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_SAMPI'
                elif wordmap['lemma'].endswith('mpi') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_RIMPI'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'H'],
                                       ['mpi', 'front', 'back'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ARKI'
                elif wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_JÄRKI'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'H'],
                                       ['ki', 'front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 7],
                                   [False, 'B', 'D', 'E', 'G', 'H'])
        elif tn == 8:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_NALLE'
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_NISSE'
                elif wordmap['lemma'].endswith('E') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_NALLE'
                elif wordmap['lemma'].endswith('E') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_NISSE'
                elif wordmap['lemma'].endswith('ë') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_NALLE'
                elif wordmap['lemma'].endswith('ě') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_NALLE'
                elif wordmap['lemma'].endswith('ě') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_NISSE'
                elif wordmap['lemma'].endswith('ë') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_NISSE'
                elif wordmap['lemma'].endswith('an') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_AAMUKAHDEKSAN'
                elif wordmap['lemma'].endswith('än') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_AAMUYHDEKSÄN'
                elif wordmap['lemma'].endswith('en') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_AAMUKYMMENEN'
                else:
                    fail_guess_because(wordmap, ['N', 8, False],
                                       ['e', 'ë', 'ě', 'front', 'back'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kke') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_NUKKE'
                elif wordmap['lemma'].endswith('kke') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_EKKE'
                else:
                    fail_guess_because(wordmap, ['N', 8, 'A'],
                                       ['kke', 'back'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppe') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_RAPPE'
                elif wordmap['lemma'].endswith('ppe') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_JEPPE'
                else:
                    fail_guess_because(wordmap, ['N', 8, 'B'],
                                       ['ppe', 'front'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tte') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LOTTE'
                elif wordmap['lemma'].endswith('tte') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_METTE'
                else:
                    fail_guess_because(wordmap, ['N', 8, 'C'],
                                       ['tte', 'front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 8],
                                   [False, 'A', 'B', 'C'],
                                   "New loan words do not simply walk into qualitative gradation")
        elif tn == 9:
            if not wordmap['kotus_av']:
                if wordmap['lemma'] in ["Kangasala", "Koskenala"]:
                    wordmap['new_para'] = 'N_KANGASALA'
                elif wordmap['lemma'].endswith('a'):
                    wordmap['new_para'] = 'N_KIRJA'
                elif wordmap['lemma'].endswith('A'):
                    wordmap['new_para'] = 'N_FIFA'
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_para'] = 'N_YMPÄRYSTÄ'
                else:
                    fail_guess_because(wordmap, ['N', 9, False],
                                       ['a', 'ä'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('ka'):
                    wordmap['new_para'] = 'N_POLITIIKKA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'A'],
                                       ['kka'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppa'):
                    wordmap['new_para'] = 'N_TIPPA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'B'],
                                       ['ppa'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tta'):
                    wordmap['new_para'] = 'N_MITTA'
                elif wordmap['lemma'].endswith('ttä'):
                    wordmap['new_para'] = 'N_YRITTÄ'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'C'],
                                       ['tta', 'ttä'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('aaka'):
                    wordmap['new_para'] = 'N_VAAKA'
                elif wordmap['lemma'].endswith('ka'):
                    wordmap['new_para'] = 'N_VIKA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'D'],
                                       ['ka'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('pa'):
                    wordmap['new_para'] = 'N_SALPA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'E'],
                                       ['pa'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('ta'):
                    wordmap['new_para'] = 'N_PATA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'F'],
                                       ['ta'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nka'):
                    wordmap['new_para'] = 'N_LANKA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'G'],
                                       ['nka'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mpa'):
                    wordmap['new_para'] = 'N_RAMPA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'H'],
                                       ['mpa'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('lta'):
                    wordmap['new_para'] = 'N_VALTA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'I'],
                                       ['lta'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nta'):
                    wordmap['new_para'] = 'N_KUTSUNTA'
                elif wordmap['lemma'].endswith('ntä'):
                    wordmap['new_para'] = 'N_KYSYNTÄ'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'J'],
                                       ['nta', 'ntä'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rta'):
                    wordmap['new_para'] = 'N_KERTA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'K'],
                                       ['rta'])
            else:
                fail_guess_because(wordmap, ['N', 9],
                                   [False, 'A-K'])
        elif tn == 10:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('a'):
                    if three_syllable(wordmap['stub']):
                        wordmap['new_para'] = 'N_ASEMA'
                    else:
                        wordmap['new_para'] = 'N_VOIMA'
                elif wordmap['lemma'].endswith('A'):
                    wordmap['new_para'] = 'N_FIFA'
                elif wordmap['lemma'].endswith('ă'):
                    wordmap['new_para'] = 'N_VODĂ'
                elif wordmap['lemma'].endswith('ä'):
                    if three_syllable(wordmap['stub']):
                        wordmap['new_para'] = 'N_ELÄMÄ'
                    else:
                        wordmap['new_para'] = ['N_HÖPÖTTÄJÄ']
                elif wordmap['lemma'].endswith('an'):
                    wordmap['new_para'] = 'N_AAMUKAHDEKSAN'
                elif wordmap['lemma'].endswith('än'):
                    wordmap['new_para'] = 'N_AAMUYHDEKSÄN'
                else:
                    fail_guess_because(wordmap, ['N', 10, False],
                                       ['a ă', 'ä'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('ka'):
                    wordmap['new_para'] = 'N_LUOKKA'
                elif wordmap['lemma'].endswith('kä'):
                    wordmap['new_para'] = 'N_HÖLKKÄ'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'A'],
                                       ['kka', 'kkä'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppa'):
                    wordmap['new_para'] = 'N_KUOPPA'
                elif wordmap['lemma'].endswith('ppä'):
                    wordmap['new_para'] = 'N_SEPPÄ'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'B'],
                                       ['ppa', 'ppä'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tta'):
                    wordmap['new_para'] = 'N_ROTTA'
                elif wordmap['lemma'].endswith('ttä'):
                    wordmap['new_para'] = 'N_KENTTÄ'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'C'],
                                       ['tta', 'ttä'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('lka'):
                    wordmap['new_para'] = 'N_SULKA'
                elif wordmap['lemma'].endswith('lkä'):
                    wordmap['new_para'] = 'N_NÄLKÄ'
                elif wordmap['lemma'].endswith('uoka'):
                    wordmap['new_para'] = 'N_RUOKA'
                elif wordmap['lemma'].endswith('ka'):
                    wordmap['new_para'] = 'N_LOKA'
                elif wordmap['lemma'].endswith('kä'):
                    wordmap['new_para'] = 'N_REIKÄ'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'D'],
                                       ['ka', 'kä'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('pa'):
                    wordmap['new_para'] = 'N_LUPA'
                elif wordmap['lemma'].endswith('pä'):
                    wordmap['new_para'] = 'N_LEIPÄ'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'E'],
                                       ['pa', 'pä'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('ta'):
                    wordmap['new_para'] = 'N_SOTA'
                elif wordmap['lemma'].endswith('tä'):
                    wordmap['new_para'] = 'N_PÖYTÄ'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'F'],
                                       ['ta', 'tä'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nka'):
                    wordmap['new_para'] = 'N_HONKA'
                elif wordmap['lemma'].endswith('nkä'):
                    wordmap['new_para'] = 'N_KENKÄ'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'G'],
                                       ['nka', 'nkä'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mpa'):
                    wordmap['new_para'] = 'N_KOMPA'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'H'],
                                       ['mpa', 'mpä'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('lta'):
                    wordmap['new_para'] = 'N_MULTA'
                elif wordmap['lemma'].endswith('ltä'):
                    wordmap['new_para'] = 'N_SYLTÄ'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'I'],
                                       ['lta', 'ltä'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nta'):
                    wordmap['new_para'] = 'N_KUNTA'
                elif wordmap['lemma'].endswith('ntä'):
                    wordmap['new_para'] = 'N_HÄNTÄ'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'J'],
                                       ['nta', 'ntä'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rta'):
                    wordmap['new_para'] = 'N_HORTA'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'K'],
                                       ['rta'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('kä'):
                    wordmap['new_para'] = 'N_SELKÄ'
                elif wordmap['lemma'].endswith('ka'):
                    wordmap['new_para'] = 'N_OLKA'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'L'],
                                       ['kä'])
            else:
                fail_guess_because(wordmap, ['N', 10],
                                   [False, 'A-J', 'L'])
        elif tn == 11:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('a'):
                    wordmap['new_para'] = 'N_PROBLEEMA'
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_para'] = 'N_KÄPÄLÄ'
                else:
                    fail_guess_because(wordmap, ['N', 11, False],
                                       ['a', 'ä'])
            else:
                fail_guess_because(wordmap, ['N', 11],
                                   [False])
        elif tn == 12:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('a'):
                    wordmap['new_para'] = 'N_MAKKARA'
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_para'] = 'N_HÄKKYRÄ'
                elif wordmap['lemma'].endswith('A'):
                    wordmap['new_para'] = 'N_FIFA'
                else:
                    fail_guess_because(wordmap, ['N', 12, False],
                                       ['a', 'ä'])
            else:
                fail_guess_because(wordmap, ['N', 12],
                                   [False])
        elif tn == 13:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('a'):
                    wordmap['new_para'] = 'N_KITARA'
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_para'] = 'N_SIIVILÄ'
                else:
                    fail_guess_because(wordmap, ['N', 13, False],
                                       ['a', 'ä'])
            else:
                fail_guess_because(wordmap, ['N', 13],
                                   [False])
        elif tn == 14:
            if wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kka'):
                    wordmap['new_para'] = 'N_LUSIKKA'
                elif wordmap['lemma'].endswith('kkä'):
                    wordmap['new_para'] = 'N_KÄMMEKKÄ'
                else:
                    fail_guess_because(wordmap, ['N', 14, 'A'],
                                       ['kka', 'kkä'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppa'):
                    wordmap['new_para'] = 'N_ULAPPA'
                else:
                    fail_guess_because(wordmap, ['N', 14, 'B'],
                                       ['ppä'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tta'):
                    wordmap['new_para'] = 'N_POHATTA'
                else:
                    fail_guess_because(wordmap, ['N', 14, 'C'],
                                       ['tta'])
            else:
                fail_guess_because(wordmap, ['N', 14],
                                   ['A', 'B', 'C'])
        elif tn == 15:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('oa'):
                    wordmap['new_para'] = 'N_PIIROA'
                elif wordmap['lemma'].endswith('ôa'):
                    wordmap['new_para'] = 'N_PIIROA'
                elif wordmap['lemma'].endswith('ea'):
                    wordmap['new_para'] = 'N_SOKEA'
                elif wordmap['lemma'].endswith('eä'):
                    wordmap['new_para'] = 'N_LIPEÄ'
                elif wordmap['lemma'].endswith('ua'):
                    wordmap['new_para'] = 'N_TANHUA'
                else:
                    fail_guess_because(wordmap, ['N', 15, False],
                                       ['oa ôa', 'ea', 'eä', 'ua'])
            else:
                fail_guess_because(wordmap, ['N', 15],
                                   [False])
        elif tn == 16:
            if wordmap['kotus_av'] == 'H':
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_VANHEMPI'
                else:
                    fail_guess_because(wordmap, ['N', 16, 'H'],
                                       ['back'])
            else:
                fail_guess_because(wordmap, ['N', 16],
                                   ['H'])
        elif tn == 17:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aa'):
                    wordmap['new_para'] = 'N_VAINAA'
                elif wordmap['lemma'].endswith('ee') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_TOKEE'
                elif wordmap['lemma'].endswith('ee') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_LENTTEE'
                elif wordmap['lemma'].endswith('ii') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_VAANII'
                elif wordmap['lemma'].endswith('ii') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_TIHVII'
                elif wordmap['lemma'].endswith('oo'):
                    wordmap['new_para'] = 'N_TIENOO'
                elif wordmap['lemma'].endswith('uu'):
                    wordmap['new_para'] = 'N_LEIKKUU'
                elif wordmap['lemma'].endswith('yy'):
                    wordmap['new_para'] = 'N_HYÖTYY'
                elif wordmap['lemma'].endswith('ää'):
                    wordmap['new_para'] = 'N_PYHTÄÄ'
                elif wordmap['lemma'].endswith('öö'):
                    wordmap['new_para'] = 'N_YLÖÖ'
                else:
                    fail_guess_because(wordmap, ['N', 17, False],
                                       ['aa', 'ee', 'oo', 'uu', 'yy', 'ää', 'öö'])
            else:
                fail_guess_because(wordmap, ['N', 17],
                                   [False])
        elif tn == 18:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('a'):
                    wordmap['new_para'] = 'N_MAA'
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_MATEE'
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_TEE'
                elif wordmap['lemma'].endswith('i') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_HAI'
                elif wordmap['lemma'].endswith('i') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_PII'
                elif wordmap['lemma'].endswith('o'):
                    wordmap['new_para'] = 'N_OOKOO'
                elif wordmap['lemma'].endswith('u'):
                    wordmap['new_para'] = 'N_PUU'
                elif wordmap['lemma'].endswith('y'):
                    wordmap['new_para'] = 'N_PYY'
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_para'] = 'N_PÄÄ'
                elif wordmap['lemma'].endswith('ö'):
                    wordmap['new_para'] = 'N_KÖÖ'
                else:
                    fail_guess_because(wordmap, ['N', 18, False],
                                       ['a', 'e', 'i', 'o', 'u', 'y', 'ä', 'ö', 'back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 18],
                                   [False])
        elif tn == 19:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('uo'):
                    wordmap['new_para'] = 'N_VUO'
                elif wordmap['lemma'].endswith('ie') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_TIE'
                elif wordmap['lemma'].endswith('yö'):
                    wordmap['new_para'] = 'N_TYÖ'
                else:
                    fail_guess_because(wordmap, ['N', 19, False],
                                       ['ie', 'uo', 'yö'])
            else:
                fail_guess_because(wordmap, ['N', 19],
                                   [False])
        elif tn == 20:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aa'):
                    wordmap['new_para'] = 'N_NUGAA'
                elif wordmap['lemma'].endswith('ee') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_PATEE'
                elif wordmap['lemma'].endswith('ee') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_BIDEE'
                elif wordmap['lemma'].endswith('EE') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_PATEE'
                elif wordmap['lemma'].endswith('EE') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_BIDEE'
                elif wordmap['lemma'].endswith('oo'):
                    wordmap['new_para'] = 'N_TRIKOO'
                elif wordmap['lemma'].endswith('uu'):
                    wordmap['new_para'] = 'N_RAGUU'
                elif wordmap['lemma'].endswith('yy'):
                    wordmap['new_para'] = 'N_FONDYY'
                elif wordmap['lemma'].endswith('öö'):
                    wordmap['new_para'] = 'N_MILJÖÖ'
                else:
                    fail_guess_because(wordmap, ['N', 20, False],
                                       ['aa', 'ee', 'oo', 'uu', 'yy', 'öö'])
            else:
                fail_guess_because(wordmap, ['N', 20],
                                   [False])
        elif tn == 21:
            if not wordmap['kotus_av']:
                if not wordmap['stem_vowel']:
                    # No pre-defined pronunciation, use guessing
                    if wordmap['lemma'].endswith('ae'):
                        wordmap['new_para'] = 'N_REGGAE'
                    elif wordmap['lemma'].endswith('ie') and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_BRASSERIE'
                    elif wordmap['lemma'].endswith('ie') and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_BRIE'
                    elif wordmap['lemma'].endswith('ci'):
                        wordmap['new_para'] = 'N_JOCKEY'
                    elif wordmap['lemma'].endswith('ay') or wordmap['lemma'].endswith('ey'):
                        if len(wordmap['lemma']) < 5:
                            wordmap['new_para'] = 'N_GAY'
                        else:
                            wordmap['new_para'] = 'N_JOCKEY'
                    elif wordmap['lemma'].endswith('oy') or wordmap['lemma'].endswith('uy'):
                        wordmap['new_para'] = 'N_COWBOY'
                    elif wordmap['lemma'].endswith('y'):
                        wordmap['new_para'] = 'N_SPOTIFY'
                    else:
                        wordmap['stem_vowel'] = wordmap['lemma'][-1]
                if wordmap['stem_vowel']:
                    # Pre-defined pronunciation or last ortographic vowel if
                    # not handled above
                    if wordmap['stem_vowel'] in 'aAáàâãăąā':
                        wordmap['new_para'] = 'N_CHACHACHA'
                    elif wordmap['stem_vowel'] in 'eEéèêėěęē' and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_ROSÉ'
                    elif wordmap['stem_vowel'] in 'eEéèêëėěęē' and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_BÉBÉ'
                    elif wordmap['stem_vowel'] in 'iIíìîïī' and (wordmap['lemma'][-2] == 'a' or
                                                                 wordmap['lemma'][-2] == 'e'):
                        if len(wordmap['lemma']) < 5:
                            wordmap['new_para'] = 'N_GAY'
                        else:
                            wordmap['new_para'] = 'N_JOCKEY'
                    elif wordmap['stem_vowel'] in 'iIíìîïī' and (wordmap['lemma'][-2] == 'o' or
                                                                 wordmap['lemma'][-2] == 'u'):
                        wordmap['new_para'] = 'N_COWBOY'
                    elif wordmap['stem_vowel'] in 'iIíìîïī' and wordmap['lemma'][-1] == 'y':
                        wordmap['new_para'] = 'N_SPOTIFY'
                    elif wordmap['stem_vowel'] in 'iIíìîïī' and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_BRASSERIE'
                    elif wordmap['stem_vowel'] in 'iIíìîïī' and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_BRIE'
                    elif wordmap['stem_vowel'] in 'oOóòôõōå':
                        wordmap['new_para'] = 'N_ESQUIMAU'
                    elif wordmap['stem_vowel'] in 'uUúùûū':
                        wordmap['new_para'] = 'N_KUNGFU'
                    elif wordmap['stem_vowel'] in 'yYýÿüű':
                        wordmap['new_para'] = 'N_FONDUE'
                    elif wordmap['stem_vowel'] in 'öÖøő':
                        wordmap['new_para'] = 'N_MALMÖ'
                if not wordmap['new_para']:
                    fail_guess_because(wordmap, ['N', 21, False],
                                       ['gay', 'eéè', "etc."], "unhandled stem type for 21 - using #")
                    wordmap['new_para'] = '#'
            else:
                fail_guess_because(wordmap, ['N', 21],
                                   [False])
        elif tn == 22:
            if not wordmap['kotus_av']:
                # Known pronunciations
                if wordmap['stem_vowel'] == 'a':
                    wordmap['new_para'] = 'N_NOUGAT'
                elif wordmap['stem_vowel'] == 'e' and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_PARFAIT'
                elif wordmap['stem_vowel'] == 'e' and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_BEIGNET'
                elif wordmap['stem_vowel'] == 'i' and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_VERSAILLES'
                elif wordmap['stem_vowel'] == 'i' and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_BEIGNET'  # !
                elif wordmap['stem_vowel'] == 'o':
                    wordmap['new_para'] = 'N_BORDEAUX'
                elif wordmap['stem_vowel'] == 'u':
                    wordmap['new_para'] = 'N_SHOW'
                elif wordmap['stem_vowel'] == 'y':
                    wordmap['new_para'] = 'N_CAMUS'
                elif wordmap['stem_vowel'] == 'ö':
                    wordmap['new_para'] = 'N_MONSIEUR'
                # Guessed pronunciations
                elif wordmap['lemma'].endswith('j'):
                    wordmap['new_para'] = 'N_SERGEJ'
                elif wordmap['lemma'].endswith('ah'):
                    wordmap['new_para'] = 'N_NOUGAT'
                elif wordmap['lemma'].endswith('at'):
                    wordmap['new_para'] = 'N_NOUGAT'
                elif wordmap['lemma'].endswith('ait'):
                    wordmap['new_para'] = 'N_PARFAIT'
                elif wordmap['lemma'].endswith('et'):
                    wordmap['new_para'] = 'N_BEIGNET'
                elif wordmap['lemma'].endswith('ot'):
                    wordmap['new_para'] = 'N_BORDEAUX'
                elif wordmap['lemma'].endswith('os'):
                    wordmap['new_para'] = 'N_BORDEAUX'
                elif wordmap['lemma'].endswith('us'):
                    wordmap['new_para'] = 'N_CAMUS'
                elif wordmap['lemma'].endswith('ois'):
                    wordmap['new_para'] = 'N_NOUGAT'
                elif wordmap['lemma'].endswith('ew'):
                    wordmap['new_para'] = 'N_SHOW'
                elif wordmap['lemma'].endswith('ow'):
                    wordmap['new_para'] = 'N_SHOW'
                elif wordmap['lemma'].endswith('ough'):
                    wordmap['new_para'] = 'N_SHOW'
                elif wordmap['lemma'].endswith('oux'):
                    wordmap['new_para'] = 'N_SHOW'
                elif wordmap['lemma'].endswith('aux'):
                    wordmap['new_para'] = 'N_BORDEAUX'
                elif wordmap['lemma'].endswith('eux'):
                    wordmap['new_para'] = 'N_MONSIEUR'
                else:
                    fail_guess_because(wordmap, ['N', 22, False],
                                       ['ait', 'ow', "etc."], "unhandled stem type for 22 - using #")
                    wordmap['new_para'] = '#'
            else:
                fail_guess_because(wordmap, ['N', 22],
                                   [False])
        elif tn == 23:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_TULI'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SYLI'
                else:
                    fail_guess_because(wordmap, ['N', 23, False],
                                       ['back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 23],
                                   [False])
        elif tn in [24, 26]:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_RUUHI'
                elif wordmap['harmony'] == 'front' and wordmap['lemma'].endswith('meri'):
                    wordmap['new_para'] = 'N_MERI'
                elif wordmap['harmony'] == 'front' and wordmap['lemma'].endswith('veri'):
                    wordmap['new_para'] = 'N_VERI'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_HIIRI'
                else:
                    fail_guess_because(wordmap, ['N', 24, 26, False],
                                       ['back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 24, 26],
                                   [False])
        elif tn == 25:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_TAIMI'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_LIEMI'
                else:
                    fail_guess_because(wordmap, ['N', 25, False],
                                       ['back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 25],
                                   [False])
        elif tn == 27:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('si'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_KAUSI'
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_KÖYSI'
                    else:
                        fail_guess_because(wordmap, ['N', 27, False, 'si'],
                                           ['back', 'front'])
                elif wordmap['lemma'].endswith('s'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_KUUS'
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_VIIS'
                    else:
                        fail_guess_because(wordmap, ['N', 27, False, 's'],
                                           ['back', 'front'])
                else:
                    fail_guess_because(wordmap, ['N', 27, False],
                                       ['si', 's'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('si'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_KAUSI'
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_KÖYSI'
                    else:
                        fail_guess_because(wordmap, ['N', 27, 'F', 'si'],
                                           ['back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 27],
                                   [False])
        elif tn == 28:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('nsi'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_PONSI'
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_LÄNSI'
                    else:
                        fail_guess_because(wordmap, ['N', 28, 'F', 'nsi'],
                                           ['back', 'front'])
                elif wordmap['lemma'].endswith('rsi'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_VARSI'
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_VIRSI'
                    else:
                        fail_guess_because(wordmap, ['N', 28, 'F', 'rsi'],
                                           ['back', 'front'])
                elif wordmap['lemma'].endswith('lsi'):
                    if wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_JÄLSI'
                    else:
                        fail_guess_because(wordmap, ['N', 28, 'F', 'lsi'],
                                           ['front'])
                else:
                    fail_guess_because(wordmap, ['N', 28, False],
                                       ['nsi', 'rsi', 'lsi'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nsi'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_PONSI'
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_LÄNSI'
                    else:
                        fail_guess_because(wordmap, ['N', 28, 'J', 'nsi'],
                                           ['back', 'front'])
                else:
                    fail_guess_because(wordmap, ['N', 28, 'J'],
                                       ['nsi'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rsi'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_VARSI'
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_VIRSI'
                    else:
                        fail_guess_because(wordmap, ['N', 28, 'K', 'rsi'],
                                           ['back', 'front'])
                else:
                    fail_guess_because(wordmap, ['N', 28, 'K'],
                                       ['rsi'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('lsi'):
                    if wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_JÄLSI'
                    else:
                        fail_guess_because(wordmap, ['N', 28, 'I', 'lsi'],
                                           ['front'])
                else:
                    fail_guess_because(wordmap, ['N', 28, 'I'],
                                       ['lsi'])
            else:
                fail_guess_because(wordmap, ['N', 28],
                                   [False, 'J', 'K', 'I'])
        elif tn == 29:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('psi'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_LAPSI'
                    else:
                        fail_guess_because(wordmap, ['N', 29, False, 'psi'],
                                           ['back'])
                elif wordmap['lemma'].endswith('ksi'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_UKSI'
                    else:
                        fail_guess_because(wordmap, ['N', 29, False, 'ksi'],
                                           ['back'])
                else:
                    fail_guess_because(wordmap, ['N', 29, False],
                                       ['psi'])
            else:
                fail_guess_because(wordmap, ['N', 29],
                                   [False])
        elif tn == 30:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('tsi'):
                    if wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_VEITSI'
                    else:
                        fail_guess_because(wordmap, ['N', 30, False, 'tsi'],
                                           ['front'])
                else:
                    fail_guess_because(wordmap, ['N', 30, False],
                                       ['tsi'])
            else:
                fail_guess_because(wordmap, ['N', 30],
                                   [False])
        elif tn == 31:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ksi'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_HAAKSI'
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_AAMUYKSI'
                    else:
                        fail_guess_because(wordmap, ['N', 31, False, 'ksi'],
                                           ['back', 'front'])
                else:
                    fail_guess_because(wordmap, ['N', 31, False],
                                       ['ksi'])
            else:
                fail_guess_because(wordmap, ['N', 31],
                                   [False])
        elif tn == 32:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_JOUTSEN'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SIEMEN'
                else:
                    fail_guess_because(wordmap, ['N', 32, False],
                                       ['back', 'front'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_AJATAR'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_TYTÄR'
                else:
                    fail_guess_because(wordmap, ['N', 32, 'C'],
                                       ['back', 'front'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_IEN'
                else:
                    fail_guess_because(wordmap, ['N', 32, 'D'],
                                       ['back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 32],
                                   [False, 'C', 'D'])
        elif tn == 33:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_PUHELIN'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_ELIN'
                else:
                    fail_guess_because(wordmap, ['N', 33, False],
                                       ['back', 'front'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kin') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_HÄRKIN'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'A'],
                                       ['kin', 'front'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tin') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_SUODATIN'
                elif wordmap['lemma'].endswith('tin') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_HEITIN'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'C'],
                                       ['tin', 'back', 'front'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('in') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_PUIN'
                elif wordmap['lemma'].endswith('in') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_PYYHIN'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'D'],
                                       ['in', 'back', 'front'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('vin') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_RAAVIN'
                elif wordmap['lemma'].endswith('vin') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SÄRVIN'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'E'],
                                       ['vin', 'back', 'front'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('din') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_VAADIN'
                elif wordmap['lemma'].endswith('din') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SÄÄDIN'
                elif wordmap['lemma'].endswith('don'):
                    wordmap['new_para'] = 'N_JÄRVITAHDON'
                elif wordmap['lemma'].endswith('dun'):
                    wordmap['new_para'] = 'N_LAIDUN'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'F'],
                                       ['din', 'dun', 'back', 'front'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('llin') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ASKELLIN'
                elif wordmap['lemma'].endswith('llin') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SIVELLIN'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'I'],
                                       ['llin', 'back', 'front'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnin') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_MUUNNIN'
                elif wordmap['lemma'].endswith('in') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KÄÄNNIN'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'J'],
                                       ['nnin', 'back', 'front'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rrin') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KIHARRIN'
                elif wordmap['lemma'].endswith('rrin') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KIERRIN'
                elif wordmap['lemma'].endswith('rroin'):
                    wordmap['new_para'] = 'N_KERROIN'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'K'],
                                       ['rrin', 'rroin', 'back', 'front'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('jin') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_POLJIN'
                elif wordmap['lemma'].endswith('jin') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_NYLJIN'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'J'],
                                       ['jin', 'back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 33],
                                   [False, 'A', 'C-F', 'I-L'])
        elif wordmap['kotus_tn'] == 34:
            if wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pan'):
                    wordmap['new_para'] = 'N_HAPAN'
                else:
                    fail_guess_because(wordmap, ['N', 34, 'B'],
                                       ['pan'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('ton'):
                    wordmap['new_para'] = 'N_OSATON'
                elif wordmap['lemma'].endswith('tön'):
                    wordmap['new_para'] = 'N_NIMETÖN'
                elif wordmap['lemma'].endswith('toin'):
                    wordmap['new_para'] = 'N_KALATOIN'
                elif wordmap['lemma'].endswith('töin'):
                    wordmap['new_para'] = 'N_NIMETÖIN'
                else:
                    fail_guess_because(wordmap, ['N', 34, 'C'],
                                       ['ton', 'tön', 'toin', 'töin'])
            else:
                fail_guess_because(wordmap, ['N', 34], [False, 'C'])
        elif wordmap['kotus_tn'] == 35:
            if wordmap['kotus_av'] == 'H':
                if wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_LÄMMIN'
                else:
                    fail_guess_because(wordmap, ['N', 35, False],
                                       ['back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 35],
                                   ['H'])
        elif wordmap['kotus_tn'] == 36:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KYLÄNVANHIN'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_LÄHIN'
                else:
                    fail_guess_because(wordmap, ['N', 36, 'J'],
                                       ['jin', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 36],
                                   [False], "cannot have gradation")
        elif wordmap['kotus_tn'] == 37:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('vasen'):
                    wordmap['new_para'] = 'N_VASEN'
                else:
                    fail_guess_because(wordmap, ['N', 37, False],
                                       ['vasen'])
            else:
                fail_guess_because(wordmap, ['N', 37],
                                   [False], "cannot have gradation")
        elif wordmap['kotus_tn'] == 38:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_AAKKOSTAMINEN'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KYLKIÄINEN'
                else:
                    fail_guess_because(wordmap, ['N', 38, False],
                                       ['front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 38],
                                   [False], "cannot have gradation")
        elif wordmap['kotus_tn'] == 39:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_VAKUUTUS'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_RÄJÄYTYS'
                else:
                    fail_guess_because(wordmap, ['N', 39, False],
                                       ['front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 39],
                                   [False], "cannot have gradation")
        elif wordmap['kotus_tn'] == 40:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_para'] = 'N_TOULAT'
                elif wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_AAKKOSELLISUUS'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KÖYHYYS'
                else:
                    fail_guess_because(wordmap, ['N', 38, False],
                                       ['front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 38],
                                   [False], "cannot have gradation")
        elif wordmap['kotus_tn'] == 41:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('as'):
                    wordmap['new_para'] = 'N_PATSAS'
                elif wordmap['lemma'].endswith('es') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ARISTOTELES'
                elif wordmap['lemma'].endswith('es') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KIRVES'
                elif wordmap['lemma'].endswith('is') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_RUUMIS'
                elif wordmap['lemma'].endswith('is') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_DIMITRIS'
                elif wordmap['lemma'].endswith('os'):
                    wordmap['new_para'] = 'N_UROS'
                elif wordmap['lemma'].endswith('äs'):
                    wordmap['new_para'] = 'N_ÄYRÄS'
                else:
                    fail_guess_because(wordmap, ['N', 41, False],
                                       ['as', 'es', 'is', 'os', 'äs', 'front', 'back'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kas'):
                    wordmap['new_para'] = 'N_ASUKAS'
                elif wordmap['lemma'].endswith('käs'):
                    wordmap['new_para'] = 'N_KÄRSÄKÄS'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'A'],
                                       ['kas', 'käs'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pas'):
                    wordmap['new_para'] = 'N_SAAPAS'
                elif wordmap['lemma'].endswith('päs'):
                    wordmap['new_para'] = 'N_RYPÄS'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'B'],
                                       ['pas', 'päs'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tas'):
                    wordmap['new_para'] = 'N_RATAS'
                elif wordmap['lemma'].endswith('tes') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KORTES'
                elif wordmap['lemma'].endswith('tis') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ALTIS'
                elif wordmap['lemma'].endswith('tis') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KELTIS'
                elif wordmap['lemma'].endswith('täs'):
                    wordmap['new_para'] = 'N_MÄTÄS'
                elif wordmap['lemma'].endswith('tus'):
                    wordmap['new_para'] = 'N_VANTUS'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'C'],
                                       ['tas', 'tis', 'tus', 'täs', 'front'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('as'):
                    wordmap['new_para'] = 'N_VARAS'
                elif wordmap['lemma'].endswith('es') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_IES'
                elif wordmap['lemma'].endswith('is') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_RUIS'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'D'],
                                       ['as', 'es', 'is', 'front', 'back'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('vas'):
                    wordmap['new_para'] = 'N_VARVAS'
                elif wordmap['lemma'].endswith('väs'):
                    wordmap['new_para'] = 'N_SEIVÄS'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'E'],
                                       ['vas', 'väs'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('das'):
                    wordmap['new_para'] = 'N_TEHDAS'
                elif wordmap['lemma'].endswith('des') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LUODES'
                elif wordmap['lemma'].endswith('des') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_LÄHDES'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'F'],
                                       ['das', 'des'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('ngas'):
                    wordmap['new_para'] = 'N_KANGAS'
                elif wordmap['lemma'].endswith('ngäs'):
                    wordmap['new_para'] = 'N_KÖNGÄS'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'G'],
                                       ['gas', 'gäs'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmas'):
                    wordmap['new_para'] = 'N_HAMMAS'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'H'],
                                       ['mmas'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('llas'):
                    wordmap['new_para'] = 'N_ALLAS'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'I'],
                                       ['llas', 'lles', 'back'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnas'):
                    wordmap['new_para'] = 'N_KINNAS'
                elif wordmap['lemma'].endswith('nnäs'):
                    wordmap['new_para'] = 'N_RYNNÄS'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'J'],
                                       ['nnas', 'nnäs'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('ras'):
                    wordmap['new_para'] = 'N_PORRAS'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'K'],
                                       ['rras'])
            else:
                fail_guess_because(wordmap, ['N', 41],
                                   [False, 'A-K'])
        elif wordmap['kotus_tn'] == 42:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('mies') or wordmap['lemma'].endswith('Mies'):
                    wordmap['new_para'] = 'N_MIES'
                else:
                    fail_guess_because(wordmap, ['N', 42, False],
                                       ['mies'])
            else:
                fail_guess_because(wordmap, ['N', 42],
                                   [False], "cannot gradate")
        elif wordmap['kotus_tn'] == 43:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ut'):
                    wordmap['new_para'] = 'N_OLUT'
                elif wordmap['lemma'].endswith('yt'):
                    wordmap['new_para'] = 'N_NEITSYT'
                else:
                    fail_guess_because(wordmap, ['N', 43, False],
                                       ['ut', 'yt'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('ut'):
                    wordmap['new_para'] = 'N_POIUT'
                else:
                    fail_guess_because(wordmap, ['N', 43, 'D'],
                                       ['ut'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmyt'):
                    wordmap['new_para'] = 'N_IMMYT'
                else:
                    fail_guess_because(wordmap, ['N', 43, 'H'],
                                       ['mmyt'])
            else:
                fail_guess_because(wordmap, ['N', 43],
                                   [False, 'H'])
        elif wordmap['kotus_tn'] == 44:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ät'):
                    wordmap['new_para'] = 'N_KEVÄT'
                elif wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KAARET'
                elif wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_HÄMET'
                else:
                    fail_guess_because(wordmap, ['N', 44, False],
                                       ['ät', 'et'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KORTET'
                else:
                    fail_guess_because(wordmap, ['N', 44, 'C'],
                                       ['tet'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LOUET'
                else:
                    fail_guess_because(wordmap, ['N', 44, 'D'],
                                       ['et'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('det') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_AHDET'
                elif wordmap['lemma'].endswith('det') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_LÄHDET'
                else:
                    fail_guess_because(wordmap, ['N', 44, 'F'],
                                       ['det'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('get') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_INGET'
                else:
                    fail_guess_because(wordmap, ['N', 44, 'F'],
                                       ['det'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('llet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_VUOLLET'
                else:
                    fail_guess_because(wordmap, ['N', 44, 'I'],
                                       ['llet'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LANNET'
                elif wordmap['lemma'].endswith('nnet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_RINNET'
                else:
                    fail_guess_because(wordmap, ['N', 44, 'J'],
                                       ['nnet'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rret') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KAARRET'
                elif wordmap['lemma'].endswith('rret') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_VIIRRET'
                else:
                    fail_guess_because(wordmap, ['N', 44, 'K'],
                                       ['rret'])
            else:
                fail_guess_because(wordmap, ['N', 44],
                                   [False, 'C', 'D', 'F', 'G', 'I', 'J', 'K'])
        elif wordmap['kotus_tn'] == 45:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('s'):
                    wordmap['new_para'] = 'N_TUHANNES'
                else:
                    fail_guess_because(wordmap, ['N', 45, False],
                                       ['s'])
            else:
                fail_guess_because(wordmap, ['N', 45],
                                   [False], "cannot gradate")
        elif wordmap['kotus_tn'] == 46:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('tuhat'):
                    wordmap['new_para'] = 'N_VUOSITUHAT'
                else:
                    fail_guess_because(wordmap, ['N', 46, False],
                                       ['tuhat'])
            else:
                fail_guess_because(wordmap, ['N', 46],
                                   [False], "cannot gradate")
        elif wordmap['kotus_tn'] == 47:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ut'):
                    wordmap['new_para'] = 'N_AIVOKUOLLUT'
                elif wordmap['lemma'].endswith('yt'):
                    wordmap['new_para'] = 'N_SIVISTYNYT'
                else:
                    fail_guess_because(wordmap, ['N', 47, False],
                                       ['yt'])
            else:
                fail_guess_because(wordmap, ['N', 47],
                                   [False], "cannot gradate")
        elif tn == 48:
            if wordmap['lemma'].endswith('e'):
                if not wordmap['kotus_av']:
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_ASTE'
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_PISTE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, False],
                                           ['front', 'back'])
                elif wordmap['kotus_av'] == 'A':
                    if wordmap['lemma'].endswith('ke') and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_KASTIKE'
                    elif wordmap['lemma'].endswith('ke') and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_LÄÄKE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'A'],
                                           ['ke', 'front', 'back'])
                elif wordmap['kotus_av'] == 'B':
                    if wordmap['lemma'].endswith('pe') and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_APE'
                    elif wordmap['lemma'].endswith('pe') and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_RIPE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'B'],
                                           ['pe', 'front', 'back'])
                elif wordmap['kotus_av'] == 'C':
                    if wordmap['lemma'].endswith('te') and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_OSOITE'
                    elif wordmap['lemma'].endswith('te') and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_KÄSITE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'C'],
                                           ['te', 'front', 'back'])
                elif wordmap['kotus_av'] == 'D':
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_KOE'
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_PYYHE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'D'],
                                           ['e', 'front', 'back'])
                elif wordmap['kotus_av'] == 'E':
                    if wordmap['lemma'].endswith('ve') and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_TARVE'
                    elif wordmap['lemma'].endswith('ve') and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_VIIVE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'E'],
                                           ['ve', 'front', 'back'])
                elif wordmap['kotus_av'] == 'F':
                    if wordmap['lemma'].endswith('de') and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_LUODE'
                    elif wordmap['lemma'].endswith('de') and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_KIDE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'F'],
                                           ['de', 'front', 'back'])
                elif wordmap['kotus_av'] == 'G':
                    if wordmap['lemma'].endswith('ge') and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_MIELENGE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'F'],
                                           ['ge', 'front'])
                elif wordmap['kotus_av'] == 'H':
                    if wordmap['lemma'].endswith('mme') and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_LUMME'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'H'],
                                           ['mme', 'back'])
                elif wordmap['kotus_av'] == 'I':
                    if wordmap['lemma'].endswith('lle') and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_VUOLLE'
                    elif wordmap['lemma'].endswith('lle') and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_MIELLE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'I'],
                                           ['lle', 'front', 'back'])
                elif wordmap['kotus_av'] == 'J':
                    if wordmap['lemma'].endswith('nne') and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_RAKENNE'
                    elif wordmap['lemma'].endswith('nne') and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_KIINNE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'J'],
                                           ['nne', 'front', 'back'])
                elif wordmap['kotus_av'] == 'K':
                    if wordmap['lemma'].endswith('rre') and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_AARRE'
                    elif wordmap['lemma'].endswith('rre') and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_KIERRE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'K'],
                                           ['rre', 'front', 'back'])
                elif wordmap['kotus_av'] == 'L':
                    if wordmap['lemma'].endswith('je') and wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_POHJE'
                    elif wordmap['lemma'].endswith('je') and wordmap['harmony'] == 'front':
                        wordmap['new_para'] = 'N_HYLJE'
                    else:
                        fail_guess_because(wordmap, ['N', 48, 'L'],
                                           ['je', 'front', 'back'])
                else:
                    fail_guess_because(wordmap, ['N', 48],
                                       [False, 'A-L'])
            elif wordmap['lemma'].endswith('i'):
                if not wordmap['kotus_av']:
                    if wordmap['harmony'] == 'back':
                        wordmap['new_para'] = 'N_ORI'
                    else:
                        fail_guess_because(wordmap, ['N', 48, False, 'i'],
                                           ['back'])
                else:
                    fail_guess_because(wordmap, ['N', 48, 'i'],
                                       [False])
            elif wordmap['lemma'].endswith('u'):
                if not wordmap['kotus_av']:
                    wordmap['new_para'] = 'N_KIIRU'
                else:
                    fail_guess_because(wordmap, ['N', 48, 'u'],
                                       [False])
            else:
                fail_guess_because(wordmap, ['N', 48],
                                   ['e', 'i', 'u'])
        elif tn == 49:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('al'):
                    wordmap['new_para'] = 'N_ASKAR'
                elif wordmap['lemma'].endswith('ar'):
                    wordmap['new_para'] = 'N_ASKAR'
                elif wordmap['lemma'].endswith('en') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ASKAR'
                elif wordmap['lemma'].endswith('el') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ASKAR'
                elif wordmap['lemma'].endswith('el') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KYYNEL'
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ASTE'
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_PISTE'
                else:
                    fail_guess_because(wordmap, ['N', 49, False],
                                       ['al ar', 'el en', 'e', 'front', 'back'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('en') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SÄEN'
                else:
                    fail_guess_because(wordmap, ['N', 49, 'D'],
                                       ['en', 'front'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('val'):
                    wordmap['new_para'] = 'N_TAIVAL'
                else:
                    fail_guess_because(wordmap, ['N', 49, 'E'],
                                       ['al', 'front'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('dar'):
                    wordmap['new_para'] = 'N_UDAR'
                else:
                    fail_guess_because(wordmap, ['N', 49, 'F'],
                                       ['dar'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nger') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_PENGER'
                else:
                    fail_guess_because(wordmap, ['N', 49, 'G'],
                                       ['ger', 'front'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmel') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_OMMEL'
                elif wordmap['lemma'].endswith('mmel') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_VEMMEL'
                elif wordmap['lemma'].endswith('mmol'):
                    wordmap['new_para'] = 'N_LOMMOL'
                else:
                    fail_guess_because(wordmap, ['N', 49, 'H'],
                                       ['mmel', 'mmol', 'front', 'back'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnar'):
                    wordmap['new_para'] = 'N_PIENNAR'
                elif wordmap['lemma'].endswith('nnel') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KANNEL'
                elif wordmap['lemma'].endswith('nner') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_MANNER'
                elif wordmap['lemma'].endswith('nner') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KINNER'
                else:
                    fail_guess_because(wordmap, ['N', 49, 'J'],
                                       ['nnar', 'nnel', 'nner', 'front'])
            elif wordmap['kotus_av'] == 'T':
                if wordmap['lemma'].endswith('auer'):
                    wordmap['new_para'] = 'N_AUER'
                else:
                    fail_guess_because(wordmap, ['N', 49, 'T'],
                                       ['auer'])
            else:
                fail_guess_because(wordmap, ['N', 49],
                                   [False, 'D-H', 'J', 'T'])
        elif tn == 1007:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('veli') or wordmap['lemma'].endswith('Veli'):
                    wordmap['new_para'] = 'N_VELI'
                else:
                    fail_guess_because(wordmap, ['N', 7, False, 'VELI'],
                                       ['veli'], 'must be veli')
            else:
                fail_guess_because(wordmap, ['N', 7, 'VELI'],
                                   [False], 'Cannot gradate')
        elif tn == 1009:
            if wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('aika') or wordmap['lemma'].endswith('Aika'):
                    wordmap['new_para'] = 'N_AIKA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'D', 'AIKA'],
                                       ['aika'], 'must be aika')
            elif not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aika') or wordmap['lemma'].endswith('Aika'):
                    fail_guess_because(wordmap, ["aika"], ["D"])
                    exit(1)
                    wordmap['new_para'] = 'N_AIKA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'D', 'AIKA'],
                                       ['aika'], 'must be aika')
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('aika'):
                    wordmap['new_para'] = 'N_AIKA'
                    fail_guess_because(wordmap, ["aika"], ["D"])
                    exit(1)
                else:
                    fail_guess_because(wordmap, ['N', 9, 'D', 'AIKA'],
                                       ['aika'], 'must be aika')
            else:
                fail_guess_because(wordmap, ['N', 9, 'AIKA'],
                                   ['D'], 'must be D')
        elif tn == 1010:
            if wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('poika') or wordmap['lemma'].endswith('Poika'):
                    wordmap['new_para'] = 'N_POIKA'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'D', 'POIKA'],
                                       ['poika'], 'must be poika')
            elif not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('poika'):
                    fail_guess_because(wordmap, ["poika"], ["D"])
                    exit(1)
                else:
                    fail_guess_because(wordmap, ['N', 10, 'D', 'POIKA'],
                                       ['poika'], 'must be poika')
            else:
                fail_guess_because(wordmap, ['N', 10, 'POIKA'],
                                   ['D'], 'must be D')
        elif tn == 1024:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('meri') or wordmap['lemma'].endswith('Meri'):
                    wordmap['new_para'] = 'N_MERI'
                else:
                    fail_guess_because(wordmap, ['N', 24, False, 'MERI'],
                                       ['meri'], 'must be meri')
            else:
                fail_guess_because(wordmap, ['N', 24, 'MERI'],
                                   [False], 'must be 0')
        elif tn == 1026:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('veri') or wordmap['lemma'].endswith('Veri'):
                    wordmap['new_para'] = 'N_VERI'
                else:
                    fail_guess_because(wordmap, ['N', 24, 'False', 'VERI'],
                                       ['veri'], 'must be veri')
            else:
                fail_guess_because(wordmap, ['N', 26, 'VERI'],
                                   [False], 'must be 0')
        elif tn == 99 and not wordmap['is_proper']:
            fail_guess_because(wordmap, ['N', 99], [99],
                               "Illegal class for N, 99 can only apply to P (and PropN)")
            wordmap['new_para'] = '#'
        elif tn == 99 and wordmap['is_proper']:
            wordmap['new_para'] = 'N_VAASAN'
        else:
            fail_guess_because(wordmap, ['N'],
                               ['1-49', '99', '1007-1026'])
    else:
        if not wordmap['lemma'].endswith('t'):
            fail_guess_because(wordmap, ['N', 'PLT'],
                               ['-t'], 'not a plt lemma')
        elif tn == 1:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ot'):
                    wordmap['new_para'] = 'N_AIVOT'
                elif wordmap['lemma'].endswith('yt'):
                    wordmap['new_para'] = 'N_PÖKSYT'
                elif wordmap['lemma'].endswith('ut'):
                    wordmap['new_para'] = 'N_HOUSUT'
                elif wordmap['lemma'].endswith('öt'):
                    wordmap['new_para'] = 'N_PÖLLÖT'
                else:
                    fail_guess_because(wordmap, ['N', 1, False, 'PLT'],
                                       ['ot', 'ut', 'yt'])
            elif wordmap['kotus_av'] in ['A', 'D']:
                if wordmap['lemma'].endswith('ot'):
                    wordmap['new_para'] = 'N_JOUKOT'
                elif wordmap['lemma'].endswith('ut'):
                    wordmap['new_para'] = 'N_FARKUT'
                elif wordmap['lemma'].endswith('yt'):
                    wordmap['new_para'] = 'N_JYLKYT'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'A', 'PLT'],
                                       ['kot', 'kut', 'kyt'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('put'):
                    wordmap['new_para'] = 'N_RAPUT'
                elif wordmap['lemma'].endswith('pot'):
                    wordmap['new_para'] = 'N_PEIPOT'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'B', 'PLT'],
                                       ['put'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tyt'):
                    wordmap['new_para'] = 'N_NIITYT'
                elif wordmap['lemma'].endswith('tut'):
                    wordmap['new_para'] = 'N_NIITUT'
                elif wordmap['lemma'].endswith('tot'):
                    wordmap['new_para'] = 'N_ROITOT'
                elif wordmap['lemma'].endswith('töt'):
                    wordmap['new_para'] = 'N_TYTÖT'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'C', 'PLT'],
                                       ['tyt', 'tut', 'töt'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('vut'):
                    wordmap['new_para'] = 'N_RAVUT'
                elif wordmap['lemma'].endswith('vot'):
                    wordmap['new_para'] = 'N_KOUVOT'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'E', 'PLT'],
                                       ['vut'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('dot'):
                    wordmap['new_para'] = 'N_PIDOT'
                elif wordmap['lemma'].endswith('dyt'):
                    wordmap['new_para'] = 'N_KÄÄDYT'
                elif wordmap['lemma'].endswith('döt'):
                    wordmap['new_para'] = 'N_KYDÖT'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'F', 'PLT'],
                                       ['dot', 'dyt'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('got'):
                    wordmap['new_para'] = 'N_LINGOT'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'F', 'PLT'],
                                       ['dot', 'dyt'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmut'):
                    wordmap['new_para'] = 'N_KUMMUT'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'H', 'PLT'],
                                       ['mmut'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('llot'):
                    wordmap['new_para'] = 'N_AALLOT'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'I', 'PLT'],
                                       ['llot'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnot'):
                    wordmap['new_para'] = 'N_OPINNOT'
                elif wordmap['lemma'].endswith('nnyt'):
                    wordmap['new_para'] = 'N_MÄNNYT'
                elif wordmap['lemma'].endswith('nnöt'):
                    wordmap['new_para'] = 'N_SÄÄNNÖT'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'J', 'PLT'],
                                       ['nnot', 'nnöt'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rrot'):
                    wordmap['new_para'] = 'N_KAARROT'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'K', 'PLT'],
                                       ['rrot'])
            else:
                fail_guess_because(wordmap, ['N', 1, 'PLT'],
                                   [False, 'A-F', 'I', 'J'])
        elif tn == 2:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ot'):
                    wordmap['new_para'] = 'N_PIPPALOT'
                elif wordmap['lemma'].endswith('ut'):
                    wordmap['new_para'] = 'N_NEUVOTTELUT'
                elif wordmap['lemma'].endswith('öt'):
                    wordmap['new_para'] = 'N_JÄRJESTÖT'
                else:
                    fail_guess_because(wordmap, ['N', 2, False, 'PLT'],
                                       ['ot', 'ut', 'öt'])
            else:
                fail_guess_because(wordmap, ['N', 2, 'PLT'],
                                   [False])
        elif tn == 3:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ot'):
                    wordmap['new_para'] = 'N_RAUNIOT'
                elif wordmap['lemma'].endswith('öt'):
                    wordmap['new_para'] = 'N_YHTIÖT'
                else:
                    fail_guess_because(wordmap, ['N', 3, False, 'PLT'],
                                       ['ot', 'öt'])
            else:
                fail_guess_because(wordmap, ['N', 3, 'PLT'],
                                   [False])
        elif tn == 4:
            if wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('öt'):
                    wordmap['new_para'] = 'N_TÖLPÄKÖT'
                elif wordmap['lemma'].endswith('ot'):
                    wordmap['new_para'] = 'N_LUOLIKOT'
                else:
                    fail_guess_because(wordmap, ['N', 4, 'A', 'PLT'],
                                       ['ot'])
            else:
                fail_guess_because(wordmap, ['N', 4, 'PLT'],
                                   [False])
        elif tn == 5:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('it') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LASIT'
                elif wordmap['lemma'].endswith('it') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_LIIVIT'
                else:
                    fail_guess_because(wordmap, ['N', 5, False, 'PLT'],
                                       ['it', 'back'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kit') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_PANKIT'
                elif wordmap['lemma'].endswith('kit') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_FÄNRIKIT'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'A', 'PLT'],
                                       ['kit', 'back'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pit') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KLUMPIT'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'C', 'PLT'],
                                       ['pit', 'back'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tit') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KASTANJETIT'
                elif wordmap['lemma'].endswith('tit') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_PINSETIT'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'C', 'PLT'],
                                       ['tit', 'back'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('dit') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_TAUDIT'
                elif wordmap['lemma'].endswith('dit') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_PIHDIT'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'F', 'PLT'],
                                       ['dit'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('ngit') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_TONGIT'
                elif wordmap['lemma'].endswith('ngit') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SYÖMINGIT'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'G', 'PLT'],
                                       ['ngit', 'back'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmit') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LAMMIT'
                elif wordmap['lemma'].endswith('mmit') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_RIMMIT'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'H', 'PLT'],
                                       ['mmit', 'back'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnit') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_TUNNIT'
                else:
                    fail_guess_because(wordmap, ['N', 5, 'J', 'PLT'],
                                       ['nnit', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 5, 'PLT'],
                                   [False, 'C', 'F', 'G', 'J'])
        elif tn == 6:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_FARMARIT'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_BIKINIT'
                else:
                    fail_guess_because(wordmap, ['N', 6, False, 'PLT'],
                                       ['back'])
            else:
                fail_guess_because(wordmap, ['N', 6, 'PLT'],
                                   [False])
        elif tn == 7:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_SAKSET'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_RIPSET'
                else:
                    fail_guess_because(wordmap, ['N', 7, False, 'PLT'],
                                       ['front', 'back'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LAET'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_MÄET'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'D', 'PLT'],
                                       ['front'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KORVET'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_RIIVET'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'E', 'PLT'],
                                       ['front'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LAHDET'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_LEHDET'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'F', 'PLT'],
                                       ['front'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_LÄNGET'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'G', 'PLT'],
                                       ['front'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LAMMET'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'H', 'PLT'],
                                       ['front'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ONNET'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'J', 'PLT'],
                                       ['front'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KÄRJET'
                else:
                    fail_guess_because(wordmap, ['N', 7, 'L', 'PLT'],
                                       ['front'])
            else:
                fail_guess_because(wordmap, ['N', 7, 'PLT'],
                                   [False, 'F', 'G', 'H', 'J', 'L'])
        elif tn == 8:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_RAVET'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_BÄNET'
                else:
                    fail_guess_because(wordmap, ['N', 8, False, 'PLT'],
                                       ['back'])
            else:
                fail_guess_because(wordmap, ['N', 8, 'PLT'],
                                   [False])
        elif tn == 9:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_para'] = 'N_VARAT'
                else:
                    fail_guess_because(wordmap, ['N', 9, False, 'PLT'],
                                       ['at'])
            elif wordmap['kotus_av'] in ['A', 'D']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_para'] = 'N_PAIKAT'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'A', 'PLT'],
                                       ['kat'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pat'):
                    wordmap['new_para'] = 'N_HIPAT'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'B', 'PLT'],
                                       ['pat'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tat'):
                    wordmap['new_para'] = 'N_RIUTAT'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'B', 'PLT'],
                                       ['pat'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('vat'):
                    wordmap['new_para'] = 'N_TAVAT'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'E', 'PLT'],
                                       ['vat'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('dat'):
                    wordmap['new_para'] = 'N_RAUDAT'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'F', 'PLT'],
                                       ['dat'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('gat'):
                    wordmap['new_para'] = 'N_RANGAT'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'G', 'PLT'],
                                       ['gat'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('llat'):
                    wordmap['new_para'] = 'N_VALLAT'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'I', 'PLT'],
                                       ['llat'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnat'):
                    wordmap['new_para'] = 'N_RANNAT'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'J', 'PLT'],
                                       ['llat'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rrat'):
                    wordmap['new_para'] = 'N_KARRAT'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'K', 'PLT'],
                                       ['rrat'])
            else:
                fail_guess_because(wordmap, ['N', 9, 'PLT'],
                                   [False, 'A-G', 'I-K'])
        elif tn == 10:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_para'] = 'N_JUHLAT'
                elif wordmap['lemma'].endswith('ät'):
                    wordmap['new_para'] = 'N_KÄRÄJÄT'
                else:
                    fail_guess_because(wordmap, ['N', 10, False, 'PLT'],
                                       ['at', 'ät'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kat'):
                    wordmap['new_para'] = 'N_SUKAT'
                elif wordmap['lemma'].endswith('kät'):
                    wordmap['new_para'] = 'N_SÄRKÄT'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'A', 'PLT'],
                                       ['kat', 'kät'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pat'):
                    wordmap['new_para'] = 'N_KUOPAT'
                elif wordmap['lemma'].endswith('pät'):
                    wordmap['new_para'] = 'N_TÖLPÄT'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'B', 'PLT'],
                                       ['pat'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tat'):
                    wordmap['new_para'] = 'N_ROTAT'
                elif wordmap['lemma'].endswith('tät'):
                    wordmap['new_para'] = 'N_KENTÄT'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'C', 'PLT'],
                                       ['tät'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('ät'):
                    wordmap['new_para'] = 'N_REIÄT'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'D', 'PLT'],
                                       ['ät'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('vat'):
                    wordmap['new_para'] = 'N_JUOVAT'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'E', 'PLT'],
                                       ['vat'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('dat'):
                    wordmap['new_para'] = 'N_LUHDAT'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'D', 'PLT'],
                                       ['dat'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('ngät'):
                    wordmap['new_para'] = 'N_KENGÄT'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'G', 'PLT'],
                                       ['ngät'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnat'):
                    wordmap['new_para'] = 'N_KUNNAT'
                elif wordmap['lemma'].endswith('nnät'):
                    wordmap['new_para'] = 'N_HÄNNÄT'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'J', 'PLT'],
                                       ['nnat'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('ljät'):
                    wordmap['new_para'] = 'N_SELJÄT'
                else:
                    fail_guess_because(wordmap, ['N', 10, 'L', 'PLT'],
                                       ['ljät'])
            else:
                fail_guess_because(wordmap, ['N', 10, 'PLT'],
                                   [False, 'A', 'B', 'D', 'F' 'G', 'J'])
        elif tn == 11:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_para'] = 'N_KIHARAT'
                else:
                    fail_guess_because(wordmap, ['N', 11, False, 'PLT'],
                                       ['at'])
            else:
                fail_guess_because(wordmap, ['N', 11, 'PLT'],
                                   [False])
        elif tn == 12:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_para'] = 'N_MARKKINAT'
                elif wordmap['lemma'].endswith('ät'):
                    wordmap['new_para'] = 'N_RÄMIÄT'
                else:
                    fail_guess_because(wordmap, ['N', 12, False, 'PLT'],
                                       ['at', 'ät'])
            else:
                fail_guess_because(wordmap, ['N', 12, 'PLT'],
                                   [False])
        elif tn == 13:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_para'] = 'N_KASTILJAT'
                else:
                    fail_guess_because(wordmap, ['N', 13, False, 'PLT'],
                                       ['at'])
            else:
                fail_guess_because(wordmap, ['N', 13, 'PLT'],
                                   [False])
        elif tn == 14:
            if wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kat'):
                    wordmap['new_para'] = 'N_SILAKAT'
                else:
                    fail_guess_because(wordmap, ['N', 14, 'A', 'PLT'],
                                       ['at'])
            else:
                fail_guess_because(wordmap, ['N', 14, 'PLT'],
                                   ['A'])
        elif tn == 15:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_para'] = 'N_HOPEAT'
                elif wordmap['lemma'].endswith('ät'):
                    wordmap['new_para'] = 'N_RÄMEÄT'
                else:
                    fail_guess_because(wordmap, ['N', 15, False, 'PLT'],
                                       ['at'])
            else:
                fail_guess_because(wordmap, ['N', 15, 'PLT'],
                                   [False])
        elif tn == 16:
            if wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmat'):
                    wordmap['new_para'] = 'N_VANHEMMAT'
                else:
                    fail_guess_because(wordmap, ['N', 16, 'H', 'PLT'],
                                       ['at'])
            else:
                fail_guess_because(wordmap, ['N', 16, 'PLT'],
                                   ['H'])
        elif tn == 17:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aat'):
                    wordmap['new_para'] = 'N_HARMAAT'
                elif wordmap['lemma'].endswith('oot'):
                    wordmap['new_para'] = 'N_TALKOOT'
                elif wordmap['lemma'].endswith('yyt'):
                    wordmap['new_para'] = 'N_HYNTTYYT'
                elif wordmap['lemma'].endswith('äät'):
                    wordmap['new_para'] = 'N_PÖLHÄÄT'
                else:
                    fail_guess_because(wordmap, ['N', 17, False, 'PLT'],
                                       ['oot', 'yyt', 'äät'])
            else:
                fail_guess_because(wordmap, ['N', 17, 'PLT'],
                                   [False])
        elif tn == 18:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aat'):
                    wordmap['new_para'] = 'N_ITÄMAAT'
                elif wordmap['lemma'].endswith('ait'):
                    wordmap['new_para'] = 'N_HAIT'
                elif wordmap['lemma'].endswith('uut'):
                    wordmap['new_para'] = 'N_PUUT'
                elif wordmap['lemma'].endswith('yyt'):
                    wordmap['new_para'] = 'N_PYYT'
                elif wordmap['lemma'].endswith('äät'):
                    wordmap['new_para'] = 'N_HÄÄT'
                else:
                    fail_guess_because(wordmap, ['N', 18, False, 'PLT'],
                                       ['aat', 'ait', 'uut', 'yyt', 'äät'])
            else:
                fail_guess_because(wordmap, ['N', 18, 'PLT'],
                                   [False])
        elif tn == 19:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('iet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_TIET'
                elif wordmap['lemma'].endswith('uot'):
                    wordmap['new_para'] = 'N_SUOT'
                elif wordmap['lemma'].endswith('yöt'):
                    wordmap['new_para'] = 'N_TYÖT'
                else:
                    fail_guess_because(wordmap, ['N', 19, False, 'PLT'],
                                       ['iet', 'uot', 'yöt'])
            else:
                fail_guess_because(wordmap, ['N', 19, 'PLT'],
                                   [False])
        elif tn == 20:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ööt'):
                    wordmap['new_para'] = 'N_MILJÖÖT'
                else:
                    fail_guess_because(wordmap, ['N', 20, False, 'PLT'],
                                       ['ööt'])
            else:
                fail_guess_because(wordmap, ['N', 20, 'PLT'],
                                   [False])
        elif tn == 21:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('át'):
                    wordmap['new_para'] = 'N_LIVVADIEVÁT'
                else:
                    fail_guess_because(wordmap, ['N', 21, False, 'PLT'],
                                       ['át'])
            else:
                fail_guess_because(wordmap, ['N', 21, 'PLT'],
                                   [False])
        elif tn == 25:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('met') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_TOIMET'
                elif wordmap['lemma'].endswith('met') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_NIEMET'
                else:
                    fail_guess_because(wordmap, ['N', 25, False, 'PLT'],
                                       ['met'])
            else:
                fail_guess_because(wordmap, ['N', 25, 'PLT'],
                                   [False])
        elif tn in [24, 26]:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_SAARET'
                elif wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SÄÄRET'
                else:
                    fail_guess_because(wordmap, ['N', 26, False, 'PLT'],
                                       ['et'])
            else:
                fail_guess_because(wordmap, ['N', 26, 'PLT'],
                                   [False])
        elif tn == 27:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('det') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_VUODET'
                else:
                    fail_guess_because(wordmap, ['N', 27, False, 'PLT'],
                                       ['det'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('det') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_VUODET'
                else:
                    fail_guess_because(wordmap, ['N', 27, False, 'PLT'],
                                       ['det'])
            else:
                fail_guess_because(wordmap, ['N', 27, 'PLT'],
                                   [False])
        elif tn == 28:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('nnet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KANNET'
                elif wordmap['lemma'].endswith('rret') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_VIRRET'
                else:
                    fail_guess_because(wordmap, ['N', 28, False, 'PLT'],
                                       ['nnet', 'rret'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KANNET'
                elif wordmap['lemma'].endswith('nnet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KYNNET'
                else:
                    fail_guess_because(wordmap, ['N', 28, 'J', 'PLT'],
                                       ['nnet'])
            else:
                fail_guess_because(wordmap, ['N', 28, 'PLT'],
                                   ['J'])
        elif tn == 32:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_HÖYHENET'
                else:
                    fail_guess_because(wordmap, ['N', 32, False, 'PLT'],
                                       ['et'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('taret'):
                    wordmap['new_para'] = 'N_LIPOTTARET'
                elif wordmap['lemma'].endswith('täret'):
                    wordmap['new_para'] = 'N_KIRITTÄRET'
                else:
                    fail_guess_because(wordmap, ['N', 32, 'C', 'PLT'],
                                       ['taret'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('kenet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_IKENET'
                else:
                    fail_guess_because(wordmap, ['N', 32, 'D', 'PLT'],
                                       ['kenet'])
            else:
                fail_guess_because(wordmap, ['N', 32, 'PLT'],
                                   [False])
        elif tn == 33:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('met') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ATERIMET'
                elif wordmap['lemma'].endswith('met') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_KERITSIMET'
                else:
                    fail_guess_because(wordmap, ['N', 33, False, 'PLT'],
                                       ['met'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('ttimet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_HOKSOTTIMET'
                elif wordmap['lemma'].endswith('ttimet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SYNNYTTIMET'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'C', 'PLT'],
                                       ['ttimet'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('kimet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_PUKIMET'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'D', 'PLT'],
                                       ['kimet'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('timet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ROHTIMET'
                elif wordmap['lemma'].endswith('timet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_VETIMET'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'F', 'PLT'],
                                       ['timet'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('ntimet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ANTIMET'
                else:
                    fail_guess_because(wordmap, ['N', 33, 'J', 'PLT'],
                                       ['ntimet'])
            else:
                fail_guess_because(wordmap, ['N', 33, 'PLT'],
                                   [False, 'C', 'D', 'F', 'J'])
        elif tn == 34:
            if wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('mat'):
                    wordmap['new_para'] = 'N_SIUNAAMATTOMAT'
                elif wordmap['lemma'].endswith('mät'):
                    wordmap['new_para'] = 'N_TYÖTTÖMÄT'
                else:
                    fail_guess_because(wordmap, ['N', 34, 'C', 'PLT'],
                                       ['mät'])
            else:
                fail_guess_because(wordmap, ['N', 34, 'PLT'],
                                   ['C'])
        elif tn == 38:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('set') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_RAPPUSET'
                elif wordmap['lemma'].endswith('set') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_VIHKIÄISET'
                else:
                    fail_guess_because(wordmap, ['N', 38, False, 'PLT'],
                                       ['eet'])
            else:
                fail_guess_because(wordmap, ['N', 38, 'PLT'],
                                   [False])
        elif tn == 39:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('set') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_SERKUKSET'
                elif wordmap['lemma'].endswith('set') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_YSTÄVYKSET'
                else:
                    fail_guess_because(wordmap, ['N', 39, False, 'PLT'],
                                       ['eet'])
            else:
                fail_guess_because(wordmap, ['N', 39, 'PLT'],
                                   [False])
        elif tn == 40:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('det') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_OIKEUDET'
                else:
                    fail_guess_because(wordmap, ['N', 40, False, 'PLT'],
                                       ['eet'])
            else:
                fail_guess_because(wordmap, ['N', 40, 'PLT'],
                                   [False])
        elif tn == 41:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aat'):
                    wordmap['new_para'] = 'N_VALJAAT'
                elif wordmap['lemma'].endswith('äät'):
                    wordmap['new_para'] = 'N_KYNNÄÄT'
                else:
                    fail_guess_because(wordmap, ['N', 41, False, 'PLT'],
                                       ['aat'])
            elif wordmap['kotus_av'] in ['A', 'D']:
                if wordmap['lemma'].endswith('kaat'):
                    wordmap['new_para'] = 'N_TIKKAAT'
                elif wordmap['lemma'].endswith('käät'):
                    wordmap['new_para'] = 'N_KILPIKKÄÄT'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'A', 'PLT'],
                                       ['kaat'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppaat'):
                    wordmap['new_para'] = 'N_RUOPPAAT'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'C', 'PLT'],
                                       ['ttaat'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('ttaat'):
                    wordmap['new_para'] = 'N_RATTAAT'
                elif wordmap['lemma'].endswith('ttyyt'):
                    wordmap['new_para'] = 'N_RYNTTYYT'
                elif wordmap['lemma'].endswith('ttäät'):
                    wordmap['new_para'] = 'N_MÄTTÄÄT'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'C', 'PLT'],
                                       ['ttaat'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('paat'):
                    wordmap['new_para'] = 'N_VARPAAT'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'E', 'PLT'],
                                       ['rpaat'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('taat'):
                    wordmap['new_para'] = 'N_TEHTAAT'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'F', 'PLT'],
                                       ['taat'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nkaat'):
                    wordmap['new_para'] = 'N_RENKAAT'
                elif wordmap['lemma'].endswith('nkahat'):
                    wordmap['new_para'] = 'N_KANKAHAT'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'G', 'PLT'],
                                       ['nkaat'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mpaat'):
                    wordmap['new_para'] = 'N_ROMPAAT'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'H', 'PLT'],
                                       ['mpaat'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('ltaat'):
                    wordmap['new_para'] = 'N_MALTAAT'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'I', 'PLT'],
                                       ['ltaat'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('ntäät'):
                    wordmap['new_para'] = 'N_RYNTÄÄT'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'J', 'PLT'],
                                       ['ntäät'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rtaat'):
                    wordmap['new_para'] = 'N_PORTAAT'
                else:
                    fail_guess_because(wordmap, ['N', 41, 'K', 'PLT'],
                                       ['rtaat'])
            else:
                fail_guess_because(wordmap, ['N', 41, 'PLT'],
                                   [False, 'A', 'C', 'F', 'G', 'J', 'K'])
        elif tn == 42:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('iehet'):
                    wordmap['new_para'] = 'N_MIEHET'
                else:
                    fail_guess_because(wordmap, ['N', 42, False, 'PLT'],
                                       ['het'])
            else:
                fail_guess_because(wordmap, ['N', 42, 'PLT'],
                                   [False])
        elif tn == 43:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('uet'):
                    wordmap['new_para'] = 'N_MATKUET'
                else:
                    fail_guess_because(wordmap, ['N', 43, False, 'PLT'],
                                       ['uet'])
            else:
                fail_guess_because(wordmap, ['N', 43, 'PLT'],
                                   [False])
        elif tn == 47:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('eet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_LIITTOUTUNEET'
                elif wordmap['lemma'].endswith('eet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_HÄVINNEET'
                else:
                    fail_guess_because(wordmap, ['N', 47, False, 'PLT'],
                                       ['eet'])
            else:
                fail_guess_because(wordmap, ['N', 47, 'PLT'],
                                   [False])
        elif tn == 48:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('eet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_HIUTALEET'
                elif wordmap['lemma'].endswith('eet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_RÄMEET'
                else:
                    fail_guess_because(wordmap, ['N', 48, False, 'PLT'],
                                       ['eet'])
            elif wordmap['kotus_av'] in ['A', 'D']:
                if wordmap['lemma'].endswith('keet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KUULOKKEET'
                elif wordmap['lemma'].endswith('keet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_SILMÄKKEET'
                else:
                    fail_guess_because(wordmap, ['N', 48, 'AD', 'PLT'],
                                       ['peet'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('peet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_KAMPPEET'
                else:
                    fail_guess_because(wordmap, ['N', 48, 'B', 'PLT'],
                                       ['peet'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('teet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_VAATTEET'
                elif wordmap['lemma'].endswith('teet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_HYNTTEET'
                else:
                    fail_guess_because(wordmap, ['N', 48, 'C', 'PLT'],
                                       ['teet'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('peet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_TARPEET'
                else:
                    fail_guess_because(wordmap, ['N', 48, 'E', 'PLT'],
                                       ['teet'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('teet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_SUHTEET'
                elif wordmap['lemma'].endswith('teet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_TIETEET'
                else:
                    fail_guess_because(wordmap, ['N', 48, 'F', 'PLT'],
                                       ['teet'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nteet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_SALONTEET'
                elif wordmap['lemma'].endswith('nteet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_RINTEET'
                else:
                    fail_guess_because(wordmap, ['N', 48, 'J', 'PLT'],
                                       ['teet'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rteet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_MURTEET'
                else:
                    fail_guess_because(wordmap, ['N', 48, 'J', 'PLT'],
                                       ['teet'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('keet') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ALKEET'
                elif wordmap['lemma'].endswith('keet') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_PERKEET'
                else:
                    fail_guess_because(wordmap, ['N', 48, 'L', 'PLT'],
                                       ['teet'])
            else:
                fail_guess_because(wordmap, ['N', 48, 'PLT'],
                                   ['F'])
        elif tn == 49:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_SAMMALET'
                else:
                    fail_guess_because(wordmap, ['N', 49, False, 'PLT'],
                                       ['eet'])
            else:
                fail_guess_because(wordmap, ['N', 49, 'PLT'],
                                   [False])
        elif tn == 1007:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('veljet') or wordmap['lemma'].endswith('Veljet'):
                    wordmap['new_para'] = 'N_VELJET'
                else:
                    fail_guess_because(wordmap, ['N', 7, False, 'PLT'],
                                       ['veljet'])
            elif wordmap['kotus_av'] in ['D', 'L']:
                if wordmap['lemma'].endswith('veljet') or wordmap['lemma'].endswith('Veljet'):
                    wordmap['new_para'] = 'N_VELJET'
                else:
                    fail_guess_because(wordmap, ['N', 7, False, 'PLT'],
                                       ['veljet'])
            else:
                fail_guess_because(wordmap, ['N', 7, 'PLT'],
                                   [False, 'D', 'L'])
        elif tn == 1010:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('pojat') or wordmap['lemma'].endswith('Pojat'):
                    wordmap['new_para'] = 'N_POJAT'
                else:
                    fail_guess_because(wordmap, ['N', 10, False, 'PLT'],
                                       ['pojat'])
            elif wordmap['kotus_av'] in ['D', 'L']:
                if wordmap['lemma'].endswith('pojat') or wordmap['lemma'].endswith('Pojat'):
                    wordmap['new_para'] = 'N_POJAT'
                else:
                    fail_guess_because(wordmap, ['N', 10, False, 'PLT'],
                                       ['pojat'])
            else:
                fail_guess_because(wordmap, ['N', 10, 'PLT'],
                                   [False, 'D', 'L'])
        else:
            fail_guess_because(wordmap, ['N', 'PLT'],
                               [1, 2, 3, 8])
    return wordmap


def guess_new_adjective(wordmap):
    tn = int(wordmap['kotus_tn'])
    if tn == 1:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('o') or wordmap['lemma'].endswith('O'):
                wordmap['new_para'] = 'A_TUMMAHKO'
            elif wordmap['lemma'].endswith('u') or wordmap['lemma'].endswith('U'):
                wordmap['new_para'] = 'A_VALKAISTU'
            elif wordmap['lemma'].endswith('y') or wordmap['lemma'].endswith('Y'):
                wordmap['new_para'] = 'A_HÄPÄISTY'
            elif wordmap['lemma'].endswith('ö'):
                wordmap['new_para'] = 'A_HÖLÖ'
            else:
                fail_guess_because(wordmap, ['A', 1, False],
                                   ['o O', 'u', 'yY', 'ö'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('ko'):
                wordmap['new_para'] = 'A_KOLKKO'
            elif wordmap['lemma'].endswith('ku'):
                wordmap['new_para'] = 'A_VIRKKU'
            elif wordmap['lemma'].endswith('ky'):
                wordmap['new_para'] = 'A_SÄIKKY'
            elif wordmap['lemma'].endswith('kö'):
                wordmap['new_para'] = 'A_KÖKKÖ'
            else:
                fail_guess_because(wordmap, ['A', 1, 'A'],
                                   ['ko', 'ku', 'ky', 'kö'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppo'):
                wordmap['new_para'] = 'A_SUIPPO'
            elif wordmap['lemma'].endswith('ppu'):
                wordmap['new_para'] = 'A_IKÄLOPPU'
            elif wordmap['lemma'].endswith('ppö'):
                wordmap['new_para'] = 'A_LÖRPPÖ'
            else:
                fail_guess_because(wordmap, ['A', 1, 'B'],
                                   ['ppo', 'ppu', 'ppö'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tto'):
                wordmap['new_para'] = 'A_VELTTO'
            elif wordmap['lemma'].endswith('ttu'):
                wordmap['new_para'] = 'A_VIMMATTU'
            elif wordmap['lemma'].endswith('tty'):
                wordmap['new_para'] = 'A_YLENNETTY'
            elif wordmap['lemma'].endswith('ttö'):
                wordmap['new_para'] = 'A_KYYTTÖ'
            else:
                fail_guess_because(wordmap, ['A', 1, 'C'],
                                   ['tto', 'ttu', 'tty', 'ttö'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('ko'):
                wordmap['new_para'] = 'A_LAKO'
            else:
                fail_guess_because(wordmap, ['A', 1, 'D'],
                                   ['ko'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('po'):
                wordmap['new_para'] = 'A_KELPO'
            else:
                fail_guess_because(wordmap, ['A', 1, 'E'],
                                   ['po'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('to'):
                wordmap['new_para'] = 'A_MIETO'
            elif wordmap['lemma'].endswith('tu'):
                wordmap['new_para'] = 'A_VIIPALOITU'
            elif wordmap['lemma'].endswith('ty'):
                wordmap['new_para'] = 'A_YKSILÖITY'
            elif wordmap['lemma'].endswith('tö'):
                fail_guess_because(wordmap, ['A', 1, 'F'],
                                   ['to', 'tu', 'ty'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nko'):
                wordmap['new_para'] = 'A_LENKO'
            else:
                fail_guess_because(wordmap, ['A', 1, 'G'],
                                   ['nko'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('lto'):
                wordmap['new_para'] = 'A_MELTO'
            elif wordmap['lemma'].endswith('ltu'):
                wordmap['new_para'] = 'A_PARANNELTU'
            elif wordmap['lemma'].endswith('lty'):
                wordmap['new_para'] = 'A_VÄHÄTELTY'
            else:
                fail_guess_because(wordmap, ['A', 1, 'I'],
                                   ['lto', 'ltu', 'lty'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nto'):
                wordmap['new_para'] = 'A_VENTO'
            elif wordmap['lemma'].endswith('ntu'):
                wordmap['new_para'] = 'A_PANTU'
            elif wordmap['lemma'].endswith('nty'):
                wordmap['new_para'] = 'A_MENTY'
            else:
                fail_guess_because(wordmap, ['A', 1, 'J'],
                                   ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rto'):
                wordmap['new_para'] = 'A_MARTO'
            elif wordmap['lemma'].endswith('rtu'):
                wordmap['new_para'] = 'A_PURTU'
            elif wordmap['lemma'].endswith('rty'):
                wordmap['new_para'] = 'A_PIERTY'
            else:
                fail_guess_because(wordmap, ['A', 1, 'K'],
                                   ['rto', 'rto', 'rty'])
        else:
            fail_guess_because(wordmap, ['A', 1], ['A–K'])
    elif tn == 2:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('o'):
                wordmap['new_para'] = 'A_KOHELO'
            elif wordmap['lemma'].endswith('ö'):
                wordmap['new_para'] = 'A_LÖPERÖ'
            else:
                fail_guess_because(wordmap, ['A', 2, False],
                                   ['o', 'ö'])
        else:
            fail_guess_because(wordmap, ['A', 2], [False])
    elif tn == 3:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('io'):
                wordmap['new_para'] = 'A_AUTIO'
            elif wordmap['lemma'].endswith('iö'):
                wordmap['new_para'] = 'A_RIIVIÖ'
            else:
                fail_guess_because(wordmap, ['A', 3, False],
                                   ['io', 'iö'])
        else:
            fail_guess_because(wordmap, ['A', 3], [False])
    elif tn == 4:
        if wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('kko'):
                wordmap['new_para'] = 'A_HUPAKKO'
            else:
                fail_guess_because(wordmap, ['A', 4, 'A'],
                                   ['kko'])
        else:
            fail_guess_because(wordmap, ['A', 4], ['A'])
    elif tn == 5:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_ABNORMI'
            elif wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_STYDI'
            else:
                fail_guess_because(wordmap, ['A', 5, False, 'i'],
                                   ['front', 'back'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_OPAAKKI'
            elif wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_PINKKI'
            else:
                fail_guess_because(wordmap, ['A', 5, 'A'],
                                   ['ki', 'front', 'back'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppi') and wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_SIPPI'
            else:
                fail_guess_because(wordmap, ['A', 5, 'B'],
                                   ['ppi', 'front', 'back'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tti') and wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_HURTTI'
            elif wordmap['lemma'].endswith('tti') and wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_VÄÄRTTI'
            else:
                fail_guess_because(wordmap, ['A', 5, 'C'],
                                   ['tti', 'front', 'back'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_TUHTI'
            elif wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_REHTI'
            else:
                fail_guess_because(wordmap, ['A', 5, 'F'],
                                   ['ti', 'front', 'back'])
    elif tn == 6:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_ABNORMAALI'
            elif wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_ÖYKKÄRI'
            else:
                fail_guess_because(wordmap, ['A', 6, False, 'i'],
                                   ['front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 6],
                               [False])
    elif tn == 8:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_TOOPE'
            elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_BEIGE'
            else:
                fail_guess_because(wordmap, ['A', 8, False],
                                   ['e', 'front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 8],
                               [False])
    elif tn == 9:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a') or wordmap['lemma'].endswith('A'):
                wordmap['new_para'] = 'A_AAVA'
            else:
                fail_guess_because(wordmap, ['A', 9, False],
                                   ['a'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('ka'):
                wordmap['new_para'] = 'A_TARKKA'
            else:
                fail_guess_because(wordmap, ['A', 9, 'A'],
                                   ['kka'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tta'):
                wordmap['new_para'] = 'A_MATTA'
            else:
                fail_guess_because(wordmap, ['A', 9, 'C'],
                                   ['tta'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('ka'):
                wordmap['new_para'] = 'A_TARKKA'
            else:
                fail_guess_because(wordmap, ['A', 9, 'D'],
                                   ['ka'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('pa'):
                wordmap['new_para'] = 'A_HALPA'
            else:
                fail_guess_because(wordmap, ['A', 9, 'E'],
                                   ['pa'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('ta'):
                wordmap['new_para'] = 'A_EHTA'
            else:
                fail_guess_because(wordmap, ['A', 9, 'F'],
                                   ['ta'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nka'):
                wordmap['new_para'] = 'A_SANKA'
            else:
                fail_guess_because(wordmap, ['A', 9, 'F'],
                                   ['ta'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mpa'):
                wordmap['new_para'] = 'A_RAMPA'
            else:
                fail_guess_because(wordmap, ['A', 9, 'H'],
                                   ['mpa'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nta'):
                wordmap['new_para'] = 'A_VIHANTA'
        else:
            fail_guess_because(wordmap, ['A', 9],
                               [False, 'A-K'])
    elif tn == 10:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a') or wordmap['lemma'].endswith('A'):
                if three_syllable(wordmap['stub']):
                    wordmap['new_para'] = 'A_MATALA'
                else:
                    wordmap['new_para'] = 'A_RUMA'
            elif wordmap['lemma'].endswith('ä'):
                if three_syllable(wordmap['stub']):
                    wordmap['new_para'] = 'A_TERÄVÄ'
                else:
                    wordmap['new_para'] = 'A_TYHMÄ'
            else:
                fail_guess_because(wordmap, ['A', 10, False],
                                   ['a', 'ä'])
        elif wordmap['kotus_av'] in ['A', 'D']:
            if wordmap['lemma'].endswith('ka'):
                wordmap['new_para'] = 'A_HOIKKA'
            elif wordmap['lemma'].endswith('kä'):
                wordmap['new_para'] = 'A_MYKKÄ'
            else:
                fail_guess_because(wordmap, ['A', 10, 'A'],
                                   ['kka', 'kkä'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppa'):
                wordmap['new_para'] = 'A_POPPA'
            elif wordmap['lemma'].endswith('ppä'):
                wordmap['new_para'] = 'A_HÖMPPÄ'
            else:
                fail_guess_because(wordmap, ['A', 10, 'B'],
                                   ['ppa', 'ppä'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('pa'):
                wordmap['new_para'] = 'A_VOIPA'
            elif wordmap['lemma'].endswith('pä'):
                wordmap['new_para'] = 'A_KÄYPÄ'
            else:
                fail_guess_because(wordmap, ['A', 10, 'E'],
                                   ['pa', 'pä'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('tä'):
                wordmap['new_para'] = 'A_MÄTÄ'
            else:
                fail_guess_because(wordmap, ['A', 10, 'F'],
                                   ['ta', 'tä'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nka'):
                wordmap['new_para'] = 'A_SANKA'
            elif wordmap['lemma'].endswith('nkä'):
                wordmap['new_para'] = 'A_VÄNKÄ'
            else:
                fail_guess_because(wordmap, ['A', 10, 'G'],
                                   ['nka', 'nkä'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('lta'):
                wordmap['new_para'] = 'A_KULTA'
            else:
                fail_guess_because(wordmap, ['A', 10, 'I'],
                                   ['lta'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntä'):
                wordmap['new_para'] = 'A_LÄNTÄ'
            else:
                fail_guess_because(wordmap, ['A', 10, 'J'],
                                   ['ntä'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rta'):
                wordmap['new_para'] = 'A_TURTA'
            else:
                fail_guess_because(wordmap, ['A', 10, 'K'],
                                   ['rta'])
        else:
            fail_guess_because(wordmap, ['A', 10],
                               [False, 'A', 'B', 'E', 'G', 'I-K'])
    elif tn == 11:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a'):
                wordmap['new_para'] = 'A_HAPERA'
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_para'] = 'A_SÄKKÄRÄ'
            else:
                fail_guess_because(wordmap, ['A', 11, False],
                                   ['a', 'ä'])
        else:
            fail_guess_because(wordmap, ['A', 11],
                               [False])
    elif tn == 12:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a') or wordmap['lemma'].endswith('A'):
                wordmap['new_para'] = 'A_HARMAJA'
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_para'] = 'A_HÖPPÄNÄ'
            else:
                fail_guess_because(wordmap, ['A', 12, False],
                                   ['a', 'ä'])
        else:
            fail_guess_because(wordmap, ['A', 12],
                               [False])
    elif tn == 13:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a'):
                wordmap['new_para'] = 'A_LATUSKA'
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_para'] = 'A_LÄTYSKÄ'
            else:
                fail_guess_because(wordmap, ['A', 13, False],
                                   ['a', 'ä'])
        else:
            fail_guess_because(wordmap, ['A', 13],
                               [False])
    elif tn == 14:
        if wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('kka'):
                wordmap['new_para'] = 'A_HAILAKKA'
            elif wordmap['lemma'].endswith('kkä'):
                wordmap['new_para'] = 'A_RÄVÄKKÄ'
            else:
                fail_guess_because(wordmap, ['A', 14, 'A'],
                                   ['kka', 'kkä'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tta'):
                wordmap['new_para'] = 'A_POHATTA'
            else:
                fail_guess_because(wordmap, ['A', 14, 'C'],
                                   ['tta'])
        else:
            fail_guess_because(wordmap, ['A', 14],
                               ['A', 'C'])
    elif tn == 15:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('oa'):
                wordmap['new_para'] = 'A_AINOA'
            elif wordmap['lemma'].endswith('ea'):
                wordmap['new_para'] = 'A_KORKEA'
            elif wordmap['lemma'].endswith('eä'):
                wordmap['new_para'] = 'A_JÄREÄ'
            else:
                fail_guess_because(wordmap, ['A', 15, False],
                                   ['oa', 'ea', 'eä'])
        else:
            fail_guess_because(wordmap, ['A', 15],
                               [False])
    elif tn == 16:
        if wordmap['kotus_av'] == 'H':
            if wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_AIEMPI'
            elif wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_LÄHEMPI'
            else:
                fail_guess_because(wordmap, ['A', 16, 'H'],
                                   ['back'])
        else:
            fail_guess_because(wordmap, ['A', 16],
                               ['H'])
    elif tn == 17:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aa'):
                wordmap['new_para'] = 'A_VAPAA'
            elif wordmap['lemma'].endswith('ee'):
                wordmap['new_para'] = 'A_OIKEE'
            else:
                fail_guess_because(wordmap, ['A', 17, False],
                                   ['aa', 'ee'])  # , 'oo', 'uu', 'yy', 'ää', 'öö'])
        else:
            fail_guess_because(wordmap, ['A', 17],
                               [False])
    elif tn == 18:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a'):
                wordmap['new_para'] = 'A_PEEAA'
            elif wordmap['lemma'].endswith('u'):
                wordmap['new_para'] = 'A_MUU'
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_para'] = 'A_SYYPÄÄ'
            else:
                fail_guess_because(wordmap, ['A', 18, False],
                                   ['a', 'u', 'ä'])
        else:
            fail_guess_because(wordmap, ['A', 18],
                               [False])
    elif tn == 20:
        fail_guess_because(wordmap, ['A', 20],
                           [False])
    elif tn == 21:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('gay'):
                wordmap['new_para'] = 'A_GAY'
            else:
                fail_guess_because(wordmap, ['A', 21, False],
                                   ['gay', 'é', 'è'], "guessing 21 is not possible")
        else:
            fail_guess_because(wordmap, ['A', 21],
                               [False])
    elif tn in [24, 26]:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_SUURI'
            elif wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_PIENI'
            else:
                fail_guess_because(wordmap, ['A', 23, False],
                                   ['back', 'front'])
        else:
            fail_guess_because(wordmap, ['A', 22],
                               [False])
    elif tn == 27:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('si'):
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'A_UUSI'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'A_TÄYSI'
                else:
                    fail_guess_because(wordmap, ['A', 26, False, 'si'],
                                       ['back', 'front'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('si'):
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'A_UUSI'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'A_TÄYSI'
                else:
                    fail_guess_because(wordmap, ['A', 27, 'F', 'si'],
                                       ['back', 'front'])
        else:
            fail_guess_because(wordmap, ['A', 27],
                               [False])
    elif tn == 32:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_TYVEN'
            else:
                fail_guess_because(wordmap, ['A', 32, False],
                                   ['front'])
    elif wordmap['kotus_tn'] == 33:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('in') and wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_AVOIN'
            else:
                fail_guess_because(wordmap, ['A', 33, 'B'],
                                   ['in', 'back'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('hapan'):
                wordmap['new_para'] = 'A_HAPAN'
            else:
                fail_guess_because(wordmap, ['A', 33, 'B'],
                                   ['hapan'])
        else:
            fail_guess_because(wordmap, ['A', 33], ['B'])
    elif wordmap['kotus_tn'] == 34:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ton'):
                wordmap['new_para'] = 'A_ALASTON'
            else:
                fail_guess_because(wordmap, ['A', 34, False],
                                   ['ton'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('ton'):
                wordmap['new_para'] = 'A_VIATON'
            elif wordmap['lemma'].endswith('tön'):
                wordmap['new_para'] = 'A_KYVYTÖN'
            else:
                fail_guess_because(wordmap, ['A', 34, 'C'],
                                   ['ton', 'tön'])
        else:
            fail_guess_because(wordmap, ['A', 34], [False, 'C'])
    elif wordmap['kotus_tn'] == 35:
        if wordmap['kotus_av'] == 'H':
            if wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_LÄMMIN'
            else:
                fail_guess_because(wordmap, ['A', 35, False],
                                   ['front'])
        else:
            fail_guess_because(wordmap, ['A', 35],
                               ['H'])
    elif wordmap['kotus_tn'] == 36:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_PAHIN'
            elif wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_SISIN'
            else:
                fail_guess_because(wordmap, ['A', 36, 'J'],
                                   ['front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 36],
                               [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 37:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('vasen'):
                wordmap['new_para'] = 'A_VASEN'
            else:
                fail_guess_because(wordmap, ['A', 37, False],
                                   ['vasen'])
        else:
            fail_guess_because(wordmap, ['A', 37],
                               [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 38:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_AAKKOSELLINEN'
            elif wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_KYLMÄJÄRKINEN'
            else:
                fail_guess_because(wordmap, ['A', 38, False],
                                   ['front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 38],
                               [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 39:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_SYMPPIS'
            else:
                fail_guess_because(wordmap, ['A', 38, False],
                                   ['front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 38],
                               [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 40:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('yys'):
                wordmap['new_para'] = 'A_LÄHTEISYYS'
            else:
                fail_guess_because(wordmap, ['A', 40],
                                   ['yys'])
        else:
            fail_guess_because(wordmap, ['A', 40],
                               [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 41:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('paras'):
                wordmap['new_para'] = 'A_PARAS'
            elif wordmap['lemma'].endswith('as'):
                wordmap['new_para'] = 'A_AUTUAS'
            elif wordmap['lemma'].endswith('is') and wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_VALMIS'
            elif wordmap['lemma'].endswith('is') and wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_TIIVIS'
            elif wordmap['lemma'].endswith('äs'):
                wordmap['new_para'] = 'A_TYÖLÄS'
            else:
                fail_guess_because(wordmap, ['A', 41, False],
                                   ['as', 'is', 'äs'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('kas'):
                wordmap['new_para'] = 'A_VOIMAKAS'
            elif wordmap['lemma'].endswith('käs'):
                wordmap['new_para'] = 'A_TYYLIKÄS'
            else:
                fail_guess_because(wordmap, ['A', 41, 'A'],
                                   ['kas', 'käs'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('pas'):
                wordmap['new_para'] = 'A_REIPAS'
            else:
                fail_guess_because(wordmap, ['A', 41, 'B'],
                                   ['pas', 'päs'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tas'):
                wordmap['new_para'] = 'A_RIETAS'
            elif wordmap['lemma'].endswith('tis') and wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_RAITIS'
            else:
                fail_guess_because(wordmap, ['A', 41, 'C'],
                                   ['tas', 'tis', 'tus', 'täs', 'front'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('das'):
                wordmap['new_para'] = 'A_HIDAS'
            else:
                fail_guess_because(wordmap, ['A', 41, 'F'],
                                   ['das'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('ras'):
                wordmap['new_para'] = 'A_HARRAS'
            else:
                fail_guess_because(wordmap, ['A', 41, 'K'],
                                   ['rras'])
        else:
            fail_guess_because(wordmap, ['A', 41],
                               [False, 'A B C F K'])
    elif wordmap['kotus_tn'] == 43:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ut'):
                wordmap['new_para'] = 'A_OHUT'
            elif wordmap['lemma'].endswith('yt'):
                wordmap['new_para'] = 'A_EHYT'
            else:
                fail_guess_because(wordmap, ['A', 43, False],
                                   ['ut', 'yt'])
        else:
            fail_guess_because(wordmap, ['A', 43],
                               [False])
    elif wordmap['kotus_tn'] == 44:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ut'):
                wordmap['new_para'] = 'A_AINUT'
            else:
                fail_guess_because(wordmap, ['A', 44, False],
                                   ['ut'])
        else:
            fail_guess_because(wordmap, ['A', 44],
                               [False])
    elif wordmap['kotus_tn'] == 47:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ut'):
                wordmap['new_para'] = 'A_KULUNUT'
            elif wordmap['lemma'].endswith('yt'):
                wordmap['new_para'] = 'A_ÄLLISTYNYT'
            else:
                fail_guess_because(wordmap, ['A', 47, False],
                                   ['yt'])
        else:
            fail_guess_because(wordmap, ['A', 47],
                               [False], "cannot gradate")
    elif tn == 48:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_AHNE'
            elif wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_TERVE'
            else:
                fail_guess_because(wordmap, ['A', 48, False],
                                   ['front', 'back'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('de') and wordmap['harmony'] == 'back':
                wordmap['new_para'] = 'A_KADE'
            else:
                fail_guess_because(wordmap, ['A', 48, 'F'],
                                   ['de', 'front', 'back'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('lle') and wordmap['harmony'] == 'front':
                wordmap['new_para'] = 'A_HELLE'
            else:
                fail_guess_because(wordmap, ['A', 48, 'I'],
                                   ['lle', 'front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 48],
                               [False, 'F', 'I'])
    elif tn == 99:
        fail_guess_because(wordmap, ['A', 99], [99],
                           "Illegal class for A, 99 can only apply to P")
        wordmap['new_para'] = '#'
    elif tn == 1010:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('pitkä'):
                wordmap['new_para'] = 'A_PITKÄ'
            else:
                fail_guess_because(wordmap, ['A', 10, 'D', 'PITKÄ'],
                                   ['pitkä'], 'must be pitkä')
        else:
            fail_guess_because(wordmap, ['A', 10],
                               ['D'])
    else:
        fail_guess_because(wordmap, ['A'],
                           ['1-49', '99', '1010'])
    return wordmap


def guess_new_verb(wordmap):
    tn = int(wordmap['kotus_tn'])
    if tn == 52:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('oa'):
                wordmap['new_para'] = 'V_PUNOA'
            elif wordmap['lemma'].endswith('ua'):
                wordmap['new_para'] = 'V_KAUNISTUA'
            elif wordmap['lemma'].endswith('yä'):
                wordmap['new_para'] = 'V_ÄLLISTYÄ'
            elif wordmap['lemma'].endswith('öä'):
                wordmap['new_para'] = 'V_SÄILÖÄ'
            else:
                fail_guess_because(wordmap, ['V', 52, False],
                                   ['oa', 'ua', 'yä', 'öä'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('koa'):
                wordmap['new_para'] = 'V_HAUKKOA'
            elif wordmap['lemma'].endswith('kua'):
                wordmap['new_para'] = 'V_NUOKKUA'
            elif wordmap['lemma'].endswith('kyä'):
                wordmap['new_para'] = 'V_KÄRKKYÄ'
            else:
                fail_guess_because(wordmap, ['V', 52, 'A'],
                                   ['ko', 'ku', 'ky'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppoa'):
                wordmap['new_para'] = 'V_HARPPOA'
            elif wordmap['lemma'].endswith('ppua'):
                wordmap['new_para'] = 'V_LOPPUA'
            elif wordmap['lemma'].endswith('ppyä'):
                wordmap['new_para'] = 'V_LEPPYÄ'
            else:
                fail_guess_because(wordmap, ['V', 52, 'B'],
                                   ['ppo', 'ppu', 'ppy'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('ttoa'):
                wordmap['new_para'] = 'V_VIITTOA'
            elif wordmap['lemma'].endswith('ttua'):
                wordmap['new_para'] = 'V_HERMOTTUA'
            elif wordmap['lemma'].endswith('ttyä'):
                wordmap['new_para'] = 'V_KIVETTYÄ'
            else:
                fail_guess_because(wordmap, ['V', 52, 'C'],
                                   ['tto', 'ttu', 'tty'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('koa'):
                wordmap['new_para'] = 'V_TAKOA'
            elif wordmap['lemma'].endswith('ukua'):
                wordmap['new_para'] = 'V_MAUKUA'
            elif wordmap['lemma'].endswith('kua'):
                wordmap['new_para'] = 'V_NUOKKUA'
            elif wordmap['lemma'].endswith('kyä'):
                wordmap['new_para'] = 'V_MÄIKYÄ'
            else:
                fail_guess_because(wordmap, ['V', 52, 'D'],
                                   ['ko'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('poa'):
                wordmap['new_para'] = 'V_SILPOA'
            elif wordmap['lemma'].endswith('pua'):
                wordmap['new_para'] = 'V_HIIPUA'
            elif wordmap['lemma'].endswith('pyä'):
                wordmap['new_para'] = 'V_SYÖPYÄ'
            else:
                fail_guess_because(wordmap, ['V', 52, 'E'],
                                   ['poa', 'pua', 'pyä'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('toa'):
                wordmap['new_para'] = 'V_KIETOA'
            elif wordmap['lemma'].endswith('tua'):
                wordmap['new_para'] = 'V_ROHTUA'
            elif wordmap['lemma'].endswith('tyä'):
                wordmap['new_para'] = 'V_SILIYTYÄ'
            else:
                fail_guess_because(wordmap, ['V', 52, 'F'],
                                   ['toa', 'tua', 'tyä'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nkua'):
                wordmap['new_para'] = 'V_VINKUA'
            elif wordmap['lemma'].endswith('nkoa'):
                wordmap['new_para'] = 'V_PENKOA'
            else:
                fail_guess_because(wordmap, ['V', 52, 'G'],
                                   ['nko'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mpoa'):
                wordmap['new_para'] = 'V_TEMPOA'
            elif wordmap['lemma'].endswith('mpua'):
                wordmap['new_para'] = 'V_AMPUA'
            else:
                fail_guess_because(wordmap, ['V', 52, 'G'],
                                   ['nko'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('ltua'):
                wordmap['new_para'] = 'V_HUMALTUA'
            elif wordmap['lemma'].endswith('ltyä'):
                wordmap['new_para'] = 'V_MIELTYÄ'
            else:
                fail_guess_because(wordmap, ['V', 52, 'I'],
                                   ['lto', 'ltu', 'lty'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntua'):
                wordmap['new_para'] = 'V_VAKAANTUA'
            elif wordmap['lemma'].endswith('ntyä'):
                wordmap['new_para'] = 'V_TYHJENTYÄ'
            else:
                fail_guess_because(wordmap, ['V', 52, 'J'],
                                   ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rtoa'):
                wordmap['new_para'] = 'V_VARTOA'
            elif wordmap['lemma'].endswith('rtua'):
                wordmap['new_para'] = 'V_PUSERTUA'
            elif wordmap['lemma'].endswith('rtyä'):
                wordmap['new_para'] = 'V_KIERTYÄ'
            else:
                fail_guess_because(wordmap, ['V', 52, 'K'],
                                   ['rtoa', 'rtua', 'rtyä'])
        else:
            fail_guess_because(wordmap, ['V', 52],
                               [False, 'A-K'])
    elif tn == 53:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aa'):
                wordmap['new_para'] = 'V_MUTRISTAA'
            elif wordmap['lemma'].endswith('ää'):
                wordmap['new_para'] = 'V_KIVISTÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 53, False],
                                   ['aa', 'ää'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('ttaa'):
                wordmap['new_para'] = 'V_VIEROITTAA'
            elif wordmap['lemma'].endswith('ttää'):
                wordmap['new_para'] = 'V_RÄPSYTTÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 53, 'C'],
                                   ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('kaa'):
                wordmap['new_para'] = 'V_PURKAA'
            else:
                fail_guess_because(wordmap, ['V', 53, 'D'],
                                   ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_para'] = 'V_MOJAHTAA'
            elif wordmap['lemma'].endswith('tää'):
                wordmap['new_para'] = 'V_YSKÄHTÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 53, 'F'],
                                   ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntää'):
                wordmap['new_para'] = 'V_KYNTÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 53, 'J'],
                                   ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rtaa'):
                wordmap['new_para'] = 'V_SORTAA'
            else:
                fail_guess_because(wordmap, ['V', 53, 'K'],
                                   ['nto', 'ntu', 'nty'])
        else:
            fail_guess_because(wordmap, ['V', 53], [False])
    elif tn == 54:
        if wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_para'] = 'V_HUUTAA'
            elif wordmap['lemma'].endswith('tää'):
                wordmap['new_para'] = 'V_PYYTÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 54, False],
                                   ['tää', 'taa'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('ltaa'):
                wordmap['new_para'] = 'V_SIVALTAA'
            elif wordmap['lemma'].endswith('ltää'):
                wordmap['new_para'] = 'V_VIHELTÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 54, 'I'],
                                   ['tää', 'taa'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntaa'):
                wordmap['new_para'] = 'V_HUONONTAA'
            elif wordmap['lemma'].endswith('ntää'):
                wordmap['new_para'] = 'V_HIVENTÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 54, 'J'],
                                   ['tää', 'taa'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rtaa'):
                wordmap['new_para'] = 'V_KUHERTAA'
            elif wordmap['lemma'].endswith('rtää'):
                wordmap['new_para'] = 'V_NÄPERTÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 54, 'K'],
                                   ['tää', 'taa'])
        else:
            fail_guess_because(wordmap, ['V', 54], ['F', 'I-K'])
    elif tn == 55:
        if wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_para'] = 'V_JOUTAA'
            elif wordmap['lemma'].endswith('tää'):
                wordmap['new_para'] = 'V_KIITÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 55, 'F'],
                                   ['kko'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('ltää'):
                wordmap['new_para'] = 'V_YLTÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 55, 'I'],
                                   ['ltää'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntää'):
                wordmap['new_para'] = 'V_ENTÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 55, 'J'],
                                   ['tää', 'taa'])
        else:
            fail_guess_because(wordmap, ['V', 55], ['F', 'I', 'J'])
    elif tn == 56:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aa'):
                wordmap['new_para'] = 'V_KASVAA'
            else:
                fail_guess_because(wordmap, ['V', 56, False],
                                   ['front', 'back'])
        elif wordmap['kotus_av'] in ['A', 'D']:
            if wordmap['lemma'].endswith('kaa'):
                wordmap['new_para'] = 'V_VIRKKAA'
            else:
                fail_guess_because(wordmap, ['V', 56, 'A'],
                                   ['kaa'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppaa'):
                wordmap['new_para'] = 'V_TAPPAA'
            else:
                fail_guess_because(wordmap, ['V', 56, 'B'],
                                   ['kkaa'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('ttaa'):
                wordmap['new_para'] = 'V_AUTTAA'
            else:
                fail_guess_because(wordmap, ['V', 56, 'C'],
                                   ['kkaa'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_para'] = 'V_SATAA'
            else:
                fail_guess_because(wordmap, ['V', 56, 'F'],
                                   ['kkaa'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntaa'):
                wordmap['new_para'] = 'V_KANTAA'
            else:
                fail_guess_because(wordmap, ['V', 56, 'J'],
                                   ['kkaa'])
        else:
            fail_guess_because(wordmap, ['V', 56],
                               [False])
    elif tn == 57:
        if wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_para'] = 'V_KAATAA'
            else:
                fail_guess_because(wordmap, ['V', 57, 'F'],
                                   ['e', 'front', 'back'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rtaa'):
                wordmap['new_para'] = 'V_SAARTAA'
            else:
                fail_guess_because(wordmap, ['V', 57, 'K'],
                                   ['e', 'front', 'back'])
        else:
            fail_guess_because(wordmap, ['V', 57],
                               [False])
    elif tn == 58:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ea'):
                wordmap['new_para'] = 'V_SOTKEA'
            elif wordmap['lemma'].endswith('eä'):
                wordmap['new_para'] = 'V_KYTKEÄ'
            else:
                fail_guess_because(wordmap, ['V', 58, False],
                                   ['ea', 'eä'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('kea'):
                wordmap['new_para'] = 'V_PUKEA'
            else:
                fail_guess_because(wordmap, ['V', 58, 'D'],
                                   ['kka'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('peä'):
                wordmap['new_para'] = 'V_RYPEÄ'
            else:
                fail_guess_because(wordmap, ['V', 58, 'E'],
                                   ['tta'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('tea'):
                wordmap['new_para'] = 'V_KUTEA'
            elif wordmap['lemma'].endswith('teä'):
                wordmap['new_para'] = 'V_PÄTEÄ'
            else:
                fail_guess_because(wordmap, ['V', 58, 'F'],
                                   ['ka'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nkea'):
                wordmap['new_para'] = 'V_TUNKEA'
            else:
                fail_guess_because(wordmap, ['V', 58, 'G'],
                                   ['pa'])
        elif wordmap['kotus_av'] == 'L':
            if wordmap['lemma'].endswith('kea'):
                wordmap['new_para'] = 'V_POLKEA'
            elif wordmap['lemma'].endswith('keä'):
                wordmap['new_para'] = 'V_SÄRKEÄ'
            else:
                fail_guess_because(wordmap, ['V', 58, 'L'],
                                   ['ta'])
        else:
            fail_guess_because(wordmap, ['V', 58],
                               [False, 'V-K'])
    elif tn == 59:
        if wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntea'):
                wordmap['new_para'] = 'V_TUNTEA'
            else:
                fail_guess_because(wordmap, ['V', 59, False],
                                   ['a', 'ä'])
        else:
            fail_guess_because(wordmap, ['V', 59, 'K'],
                               ['rta'])
    elif tn == 60:
        if wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('hteä'):
                wordmap['new_para'] = 'V_LÄHTEÄ'
            else:
                fail_guess_because(wordmap, ['V', 60, False],
                                   ['a', 'ä'])
        else:
            fail_guess_because(wordmap, ['V', 60],
                               [False])
    elif tn == 61:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ia'):
                wordmap['new_para'] = 'V_KOSIA'
            elif wordmap['lemma'].endswith('iä'):
                wordmap['new_para'] = 'V_RYSKIÄ'
            else:
                fail_guess_because(wordmap, ['V', 61, False],
                                   ['ia', 'iä'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('kia'):
                wordmap['new_para'] = 'V_KUKKIA'
            elif wordmap['lemma'].endswith('kiä'):
                wordmap['new_para'] = 'V_SÖRKKIÄ'
            else:
                fail_guess_because(wordmap, ['V', 61, 'A'],
                                   ['kia', 'kiä'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppia'):
                wordmap['new_para'] = 'V_KALPPIA'
            elif wordmap['lemma'].endswith('ppiä'):
                wordmap['new_para'] = 'V_HYPPIÄ'
            else:
                fail_guess_because(wordmap, ['V', 61, 'B'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('ttia'):
                wordmap['new_para'] = 'V_MOITTIA'
            elif wordmap['lemma'].endswith('ttiä'):
                wordmap['new_para'] = 'V_MIETTIÄ'
            else:
                fail_guess_because(wordmap, ['V', 61, 'C'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('kia'):
                wordmap['new_para'] = 'V_KUKKIA'
            elif wordmap['lemma'].endswith('kiä'):
                wordmap['new_para'] = 'V_SÖRKKIÄ'
            else:
                fail_guess_because(wordmap, ['V', 61, 'D'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('pia'):
                wordmap['new_para'] = 'V_RAAPIA'
            elif wordmap['lemma'].endswith('piä'):
                wordmap['new_para'] = 'V_RIIPIÄ'
            else:
                fail_guess_because(wordmap, ['V', 61, 'E'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('tia'):
                wordmap['new_para'] = 'V_AHNEHTIA'
            elif wordmap['lemma'].endswith('tiä'):
                wordmap['new_para'] = 'V_EHTIÄ'
            else:
                fail_guess_because(wordmap, ['V', 61, 'F'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nkia'):
                wordmap['new_para'] = 'V_ONKIA'
            elif wordmap['lemma'].endswith('nkiä'):
                wordmap['new_para'] = 'V_MÖNKIÄ'
            else:
                fail_guess_because(wordmap, ['V', 61, 'G'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mpiä'):
                wordmap['new_para'] = 'V_TYMPIÄ'
            else:
                fail_guess_because(wordmap, ['V', 61, 'H'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntia'):
                wordmap['new_para'] = 'V_KONTIA'
            else:
                fail_guess_because(wordmap, ['V', 61, 'J'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'L':
            if wordmap['lemma'].endswith('kiä'):
                wordmap['new_para'] = 'V_HYLKIÄ'
            else:
                fail_guess_because(wordmap, ['V', 61, 'L'],
                                   ['a'])
        else:
            fail_guess_because(wordmap, ['V', 61],
                               [False])
    elif tn == 62:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ida'):
                wordmap['new_para'] = 'V_KOPIOIDA'
            elif wordmap['lemma'].endswith('idä'):
                wordmap['new_para'] = 'V_ÖYKKÄRÖIDÄ'
            else:
                fail_guess_because(wordmap, ['V', 62, False],
                                   ['ida', 'idä'])
        else:
            fail_guess_because(wordmap, ['V', 62],
                               [False])
    elif tn == 63:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aada'):
                wordmap['new_para'] = 'V_SAADA'
            elif wordmap['lemma'].endswith('yydä'):
                wordmap['new_para'] = 'V_MYYDÄ'
            elif wordmap['lemma'].endswith('äädä'):
                wordmap['new_para'] = 'V_JÄÄDÄ'
            else:
                fail_guess_because(wordmap, ['V', 63, False],
                                   ['kka', 'kkä'])
        else:
            fail_guess_because(wordmap, ['V', 63],
                               [False])
    elif tn == 64:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('iedä'):
                wordmap['new_para'] = 'V_VIEDÄ'
            elif wordmap['lemma'].endswith('uoda'):
                wordmap['new_para'] = 'V_TUODA'
            elif wordmap['lemma'].endswith('yödä'):
                wordmap['new_para'] = 'V_SYÖDÄ'
            else:
                fail_guess_because(wordmap, ['V', 64, False],
                                   ['oa', 'ea', 'eä'])
        else:
            fail_guess_because(wordmap, ['V', 64],
                               [False])
    elif tn == 65:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('käydä'):
                wordmap['new_para'] = 'V_KÄYDÄ'
            else:
                fail_guess_because(wordmap, ['V', 65, False],
                                   ['back'])
        else:
            fail_guess_because(wordmap, ['V', 65],
                               ['H'])
    elif tn == 66:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ta'):
                wordmap['new_para'] = 'V_MARISTA'
            elif wordmap['lemma'].endswith('tä'):
                wordmap['new_para'] = 'V_ÄRISTÄ'
            else:
                fail_guess_because(wordmap, ['V', 66, False],
                                   ['ta', 'tä'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('vista'):
                wordmap['new_para'] = 'V_VAVISTA'
            elif wordmap['lemma'].endswith('väistä'):
                wordmap['new_para'] = 'V_HÄVÄISTÄ'
            else:
                fail_guess_because(wordmap, ['V', 66, False],
                                   ['vista', 'väistä'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('ngaista'):
                wordmap['new_para'] = 'V_RANGAISTA'
            else:
                fail_guess_because(wordmap, ['V', 66, False],
                                   ['gaista'])
        else:
            fail_guess_because(wordmap, ['V', 66],
                               [False])
    elif tn == 67:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('tulla'):
                wordmap['new_para'] = 'V_TULLA'
            elif wordmap['lemma'].endswith('ailla') or \
                    wordmap['lemma'].endswith('oilla'):
                wordmap['new_para'] = 'V_ARVAILLA'
            elif wordmap['lemma'].endswith('äillä') or \
                    wordmap['lemma'].endswith('öilla'):
                wordmap['new_para'] = 'V_LEPÄILLÄ'
            elif wordmap['lemma'].endswith('lla'):
                wordmap['new_para'] = 'V_ETUILLA'
            elif wordmap['lemma'].endswith('llä'):
                wordmap['new_para'] = 'V_ÄKSYILLÄ'
            elif wordmap['lemma'].endswith('nna'):
                wordmap['new_para'] = 'V_PANNA'
            elif wordmap['lemma'].endswith('nnä'):
                wordmap['new_para'] = 'V_MENNÄ'
            elif wordmap['lemma'].endswith('rra'):
                wordmap['new_para'] = 'V_SURRA'
            elif wordmap['lemma'].endswith('rrä'):
                wordmap['new_para'] = 'V_PIERRÄ'
            else:
                fail_guess_because(wordmap, ['V', 67, False],
                                   ['rra', 'rrä'])
        elif wordmap['kotus_av'] in ['A', 'D']:
            if wordmap['lemma'].endswith('ella'):
                wordmap['new_para'] = 'V_NAKELLA'
            elif wordmap['lemma'].endswith('ellä'):
                wordmap['new_para'] = 'V_LEIKELLÄ'
            else:
                fail_guess_because(wordmap, ['V', 67, 'A'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('pella'):
                wordmap['new_para'] = 'V_TAPELLA'
            elif wordmap['lemma'].endswith('pellä'):
                wordmap['new_para'] = 'V_HYPELLÄ'
            else:
                fail_guess_because(wordmap, ['V', 67, 'B'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tella'):
                wordmap['new_para'] = 'V_SULATELLA'
            elif wordmap['lemma'].endswith('tellä'):
                wordmap['new_para'] = 'V_HERÄTELLÄ'
            else:
                fail_guess_because(wordmap, ['V', 67, 'C'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('della'):
                wordmap['new_para'] = 'V_TIPAHDELLA'
            elif wordmap['lemma'].endswith('dellä'):
                wordmap['new_para'] = 'V_SÄPSÄHDELLÄ'
            else:
                fail_guess_because(wordmap, ['V', 67, 'F'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mmella'):
                wordmap['new_para'] = 'V_OMMELLA'
            else:
                fail_guess_because(wordmap, ['V', 67, 'H'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('llella'):
                wordmap['new_para'] = 'V_VAELLELLA'
            elif wordmap['lemma'].endswith('llellä'):
                wordmap['new_para'] = 'V_KIILLELLÄ'
            else:
                fail_guess_because(wordmap, ['V', 67, 'I'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nnella'):
                wordmap['new_para'] = 'V_KOMENNELLA'
            elif wordmap['lemma'].endswith('nnellä'):
                wordmap['new_para'] = 'V_KÄÄNNELLÄ'
            else:
                fail_guess_because(wordmap, ['V', 67, 'J'],
                                   ['a'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rrella'):
                wordmap['new_para'] = 'V_NAKERRELLA'
            elif wordmap['lemma'].endswith('rrellä'):
                wordmap['new_para'] = 'V_KIHERRELLÄ'
            else:
                fail_guess_because(wordmap, ['V', 67, 'K'],
                                   ['a'])
        else:
            fail_guess_because(wordmap, ['V', 18],
                               [False])
    elif tn == 68:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('oida'):
                wordmap['new_para'] = 'V_MELLAKOIDA'
            elif wordmap['lemma'].endswith('öidä'):
                wordmap['new_para'] = 'V_ISÄNNÖIDÄ'
            else:
                fail_guess_because(wordmap, ['V', 68, False],
                                   ['a'])
        else:
            fail_guess_because(wordmap, ['V', 68],
                               [False])
    elif tn == 69:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ita'):
                wordmap['new_para'] = 'V_PALKITA'
            elif wordmap['lemma'].endswith('itä'):
                wordmap['new_para'] = 'V_MERKITÄ'
            else:
                fail_guess_because(wordmap, ['V', 69, False],
                                   ['a'])
        else:
            fail_guess_because(wordmap, ['V', 69],
                               [False])
    elif tn == 70:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('sta'):
                wordmap['new_para'] = 'V_JUOSTA'
            elif wordmap['lemma'].endswith('stä'):
                wordmap['new_para'] = 'V_PIESTÄ'
            else:
                fail_guess_because(wordmap, ['V', 70, False],
                                   ['back', 'front'])
        else:
            fail_guess_because(wordmap, ['V', 70],
                               [False])
    elif tn == 71:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('hdä'):
                wordmap['new_para'] = 'V_NÄHDÄ'
            else:
                fail_guess_because(wordmap, ['V', 71, False],
                                   ['back', 'front'])
        else:
            fail_guess_because(wordmap, ['V', 71],
                               [False])
    elif tn == 72:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ta'):
                wordmap['new_para'] = 'V_KARHETA'
            elif wordmap['lemma'].endswith('tä'):
                wordmap['new_para'] = 'V_VÄHETÄ'
            else:
                fail_guess_because(wordmap, ['V', 72, False],
                                   ['back', 'front'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('keta'):
                wordmap['new_para'] = 'V_NIUKETA'
            elif wordmap['lemma'].endswith('kota'):
                wordmap['new_para'] = 'V_ULOTA'
            elif wordmap['lemma'].endswith('ketä'):
                wordmap['new_para'] = 'V_JYRKETÄ'
            else:
                fail_guess_because(wordmap, ['V', 72, 'A'],
                                   ['back', 'front'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('peta'):
                wordmap['new_para'] = 'V_SUPETA'
            elif wordmap['lemma'].endswith('petä'):
                wordmap['new_para'] = 'V_TYLPETÄ'
            elif wordmap['lemma'].endswith('pota'):
                wordmap['new_para'] = 'V_HELPOTA'
            elif wordmap['lemma'].endswith('pata'):
                wordmap['new_para'] = 'V_HAPATA'
            else:
                fail_guess_because(wordmap, ['V', 72, 'B'],
                                   ['peta', 'petä', 'pata', 'pota'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tota'):
                wordmap['new_para'] = 'V_LOITOTA'
            else:
                fail_guess_because(wordmap, ['V', 72, 'C'],
                                   ['back', 'front'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('ota'):
                wordmap['new_para'] = 'V_ULOTA'
            elif wordmap['lemma'].endswith('ata'):
                wordmap['new_para'] = 'V_ERATA'
            elif wordmap['lemma'].endswith('eta'):
                wordmap['new_para'] = 'V_NIUKETA'
            elif wordmap['lemma'].endswith('etä'):
                wordmap['new_para'] = 'V_JYRKETÄ'
            else:
                fail_guess_because(wordmap, ['V', 72, 'D'],
                                   ['back', 'front'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('veta'):
                wordmap['new_para'] = 'V_KAVETA'
            elif wordmap['lemma'].endswith('vetä'):
                wordmap['new_para'] = 'V_KIVETÄ'
            else:
                fail_guess_because(wordmap, ['V', 72, 'E'],
                                   ['back', 'front'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('dota'):
                wordmap['new_para'] = 'V_LEUDOTA'
            elif wordmap['lemma'].endswith('detä'):
                wordmap['new_para'] = 'V_PIDETÄ'
            elif wordmap['lemma'].endswith('dätä'):
                wordmap['new_para'] = 'V_MÄDÄTÄ'
            else:
                fail_guess_because(wordmap, ['V', 72, 'F'],
                                   ['back', 'front'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mmetä'):
                wordmap['new_para'] = 'V_LÄMMETÄ'
            else:
                fail_guess_because(wordmap, ['V', 72, 'H'],
                                   ['back', 'front'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nnetä'):
                wordmap['new_para'] = 'V_KIINNETÄ'
            elif wordmap['lemma'].endswith('nnota'):
                wordmap['new_para'] = 'V_RENNOTA'
            else:
                fail_guess_because(wordmap, ['V', 72, 'J'],
                                   ['nnetä', 'nnota'])
        elif wordmap['kotus_av'] == 'L':
            if wordmap['lemma'].endswith('jeta'):
                wordmap['new_para'] = 'V_ROHJETA'
            elif wordmap['lemma'].endswith('jetä'):
                wordmap['new_para'] = 'V_ILJETÄ'
            else:
                fail_guess_because(wordmap, ['V', 72, 'L'],
                                   ['back', 'front'])
        else:
            fail_guess_because(wordmap, ['V', 72],
                               [False, 'A-L'])
    elif wordmap['kotus_tn'] == 73:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ata'):
                wordmap['new_para'] = 'V_ARVATA'
            elif wordmap['lemma'].endswith('ätä'):
                wordmap['new_para'] = 'V_YNNÄTÄ'
            else:
                fail_guess_because(wordmap, ['V', 73, False],
                                   ['ata', 'ätä'])
        elif wordmap['kotus_av'] in ['A', 'D']:
            if wordmap['lemma'].endswith('ata'):
                wordmap['new_para'] = 'V_MORKATA'
            elif wordmap['lemma'].endswith('ätä'):
                wordmap['new_para'] = 'V_YÖKÄTÄ'
            else:
                fail_guess_because(wordmap, ['V', 73, 'A'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('pata'):
                wordmap['new_para'] = 'V_SIEPATA'
            elif wordmap['lemma'].endswith('pätä'):
                wordmap['new_para'] = 'V_VÄLPÄTÄ'
            else:
                fail_guess_because(wordmap, ['V', 73, 'B'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tata'):
                wordmap['new_para'] = 'V_LUNTATA'
            elif wordmap['lemma'].endswith('tätä'):
                wordmap['new_para'] = 'V_LÄNTÄTÄ'
            else:
                fail_guess_because(wordmap, ['V', 73, 'C'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('vata'):
                wordmap['new_para'] = 'V_KAIVATA'
            elif wordmap['lemma'].endswith('vätä'):
                wordmap['new_para'] = 'V_LEVÄTÄ'
            else:
                fail_guess_because(wordmap, ['V', 73, 'E'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('data'):
                wordmap['new_para'] = 'V_JAHDATA'
            elif wordmap['lemma'].endswith('dätä'):
                wordmap['new_para'] = 'V_TÄHDÄTÄ'
            else:
                fail_guess_because(wordmap, ['V', 73, 'F'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('gata'):
                wordmap['new_para'] = 'V_VONGATA'
            elif wordmap['lemma'].endswith('gätä'):
                wordmap['new_para'] = 'V_VÄNGÄTÄ'
            else:
                fail_guess_because(wordmap, ['V', 73, 'G'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mmata'):
                wordmap['new_para'] = 'V_TEMMATA'
            else:
                fail_guess_because(wordmap, ['V', 73, 'H'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('llata'):
                wordmap['new_para'] = 'V_MULLATA'
            else:
                fail_guess_because(wordmap, ['V', 73, 'I'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nnata'):
                wordmap['new_para'] = 'V_SUUNNATA'
            elif wordmap['lemma'].endswith('nnätä'):
                wordmap['new_para'] = 'V_RYNNÄTÄ'
            else:
                fail_guess_because(wordmap, ['V', 73, 'J'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rata'):
                wordmap['new_para'] = 'V_VERRATA'
            else:
                fail_guess_because(wordmap, ['V', 73, 'K'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'L':
            if wordmap['lemma'].endswith('jätä'):
                wordmap['new_para'] = 'V_HYLJÄTÄ'
            else:
                fail_guess_because(wordmap, ['V', 73, 'K'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'O':
            if wordmap['lemma'].endswith('gata'):
                wordmap['new_para'] = 'V_DIGATA'
            else:
                fail_guess_because(wordmap, ['V', 73, 'N'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'P':
            if wordmap['lemma'].endswith('bata'):
                wordmap['new_para'] = 'V_LOBATA'
            else:
                fail_guess_because(wordmap, ['V', 73, 'P'],
                                   ['hapan'])
        else:
            fail_guess_because(wordmap, ['V', 73], [False, 'A-P'])
    elif wordmap['kotus_tn'] == 74:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ta'):
                wordmap['new_para'] = 'V_KARHUTA'
            elif wordmap['lemma'].endswith('tä'):
                wordmap['new_para'] = 'V_TÄHYTÄ'
            else:
                fail_guess_because(wordmap, ['V', 74, False],
                                   ['ton'])
        elif wordmap['kotus_av'] in ['A', 'D']:
            if wordmap['lemma'].endswith('ota'):
                wordmap['new_para'] = 'V_KAIKOTA'
            elif wordmap['lemma'].endswith('eta'):
                wordmap['new_para'] = 'V_POIKETA'
            elif wordmap['lemma'].endswith('etä'):
                wordmap['new_para'] = 'V_KERETÄ'
            elif wordmap['lemma'].endswith('uta'):
                wordmap['new_para'] = 'V_KOUKUTA'
            else:
                fail_guess_because(wordmap, ['V', 74, 'A'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('puta'):
                wordmap['new_para'] = 'V_PULPUTA'
            elif wordmap['lemma'].endswith('pota'):
                wordmap['new_para'] = 'V_UPOTA'
            else:
                fail_guess_because(wordmap, ['V', 74, 'B'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tota'):
                wordmap['new_para'] = 'V_LOTOTA'
            elif wordmap['lemma'].endswith('tuta'):
                wordmap['new_para'] = 'V_LUUTUTA'
            else:
                fail_guess_because(wordmap, ['V', 74, 'C'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('vuta'):
                wordmap['new_para'] = 'V_KIVUTA'
            elif wordmap['lemma'].endswith('veta'):
                wordmap['new_para'] = 'V_KORVETA'
            elif wordmap['lemma'].endswith('vetä'):
                wordmap['new_para'] = 'V_REVETÄ'
            elif wordmap['lemma'].endswith('vota'):
                wordmap['new_para'] = 'V_KIRVOTA'
            else:
                fail_guess_because(wordmap, ['V', 74, 'E'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('duta'):
                wordmap['new_para'] = 'V_LIIDUTA'
            elif wordmap['lemma'].endswith('deta'):
                wordmap['new_para'] = 'V_TODETA'
            elif wordmap['lemma'].endswith('dota'):
                wordmap['new_para'] = 'V_VAAHDOTA'
            elif wordmap['lemma'].endswith('detä'):
                wordmap['new_para'] = 'V_VYYHDETÄ'
            else:
                fail_guess_because(wordmap, ['V', 74, 'F'],
                                   ['deta', 'detä', 'dota', 'duta'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('geta'):
                wordmap['new_para'] = 'V_TUNGETA'
            elif wordmap['lemma'].endswith('gota'):
                wordmap['new_para'] = 'V_PINGOTA'
            elif wordmap['lemma'].endswith('getä'):
                wordmap['new_para'] = 'V_ÄNGETÄ'
            else:
                fail_guess_because(wordmap, ['V', 74, 'G'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mmuta'):
                wordmap['new_para'] = 'V_KUMMUTA'
            elif wordmap['lemma'].endswith('mmeta'):
                wordmap['new_para'] = 'V_KAMMETA'
            elif wordmap['lemma'].endswith('mmota'):
                wordmap['new_para'] = 'V_SAMMOTA'
            else:
                fail_guess_because(wordmap, ['V', 74, 'H'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nnota'):
                wordmap['new_para'] = 'V_INNOTA'
            else:
                fail_guess_because(wordmap, ['V', 74, 'J'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rrota'):
                wordmap['new_para'] = 'V_IRROTA'
            else:
                fail_guess_because(wordmap, ['V', 74, 'K'],
                                   ['hapan'])
        elif wordmap['kotus_av'] == 'L':
            if wordmap['lemma'].endswith('jeta'):
                wordmap['new_para'] = 'V_HALJETA'
            elif wordmap['lemma'].endswith('jetä'):
                wordmap['new_para'] = 'V_ILJETÄ'
            else:
                fail_guess_because(wordmap, ['V', 74, 'K'],
                                   ['hapan'])
        else:
            fail_guess_because(wordmap, ['V', 74], [False, 'A-K'])
    elif wordmap['kotus_tn'] == 75:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ta'):
                wordmap['new_para'] = 'V_LASSOTA'
            elif wordmap['lemma'].endswith('tä'):
                wordmap['new_para'] = 'V_SELVITÄ'
            else:
                fail_guess_because(wordmap, ['V', 75, False],
                                   ['ta', 'tä'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('pytä'):
                wordmap['new_para'] = 'V_RYÖPYTÄ'
            else:
                fail_guess_because(wordmap, ['V', 75, 'B'],
                                   ['ton'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tota'):
                wordmap['new_para'] = 'V_PEITOTA'
            else:
                fail_guess_because(wordmap, ['V', 75, 'C'],
                                   ['ton'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('itä'):
                wordmap['new_para'] = 'V_KERITÄ'
            else:
                fail_guess_because(wordmap, ['V', 75, 'D'],
                                   ['ton'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('dota'):
                wordmap['new_para'] = 'V_MUODOTA'
            else:
                fail_guess_because(wordmap, ['V', 75, 'E'],
                                   ['ton'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mmitä'):
                wordmap['new_para'] = 'V_LÄMMITÄ'
            else:
                fail_guess_because(wordmap, ['V', 75, 'H'],
                                   ['ton'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('llitä'):
                wordmap['new_para'] = 'V_HELLITÄ'
            elif wordmap['lemma'].endswith('llota'):
                wordmap['new_para'] = 'V_AALLOTA'
            else:
                fail_guess_because(wordmap, ['V', 75, 'I'],
                                   ['ton'])
        else:
            fail_guess_because(wordmap, ['V', 75],
                               [False, 'B', 'D', 'F', 'H', 'I'])
    elif wordmap['kotus_tn'] == 76:
        if wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_para'] = 'V_TAITAA'
            elif wordmap['lemma'].endswith('tää'):
                wordmap['new_para'] = 'V_TIETÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 76, 'F'],
                                   ['front', 'back'])
        else:
            fail_guess_because(wordmap, ['V', 76],
                               ['F'])
    elif wordmap['kotus_tn'] == 77:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aa'):
                wordmap['new_para'] = 'V_VIPAJAA'
            elif wordmap['lemma'].endswith('ää'):
                wordmap['new_para'] = 'V_HELÄJÄÄ'
            else:
                fail_guess_because(wordmap, ['V', 77, False],
                                   ['vasen'])
        else:
            fail_guess_because(wordmap, ['V', 77],
                               [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 78:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aa'):
                wordmap['new_para'] = 'V_RAIKAA'
            elif wordmap['lemma'].endswith('ää'):
                wordmap['new_para'] = 'V_ÄHKÄÄ'
            elif wordmap['lemma'].endswith('ata'):
                wordmap['new_para'] = 'V_HALAJAA'
            else:
                fail_guess_because(wordmap, ['V', 78, False],
                                   ['aa', 'ää', 'ata'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('kkaa'):
                wordmap['new_para'] = 'V_TUIKKAA'
            else:
                fail_guess_because(wordmap, ['V', 78, 'A'],
                                   ['kkaa'])
        else:
            fail_guess_because(wordmap, ['V', 78],
                               [False, 'A'])
    elif tn == 99:
        fail_guess_because(wordmap, ['V', 99], [99],
                           "Illegal class for V, 99 can only apply to P")
        wordmap['new_para'] = '#'
    elif tn == 1067:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('olla'):
                wordmap['new_para'] = 'V_OLLA'
            else:
                fail_guess_because(wordmap, ['V', 10, 'D', 'OLLA'],
                                   ['olla'], 'must be olla')
    elif tn == 1099:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ei'):
                wordmap['new_para'] = 'V_EI'
            else:
                fail_guess_because(wordmap, ['V', 99, 'D', 'EI'],
                                   ['ei'], 'must be ei')
    else:
        fail_guess_because(wordmap, ['V'],
                           ['52-78', '99', '1067'])
    return wordmap


def guess_new_acro(wordmap):
    if wordmap['lemma'][-1] == '1':
        wordmap['new_para'] = 'ACRO_YKSI'
    elif wordmap['lemma'][-1] == '2':
        wordmap['new_para'] = 'ACRO_KAKSI'
    elif wordmap['lemma'][-1] == '3':
        wordmap['new_para'] = 'ACRO_KOLME'
    elif wordmap['lemma'][-1] == '4':
        wordmap['new_para'] = 'ACRO_NELJÄ'
    elif wordmap['lemma'][-1] == '5':
        wordmap['new_para'] = 'ACRO_VIISI'
    elif wordmap['lemma'][-1] == '6':
        wordmap['new_para'] = 'ACRO_KUUSI'
    elif wordmap['lemma'][-1] == '7':
        wordmap['new_para'] = 'ACRO_SEITSEMÄN'
    elif wordmap['lemma'][-1] == '8':
        wordmap['new_para'] = 'ACRO_KAHDEKSAN'
    elif wordmap['lemma'][-1] == '9':
        wordmap['new_para'] = 'ACRO_YHDEKSÄN'
    elif wordmap['lemma'][-1] == '0':
        wordmap['new_para'] = 'ACRO_NOLLA'
    elif wordmap['lemma'][-1] in ['a', 'A']:
        wordmap['new_para'] = 'ACRO_AA'
    elif wordmap['lemma'][-1] in ['b', 'B', 'C', 'c', 'd', 'D', 'e', 'E', 'g', 'G', 'p', 'P', 't', 'T', 'v', 'V', 'w', 'W']:
        wordmap['new_para'] = 'ACRO_EE'
    elif wordmap['lemma'][-1] in ['f', 'F', 'l', 'L', 'm', 'M', 'n', 'N', 'r', 'R', 's', 'S', 'x', 'X', 'š', 'Š', 'ž', 'Ž']:
        wordmap['new_para'] = 'ACRO_ÄKS'
    elif wordmap['lemma'][-1] in ['h', 'H', 'k', 'K', 'o', 'O', 'å', 'Å']:
        wordmap['new_para'] = 'ACRO_OO'
    elif wordmap['lemma'][-1] in ['i', 'I', 'j', 'J']:
        wordmap['new_para'] = 'ACRO_II'
    elif wordmap['lemma'][-1] in ['q', 'Q', 'u', 'U']:
        wordmap['new_para'] = 'ACRO_UU'
    elif wordmap['lemma'][-1] in ['y', 'Y', 'ü', 'Ü']:
        wordmap['new_para'] = 'ACRO_YY'
    elif wordmap['lemma'][-1] in ['z', 'Z']:
        wordmap['new_para'] = 'ACRO_ZET'
    elif wordmap['lemma'][-1] in ['ä', 'Ä']:
        wordmap['new_para'] = 'ACRO_ÄÄ'
    elif wordmap['lemma'][-1] in ['ö', 'Ö']:
        wordmap['new_para'] = 'ACRO_ÖÖ'
    elif wordmap['lemma'][-1] == '€':
        wordmap['new_para'] = 'ACRO_EURO'
    elif wordmap['lemma'][-1] == 'Ω':
        wordmap['new_para'] = 'ACRO_OHMI'
    elif wordmap['lemma'][-1] in ['¢', '¥']:
        wordmap['new_para'] = 'ACRO_SENTTI'
    elif wordmap['lemma'][-1] == '$':
        wordmap['new_para'] = 'ACRO_DOLLARI'
    elif wordmap['lemma'][-1] in ['£', '₤', '+']:
        wordmap['new_para'] = 'ACRO_PUNTA'
    elif wordmap['lemma'][-1] in ['²', '³'] and wordmap['lemma'][-2] == 'm':
        wordmap['new_para'] = 'ACRO_ÄKS'
    else:
        fail_guess_because(wordmap, ['ACRO'], ['A-Ö', '€$£Ω¢¥₤'],
                           "Last character of lemma fail")
    return wordmap


def guess_new_pronoun(wordmap):
    if wordmap['kotus_tn'] == 7:
        if wordmap['lemma'] == 'kaikki':
            wordmap['new_para'] = 'PRON_KAIKKI'
        else:
            fail_guess_because(wordmap, ['PRON', 7], ['kaikki'])
    elif wordmap['kotus_tn'] == 8:
        if wordmap['lemma'] == 'itse':
            wordmap['new_para'] = 'PRON_ITSE'
        else:
            fail_guess_because(wordmap, ['PRON', 8], ['itse'])
    elif wordmap['kotus_tn'] == 9:
        if wordmap['lemma'] == 'sama':
            wordmap['new_para'] = 'PRON_SAMA'
        else:
            fail_guess_because(wordmap, ['PRON', 9], ['sama'])
    elif wordmap['kotus_tn'] == 10:
        if wordmap['lemma'] == 'muutama':
            wordmap['new_para'] = 'PRON_MUUTAMA'
        else:
            fail_guess_because(wordmap, ['PRON', 8], ['muutama'])
    elif wordmap['kotus_tn'] == 15:
        if wordmap['lemma'] == 'usea':
            wordmap['new_para'] = 'PRON_USEA'
        else:
            fail_guess_because(wordmap, ['PRON', 15], ['itse'])
    elif wordmap['kotus_tn'] == 16:
        if wordmap['lemma'] == 'jompikumpi':
            wordmap['new_para'] = 'PRON_JOMPIKUMPI'
        elif wordmap['lemma'] in ['jompi', 'kumpi']:
            wordmap['new_para'] = 'PRON_KUMPI'
        elif wordmap['lemma'] == 'kumpikaan':
            wordmap['new_para'] = 'PRON_KUMPIKAAN'
        elif wordmap['lemma'] == 'kumpikin':
            wordmap['new_para'] = 'PRON_KUMPIKIN'
        elif wordmap['lemma'] in ['molempi', 'molemmat']:
            wordmap['new_para'] = 'PRON_MOLEMMAT'
        elif wordmap['lemma'] in ['useampi']:
            wordmap['new_para'] = 'PRON_USEAMPI'
        else:
            fail_guess_because(
                wordmap, ['PRON', 16], ['jompi', 'kumpi', '...'])
    elif wordmap['kotus_tn'] == 18:
        if wordmap['lemma'] == 'muu':
            wordmap['new_para'] = 'PRON_MUU'
        else:
            fail_guess_because(wordmap, ['PRON', 18], ['muu'])
    elif wordmap['kotus_tn'] == 23:
        if wordmap['lemma'] == 'moni':
            wordmap['new_para'] = 'PRON_MONI'
        else:
            fail_guess_because(wordmap, ['PRON', 23], ['moni'])
    elif wordmap['kotus_tn'] == 31:
        if wordmap['lemma'] == 'yksi':
            wordmap['new_para'] = 'PRON_YKSI'
        else:
            fail_guess_because(wordmap, ['PRON', 31], ['yksi'])
    elif wordmap['kotus_tn'] == 36:
        if wordmap['lemma'] in ['usein', 'useimmat']:
            wordmap['new_para'] = 'PRON_USEIMMAT'
        else:
            fail_guess_because(wordmap, ['PRON', 36], ['usein', 'useimmat'])
    elif wordmap['kotus_tn'] == 38:
        if wordmap['lemma'].endswith('lainen'):
            wordmap['new_para'] = 'PRON_LAINEN'
        elif wordmap['lemma'] == 'toinen':
            wordmap['new_para'] = 'PRON_TOINEN'
        elif wordmap['harmony'] == 'back':
            wordmap['new_para'] = 'PRON_JOKAINEN'
        elif wordmap['harmony'] == 'front':
            wordmap['new_para'] = 'PRON_IKINEN'
        else:
            fail_guess_because(
                wordmap, ['PRON', 38], ['back', 'front', 'lainen'])
    elif wordmap['kotus_tn'] == 41:
        if wordmap['lemma'] == 'monias':
            wordmap['new_para'] = 'PRON_MONIAS'
        elif wordmap['lemma'] == 'eräs':
            wordmap['new_para'] = 'PRON_ERÄS'
        else:
            fail_guess_because(wordmap, ['PRON', 41], ['monias', 'eräs'])
    elif wordmap['kotus_tn'] == 45:
        if wordmap['lemma'] == 'mones':
            wordmap['new_para'] = 'PRON_MONES'
        else:
            fail_guess_because(wordmap, ['PRON', 45], ['mones'])
    elif wordmap['kotus_tn'] == 101:
        if wordmap['lemma'] in ['minä', 'sinä']:
            wordmap['new_para'] = 'PRON_MINÄ'
        elif wordmap['lemma'] == 'hän':
            wordmap['new_para'] = 'PRON_HÄN'
        elif wordmap['lemma'] in ['me', 'te', 'he']:
            wordmap['new_para'] = 'PRON_ME'
        elif wordmap['lemma'] == 'tämä':
            wordmap['new_para'] = 'PRON_TÄMÄ'
        elif wordmap['lemma'] == 'tuo':
            wordmap['new_para'] = 'PRON_TUO'
        elif wordmap['lemma'] == 'se':
            wordmap['new_para'] = 'PRON_SE'
        elif wordmap['lemma'] == 'nämä':
            wordmap['new_para'] = 'PRON_NÄMÄ'
        elif wordmap['lemma'] == 'nuo':
            wordmap['new_para'] = 'PRON_NUO'
        elif wordmap['lemma'] == 'ne':
            wordmap['new_para'] = 'PRON_NE'
        elif wordmap['lemma'] == 'joka':
            wordmap['new_para'] = 'PRON_JOKA'
        elif wordmap['lemma'] == 'jokin':
            wordmap['new_para'] = 'PRON_JOKIN'
        elif wordmap['lemma'] == 'joku':
            wordmap['new_para'] = 'PRON_JOKU'
        elif wordmap['lemma'] == 'kuka':
            wordmap['new_para'] = 'PRON_KUKA'
        elif wordmap['lemma'] == 'kukaan':
            wordmap['new_para'] = 'PRON_KUKAAN'
        elif wordmap['lemma'].endswith('kukin'):
            wordmap['new_para'] = 'PRON_KUKIN'
        elif wordmap['lemma'] == 'mikin':
            wordmap['new_para'] = 'PRON_MIKIN'
        elif wordmap['lemma'] == 'mikä':
            wordmap['new_para'] = 'PRON_MIKÄ'
        elif wordmap['lemma'] == 'mikään':
            wordmap['new_para'] = 'PRON_MIKÄÄN'
        elif wordmap['lemma'] == 'missä':
            wordmap['new_para'] = 'PRON_MISSÄ'
        elif wordmap['lemma'] == 'missäkään':
            wordmap['new_para'] = 'PRON_MISSÄKÄÄN'
        elif wordmap['lemma'] == 'missään':
            wordmap['new_para'] = 'PRON_MISSÄÄN'
        elif wordmap['lemma'] == 'monta':
            wordmap['new_para'] = 'PRON_MONTA'
        elif wordmap['lemma'] == 'muuan':
            wordmap['new_para'] = 'PRON_MUUAN'
        elif wordmap['lemma'] in ['mä', 'sä']:
            wordmap['new_para'] = 'PRON_MÄ'
        elif wordmap['lemma'] in ['mie', 'sie']:
            wordmap['new_para'] = 'PRON_MIE'
        elif wordmap['lemma'] == 'toi':
            wordmap['new_para'] = 'PRON_TOI'
        elif wordmap['lemma'] == 'noi':
            wordmap['new_para'] = 'PRON_NOI'
        elif wordmap['lemma'].endswith('ainoa'):
            wordmap['new_para'] = 'PRON_AINOA'
        elif wordmap['lemma'] in ['jota', 'kenkään', 'kuta', 'ma', 'mi',
                                  'missäkin', 'mikäkin', 'sa', 'tää', 'ken',
                                  'koko', 'yks', 'yksikään', 'mää', 'sää', 'hää']:
            wordmap['new_para'] = '#'
        else:
            fail_guess_because(wordmap, ['PRON', 101], ['minä', 'sinä', 'hän',
                                                        'me', 'te', 'he', '...'])
    elif wordmap['kotus_tn'] == 1101:
        # temporary hacks for multiclassing
        if wordmap['lemma'] == 'joka':
            wordmap['new_para'] = 'PRON_JOKA'
        elif wordmap['lemma'] == 'mikä':
            wordmap['new_para'] = 'PRON_MIKÄ'
        else:
            fail_guess_because(wordmap, ['PRON', 1101], ['joka', 'mikä'])
    else:
        fail_guess_because(wordmap, ['PRON'], [7, 8, 9, 10, 15, 16, 23, 31, 38,
                                               41, 45, 101],
                           'Not implemented pron classes yet')
    return wordmap


def guess_new_numeral(wordmap):
    tn = wordmap['kotus_tn']
    if tn == 6:
        if wordmap['lemma'].endswith('jardi'):
            wordmap['new_para'] = 'NUM_MILJARDI'
        else:
            fail_guess_because(wordmap, ['NUM', 6],
                               ['iljardi'])
    elif tn == 9:
        if wordmap['lemma'].endswith('sata'):
            wordmap['new_para'] = 'NUM_SATA'
        else:
            fail_guess_because(wordmap, ['NUM', 9], ['sata'])
    elif tn == 10:
        if wordmap['lemma'].endswith('an'):
            wordmap['new_para'] = 'NUM_KAHDEKSAN'
        elif wordmap['lemma'].endswith('än'):
            wordmap['new_para'] = 'NUM_YHDEKSÄN'
        elif wordmap['lemma'].endswith('a'):
            wordmap['new_para'] = 'NUM_MILJOONA'
        elif wordmap['lemma'].endswith('ä'):
            wordmap['new_para'] = 'NUM_NELJÄ'
        else:
            fail_guess_because(wordmap, ['NUM', 10],
                               ['yksi', 'kaksi'])
    elif tn == 27:
        if wordmap['lemma'].endswith('kuusi'):
            wordmap['new_para'] = 'NUM_KUUSI'
        elif wordmap['lemma'].endswith('viisi'):
            wordmap['new_para'] = 'NUM_VIISI'
        else:
            fail_guess_because(wordmap, ['NUM', 27],
                               ['viisi', 'kuusi'])
    elif wordmap['kotus_tn'] == 31:
        if wordmap['lemma'].endswith('kaksi'):
            wordmap['new_para'] = 'NUM_KAKSI'
        elif wordmap['lemma'].endswith('yksi'):
            wordmap['new_para'] = 'NUM_YKSI'
        else:
            fail_guess_because(wordmap, ['NUM', 31],
                               ['yksi', 'kaksi'])
    elif wordmap['kotus_tn'] == 32:
        if wordmap['lemma'].endswith('kymmenen'):
            wordmap['new_para'] = 'NUM_KYMMENEN'
        elif wordmap['lemma'].endswith('kymmen'):
            wordmap['new_para'] = 'N_KYMMEN'
        else:
            fail_guess_because(wordmap, ['NUM', 32],
                               ['viisi', 'kuusi'])
    elif wordmap['kotus_tn'] == 38:
        if wordmap['lemma'].endswith('oinen'):
            wordmap['new_para'] = 'NUM_TOINEN'
        elif wordmap['lemma'].endswith('äinen'):
            wordmap['new_para'] = 'NUM_ENSIMMÄINEN'
        else:
            fail_guess_because(wordmap, ['NUM', 38],
                               ['ensimmäinen', 'toinen'])
    elif wordmap['kotus_tn'] == 45:
        if wordmap['lemma'].endswith('s') and wordmap['harmony'] == 'back':
            wordmap['new_para'] = 'NUM_KOLMAS'
        elif wordmap['lemma'].endswith('s') and wordmap['harmony'] == 'front':
            wordmap['new_para'] = 'NUM_NELJÄS'
        else:
            fail_guess_because(wordmap, ['N', 45, False],
                               ['s'])
    elif wordmap['kotus_tn'] == 46:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('tuhat'):
                wordmap['new_para'] = 'NUM_TUHAT'
            else:
                fail_guess_because(wordmap, ['NUM', 46],
                                   ['tuhat'])
    elif wordmap['kotus_tn'] == 99:
        wordmap['new_para'] = 'NUM_KYMMENTÄ'
    elif wordmap['kotus_tn'] == 1008:
        if wordmap['lemma'].endswith('kolme'):
            wordmap['new_para'] = 'NUM_KOLME'
        else:
            fail_guess_because(wordmap, ['NUM', 1008], ['kolme'])
    else:
        fail_guess_because(wordmap, ['NUM'], [3, 6, 9, 10, 27, 31, 32, 45, 46,
                                              1008], "Not a NUM class?")
        wordmap['new_para'] = '#'
    return wordmap


def guess_new_particle(wordmap):
    if wordmap['clitics'] == 'none':
        wordmap['clitics'] = None
    elif wordmap['particle'] and wordmap['particle'] == 'ADVERB':
        wordmap['clitics'] = 'opt'

    if wordmap['possessive']:
        if wordmap['possessive'] == 'opt':
            if wordmap['harmony'] == 'front':
                if wordmap['lemma'].endswith('ä'):
                    wordmap['new_para'] = 'PCLE_IKINÄ'
                elif wordmap['lemma'].endswith('e'):
                    wordmap['new_para'] = 'PCLE_YLLE'
                elif wordmap['lemma'].endswith('i'):
                    wordmap['new_para'] = 'PCLE_LISÄKSI'
                elif wordmap['lemma'].endswith('den'):
                    wordmap['new_para'] = 'PCLE_NÄHDEN'
                elif wordmap['lemma'].endswith('n'):
                    wordmap['new_para'] = 'PCLE_NÄKYVIIN'
                else:
                    fail_guess_because(wordmap, ['PCLE', 'POSS=OPT'],
                                       ['ä', 'e', 'i', 'n', 'front'])
            elif wordmap['harmony'] == 'back':
                if wordmap['lemma'].endswith('a'):
                    wordmap['new_para'] = 'PCLE_KOTONA'
                elif wordmap['lemma'].endswith('e'):
                    wordmap['new_para'] = 'PCLE_ALLE'
                elif wordmap['lemma'].endswith('i'):
                    wordmap['new_para'] = 'PCLE_VUOKSI'
                elif wordmap['lemma'].endswith('n'):
                    wordmap['new_para'] = 'PCLE_VALTAAN'
                else:
                    fail_guess_because(wordmap, ['PCLE', 'POSS=OPT'],
                                       ['a', 'e', 'i', 'n', 'back'])
            else:
                fail_guess_because(wordmap, ["PCLE", "POSS"],
                                   ["front", "back"])
        elif wordmap['possessive'] == 'obl':
            if wordmap['harmony'] == 'front':
                if wordmap['lemma'].endswith('än'):
                    wordmap['new_para'] = 'PCLE_HYVILLÄÄN'
                elif wordmap['lemma'].endswith('en'):
                    wordmap['new_para'] = 'PCLE_LEVÄLLEEN'
                elif wordmap['lemma'].endswith('nsä'):
                    wordmap['new_para'] = 'PCLE_YLIPÄÄNSÄ'
                else:
                    fail_guess_because(wordmap, ['PCLE', 'POSS=OBL'],
                                       ['än', 'en', 'nsä', 'front'])
            elif wordmap['harmony'] == 'back':
                if wordmap['lemma'].endswith('an'):
                    wordmap['new_para'] = 'PCLE_ILKOSILLAAN'
                elif wordmap['lemma'].endswith('en'):
                    wordmap['new_para'] = 'PCLE_ISTUALLEEN'
                elif wordmap['lemma'].endswith('nsä'):
                    wordmap['new_para'] = 'PCLE_AIKANSA'
                else:
                    fail_guess_because(wordmap, ['PCLE', 'POSS=OBL'],
                                       ['an', 'en', 'nsa', 'back'])
            else:
                fail_guess_because(wordmap, ["PCLE", "POSS"],
                                   ["front", "back"])
        else:
            fail_guess_because(wordmap, ["PCLE", "POSS"],
                               ["opt", "obl"])
    # Clitics +kA (+s) only manually (PCLE_JONNE, PCLE_KUHUN, PCLE_MITEN)
    elif wordmap['clitics']:
        if wordmap['harmony'] == 'front':
            wordmap['new_para'] = 'PCLE_TYHMÄSTI'
        elif wordmap['harmony'] == 'back':
            wordmap['new_para'] = 'PCLE_NOPEASTI'
        else:
            fail_guess_because(wordmap, ["PCLE", "CLIT"],
                               ["front", "back"])
    elif wordmap['particle'] and wordmap['particle'] == 'INTERJECTION':
        # (Is it a good idea to classify new interjectons as chainable by default?)
        wordmap['new_para'] = 'PCLE_HAH'
    else:
        wordmap['new_para'] = 'PCLE_VAAN'
    return wordmap
