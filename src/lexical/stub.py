#!/usr/bin/env python3

from sys import stderr

from omor_strings_io import remove_suffixes_or_die, fail_guess_because

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
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'],
                        ['i'])
            else:
                wordmap['stub'] = wordmap['stub']
        elif tn == 10:
            if wordmap['stub'].endswith('n'):
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'],
                        ['an', 'än'])
            else:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'],
                        ['a', 'ä'])
        elif tn == 41 and wordmap['pos'] == 'ADJECTIVE' and (wordmap['stub'].endswith('is') or wordmap['stub'].endswith('paras')):
            wordmap['stub'] = wordmap['stub'][:-2] 
        elif tn in [7, 16] or tn in range(33, 38) or tn in range(39, 47):
            wordmap['stub'] = wordmap['stub'][:-1]
        elif tn in range(9, 16):
            wordmap['stub'] = wordmap['stub'][:-1]
        elif tn in [16, 23, 24, 26]:
            wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'],
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
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'],
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
            wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['e'])
        elif tn in [1010, 1009]:
            wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], 
                    ['ika', 'tkä'])
        elif tn in [1024, 1026]:
            wordmap['stub'] = wordmap['stub'][:-1]
        elif tn == 1067:
            wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['olla'])
        elif tn == 1099:
            wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['ei'])
        elif wordmap['kotus_tn'] == 101:
            if wordmap['lemma'] in ['minä', 'sinä']:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['nä'])
            elif wordmap['lemma'] == 'hän':
                pass
            elif wordmap['lemma'] in ['me', 'te', 'he']:
                pass
            elif wordmap['lemma'] == 'tämä':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['mä'])
            elif wordmap['lemma'] == 'tuo':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['uo'])
            elif wordmap['lemma'] == 'se':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['e'])
            elif wordmap['lemma'] == 'nämä':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['mä'])
            elif wordmap['lemma'] == 'nuo':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['uo'])
            elif wordmap['lemma'] == 'ne':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['e'])
            elif wordmap['lemma'] == 'joku':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['ku'])
            elif wordmap['lemma'] == 'joka':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['ka'])
            elif wordmap['lemma'] == 'jokin':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['kin'])
            elif wordmap['lemma'] == 'kuka':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['uka'])
            elif wordmap['lemma'] == 'kukaan':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['ukaan'])
            elif wordmap['lemma'].endswith('kukin'):
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['ukin'])
            elif wordmap['lemma'] == 'mikin':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['kin'])
            elif wordmap['lemma'] == 'mikä':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['kä'])
            elif wordmap['lemma'] == 'mikään':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['kään'])
            elif wordmap['lemma'] == 'missä':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['ssä'])
            elif wordmap['lemma'] == 'missäkään':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['ssäkään'])
            elif wordmap['lemma'] == 'missään':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['ssään'])
            elif wordmap['lemma'] == 'muuan':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['n'])
            elif wordmap['lemma'] in ['mä', 'sä']:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['ä'])
            elif wordmap['lemma'] in ['mie', 'sie']:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['e'])
            elif wordmap['lemma'] == 'toi':
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['i'])
            elif wordmap['lemma'].endswith('ainoa'):
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['a'])
            elif wordmap['lemma'] in ['jota', 'kenkään', 'kuta', 'ma', 'mi',
                    'missäkin', 'mikäkin', 'monta', 'montaa', 'sa', 'tää', 'ken',
                    'koko']:
                pass
        elif wordmap['kotus_tn'] == 99 and wordmap['possessive'] \
                and wordmap['stub'].endswith('n'):
            wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['n'])
        elif wordmap['kotus_tn'] in [0, 99]:
            pass
        else:
            fail_guess_because(wordmap, ['!av'], ['0-71', 1007, 1010,1009,
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
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['en'])
            elif wordmap['kotus_tn'] == 33:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['in'])
            elif wordmap['kotus_tn'] == 41:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'],
                        ['as', 'es', 'is', 'äs'])
            elif wordmap['kotus_tn'] == 44:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['et'])
            elif wordmap['kotus_tn'] == 48:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['e'])
            elif wordmap['kotus_tn'] == 49:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], ['en'])
            elif wordmap['kotus_tn'] == 67:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], 
                        ['ella', 'illa'])
            elif wordmap['kotus_tn'] == 72:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], 
                        ['ata', 'eta', 'etä', 'ota'])
            elif wordmap['kotus_tn'] == 73:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], 
                        ['ata', 'ätä'])
            elif wordmap['kotus_tn'] == 74:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], 
                        ['ota', 'eta', 'ötä', 'etä'])
            elif wordmap['kotus_tn'] == 75:
                wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], 
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


