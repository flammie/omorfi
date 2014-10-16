#!/usr/bin/env python3
#
# utils to format apertium style data from omorfi database values

from omor_strings_io import lexc_escape, word_boundary, weak_boundary, \
        morph_boundary, deriv_boundary, optional_hyphen, \
        fail_formatting_missing_for


ftb3_multichars= {
        '% A',
        '% V',
        '% N',
        '% Abbr',
        '% Pron',
        '% Num',
        '% Prop',
        '% Interj',
        '% Dem',
        '% Interr',
        '% Rel',
        '% Qnt',
        '% Refl',
        '% N% Abbr',
        '% %>%>%>',
        '% CS',
        '% CC',
        '% Adv',
        '% Adp',
        '% Po',
        '% Pr',
        '% Adp% Po',
        '% Punct',
        '% Quote',
        '% Dash',
        '% Digit',
        '% Roman',
        '% Nom',
        '% Par',
        '% Gen',
        '% Ine',
        '% Ela',
        '% Ill',
        '% Ade',
        '% Abl',
        '% All',
        '% Ess',
        '% Ins',
        '% Abe',
        '% Tra',
        '% Com' ,
        '% Lat',
        '% Acc',
        '% Sg',
        '% Pl',
        '% PxSg1',
        '% PxSg2',
        '% PxPl1',
        '% PxPl2',
        '% PxPl3',
        '% Px3',
        '% TrunCo',
        'TrunCo% ',
        '% TruncPrefix',
        'TruncSuffix% ',
        '% Prt',
        '% Prs',
        '% Pst',
        '% Cond',
        '% Pot',
        '% Impv',
        '% Opt',
        '% Sg1',
        '% Sg2',
        '% Sg3',
        '% Pl1',
        '% Pl2',
        '% Pl3',
        '% Pe4',
        '% ConNeg' ,
        '% Neg',
        '% Act',
        '% Pass',
        '% Inf1',
        '% Inf2',
        '% Inf3',
        '% Inf5',
        '% PrsPrc',
        '% PrsPrc% Act',
        '% PrsPrc% Pass',
        '% PrfPrc',
        '% PrfPrc% Act',
        '% PrfPrc% Pass',
        '% AgPrc',
        '% NegPrc',
        '% Pos',
        '% Comp',
        '% Superl',
        "% Dem",
        "% Qnt",
        "% Pers",
        "% Indef",
        "% Interr",
        "% Refl",
        "% Rel",
        '% Ord',
        '% Foc_hAn',
        '% Foc_kAAn',
        '% Foc_kin',
        '% Foc_kO',
        '% Foc_pA',
        '% Foc_s',
        '% Foc_kA',
        '% Man',
        '%<Del%>→',
        '←%<Del%>'}


stuff2ftb3 = {"Bc": "#",
        ".sent": "",
        "B-": "% TrunCo",
        "B→": "TrunCo% ",
        "B←": "% TrunCo",
        "Cma": "% AgPrc",
        "Cmaisilla": "% Adv",
        "Cnut": "% PrfPrc",
        "Cva": "% PrsPrc",
        "Cmaton": "% NegPrc",
        "Cpos": "% Pos",
        "Ccmp": "% Comp",
        "Csup": "% Superl",
        "Dmaisilla": "% Inf5",
        "Dminen": "% N",
        "Dnut": "% PrfPrc% Act",
        "Dtu": "% PrfPrc% Pass",
        "Dva": "% PrsPrc% Act",
        "Dtava": "% PrsPrc% Pass",
        "Dmaton": "% NegPrc",
        "Duus": "",
        "Dttaa": "",
        "Dtattaa": "",
        "Dtatuttaa": "",
        "Dma": "% AgPrc",
        "Dinen": "",
        "Dja": "",
        "Dmpi": "",
        "Din": "",
        "Ds": "",
        "Du": "",
        "Dsti": "",
        "FTB3man": "% Man",
        "Ia": "% Inf1",
        "Ie": "% Inf2",
        "Ima": "% Inf3",
        "Iminen": "% N",
        "Ncon": "% ConNeg",
        "Nneg": "% Neg", 
        "Npl": "% Pl", 
        "Nsg": "% Sg", 
        "N??": "% Sg",
        "Osg1": "% PxSg1",
        "Osg2": "% PxSg2",
        "O3": "% Px3",
        "Opl1": "% PxPl1",
        "Opl2": "% PxPl2",
        "Ppl1": "% Pl1", 
        "Ppl2": "% Pl2",
        "Ppl3": "% Pl3",
        "Psg1": "% Sg1", 
        "Psg2": "% Sg2",
        "Psg3": "% Sg3",
        "Ppe4": "% Pe4", 
        "Qka": "% Foc_kA",
        "Qs": "% Foc_s",
        "Qpa": "% Foc_pA",
        "Qko": "% Foc_kO",
        "Qkin": "% Foc_kin",
        "Qkaan": "% Foc_kAAn",
        "Qhan": "% Foc_hAn",
        "Tcond": "% Cond",
        "Timp": "% Impv", 
        "Tpast": "% Pst",
        "Tpot": "% Pot", 
        "Tpres": "% Prs",
        "Topt": "% Opt",
        "Uarch": "", "Udial": "", "Urare": "", "Unonstd": "",
        "Vact": "% Act",
        "Vpss": "% Pass",
        "Xabe": "% Abe",
        "Xabl": "% Abl",
        "Xade": "% Ade",
        "Xall": "% All",
        "Xcom": "% Com",
        "Xela": "% Ela",
        "Xess": "% Ess", 
        "Xgen": "% Gen",
        "Xill": "% Ill", 
        "Xine": "% Ine",
        "Xins": "% Ins",
        "Xnom": "% Nom",
        "Xpar": "% Par", 
        "Xtra": "% Tra", 
        "Xlat": "% Lat",
        "Xacc": "% Acc",
        "X???": "% Nom",
        "NOUN": "% N",
        "ADJECTIVE": "% A", "QUALIFIER": "% A",
        "VERB": "% V",
        "ADVERB": "% Adv",
        "INTERJECTION": "% Interj",
        "PRONOUN": "% Pron",
        "NUMERAL": "% Num",
        "ADPOSITION": "% Adp% Po",
        "CONJUNCTION": "", "COORDINATING": "% CC", "ADVERBIAL": "% CS",
        "COMPARATIVE": "% CS",
        "ABBREVIATION": "% Abbr", "ACRONYM": "% N% Abbr",
        "PROPER": "% Prop",
        "CARDINAL": "", "ORDINAL": "% Ord",
        "DEMONSTRATIVE": "% Dem", "QUANTOR": "% Qnt", "PERSONAL": "% Pers",
        "INDEFINITE": "% Indef", "INTERROGATIVE": "% Interr",
        "REFLEXIVE": "% Refl", "RELATIVE": "% Rel",
        "RECIPROCAL": "",
        "PUNCTUATION": "% Punct",
        "DASH": "% Dash",
        "SPACE": "",
        "DECIMAL": "",
        "CLAUSE-BOUNDARY": "",
        "SENTENCE-BOUNDARY": "",
        "INITIAL-QUOTE": "% Quote",
        "FINAL-QUOTE": "% Quote",
        "INITIAL-BRACKET": "",
        "FINAL-BRACKET": "",
        "DIGIT": "% Digit",
        "ROMAN": "% Roman",
        "PL1": "% Pl1", 
        "PL2": "% Pl2",
        "PL3": "% Pl3",
        "SG1": "% Sg1", 
        "SG2": "% Sg2",
        "SG3": "% Sg3",
        "PE4": "% Pe4",
        "COMP": "% Comp",
        "SUPERL": "% Superl",
        "UNSPECIFIED": "% Adv",
        "LEMMA-START": "",
        "": ""
        }

def format_tag_ftb3(stuff):
    if stuff == '0':
        return "0"
    elif stuff in stuff2ftb3:
        return stuff2ftb3[stuff]
    else:
        fail_formatting_missing_for(stuff, "ftb3.1")
        return ""

def format_analysis_lexc_ftb3(anals):
    ftbstring = ""
    if 'Nneg|Vact' in anals:
        anals = anals.replace('|Vact', '')
    elif anals == 'Vact|Ia|Xlat':
        anals = 'Ia|Xlat'
    elif anals == 'Vact|Ima|Xins':
        anals = 'Ima|FTB3man'
    elif 'Vact|Ima' in anals:
        anals = anals.replace('Vact|', '')
    elif anals == 'Vact|Ie|Nsg|Xins':
        anals = 'Ie|Vact|Xins'
    elif anals == 'Vact|Tpres|Ppe4|Ncon':
        anals = 'Vact|Tpres|Ncon'
    elif anals == 'Vpss|Tpres|Ppe4|Ncon':
        anals = 'Vpss|Tpres|Ncon'
    elif 'Dmaton' in anals:
        anals = anals.replace('Dmaton', 'Cmaton')
    elif 'Dma' in anals:
        anals = anals.replace('Dma', 'Cma')
    parts = anals.split('|')
    # Here is a bit of puzzle
    # I < X
    # V < X
    # T < V
    # C < V
    # X < S
    # -----
    # I < T,C < V < X < N
    reordered = []
    # append I first
    for part in parts:
        if part.startswith('I'):
            # Infinitive I before case X
            reordered.append(part)
    # then T or C
    for part in parts:
        if part.startswith('T'):
            # Tense T before Voice V
            reordered.append(part)
        elif part.startswith('C'):
            # Participle C before voice V
            reordered.append(part)
    # then V
    for part in parts:
        if part.startswith('V'):
            # Voice V before Case X
            reordered.append(part)
    # then X
    for part in parts:
        if part.startswith('X'):
            # Case X before Number N
            reordered.append(part)
    # then rest in their natural order
    parts = [x for x in parts if not x.startswith('X') and not x.startswith('T') and not x.startswith('C') and not x.startswith('I') and not x.startswith('V')]
    for part in parts:
        reordered.append(part)
    for anal in reordered:
        ftbstring += format_tag_ftb3(anal)
    return ftbstring

def format_continuation_lexc_ftb3(anals, surf, cont):
    ftbstring = format_analysis_lexc_ftb3(anals)
    if 'COMPOUND' in cont:
        # XXX: there was += before
        ftbstring =  surf.replace(morph_boundary, '').replace(deriv_boundary, '')
    elif 'NUM_' in cont and ('BACK' in cont or 'FRONT' in cont and not ('CLIT' in cont or 'POSS' in cont)):
        ftbstring +=  surf.replace(morph_boundary, '').replace(deriv_boundary, '')
    elif 'DIGITS_' in cont and not ('BACK' in cont or 'FRONT' in cont):
        ftbstring = lexc_escape(surf) + ftbstring
    surf = lexc_escape(surf)
    return "%s:%s\t%s ;\n" %(ftbstring, surf, cont)

def format_lexc_ftb3(wordmap, format):
    '''
    format string for canonical ftb3 format for morphological analysis
    '''
    if wordmap['stub'] == ' ':
        # do not include normal white space for now
        return ""
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    wordmap['analysis'] = "%s" %(lexc_escape(wordmap['bracketstub'].replace(word_boundary, '#')  + '←<Del>'))
    if (wordmap['pos'] == 'ACRONYM' and (len(wordmap['stub']) == 1 and not wordmap['stub'].isalpha())) or wordmap['stub'] == '§§':
        wordmap['analysis'] += format_tag_ftb3('PUNCTUATION')
    elif wordmap['pos'] in ['NOUN', 'VERB', 'ADJECTIVE', 'PRONOUN', 'NUMERAL', 'ACRONYM', 'PUNCTUATION']:
        wordmap['analysis'] += format_tag_ftb3(wordmap['pos'])
    elif wordmap['pos'] == 'CONJUNCTIONVERB':
        if wordmap['lemma'] == 'eikä':
            wordmap['lemma'] = 'ei'
            wordmap['analysis'] = format_tag_ftb3('COORDINATING') + \
                    format_tag_ftb3('Nneg')
        else:
            wordmap['analysis'] = format_tag_ftb3('ADVERBIAL') + \
                    format_tag_ftb3('Nneg')
    elif wordmap['particle']:
        for pclass in wordmap['particle'].split('|'):
            wordmap['analysis'] += format_tag_ftb3(pclass)
    else:
        print("not in FTB3 known poses or particle!\n", wordmap)
        exit(1)
    if wordmap['subcat']:
        if 'PERSONAL' in wordmap['subcat']:
            wordmap['subcat'] = 'PERSONAL'
        for subcat in wordmap['subcat'].split('|'):
            wordmap['analysis'] += format_tag_ftb3(subcat)
    if wordmap['is_proper']:
        wordmap['analysis'] += format_tag_ftb3('PROPER')
    if wordmap['symbol']:
        for subcat in wordmap['symbol'].split('|'):
            wordmap['analysis'] += format_tag_ftb3(subcat)
        if wordmap['lemma'] == '–':
            wordmap['analysis'].replace('Dash', 'EnDash')
        if wordmap['lemma'] == '—':
            wordmap['analysis'].replace('Dash', 'EmDash')
    lex_stub = wordmap['stub']
    retvals = []
    for new_para in wordmap['new_paras']:
        retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, 
                new_para)]
    if wordmap['lemma'] in ['-', '–', '—', '(']:
        retvals += ["%s%% %%>%%>%%>:%s\t%s\t;" %(wordmap['analysis'], lex_stub,
            new_para)]
    return "\n".join(retvals)

def format_multichars_lexc_ftb3():
    multichars = "!! FTB 3.1 multichar set:\n"
    for mcs in ftb3_multichars:
        multichars += mcs + "\n"
    return multichars

# self test
if __name__ == '__main__':
    fail = False
    for stuff, ftb3 in stuff2ftb3.items():
        if len(ftb3) < 2:
            continue
        elif not ftb3 in ftb3_multichars:
            print("There are conflicting formattings in here!", ftb3, 
                    "is not a valid defined ftb3 multichar_symbol!")
            fail = True
    if fail:
        exit(1)

