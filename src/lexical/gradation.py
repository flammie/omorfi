#!/usr/bin/env python3

from lexc_string_utils import replace_rightmost, replace_rightmosts

def gradation_make_morphophonemes(wordmap):
    '''mark up gradating stop for morphophonological handling'''
    tn = wordmap['kotus_tn']
    av = wordmap['kotus_av']
    if not wordmap['kotus_av']:
        return wordmap
    if tn in range(1, 28) or tn in range(29, 32) or tn in range(52, 66) or tn == 76 or tn in [1009, 1010]:
        # strong root stem
        if av == 'A':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', '{k~~}')
        elif av == 'B':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'p', '{p~~}')
        elif av == 'C':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', '{t~~}')
        elif av == 'D':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', '{k~~}')
        elif av == 'E':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'p', '{p~~}')
        elif av == 'F':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', '{t~~}')
        elif av == 'G':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', '{k~~}')
        elif av == 'H':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'p', '{p~~}')
        elif av == 'I':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', '{t~~}')
        elif av == 'J':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', '{t~~}')
        elif av == 'K':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', '{t~~}')
        elif av == 'L':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', '{k~~}')
        elif av == 'M':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', '{k~~}')
        elif av == 'O':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'g', '{g~~}')
        elif av == 'P':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'b', '{b~~}')
        elif av == 'N':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'd', '{d~~}')
        else:
            print("unhandled gradation in", wordmap, file=stderr)
            return None
        return wordmap
    elif tn == 28:
        # gah gradation in stemparts
        return wordmap
    else:
        # weak root stem
        if av == 'A':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', 'k{k~~}')
        elif av == 'B':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'p', 'p{p~~}')
        elif av == 'C' and tn in range(72, 76):
            # TVtA verbs
            wordmap['stub'] = wordmap['stub'][:wordmap['stub'].rfind('t')- 2 ] + 't{t~~}' + wordmap['stub'][wordmap['stub'].rfind('t')-1:]
        elif av == 'C':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', 't{t~~}')
        elif av == 'D':
            # danger ahead! (it appears from middle of nowhere)
            if tn == 32:
                wordmap['stub'] = replace_rightmost(wordmap['stub'], 'e', '{k~~}e')
            elif tn == 33:
                wordmap['stub'] = replace_rightmost(wordmap['stub'], 'i', '{k~~}i')
            elif tn == 41:
                wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['as', 'es', 'is'], ['{k~~}as', '{k~0}es', '{k~0}is'])
            elif tn == 48:
                wordmap['stub'] = replace_rightmost(wordmap['stub'], 'e', '{k~~}e')
            elif tn == 49:
                wordmap['stub'] = replace_rightmost(wordmap['stub'], 'en', '{k~~}en')
            elif tn == 67:
                wordmap['stub'] = replace_rightmost(wordmap['stub'], 'ell', '{k~~}ell')
            elif tn == 72:
                wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['et', 'ot'], ['{k~~}et', '{k~0}ot'])
            elif tn == 73:
                wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['ata', 'ätä'], ['{k~~}ata', '{k~0}ätä'])
            elif tn == 74:
                wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['ota', 'eta', 'ötä', 'etä'], ['{k~~}ota', '{k~0}eta', '{k~0}ötä', '{k~0}etä'])
            elif tn == 75:
                wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['ita', 'itä'], ['{k~~}ita', '{k~0}itä'])
            else:
                print("Unhandled D weak", wordmap['stub'], tn, file=stderr)
        elif av == 'E':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'v', '{p~~}')
        elif av == 'F':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'd', '{t~~}')
        elif av == 'G':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'g', '{k~~}')
        elif av == 'H':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'm', '{p~~}')
        elif av == 'I' and tn != 67:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'l', '{t~~}')
        elif av == 'I' and tn == 67:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'lell', '{t~~}ell')
        elif av == 'J' and tn != 33:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'n', '{t~~}')
        elif av == 'J' and tn == 33:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'nin', '{t~~}in')
        elif av == 'K':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'r', '{t~~}')
        elif av == 'L':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'j', '{k~~}')
        elif av == 'N':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'd', 'd{d~~}')
        elif av == 'O':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'g', 'g{g~~}')
        elif av == 'P':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'b', 'b{b~~}')
        elif av == 'T' and tn == 49:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'e', '{t~~}e')
        else:
            print("unhandled gradation in", wordmap, file=stderr)
            return None
        return wordmap
    return None

