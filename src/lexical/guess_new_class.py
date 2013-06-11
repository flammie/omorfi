#!/usr/bin/env python3

from sys import stderr
from omor_strings_io import fail_guess_because

def guess_new_class(wordmap):
    '''Guess more exact classification now
    '''
    tn = int(wordmap['kotus_tn'])
    if not wordmap['pos']:
        wordmap['pos'] = 'PARTICLE'
        wordmap['new_paras'] = ['#']
    if wordmap['is_prefix']:
        wordmap['new_paras'] = ['PREFIX_COMPOUND']
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
        fail_guess_because(wordmap, ["POS"], ['!POS', 'PARTICLE', 'N', 'PROP', 'A', 'V', 'ACRO', 'NUM', 'INTJ', 'CONJ', 'ABBR'])
    if not wordmap['new_paras']:
        fail_guess_because(wordmap, ["???"], ["???"], 
            "shouldn't reach this point (missing case somewhere)\n"
            "Temporarily recovering by setting new_para to #!")
        wordmap['new_paras'] = ['#']
    return wordmap

def guess_new_noun(wordmap):
    '''Guessing new noun class based on kotus class.'''
    tn = int(wordmap['kotus_tn'])
    if not wordmap['plurale_tantum'] or wordmap['plurale_tantum'] == 'common':
        if tn == 1:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('o') or wordmap['lemma'].endswith('O'):
                    wordmap['new_paras'] = ['N_TALO']
                elif wordmap['lemma'].endswith('u') or wordmap['lemma'].endswith('U'):
                    wordmap['new_paras'] = ['N_ASU']
                elif wordmap['lemma'].endswith('ú'):
                    wordmap['new_paras'] = ['N_ASU']
                elif wordmap['lemma'].endswith('y') or wordmap['lemma'].endswith('Y'):
                    wordmap['new_paras'] = ['N_KÄRRY']
                elif wordmap['lemma'].endswith('ÿ'):
                    wordmap['new_paras'] = ['N_KÄRRY']
                elif wordmap['lemma'].endswith('ö'):
                    wordmap['new_paras'] = ['N_MÖMMÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, False], 
                            ['o O', 'u ú', 'y ÿ Y', 'ö'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('ko'):
                    wordmap['new_paras'] = ['N_UKKO']
                elif wordmap['lemma'].endswith('ku'):
                    wordmap['new_paras'] = ['N_TIKKU']
                elif wordmap['lemma'].endswith('ky'):
                    wordmap['new_paras'] = ['N_MYRKKY']
                elif wordmap['lemma'].endswith('kö'):
                    wordmap['new_paras'] = ['N_YÖKKÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'A'], 
                            ['ko', 'ku', 'ky', 'kö'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppo'):
                    wordmap['new_paras'] = ['N_HAPPO']
                elif wordmap['lemma'].endswith('ppu'):
                    wordmap['new_paras'] = ['N_LIPPU']
                elif wordmap['lemma'].endswith('ppy'):
                    wordmap['new_paras'] = ['N_RYYPPY']
                elif wordmap['lemma'].endswith('ppö'):
                    wordmap['new_paras'] = ['N_TÖRPPÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'B'], 
                            ['ppo', 'ppu', 'ppy', 'ppö'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tto'):
                    wordmap['new_paras'] = ['N_HIRTTO']
                elif wordmap['lemma'].endswith('ttu'):
                    wordmap['new_paras'] = ['N_TORTTU']
                elif wordmap['lemma'].endswith('tty'):
                    wordmap['new_paras'] = ['N_PYTTY']
                elif wordmap['lemma'].endswith('ttö'):
                    wordmap['new_paras'] = ['N_PÖNTTÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'C'], 
                            ['tto', 'ttu', 'tty', 'ttö'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('uoko'):
                    wordmap['new_paras'] = ['N_RUOKO']
                elif wordmap['lemma'].endswith('iuku'):
                    wordmap['new_paras'] = ['N_LIUKU']
                elif wordmap['lemma'].endswith('ko'):
                    wordmap['new_paras'] = ['N_TEKO']
                elif wordmap['lemma'].endswith('ku'):
                    wordmap['new_paras'] = ['N_MAKU']
                elif wordmap['lemma'].endswith('ky'):
                    wordmap['new_paras'] = ['N_NÄKY']
                elif wordmap['lemma'].endswith('kö'):
                    wordmap['new_paras'] = ['N_NÄKÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'D'],
                            ['ko', 'ku', 'ky', 'kö'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('po'):
                    wordmap['new_paras'] = ['N_HEPO']
                elif wordmap['lemma'].endswith('pu'):
                    wordmap['new_paras'] = ['N_APU']
                elif wordmap['lemma'].endswith('py'):
                    wordmap['new_paras'] = ['N_KÄPY']
                elif wordmap['lemma'].endswith('pö'):
                    wordmap['new_paras'] = ['N_LÖPÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'E'],
                            ['po', 'pu', 'py', 'pö'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('to'):
                    wordmap['new_paras'] = ['N_VETO']
                elif wordmap['lemma'].endswith('tu'):
                    wordmap['new_paras'] = ['N_KUITU']
                elif wordmap['lemma'].endswith('ty'):
                    wordmap['new_paras'] = ['N_VETY']
                elif wordmap['lemma'].endswith('tö'):
                    wordmap['new_paras'] = ['N_HÄÄTÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'F'],
                            ['to', 'tu', 'ty', 'tö'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nko'):
                    wordmap['new_paras'] = ['N_RUNKO']
                elif wordmap['lemma'].endswith('nku'):
                    wordmap['new_paras'] = ['N_VINKU']
                elif wordmap['lemma'].endswith('nky'):
                    wordmap['new_paras'] = ['N_SÄNKY']
                elif wordmap['lemma'].endswith('nkö'):
                    wordmap['new_paras'] = ['N_YLÄNKÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'G'],
                            ['nko', 'nku', 'nky', 'nkö'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mpo'):
                    wordmap['new_paras'] = ['N_SAMPO']
                elif wordmap['lemma'].endswith('mpu'):
                    wordmap['new_paras'] = ['N_RUMPU']
                elif wordmap['lemma'].endswith('mpö'):
                    wordmap['new_paras'] = ['N_LÄMPÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'H'],
                            ['mpo', 'mpu', 'mpö'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('lto'):
                    wordmap['new_paras'] = ['N_KIELTO']
                elif wordmap['lemma'].endswith('ltu'):
                    wordmap['new_paras'] = ['N_HUOLITELTU']
                elif wordmap['lemma'].endswith('lty'):
                    wordmap['new_paras'] = ['N_EPÄILTY']
                elif wordmap['lemma'].endswith('ltö'):
                    wordmap['new_paras'] = ['N_SISÄLTÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'I'],
                            ['lto', 'ltu', 'lty', 'ltö'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nto'):
                    wordmap['new_paras'] = ['N_TUNTO']
                elif wordmap['lemma'].endswith('ntu'):
                    wordmap['new_paras'] = ['N_LINTU']
                elif wordmap['lemma'].endswith('nty'):
                    wordmap['new_paras'] = ['N_MÄNTY']
                elif wordmap['lemma'].endswith('ntö'):
                    wordmap['new_paras'] = ['N_KÄÄNTÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'J'],
                            ['nto', 'ntu', 'nty', 'ntö'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rto'):
                    wordmap['new_paras'] = ['N_SIIRTO']
                elif wordmap['lemma'].endswith('rtu'):
                    wordmap['new_paras'] = ['N_MERTU']
                elif wordmap['lemma'].endswith('rtö'):
                    wordmap['new_paras'] = ['N_VÄRTÖ']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'K'],
                            ['rto'])
            elif wordmap['kotus_av'] == 'M':
                if wordmap['lemma'].endswith('uku'):
                    wordmap['new_paras'] = ['N_LUKU']
                elif wordmap['lemma'].endswith('yky'):
                    wordmap['new_paras'] = ['N_KYKY']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'M'],
                            ['uku', 'yky'])
            else:
                fail_guess_because(wordmap, ['N', 1], ['A–K', 'M'])
        elif tn == 2:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('o'):
                    wordmap['new_paras'] = ['N_RUIPELO']
                elif wordmap['lemma'].endswith('u'):
                    wordmap['new_paras'] = ['N_SEIKKAILU']
                elif wordmap['lemma'].endswith('y'):
                    wordmap['new_paras'] = ['N_VEHKEILY']
                elif wordmap['lemma'].endswith('ö'):
                    wordmap['new_paras'] = ['N_JÄÄTELÖ']
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_EUGENE']
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SELENE']
                else:
                    fail_guess_because(wordmap, ['N', 2, False],
                            ['o', 'u', 'y', 'ö', 'e'])
            else:
                fail_guess_because(wordmap, ['N', 2], [False])
        elif tn == 3:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ao'):
                    wordmap['new_paras'] = ['N_TUOMIO']
                elif wordmap['lemma'].endswith('ão'):
                    wordmap['new_paras'] = ['N_TUOMIO']
                elif wordmap['lemma'].endswith('ae'):
                    wordmap['new_paras'] = ['N_ZOMBIE']
                elif wordmap['lemma'].endswith('eo'):
                    wordmap['new_paras'] = ['N_TUOMIO']
                elif wordmap['lemma'].endswith('io'):
                    wordmap['new_paras'] = ['N_TUOMIO']
                elif wordmap['lemma'].endswith('iö'):
                    wordmap['new_paras'] = ['N_HÄIRIÖ']
                elif wordmap['lemma'].endswith('ie') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ZOMBIE']
                elif wordmap['lemma'].endswith('ie') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_BERNIE']
                elif wordmap['lemma'].endswith('ye') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_BERNIE']
                elif wordmap['lemma'].endswith('oe'):
                    wordmap['new_paras'] = ['N_ZOMBIE']
                elif wordmap['lemma'].endswith('ue'):
                    wordmap['new_paras'] = ['N_ZOMBIE']
                elif wordmap['lemma'].endswith('yo'):
                    wordmap['new_paras'] = ['N_TUOMIO']
                elif wordmap['lemma'].endswith('kolme'):
                    wordmap['new_paras'] = ['N_AAMUKOLME']
                else:
                    fail_guess_because(wordmap, ['N', 3, False],
                            ['ae', 'ao ão', 'eo', 'io', 'ie', 'iö', 'oe', 'ue', '*yo ye'])
            else:
                fail_guess_because(wordmap, ['N', 3], [False])
        elif tn == 4:
            if wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kko'):
                    wordmap['new_paras'] = ['N_LEPAKKO']
                elif wordmap['lemma'].endswith('kkö'):
                    wordmap['new_paras'] = ['N_YKSIKKÖ']
                else:
                    fail_guess_because(wordmap, ['N', 4, 'A'],
                            ['kko', 'kkö'])
            else:
                fail_guess_because(wordmap, ['N', 4], ['A'])
        elif tn == 5:
            if not wordmap['lemma'].endswith('i'):
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_PUNK']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_ZEN']
                else:
                    fail_guess_because(wordmap, ['N', 5, False, '!i'], 
                            ['front', 'back'])
            elif not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_RUUVI']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_TYYLI']
                else:
                    fail_guess_because(wordmap, ['N', 5, False, 'i'],
                            ['front', 'back'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LOKKI']
                elif wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HÄKKI']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'A'],
                            ['ki', 'front', 'back'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppi') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KUPPI']
                elif wordmap['lemma'].endswith('ppi') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_TYYPPI']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'B'],
                            ['ppi', 'front', 'back'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tti') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KORTTI']
                elif wordmap['lemma'].endswith('tti') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SKEITTI']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'C'],
                            ['tti', 'front', 'back'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LAKI']
                elif wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HÄKKI']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'D'],
                            ['ki', 'front', 'back'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('pi') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_HUPI']
                elif wordmap['lemma'].endswith('pi') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_RIIPI']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'E'],
                            ['pi', 'back', 'front'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_TAUTI']
                elif wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_NIHTI']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'F'],
                            ['ti', 'front', 'back'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nki') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_VANKI']
                elif wordmap['lemma'].endswith('nki') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HÄMMINKI']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'F'],
                            ['nki', 'front', 'back'])
            elif wordmap['kotus_av'] == 'H':
                # obs! lampi och rimpi kan vara 5 eller 7
                if wordmap['lemma'].endswith('mpi') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LAMMI']
                elif wordmap['lemma'].endswith('mpi') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_RIMMI']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'H'],
                            ['mpi', 'front', 'back'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('lti') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_PELTI']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'I'],
                            ['lti', 'back'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nti') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_SOINTI']
                elif wordmap['lemma'].endswith('nti') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_VIENTI']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'J'],
                            ['nti', 'front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 5],
                        ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'J'])
        elif tn == 6:
            if not wordmap['lemma'].endswith('i'):
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_STADION']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_BESSERWISSER']
                else:
                    fail_guess_because(wordmap, ['N', 6, False, '!i'],
                            ['front', 'back'])
            elif not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KANAALI']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KEHVELI']
                else:
                    fail_guess_because(wordmap, ['N', 6, False, 'i'],
                            ['front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 6],
                        [False])
        elif tn == 7:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ONNI']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KIVI']
                else:
                    fail_guess_because(wordmap, ['N', 7, False],
                            ['front', 'back'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppi') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_HAPPI']
                elif wordmap['lemma'].endswith('ppi') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_TYPPI']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'B'],
                            ['ppi', 'front', 'back'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_NOKI']
                elif wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KÄKI']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'D'],
                            ['ki', 'front', 'back'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('pi') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KORPI']
                elif wordmap['lemma'].endswith('pi') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KILPI']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'E'],
                            ['pi', 'front', 'back'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LAHTI']
                elif wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_LEHTI']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'F'],
                            ['hti', 'front', 'back'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nki') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ONKI']
                elif wordmap['lemma'].endswith('nki') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HENKI']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'G'],
                            ['nki', 'front', 'back'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mpi') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_SAMPI']
                elif wordmap['lemma'].endswith('mpi') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_RIMPI']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'H'],
                            ['mpi', 'front', 'back'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ARKI']
                elif wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_JÄRKI']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'H'],
                            ['ki', 'front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 7],
                        [False, 'B', 'D', 'E', 'G', 'H'])
        elif tn == 8:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_NALLE']
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_NISSE']
                elif wordmap['lemma'].endswith('E') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_NALLE']
                elif wordmap['lemma'].endswith('E') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_NISSE']
                elif wordmap['lemma'].endswith('ë') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_NALLE']
                elif wordmap['lemma'].endswith('ě') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_NALLE']
                elif wordmap['lemma'].endswith('ě') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_NISSE']
                elif wordmap['lemma'].endswith('ë') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_NISSE']
                elif wordmap['lemma'].endswith('an') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_AAMUKAHDEKSAN']
                elif wordmap['lemma'].endswith('än') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_AAMUYHDEKSÄN']
                elif wordmap['lemma'].endswith('en') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_AAMUKYMMENEN']
                else:
                    fail_guess_because(wordmap, ['N', 8, False],
                            ['e', 'ë', 'ě', 'front', 'back'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kke') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_NUKKE']
                elif wordmap['lemma'].endswith('kke') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_EKKE']
                else:
                    fail_guess_because(wordmap, ['N', 8, 'A'],
                            ['kke', 'back'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppe') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_RAPPE']
                elif wordmap['lemma'].endswith('ppe') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_JEPPE']
                else:
                    fail_guess_because(wordmap, ['N', 8, 'B'],
                            ['ppe', 'front'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tte') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LOTTE']
                elif wordmap['lemma'].endswith('tte') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_METTE']
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
                    wordmap['new_paras'] = ['N_KIRJA']
                elif wordmap['lemma'].endswith('ą'):
                    wordmap['new_paras'] = ['N_KIRJA']
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_paras'] = ['N_YMPÄRYSTÄ']
                else:
                    fail_guess_because(wordmap, ['N', 9, False],
                            ['a', 'ä'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('ka'):
                    wordmap['new_paras'] = ['N_POLITIIKKA']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'A'],
                            ['kka'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppa'):
                    wordmap['new_paras'] = ['N_TIPPA']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'B'],
                            ['ppa'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tta'):
                    wordmap['new_paras'] = ['N_MITTA']
                elif wordmap['lemma'].endswith('ttä'):
                    wordmap['new_paras'] = ['N_YRITTÄ']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'C'],
                            ['tta', 'ttä'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('aaka'):
                    wordmap['new_paras'] = ['N_VAAKA']
                elif wordmap['lemma'].endswith('ka'):
                    wordmap['new_paras'] = ['N_VIKA']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'D'],
                            ['ka'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('pa'):
                    wordmap['new_paras'] = ['N_HALPA']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'E'],
                            ['pa'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('ta'):
                    wordmap['new_paras'] = ['N_PATA']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'F'],
                            ['ta'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nka'):
                    wordmap['new_paras'] = ['N_LANKA']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'G'],
                            ['nka'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mpa'):
                    wordmap['new_paras'] = ['N_RAMPA']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'H'],
                            ['mpa'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('lta'):
                    wordmap['new_paras'] = ['N_VALTA']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'I'],
                            ['lta'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nta'):
                    wordmap['new_paras'] = ['N_KUTSUNTA']
                elif wordmap['lemma'].endswith('ntä'):
                    wordmap['new_paras'] = ['N_KYSYNTÄ']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'J'],
                            ['nta', 'ntä'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rta'):
                    wordmap['new_paras'] = ['N_KERTA']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'K'],
                            ['rta'])
            else:
                fail_guess_because(wordmap, ['N', 9],
                        [False, 'A-K'])
        elif tn == 10:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('a') or wordmap['lemma'].endswith('A'):
                    wordmap['new_paras'] = ['N_SOITTAJA']
                elif wordmap['lemma'].endswith('ą'):
                    wordmap['new_paras'] = ['N_SOITTAJA']
                elif wordmap['lemma'].endswith('ă'):
                    wordmap['new_paras'] = ['N_SOITTAJA']
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_paras'] = ['N_HÖPÖTTÄJÄ']
                elif wordmap['lemma'].endswith('an'):
                    wordmap['new_paras'] = ['N_AAMUKAHDEKSAN']
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_paras'] = ['N_AAMUYHDEKSÄN']
                else:
                    fail_guess_because(wordmap, ['N', 10, False],
                            ['a ą ă', 'ä'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('ka'):
                    wordmap['new_paras'] = ['N_LUOKKA']
                elif wordmap['lemma'].endswith('kä'):
                    wordmap['new_paras'] = ['N_HÖLKKÄ']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'A'],
                            ['kka', 'kkä'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppa'):
                    wordmap['new_paras'] = ['N_KUOPPA']
                elif wordmap['lemma'].endswith('ppä'):
                    wordmap['new_paras'] = ['N_SEPPÄ']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'B'],
                            ['ppa', 'ppä'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tta'):
                    wordmap['new_paras'] = ['N_ROTTA']
                elif wordmap['lemma'].endswith('ttä'):
                    wordmap['new_paras'] = ['N_KENTTÄ']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'C'],
                            ['tta', 'ttä'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('ka'):
                    wordmap['new_paras'] = ['N_VUOKA']
                elif wordmap['lemma'].endswith('kä'):
                    wordmap['new_paras'] = ['N_REIKÄ']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'D'],
                            ['ka', 'kä'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('pa'):
                    wordmap['new_paras'] = ['N_LUPA']
                elif wordmap['lemma'].endswith('pä'):
                    wordmap['new_paras'] = ['N_LEIPÄ']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'E'],
                            ['pa', 'pä'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('ta'):
                    wordmap['new_paras'] = ['N_SOTA']
                elif wordmap['lemma'].endswith('tä'):
                    wordmap['new_paras'] = ['N_PÖYTÄ']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'F'],
                            ['ta', 'tä'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nka'):
                    wordmap['new_paras'] = ['N_HONKA']
                elif wordmap['lemma'].endswith('nkä'):
                    wordmap['new_paras'] = ['N_KENKÄ']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'G'],
                            ['nka', 'nkä'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mpa'):
                    wordmap['new_paras'] = ['N_KOMPA']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'H'],
                            ['mpa', 'mpä'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('lta'):
                    wordmap['new_paras'] = ['N_MULTA']
                elif wordmap['lemma'].endswith('ltä'):
                    wordmap['new_paras'] = ['N_SYLTÄ']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'I'],
                            ['lta', 'ltä'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nta'):
                    wordmap['new_paras'] = ['N_KUNTA']
                elif wordmap['lemma'].endswith('ntä'):
                    wordmap['new_paras'] = ['N_EMÄNTÄ']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'J'],
                            ['nta', 'ntä'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rta'):
                    wordmap['new_paras'] = ['N_HORTA']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'K'],
                            ['rta'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('kä'):
                    wordmap['new_paras'] = ['N_SELKÄ']
                elif wordmap['lemma'].endswith('ka'):
                    wordmap['new_paras'] = ['N_OLKA']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'L'],
                            ['kä'])
            else:
                fail_guess_because(wordmap, ['N', 10],
                        [False, 'A-J', 'L'])
        elif tn == 11:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('a'):
                    wordmap['new_paras'] = ['N_PROBLEEMA']
                elif wordmap['lemma'].endswith('ă'):
                    wordmap['new_paras'] = ['N_PROBLEEMA']
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_paras'] = ['N_KÄPÄLÄ']
                else:
                    fail_guess_because(wordmap, ['N', 11, False],
                            ['a', 'ä'])
            else:
                fail_guess_because(wordmap, ['N', 11],
                        [False])
        elif tn == 12:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('a') or wordmap['lemma'].endswith('A'):
                    wordmap['new_paras'] = ['N_MAKKARA']
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_paras'] = ['N_HÄKKYRÄ']
                else:
                    fail_guess_because(wordmap, ['N', 12, False],
                            ['a', 'ä'])
            else:
                fail_guess_because(wordmap, ['N', 12],
                        [False])
        elif tn == 13:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('a'):
                    wordmap['new_paras'] = ['N_KITARA']
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_paras'] = ['N_SIIVILÄ']
                else:
                    fail_guess_because(wordmap, ['N', 13, False],
                            ['a', 'ä'])
            else:
                fail_guess_because(wordmap, ['N', 13],
                        [False])
        elif tn == 14:
            if wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kka'):
                    wordmap['new_paras'] = ['N_LUSIKKA']
                elif wordmap['lemma'].endswith('kkä'):
                    wordmap['new_paras'] = ['N_KÄMMEKKÄ']
                else:
                    fail_guess_because(wordmap, ['N', 14, 'A'],
                            ['kka', 'kkä'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppa'):
                    wordmap['new_paras'] = ['N_ULAPPA']
                else:
                    fail_guess_because(wordmap, ['N', 14, 'B'],
                            ['ppä'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tta'):
                    wordmap['new_paras'] = ['N_POHATTA']
                else:
                    fail_guess_because(wordmap, ['N', 14, 'C'],
                            ['tta'])
            else:
                fail_guess_because(wordmap, ['N', 14],
                        ['A', 'B', 'C'])
        elif tn == 15:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('oa'):
                    wordmap['new_paras'] = ['N_AINOA']
                elif wordmap['lemma'].endswith('ôa'):
                    wordmap['new_paras'] = ['N_AINOA']
                elif wordmap['lemma'].endswith('ea'):
                    wordmap['new_paras'] = ['N_SOKEA']
                elif wordmap['lemma'].endswith('eä'):
                    wordmap['new_paras'] = ['N_LIPEÄ']
                elif wordmap['lemma'].endswith('ua'):
                    wordmap['new_paras'] = ['N_TANHUA']
                else:
                    fail_guess_because(wordmap, ['N', 15, False],
                            ['oa ôa', 'ea', 'eä', 'ua'])
            else:
                fail_guess_because(wordmap, ['N', 15],
                        [False])
        elif tn == 16:
            if wordmap['kotus_av'] == 'H':
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_VANHEMPI']
                else:
                    fail_guess_because(wordmap, ['N', 16, 'H'],
                            ['back'])
            else:
                fail_guess_because(wordmap, ['N', 16],
                        ['H'])
        elif tn == 17:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aa'):
                    wordmap['new_paras'] = ['N_VAINAA']
                elif wordmap['lemma'].endswith('ee') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_TOKEE']
                elif wordmap['lemma'].endswith('ee') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_LENTTEE']
                elif wordmap['lemma'].endswith('oo'):
                    wordmap['new_paras'] = ['N_TIENOO']
                elif wordmap['lemma'].endswith('uu'):
                    wordmap['new_paras'] = ['N_LEIKKUU']
                elif wordmap['lemma'].endswith('yy'):
                    wordmap['new_paras'] = ['N_HYÖTYY']
                elif wordmap['lemma'].endswith('ää'):
                    wordmap['new_paras'] = ['N_HYVINKÄÄ']
                elif wordmap['lemma'].endswith('öö'):
                    wordmap['new_paras'] = ['N_YLÖÖ']
                else:
                    fail_guess_because(wordmap, ['N', 17, False],
                            ['aa', 'ee', 'oo', 'uu', 'yy', 'ää', 'öö'])
            else:
                fail_guess_because(wordmap, ['N', 17],
                        [False])
        elif tn == 18:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('a'):
                    wordmap['new_paras'] = ['N_MAA']
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_MATEE']
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_TEE']
                elif wordmap['lemma'].endswith('i') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_HAI']
                elif wordmap['lemma'].endswith('i') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_PII']
                elif wordmap['lemma'].endswith('o'):
                    wordmap['new_paras'] = ['N_OOKOO']
                elif wordmap['lemma'].endswith('u'):
                    wordmap['new_paras'] = ['N_PUU']
                elif wordmap['lemma'].endswith('y'):
                    wordmap['new_paras'] = ['N_PYY']
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_paras'] = ['N_PÄÄ']
                elif wordmap['lemma'].endswith('ö'):
                    wordmap['new_paras'] = ['N_KÖÖ']
                else:
                    fail_guess_because(wordmap, ['N', 18, False],
                            ['a', 'e', 'i', 'o', 'u', 'y', 'ä', 'ö', 'back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 18],
                        [False])
        elif tn == 19:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('uo'):
                    wordmap['new_paras'] = ['N_VUO']
                elif wordmap['lemma'].endswith('ie') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_TIE']
                elif wordmap['lemma'].endswith('yö'):
                    wordmap['new_paras'] = ['N_TYÖ']
                else:
                    fail_guess_because(wordmap, ['N', 19, False],
                            ['ie', 'uo', 'yö'])
            else:
                fail_guess_because(wordmap, ['N', 18],
                        [False])
        elif tn == 20:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aa'):
                    wordmap['new_paras'] = ['N_NUGAA']
                elif wordmap['lemma'].endswith('ee') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_PATEE']
                elif wordmap['lemma'].endswith('ee') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_BIDEE']
                elif wordmap['lemma'].endswith('EE') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_PATEE']
                elif wordmap['lemma'].endswith('EE') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_BIDEE']
                elif wordmap['lemma'].endswith('oo'):
                    wordmap['new_paras'] = ['N_TRIKOO']
                elif wordmap['lemma'].endswith('uu'):
                    wordmap['new_paras'] = ['N_RAGUU']
                elif wordmap['lemma'].endswith('yy'):
                    wordmap['new_paras'] = ['N_FONDYY']
                elif wordmap['lemma'].endswith('öö'):
                    wordmap['new_paras'] = ['N_MILJÖÖ']
                else:
                    fail_guess_because(wordmap, ['N', 20, False],
                            ['aa', 'ee', 'oo', 'uu', 'yy', 'öö'])
            else:
                fail_guess_because(wordmap, ['N', 20],
                        [False])
        elif tn == 21:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('gay'):
                    wordmap['new_paras'] = ['N_GAY']
                elif wordmap['lemma'].endswith('ie') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_BRASSERIE']
                elif wordmap['lemma'].endswith('è') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ROSÉ']
                elif wordmap['lemma'].endswith('é') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ROSÉ']
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ROSÉ']
                elif wordmap['lemma'].endswith('é') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_BÉBÉ']
                elif wordmap['lemma'].endswith('ci'):
                    wordmap['new_paras'] = ['N_GAY']
                elif wordmap['lemma'].endswith('oí'):
                    wordmap['new_paras'] = ['N_GAY']
                elif wordmap['lemma'].endswith('fu'):
                    wordmap['new_paras'] = ['N_KUNGFU']
                elif wordmap['lemma'].endswith('au'):
                    wordmap['new_paras'] = ['N_KUNGFU']
                elif wordmap['lemma'].endswith('ou'):
                    wordmap['new_paras'] = ['N_KUNGFU']
                elif wordmap['lemma'].endswith('ao'):
                    wordmap['new_paras'] = ['N_KUNGFU']
                elif wordmap['lemma'].endswith('ho'):
                    wordmap['new_paras'] = ['N_KUNGFU']
                else:
                    #fail_guess_because(wordmap, ['N', 21, False],
                    #        ['gay', 'eéè'], "guessing 21 is not possible"
                    #        "Using #")
                    wordmap['new_paras'] = ['#']
            else:
                fail_guess_because(wordmap, ['N', 21],
                        [False])
        elif tn == 22:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ait'):
                    wordmap['new_paras'] = ['N_PARFAIT']
                elif wordmap['lemma'].endswith('ow'):
                    wordmap['new_paras'] = ['N_SHOW']
                elif wordmap['lemma'].endswith('ough'):
                    wordmap['new_paras'] = ['N_SHOW']
                elif wordmap['lemma'].endswith('et'):
                    wordmap['new_paras'] = ['N_BEIGNET']
                else:
                    #fail_guess_because(wordmap, ['N', 22, False],
                    #        ['ait', 'ow'], "guessing 22 is not possible"
                    #        "Using #")
                    wordmap['new_paras'] = ['#']
            else:
                fail_guess_because(wordmap, ['N', 22],
                        [False])
        elif tn == 23:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_TULI']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SYLI']
                else:
                    fail_guess_because(wordmap, ['N', 23, False],
                            ['back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 23],
                        [False])
        elif tn in [24, 26]:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_RUUHI']
                elif wordmap['harmony'] == 'front' and wordmap['lemma'].endswith('meri'):
                    wordmap['new_paras'] = ['N_MERI']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HIIRI']
                else:
                    fail_guess_because(wordmap, ['N', 24, 26, False],
                            ['back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 24, 26],
                        [False])
        elif tn == 25:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_TAIMI']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_LIEMI']
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
                        wordmap['new_paras'] = ['N_KAUSI']
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_paras'] = ['N_KÖYSI']
                    else:
                        fail_guess_because(wordmap, ['N', 27, False, 'si'],
                                ['back', 'front'])
                else:
                    fail_guess_because(wordmap, ['N', 25, False],
                            ['s'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('si'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_paras'] = ['N_KAUSI']
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_paras'] = ['N_KÖYSI']
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
                        wordmap['new_paras'] = ['N_PONSI']
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_paras'] = ['N_LÄNSI']
                    else:
                        fail_guess_because(wordmap, ['N', 28, 'F', 'nsi'],
                                ['back', 'front'])
                elif wordmap['lemma'].endswith('rsi'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_paras'] = ['N_VARSI']
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_paras'] = ['N_VIRSI']
                    else:
                        fail_guess_because(wordmap, ['N', 28, 'F', 'rsi'],
                                ['back', 'front'])
                elif wordmap['lemma'].endswith('lsi'):
                    if wordmap['harmony'] == 'front':
                        wordmap['new_paras'] = ['N_JÄLSI']
                    else:
                        fail_guess_because(wordmap, ['N', 28, 'F', 'lsi'],
                                ['front'])
                else:
                    fail_guess_because(wordmap, ['N', 28, False],
                            ['nsi', 'rsi', 'lsi'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nsi'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_paras'] = ['N_PONSI']
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_paras'] = ['N_LÄNSI']
                    else:
                        fail_guess_because(wordmap, ['N', 28, 'J', 'nsi'],
                            ['back', 'front'])
                else:
                    fail_guess_because(wordmap, ['N', 28, 'J'],
                            ['nsi'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rsi'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_paras'] = ['N_VARSI']
                    elif wordmap['harmony'] == 'front':
                        wordmap['new_paras'] = ['N_VIRSI']
                    else:
                        fail_guess_because(wordmap, ['N', 28, 'K', 'rsi'],
                            ['back', 'front'])
                else:
                    fail_guess_because(wordmap, ['N', 28, 'K'],
                            ['rsi'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('lsi'):
                    if wordmap['harmony'] == 'front':
                        wordmap['new_paras'] = ['N_JÄLSI']
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
                        wordmap['new_paras'] = ['N_LAPSI']
                    else:
                        fail_guess_because(wordmap, ['N', 29, False, 'psi'],
                            ['back'])
                elif wordmap['lemma'].endswith('ksi'):
                    if wordmap['harmony'] == 'back':
                        wordmap['new_paras'] = ['N_UKSI']
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
                        wordmap['new_paras'] = ['N_VEITSI']
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
                        wordmap['new_paras'] = ['N_HAAKSI']
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
                    wordmap['new_paras'] = ['N_JOUTSEN']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SIEMEN']
                else:
                    fail_guess_because(wordmap, ['N', 32, False],
                        ['back', 'front'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_AJATAR']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_TYTÄR']
                else:
                    fail_guess_because(wordmap, ['N', 32, 'C'],
                        ['back', 'front'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_IEN']
                else:
                    fail_guess_because(wordmap, ['N', 32, 'D'],
                        ['back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 32],
                    [False, 'C', 'D'])
        elif tn == 33:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_PUHELIN']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_ELIN']
                else:
                    fail_guess_because(wordmap, ['N', 33, False],
                        ['back', 'front'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kin') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HÄRKIN']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'A'],
                        ['kin', 'front'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tin') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_SUODATIN']
                elif wordmap['lemma'].endswith('tin') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HEITIN']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'C'],
                        ['tin', 'back', 'front'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('in') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_PUIN']
                elif wordmap['lemma'].endswith('in') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_PYYHIN']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'D'],
                        ['in', 'back', 'front'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('vin') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_RAAVIN']
                elif wordmap['lemma'].endswith('vin') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SÄRVIN']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'E'],
                        ['vin', 'back', 'front'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('din') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_VAADIN']
                elif wordmap['lemma'].endswith('din') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SÄÄDIN']
                elif wordmap['lemma'].endswith('don'):
                    wordmap['new_paras'] = ['N_JÄRVITAHDON']
                elif wordmap['lemma'].endswith('dun'):
                    wordmap['new_paras'] = ['N_LAIDUN']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'F'],
                        ['din', 'dun', 'back', 'front'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('llin') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ASKELLIN']
                elif wordmap['lemma'].endswith('llin') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SIVELLIN']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'I'],
                        ['llin', 'back', 'front'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnin') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_MUUNNIN']
                elif wordmap['lemma'].endswith('in') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KÄÄNNIN']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'J'],
                        ['nnin', 'back', 'front'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rrin') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KIHARRIN']
                elif wordmap['lemma'].endswith('rrin') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KIERRIN']
                elif wordmap['lemma'].endswith('rroin'):
                    wordmap['new_paras'] = ['N_KERROIN']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'K'],
                        ['rrin', 'rroin', 'back', 'front'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('jin') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_POLJIN']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'J'],
                        ['jin', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 33],
                    [False, 'A', 'C-F', 'J-L'])
        elif wordmap['kotus_tn'] == 34:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('toin'):
                    wordmap['new_paras'] = ['N_KALATOIN']
                elif wordmap['lemma'].endswith('töin'):
                    wordmap['new_paras'] = ['N_NIMETÖIN']
                else:
                    fail_guess_because(wordmap, ['N', 34, False],
                            ['toin', 'töin'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pan'):
                    wordmap['new_paras'] = ['N_HAPAN']
                else:
                    fail_guess_because(wordmap, ['N', 34, 'B'],
                            ['pan'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('ton'):
                    wordmap['new_paras'] = ['N_OSATON']
                elif wordmap['lemma'].endswith('tön'):
                    wordmap['new_paras'] = ['N_NIMETÖN']
                else:
                    fail_guess_because(wordmap, ['N', 34, 'C'],
                            ['ton', 'tön'])
            else:
                fail_guess_because(wordmap, ['N', 34], [False, 'C'])
        elif wordmap['kotus_tn'] == 35:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_AAMUKAKSI']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_AAMUYKSI']
                else:
                    fail_guess_because(wordmap, ['N', 35, False],
                        ['back', 'front'])
            else:
                fail_guess_because(wordmap, ['N', 35],
                    [False, 'C-F', 'J-L'])
        elif wordmap['kotus_tn'] == 36:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KYLÄNVANHIN']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_LÄHIN']
                else:
                    fail_guess_because(wordmap, ['N', 36, 'J'],
                        ['jin', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 36],
                    [False], "cannot have gradation")
        elif wordmap['kotus_tn'] == 37:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('vasen'):
                    wordmap['new_paras'] = ['N_VASEN']
                else:
                    fail_guess_because(wordmap, ['N', 37, False],
                        ['vasen'])
            else:
                fail_guess_because(wordmap, ['N', 37],
                    [False], "cannot have gradation")
        elif wordmap['kotus_tn'] == 38:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_AAKKOSTAMINEN']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KYLKIÄINEN']
                else:
                    fail_guess_because(wordmap, ['N', 38, False],
                        ['front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 38],
                    [False], "cannot have gradation")
        elif wordmap['kotus_tn'] == 39:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_VAKUUTUS']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_RÄJÄYTYS']
                else:
                    fail_guess_because(wordmap, ['N', 39, False],
                        ['front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 39],
                    [False], "cannot have gradation")
        elif wordmap['kotus_tn'] == 40:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_AAKKOSELLISUUS']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KÖYHYYS']
                else:
                    fail_guess_because(wordmap, ['N', 38, False],
                        ['front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 38],
                    [False], "cannot have gradation")
        elif wordmap['kotus_tn'] == 41:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('as'):
                    wordmap['new_paras'] = ['N_PATSAS']
                elif wordmap['lemma'].endswith('es') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ARISTOTELES']
                elif wordmap['lemma'].endswith('es') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KIRVES']
                elif wordmap['lemma'].endswith('is') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_RUUMIS']
                elif wordmap['lemma'].endswith('is') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_TIIVIS']
                elif wordmap['lemma'].endswith('os'):
                    wordmap['new_paras'] = ['N_UROS']
                elif wordmap['lemma'].endswith('äs'):
                    wordmap['new_paras'] = ['N_ÄYRÄS']
                else:
                    fail_guess_because(wordmap, ['N', 41, False],
                        ['as', 'es', 'is', 'os', 'äs', 'front', 'back'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kas'):
                    wordmap['new_paras'] = ['N_ASUKAS']
                elif wordmap['lemma'].endswith('käs'):
                    wordmap['new_paras'] = ['N_KÄRSÄKÄS']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'A'],
                        ['kas', 'käs'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pas'):
                    wordmap['new_paras'] = ['N_SAAPAS']
                elif wordmap['lemma'].endswith('päs'):
                    wordmap['new_paras'] = ['N_RYPÄS']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'B'],
                        ['pas', 'päs'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tas'):
                    wordmap['new_paras'] = ['N_RATAS']
                elif wordmap['lemma'].endswith('tes') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KORTES']
                elif wordmap['lemma'].endswith('tis') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ALTIS']
                elif wordmap['lemma'].endswith('tis') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KELTIS']
                elif wordmap['lemma'].endswith('täs'):
                    wordmap['new_paras'] = ['N_MÄTÄS']
                elif wordmap['lemma'].endswith('tus'):
                    wordmap['new_paras'] = ['N_VANTUS']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'C'],
                        ['tas', 'tis', 'tus', 'täs', 'front'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('as'):
                    wordmap['new_paras'] = ['N_VARAS']
                elif wordmap['lemma'].endswith('es') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_IES']
                elif wordmap['lemma'].endswith('is') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_RUIS']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'D'],
                        ['as', 'es', 'is', 'front', 'back'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('vas'):
                    wordmap['new_paras'] = ['N_VARVAS']
                elif wordmap['lemma'].endswith('väs'):
                    wordmap['new_paras'] = ['N_SEIVÄS']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'E'],
                        ['vas', 'väs'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('das'):
                    wordmap['new_paras'] = ['N_TEHDAS']
                elif wordmap['lemma'].endswith('des') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LUODES']
                elif wordmap['lemma'].endswith('des') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_LÄHDES']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'F'],
                        ['das', 'des'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('ngas'):
                    wordmap['new_paras'] = ['N_KANGAS']
                elif wordmap['lemma'].endswith('ngäs'):
                    wordmap['new_paras'] = ['N_KÖNGÄS']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'G'],
                        ['gas', 'gäs'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmas'):
                    wordmap['new_paras'] = ['N_HAMMAS']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'H'],
                        ['mmas'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('llas'):
                    wordmap['new_paras'] = ['N_ALLAS']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'I'],
                        ['llas', 'lles', 'back'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnas'):
                    wordmap['new_paras'] = ['N_KINNAS']
                elif wordmap['lemma'].endswith('nnäs'):
                    wordmap['new_paras'] = ['N_RYNNÄS']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'J'],
                        ['nnas', 'nnäs'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('ras'):
                    wordmap['new_paras'] = ['N_PORRAS']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'K'],
                        ['rras'])
            else:
                fail_guess_because(wordmap, ['N', 41],
                    [False, 'A-K'])
        elif wordmap['kotus_tn'] == 42:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('mies') or wordmap['lemma'].endswith('Mies'):
                    wordmap['new_paras'] = ['N_MIES']
                else:
                    fail_guess_because(wordmap, ['N', 42, False],
                        ['mies'])
            else:
                fail_guess_because(wordmap, ['N', 42],
                    [False], "cannot gradate")
        elif wordmap['kotus_tn'] == 43:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ut'):
                    wordmap['new_paras'] = ['N_OLUT']
                elif wordmap['lemma'].endswith('yt'):
                    wordmap['new_paras'] = ['N_NEITSYT']
                else:
                    fail_guess_because(wordmap, ['N', 43, False],
                        ['ut', 'yt'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmyt'):
                    wordmap['new_paras'] = ['N_IMMYT']
                else:
                    fail_guess_because(wordmap, ['N', 43, 'H'],
                        ['mmyt'])
            else:
                fail_guess_because(wordmap, ['N', 43],
                    [False, 'H'])
        elif wordmap['kotus_tn'] == 44:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ät'):
                    wordmap['new_paras'] = ['N_KEVÄT']
                elif wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KAARET']
                elif wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HÄMET']
                else:
                    fail_guess_because(wordmap, ['N', 44, False],
                        ['ät','et'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KORTET']
                else:
                    fail_guess_because(wordmap, ['N', 44, 'C'],
                            ['tet'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LOUET']
                else:
                    fail_guess_because(wordmap, ['N', 44, 'D'],
                            ['et'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('det') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_AHDET']
                elif wordmap['lemma'].endswith('det') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_LÄHDET']
                else:
                    fail_guess_because(wordmap, ['N', 44, 'F'],
                            ['det'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('get') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_INGET']
                else:
                    fail_guess_because(wordmap, ['N', 44, 'F'],
                            ['det'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('llet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_VUOLLET']
                else:
                    fail_guess_because(wordmap, ['N', 44, 'I'],
                            ['llet'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LANNET']
                elif wordmap['lemma'].endswith('nnet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_RINNET']
                else:
                    fail_guess_because(wordmap, ['N', 44, 'J'],
                            ['nnet'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rret') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KAARRET']
                elif wordmap['lemma'].endswith('rret') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_VIIRRET']
                else:
                    fail_guess_because(wordmap, ['N', 44, 'K'],
                            ['rret'])
            else:
                fail_guess_because(wordmap, ['N', 44],
                    [False, 'C', 'D', 'F', 'G', 'I', 'J', 'K'])
        elif wordmap['kotus_tn'] == 45:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('s'):
                    wordmap['new_paras'] = ['N_TUHANNES']
                else:
                    fail_guess_because(wordmap, ['N', 45, False],
                        ['s'])
            else:
                fail_guess_because(wordmap, ['N', 45],
                    [False], "cannot gradate")
        elif wordmap['kotus_tn'] == 46:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('tuhat'):
                    wordmap['new_paras'] = ['N_VUOSITUHAT']
                else:
                    fail_guess_because(wordmap, ['N', 46, False],
                        ['tuhat'])
            else:
                fail_guess_because(wordmap, ['N', 46],
                    [False], "cannot gradate")
        elif wordmap['kotus_tn'] == 47:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ut'):
                    wordmap['new_paras'] = ['N_AIVOKUOLLUT']
                elif wordmap['lemma'].endswith('yt'):
                    wordmap['new_paras'] = ['N_SIVISTYNYT']
                else:
                    fail_guess_because(wordmap, ['N', 47, False],
                        ['yt'])
            else:
                fail_guess_because(wordmap, ['N', 46],
                    [False], "cannot gradate")
        elif tn == 48:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ASTE']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_PISTE']
                else:
                    fail_guess_because(wordmap, ['N', 48, False],
                        ['front', 'back'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('ke') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KASTIKE']
                elif wordmap['lemma'].endswith('ke') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_LÄÄKE']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'A'],
                        ['ke', 'front', 'back'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pe') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_APE']
                elif wordmap['lemma'].endswith('pe') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_RIPE']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'B'],
                        ['pe', 'front', 'back'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('te') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_OSOITE']
                elif wordmap['lemma'].endswith('te') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KÄSITE']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'C'],
                        ['te', 'front', 'back'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KOE']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_PYYHE']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'D'],
                        ['e', 'front', 'back'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('ve') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_TARVE']
                elif wordmap['lemma'].endswith('ve') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_VIIVE']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'E'],
                        ['ve', 'front', 'back'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('de') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LUODE']
                elif wordmap['lemma'].endswith('de') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KIDE']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'F'],
                        ['de', 'front', 'back'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mme') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LUMME']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'H'],
                        ['mme', 'back'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('lle') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_VUOLLE']
                elif wordmap['lemma'].endswith('lle') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_MIELLE']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'I'],
                        ['lle', 'front', 'back'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nne') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_RAKENNE']
                elif wordmap['lemma'].endswith('nne') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KIINNE']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'J'],
                        ['nne', 'front', 'back'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rre') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_AARRE']
                elif wordmap['lemma'].endswith('rre') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KIERRE']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'K'],
                        ['rre', 'front', 'back'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('je') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_POHJE']
                elif wordmap['lemma'].endswith('je') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HYLJE']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'L'],
                        ['je', 'front', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 48],
                    [False, 'A-F', 'H-L'])
        elif tn == 49:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('al'):
                    wordmap['new_paras'] = ['N_ASKAR']
                elif wordmap['lemma'].endswith('ar'):
                    wordmap['new_paras'] = ['N_ASKAR']
                elif wordmap['lemma'].endswith('en') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ASKAR']
                elif wordmap['lemma'].endswith('el') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ASKAR']
                elif wordmap['lemma'].endswith('el') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KYYNEL']
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ASTE']
                elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_PISTE']
                else:
                    fail_guess_because(wordmap, ['N', 49, False],
                        ['al ar', 'el en', 'e', 'front', 'back'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('en') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SÄEN']
                else:
                    fail_guess_because(wordmap, ['N', 49, 'D'],
                        ['en', 'front'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('val'):
                    wordmap['new_paras'] = ['N_TAIVAL']
                else:
                    fail_guess_because(wordmap, ['N', 49, 'E'],
                        ['al', 'front'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('dar'):
                    wordmap['new_paras'] = ['N_UDAR']
                else:
                    fail_guess_because(wordmap, ['N', 49, 'F'],
                        ['dar'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nger') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_PENGER']
                else:
                    fail_guess_because(wordmap, ['N', 49, 'G'],
                        ['ger', 'front'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmel') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_OMMEL']
                elif wordmap['lemma'].endswith('mmel') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_VEMMEL']
                elif wordmap['lemma'].endswith('mmol'):
                    wordmap['new_paras'] = ['N_LOMMOL']
                else:
                    fail_guess_because(wordmap, ['N', 49, 'H'],
                        ['mmel', 'mmol', 'front', 'back'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnar'):
                    wordmap['new_paras'] = ['N_PIENNAR']
                elif wordmap['lemma'].endswith('nnel') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KANNEL']
                elif wordmap['lemma'].endswith('nner') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_MANNER']
                elif wordmap['lemma'].endswith('nner') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KINNER']
                else:
                    fail_guess_because(wordmap, ['N', 49, 'J'],
                        ['nnar', 'nnel', 'nner', 'front'])
            elif wordmap['kotus_av'] == 'T':
                if wordmap['lemma'].endswith('auer'):
                    wordmap['new_paras'] = ['N_AUER']
                else:
                    fail_guess_because(wordmap, ['N', 49, 'T'],
                        ['auer'])
            else:
                fail_guess_because(wordmap, ['N', 49],
                    [False, 'D-H', 'J', 'T'])
        elif tn == 99:
            wordmap['new_paras'] = ['#']
        elif tn == 1007:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('veli') or wordmap['lemma'].endswith('Veli'):
                    wordmap['new_paras'] = ['N_VELI']
                else:
                    fail_guess_because(wordmap, ['N', 7, False, 'VELI'],
                            ['veli'], 'must be veli')
            else:
                fail_guess_because(wordmap, ['N', 7, 'VELI'],
                        [False], 'Cannot gradate')
        elif tn == 1009:
            if wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('aika') or wordmap['lemma'].endswith('Aika'):
                    wordmap['new_paras'] = ['N_AIKA']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'D', 'AIKA'],
                            ['aika'], 'must be aika')
            elif not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aika') or wordmap['lemma'].endswith('Aika'):
                    print("N_AIKA is k:0 gradation + i:j variation!",
                            "in", wordmap['lemma'],
                            file=stderr)
                    wordmap['new_paras'] = ['N_AIKA']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'D', 'AIKA'],
                            ['aika'], 'must be aika')
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('aika'):
                    wordmap['new_paras'] = ['N_AIKA']
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
                    wordmap['new_paras'] = ['N_POIKA']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'D', 'POIKA'],
                            ['poika'], 'must be poika')
            elif not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('poika'):
                    print("N_POIKA is k:0 gradation + i:j variation!",
                            "in", wordmap['lemma'],
                            file=stderr)
                    wordmap['new_paras'] = ['N_POIKA']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'D', 'POIKA'],
                            ['poika'], 'must be poika')
            else:
                fail_guess_because(wordmap, ['N', 10, 'POIKA'],
                        ['D'], 'must be D')
        elif tn == 1024:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('meri') or wordmap['lemma'].endswith('Meri'):
                    wordmap['new_paras'] = ['N_MERI']
                else:
                    fail_guess_because(wordmap, ['N', 24, False, 'MERI'],
                            ['meri'], 'must be meri')
            else:
                fail_guess_because(wordmap, ['N', 24, 'MERI'],
                        [False], 'must be 0')
        elif tn == 1026:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('veri') or wordmap['lemma'].endswith('Veri'):
                    wordmap['new_paras'] = ['N_VERI']
                else:
                    fail_guess_because(wordmap, ['N', 24, 'False', 'VERI'],
                            ['poika'], 'must be poika')
            else:
                fail_guess_because(wordmap, ['N', 26, 'VERI'],
                        [False], 'must be 0')
        else:
            fail_guess_because(wordmap, ['N'],
                ['1-49', '99', '1009-1010'])
    else:
        if not wordmap['lemma'].endswith('t'):
            #fail_guess_because(wordmap, ['N', 'PLT'],
            #        ['t'], 'not a plt lemma')
            pass
        elif tn == 1:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ot'):
                    wordmap['new_paras'] = ['N_AIVOT']
                elif wordmap['lemma'].endswith('yt'):
                    wordmap['new_paras'] = ['N_PÖKSYT']
                elif wordmap['lemma'].endswith('ut'):
                    wordmap['new_paras'] = ['N_HOUSUT']
                elif wordmap['lemma'].endswith('öt'):
                    wordmap['new_paras'] = ['N_PÖLLÖT']
                else:
                    fail_guess_because(wordmap, ['N', 1, False, 'PLT'],
                            ['ot', 'ut', 'yt'])
            elif wordmap['kotus_av'] in ['A', 'D']:
                if wordmap['lemma'].endswith('ot'):
                    wordmap['new_paras'] = ['N_JOUKOT']
                elif wordmap['lemma'].endswith('ut'):
                    wordmap['new_paras'] = ['N_FARKUT']
                elif wordmap['lemma'].endswith('yt'):
                    wordmap['new_paras'] = ['N_JYLKYT']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'A', 'PLT'],
                            ['kot', 'kut', 'kyt'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('put'):
                    wordmap['new_paras'] = ['N_RAPUT']
                elif wordmap['lemma'].endswith('pot'):
                    wordmap['new_paras'] = ['N_PEIPOT']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'B', 'PLT'],
                            ['put'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tyt'):
                    wordmap['new_paras'] = ['N_NIITYT']
                elif wordmap['lemma'].endswith('tut'):
                    wordmap['new_paras'] = ['N_NIITUT']
                elif wordmap['lemma'].endswith('tot'):
                    wordmap['new_paras'] = ['N_ROITOT']
                elif wordmap['lemma'].endswith('töt'):
                    wordmap['new_paras'] = ['N_TYTÖT']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'C', 'PLT'],
                            ['tyt', 'tut', 'töt'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('vut'):
                    wordmap['new_paras'] = ['N_RAVUT']
                elif wordmap['lemma'].endswith('vot'):
                    wordmap['new_paras'] = ['N_KOUVOT']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'E', 'PLT'],
                            ['vut'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('dot'):
                    wordmap['new_paras'] = ['N_PIDOT']
                elif wordmap['lemma'].endswith('dyt'):
                    wordmap['new_paras'] = ['N_KÄÄDYT']
                elif wordmap['lemma'].endswith('döt'):
                    wordmap['new_paras'] = ['N_KYDÖT']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'F', 'PLT'],
                            ['dot', 'dyt'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('got'):
                    wordmap['new_paras'] = ['N_LINGOT']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'F', 'PLT'],
                            ['dot', 'dyt'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmut'):
                    wordmap['new_paras'] = ['N_KUMMUT']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'H', 'PLT'],
                            ['mmut'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('llot'):
                    wordmap['new_paras'] = ['N_AALLOT']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'I', 'PLT'],
                            ['llot'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnot'):
                    wordmap['new_paras'] = ['N_OPINNOT']
                elif wordmap['lemma'].endswith('nnyt'):
                    wordmap['new_paras'] = ['N_MÄNNYT']
                elif wordmap['lemma'].endswith('nnöt'):
                    wordmap['new_paras'] = ['N_SÄÄNNÖT']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'J', 'PLT'],
                            ['nnot', 'nnöt'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rrot'):
                    wordmap['new_paras'] = ['N_KAARROT']
                else:
                    fail_guess_because(wordmap, ['N', 1, 'K', 'PLT'],
                            ['rrot'])
            else:
                fail_guess_because(wordmap, ['N', 1, 'PLT'],
                        [False, 'A-F', 'I', 'J'])
        elif tn == 2:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ot'):
                    wordmap['new_paras'] = ['N_PIPPALOT']
                elif wordmap['lemma'].endswith('ut'):
                    wordmap['new_paras'] = ['N_NEUVOTTELUT']
                elif wordmap['lemma'].endswith('öt'):
                    wordmap['new_paras'] = ['N_JÄRJESTÖT']
                else:
                    fail_guess_because(wordmap, ['N', 2, False, 'PLT'],
                            ['ot', 'ut', 'öt'])
            else:
                fail_guess_because(wordmap, ['N', 2, 'PLT'],
                        [False])
        elif tn == 3:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('ot'):
                    wordmap['new_paras'] = ['N_RAUNIOT']
                elif wordmap['lemma'].endswith('öt'):
                    wordmap['new_paras'] = ['N_YHTIÖT']
                else:
                    fail_guess_because(wordmap, ['N', 3, False, 'PLT'],
                            ['ot', 'öt'])
            else:
                fail_guess_because(wordmap, ['N', 3, 'PLT'],
                        [False])
        elif tn == 4:
            if wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('öt'):
                    wordmap['new_paras'] = ['N_TÖLPÄKÖT']
                elif wordmap['lemma'].endswith('ot'):
                    wordmap['new_paras'] = ['N_LUOLIKOT']
                else:
                    fail_guess_because(wordmap, ['N', 4, 'A', 'PLT'],
                            ['ot'])
            else:
                fail_guess_because(wordmap, ['N', 4, 'PLT'],
                        [False])
        elif tn == 5:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('it') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LASIT']
                elif wordmap['lemma'].endswith('it') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_LIIVIT']
                else:
                    fail_guess_because(wordmap, ['N', 5, False, 'PLT'],
                            ['it', 'back'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kit') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_PANKIT']
                elif wordmap['lemma'].endswith('kit') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_FÄNRIKIT']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'A', 'PLT'],
                            ['kit', 'back'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pit') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KLUMPIT']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'C', 'PLT'],
                            ['pit', 'back'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tit') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KASTANJETIT']
                elif wordmap['lemma'].endswith('tit') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_PINSETIT']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'C', 'PLT'],
                            ['tit', 'back'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('dit') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_TAUDIT']
                elif wordmap['lemma'].endswith('dit') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_PIHDIT']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'F', 'PLT'],
                            ['dit'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('ngit') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_TONGIT']
                elif wordmap['lemma'].endswith('ngit') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SYÖMINGIT']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'G', 'PLT'],
                            ['ngit', 'back'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmit') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LAMMIT']
                elif wordmap['lemma'].endswith('mmit') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_RIMMIT']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'H', 'PLT'],
                            ['mmit', 'back'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnit') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_TUNNIT']
                else:
                    fail_guess_because(wordmap, ['N', 5, 'J', 'PLT'],
                            ['nnit', 'back'])
            else:
                fail_guess_because(wordmap, ['N', 5, 'PLT'],
                        [False, 'C', 'F', 'G', 'J'])
        elif tn == 6:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_FARMARIT']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_BIKINIT']
                else:
                    fail_guess_because(wordmap, ['N', 6, False, 'PLT'],
                            ['back'])
            else:
                fail_guess_because(wordmap, ['N', 6, 'PLT'],
                        [False])
        elif tn == 7:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_SAKSET']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_RIPSET']
                else:
                    fail_guess_because(wordmap, ['N', 7, False, 'PLT'],
                            ['front', 'back'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LAET']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_MÄET']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'D', 'PLT'],
                            ['front'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KORVET']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_RIIVET']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'E', 'PLT'],
                            ['front'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LAHDET']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_LEHDET']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'F', 'PLT'],
                            ['front'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_LÄNGET']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'G', 'PLT'],
                            ['front'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LAMMET']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'H', 'PLT'],
                            ['front'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ONNET']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'J', 'PLT'],
                            ['front'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KÄRJET']
                else:
                    fail_guess_because(wordmap, ['N', 7, 'L', 'PLT'],
                            ['front'])
            else:
                fail_guess_because(wordmap, ['N', 7, 'PLT'],
                        [False, 'F', 'G', 'H', 'J', 'L'])
        elif tn == 8:
            if not wordmap['kotus_av']:
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_RAVET']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_BÄNET']
                else:
                    fail_guess_because(wordmap, ['N', 8, False, 'PLT'],
                            ['back'])
            else:
                fail_guess_because(wordmap, ['N', 8, 'PLT'],
                        [False])
        elif tn == 9:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_paras'] = ['N_VARAT']
                else:
                    fail_guess_because(wordmap, ['N', 9, False, 'PLT'],
                            ['at'])
            elif wordmap['kotus_av'] in ['A', 'D']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_paras'] = ['N_PAIKAT']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'A', 'PLT'],
                            ['kat'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pat'):
                    wordmap['new_paras'] = ['N_HIPAT']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'B', 'PLT'],
                            ['pat'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tat'):
                    wordmap['new_paras'] = ['N_RIUTAT']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'B', 'PLT'],
                            ['pat'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('vat'):
                    wordmap['new_paras'] = ['N_TAVAT']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'E', 'PLT'],
                            ['vat'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('dat'):
                    wordmap['new_paras'] = ['N_RAUDAT']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'F', 'PLT'],
                            ['dat'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('gat'):
                    wordmap['new_paras'] = ['N_RANGAT']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'G', 'PLT'],
                            ['gat'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('llat'):
                    wordmap['new_paras'] = ['N_VALLAT']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'I', 'PLT'],
                            ['llat'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnat'):
                    wordmap['new_paras'] = ['N_RANNAT']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'J', 'PLT'],
                            ['llat'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rrat'):
                    wordmap['new_paras'] = ['N_KARRAT']
                else:
                    fail_guess_because(wordmap, ['N', 9, 'K', 'PLT'],
                            ['rrat'])
            else:
                fail_guess_because(wordmap, ['N', 9, 'PLT'],
                        [False, 'A-G', 'I-K'])
        elif tn == 10:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_paras'] = ['N_JUHLAT']
                elif wordmap['lemma'].endswith('ät'):
                    wordmap['new_paras'] = ['N_KÄRÄJÄT']
                else:
                    fail_guess_because(wordmap, ['N', 10, False, 'PLT'],
                            ['at', 'ät'])
            elif wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kat'):
                    wordmap['new_paras'] = ['N_SUKAT']
                elif wordmap['lemma'].endswith('kät'):
                    wordmap['new_paras'] = ['N_SÄRKÄT']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'A', 'PLT'],
                            ['kat', 'kät'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('pat'):
                    wordmap['new_paras'] = ['N_KUOPAT']
                elif wordmap['lemma'].endswith('pät'):
                    wordmap['new_paras'] = ['N_TÖLPÄT']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'B', 'PLT'],
                            ['pat'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('tat'):
                    wordmap['new_paras'] = ['N_ROTAT']
                elif wordmap['lemma'].endswith('tät'):
                    wordmap['new_paras'] = ['N_KENTÄT']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'C', 'PLT'],
                            ['tät'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('ät'):
                    wordmap['new_paras'] = ['N_REIÄT']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'D', 'PLT'],
                            ['ät'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('vat'):
                    wordmap['new_paras'] = ['N_JUOVAT']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'E', 'PLT'],
                            ['vat'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('dat'):
                    wordmap['new_paras'] = ['N_LUHDAT']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'D', 'PLT'],
                            ['dat'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('ngät'):
                    wordmap['new_paras'] = ['N_KENGÄT']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'G', 'PLT'],
                            ['ngät'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnat'):
                    wordmap['new_paras'] = ['N_KUNNAT']
                elif wordmap['lemma'].endswith('nnät'):
                    wordmap['new_paras'] = ['N_HÄNNÄT']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'J', 'PLT'],
                            ['nnat'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('ljät'):
                    wordmap['new_paras'] = ['N_SELJÄT']
                else:
                    fail_guess_because(wordmap, ['N', 10, 'L', 'PLT'],
                            ['ljät'])
            else:
                fail_guess_because(wordmap, ['N', 10, 'PLT'],
                        [False, 'A', 'B', 'D', 'F' 'G', 'J'])
        elif tn == 11:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_paras'] = ['N_KIHARAT']
                else:
                    fail_guess_because(wordmap, ['N', 11, False, 'PLT'],
                            ['at'])
            else:
                fail_guess_because(wordmap, ['N', 11, 'PLT'],
                        [False])
        elif tn == 12:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_paras'] = ['N_MARKKINAT']
                elif wordmap['lemma'].endswith('ät'):
                    wordmap['new_paras'] = ['N_RÄMIÄT']
                else:
                    fail_guess_because(wordmap, ['N', 12, False, 'PLT'],
                            ['at', 'ät'])
            else:
                fail_guess_because(wordmap, ['N', 12, 'PLT'],
                        [False])
        elif tn == 13:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_paras'] = ['N_KASTILJAT']
                else:
                    fail_guess_because(wordmap, ['N', 13, False, 'PLT'],
                            ['at'])
            else:
                fail_guess_because(wordmap, ['N', 13, 'PLT'],
                        [False])
        elif tn == 14:
            if wordmap['kotus_av'] == 'A':
                if wordmap['lemma'].endswith('kat'):
                    wordmap['new_paras'] = ['N_SILAKAT']
                else:
                    fail_guess_because(wordmap, ['N', 14, 'A', 'PLT'],
                            ['at'])
            else:
                fail_guess_because(wordmap, ['N', 14, 'PLT'],
                        ['A'])
        elif tn == 15:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('at'):
                    wordmap['new_paras'] = ['N_HOPEAT']
                elif wordmap['lemma'].endswith('ät'):
                    wordmap['new_paras'] = ['N_RÄMEÄT']
                else:
                    fail_guess_because(wordmap, ['N', 15, False, 'PLT'],
                            ['at'])
            else:
                fail_guess_because(wordmap, ['N', 15, 'PLT'],
                        [False])
        elif tn == 16:
            if wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mmat'):
                    wordmap['new_paras'] = ['N_VANHEMMAT']
                else:
                    fail_guess_because(wordmap, ['N', 16, 'H', 'PLT'],
                            ['at'])
            else:
                fail_guess_because(wordmap, ['N', 16, 'PLT'],
                        ['H'])
        elif tn == 17:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aat'):
                    wordmap['new_paras'] = ['N_HARMAAT']
                elif wordmap['lemma'].endswith('oot'):
                    wordmap['new_paras'] = ['N_TALKOOT']
                elif wordmap['lemma'].endswith('yyt'):
                    wordmap['new_paras'] = ['N_HYNTTYYT']
                elif wordmap['lemma'].endswith('äät'):
                    wordmap['new_paras'] = ['N_PÖLHÄÄT']
                else:
                    fail_guess_because(wordmap, ['N', 17, False, 'PLT'],
                            ['oot', 'yyt', 'äät'])
            else:
                fail_guess_because(wordmap, ['N', 17, 'PLT'],
                        [False])
        elif tn == 18:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aat'):
                    wordmap['new_paras'] = ['N_ITÄMAAT']
                elif wordmap['lemma'].endswith('ait'):
                    wordmap['new_paras'] = ['N_HAIT']
                elif wordmap['lemma'].endswith('uut'):
                    wordmap['new_paras'] = ['N_PUUT']
                elif wordmap['lemma'].endswith('yyt'):
                    wordmap['new_paras'] = ['N_PYYT']
                elif wordmap['lemma'].endswith('äät'):
                    wordmap['new_paras'] = ['N_HÄÄT']
                else:
                    fail_guess_because(wordmap, ['N', 18, False, 'PLT'],
                            ['aat', 'ait', 'uut', 'yyt', 'äät'])
            else:
                fail_guess_because(wordmap, ['N', 18, 'PLT'],
                        [False])
        elif tn == 19:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('iet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_TIET']
                elif wordmap['lemma'].endswith('uot'):
                    wordmap['new_paras'] = ['N_SUOT']
                elif wordmap['lemma'].endswith('yöt'):
                    wordmap['new_paras'] = ['N_TYÖT']
                else:
                    fail_guess_because(wordmap, ['N', 19, False, 'PLT'],
                            ['iet', 'yöt'])
            else:
                fail_guess_because(wordmap, ['N', 19, 'PLT'],
                        [False])
        elif tn == 25:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('met') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_TOIMET']
                elif wordmap['lemma'].endswith('met') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_NIEMET']
                else:
                    fail_guess_because(wordmap, ['N', 25, False, 'PLT'],
                            ['met'])
            else:
                fail_guess_because(wordmap, ['N', 25, 'PLT'],
                        [False])
        elif tn in [24, 26]:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_SAARET']
                elif wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SÄÄRET']
                else:
                    fail_guess_because(wordmap, ['N', 26, False, 'PLT'],
                            ['et'])
            else:
                fail_guess_because(wordmap, ['N', 26, 'PLT'],
                        [False])
        elif tn == 27:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('det') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_VUODET']
                else:
                    fail_guess_because(wordmap, ['N', 27, False, 'PLT'],
                            ['det'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('det') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_VUODET']
                else:
                    fail_guess_because(wordmap, ['N', 27, False, 'PLT'],
                            ['det'])
            else:
                fail_guess_because(wordmap, ['N', 27, 'PLT'],
                        [False])
        elif tn == 28:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('nnet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KANNET']
                elif wordmap['lemma'].endswith('rret') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_VIRRET']
                else:
                    fail_guess_because(wordmap, ['N', 28, False, 'PLT'],
                            ['nnet', 'rret'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nnet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KANNET']
                elif wordmap['lemma'].endswith('nnet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KYNNET']
                else:
                    fail_guess_because(wordmap, ['N', 28, 'J', 'PLT'],
                            ['nnet'])
            else:
                fail_guess_because(wordmap, ['N', 28, 'PLT'],
                        ['J'])
        elif tn == 32:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HÖYHENET']
                else:
                    fail_guess_because(wordmap, ['N', 32, False, 'PLT'],
                            ['et'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('taret'):
                    wordmap['new_paras'] = ['N_LIPOTTARET']
                elif wordmap['lemma'].endswith('täret'):
                    wordmap['new_paras'] = ['N_KIRITTÄRET']
                else:
                    fail_guess_because(wordmap, ['N', 32, 'C', 'PLT'],
                            ['taret'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('kenet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_IKENET']
                else:
                    fail_guess_because(wordmap, ['N', 32, 'D', 'PLT'],
                            ['kenet'])
            else:
                fail_guess_because(wordmap, ['N', 32, 'PLT'],
                        [False])
        elif tn == 33:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('met') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ATERIMET']
                elif wordmap['lemma'].endswith('met') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_KERITSIMET']
                else:
                    fail_guess_because(wordmap, ['N', 33, False, 'PLT'],
                            ['met'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('ttimet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_HOKSOTTIMET']
                elif wordmap['lemma'].endswith('ttimet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SYNNYTTIMET']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'C', 'PLT'],
                            ['ttimet'])
            elif wordmap['kotus_av'] == 'D':
                if wordmap['lemma'].endswith('kimet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_PUKIMET']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'D', 'PLT'],
                            ['kimet'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('timet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ROHTIMET']
                elif wordmap['lemma'].endswith('timet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_VETIMET']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'F', 'PLT'],
                            ['timet'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('ntimet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ANTIMET']
                else:
                    fail_guess_because(wordmap, ['N', 33, 'J', 'PLT'],
                            ['ntimet'])
            else:
                fail_guess_because(wordmap, ['N', 33, 'PLT'],
                        [False, 'C', 'D', 'F', 'J'])
        elif tn == 34:
            if wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('mat'):
                    wordmap['new_paras'] = ['N_SIUNAAMATTOMAT']
                elif wordmap['lemma'].endswith('mät'):
                    wordmap['new_paras'] = ['N_TYÖTTÖMÄT']
                else:
                    fail_guess_because(wordmap, ['N', 34, 'C', 'PLT'],
                            ['mät'])
            else:
                fail_guess_because(wordmap, ['N', 34, 'PLT'],
                        ['C'])
        elif tn == 38:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('set') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_RAPPUSET']
                elif wordmap['lemma'].endswith('set') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_VIHKIÄISET']
                else:
                    fail_guess_because(wordmap, ['N', 38, False, 'PLT'],
                            ['eet'])
            else:
                fail_guess_because(wordmap, ['N', 38, 'PLT'],
                        [False])
        elif tn == 39:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('set') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_SERKUKSET']
                elif wordmap['lemma'].endswith('set') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_YSTÄVYKSET']
                else:
                    fail_guess_because(wordmap, ['N', 39, False, 'PLT'],
                            ['eet'])
            else:
                fail_guess_because(wordmap, ['N', 39, 'PLT'],
                        [False])
        elif tn == 40:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('det') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_OIKEUDET']
                else:
                    fail_guess_because(wordmap, ['N', 40, False, 'PLT'],
                            ['eet'])
            else:
                fail_guess_because(wordmap, ['N', 40, 'PLT'],
                        [False])
        elif tn == 41:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('aat'):
                    wordmap['new_paras'] = ['N_VALJAAT']
                elif wordmap['lemma'].endswith('äät'):
                    wordmap['new_paras'] = ['N_KYNNÄÄT']
                else:
                    fail_guess_because(wordmap, ['N', 41, False, 'PLT'],
                            ['aat'])
            elif wordmap['kotus_av'] in ['A', 'D']:
                if wordmap['lemma'].endswith('kaat'):
                    wordmap['new_paras'] = ['N_TIKKAAT']
                elif wordmap['lemma'].endswith('käät'):
                    wordmap['new_paras'] = ['N_KILPIKKÄÄT']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'A', 'PLT'],
                            ['kaat'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('ppaat'):
                    wordmap['new_paras'] = ['N_RUOPPAAT']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'C', 'PLT'],
                            ['ttaat'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('ttaat'):
                    wordmap['new_paras'] = ['N_RATTAAT']
                elif wordmap['lemma'].endswith('ttyyt'):
                    wordmap['new_paras'] = ['N_RYNTTYYT']
                elif wordmap['lemma'].endswith('ttäät'):
                    wordmap['new_paras'] = ['N_MÄTTÄÄT']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'C', 'PLT'],
                            ['ttaat'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('paat'):
                    wordmap['new_paras'] = ['N_VARPAAT']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'E', 'PLT'],
                            ['rpaat'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('taat'):
                    wordmap['new_paras'] = ['N_TEHTAAT']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'F', 'PLT'],
                            ['taat'])
            elif wordmap['kotus_av'] == 'G':
                if wordmap['lemma'].endswith('nkaat'):
                    wordmap['new_paras'] = ['N_RENKAAT']
                elif wordmap['lemma'].endswith('nkahat'):
                    wordmap['new_paras'] = ['N_KANKAHAT']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'G', 'PLT'],
                            ['nkaat'])
            elif wordmap['kotus_av'] == 'H':
                if wordmap['lemma'].endswith('mpaat'):
                    wordmap['new_paras'] = ['N_ROMPAAT']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'H', 'PLT'],
                            ['mpaat'])
            elif wordmap['kotus_av'] == 'I':
                if wordmap['lemma'].endswith('ltaat'):
                    wordmap['new_paras'] = ['N_MALTAAT']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'I', 'PLT'],
                            ['ltaat'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('ntäät'):
                    wordmap['new_paras'] = ['N_RYNTÄÄT']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'J', 'PLT'],
                            ['ntäät'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rtaat'):
                    wordmap['new_paras'] = ['N_PORTAAT']
                else:
                    fail_guess_because(wordmap, ['N', 41, 'K', 'PLT'],
                            ['rtaat'])
            else:
                fail_guess_because(wordmap, ['N', 41, 'PLT'],
                        [False, 'A', 'C', 'F', 'G', 'J', 'K'])
        elif tn == 42:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('iehet'):
                    wordmap['new_paras'] = ['N_MIEHET']
                else:
                    fail_guess_because(wordmap, ['N', 42, False, 'PLT'],
                            ['het'])
            else:
                fail_guess_because(wordmap, ['N', 42, 'PLT'],
                        [False])
        elif tn == 43:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('uet'):
                    wordmap['new_paras'] = ['N_MATKUET']
                else:
                    fail_guess_because(wordmap, ['N', 43, False, 'PLT'],
                            ['uet'])
            else:
                fail_guess_because(wordmap, ['N', 43, 'PLT'],
                        [False])
        elif tn == 47:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('eet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_LIITTOUTUNEET']
                elif wordmap['lemma'].endswith('eet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HÄVINNEET']
                else:
                    fail_guess_because(wordmap, ['N', 47, False, 'PLT'],
                            ['eet'])
            else:
                fail_guess_because(wordmap, ['N', 47, 'PLT'],
                        [False])
        elif tn == 48:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('eet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_HIUTALEET']
                elif wordmap['lemma'].endswith('eet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_RÄMEET']
                else:
                    fail_guess_because(wordmap, ['N', 48, False, 'PLT'],
                            ['eet'])
            elif wordmap['kotus_av'] in ['A', 'D']:
                if wordmap['lemma'].endswith('keet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KUULOKKEET']
                elif wordmap['lemma'].endswith('keet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_SILMÄKKEET']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'AD', 'PLT'],
                            ['peet'])
            elif wordmap['kotus_av'] == 'B':
                if wordmap['lemma'].endswith('peet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_KAMPPEET']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'B', 'PLT'],
                            ['peet'])
            elif wordmap['kotus_av'] == 'C':
                if wordmap['lemma'].endswith('teet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_VAATTEET']
                elif wordmap['lemma'].endswith('teet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_HYNTTEET']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'C', 'PLT'],
                            ['teet'])
            elif wordmap['kotus_av'] == 'E':
                if wordmap['lemma'].endswith('peet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_TARPEET']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'E', 'PLT'],
                            ['teet'])
            elif wordmap['kotus_av'] == 'F':
                if wordmap['lemma'].endswith('teet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_SUHTEET']
                elif wordmap['lemma'].endswith('teet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_TIETEET']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'F', 'PLT'],
                            ['teet'])
            elif wordmap['kotus_av'] == 'J':
                if wordmap['lemma'].endswith('nteet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_SALONTEET']
                elif wordmap['lemma'].endswith('nteet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_RINTEET']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'J', 'PLT'],
                            ['teet'])
            elif wordmap['kotus_av'] == 'K':
                if wordmap['lemma'].endswith('rteet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_MURTEET']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'J', 'PLT'],
                            ['teet'])
            elif wordmap['kotus_av'] == 'L':
                if wordmap['lemma'].endswith('keet') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_ALKEET']
                elif wordmap['lemma'].endswith('keet') and wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['N_PERKEET']
                else:
                    fail_guess_because(wordmap, ['N', 48, 'L', 'PLT'],
                            ['teet'])
            else:
                fail_guess_because(wordmap, ['N', 48, 'PLT'],
                        ['F'])
        elif tn == 49:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('et') and wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['N_SAMMALET']
                else:
                    fail_guess_because(wordmap, ['N', 49, False, 'PLT'],
                            ['eet'])
            else:
                fail_guess_because(wordmap, ['N', 49, 'PLT'],
                        [False])
        elif tn == 1007:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('veljet') or wordmap['lemma'].endswith('Veljet'):
                    wordmap['new_paras'] = ['N_VELJET']
                else:
                    fail_guess_because(wordmap, ['N', 7, False, 'PLT'],
                            ['veljet'])
            elif wordmap['kotus_av'] in ['D', 'L']:
                if wordmap['lemma'].endswith('veljet') or wordmap['lemma'].endswith('Veljet'):
                    wordmap['new_paras'] = ['N_VELJET']
                else:
                    fail_guess_because(wordmap, ['N', 7, False, 'PLT'],
                            ['veljet'])
            else:
                fail_guess_because(wordmap, ['N', 7, 'PLT'],
                        [False, 'D', 'L'])
        elif tn == 1010:
            if not wordmap['kotus_av']:
                if wordmap['lemma'].endswith('pojat') or wordmap['lemma'].endswith('Pojat'):
                    wordmap['new_paras'] = ['N_POJAT']
                else:
                    fail_guess_because(wordmap, ['N', 10, False, 'PLT'],
                            ['pojat'])
            elif wordmap['kotus_av'] in ['D', 'L']:
                if wordmap['lemma'].endswith('pojat') or wordmap['lemma'].endswith('Pojat'):
                    wordmap['new_paras'] = ['N_POJAT']
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
                wordmap['new_paras'] = ['A_TUMMAHKO']
            elif wordmap['lemma'].endswith('u') or wordmap['lemma'].endswith('U'):
                wordmap['new_paras'] = ['A_VALKAISTU']
            elif wordmap['lemma'].endswith('y') or wordmap['lemma'].endswith('Y'):
                wordmap['new_paras'] = ['A_HÄPÄISTY']
            elif wordmap['lemma'].endswith('ö'):
                wordmap['new_paras'] = ['A_HÖLÖ']
            else:
                fail_guess_because(wordmap, ['A', 1, False], 
                        ['o O', 'u', 'yY', 'ö'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('ko'):
                wordmap['new_paras'] = ['A_KOLKKO']
            elif wordmap['lemma'].endswith('ku'):
                wordmap['new_paras'] = ['A_VIRKKU']
            elif wordmap['lemma'].endswith('ky'):
                wordmap['new_paras'] = ['A_SÄIKKY']
            elif wordmap['lemma'].endswith('kö'):
                wordmap['new_paras'] = ['A_KÖKKÖ']
            else:
                fail_guess_because(wordmap, ['A', 1, 'A'], 
                        ['ko', 'ku', 'ky', 'kö'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppo'):
                wordmap['new_paras'] = ['A_SUIPPO']
            elif wordmap['lemma'].endswith('ppu'):
                wordmap['new_paras'] = ['A_IKÄLOPPU']
            elif wordmap['lemma'].endswith('ppö'):
                wordmap['new_paras'] = ['A_LÖRPPÖ']
            else:
                fail_guess_because(wordmap, ['A', 1, 'B'], 
                        ['ppo', 'ppu', 'ppö'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tto'):
                wordmap['new_paras'] = ['A_VELTTO']
            elif wordmap['lemma'].endswith('ttu'):
                wordmap['new_paras'] = ['A_VIMMATTU']
            elif wordmap['lemma'].endswith('tty'):
                wordmap['new_paras'] = ['A_YLENNETTY']
            elif wordmap['lemma'].endswith('ttö'):
                wordmap['new_paras'] = ['A_KYYTTÖ']
            else:
                fail_guess_because(wordmap, ['A', 1, 'C'], 
                        ['tto', 'ttu', 'tty', 'ttö'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('ko'):
                wordmap['new_paras'] = ['A_LAKO']
            else:
                fail_guess_because(wordmap, ['A', 1, 'D'],
                        ['ko'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('po'):
                wordmap['new_paras'] = ['A_KELPO']
            else:
                fail_guess_because(wordmap, ['A', 1, 'E'],
                        ['po'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('to'):
                wordmap['new_paras'] = ['A_MIETO']
            elif wordmap['lemma'].endswith('tu'):
                wordmap['new_paras'] = ['A_VIIPALOITU']
            elif wordmap['lemma'].endswith('ty'):
                wordmap['new_paras'] = ['A_YKSILÖITY']
            elif wordmap['lemma'].endswith('tö'):
                fail_guess_because(wordmap, ['A', 1, 'F'],
                        ['to', 'tu', 'ty'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nko'):
                wordmap['new_paras'] = ['A_LENKO']
            else:
                fail_guess_because(wordmap, ['A', 1, 'G'],
                        ['nko'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('lto'):
                wordmap['new_paras'] = ['A_MELTO']
            elif wordmap['lemma'].endswith('ltu'):
                wordmap['new_paras'] = ['A_PARANNELTU']
            elif wordmap['lemma'].endswith('lty'):
                wordmap['new_paras'] = ['A_VÄHÄTELTY']
            else:
                fail_guess_because(wordmap, ['A', 1, 'I'],
                        ['lto', 'ltu', 'lty'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nto'):
                wordmap['new_paras'] = ['A_VENTO']
            elif wordmap['lemma'].endswith('ntu'):
                wordmap['new_paras'] = ['A_PANTU']
            elif wordmap['lemma'].endswith('nty'):
                wordmap['new_paras'] = ['A_MENTY']
            else:
                fail_guess_because(wordmap, ['A', 1, 'J'],
                        ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rto'):
                wordmap['new_paras'] = ['A_MARTO']
            elif wordmap['lemma'].endswith('rtu'):
                wordmap['new_paras'] = ['A_PURTU']
            elif wordmap['lemma'].endswith('rty'):
                wordmap['new_paras'] = ['A_PIERTY']
            else:
                fail_guess_because(wordmap, ['A', 1, 'K'],
                        ['rto', 'rto', 'rty'])
        else:
            fail_guess_because(wordmap, ['A', 1], ['A–K'])
    elif tn == 2:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('o'):
                wordmap['new_paras'] = ['A_KOHELO']
            elif wordmap['lemma'].endswith('ö'):
                wordmap['new_paras'] = ['A_LÖPERÖ']
            else:
                fail_guess_because(wordmap, ['A', 2, False],
                        ['o', 'ö'])
        else:
            fail_guess_because(wordmap, ['A', 2], [False])
    elif tn == 3:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('io'):
                wordmap['new_paras'] = ['A_AUTIO']
            elif wordmap['lemma'].endswith('iö'):
                wordmap['new_paras'] = ['A_RIIVIÖ']
            else:
                fail_guess_because(wordmap, ['A', 3, False],
                        ['io', 'iö'])
        else:
            fail_guess_because(wordmap, ['A', 3], [False])
    elif tn == 4:
        if wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('kko'):
                wordmap['new_paras'] = ['A_HUPAKKO']
            else:
                fail_guess_because(wordmap, ['A', 4, 'A'],
                        ['kko'])
        else:
            fail_guess_because(wordmap, ['A', 4], ['A'])
    elif tn == 5:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_ABNORMI']
            elif wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_STYDI']
            else:
                fail_guess_because(wordmap, ['A', 5, False, 'i'],
                        ['front', 'back'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_OPAAKKI']
            elif wordmap['lemma'].endswith('ki') and wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_PINKKI']
            else:
                fail_guess_because(wordmap, ['A', 5, 'A'],
                        ['ki', 'front', 'back'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppi') and wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_SIPPI']
            else:
                fail_guess_because(wordmap, ['A', 5, 'B'],
                        ['ppi', 'front', 'back'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tti') and wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_HURTTI']
            elif wordmap['lemma'].endswith('tti') and wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_VÄÄRTTI']
            else:
                fail_guess_because(wordmap, ['A', 5, 'C'],
                        ['tti', 'front', 'back'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_TUHTI']
            elif wordmap['lemma'].endswith('ti') and wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_REHTI']
            else:
                fail_guess_because(wordmap, ['A', 5, 'F'],
                        ['ti', 'front', 'back'])
    elif tn == 6:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_ABNORMAALI']
            elif wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_ÖYKKÄRI']
            else:
                fail_guess_because(wordmap, ['A', 6, False, 'i'],
                        ['front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 6],
                    [False])
    elif tn == 8:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_TOOPE']
            elif wordmap['lemma'].endswith('e') and wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_BEIGE']
            else:
                fail_guess_because(wordmap, ['A', 8, False],
                        ['e', 'front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 8],
                    [False])
    elif tn == 9:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a') or wordmap['lemma'].endswith('A'):
                wordmap['new_paras'] = ['A_AAVA']
            else:
                fail_guess_because(wordmap, ['A', 9, False],
                        ['a'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('ka'):
                wordmap['new_paras'] = ['A_TARKKA']
            else:
                fail_guess_because(wordmap, ['A', 9, 'A'],
                        ['kka'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tta'):
                wordmap['new_paras'] = ['A_MATTA']
            else:
                fail_guess_because(wordmap, ['A', 9, 'C'],
                        ['tta'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('ka'):
                wordmap['new_paras'] = ['A_TARKKA']
            else:
                fail_guess_because(wordmap, ['A', 9, 'D'],
                        ['ka'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('pa'):
                wordmap['new_paras'] = ['A_HALPA']
            else:
                fail_guess_because(wordmap, ['A', 9, 'E'],
                        ['pa'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('ta'):
                wordmap['new_paras'] = ['A_EHTA']
            else:
                fail_guess_because(wordmap, ['A', 9, 'F'],
                        ['ta'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nka'):
                wordmap['new_paras'] = ['A_SANKA']
            else:
                fail_guess_because(wordmap, ['A', 9, 'F'],
                        ['ta'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mpa'):
                wordmap['new_paras'] = ['A_RAMPA']
            else:
                fail_guess_because(wordmap, ['A', 9, 'H'],
                        ['mpa'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nta'):
                wordmap['new_paras'] = ['A_VIHANTA']
        else:
            fail_guess_because(wordmap, ['A', 9],
                    [False, 'A-K'])
    elif tn == 10:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a') or wordmap['lemma'].endswith('A'):
                wordmap['new_paras'] = ['A_RUMA']
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_paras'] = ['A_TYHMÄ']
            else:
                fail_guess_because(wordmap, ['A', 10, False],
                        ['a', 'ä'])
        elif wordmap['kotus_av'] in ['A', 'D']:
            if wordmap['lemma'].endswith('ka'):
                wordmap['new_paras'] = ['A_HOIKKA']
            elif wordmap['lemma'].endswith('kä'):
                wordmap['new_paras'] = ['A_MYKKÄ']
            else:
                fail_guess_because(wordmap, ['A', 10, 'A'],
                        ['kka', 'kkä'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppa'):
                wordmap['new_paras'] = ['A_POPPA']
            elif wordmap['lemma'].endswith('ppä'):
                wordmap['new_paras'] = ['A_HÖMPPÄ']
            else:
                fail_guess_because(wordmap, ['A', 10, 'B'],
                        ['ppa', 'ppä'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('pa'):
                wordmap['new_paras'] = ['A_VOIPA']
            elif wordmap['lemma'].endswith('pä'):
                wordmap['new_paras'] = ['A_KÄYPÄ']
            else:
                fail_guess_because(wordmap, ['A', 10, 'E'],
                        ['pa', 'pä'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('tä'):
                wordmap['new_paras'] = ['A_MÄTÄ']
            else:
                fail_guess_because(wordmap, ['A', 10, 'F'],
                        ['ta', 'tä'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nka'):
                wordmap['new_paras'] = ['A_SANKA']
            elif wordmap['lemma'].endswith('nkä'):
                wordmap['new_paras'] = ['A_VÄNKÄ']
            else:
                fail_guess_because(wordmap, ['A', 10, 'G'],
                        ['nka', 'nkä'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('lta'):
                wordmap['new_paras'] = ['A_KULTA']
            else:
                fail_guess_because(wordmap, ['A', 10, 'I'],
                        ['lta'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntä'):
                wordmap['new_paras'] = ['A_LÄNTÄ']
            else:
                fail_guess_because(wordmap, ['A', 10, 'J'],
                        ['ntä'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rta'):
                wordmap['new_paras'] = ['A_TURTA']
            else:
                fail_guess_because(wordmap, ['A', 10, 'K'],
                        ['rta'])
        else:
            fail_guess_because(wordmap, ['A', 10],
                    [False, 'A', 'B', 'E', 'G', 'I-K'])
    elif tn == 11:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a'):
                wordmap['new_paras'] = ['A_HAPERA']
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_paras'] = ['A_SÄKKÄRÄ']
            else:
                fail_guess_because(wordmap, ['A', 11, False],
                        ['a', 'ä'])
        else:
            fail_guess_because(wordmap, ['A', 11],
                    [False])
    elif tn == 12:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a') or wordmap['lemma'].endswith('A'):
                wordmap['new_paras'] = ['A_HARMAJA']
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_paras'] = ['A_HÖPPÄNÄ']
            else:
                fail_guess_because(wordmap, ['A', 12, False],
                        ['a'])
        else:
            fail_guess_because(wordmap, ['A', 12],
                    [False])
    elif tn == 13:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a'):
                wordmap['new_paras'] = ['A_LATUSKA']
            else:
                fail_guess_because(wordmap, ['A', 13, False],
                        ['a', 'ä'])
        else:
            fail_guess_because(wordmap, ['A', 13],
                    [False])
    elif tn == 14:
        if wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('kka'):
                wordmap['new_paras'] = ['A_HAILAKKA']
            elif wordmap['lemma'].endswith('kkä'):
                wordmap['new_paras'] = ['A_RÄVÄKKÄ']
            else:
                fail_guess_because(wordmap, ['A', 14, 'A'],
                        ['kka', 'kkä'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tta'):
                wordmap['new_paras'] = ['A_POHATTA']
            else:
                fail_guess_because(wordmap, ['A', 14, 'C'],
                        ['tta'])
        else:
            fail_guess_because(wordmap, ['A', 14],
                    ['A', 'C'])
    elif tn == 15:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('oa'):
                wordmap['new_paras'] = ['A_AINOA']
            elif wordmap['lemma'].endswith('ee') and wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_OIKEE']
            elif wordmap['lemma'].endswith('ea'):
                wordmap['new_paras'] = ['A_KORKEA']
            elif wordmap['lemma'].endswith('eä'):
                wordmap['new_paras'] = ['A_JÄREÄ']
            else:
                fail_guess_because(wordmap, ['A', 15, False],
                        ['oa', 'ea', 'eä'])
        else:
            fail_guess_because(wordmap, ['A', 15],
                    [False])
    elif tn == 16:
        if wordmap['kotus_av'] == 'H':
            if wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_AIEMPI']
            elif wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_LÄHEMPI']
            else:
                fail_guess_because(wordmap, ['A', 16, 'H'],
                        ['back'])
        else:
            fail_guess_because(wordmap, ['A', 16],
                    ['H'])
    elif tn == 17:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aa'):
                wordmap['new_paras'] = ['A_VAPAA']
            else:
                fail_guess_because(wordmap, ['A', 17, False],
                        ['aa', 'ee', 'oo', 'uu', 'yy', 'ää', 'öö'])
        else:
            fail_guess_because(wordmap, ['A', 17],
                    [False])
    elif tn == 18:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('a'):
                wordmap['new_paras'] = ['A_PEEAA']
            elif wordmap['lemma'].endswith('u'):
                wordmap['new_paras'] = ['A_MUU']
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_paras'] = ['A_SYYPÄÄ']
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
                wordmap['new_paras'] = ['A_GAY']
            else:
                fail_guess_because(wordmap, ['A', 21, False],
                        ['gay', 'é', 'è'], "guessing 21 is not possible")
        else:
            fail_guess_because(wordmap, ['A', 21],
                    [False])
    elif tn in [24, 26]:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_SUURI']
            elif wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_PIENI']
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
                    wordmap['new_paras'] = ['A_UUSI']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['A_TÄYSI']
                else:
                    fail_guess_because(wordmap, ['A', 26, False, 'si'],
                            ['back', 'front'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('si'):
                if wordmap['harmony'] == 'back':
                    wordmap['new_paras'] = ['A_UUSI']
                elif wordmap['harmony'] == 'front':
                    wordmap['new_paras'] = ['A_TÄYSI']
                else:
                    fail_guess_because(wordmap, ['A', 27, 'F', 'si'],
                            ['back', 'front'])
        else:
            fail_guess_because(wordmap, ['A', 27],
                    [False])
    elif tn == 32:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_AVOIN']
            elif wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_TYVEN']
            else:
                fail_guess_because(wordmap, ['A', 32, False],
                    ['back', 'front'])
    elif wordmap['kotus_tn'] == 33:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('in') and wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_AVOIN']
            else:
                fail_guess_because(wordmap, ['A', 33, 'B'],
                        ['in', 'back'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('hapan'):
                wordmap['new_paras'] = ['A_HAPAN']
            else:
                fail_guess_because(wordmap, ['A', 33, 'B'],
                        ['hapan'])
        else:
            fail_guess_because(wordmap, ['A', 33], ['B'])
    elif wordmap['kotus_tn'] == 34:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ton'):
                wordmap['new_paras'] = ['A_ALASTON']
            else:
                fail_guess_because(wordmap, ['A', 34, False],
                        ['ton'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('ton'):
                wordmap['new_paras'] = ['A_VIATON']
            elif wordmap['lemma'].endswith('tön'):
                wordmap['new_paras'] = ['A_KYVYTÖN']
            else:
                fail_guess_because(wordmap, ['A', 34, 'C'],
                        ['ton', 'tön'])
        else:
            fail_guess_because(wordmap, ['A', 34], [False, 'C'])
    elif wordmap['kotus_tn'] == 35:
        if wordmap['kotus_av'] == 'H':
            if wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_LÄMMIN']
            else:
                fail_guess_because(wordmap, ['A', 35, False],
                    ['back', 'front'])
        else:
            fail_guess_because(wordmap, ['A', 35],
                ['H' ])
    elif wordmap['kotus_tn'] == 36:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_PAHIN']
            elif wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_SISIN']
            else:
                fail_guess_because(wordmap, ['A', 36, 'J'],
                    ['front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 36],
                [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 37:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('vasen'):
                wordmap['new_paras'] = ['A_VASEN']
            else:
                fail_guess_because(wordmap, ['A', 37, False],
                    ['vasen'])
        else:
            fail_guess_because(wordmap, ['A', 37],
                [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 38:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_AAKKOSELLINEN']
            elif wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_KYLMÄJÄRKINEN']
            else:
                fail_guess_because(wordmap, ['A', 38, False],
                    ['front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 38],
                [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 39:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_SYMPPIS']
            else:
                fail_guess_because(wordmap, ['A', 38, False],
                    ['front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 38],
                [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 40:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('yys'):
                wordmap['new_paras'] = ['A_LÄHTEISYYS']
            else:
                fail_guess_because(wordmap, ['A', 40],
                        ['yys'])
        else:
            fail_guess_because(wordmap, ['A', 40],
                [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 41:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('as'):
                wordmap['new_paras'] = ['A_AUTUAS']
            elif wordmap['lemma'].endswith('is') and wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_VALMIS']
            elif wordmap['lemma'].endswith('is') and wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_TIIVIS']
            elif wordmap['lemma'].endswith('äs'):
                wordmap['new_paras'] = ['A_TYÖLÄS']
            else:
                fail_guess_because(wordmap, ['A', 41, False],
                    ['as', 'is', 'äs'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('kas'):
                wordmap['new_paras'] = ['A_VOIMAKAS']
            elif wordmap['lemma'].endswith('käs'):
                wordmap['new_paras'] = ['A_TYYLIKÄS']
            else:
                fail_guess_because(wordmap, ['A', 41, 'A'],
                    ['kas', 'käs'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('pas'):
                wordmap['new_paras'] = ['A_REIPAS']
            else:
                fail_guess_because(wordmap, ['A', 41, 'B'],
                    ['pas', 'päs'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tas'):
                wordmap['new_paras'] = ['A_RIETAS']
            elif wordmap['lemma'].endswith('tis') and wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_RAITIS']
            else:
                fail_guess_because(wordmap, ['A', 41, 'C'],
                    ['tas', 'tis', 'tus', 'täs', 'front'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('das'):
                wordmap['new_paras'] = ['A_HIDAS']
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('ras'):
                wordmap['new_paras'] = ['A_HARRAS']
            else:
                fail_guess_because(wordmap, ['A', 41, 'K'],
                    ['rras'])
        else:
            fail_guess_because(wordmap, ['A', 41],
                [False, 'A C F K'])
    elif wordmap['kotus_tn'] == 43:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ut'):
                wordmap['new_paras'] = ['A_OHUT']
            elif wordmap['lemma'].endswith('yt'):
                wordmap['new_paras'] = ['A_EHYT']
            else:
                fail_guess_because(wordmap, ['A', 43, False],
                    ['ut', 'yt'])
        else:
            fail_guess_because(wordmap, ['A', 43],
                [False])
    elif wordmap['kotus_tn'] == 44:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ut'):
                wordmap['new_paras'] = ['A_AINUT']
            else:
                fail_guess_because(wordmap, ['A', 44, False],
                    ['ut'])
        else:
            fail_guess_because(wordmap, ['A', 44],
                [False])
    elif wordmap['kotus_tn'] == 47:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ut'):
                wordmap['new_paras'] = ['A_KULUNUT']
            elif wordmap['lemma'].endswith('yt'):
                wordmap['new_paras'] = ['A_ÄLLISTYNYT']
            else:
                fail_guess_because(wordmap, ['A', 47, False],
                    ['yt'])
        else:
            fail_guess_because(wordmap, ['A', 46],
                [False], "cannot gradate")
    elif tn == 48:
        if not wordmap['kotus_av']:
            if wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_AHNE']
            elif wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_TERVE']
            else:
                fail_guess_because(wordmap, ['A', 48, False],
                    ['front', 'back'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('de') and wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['A_KADE']
            else:
                fail_guess_because(wordmap, ['A', 48, 'F'],
                    ['de', 'front', 'back'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('lle') and wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['A_HELLE']
            else:
                fail_guess_because(wordmap, ['A', 48, 'I'],
                    ['lle', 'front', 'back'])
        else:
            fail_guess_because(wordmap, ['A', 48],
                    [False, 'F', 'I'])
    elif tn == 99:
        wordmap['new_paras'] = ['#']
    elif tn == 1010:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('pitkä'):
                wordmap['new_paras'] = ['A_PITKÄ']
            else:
                fail_guess_because(wordmap, ['A', 10, 'D', 'POIKA'],
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
                wordmap['new_paras'] = ['V_PUNOA']
            elif wordmap['lemma'].endswith('ua'):
                wordmap['new_paras'] = ['V_KAUNISTUA']
            elif wordmap['lemma'].endswith('yä'):
                wordmap['new_paras'] = ['V_ÄLLISTYÄ']
            elif wordmap['lemma'].endswith('öä'):
                wordmap['new_paras'] = ['V_SÄILÖÄ']
            else:
                fail_guess_because(wordmap, ['V', 52, False], 
                        ['oa', 'ua', 'yä', 'öä'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('koa'):
                wordmap['new_paras'] = ['V_HAUKKOA']
            elif wordmap['lemma'].endswith('kua'):
                wordmap['new_paras'] = ['V_NUOKKUA']
            elif wordmap['lemma'].endswith('kyä'):
                wordmap['new_paras'] = ['V_KÄRKKYÄ']
            else:
                fail_guess_because(wordmap, ['V', 52, 'A'], 
                        ['ko', 'ku', 'ky'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppoa'):
                wordmap['new_paras'] = ['V_HARPPOA']
            elif wordmap['lemma'].endswith('ppua'):
                wordmap['new_paras'] = ['V_LOPPUA']
            elif wordmap['lemma'].endswith('ppyä'):
                wordmap['new_paras'] = ['V_LEPPYÄ']
            else:
                fail_guess_because(wordmap, ['V', 52, 'B'], 
                        ['ppo', 'ppu', 'ppy'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('ttoa'):
                wordmap['new_paras'] = ['V_VIITTOA']
            elif wordmap['lemma'].endswith('ttua'):
                wordmap['new_paras'] = ['V_HERMOTTUA']
            elif wordmap['lemma'].endswith('ttyä'):
                wordmap['new_paras'] = ['V_KIVETTYÄ']
            else:
                fail_guess_because(wordmap, ['V', 52, 'C'], 
                        ['tto', 'ttu', 'tty'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('koa'):
                wordmap['new_paras'] = ['V_TAKOA']
            elif wordmap['lemma'].endswith('ukua'):
                wordmap['new_paras'] = ['V_MAUKUA']
            elif wordmap['lemma'].endswith('kua'):
                wordmap['new_paras'] = ['V_NUOKKUA']
            elif wordmap['lemma'].endswith('kyä'):
                wordmap['new_paras'] = ['V_MÄIKYÄ']
            else:
                fail_guess_because(wordmap, ['V', 52, 'D'],
                        ['ko'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('poa'):
                wordmap['new_paras'] = ['V_SILPOA']
            elif wordmap['lemma'].endswith('pua'):
                wordmap['new_paras'] = ['V_HIIPUA']
            elif wordmap['lemma'].endswith('pyä'):
                wordmap['new_paras'] = ['V_SYÖPYÄ']
            else:
                fail_guess_because(wordmap, ['V', 52, 'E'],
                        ['poa', 'pua', 'pyä'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('toa'):
                wordmap['new_paras'] = ['V_KIETOA']
            elif wordmap['lemma'].endswith('tua'):
                wordmap['new_paras'] = ['V_ROHTUA']
            elif wordmap['lemma'].endswith('tyä'):
                wordmap['new_paras'] = ['V_SILIYTYÄ']
            else:
                fail_guess_because(wordmap, ['V', 52, 'F'],
                        ['toa', 'tua', 'tyä'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nkua'):
                wordmap['new_paras'] = ['V_VINKUA']
            elif wordmap['lemma'].endswith('nkoa'):
                wordmap['new_paras'] = ['V_PENKOA']
            else:
                fail_guess_because(wordmap, ['V', 52, 'G'],
                        ['nko'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mpoa'):
                wordmap['new_paras'] = ['V_TEMPOA']
            elif wordmap['lemma'].endswith('mpua'):
                wordmap['new_paras'] = ['V_AMPUA']
            else:
                fail_guess_because(wordmap, ['V', 52, 'G'],
                        ['nko'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('ltua'):
                wordmap['new_paras'] = ['V_HUMALTUA']
            elif wordmap['lemma'].endswith('ltyä'):
                wordmap['new_paras'] = ['V_MIELTYÄ']
            else:
                fail_guess_because(wordmap, ['V', 52, 'I'],
                        ['lto', 'ltu', 'lty'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntua'):
                wordmap['new_paras'] = ['V_VAKAANTUA']
            elif wordmap['lemma'].endswith('ntyä'):
                wordmap['new_paras'] = ['V_TYHJENTYÄ']
            else:
                fail_guess_because(wordmap, ['V', 52, 'J'],
                        ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rtoa'):
                wordmap['new_paras'] = ['V_VARTOA']
            elif wordmap['lemma'].endswith('rtua'):
                wordmap['new_paras'] = ['V_PUSERTUA']
            elif wordmap['lemma'].endswith('rtyä'):
                wordmap['new_paras'] = ['V_KIERTYÄ']
            else:
                fail_guess_because(wordmap, ['V', 52, 'K'],
                        ['rtoa', 'rtua', 'rtyä'])
        else:
            fail_guess_because(wordmap, ['V', 52],
                    [False, 'A-K'])
    elif tn == 53:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aa'):
                wordmap['new_paras'] = ['V_MUTRISTAA']
            elif wordmap['lemma'].endswith('ää'):
                wordmap['new_paras'] = ['V_KIVISTÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 53, False],
                        ['aa', 'ää'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('ttaa'):
                wordmap['new_paras'] = ['V_VIEROITTAA']
            elif wordmap['lemma'].endswith('ttää'):
                wordmap['new_paras'] = ['V_RÄPSYTTÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 53, 'C'],
                        ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('kaa'):
                wordmap['new_paras'] = ['V_PURKAA']
            else:
                fail_guess_because(wordmap, ['V', 53, 'D'],
                        ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_paras'] = ['V_MOJAHTAA']
            elif wordmap['lemma'].endswith('tää'):
                wordmap['new_paras'] = ['V_YSKÄHTÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 53, 'F'],
                        ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntää'):
                wordmap['new_paras'] = ['V_KYNTÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 53, 'J'],
                        ['nto', 'ntu', 'nty'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rtaa'):
                wordmap['new_paras'] = ['V_SORTAA']
            else:
                fail_guess_because(wordmap, ['V', 53, 'K'],
                        ['nto', 'ntu', 'nty'])
        else:
            fail_guess_because(wordmap, ['V', 53], [False])
    elif tn == 54:
        if wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_paras'] = ['V_HUUTAA']
            elif wordmap['lemma'].endswith('tää'):
                wordmap['new_paras'] = ['V_PYYTÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 54, False],
                        ['tää', 'taa'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('ltaa'):
                wordmap['new_paras'] = ['V_SIVALTAA']
            elif wordmap['lemma'].endswith('ltää'):
                wordmap['new_paras'] = ['V_VIHELTÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 54, 'I'],
                        ['tää', 'taa'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntaa'):
                wordmap['new_paras'] = ['V_HUONONTAA']
            elif wordmap['lemma'].endswith('ntää'):
                wordmap['new_paras'] = ['V_HIVENTÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 54, 'J'],
                        ['tää', 'taa'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rtaa'):
                wordmap['new_paras'] = ['V_KUHERTAA']
            elif wordmap['lemma'].endswith('rtää'):
                wordmap['new_paras'] = ['V_NÄPERTÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 54, 'K'],
                        ['tää', 'taa'])
        else:
            fail_guess_because(wordmap, ['V', 54], ['F', 'I-K'])
    elif tn == 55:
        if wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_paras'] = ['V_JOUTAA']
            elif wordmap['lemma'].endswith('tää'):
                wordmap['new_paras'] = ['V_KIITÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 55, 'F'],
                        ['kko'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('ltää'):
                wordmap['new_paras'] = ['V_YLTÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 55, 'I'],
                        ['ltää'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntää'):
                wordmap['new_paras'] = ['V_ENTÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 55, 'J'],
                        ['tää', 'taa'])
        else:
            fail_guess_because(wordmap, ['V', 55], ['F', 'I', 'J'])
    elif tn == 56:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aa'):
                wordmap['new_paras'] = ['V_KASVAA']
            else:
                fail_guess_because(wordmap, ['V', 56, False],
                        ['front', 'back'])
        elif wordmap['kotus_av'] in ['A', 'D']:
            if wordmap['lemma'].endswith('kaa'):
                wordmap['new_paras'] = ['V_VIRKKAA']
            else:
                fail_guess_because(wordmap, ['V', 56, 'A'],
                        ['kaa'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppaa'):
                wordmap['new_paras'] = ['V_TAPPAA']
            else:
                fail_guess_because(wordmap, ['V', 56, 'B'],
                        ['kkaa'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('ttaa'):
                wordmap['new_paras'] = ['V_AUTTAA']
            else:
                fail_guess_because(wordmap, ['V', 56, 'C'],
                        ['kkaa'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_paras'] = ['V_SATAA']
            else:
                fail_guess_because(wordmap, ['V', 56, 'F'],
                        ['kkaa'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntaa'):
                wordmap['new_paras'] = ['V_KANTAA']
            else:
                fail_guess_because(wordmap, ['V', 56, 'J'],
                        ['kkaa'])
        else:
            fail_guess_because(wordmap, ['V', 56],
                    [False])
    elif tn == 57:
        if wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_paras'] = ['V_KAATAA']
            else:
                fail_guess_because(wordmap, ['V', 57, 'F'],
                        ['e', 'front', 'back'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rtaa'):
                wordmap['new_paras'] = ['V_SAARTAA']
            else:
                fail_guess_because(wordmap, ['V', 57, 'K'],
                        ['e', 'front', 'back'])
        else:
            fail_guess_because(wordmap, ['V', 57],
                    [False])
    elif tn == 58:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ea'):
                wordmap['new_paras'] = ['V_SOTKEA']
            elif wordmap['lemma'].endswith('eä'):
                wordmap['new_paras'] = ['V_KYTKEÄ']
            else:
                fail_guess_because(wordmap, ['V', 58, False],
                        ['ea', 'eä'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('kea'):
                wordmap['new_paras'] = ['V_PUKEA']
            else:
                fail_guess_because(wordmap, ['V', 58, 'D'],
                        ['kka'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('peä'):
                wordmap['new_paras'] = ['V_RYPEÄ']
            else:
                fail_guess_because(wordmap, ['V', 58, 'E'],
                        ['tta'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('tea'):
                wordmap['new_paras'] = ['V_KUTEA']
            elif wordmap['lemma'].endswith('teä'):
                wordmap['new_paras'] = ['V_PÄTEÄ']
            else:
                fail_guess_because(wordmap, ['V', 58, 'F'],
                        ['ka'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nkea'):
                wordmap['new_paras'] = ['V_TUNKEA']
            else:
                fail_guess_because(wordmap, ['V', 58, 'G'],
                        ['pa'])
        elif wordmap['kotus_av'] == 'L':
            if wordmap['lemma'].endswith('kea'):
                wordmap['new_paras'] = ['V_POLKEA']
            elif wordmap['lemma'].endswith('keä'):
                wordmap['new_paras'] = ['V_SÄRKEÄ']
            else:
                fail_guess_because(wordmap, ['V', 58, 'L'],
                        ['ta'])
        else:
            fail_guess_because(wordmap, ['V', 58],
                    [False, 'V-K'])
    elif tn == 59:
        if wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntea'):
                wordmap['new_paras'] = ['V_TUNTEA']
            else:
                fail_guess_because(wordmap, ['V', 59, False],
                        ['a', 'ä'])
        else:
            fail_guess_because(wordmap, ['V', 59, 'K'],
                    ['rta'])
    elif tn == 60:
        if wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('hteä'):
                wordmap['new_paras'] = ['V_LÄHTEÄ']
            else:
                fail_guess_because(wordmap, ['V', 60, False],
                        ['a', 'ä'])
        else:
            fail_guess_because(wordmap, ['V', 60],
                    [False])
    elif tn == 61:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ia'):
                wordmap['new_paras'] = ['V_KOSIA']
            elif wordmap['lemma'].endswith('iä'):
                wordmap['new_paras'] = ['V_RYSKIÄ']
            else:
                fail_guess_because(wordmap, ['V', 61, False],
                        ['ia', 'iä'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('kia'):
                wordmap['new_paras'] = ['V_KUKKIA']
            elif wordmap['lemma'].endswith('kiä'):
                wordmap['new_paras'] = ['V_SÖRKKIÄ']
            else:
                fail_guess_because(wordmap, ['V', 61, 'A'],
                        ['kia', 'kiä'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('ppia'):
                wordmap['new_paras'] = ['V_KALPPIA']
            elif wordmap['lemma'].endswith('ppiä'):
                wordmap['new_paras'] = ['V_HYPPIÄ']
            else:
                fail_guess_because(wordmap, ['V', 61, 'B'],
                        ['a'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('ttia'):
                wordmap['new_paras'] = ['V_MOITTIA']
            elif wordmap['lemma'].endswith('ttiä'):
                wordmap['new_paras'] = ['V_MIETTIÄ']
            else:
                fail_guess_because(wordmap, ['V', 61, 'C'],
                        ['a'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('kia'):
                wordmap['new_paras'] = ['V_KUKKIA']
            elif wordmap['lemma'].endswith('kiä'):
                wordmap['new_paras'] = ['V_SÖRKKIÄ']
            else:
                fail_guess_because(wordmap, ['V', 61, 'D'],
                        ['a'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('pia'):
                wordmap['new_paras'] = ['V_RAAPIA']
            elif wordmap['lemma'].endswith('piä'):
                wordmap['new_paras'] = ['V_RIIPIÄ']
            else:
                fail_guess_because(wordmap, ['V', 61, 'E'],
                        ['a'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('tia'):
                wordmap['new_paras'] = ['V_AHNEHTIA']
            elif wordmap['lemma'].endswith('tiä'):
                wordmap['new_paras'] = ['V_EHTIÄ']
            else:
                fail_guess_because(wordmap, ['V', 61, 'F'],
                        ['a'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('nkia'):
                wordmap['new_paras'] = ['V_ONKIA']
            elif wordmap['lemma'].endswith('nkiä'):
                wordmap['new_paras'] = ['V_MÖNKIÄ']
            else:
                fail_guess_because(wordmap, ['V', 61, 'G'],
                        ['a'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mpiä'):
                wordmap['new_paras'] = ['V_TYMPIÄ']
            else:
                fail_guess_because(wordmap, ['V', 61, 'H'],
                        ['a'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('ntia'):
                wordmap['new_paras'] = ['V_KONTIA']
            else:
                fail_guess_because(wordmap, ['V', 61, 'J'],
                        ['a'])
        elif wordmap['kotus_av'] == 'L':
            if wordmap['lemma'].endswith('kiä'):
                wordmap['new_paras'] = ['V_HYLKIÄ']
            else:
                fail_guess_because(wordmap, ['V', 61, 'L'],
                        ['a'])
        else:
            fail_guess_because(wordmap, ['V', 61],
                    [False])
    elif tn == 62:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ida'):
                wordmap['new_paras'] = ['V_KOPIOIDA']
            elif wordmap['lemma'].endswith('idä'):
                wordmap['new_paras'] = ['V_ÖYKKÄRÖIDÄ']
            else:
                fail_guess_because(wordmap, ['V', 62, False],
                        ['ida', 'idä'])
        else:
            fail_guess_because(wordmap, ['V', 62],
                    [False])
    elif tn == 63:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aada'):
                wordmap['new_paras'] = ['V_SAADA']
            elif wordmap['lemma'].endswith('yydä'):
                wordmap['new_paras'] = ['V_MYYDÄ']
            elif wordmap['lemma'].endswith('äädä'):
                wordmap['new_paras'] = ['V_JÄÄDÄ']
            else:
                fail_guess_because(wordmap, ['V', 63, False],
                        ['kka', 'kkä'])
        else:
            fail_guess_because(wordmap, ['V', 63],
                    [False])
    elif tn == 64:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('iedä'):
                wordmap['new_paras'] = ['V_VIEDÄ']
            elif wordmap['lemma'].endswith('uoda'):
                wordmap['new_paras'] = ['V_TUODA']
            elif wordmap['lemma'].endswith('yödä'):
                wordmap['new_paras'] = ['V_SYÖDÄ']
            else:
                fail_guess_because(wordmap, ['V', 64, False],
                        ['oa', 'ea', 'eä'])
        else:
            fail_guess_because(wordmap, ['V', 64],
                    [False])
    elif tn == 65:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('käydä'):
                wordmap['new_paras'] = ['V_KÄYDÄ']
            else:
                fail_guess_because(wordmap, ['V', 65, False],
                        ['back'])
        else:
            fail_guess_because(wordmap, ['V', 65],
                    ['H'])
    elif tn == 66:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ta'):
                wordmap['new_paras'] = ['V_MARISTA']
            elif wordmap['lemma'].endswith('tä'):
                wordmap['new_paras'] = ['V_ÄRISTÄ']
            else:
                fail_guess_because(wordmap, ['V', 66, False],
                        ['ta', 'tä'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('vista'):
                wordmap['new_paras'] = ['V_VAVISTA']
            elif wordmap['lemma'].endswith('väistä'):
                wordmap['new_paras'] = ['V_HÄVÄISTÄ']
            else:
                fail_guess_because(wordmap, ['V', 66, False],
                        ['vista', 'väistä'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('ngaista'):
                wordmap['new_paras'] = ['V_RANGAISTA']
            else:
                fail_guess_because(wordmap, ['V', 66, False],
                        ['gaista'])
        else:
            fail_guess_because(wordmap, ['V', 66],
                    [False])
    elif tn == 67:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('rra'):
                wordmap['new_paras'] = ['V_SURRA']
            elif wordmap['lemma'].endswith('lla'):
                wordmap['new_paras'] = ['V_VASTAILLA']
            elif wordmap['lemma'].endswith('llä'):
                wordmap['new_paras'] = ['V_ÄKSYILLÄ']
            elif wordmap['lemma'].endswith('nna'):
                wordmap['new_paras'] = ['V_PANNA']
            elif wordmap['lemma'].endswith('nnä'):
                wordmap['new_paras'] = ['V_MENNÄ']
            elif wordmap['lemma'].endswith('rrä'):
                wordmap['new_paras'] = ['V_PIERRÄ']
            else:
                fail_guess_because(wordmap, ['V', 67, False],
                        ['rra', 'rrä'])
        elif wordmap['kotus_av'] in ['A', 'D']:
            if wordmap['lemma'].endswith('ella'):
                wordmap['new_paras'] = ['V_NAKELLA']
            elif wordmap['lemma'].endswith('ellä'):
                wordmap['new_paras'] = ['V_LEIKELLÄ']
            else:
                fail_guess_because(wordmap, ['V', 67, 'A'],
                        ['a'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('pella'):
                wordmap['new_paras'] = ['V_TAPELLA']
            elif wordmap['lemma'].endswith('pellä'):
                wordmap['new_paras'] = ['V_HYPELLÄ']
            else:
                fail_guess_because(wordmap, ['V', 67, 'B'],
                        ['a'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tella'):
                wordmap['new_paras'] = ['V_SULATELLA']
            elif wordmap['lemma'].endswith('tellä'):
                wordmap['new_paras'] = ['V_HERÄTELLÄ']
            else:
                fail_guess_because(wordmap, ['V', 67, 'C'],
                        ['a'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('della'):
                wordmap['new_paras'] = ['V_TIPAHDELLA']
            elif wordmap['lemma'].endswith('dellä'):
                wordmap['new_paras'] = ['V_SÄPSÄHDELLÄ']
            else:
                fail_guess_because(wordmap, ['V', 67, 'F'],
                        ['a'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mmella'):
                wordmap['new_paras'] = ['V_OMMELLA']
            else:
                fail_guess_because(wordmap, ['V', 67, 'H'],
                        ['a'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('llella'):
                wordmap['new_paras'] = ['V_VAELLELLA']
            elif wordmap['lemma'].endswith('llellä'):
                wordmap['new_paras'] = ['V_KIILLELLÄ']
            else:
                fail_guess_because(wordmap, ['V', 67, 'I'],
                        ['a'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nnella'):
                wordmap['new_paras'] = ['V_KOMENNELLA']
            elif wordmap['lemma'].endswith('nnellä'):
                wordmap['new_paras'] = ['V_KÄÄNNELLÄ']
            else:
                fail_guess_because(wordmap, ['V', 67, 'J'],
                        ['a'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rrella'):
                wordmap['new_paras'] = ['V_NAKERRELLA']
            elif wordmap['lemma'].endswith('rrellä'):
                wordmap['new_paras'] = ['V_KIHERRELLÄ']
            else:
                fail_guess_because(wordmap, ['V', 67, 'K'],
                        ['a'])
        else:
            fail_guess_because(wordmap, ['V', 18],
                    [False])
    elif tn == 68:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('oida'):
                wordmap['new_paras'] = ['V_MELLAKOIDA']
            elif wordmap['lemma'].endswith('öidä'):
                wordmap['new_paras'] = ['V_ISÄNNÖIDÄ']
            else:
                fail_guess_because(wordmap, ['V', 68, False],
                        ['a'])
        else:
            fail_guess_because(wordmap, ['V', 68],
                    [False])
    elif tn == 69:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ita'):
                wordmap['new_paras'] = ['V_PALKITA']
            elif wordmap['lemma'].endswith('itä'):
                wordmap['new_paras'] = ['V_MERKITÄ']
            else:
                fail_guess_because(wordmap, ['V', 69, False],
                        ['a'])
        else:
            fail_guess_because(wordmap, ['V', 69],
                    [False])
    elif tn == 70:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('sta'):
                wordmap['new_paras'] = ['V_JUOSTA']
            elif wordmap['lemma'].endswith('stä'):
                wordmap['new_paras'] = ['V_PIESTÄ']
            else:
                fail_guess_because(wordmap, ['V', 70, False],
                        ['back', 'front'])
        else:
            fail_guess_because(wordmap, ['V', 70],
                    [False])
    elif tn == 71:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('hdä'):
                wordmap['new_paras'] = ['V_NÄHDÄ']
            else:
                fail_guess_because(wordmap, ['V', 71, False],
                        ['back', 'front'])
        else:
            fail_guess_because(wordmap, ['V', 71],
                    [False])
    elif tn == 72:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ta'):
                wordmap['new_paras'] = ['V_KARHETA']
            elif wordmap['lemma'].endswith('tä'):
                wordmap['new_paras'] = ['V_VÄHETÄ']
            else:
                fail_guess_because(wordmap, ['V', 72, False],
                    ['back', 'front'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('keta'):
                wordmap['new_paras'] = ['V_NIUKETA']
            elif wordmap['lemma'].endswith('kota'):
                wordmap['new_paras'] = ['V_ULOTA']
            elif wordmap['lemma'].endswith('ketä'):
                wordmap['new_paras'] = ['V_JYRKETÄ']
            else:
                fail_guess_because(wordmap, ['V', 72, 'A'],
                    ['back', 'front'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('peta'):
                wordmap['new_paras'] = ['V_SUPETA']
            elif wordmap['lemma'].endswith('petä'):
                wordmap['new_paras'] = ['V_TYLPETÄ']
            elif wordmap['lemma'].endswith('pota'):
                wordmap['new_paras'] = ['V_HELPOTA']
            elif wordmap['lemma'].endswith('pata'):
                wordmap['new_paras'] = ['V_HAPATA']
            else:
                fail_guess_because(wordmap, ['V', 72, 'B'],
                    ['peta', 'petä', 'pata', 'pota'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tota'):
                wordmap['new_paras'] = ['V_LOITOTA']
            else:
                fail_guess_because(wordmap, ['V', 72, 'C'],
                    ['back', 'front'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('ota'):
                wordmap['new_paras'] = ['V_ULOTA']
            elif wordmap['lemma'].endswith('ata'):
                wordmap['new_paras'] = ['V_ERATA']
            elif wordmap['lemma'].endswith('eta'):
                wordmap['new_paras'] = ['V_NIUKETA']
            elif wordmap['lemma'].endswith('etä'):
                wordmap['new_paras'] = ['V_JYRKETÄ']
            else:
                fail_guess_because(wordmap, ['V', 72, 'D'],
                    ['back', 'front'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('veta'):
                wordmap['new_paras'] = ['V_KAVETA']
            else:
                fail_guess_because(wordmap, ['V', 72, 'E'],
                    ['back', 'front'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('dota'):
                wordmap['new_paras'] = ['V_LEUDOTA']
            elif wordmap['lemma'].endswith('detä'):
                wordmap['new_paras'] = ['V_PIDETÄ']
            elif wordmap['lemma'].endswith('dätä'):
                wordmap['new_paras'] = ['V_MÄDÄTÄ']
            else:
                fail_guess_because(wordmap, ['V', 72, 'F'],
                    ['back', 'front'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mmetä'):
                wordmap['new_paras'] = ['V_LÄMMETÄ']
            else:
                fail_guess_because(wordmap, ['V', 72, 'H'],
                    ['back', 'front'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nnetä'):
                wordmap['new_paras'] = ['V_KIINNETÄ']
            else:
                fail_guess_because(wordmap, ['V', 72, 'I'],
                    ['nnetä'])
        elif wordmap['kotus_av'] == 'L':
            if wordmap['lemma'].endswith('jeta'):
                wordmap['new_paras'] = ['V_JULJETA']
            elif wordmap['lemma'].endswith('jetä'):
                wordmap['new_paras'] = ['V_ILJETÄ']
            else:
                fail_guess_because(wordmap, ['V', 72, 'L'],
                    ['back', 'front'])
        else:
            fail_guess_because(wordmap, ['V', 72],
                [False, 'A-L'])
    elif wordmap['kotus_tn'] == 73:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ata'):
                wordmap['new_paras'] = ['V_ARVATA']
            elif wordmap['lemma'].endswith('ätä'):
                wordmap['new_paras'] = ['V_YNNÄTÄ']
            else:
                fail_guess_because(wordmap, ['V', 73, False],
                        ['ata', 'ätä'])
        elif wordmap['kotus_av'] in ['A', 'D']:
            if wordmap['lemma'].endswith('ata'):
                wordmap['new_paras'] = ['V_MORKATA']
            elif wordmap['lemma'].endswith('ätä'):
                wordmap['new_paras'] = ['V_YÖKÄTÄ']
            else:
                fail_guess_because(wordmap, ['V', 73, 'A'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('pata'):
                wordmap['new_paras'] = ['V_SIEPATA']
            elif wordmap['lemma'].endswith('pätä'):
                wordmap['new_paras'] = ['V_VÄLPÄTÄ']
            else:
                fail_guess_because(wordmap, ['V', 73, 'B'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tata'):
                wordmap['new_paras'] = ['V_LUNTATA']
            elif wordmap['lemma'].endswith('tätä'):
                wordmap['new_paras'] = ['V_LÄNTÄTÄ']
            else:
                fail_guess_because(wordmap, ['V', 73, 'C'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('vata'):
                wordmap['new_paras'] = ['V_KAIVATA']
            elif wordmap['lemma'].endswith('vätä'):
                wordmap['new_paras'] = ['V_LEVÄTÄ']
            else:
                fail_guess_because(wordmap, ['V', 73, 'E'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('data'):
                wordmap['new_paras'] = ['V_JAHDATA']
            elif wordmap['lemma'].endswith('dätä'):
                wordmap['new_paras'] = ['V_TÄHDÄTÄ']
            else:
                fail_guess_because(wordmap, ['V', 73, 'F'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('gata'):
                wordmap['new_paras'] = ['V_VONGATA']
            elif wordmap['lemma'].endswith('gätä'):
                wordmap['new_paras'] = ['V_VÄNGÄTÄ']
            else:
                fail_guess_because(wordmap, ['V', 73, 'G'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mmata'):
                wordmap['new_paras'] = ['V_TEMMATA']
            else:
                fail_guess_because(wordmap, ['V', 73, 'H'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('llata'):
                wordmap['new_paras'] = ['V_MULLATA']
            else:
                fail_guess_because(wordmap, ['V', 73, 'I'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nnata'):
                wordmap['new_paras'] = ['V_SUUNNATA']
            elif wordmap['lemma'].endswith('nnätä'):
                wordmap['new_paras'] = ['V_RYNNÄTÄ']
            else:
                fail_guess_because(wordmap, ['V', 73, 'J'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rata'):
                wordmap['new_paras'] = ['V_VERRATA']
            else:
                fail_guess_because(wordmap, ['V', 73, 'K'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'L':
            if wordmap['lemma'].endswith('jätä'):
                wordmap['new_paras'] = ['V_HYLJÄTÄ']
            else:
                fail_guess_because(wordmap, ['V', 73, 'K'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'O':
            if wordmap['lemma'].endswith('gata'):
                wordmap['new_paras'] = ['V_DIGATA']
            else:
                fail_guess_because(wordmap, ['V', 73, 'N'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'P':
            if wordmap['lemma'].endswith('bata'):
                wordmap['new_paras'] = ['V_LOBATA']
            else:
                fail_guess_because(wordmap, ['V', 73, 'P'],
                        ['hapan'])
        else:
            fail_guess_because(wordmap, ['V', 73], [False, 'A-P'])
    elif wordmap['kotus_tn'] == 74:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ta'):
                wordmap['new_paras'] = ['V_KARHUTA']
            elif wordmap['lemma'].endswith('tä'):
                wordmap['new_paras'] = ['V_TÄHYTÄ']
            else:
                fail_guess_because(wordmap, ['V', 74, False],
                        ['ton'])
        elif wordmap['kotus_av'] in ['A', 'D']:
            if wordmap['lemma'].endswith('ota'):
                wordmap['new_paras'] = ['V_KAIKOTA']
            elif wordmap['lemma'].endswith('eta'):
                wordmap['new_paras'] = ['V_POIKETA']
            elif wordmap['lemma'].endswith('etä'):
                wordmap['new_paras'] = ['V_KERETÄ']
            elif wordmap['lemma'].endswith('uta'):
                wordmap['new_paras'] = ['V_KOUKUTA']
            else:
                fail_guess_because(wordmap, ['V', 74, 'A'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('puta'):
                wordmap['new_paras'] = ['V_PULPUTA']
            elif wordmap['lemma'].endswith('pota'):
                wordmap['new_paras'] = ['V_UPOTA']
            else:
                fail_guess_because(wordmap, ['V', 74, 'B'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tota'):
                wordmap['new_paras'] = ['V_LOTOTA']
            elif wordmap['lemma'].endswith('tuta'):
                wordmap['new_paras'] = ['V_LUUTUTA']
            else:
                fail_guess_because(wordmap, ['V', 74, 'C'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'E':
            if wordmap['lemma'].endswith('vuta'):
                wordmap['new_paras'] = ['V_KIVUTA']
            elif wordmap['lemma'].endswith('veta'):
                wordmap['new_paras'] = ['V_KORVETA']
            elif wordmap['lemma'].endswith('vetä'):
                wordmap['new_paras'] = ['V_REVETÄ']
            elif wordmap['lemma'].endswith('vota'):
                wordmap['new_paras'] = ['V_KIRVOTA']
            else:
                fail_guess_because(wordmap, ['V', 74, 'E'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('duta'):
                wordmap['new_paras'] = ['V_LIIDUTA']
            elif wordmap['lemma'].endswith('deta'):
                wordmap['new_paras'] = ['V_TODETA']
            elif wordmap['lemma'].endswith('dota'):
                wordmap['new_paras'] = ['V_VAAHDOTA']
            elif wordmap['lemma'].endswith('detä'):
                wordmap['new_paras'] = ['V_VYYHDETÄ']
            else:
                fail_guess_because(wordmap, ['V', 74, 'F'],
                        ['deta', 'detä', 'dota', 'duta'])
        elif wordmap['kotus_av'] == 'G':
            if wordmap['lemma'].endswith('geta'):
                wordmap['new_paras'] = ['V_TUNGETA']
            elif wordmap['lemma'].endswith('gota'):
                wordmap['new_paras'] = ['V_PINGOTA']
            elif wordmap['lemma'].endswith('getä'):
                wordmap['new_paras'] = ['V_ÄNGETÄ']
            else:
                fail_guess_because(wordmap, ['V', 74, 'G'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mmuta'):
                wordmap['new_paras'] = ['V_KUMMUTA']
            elif wordmap['lemma'].endswith('mmeta'):
                wordmap['new_paras'] = ['V_KAMMETA']
            elif wordmap['lemma'].endswith('mmota'):
                wordmap['new_paras'] = ['V_SAMMOTA']
            else:
                fail_guess_because(wordmap, ['V', 74, 'H'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'J':
            if wordmap['lemma'].endswith('nnota'):
                wordmap['new_paras'] = ['V_INNOTA']
            else:
                fail_guess_because(wordmap, ['V', 74, 'J'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'K':
            if wordmap['lemma'].endswith('rrota'):
                wordmap['new_paras'] = ['V_IRROTA']
            else:
                fail_guess_because(wordmap, ['V', 74, 'K'],
                        ['hapan'])
        elif wordmap['kotus_av'] == 'L':
            if wordmap['lemma'].endswith('jeta'):
                wordmap['new_paras'] = ['V_HALJETA']
            elif wordmap['lemma'].endswith('jetä'):
                wordmap['new_paras'] = ['V_ILJETÄ']
            else:
                fail_guess_because(wordmap, ['V', 74, 'K'],
                        ['hapan'])
        else:
            fail_guess_because(wordmap, ['V', 74], [False, 'A-K'])
    elif wordmap['kotus_tn'] == 75:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ta'):
                wordmap['new_paras'] = ['V_LASSOTA']
            elif wordmap['lemma'].endswith('tä'):
                wordmap['new_paras'] = ['V_SELVITÄ']
            else:
                fail_guess_because(wordmap, ['V', 75, False],
                        ['ta', 'tä'])
        elif wordmap['kotus_av'] == 'B':
            if wordmap['lemma'].endswith('pytä'):
                wordmap['new_paras'] = ['V_RYÖPYTÄ']
            else:
                fail_guess_because(wordmap, ['V', 75, 'B'],
                        ['ton'])
        elif wordmap['kotus_av'] == 'C':
            if wordmap['lemma'].endswith('tota'):
                wordmap['new_paras'] = ['V_PEITOTA']
            else:
                fail_guess_because(wordmap, ['V', 75, 'C'],
                        ['ton'])
        elif wordmap['kotus_av'] == 'D':
            if wordmap['lemma'].endswith('itä'):
                wordmap['new_paras'] = ['V_KERITÄ']
            else:
                fail_guess_because(wordmap, ['V', 75, 'D'],
                        ['ton'])
        elif wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('dota'):
                wordmap['new_paras'] = ['V_MUODOTA']
            else:
                fail_guess_because(wordmap, ['V', 75, 'E'],
                        ['ton'])
        elif wordmap['kotus_av'] == 'H':
            if wordmap['lemma'].endswith('mmitä'):
                wordmap['new_paras'] = ['V_LÄMMITÄ']
            else:
                fail_guess_because(wordmap, ['V', 75, 'H'],
                        ['ton'])
        elif wordmap['kotus_av'] == 'I':
            if wordmap['lemma'].endswith('llitä'):
                wordmap['new_paras'] = ['V_HELLITÄ']
            elif wordmap['lemma'].endswith('llota'):
                wordmap['new_paras'] = ['V_AALLOTA']
            else:
                fail_guess_because(wordmap, ['V', 75, 'I'],
                        ['ton'])
        else:
            fail_guess_because(wordmap, ['V', 75],
                [False, 'B', 'D', 'F', 'H', 'I' ])
    elif wordmap['kotus_tn'] == 76:
        if wordmap['kotus_av'] == 'F':
            if wordmap['lemma'].endswith('taa'):
                wordmap['new_paras'] = ['V_TAITAA']
            elif wordmap['lemma'].endswith('tää'):
                wordmap['new_paras'] = ['V_TIETÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 76, 'F'],
                    ['front', 'back'])
        else:
            fail_guess_because(wordmap, ['V', 76],
                ['F'])
    elif wordmap['kotus_tn'] == 77:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aa'):
                wordmap['new_paras'] = ['V_VIPAJAA']
            elif wordmap['lemma'].endswith('ää'):
                wordmap['new_paras'] = ['V_HELÄJÄÄ']
            else:
                fail_guess_because(wordmap, ['V', 77, False],
                    ['vasen'])
        else:
            fail_guess_because(wordmap, ['V', 77],
                [False], "cannot have gradation")
    elif wordmap['kotus_tn'] == 78:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('aa'):
                wordmap['new_paras'] = ['V_RAIKAA']
            elif wordmap['lemma'].endswith('ää'):
                wordmap['new_paras'] = ['V_ÄHKÄÄ']
            elif wordmap['lemma'].endswith('ata'):
                wordmap['new_paras'] = ['V_HALAJAA']
            else:
                fail_guess_because(wordmap, ['V', 78, False],
                    ['aa', 'ää', 'ata'])
        elif wordmap['kotus_av'] == 'A':
            if wordmap['lemma'].endswith('kkaa'):
                wordmap['new_paras'] = ['V_TUIKKAA']
            else:
                fail_guess_because(wordmap, ['V', 78, 'A'],
                    ['kkaa'])
        else:
            fail_guess_because(wordmap, ['V', 78],
                [False, 'A'])
    elif tn == 99:
        wordmap['new_paras'] = ['#']
    elif tn == 1067:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('olla'):
                wordmap['new_paras'] = ['V_OLLA']
            else:
                fail_guess_because(wordmap, ['V', 10, 'D', 'OLLA'],
                        ['olla'], 'must be olla')
    elif tn == 1099:
        if not wordmap['kotus_av']:
            if wordmap['lemma'].endswith('ei'):
                wordmap['new_paras'] = ['V_EI']
            else:
                fail_guess_because(wordmap, ['V', 99, 'D', 'EI'],
                        ['ei'], 'must be ei')
    else:
        fail_guess_because(wordmap, ['V'],
            ['52-78', '99', '1067'])
    return wordmap

def guess_new_acro(wordmap):
    if wordmap['lemma'][-1] == '1':
        wordmap['new_paras'] = ['ACRO_YKSI']
    elif wordmap['lemma'][-1] == '2':
        wordmap['new_paras'] = ['ACRO_KAKSI']
    elif wordmap['lemma'][-1] == '3':
        wordmap['new_paras'] = ['ACRO_KOLME']
    elif wordmap['lemma'][-1] == '4':
        wordmap['new_paras'] = ['ACRO_NELJÄ']
    elif wordmap['lemma'][-1] == '5':
        wordmap['new_paras'] = ['ACRO_VIISI']
    elif wordmap['lemma'][-1] == '6':
        wordmap['new_paras'] = ['ACRO_KUUSI']
    elif wordmap['lemma'][-1] == '7':
        wordmap['new_paras'] = ['ACRO_SEITSEMÄN']
    elif wordmap['lemma'][-1] == '8':
        wordmap['new_paras'] = ['ACRO_KAHDEKSAN']
    elif wordmap['lemma'][-1] == '9':
        wordmap['new_paras'] = ['ACRO_YHDEKSÄN']
    elif wordmap['lemma'][-1] == '0':
        wordmap['new_paras'] = ['ACRO_NOLLA']
    elif wordmap['lemma'][-1] in ['a', 'A']:
        wordmap['new_paras'] = ['ACRO_AA']
    elif wordmap['lemma'][-1] in ['b', 'B', 'C', 'c', 'd', 'D', 'e', 'E', 'g', 'G', 'p', 'P', 't', 'T', 'v', 'V', 'w', 'W']:
        wordmap['new_paras'] = ['ACRO_EE']
    elif wordmap['lemma'][-1] in ['f', 'F', 'l' , 'L', 'm', 'M', 'n', 'N', 'r', 'R', 's', 'S', 'x', 'X', 'š', 'Š', 'ž', 'Ž']:
        wordmap['new_paras'] = ['ACRO_ÄKS']
    elif wordmap['lemma'][-1] in ['h', 'H', 'k', 'K', 'o', 'O', 'å', 'Å']:
        wordmap['new_paras'] = ['ACRO_OO']
    elif wordmap['lemma'][-1] in ['i', 'I', 'j', 'J']:
        wordmap['new_paras'] = ['ACRO_II']
    elif wordmap['lemma'][-1] in ['q', 'Q', 'u', 'U']:
        wordmap['new_paras'] = ['ACRO_UU']
    elif wordmap['lemma'][-1] in ['y', 'Y', 'ü', 'Ü']:
        wordmap['new_paras'] = ['ACRO_YY']
    elif wordmap['lemma'][-1] in ['z', 'Z']:
        wordmap['new_paras'] = ['ACRO_ZET']
    elif wordmap['lemma'][-1] in ['ä', 'Ä']:
        wordmap['new_paras'] = ['ACRO_ÄÄ']
    elif wordmap['lemma'][-1] in ['ö', 'Ö']:
        wordmap['new_paras'] = ['ACRO_ÖÖ']
    elif wordmap['lemma'][-1] == '€':
        wordmap['new_paras'] = ['ACRO_EURO']
    elif wordmap['lemma'][-1] == 'Ω':
        wordmap['new_paras'] = ['ACRO_OHMI']
    elif wordmap['lemma'][-1] in ['¢', '¥']:
        wordmap['new_paras'] = ['ACRO_SENTTI']
    elif wordmap['lemma'][-1] == '$':
        wordmap['new_paras'] = ['ACRO_DOLLARI']
    elif wordmap['lemma'][-1] in ['£', '₤']:
        wordmap['new_paras'] = ['ACRO_PUNTA']
    if wordmap['kotus_tn'] == 1:
        if wordmap['stem_vowel'] == 'o':
            wordmap['new_paras'] += 'ACRO_TALO'
        else:
            fail_guess_because(wordmap, ['ACRO', '1'], ['o'])
    elif wordmap['kotus_tn'] == 6:
        if wordmap['harmony'] == 'back':
            wordmap['new_paras'] += 'ACRO_DOLLARI'
        else:
            fail_guess_because(wordmap, ['ACRO', '6'], ['back'])
    elif wordmap['kotus_tn'] == 99:
        fail_guess_because(wordmap, ['ACRO'], ['!99'],
                'ACROnyms should be classified according to last inflecting '
                'word')
    else:
        fail_guess_because(wordmap, ['ACRO'], ['1'],
                'Not implemented acro classes yet')
    return wordmap

def guess_new_pronoun(wordmap):
    # FIXME:
    #fail_guess_because(wordmap, ['Num'], [], "Not impl Num")
    wordmap['new_paras'] = ['#']
    return wordmap

def guess_new_numeral(wordmap):
    # FIXME:
    #fail_guess_because(wordmap, ['Num'], [], "Not impl Num")
    wordmap['new_paras'] = ['#']
    return wordmap

def guess_new_particle(wordmap):
    if not wordmap['particle']:
        wordmap['new_paras'] = ['#']
    elif wordmap['particle'] == 'ADVERB':
        wordmap = guess_new_adverb(wordmap)
    elif wordmap['particle'] == 'ADPOSITION':
        wordmap = guess_new_adposition(wordmap)
    else:
        if wordmap['possessive']:
            if wordmap['harmony'] == 'front':
                if wordmap['lemma'].endswith('e'):
                    wordmap['new_paras'] = ['PCLE_FRONT_POSS_EN_OPT']
                elif wordmap['lemma'].endswith('ä'):
                    wordmap['new_paras'] = ['PCLE_FRONT_POSS_ÄN_OPT']
                else:
                    wordmap['new_paras'] = ['PCLE_FRONT_POSS_OPT']
            elif wordmap['harmony'] == 'back':
                if wordmap['lemma'].endswith('a'):
                    wordmap['new_paras'] = ['PCLE_BACK_POSS_AN_OPT']
                elif wordmap['lemma'].endswith('e'):
                    wordmap['new_paras'] = ['PCLE_BACK_POSS_EN_OPT']
                else:
                    wordmap['new_paras'] = ['PCLE_BACK_POSS_OPT']
            else:
                fail_guess_because(wordmap, ["PCLE", "POSS"],
                        ["front", "back"])
        elif wordmap['clitics']:
            if wordmap['harmony'] == 'front':
                wordmap['new_paras'] = ['PCLE_FRONT_CLIT_OPT']
            elif wordmap['harmony'] == 'back':
                wordmap['new_paras'] = ['PCLE_BACK_CLIT_OPT']
            else:
                fail_guess_because(wordmap, ["PCLE", "CLIT"],
                        ["front", "back"])
        else:
            wordmap['new_paras'] = ['#']
    return wordmap

def guess_new_adverb(wordmap):
    if wordmap['possessive']:
        if wordmap['harmony'] == 'front':
            if wordmap['lemma'].endswith('e'):
                wordmap['new_paras'] = ['ADV_FRONT_POSS_EN_OPT']
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_paras'] = ['ADV_FRONT_POSS_ÄN_OPT']
            else:
                wordmap['new_paras'] = ['ADV_FRONT_POSS_OPT']
        elif wordmap['harmony'] == 'back':
            if wordmap['lemma'].endswith('a'):
                wordmap['new_paras'] = ['ADV_BACK_POSS_AN_OPT']
            elif wordmap['lemma'].endswith('e'):
                wordmap['new_paras'] = ['ADV_BACK_POSS_EN_OPT']
            else:
                wordmap['new_paras'] = ['ADV_BACK_POSS_OPT']
        else:
            fail_guess_because(wordmap, ["ADV", "POSS"], ["front", "back"])
    elif wordmap['clitics']:
        if wordmap['harmony'] == 'front':
            wordmap['new_paras'] = ['ADV_FRONT_CLIT_OPT']
        elif wordmap['harmony'] == 'back':
            wordmap['new_paras'] = ['ADV_BACK_CLIT_OPT']
        else:
            fail_guess_because(wordmap, ["ADV", "POSS"], ["front", "back"])
    else:
        wordmap['new_paras'] = ['#']
    return wordmap

def guess_new_adposition(wordmap):
    if wordmap['possessive']:
        if wordmap['harmony'] == 'front':
            if wordmap['lemma'].endswith('e'):
                wordmap['new_paras'] = ['ADP_FRONT_POSS_EN_OPT']
            elif wordmap['lemma'].endswith('ä'):
                wordmap['new_paras'] = ['ADP_FRONT_POSS_ÄN_OPT']
            else:
                wordmap['new_paras'] = ['ADP_FRONT_POSS_OPT']
        elif wordmap['harmony'] == 'back':
            if wordmap['lemma'].endswith('a'):
                wordmap['new_paras'] = ['ADP_BACK_POSS_AN_OPT']
            elif wordmap['lemma'].endswith('e'):
                wordmap['new_paras'] = ['ADP_BACK_POSS_EN_OPT']
            else:
                wordmap['new_paras'] = ['ADP_BACK_POSS_OPT']
        else:
            fail_guess_because(wordmap, ["ADP", "POSS"], ["front", "back"])
    elif wordmap['clitics']:
        if wordmap['harmony'] == 'front':
            wordmap['new_paras'] = ['ADP_FRONT_CLIT_OPT']
        elif wordmap['harmony'] == 'back':
            wordmap['new_paras'] = ['ADP_BACK_CLIT_OPT']
        else:
            fail_guess_because(wordmap, ["ADP", "CLIT"], ["front", "back"])
    else:
        wordmap['new_paras'] = ['#']
    return wordmap
