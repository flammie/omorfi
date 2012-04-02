#!/usr/bin/env python3

def stub_all(wordmap):
    '''Generate unmodifiable stub for inflectional processes.
    this cuts every morphologically varying character except gradating stop
    from ends of the words.
    '''
    tn = int(wordmap['kotus_tn'])
    # first save stem data we cut
    if tn in [5, 6]:
        if wordmap['stub'].endswith('i'):
            wordmap['extra_i'] = True
    elif tn in range(9, 16) or tn in [1009, 1010]:
        if wordmap['stub'].endswith('a'):
            wordmap['stem_vowel'] = 'a'
        elif wordmap['stub'].endswith('ä'):
            wordmap['stem_vowel'] = 'ä'
    elif tn in range(17, 19) or tn == 20:
        if wordmap['stub'].endswith('a'):
            wordmap['stem_vowel'] = 'a'
        elif wordmap['stub'].endswith('e'):
            wordmap['stem_vowel'] = 'e'
        elif wordmap['stub'].endswith('i'):
            wordmap['stem_vowel'] = 'i'
        elif wordmap['stub'].endswith('o'):
            wordmap['stem_vowel'] = 'o'
        elif wordmap['stub'].endswith(''):
            wordmap['stem_vowel'] = ''
        elif wordmap['stub'].endswith('y'):
            wordmap['stem_vowel'] = 'y'
        elif wordmap['stub'].endswith('ä'):
            wordmap['stem_vowel'] = 'ä'
        elif wordmap['stub'].endswith('ö'):
            wordmap['stem_vowel'] = 'ö'
    elif tn == 19:
        if wordmap['stub'].endswith('uo'):
            wordmap['stem_diphtong'] = 'uo'
        elif wordmap['stub'].endswith('yö'):
            wordmap['stem_diphtong'] = 'yö'
        elif wordmap['stub'].endswith('ie'):
            wordmap['stem_diphtong'] = 'ie'
    elif tn == 47:
        if wordmap['stub'].endswith('ut'):
            wordmap['stem_vowel'] = ''
        elif wordmap['stub'].endswith('yt'):
            wordmap['stem_vowel'] = 'y'
    elif tn in range(52, 64) or tn in range(65, 79):
        if wordmap['stub'].endswith('ä'):
            wordmap['harmony'] = 'front'
        else:
            wordmap['harmony'] = 'back'
    elif tn == 64:
        if wordmap['stub'].endswith('uoda'):
            wordmap['stem_diphtong'] = 'uo'
        elif wordmap['stub'].endswith('yödä'):
            wordmap['stem_diphtong'] = 'yö'
        elif wordmap['stub'].endswith('iedä'):
            wordmap['stem_diphtong'] = 'ie'
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
        wordmap['stub'] = wordmap['stub'][:-7]
    elif tn in [55, 57, 76]:
        wordmap['stub'] = wordmap['stub'][:-7] # 3 + gradation mark
    elif tn == 58:
        wordmap['stub'] = wordmap['stub'][:-2]
    elif tn == 59:
        wordmap['stub'] = wordmap['stub'][:-7] # 3 + gradation mark
    elif tn == 60:
        wordmap['stub'] = wordmap['stub'][:-8] # 4 + gradation mark
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


