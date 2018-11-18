#!/usr/bin/env python3

from ..error_logging import fail_guess_because
from ..string_manglers import mangle_suffixes_or_die


def stub_all_new_para(wordmap, stubmap):
    if not wordmap['new_para']:
        return wordmap
    if not wordmap['new_para'] in stubmap:
        fail_guess_because(wordmap, "", wordmap['new_para'],
                           "Missing stub paradigm" +
                           ": Update stub-deletions.tsv and carry on")
        return None
    elif not stubmap[wordmap['new_para']] or \
            stubmap[wordmap['new_para']] == '':
        return wordmap
    wordmap = mangle_suffixes_or_die(wordmap, [stubmap[wordmap['new_para']]])
    return wordmap


def stub_all_ktn(wordmap):
    '''Generate unmodifiable stub for inflectional processes.
    this cuts every morphologically varying character.
    '''
    if not wordmap['kotus_tn']:
        return wordmap
    if wordmap['pos'] == 'ACRONYM':
        return wordmap
    tn = int(wordmap['kotus_tn'])
    if not wordmap['kotus_av'] or tn in [28, 60, 1007, 1009, 1010]:
        if tn in [1, 2, 3, 4, 8, 21, 22, 48]:
            pass
        elif tn in [5, 6]:
            if wordmap['stub'].endswith('i'):
                wordmap = mangle_suffixes_or_die(wordmap, ['i'])
            else:
                pass
        elif tn == 10:
            if wordmap['stub'].endswith('n'):
                wordmap = mangle_suffixes_or_die(wordmap, ['an', 'än'])
            elif not wordmap['stub'].endswith('A'):
                wordmap = mangle_suffixes_or_die(wordmap, ['a', 'ä', 'ă'])
        elif tn == 41 and wordmap['pos'] == 'ADJECTIVE'  \
                and (wordmap['stub'].endswith('is') or
                     wordmap['stub'].endswith('paras')):
            wordmap = mangle_suffixes_or_die(wordmap, ['is', 'as'])
        elif tn == 7:
            wordmap = mangle_suffixes_or_die(wordmap, ['i'])
        elif tn in range(9, 16):
            if not wordmap['stub'].endswith('A'):
                wordmap = mangle_suffixes_or_die(wordmap, ['a', 'ä', 'e'])
        elif tn in [16, 23, 24, 26]:
            wordmap = mangle_suffixes_or_die(wordmap, ['i'])
        elif tn in [17, 18, 20]:
            wordmap = mangle_suffixes_or_die(wordmap, ['a', 'e', 'i', 'o',
                                                       'u', 'y', 'ä', 'ö'])
        elif tn == 19:
            wordmap = mangle_suffixes_or_die(wordmap, ['uo', 'yö', 'ie'])
        elif tn == 25:
            wordmap = mangle_suffixes_or_die(wordmap, ['mi'])
        elif tn in [27, 28]:
            wordmap = mangle_suffixes_or_die(wordmap, ['si', 's'])
        elif tn == 29:
            wordmap = mangle_suffixes_or_die(wordmap, ['psi', 'ksi'])
        elif tn == 30:
            wordmap = mangle_suffixes_or_die(wordmap, ['tsi'])
        elif tn == 31:
            wordmap = mangle_suffixes_or_die(wordmap, ['ksi'])
        elif tn == 32:
            if wordmap['stub'].endswith('kymmenen'):
                wordmap = mangle_suffixes_or_die(wordmap, ['en'])
            else:
                pass
        elif tn in range(33, 38):
            wordmap = mangle_suffixes_or_die(wordmap, ['n'])
        elif tn == 38:
            wordmap = mangle_suffixes_or_die(wordmap, ['nen'])
        elif tn in [39, 41, 42]:
            wordmap = mangle_suffixes_or_die(wordmap, ['s'])
        elif tn == 40:
            wordmap = mangle_suffixes_or_die(wordmap, ['s', 't'])
        elif tn in [43, 44, 46]:
            wordmap = mangle_suffixes_or_die(wordmap, ['t'])
        elif tn == 45:
            wordmap = mangle_suffixes_or_die(wordmap, ['s'])
        elif tn == 47:
            wordmap = mangle_suffixes_or_die(wordmap, ['ut', 'yt'])
        elif tn == 49:
            if wordmap['stub'].endswith('e'):
                wordmap['extra_e'] = True
        elif tn == 52:
            wordmap['stub'] = wordmap['stub'][:-1]
        elif tn in [53, 56, 77]:
            wordmap['stub'] = wordmap['stub'][:-2]
        elif tn == 54:
            wordmap['stub'] = wordmap['stub'][:-3]
        elif tn in [55, 57, 76]:
            wordmap['stub'] = wordmap['stub'][:-3]
        elif tn == 58:
            wordmap['stub'] = wordmap['stub'][:-2]
        elif tn == 59:
            wordmap['stub'] = wordmap['stub'][:-3]
        elif tn == 60:
            wordmap['stub'] = wordmap['stub'][:-4]
        elif tn == 61:
            wordmap['stub'] = wordmap['stub'][:-2]
        elif tn in [62, 68]:
            wordmap['stub'] = wordmap['stub'][:-3]
        elif tn in [62, 63, 65]:
            wordmap['stub'] = wordmap['stub'][:-3]
        elif tn == 64:
            wordmap['stub'] = wordmap['stub'][:-4]
        elif tn == 67 and wordmap['stub'] in ['mennä', 'panna', 'tulla']:
            wordmap['stub'] = wordmap['stub'][:-3]
        elif tn == 67 and wordmap['stub'][-5:] in ['ailla', 'äillä', 'oilla',
                                                   'öillä']:
            wordmap['stub'] = wordmap['stub'][:-4]
        elif tn in [66, 67, 69, 72, 73, 74, 75]:
            wordmap['stub'] = wordmap['stub'][:-2]
        elif tn in [70, 71]:
            wordmap['stub'] = wordmap['stub'][:-3]
        elif tn == 78:
            wordmap = mangle_suffixes_or_die(wordmap, ['ta', 'tä', 'a', 'ä'])
        elif tn == 1007:
            wordmap = mangle_suffixes_or_die(wordmap, ['i'])
        elif tn == 1008:
            wordmap = mangle_suffixes_or_die(wordmap, ['e'])
        elif tn in [1010, 1009]:
            wordmap = mangle_suffixes_or_die(wordmap, ['ika', 'tkä'])
        elif tn in [1024, 1026]:
            wordmap = mangle_suffixes_or_die(wordmap, ['i'])
        elif tn == 1067:
            wordmap = mangle_suffixes_or_die(wordmap, ['olla'])
        elif tn == 1099:
            wordmap = mangle_suffixes_or_die(wordmap, ['ei'])
        elif wordmap['kotus_tn'] == 101:
            if wordmap['lemma'] in ['minä', 'sinä']:
                wordmap = mangle_suffixes_or_die(wordmap, ['nä'])
            elif wordmap['lemma'] == 'hän':
                pass
            elif wordmap['lemma'] in ['me', 'te', 'he']:
                pass
            elif wordmap['lemma'] == 'tämä':
                wordmap = mangle_suffixes_or_die(wordmap, ['mä'])
            elif wordmap['lemma'] == 'tuo':
                wordmap = mangle_suffixes_or_die(wordmap, ['uo'])
            elif wordmap['lemma'] == 'se':
                wordmap = mangle_suffixes_or_die(wordmap, ['e'])
            elif wordmap['lemma'] == 'nämä':
                wordmap = mangle_suffixes_or_die(wordmap, ['mä'])
            elif wordmap['lemma'] == 'nuo':
                wordmap = mangle_suffixes_or_die(wordmap, ['uo'])
            elif wordmap['lemma'] == 'ne':
                wordmap = mangle_suffixes_or_die(wordmap, ['e'])
            elif wordmap['lemma'] == 'joku':
                wordmap = mangle_suffixes_or_die(wordmap, ['ku'])
            elif wordmap['lemma'] == 'joka':
                wordmap = mangle_suffixes_or_die(wordmap, ['ka'])
            elif wordmap['lemma'] == 'jokin':
                wordmap = mangle_suffixes_or_die(wordmap, ['kin'])
            elif wordmap['lemma'] == 'jompikumpi':
                wordmap = mangle_suffixes_or_die(wordmap, ['pikumpi'])
            elif wordmap['lemma'] == 'kuka':
                wordmap = mangle_suffixes_or_die(wordmap, ['uka'])
            elif wordmap['lemma'] == 'kukaan':
                wordmap = mangle_suffixes_or_die(wordmap, ['ukaan'])
            elif wordmap['lemma'] == 'kukakin':
                wordmap = mangle_suffixes_or_die(wordmap, ['ukakin'])
            elif wordmap['lemma'].endswith('kukin'):
                wordmap = mangle_suffixes_or_die(wordmap, ['ukin'])
            elif wordmap['lemma'] == 'mikin':
                wordmap = mangle_suffixes_or_die(wordmap, ['kin'])
            elif wordmap['lemma'] == 'mikä':
                wordmap = mangle_suffixes_or_die(wordmap, ['kä'])
            elif wordmap['lemma'] == 'mikäkin':
                wordmap = mangle_suffixes_or_die(wordmap, ['käkin'])
            elif wordmap['lemma'] == 'mikään':
                wordmap = mangle_suffixes_or_die(wordmap, ['kään'])
            elif wordmap['lemma'] == 'missä':
                wordmap = mangle_suffixes_or_die(wordmap, ['ssä'])
            elif wordmap['lemma'] == 'missäkään':
                wordmap = mangle_suffixes_or_die(wordmap, ['ssäkään'])
            elif wordmap['lemma'] == 'missään':
                wordmap = mangle_suffixes_or_die(wordmap, ['ssään'])
            elif wordmap['lemma'] in ['muuan', 'muudan']:
                wordmap = mangle_suffixes_or_die(wordmap, ['n'])
            elif wordmap['lemma'] in ['mä', 'sä']:
                wordmap = mangle_suffixes_or_die(wordmap, ['ä'])
            elif wordmap['lemma'] in ['mie', 'sie']:
                wordmap = mangle_suffixes_or_die(wordmap, ['e'])
            elif wordmap['lemma'] == 'toi':
                wordmap = mangle_suffixes_or_die(wordmap, ['i'])
            elif wordmap['lemma'].endswith('ainoa'):
                wordmap = mangle_suffixes_or_die(wordmap, ['a'])
            elif wordmap['lemma'] == 'kumpikaan':
                wordmap = mangle_suffixes_or_die(wordmap, ['pikaan'])
            elif wordmap['lemma'].endswith('kumpikin'):
                wordmap = mangle_suffixes_or_die(wordmap, ['pikin'])
            elif wordmap['lemma'] in ['jota', 'kenkään', 'kuta', 'ma', 'mi',
                                      'missäkin', 'monta', 'montaa', 'sa',
                                      'tää', 'ken', 'koko']:
                pass
        elif wordmap['kotus_tn'] in [99, 999] and \
                wordmap['possessive'] == 'optional':
            if wordmap['stub'].endswith('den'):
                wordmap = mangle_suffixes_or_die(
                    wordmap, ['den'])  # näh|te| -mme
            elif wordmap['stub'].endswith('n'):
                wordmap = mangle_suffixes_or_die(
                    wordmap, ['n'])  # näkyvii|n -mme
            elif wordmap['stub'].endswith('i'):
                wordmap = mangle_suffixes_or_die(
                    wordmap, ['i'])  # vuoks|i -e-mme
        elif wordmap['kotus_tn'] in [99, 999] and \
                wordmap['possessive'] == 'obligatory':
            if wordmap['stub'].endswith('n'):
                wordmap['stub'] = wordmap['stub'][:-2]   # hyvillä|än -mme
            elif wordmap['stub'].endswith('nsa') or \
                    wordmap['stub'].endswith('nsä'):
                wordmap['stub'] = wordmap['stub'][:-3]   # aika|nsa -mme
        elif wordmap['kotus_tn'] in [0, 99, 999]:
            pass
        elif wordmap['kotus_tn'] == 1101:
            wordmap = mangle_suffixes_or_die(wordmap, ['ka', 'kä'])
        elif wordmap['kotus_tn'] == 51:
            wordmap['stub'] = ''
        else:
            fail_guess_because(wordmap, ['!av'], ['0-71', 999, 1007, 1010,
                                                  1009, 1024, 1026, 1067,
                                                  1099])
    elif wordmap['grade_dir'] == 'weaken':
        if wordmap['kotus_av'] == 'D' and wordmap['lemma'].endswith('uoka'):
            wordmap = mangle_suffixes_or_die(wordmap, ['oka'])
        elif wordmap['kotus_av'] in ['A', 'D', 'G', 'L', 'M']:
            if tn in [1, 2, 3, 4]:
                wordmap = mangle_suffixes_or_die(wordmap, ['ko', 'ku',
                                                           'ky', 'kö'])
            elif tn in [5, 6, 7]:
                wordmap = mangle_suffixes_or_die(wordmap, ['ki'])
            elif tn in [8]:
                wordmap = mangle_suffixes_or_die(wordmap, ['ke'])
            elif tn in [9, 10, 11, 12, 13, 14]:
                wordmap = mangle_suffixes_or_die(wordmap, ['ka', 'kä'])
            elif tn in range(52, 79):
                lastk = wordmap['stub'].rfind('k')
                wordmap['stub'] = wordmap['stub'][:lastk]
            else:
                fail_guess_because(wordmap, ['av-', 'A', 'D', 'G', 'L', 'M'],
                                   ['1-14'])
        elif wordmap['kotus_av'] in ['B', 'E', 'H']:
            if tn in [1, 2, 3, 4]:
                wordmap = mangle_suffixes_or_die(wordmap, ['po', 'pu',
                                                           'py', 'pö'])
            elif tn in [5, 6, 7, 16]:
                wordmap = mangle_suffixes_or_die(wordmap, ['pi'])
            elif tn in [8]:
                wordmap = mangle_suffixes_or_die(wordmap, ['pe'])
            elif tn in [9, 10, 11, 12, 13, 14]:
                wordmap = mangle_suffixes_or_die(wordmap, ['pa', 'pä'])
            elif tn in range(52, 79):
                lastp = wordmap['stub'].rfind('p')
                wordmap['stub'] = wordmap['stub'][:lastp]
            else:
                fail_guess_because(wordmap, ['av-', 'B', 'E', 'H'],
                                   ['1-14'])
        elif wordmap['kotus_av'] in ['C', 'F', 'I', 'J', 'K']:
            if tn in [1, 2, 3, 4]:
                wordmap = mangle_suffixes_or_die(wordmap, ['to', 'tu',
                                                           'ty', 'tö'])
            elif tn in [5, 6, 7]:
                wordmap = mangle_suffixes_or_die(wordmap, ['ti'])
            elif tn in [8]:
                wordmap = mangle_suffixes_or_die(wordmap, ['te'])
            elif tn in [9, 10, 11, 12, 13, 14]:
                wordmap = mangle_suffixes_or_die(wordmap, ['ta', 'tä'])
            elif tn in range(52, 79):
                lastt = wordmap['stub'].rfind('t')
                wordmap['stub'] = wordmap['stub'][:lastt]
            else:
                fail_guess_because(wordmap, ['av-', 'C', 'F', 'I', 'J', 'K'],
                                   ['1-14'])
        else:
            fail_guess_because(wordmap, ['av+'], ['A-T'])
    elif wordmap['grade_dir'] == 'strengthen':
        if wordmap['kotus_av'] == 'A':
            if tn in [33]:
                wordmap = mangle_suffixes_or_die(wordmap, ['in'])
            elif tn in [41]:
                wordmap = mangle_suffixes_or_die(wordmap, ['as', 'äs'])
            elif tn in [48]:
                wordmap = mangle_suffixes_or_die(wordmap, ['e'])
            elif tn in range(52, 79):
                lastk = wordmap['stub'].rfind('k')
                wordmap['stub'] = wordmap['stub'][:lastk + 1]
            else:
                fail_guess_because(wordmap, ['av+', 'A'], [33, 41, 48])
        elif wordmap['kotus_av'] == 'B':
            if tn in [33, 34]:
                wordmap = mangle_suffixes_or_die(wordmap, ['an'])
            elif tn in [41]:
                wordmap = mangle_suffixes_or_die(wordmap, ['as', 'äs', 'es'])
            elif tn in [48]:
                wordmap = mangle_suffixes_or_die(wordmap, ['e'])
            elif tn in range(52, 79):
                lastp = wordmap['stub'].rfind('p')
                wordmap['stub'] = wordmap['stub'][:lastp + 1]
            else:
                fail_guess_because(wordmap, ['av+', 'B'], [33, 41, 48])
        elif wordmap['kotus_av'] == 'C':
            if tn == 32:
                wordmap = mangle_suffixes_or_die(wordmap, ['ar', 'är'])
            elif tn == 33:
                wordmap = mangle_suffixes_or_die(wordmap, ['in'])
            elif tn == 34:
                wordmap = mangle_suffixes_or_die(
                    wordmap, ['on', 'ön', 'oin', 'öin'])
            elif tn == 41:
                wordmap = mangle_suffixes_or_die(wordmap, ['as', 'us', 'is',
                                                           'es', 'äs'])
            elif tn == 44:
                wordmap = mangle_suffixes_or_die(wordmap, ['et'])
            elif tn == 48:
                wordmap = mangle_suffixes_or_die(wordmap, ['e'])
            elif tn in range(52, 79):
                lastt = wordmap['stub'].rfind('t')
                if wordmap['kotus_tn'] == 73:
                    lastt = wordmap['stub'].rfind('t', 0, lastt)
                wordmap['stub'] = wordmap['stub'][:lastt + 1]
            else:
                fail_guess_because(wordmap, ['av+', 'C'], [32, 33, 34,
                                                           41, 44, 48])
        elif wordmap['kotus_av'] == 'D':
            # DANGER TERROR HORROR !!!!!!
            if wordmap['kotus_tn'] == 32:
                wordmap = mangle_suffixes_or_die(wordmap, ['en'])
            elif wordmap['kotus_tn'] == 33:
                wordmap = mangle_suffixes_or_die(wordmap, ['in'])
            elif wordmap['kotus_tn'] == 41:
                wordmap = mangle_suffixes_or_die(wordmap,
                                                 ['as', 'es', 'is', 'äs'])
            elif wordmap['kotus_tn'] == 43:
                wordmap = mangle_suffixes_or_die(wordmap, ['ut', 'yt'])
            elif wordmap['kotus_tn'] == 44:
                wordmap = mangle_suffixes_or_die(wordmap, ['et'])
            elif wordmap['kotus_tn'] == 48:
                wordmap = mangle_suffixes_or_die(wordmap, ['e'])
            elif wordmap['kotus_tn'] == 49:
                wordmap = mangle_suffixes_or_die(wordmap, ['en'])
            elif wordmap['kotus_tn'] == 67:
                wordmap = mangle_suffixes_or_die(wordmap,
                                                 ['ella', 'illa'])
            elif wordmap['kotus_tn'] == 72:
                wordmap = mangle_suffixes_or_die(wordmap,
                                                 ['ata', 'eta', 'etä', 'ota'])
            elif wordmap['kotus_tn'] == 73:
                wordmap = mangle_suffixes_or_die(wordmap,
                                                 ['ata', 'ätä'])
            elif wordmap['kotus_tn'] == 74:
                wordmap = mangle_suffixes_or_die(wordmap,
                                                 ['ota', 'eta', 'ötä', 'etä'])
            elif wordmap['kotus_tn'] == 75:
                wordmap = mangle_suffixes_or_die(wordmap,
                                                 ['ita', 'itä'])
            elif wordmap['kotus_tn'] == 99:
                pass
            else:
                fail_guess_because(wordmap, ['N', 'V', 'D'], [32, 33, 44, 48,
                                                              49, 67, 72, 73,
                                                              74, 75],
                                   "missing inverse 0:k gradation")
        elif wordmap['kotus_av'] == 'E':
            if tn == 33:
                wordmap = mangle_suffixes_or_die(wordmap, ['vin'])
            elif tn == 41:
                wordmap = mangle_suffixes_or_die(wordmap, ['vas', 'väs'])
            elif tn == 48:
                wordmap = mangle_suffixes_or_die(wordmap, ['ve'])
            elif wordmap['kotus_tn'] == 49:
                wordmap = mangle_suffixes_or_die(wordmap, ['val'])
            elif tn in range(52, 79):
                lastp = wordmap['stub'].rfind('v')
                wordmap['stub'] = wordmap['stub'][:lastp]
            else:
                fail_guess_because(wordmap, ['av+', 'E'], [33, 41, 48, 49])
        elif wordmap['kotus_av'] == 'F':
            if tn == 33:
                wordmap = mangle_suffixes_or_die(
                    wordmap, ['don', 'dun', 'din'])
            elif tn == 41:
                wordmap = mangle_suffixes_or_die(
                    wordmap, ['das', 'däs', 'des'])
            elif tn == 44:
                wordmap = mangle_suffixes_or_die(wordmap, ['det'])
            elif tn == 48:
                wordmap = mangle_suffixes_or_die(wordmap, ['de'])
            elif wordmap['kotus_tn'] == 49:
                wordmap = mangle_suffixes_or_die(wordmap, ['dar'])
            elif tn in range(52, 79):
                lastt = wordmap['stub'].rfind('d')
                wordmap['stub'] = wordmap['stub'][:lastt]
            else:
                fail_guess_because(wordmap, ['av+', 'F'], [33, 41, 44, 48, 49])
        elif wordmap['kotus_av'] == 'G':
            if tn == 41:
                wordmap = mangle_suffixes_or_die(wordmap, ['gas', 'gäs'])
            elif tn == 44:
                wordmap = mangle_suffixes_or_die(wordmap, ['get'])
            elif tn == 48:
                wordmap = mangle_suffixes_or_die(wordmap, ['ge'])
            elif wordmap['kotus_tn'] == 49:
                wordmap = mangle_suffixes_or_die(wordmap, ['ger'])
            elif tn in range(52, 79):
                lastk = wordmap['stub'].rfind('g')
                wordmap['stub'] = wordmap['stub'][:lastk]
            else:
                fail_guess_because(wordmap, ['av+', 'G'], [41, 44, 48])
        elif wordmap['kotus_av'] == 'H':
            if tn == 35:
                wordmap = mangle_suffixes_or_die(wordmap, ['min'])
            elif tn == 41:
                wordmap = mangle_suffixes_or_die(wordmap, ['mas', 'mäs'])
            elif tn == 43:
                wordmap = mangle_suffixes_or_die(wordmap, ['myt'])
            elif tn == 48:
                wordmap = mangle_suffixes_or_die(wordmap, ['me'])
            elif wordmap['kotus_tn'] == 49:
                wordmap = mangle_suffixes_or_die(wordmap, ['mel', 'mol'])
            elif tn in range(52, 79):
                lastp = wordmap['stub'].rfind('m')
                wordmap['stub'] = wordmap['stub'][:lastp]
            else:
                fail_guess_because(wordmap, ['av+', 'H'], [35, 41, 43, 48, 49])
        elif wordmap['kotus_av'] == 'I':
            if tn == 33:
                wordmap = mangle_suffixes_or_die(wordmap, ['lin'])
            elif tn == 41:
                wordmap = mangle_suffixes_or_die(wordmap, ['las', 'läs'])
            elif tn == 44:
                wordmap = mangle_suffixes_or_die(wordmap, ['let'])
            elif tn == 48:
                wordmap = mangle_suffixes_or_die(wordmap, ['le'])
            elif tn in range(52, 79):
                lastp = -1
                if wordmap['kotus_tn'] == 67:
                    lastp = wordmap['stub'].rfind('lell')
                else:
                    lastp = wordmap['stub'].rfind('l')
                wordmap['stub'] = wordmap['stub'][:lastp]
            else:
                fail_guess_because(wordmap, ['av+', 'I'], [33, 41, 44, 48])
        elif wordmap['kotus_av'] == 'J':
            if tn == 33:
                wordmap = mangle_suffixes_or_die(wordmap, ['nin'])
            elif tn == 41:
                wordmap = mangle_suffixes_or_die(wordmap, ['nas', 'näs'])
            elif tn == 44:
                wordmap = mangle_suffixes_or_die(wordmap, ['net'])
            elif tn == 48:
                wordmap = mangle_suffixes_or_die(wordmap, ['ne'])
            elif wordmap['kotus_tn'] == 49:
                wordmap = mangle_suffixes_or_die(
                    wordmap, ['nar', 'ner', 'nel'])
            elif tn in range(52, 79):
                lastp = wordmap['stub'].rfind('n')
                wordmap['stub'] = wordmap['stub'][:lastp]
            else:
                fail_guess_because(wordmap, ['av+', 'J'], [33, 41, 44, 48])
        elif wordmap['kotus_av'] == 'K':
            if tn == 33:
                wordmap = mangle_suffixes_or_die(wordmap, ['rin', 'roin'])
            elif tn == 41:
                wordmap = mangle_suffixes_or_die(wordmap, ['ras', 'räs'])
            elif tn == 44:
                wordmap = mangle_suffixes_or_die(wordmap, ['ret'])
            elif tn == 48:
                wordmap = mangle_suffixes_or_die(wordmap, ['re'])
            elif tn in range(52, 79):
                lastp = wordmap['stub'].rfind('r')
                wordmap['stub'] = wordmap['stub'][:lastp]
            else:
                fail_guess_because(wordmap, ['av+', 'K'], [33, 41, 44, 48])
        elif wordmap['kotus_av'] == 'L':
            if tn == 33:
                wordmap = mangle_suffixes_or_die(wordmap, ['jin'])
            elif tn == 48:
                wordmap = mangle_suffixes_or_die(wordmap, ['je'])
            elif tn in range(52, 79):
                lastp = wordmap['stub'].rfind('j')
                wordmap['stub'] = wordmap['stub'][:lastp]
            else:
                fail_guess_because(wordmap, ['av+', 'K'], [33, 48])
        elif wordmap['kotus_av'] == 'N':
            lastp = wordmap['stub'].rfind('d')
            wordmap['stub'] = wordmap['stub'][:lastp + 1]
            if lastp == -1:
                fail_guess_because(wordmap, ['av+', 'N'], ['d'])
        elif wordmap['kotus_av'] == 'P':
            lastp = wordmap['stub'].rfind('b')
            wordmap['stub'] = wordmap['stub'][:lastp + 1]
            if lastp == -1:
                fail_guess_because(wordmap, ['av+', 'P'], ['b'])
        elif wordmap['kotus_av'] == 'O':
            lastp = wordmap['stub'].rfind('g')
            wordmap['stub'] = wordmap['stub'][:lastp + 1]
            if lastp == -1:
                fail_guess_because(wordmap, ['av+', 'O'], ['g'])
        elif wordmap['kotus_av'] == 'T':
            lastp = wordmap['stub'].rfind('e')
            wordmap['stub'] = wordmap['stub'][:lastp]
            if lastp == -1:
                fail_guess_because(wordmap, ['av+', 'T'], ['auer'])
        else:
            fail_guess_because(wordmap, ['av-'], ['A-T'])
        return wordmap
    return wordmap


def stub_legacy(wordmap):
    '''Generate unmodifiable stub for inflectional processes.
    this cuts every morphologically varying character except gradating stop
    from ends of the words.
    '''
    tn = int(wordmap['kotus_tn'])
    # then cut
    if tn in range(1, 5) or tn in [8, 21, 22, 32, 48]:
        wordmap['stub'] = wordmap['stub']
    if tn in [5, 6]:
        if wordmap['extra_i']:
            wordmap['stub'] = wordmap['stub'][:-1]
        else:
            wordmap['stub'] = wordmap['stub']
    elif tn in [7, 16] or tn in range(33, 38) or tn in range(39, 47):
        wordmap['stub'] = wordmap['stub'][:-1]
    elif tn in range(9, 16):
        wordmap['stub'] = wordmap['stub'][:-1]
    elif tn in [16, 23, 24, 26]:
        wordmap['stub'] = wordmap['stub'].rstrip('i')
    elif tn in range(17, 19) or tn == 20:
        wordmap['stub'] = wordmap['stub'][:-1]
    elif tn == 19:
        wordmap['stub'] = wordmap['stub'][:-2]
    elif tn in [25, 27]:
        wordmap['stub'] = wordmap['stub'][:-2]
    elif tn == 28:
        wordmap['stub'] = wordmap['stub'][:-2]
    elif tn in [29, 30, 31, 38]:
        wordmap['stub'] = wordmap['stub'][:-3]
    elif tn == 47:
        wordmap['stub'] = wordmap['stub'][:-2]
    elif tn == 49:
        if wordmap['stub'].endswith('e'):
            wordmap['extra_e'] = True
    elif tn in [52, 78]:
        wordmap['stub'] = wordmap['stub'][:-1]
    elif tn in [53, 56, 77]:
        wordmap['stub'] = wordmap['stub'][:-2]
    elif tn == 54:
        if wordmap['kotus_av']:
            wordmap['stub'] = wordmap['stub'][:-7]
        else:
            wordmap['stub'] = wordmap['stub'][:-3]
    elif tn in [55, 57, 76]:
        if wordmap['kotus_av']:
            wordmap['stub'] = wordmap['stub'][:-7]  # 3 + gradation mark
        else:
            wordmap['stub'] = wordmap['stub'][:-3]
    elif tn == 58:
        wordmap['stub'] = wordmap['stub'][:-2]
    elif tn == 59:
        if wordmap['kotus_av']:
            wordmap['stub'] = wordmap['stub'][:-7]  # 3 + gradation mark
        else:
            wordmap['stub'] = wordmap['stub'][:-3]
    elif tn == 60:
        if wordmap['kotus_av']:
            wordmap['stub'] = wordmap['stub'][:-8]  # 4 + gradation mark
        else:
            wordmap['stub'] = wordmap['stub'][:-4]
    elif tn == 61:
        wordmap['stub'] = wordmap['stub'][:-2]
    elif tn in [62, 68]:
        wordmap['stub'] = wordmap['stub'][:-3]
    elif tn in [62, 63, 65]:
        wordmap['stub'] = wordmap['stub'][:-3]
    elif tn == 64:
        wordmap['stub'] = wordmap['stub'][:-4]
    elif tn in [66, 67, 1067, 69, 72, 73, 74, 75, 77]:
        wordmap['stub'] = wordmap['stub'][:-2]
    elif tn in [70, 71, 71]:
        wordmap['stub'] = wordmap['stub'][:-3]
    elif tn == 1007:
        wordmap['stub'] = wordmap['stub'][:-1]
    elif tn in [1010, 1009]:
        if wordmap['kotus_av']:
            wordmap['stub'] = wordmap['stub'][:-7]  # 3 + gradation mark
        else:
            wordmap['stub'] = wordmap['stub'][:-3]
    elif tn in [1024, 1026]:
        wordmap['stub'] = wordmap['stub'][:-1]
    return wordmap
