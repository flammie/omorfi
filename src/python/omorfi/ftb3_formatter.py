#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to format FTB 3.1 style analyses from omorfi data."""

# Author: Omorfi contributors <omorfi-devel@groups.google.com> 2015

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# utils to format apertium style data from omorfi database values

from .lexc_formatter import lexc_escape
from .settings import word_boundary, weak_boundary, \
        morph_boundary, deriv_boundary, optional_hyphen
from .error_logging import fail_formatting_missing_for


ftb3_multichars= {
        '% A',
        '% V',
        '% N',
        '% Part',
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
        '% Adp% Pr',
        '% Punct',
        '% Quote',
        '% EmDash',
        '% EnDash',
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
        '% Foc%_hAn',
        '% Foc%_kAAn',
        '% Foc%_kin',
        '% Foc%_kO',
        '% Foc%_pA',
        '% Foc%_s',
        '% Foc%_kA',
        '% Man',
        '%<Del%>→',
        '←%<Del%>'}


stuff2ftb3 = {"Bc": "#",
        ".sent": "",
        "Aiden": "",
        "Aien": "",
        "Aiin": "",
        "Ain": "",
        "Ayn": "",
        "Aän": "",
        "Aön": "",
        "Aisiin": "",
        "Aseen": "",
        "Aä": "",
        "Ajä": "",
        "Atä": "",
        "Ajen": "",
        "Aten": "",
        "Ahin": "",
        "Ahen": "",
        "Ahyn": "",
        "Aihin": "",
        "Aiä": "",
        "Ana": "",
        "Asa": "",
        "Aitten": "",
        "Aan": "",
        "Aen": "",
        "Ahan": "",
        "Ahon": "",
        "Ahun": "",
        "Aon": "",
        "Aun": "",
        "Aa": "",
        "Aia": "",
        "Aita": "",
        "Aja": "",
        "Ahän": "",
        "Ahön": "",
        "Aitä": "",
        "Ata": "",
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
        "Dttain": "",
        "FTB3man": "% Man",
        "FTB3MAN": "% Man",
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
        "Qka": "% Foc%_kA",
        "Qs": "% Foc%_s",
        "Qpa": "% Foc%_pA",
        "Qko": "% Foc%_kO",
        "Qkin": "% Foc%_kin",
        "Qkaan": "% Foc%_kAAn",
        "Qhan": "% Foc%_hAn",
        "Tcond": "% Cond",
        "Timp": "% Impv", 
        "Tpast": "% Pst",
        "Tpot": "% Pot", 
        "Tpres": "% Prs",
        "Topt": "% Opt",
        "Uarch": "",
        "Udial": "",
        "Urare": "",
        "Unonstd": "",
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
        "ADJ": "% A", 
        "ADJECTIVE": "% A", 
        "QUALIFIER": "% A",
        "ABESSIVE": "% Abe",
        "ABLATIVE": "% Abl",
        "ADESSIVE": "% Ade",
        "ALLATIVE": "% All",
        "ELATIVE": "% Ela",
        "LOCATIVE": "% Ess", 
        "GENITIVE": "% Gen",
        "ILLATIVE": "% Ill", 
        "INESSIVE": "% Ine",
        "INSTRUCTIVE": "% Man",
        "PARTITIVE": "% Par", 
        "SEPARATIVE": "% Par", 
        "LATIVE": "% Lat",
        "VERB": "% V",
        "ADV": "% Adv",
        "INTJ": "% Interj",
        "PRONOUN": "% Pron",
        "PRON": "% Pron",
        "NUMERAL": "% Num",
        "NUM": "% Num",
        "ADP": "% Adp% Po",
        "PREPOSITION": "% Adp% Pr",
        "CONJ": "% CC",
        "SCONJ": "% CS",
        "COORDINATING": "",
        "ADVERBIAL": "",
        "COMPARATIVE": "",
        "ABBREVIATION": "% Abbr",
        "ACRONYM": "% N% Abbr",
        "PROPER": "% Prop",
        "CARDINAL": "", "ORDINAL": "% Ord",
        "DEMONSTRATIVE": "% Dem",
        "QUANTOR": "% Qnt",
        "PERSONAL": "% Pers",
        "INDEFINITE": "% Indef",
        "INTERROGATIVE": "% Interr",
        "REFLEXIVE": "% Refl",
        "RELATIVE": "% Rel",
        "PARTICLE": "% Part",
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
        "DERSTI": "",
        "DERTTAIN": "",
        "UNSPECIFIED": "% Adv",
        "LEMMA-START": "",
        "COMMA": "",
        "ARROW": "",
        ".": ".",
        "X": "",
        "": ""
        }

def format_stuff_ftb3(stuff):
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
        anals = 'Ie|Vact|FTB3man'
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
    parts = [x for x in parts \
            if not x.startswith('X') and not x.startswith('T') \
            and not x.startswith('C') and not x.startswith('I') \
            and not x.startswith('V')]
    for part in parts:
        reordered.append(part)
    for anal in reordered:
        ftbstring += format_stuff_ftb3(anal)
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

def format_wordmap_lexc_ftb3(wordmap, format):
    '''
    format string for canonical ftb3 format for morphological analysis
    '''
    if wordmap['stub'] == ' ':
        # do not include normal white space for now
        return ""
    wordmap['stub'] = lexc_escape(wordmap['stub'].replace(word_boundary, optional_hyphen))
    wordmap['analysis'] = "%s" %(lexc_escape(wordmap['bracketstub'].replace(word_boundary, '#')  + '←<Del>'))
    if (wordmap['pos'] == 'ACRONYM' and (len(wordmap['stub']) == 1 and \
            not wordmap['stub'].isalpha())) or wordmap['stub'] == '§§':
        wordmap['analysis'] += format_stuff_ftb3('PUNCTUATION')
    elif wordmap['pos'] in ['NOUN', 'VERB', 'ADJECTIVE', 'PRONOUN', 'NUMERAL', 'ACRONYM', 'PUNCTUATION']:
        wordmap['analysis'] += format_stuff_ftb3(wordmap['pos'])
    elif wordmap['pos'] == 'CONJUNCTIONVERB':
        if wordmap['lemma'] == 'eikä':
            wordmap['lemma'] = 'ei'
            wordmap['analysis'] += format_stuff_ftb3('COORDINATING') + \
                    format_stuff_ftb3('Nneg')
        else:
            wordmap['analysis'] += format_stuff_ftb3('ADVERBIAL') + \
                    format_stuff_ftb3('Nneg')
    elif wordmap['pos'] == 'PARTICLE':
        if wordmap['particle']:
            for pclass in wordmap['particle'].split('|'):
                wordmap['analysis'] += format_stuff_ftb3(pclass)
        else:
            wordmap['analysis'] += format_stuff_ftb3('PARTICLE')
    else:
        print("not in FTB3 known poses or particle!\n", wordmap)
        exit(1)
    if wordmap['pronoun']:
        if 'PERSONAL' in wordmap['pronoun']:
            wordmap['pronoun'] = 'PERSONAL'
        for stuff in wordmap['pronoun'].split("|"):
            wordmap['analysis'] += format_stuff_ftb3(stuff)
    if wordmap['adjective_class']:
        for stuff in wordmap['adjective_class'].split("|"):
            wordmap['analysis'] += format_stuff_ftb3(stuff)
    if wordmap['noun_class']:
        for stuff in wordmap['noun_class'].split("|"):
            wordmap['analysis'] += format_stuff_ftb3(stuff)
    if wordmap['numeral_class']:
        for stuff in wordmap['numeral_class'].split("|"):
            wordmap['analysis'] += format_stuff_ftb3(stuff)
    if wordmap['is_proper']:
        wordmap['analysis'] += format_stuff_ftb3('PROPER')
    if wordmap['symbol']:
        for subcat in wordmap['symbol'].split('|'):
            wordmap['analysis'] += format_stuff_ftb3(subcat)
        if wordmap['lemma'] == '–':
            wordmap['analysis'].replace('Dash', 'EnDash')
        if wordmap['lemma'] == '—':
            wordmap['analysis'].replace('Dash', 'EmDash')
    lex_stub = wordmap['stub']
    retvals = []
    retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, 
                wordmap['new_para'])]
    if wordmap['lemma'] in ['-', '–', '—', '(']:
        retvals += ["%s%% %%>%%>%%>:%s\t%s\t;" %(wordmap['analysis'], lex_stub,
            wordmap['new_para'])]
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

