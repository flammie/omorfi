#!/usr/bin/env python3

from sys import stderr

from omor_strings_io import mangle_suffixes_or_die, fail_guess_because

def stub_all(wordmap):
    '''Generate unmodifiable stub for inflectional processes.
    this cuts every morphologically varying character.
    '''
    if wordmap['pos'] == 'ACRONYM':
        return wordmap
    tn = int(wordmap['kotus_tn'])
    if not wordmap['kotus_av'] or tn in [28, 60, 1007, 1009, 1010]:
        if tn in range(1, 5) or tn in [8, 21, 22, 48]:
            wordmap['stub'] = wordmap['stub']
        elif tn in [5, 6]:
            if wordmap['stub'].endswith('i'):
                wordmap = mangle_suffixes_or_die(wordmap,
                        ['i'])
            else:
                wordmap['stub'] = wordmap['stub']
        elif tn == 10:
            if wordmap['stub'].endswith('n'):
                wordmap = mangle_suffixes_or_die(wordmap,
                        ['an', 'än'])
            else:
                wordmap = mangle_suffixes_or_die(wordmap,
                        ['a', 'ä', 'ă'])
        elif tn == 41 and wordmap['pos'] == 'ADJECTIVE' and (wordmap['stub'].endswith('is') or wordmap['stub'].endswith('paras')):
            wordmap['stub'] = wordmap['stub'][:-2] 
        elif tn in [7, 16] or tn in range(33, 38) or tn in range(39, 47):
            wordmap['stub'] = wordmap['stub'][:-1]
        elif tn in range(9, 16):
            wordmap['stub'] = wordmap['stub'][:-1]
        elif tn in [16, 23, 24, 26]:
            wordmap = mangle_suffixes_or_die(wordmap,
                    ['i'])
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
        elif tn == 32:
            if wordmap['stub'].endswith('kymmenen'):
                wordmap = mangle_suffixes_or_die(wordmap,
                        ['en'])
            else:
                pass
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
        elif tn in [66, 67, 69, 72, 73, 74, 75, 77]:
            wordmap['stub'] = wordmap['stub'][:-2]
        elif tn in [70, 71, 71]:
            wordmap['stub'] = wordmap['stub'][:-3]
        elif tn == 1007:
            wordmap['stub'] = wordmap['stub'][:-1]
        elif tn == 1008:
            wordmap = mangle_suffixes_or_die(wordmap, ['e'])
        elif tn in [1010, 1009]:
            wordmap = mangle_suffixes_or_die(wordmap, 
                    ['ika', 'tkä'])
        elif tn in [1024, 1026]:
            wordmap['stub'] = wordmap['stub'][:-1]
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
            elif wordmap['lemma'] == 'kuka':
                wordmap = mangle_suffixes_or_die(wordmap, ['uka'])
            elif wordmap['lemma'] == 'kukaan':
                wordmap = mangle_suffixes_or_die(wordmap, ['ukaan'])
            elif wordmap['lemma'].endswith('kukin'):
                wordmap = mangle_suffixes_or_die(wordmap, ['ukin'])
            elif wordmap['lemma'] == 'mikin':
                wordmap = mangle_suffixes_or_die(wordmap, ['kin'])
            elif wordmap['lemma'] == 'mikä':
                wordmap = mangle_suffixes_or_die(wordmap, ['kä'])
            elif wordmap['lemma'] == 'mikään':
                wordmap = mangle_suffixes_or_die(wordmap, ['kään'])
            elif wordmap['lemma'] == 'missä':
                wordmap = mangle_suffixes_or_die(wordmap, ['ssä'])
            elif wordmap['lemma'] == 'missäkään':
                wordmap = mangle_suffixes_or_die(wordmap, ['ssäkään'])
            elif wordmap['lemma'] == 'missään':
                wordmap = mangle_suffixes_or_die(wordmap, ['ssään'])
            elif wordmap['lemma'] == 'muuan':
                wordmap = mangle_suffixes_or_die(wordmap, ['n'])
            elif wordmap['lemma'] in ['mä', 'sä']:
                wordmap = mangle_suffixes_or_die(wordmap, ['ä'])
            elif wordmap['lemma'] in ['mie', 'sie']:
                wordmap = mangle_suffixes_or_die(wordmap, ['e'])
            elif wordmap['lemma'] == 'toi':
                wordmap = mangle_suffixes_or_die(wordmap, ['i'])
            elif wordmap['lemma'].endswith('ainoa'):
                wordmap = mangle_suffixes_or_die(wordmap, ['a'])
            elif wordmap['lemma'] in ['jota', 'kenkään', 'kuta', 'ma', 'mi',
                    'missäkin', 'mikäkin', 'monta', 'montaa', 'sa', 'tää', 'ken',
                    'koko']:
                pass
        elif wordmap['kotus_tn'] in [99, 999] and wordmap['possessive'] \
                and wordmap['stub'].endswith('n'):
            wordmap = mangle_suffixes_or_die(wordmap, ['n'])
        elif wordmap['kotus_tn'] in [0, 99, 999]:
            pass
        elif wordmap['kotus_tn'] == 1101:
            wordmap = mangle_suffixes_or_die(wordmap, ['ka', 'kä'])
        else:
            fail_guess_because(wordmap, ['!av'], ['0-71', 999, 1007, 1010,1009,
                1024, 1026, 1067, 1099])
    elif wordmap['grade_dir'] == 'weaken':
        if wordmap['kotus_av'] in ['A', 'D', 'G', 'L', 'M']:
            lastk = wordmap['stub'].rfind('k')
            wordmap['stub'] = wordmap['stub'][:lastk]
            if lastk == -1:
                print("Unguessable stub; gradating K not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] in ['B', 'E', 'H']:
            lastp = wordmap['stub'].rfind('p')
            wordmap['stub'] = wordmap['stub'][:lastp]
            if lastp == -1:
                print("Unguessable stub; gradating P not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] in ['C', 'F', 'I', 'J', 'K']:
            lastt = wordmap['stub'].rfind('t')
            wordmap['stub'] = wordmap['stub'][:lastt]
            if lastt == -1:
                print("Unguessable stub; gradating T not found in", wordmap,
                        file=stderr)
        else:
            fail_guess_because(wordmap, ['av+'], ['A-T'])
    elif wordmap['grade_dir'] == 'strengthen':
        if wordmap['kotus_av'] == 'A': 
            lastk = wordmap['stub'].rfind('k')
            wordmap['stub'] = wordmap['stub'][:lastk + 1]
            if lastk == -1:
                print("Unguessable stub; gradating -K not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'B': 
            lastp = wordmap['stub'].rfind('p')
            wordmap['stub'] = wordmap['stub'][:lastp + 1]
            if lastp == -1:
                print("Unguessable stub; gradating -P not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'C': 
            lastt = wordmap['stub'].rfind('t')
            if wordmap['kotus_tn'] == 73:
                lastt = wordmap['stub'].rfind('t', 0, lastt)
            wordmap['stub'] = wordmap['stub'][:lastt + 1]
            if lastt == -1:
                print("Unguessable stub; gradating -T not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'D':
            # DANGER TERROR HORROR !!!!!!
            if wordmap['kotus_tn'] == 32:
                wordmap = mangle_suffixes_or_die(wordmap, ['en'])
            elif wordmap['kotus_tn'] == 33:
                wordmap = mangle_suffixes_or_die(wordmap, ['in'])
            elif wordmap['kotus_tn'] == 41:
                wordmap = mangle_suffixes_or_die(wordmap,
                        ['as', 'es', 'is', 'äs'])
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
                    49, 67, 72, 73, 74, 75], "missing inverse 0:k gradation")
        elif wordmap['kotus_av'] == 'E': 
            lastp = wordmap['stub'].rfind('v')
            wordmap['stub'] = wordmap['stub'][:lastp]
            if lastp == -1:
                print("Unguessable stub; gradating -V not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'F': 
            lastt = wordmap['stub'].rfind('d')
            wordmap['stub'] = wordmap['stub'][:lastt]
            if lastt == -1:
                print("Unguessable stub; gradating -D not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'G': 
            lastk = wordmap['stub'].rfind('g')
            wordmap['stub'] = wordmap['stub'][:lastk]
            if lastk == -1:
                print("Unguessable stub; gradating -G not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'H': 
            lastp = wordmap['stub'].rfind('m')
            wordmap['stub'] = wordmap['stub'][:lastp]
            if lastp == -1:
                print("Unguessable stub; gradating -M not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'I': 
            lastp = -1
            if wordmap['kotus_tn'] == 67:
                lastp = wordmap['stub'].rfind('lell')
            else:
                lastp = wordmap['stub'].rfind('l')
            wordmap['stub'] = wordmap['stub'][:lastp]
            if lastp == -1:
                print("Unguessable stub; gradating -V not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'J': 
            lastp = -1
            if wordmap['kotus_tn'] == 33:
                lastp = wordmap['stub'].rfind('nin')
            else:
                lastp = wordmap['stub'].rfind('n')
            wordmap['stub'] = wordmap['stub'][:lastp]
            if lastp == -1:
                print("Unguessable stub; gradating -N not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'K': 
            lastp = wordmap['stub'].rfind('r')
            wordmap['stub'] = wordmap['stub'][:lastp]
            if lastp == -1:
                print("Unguessable stub; gradating -R not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'L': 
            lastp = wordmap['stub'].rfind('j')
            wordmap['stub'] = wordmap['stub'][:lastp]
            if lastp == -1:
                print("Unguessable stub; gradating -J not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'N': 
            lastp = wordmap['stub'].rfind('d')
            wordmap['stub'] = wordmap['stub'][:lastp + 1]
            if lastp == -1:
                print("Unguessable stub; gradating -D not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'P': 
            lastp = wordmap['stub'].rfind('b')
            wordmap['stub'] = wordmap['stub'][:lastp + 1]
            if lastp == -1:
                print("Unguessable stub; gradating -B not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'O': 
            lastp = wordmap['stub'].rfind('g')
            wordmap['stub'] = wordmap['stub'][:lastp + 1]
            if lastp == -1:
                print("Unguessable stub; gradating -G not found in", wordmap,
                        file=stderr)
        elif wordmap['kotus_av'] == 'T': 
            lastp = wordmap['stub'].rfind('e')
            wordmap['stub'] = wordmap['stub'][:lastp]
            if lastp == -1:
                print("Unguessable stub; gradating -auer not found in", wordmap,
                        file=stderr)
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
            wordmap['stub'] = wordmap['stub'][:-7] # 3 + gradation mark
        else:
            wordmap['stub'] = wordmap['stub'][:-3]
    elif tn == 58:
        wordmap['stub'] = wordmap['stub'][:-2]
    elif tn == 59:
        if wordmap['kotus_av']:
            wordmap['stub'] = wordmap['stub'][:-7] # 3 + gradation mark
        else:
            wordmap['stub'] = wordmap['stub'][:-3]
    elif tn == 60:
        if wordmap['kotus_av']:
            wordmap['stub'] = wordmap['stub'][:-8] # 4 + gradation mark
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
            wordmap['stub'] = wordmap['stub'][:-7] # 3 + gradation mark
        else:
            wordmap['stub'] = wordmap['stub'][:-3]
    elif tn in [1024, 1026]:
        wordmap['stub'] = wordmap['stub'][:-1]
    return wordmap


