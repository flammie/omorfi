#!/usr/bin/env python3

from lexc_string_utils import replace_rightmost

def gradation_make_morphophonemes(wordmap):
    '''mark up gradating stop for morphophonological handling'''
    tn = wordmap['kotus_tn']
    av = wordmap['kotus_av']
    if not wordmap['kotus_av']):
        return wordmap
    if tn in range(1, 28) or tn in range(29, 32) or tn in range(52, 66) or tn == 76 or tn in [1009, 1010]:
        # strong root stem
        if av == 'A':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', '{k~0}')
        elif av == 'B':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'p', '{p~0}')
        elif av == 'C':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', '{t~0}')
        elif av == 'D':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', '{k~0~’}')
        elif av == 'E':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'p', '{p~v}')
        elif av == 'F':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', '{t~d}')
        elif av == 'G':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', '{k~g}')
        elif av == 'H':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'p', '{p~m}')
        elif av == 'I':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', '{t~l}')
        elif av == 'J':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', '{t~n}')
        elif av == 'K':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', '{t~r}')
        elif av == 'L':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', '{k~j}')
        elif av == 'M':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', '{k~v}')
        elif av == 'O':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'g', '{g~0}')
        elif av == 'P':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'b', '{b~0}')
        elif av == 'N':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'd', '{d~0}')
        else:
            print("unhandled gradation in", wordmap, file=stderr)
    else:
        # weak root stem
        if av == 'A':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'k', 'k{k~0}')
        elif av == 'B':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'p', 'p{p~0}')
        elif av == 'C' and tn in range(72, 76):
            # TVtA verbs
            wordmap['stub'] = wordmap['stub'][:wordmap['stub'].rfind('t')- 2 ] + 't{t~0}' + wordmap['stub'][wordmap['stub'].rfind('t')-1:]
        elif av == 'C':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 't', 't{t~0}')
        elif av == 'D':
            # danger ahead! (it appears from middle of nowhere)
            if tn == 32:
                wordmap['stub'] = replace_rightmost(wordmap['stub'], 'e', '{k~0}e')
            elif tn == 33:
                wordmap['stub'] = replace_rightmost(wordmap['stub'], 'i', '{k~0}i')
            elif tn == 41:
                wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['as', 'es', 'is'], ['{k~0}as', '{k~0}es', '{k~0}is'])
            elif tn == 48:
                wordmap['stub'] = replace_rightmost(wordmap['stub'], 'e', '{k~0}e')
            elif tn == 49:
                wordmap['stub'] = replace_rightmost(wordmap['stub'], 'en', '{k~0}en')
            elif tn == 67:
                wordmap['stub'] = replace_rightmost(wordmap['stub'], 'ell', '{k~0}ell')
            elif tn == 72:
                wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['et', 'ot'], ['{k~0}et', '{k~0}ot'])
            elif tn == 73:
                wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['ata', 'ätä'], ['{k~0}ata', '{k~0}ätä'])
            elif tn == 74:
                wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['ota', 'eta', 'ötä', 'etä'], ['{k~0}ota', '{k~0}eta', '{k~0}ötä', '{k~0}etä'])
            elif tn == 75:
                wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['ita', 'itä'], ['{k~0}ita', '{k~0}itä'])
            else:
                print("Unhandled D weak", wordmap['stub'], tn, file=stderr)
        elif av == 'E':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'v', '{p~v}')
        elif av == 'F':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'd', '{t~d}')
        elif av == 'G':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'g', '{k~g}')
        elif av == 'H':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'm', '{p~m}')
        elif av == 'I' and tn != 67:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'l', '{t~l}')
        elif av == 'I' and tn == 67:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'lell', '{t~l}ell')
        elif av == 'J' and tn != 33:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'n', '{t~n}')
        elif av == 'J' and tn == 33:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'nin', '{t~n}in')
        elif av == 'K':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'r', '{t~r}')
        elif av == 'L':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'j', '{k~j}')
        elif av == 'N':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'd', 'd{d~0}')
        elif av == 'O':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'g', 'g{g~0}')
        elif av == 'P':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'b', 'b{b~0}')
        elif av == 'T' and tn == 49:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'e', '{t~0}e')
        else:
            print("unhandled gradation in", wordmap, file=stderr)
        return wordmap
    return None

