#!/usr/bin/env python3

from sys import stderr
from omor_strings_io import fail_guess_because

def guess_new_class(wordmap):
    '''Guess more exact classification now
    '''
    tn = int(wordmap['kotus_tn'])
    if not wordmap['pos']:
        wordmap['pos'] = 'PARTICLE'
        wordmap['new_para'] = '#'
    if wordmap['pos'] in ['PROPER', 'NOUN']:
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
    elif wordmap['pos'] == 'ADVERB':
        wordmap = guess_new_adverb(wordmap)
    elif wordmap['pos'] == 'ADPOSITION':
        wordmap = guess_new_adposition(wordmap)
    elif wordmap['pos'] in ['PARTICLE', 'INTERJECTION', 'CONJUNCTION', 'ABBREVIATION']:
        wordmap['new_para'] = '#'
    else:
        fail_guess_because(wordmap, ["POS"], ['!POS', 'PARTICLE', 'N', 'PROP', 'A', 'V', 'ACRO', 'NUM', 'INTJ', 'CONJ', 'ABBR'])
    return wordmap

def guess_new_noun(wordmap):
    '''Guessing new noun class based on kotus class.'''
    tn = int(wordmap['kotus_tn'])
    if not wordmap['plurale_tantum']:
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
                    wordmap['new_para'] = 'N_TORTTY'
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
                if wordmap['lemma'].endswith('uku'):
                    wordmap['new_para'] = 'N_LUKU'
                elif wordmap['lemma'].endswith('yky'):
                    wordmap['new_para'] = 'N_KYKY'
                else:
                    fail_guess_because(wordmap, ['N', 1, 'M'],
                            ['uku', 'yky'])
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
                    wordmap['new_para'] = 'N_SELKI'
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
                    wordmap['new_para'] = 'N_AAMUSEITSEMÄN'
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
                        "New loan words do not simply walk into quantitative gradation")
        elif tn == 9:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('a') or wordmap['lemma'].endswith('A'):
                    wordmap['new_para'] = 'N_KIRJA'
                elif wordmap['lemma'].endswith('ą'):
                    wordmap['new_para'] = 'N_KIRJA'
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_para'] = 'N_YMPÄRYSTÄ'
                else:
                    fail_guess_because(wordmap, ['N', 9, False],
                            ['a', 'ä'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('ka'):
                    wordmap['new_para'] = 'N_VIRKA'
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
                    wordmap['new_para'] = 'N_HALPA'
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
                if wordmap['lemma'].endswith('a') or wordmap['lemma'].endswith('A'):
                    wordmap['new_para'] = 'N_SOITTAJA'
                elif wordmap['lemma'].endswith('ą'):
                    wordmap['new_para'] = 'N_SOITTAJA'
                elif wordmap['lemma'].endswith('ă'):
                    wordmap['new_para'] = 'N_SOITTAJA'
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_para'] = 'N_HÖPÖTTÄJÄ'
                elif wordmap['lemma'].endswith('an'):
                    wordmap['new_para'] = 'N_AAMUKAHDEKSAN'
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_para'] = 'N_AAMUYHDEKSÄN'
                else:
                    fail_guess_because(wordmap, ['N', 10, False],
                            ['a ą ă', 'ä'])
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
                if wordmap['lemma'].endswith('ka'):
                    wordmap['new_para'] = 'N_VUOKA'
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
                    wordmap['new_para'] = 'N_EMÄNTÄ'
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
                elif wordmap['lemma'].endswith('ă'):
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
                if wordmap['lemma'].endswith('a') or wordmap['lemma'].endswith('A'):
                    wordmap['new_para'] = 'N_MAKKARA'
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_para'] = 'N_HÄKKYRÄ'
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
                    wordmap['new_para'] = 'N_KÄMEKKÄ'
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
                    wordmap['new_para'] = 'N_AINOA'
                elif wordmap['lemma'].endswith('ôa'):
                    wordmap['new_para'] = 'N_AINOA'
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
                elif wordmap['lemma'].endswith('oo'):
                    wordmap['new_para'] = 'N_TIENOO'
                elif wordmap['lemma'].endswith('uu'):
                    wordmap['new_para'] = 'N_LEIKKUU'
                elif wordmap['lemma'].endswith('yy'):
                    wordmap['new_para'] = 'N_HYÖTYY'
                elif wordmap['lemma'].endswith('ää'):
                    wordmap['new_para'] = 'N_HYVINKÄÄ'
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
                fail_guess_because(wordmap, ['N', 18],
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
                if wordmap['lemma'].endswith('gay'):
                    wordmap['new_para'] = 'N_GAY'
                elif wordmap['lemma'].endswith('è') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ROSÉ'
                elif wordmap['lemma'].endswith('é') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_ROSÉ'
                elif wordmap['lemma'].endswith('é') and wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_BÉBÉ'
                #else:
                #    fail_guess_because(wordmap, ['N', 21, False],
                #            ['gay', 'é', 'è'], "guessing 21 is not possible")
            else:
                fail_guess_because(wordmap, ['N', 21],
                        [False])
        elif tn == 22:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ait'):
                    wordmap['new_para'] = 'N_PARFAIT'
                if wordmap['lemma'].endswith('ow'):
                    wordmap['new_para'] = 'N_SHOW'
                #else:
                #    fail_guess_because(wordmap, ['N', 22, False],
                #            ['ait', 'ow'], "guessing 22 is not possible")
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
                fail_guess_because(wordmap, ['N', 22],
                        [False])
        elif tn in [24, 26]:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_RUUHI'
                elif wordmap['harmony'] == 'front' and wordmap['lemma'].endswith('meri'):
                    wordmap['new_para'] = 'N_MERI'
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
                        fail_guess_because(wordmap, ['N', 26, False, 'si'],
                                ['back', 'front'])
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
                    else:
                        fail_guess_because(wordmap, ['N', 31, False, 'ksi'],
                            ['back'])
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
                else:
                    fail_guess_because(wordmap, ['N', 33, 'J'],
                        ['jin', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 33],
                    [False, 'A', 'C-F', 'J-L'])
        elif wordmap['kotus_tn'] == 34:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('toin'):
                    wordmap['new_para'] = 'N_KALATOIN'
                elif wordmap['lemma'].endswith('töin'):
                    wordmap['new_para'] = 'N_NIMETÖIN'
                else:
                    fail_guess_because(wordmap, ['N', 34, False],
                            ['toin', 'töin'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pan'):
                    wordmap['new_para'] = 'N_HAPAN'
                else:
                    fail_guess_because(wordmap, ['N', 34, 'B'],
                            ['pan'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('ton'):
                    wordmap['new_para'] = 'N_KELVOTON'
                elif wordmap['lemma'].endswith('tön'):
                    wordmap['new_para'] = 'N_HÖMETÖN'
                else:
                    fail_guess_because(wordmap, ['N', 34, 'C'],
                            ['ton', 'tön'])
            else:
                fail_guess_because(wordmap, ['N', 34], [False, 'C'])
        elif wordmap['kotus_tn'] == 35:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_AAMUKAKSI'
                elif wordmap['harmony'] == 'front':
                    wordmap['new_para'] = 'N_AAMUYKSI'
                else:
                    fail_guess_because(wordmap, ['N', 35, False],
                        ['back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 35],
                    [False, 'C-F', 'J-L'])
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
                    fail_guess_because(wordmap, ['N', 38, False],
                        ['front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 38],
                    [False], "cannot have gradation")
        elif wordmap['kotus_tn'] == 40:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
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
                    wordmap['new_para'] = 'N_TIIVIS'
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
                elif wordmap['lemma'].endswith('lles') and wordmap['harmony'] == 'back':
                    wordmap['new_para'] = 'N_AKILLES'
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
                        ['ät','et'])
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
                fail_guess_because(wordmap, ['N', 46],
                    [False], "cannot gradate")
        elif tn == 48:
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
                    [False, 'A-F', 'H-L'])
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
        elif tn == 99:
            wordmap['new_para'] = '#'
        elif tn == 1007:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('veli'):
                    wordmap['new_para'] = 'N_VELI'
                else:
                    fail_guess_because(wordmap, ['N', 7, False, 'VELI'],
                            ['veli'], 'must be veli')
            else:
                fail_guess_because(wordmap, ['N', 7, 'VELI'],
                        [False], 'Cannot gradate')
        elif tn == 1009:
            if wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('aika'):
                    wordmap['new_para'] = 'N_AIKA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'D', 'AIKA'],
                            ['aika'], 'must be aika')
            elif not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aika'):
                    print("N_AIKA is k:0 gradation + i:j variation!",
                            "in", wordmap['lemma'],
                            file=stderr)
                    wordmap['new_para'] = 'N_AIKA'
                else:
                    fail_guess_because(wordmap, ['N', 9, 'D', 'AIKA'],
                            ['aika'], 'must be aika')
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('aika'):
                    wordmap['new_para'] = 'N_AIKA'
                    print("N_AIKA is k:0 gradation + i:j variation, not k:j!",
                            "in", wordmap['lemma'],
                            file=stderr)
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
                    print("N_POIKA is k:0 gradation + i:j variation!",
                            "in", wordmap['lemma'],
                            file=stderr)
                    wordmap['new_para'] = 'N_POIKA'
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
                if wordmap['lemma'].endswith('veri'):
                    wordmap['new_para'] = 'N_VERI'
                else:
                    fail_guess_because(wordmap, ['N', 24, 'False', 'VERI'],
                            ['poika'], 'must be poika')
            else:
                fail_guess_because(wordmap, ['N', 26, 'VERI'],
                        [False], 'must be 0')
        else:
            fail_guess_because(wordmap, ['N'],
                ['1-49', '99', '1009-1010'])
    #else:
    #    fail_guess_because(wordmap, ['N'],
    #        ['SGT'], 'Plurales missing')
    return wordmap

def guess_new_adjective(wordmap):
    #fail_guess_because(wordmap, ['A'], [], "Not impl Adjs")
    return wordmap

def guess_new_verb(wordmap):
    #fail_guess_because(wordmap, ['V'], [], "Not impl Verbs")
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
        wordmap['new_para'] = 'ACRO_KAKSI'
    elif wordmap['lemma'][-1] in ['a', 'A']:
        wordmap['new_para'] = 'ACRO_AA'
    elif wordmap['lemma'][-1] in ['b', 'B', 'C', 'c', 'd', 'D', 'e', 'E', 'g', 'G', 'p', 'P', 't', 'T', 'v', 'V', 'w', 'W']:
        wordmap['new_para'] = 'ACRO_EE'
    elif wordmap['lemma'][-1] in ['f', 'F', 'l' , 'L', 'm', 'M', 'n', 'N', 'r', 'R', 's', 'S', 'x', 'X']:
        wordmap['new_para'] = 'ACRO_ÄKS'
    elif wordmap['lemma'][-1] in ['h', 'H', 'k', 'K', 'o', 'O', 'å', 'Å']:
        wordmap['new_para'] = 'ACRO_OO'
    elif wordmap['lemma'][-1] in ['i', 'I', 'j', 'J']:
        wordmap['new_para'] = 'ACRO_II'
    elif wordmap['lemma'][-1] in ['q', 'Q', 'u', 'U']:
        wordmap['new_para'] = 'ACRO_UU'
    elif wordmap['lemma'][-1] in ['y', 'Y']:
        wordmap['new_para'] = 'ACRO_YY'
    elif wordmap['lemma'][-1] in ['z', 'Z']:
        wordmap['new_para'] = 'ACRO_ZET'
    elif wordmap['lemma'][-1] in ['ä', 'Ä']:
        wordmap['new_para'] = 'ACRO_ÄÄ'
    elif wordmap['lemma'][-1] in ['ö', 'Ö']:
        wordmap['new_para'] = 'ACRO_ÖÖ'
    return wordmap

def guess_new_pronoun(wordmap):
    #fail_guess_because(wordmap, ['Num'], [], "Not impl Num")
    return wordmap

def guess_new_numeral(wordmap):
    #fail_guess_because(wordmap, ['Num'], [], "Not impl Num")
    return wordmap

def guess_new_adverb(wordmap):
    if wordmap['possessive']:
        if wordmap['harmony'] == 'front':
            if wordmap['lemma'].endswith('e'):
                wordmap['new_para'] = 'ADV_FRONT_POSS_EN_OPT'
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_para'] = 'ADV_FRONT_POSS_ÄN_OPT'
            else:
                wordmap['new_para'] = 'ADV_FRONT_POSS_OPT'
        elif wordmap['harmony'] == 'back':
            if wordmap['lemma'].endswith('a'):
                wordmap['new_para'] = 'ADV_BACK_POSS_AN_OPT'
            elif wordmap['lemma'].endswith('e'):
                wordmap['new_para'] = 'ADV_BACK_POSS_EN_OPT'
            else:
                wordmap['new_para'] = 'ADV_BACK_POSS_OPT'
        else:
            fail_guess_with(wordmap, ["ADV", "POSS"], ["front", "back"])
    elif wordmap['clitics']:
        if wordmap['harmony'] == 'front':
            wordmap['new_para'] = 'ADV_FRONT_CLIT_OPT'
        elif wordmap['harmony'] == 'back':
            wordmap['new_para'] = 'ADV_BACK_CLIT_OPT'
        else:
            fail_guess_with(wordmap, ["ADV", "POSS"], ["front", "back"])
    else:
        wordmap['new_para'] = '#'
    return wordmap

def guess_new_adposition(wordmap):
    if wordmap['possessive']:
        if wordmap['harmony'] == 'front':
            if wordmap['lemma'].endswith('e'):
                wordmap['new_para'] = 'ADP_FRONT_POSS_EN_OPT'
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_para'] = 'ADP_FRONT_POSS_ÄN_OPT'
            else:
                wordmap['new_para'] = 'ADP_FRONT_POSS_OPT'
        elif wordmap['harmony'] == 'back':
            if wordmap['lemma'].endswith('a'):
                wordmap['new_para'] = 'ADP_BACK_POSS_AN_OPT'
            elif wordmap['lemma'].endswith('e'):
                wordmap['new_para'] = 'ADP_BACK_POSS_EN_OPT'
            else:
                wordmap['new_para'] = 'ADP_BACK_POSS_OPT'
        else:
            fail_guess_with(wordmap, ["ADP", "POSS"], ["front", "back"])
    elif wordmap['clitics']:
        if wordmap['harmony'] == 'front':
            wordmap['new_para'] = 'ADP_FRONT_CLIT_OPT'
        elif wordmap['harmony'] == 'back':
            wordmap['new_para'] = 'ADP_BACK_CLIT_OPT'
        else:
            fail_guess_with(wordmap, ["ADP", "POSS"], ["front", "back"])
    else:
        wordmap['new_para'] = '#'
    return wordmap
