#!/usr/bin/env python3

from lexc_string_utils import replace_rightmost, replace_rightmosts
from sys import stderr

# 
def plurale_tantum_get_singular_stem(wordmap):
    '''Guess inflectional singulars for words whose dictionary form is plural.
    '''
    tn = wordmap['kotus_tn']
    av = wordmap['kotus_av']
    if not wordmap['plurale_tantum'] == 'obligatory':
        return wordmap
    if wordmap['kotus_av'] and tn not in [27, 28, 34]:
        if tn in [7, 23, 24, 25, 26, 29, 30]:
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'e', 'i')
			
        if (tn in range(1,7) or tn in range(8, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'A':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'k', 'kk')
        elif (tn in range(1,7) or tn in range(8, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'B':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'p', 'pp')
        elif (tn in range(1,7) or tn in range(8, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'C':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 't', 'tt')
        elif tn == 1 and wordmap['kotus_av'] == 'D':
            wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['ut', 'yt', 'öt', 'ot'], ['ku', 'ky', 'kö', 'ko'])
        elif tn in [5, 7] and wordmap['kotus_av'] == 'D':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'it', 'ki')
        elif tn in [9, 10] and wordmap['kotus_av'] == 'D':
            wordmap['stub'] = replace_rightmosts(wordmap['stub'], ['at', 'ät'], ['ka', 'kä'])
        elif tn in [1009, 1010] and wordmap['kotus_av'] == 'D':
            wordmap['stub'] = replace_rightmost(wordmap['stub'], 'jat', 'ika')
        elif tn == 32 and wordmap['kotus_av'] == 'D':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 'et', ''), 'k', '')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'E':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'v', 'p')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'F':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'd', 't')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'G':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'g', 'k')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'H':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'mm', 'mp')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'I':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'll', 'lt')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'J':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'nn', 'nt')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'K':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'rr', 'rt')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'L':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'j', 'k')
        elif (tn in range(1, 16) or tn in range(17, 22)) and wordmap['kotus_av'] == 'M':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'v', 'k')
        elif (tn in [23, 24, 25, 26, 29, 30]) and wordmap['kotus_av'] == 'G':
            wordmap['stub'] = replace_rightmost(replace_rightmost(wordmap['stub'], 't', ''), 'g', 'k')
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
        elif tn == 41 and wordmap['kotus_av'] in ['A', 'B', 'C']:
            wordmap['stub'] = wordmap['stub'][:-4] + '{aä}s'
        elif tn == 41 and wordmap['kotus_av'] == 'D':
            wordmap['stub'] = wordmap['stub'][:-4] + '{k~~}{aä}s'  # avoid replacement problem at gradation.py
        elif tn == 41 and wordmap['kotus_av'] == 'E':
            wordmap['stub'] = wordmap['stub'][:-4] + 'v{aä}s'
        elif tn == 41 and wordmap['kotus_av'] == 'F':
            wordmap['stub'] = wordmap['stub'][:-4] + 'd{aä}s'
        elif tn == 41 and wordmap['kotus_av'] == 'G':
            wordmap['stub'] = wordmap['stub'][:-4] + 'g{aä}s'
        elif tn == 41 and wordmap['kotus_av'] == 'H':
            wordmap['stub'] = wordmap['stub'][:-4] + 'm{aä}s'
        elif tn == 41 and wordmap['kotus_av'] == 'I':
            wordmap['stub'] = wordmap['stub'][:-4] + 'l{aä}s'
        elif tn == 41 and wordmap['kotus_av'] == 'J':
            wordmap['stub'] = wordmap['stub'][:-4] + 'n{aä}s'
        elif tn == 41 and wordmap['kotus_av'] == 'K':
            wordmap['stub'] = wordmap['stub'][:-4] + 'r{aä}s'
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
            print("Unhandled plt in ", wordmap, file=stderr)
            return None
        return wordmap
    else:
        if tn in range(1,7) or tn in range(8, 16) or tn in range(17, 22):
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
            print("Unhandled plurale tantum in", wordmap, file=stderr)
            return None
        return wordmap
    return None

