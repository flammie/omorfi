#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to format Turku Dependency Treebank style analyses from omorfi data."""

from sys import stderr

from .lexc_formatter import lexc_escape
from .omor_formatter import OmorFormatter

tdt_multichars = {
    '% A',
    '% Adp',
    '% Adv',
    '% C',
    '% Foreign',
    '% Interj',
    '% N',
    '% Num',
    '% Pron',
    '% Punct',
    '% Symb',
    '% V',
    '% SUBCAT_QUALIFIER', 'SUBCAT_INTERJECTION',
    '% SUBCAT_Dem', 'SUBCAT_PERSONAL', 'SUBCAT_INTERROG',
    '% SUBCAT_RELATIVE', 'SUBCAT_QUANTOR', 'SUBCAT_REFLEXIVE',
    '% SUBCAT_RECIPROC', 'SUBCAT_Indef',
    '% SUBCAT_INTERROGATIVE',
    '% SUBCAT_CARD', 'SUBCAT_ORD',
    '% SUBCAT_CONJUNCTION', '[CONJ_COORD', '[CONJ_ADVERBIAL',
    '[CONJ_COMPARATIVE', '% SUBCAT_POSTPOSITION', 'SUBCAT_PREPOSITION',
    '% SUBCAT_PREFIX', 'SUBCAT_SUFFIX', 'SUBCAT_ABBREVIATION',
    '% SUBCAT_ACRONYM',
    '[POS_PUNCTUATION', '[POS_SYMBOL',
    '% SUBCAT_SPACE', 'SUBCAT_QUOTATION', 'SUBCAT_BRACKET',
    '% SUBCAT_DASH', 'SUBCAT_CURRENCY', 'SUBCAT_MATH',
    '% SUBCAT_OPERATION', 'SUBCAT_RELATION', 'SUBCAT_INITIAL',
    '% SUBCAT_FINAL', 'SUBCAT_REFLEXIVE', 'SUBCAT_DIGIT',
    '% SUBCAT_ROMAN', 'SUBCAT_DECIMAL',
    '|CASE_Nom', '|CASE_Par', '|CASE_Gen', '|CASE_Ine', '|CASE_Ela',
    '|CASE_Ill', '|CASE_Ade', '|CASE_Abl', '|CASE_All', '|CASE_Ess',
    '|CASE_Ins', '|CASE_Abe', '|CASE_Tra', '|CASE_Com', '|CASE_Lat',
    '|CASE_Acc', '|NUM_Sg', '|NUM_Pl', '[POSS_SG1', '[POSS_SG2',
    '[POSS_SG3', '[POSS_PL1', '[POSS_PL2', '[POSS_PL3',
    '[POSS_3',
    '[BOUNDARY_COMPOUND', '[COMPOUND_FORM_S', '[COMPOUND_FORM_OMIT',
    '[TENSE_PRESENT',
    '[TENSE_PAST', '[MOOD_INDV', '[MOOD_COND', '[MOOD_POTN',
    '[MOOD_IMPV', '[MOOD_OPT', '[MOOD_EVNV',
    '[MOOD_INDV][TENSE_PAST',
    '[PERS_SG1', '[PERS_SG2', '[PERS_SG3',
    '[PERS_PL1', '[PERS_PL2', '[PERS_PL3', '[PERS_PE4',
    '[NEG_CON', '% SUBCAT_NEG', '[VOICE_ACT', '[VOICE_PSS',
    '[INF_A', '[INF_E', '[INF_MA', '[INF_MINEN', '[INF_MAISILLA',
    '|DRV_Der_MINEN', '|DRV_Der_MAISILLA',
    '[PCP_NUT', '[PCP_AGENT', '[PCP_VA', '[PCP_NEG',
    '|DRV_Der_NUT', '|DRV_Der_TU', '|DRV_Der_MA', '|DRV_Der_VA', '|DRV_Der_MATON',
    '[CMP_POS', '[CMP_CMP', '[CMP_SUP',
    '|DRV_Der_MPI', '|DRV_Der_IN',
    '|CLIT_Foc_han', '|CLIT_Foc_kaan', '|CLIT_Foc_kin', '|CLIT_Foc_Qst',
    '|CLIT_Foc_pa', '|CLIT_Foc_s', '|CLIT_Foc_ka',
    '|DRV_Der_STI', '|DRV_Der_JA',
    '|DRV_Der_INEN', '|DRV_Der_LAINEN', '|DRV_Der_TAR', '|DRV_Der_LLINEN', '|DRV_Der_TON',
    '|DRV_Der_TSE', '|DRV_Der_OI', '|DRV_Der_VS', '|DRV_Der_U', '|DRV_Der_TTAIN',
    '|DRV_Der_TTAA', '|DRV_Der_TATTAA', '|DRV_Der_TATUTTAA', '|DRV_Der_UUS',
    '|DRV_Der_S', '|DRV_Der_STI', '|DRV_Der_NUT', '|DRV_Der_TAVA',
    '[STYLE_NONSTANDARD', '[STYLE_RARE', '[STYLE_DIALECTAL',
    '[STYLE_ARCHAIC',
    '[GUESS_COMPOUND', '[GUESS_DERIVE', '[ALLO_A',
    '[ALLO_TA', '[ALLO_HVN', '[ALLO_IA', '[ALLO_IDEN', '[ALLO_ITA',
    '[ALLO_ITTEN', '[ALLO_IEN', '[ALLO_IHIN', '[ALLO_IIN', '[ALLO_IN',
    '[ALLO_ISIIN', '[ALLO_IDEN', '[ALLO_JA', '[ALLO_JEN', '[ALLO_SEEN',
    '[ALLO_TEN', '[ALLO_VN', '[FILTER_NO_PROC',
    '[PROPER_FIRST', '[PROPER_GEO', '[PROPER_LAST',
    '[PROPER_MISC', '[PROPER_ORG', '[PROPER_PRODUCT', '[PROPER_EVENT',
    '[PROPER_MEDIA', '[PROPER_CULTGRP', '[PROPER_ARTWORK', '[SEM_TITLE',
    '[SEM_ORG', '[SEM_EVENT', '[SEM_POLIT', '[SEM_MEDIA', '[SEM_GEO',
    '[SEM_COUNTRY', '[SEM_INHABITANT', '[SEM_LANGUAGE',
    '[SEM_MEASURE', '[SEM_CURRENCY', '[SEM_TIME', '[SEM_MALE', '[SEM_FEMALE',
    '[POSITION_PREFIX', '[POSITION_SUFFIX',
    '[POS_NOUN]% SUBCAT_ABBREVIATION',
    '[MOOD_INDV][TENSE_PRESENT',
    '[MOOD_INDV][TENSE_PAST'
    "% SUBCAT_DASH]", "SUBCAT_SPACE]",
    "[BOUNDARY_CLAUSE]", "[BOUNDARY_SENTENCE]",
    "% SUBCAT_QUOTATION][POSITION_INITIAL]",
    "% SUBCAT_QUOTATION][POSITION_FINAL]",
    "% SUBCAT_BRACKET][POSITION_INITIAL]",
    "% SUBCAT_BRACKET][POSITION_FINAL]",
    "[POS_VERB]% SUBCAT_NEG]"
}

stuff2tdt = {
    ".sent": "[BOUNDARY_SENTENCE]",
    "Bc": "[BOUNDARY_COMPOUND]",
    "B-": "[COMPOUND_FORM_OMIT]",
    "B→": "[POSITION_SUFFIX]",
    "B←": "[POSITION_PREFIX]",
    "Cma": "[PCP_AGENT]",
    "Cmaton": "[PCP_NEG]",
    "Cva": "[PCP_VA]",
    "Cnut": "[PCP_NUT]",
    "Cpos": "",
    # "Cpos": "[CMP_POS]",
    "Ccmp": "[CMP_CMP]",
    "Csup": "[CMP_SUP]",
    "Dinen": "|DRV_Der_INEN]",
    "Dja": "|DRV_Der_JA]",
    "Dmaisilla": "[INF_MAISILLA]",
    # "Dmaisilla": "|DRV_Der_MAISILLA]",
    "Dminen": "|DRV_Der_MINEN]",
    "Dtu": "|DRV_Der_TU]",
    "Dnut": "|DRV_Der_NUT]",
    "Dva": "|DRV_Der_VA]",
    "Dtava": "|DRV_Der_TAVA]",
    "Dma": "|DRV_Der_MA]",
    "Dmaton": "|DRV_Der_MATON]",
    "Ds": "|DRV_Der_S]",
    "Dsti": "|DRV_Der_STI]",
    "Dttaa": "|DRV_Der_TTAA]",
    "Dtattaa": "|DRV_Der_TATTAA]",
    "Dtatuttaa": "|DRV_Der_TATUTTAA]",
    "Du": "|DRV_Der_U]",
    "Duus": "|DRV_Der_UUS]",
    "Dmpi": "",
    # "Dmpi": "|DRV_Der_MPI]",
    "Din": "",
    # "Din": "|DRV_Der_IN]",
    "Ia": "[INF_A]",
    "Ie": "[INF_E]",
    "Ima": "[INF_MA]",
    "Iminen": "[INF_MINEN]",
    "Ncon": "[NEG_CON]",
    "Nneg": "% SUBCAT_NEG]",
    "Npl": "[NUM_PL]",
    "Nsg": "[NUM_SG]",
    "N??": "",
    "Osg1": "[POSS_SG1]", "Osg2": "[POSS_SG2]", "O3": "[POSS_3]",
    "Opl1": "[POSS_PL1]", "Opl2": "[POSS_PL2]",
    "Ppl1": "[PERS_PL1]", "Ppl2": "[PERS_PL2]",
    "Ppl3": "[PERS_PL3]", "Psg1": "[PERS_SG1]", "Psg2": "[PERS_SG2]",
    "Psg3": "[PERS_SG3]", "Ppe4": "[PERS_PE4]",
    "Qka": "CLIT_Foc_ka]", "Qs": "CLIT_Foc_s]",
    "Qpa": "CLIT_Foc_pa]", "Qko": "CLIT_Foc_ko]",
    "Qkin": "CLIT_Foc_kin]",
    "Qkaan": "CLIT_Foc_kaan]",
    "Qhan": "CLIT_Foc_han]",
    "Tcond": "[MOOD_COND]",
    "Timp": "[MOOD_IMPV]",
    "Tpast": "[MOOD_INDV][TENSE_PAST]",
    "Tpot": "[MOOD_POTN]",
    "Topt": "[MOOD_OPT]",
    "Tpres": "[MOOD_INDV][TENSE_PRESENT]",
    "Uarch": "[STYLE_ARCHAIC]",
    "Udial": "[STYLE_DIALECTAL]",
    "Unonstd": "[STYLE_NONSTANDARD]",
    "Urare": "[STYLE_RARE]",
    "Vact": "[VOICE_ACT]", "Vpss": "[VOICE_PSS]",
    "Xabe": "|CASE_Abe", "Xabl": "|CASE_Abl",
    "Xade": "|CASE_Ade", "Xall": "|CASE_All",
    "Xcom": "|CASE_Com", "Xela": "|CASE_Ela",
    "Xess": "|CASE_Ess", "Xgen": "|CASE_Gen",
    "Xill": "|CASE_Ill", "Xine": "|CASE_Ine",
    "Xins": "|CASE_Ins", "Xnom": "|CASE_Nom",
    "Xpar": "|CASE_Par", "Xtra": "|CASE_Tra",
    "Xlat": "|CASE_Lat", "Xacc": "|CASE_Acc",
    "X???": "",
    "NOUN": "% N",
    "PARTICLE": "% X",
    "VERB": "% V",
    "ADVERB": "% Adv",
    "ADJECTIVE": "% A",
    "CONJUNCTION": "% C",
    "COORDINATING": "SUBCAT_CC",
    "COMPARATIVE": "SUBCAT_CS",
    "PRONOUN": "% Pron",
    "ADVERBIAL": "SUBCAT_CS",
    "NUMERAL": "% Num",
    "CARDINAL": "SUBCAT_Card",
    "ORDINAL": "SUBCAT_Ord",
    "DIGIT": "",
    "DECIMAL": "% SUBCAT_DECIMAL]",
    "ROMAN": "% SUBCAT_ROMAN]",
    "QUALIFIER": "% SUBCAT_QUALIFIER]",
    "ACRONYM": "[POS_NOUN]% SUBCAT_ABBREVIATION]",
    "ABBREVIATION": "% SUBCAT_ABBREVIATION]",
    "SUFFIX": "",
    # "SUFFIX": "% SUBCAT_SUFFIX]",
    "PREFIX": "",
    # "PREFIX": "% SUBCAT_PREFIX]",
    "INTERJECTION": "% SUBCAT_INTERJECTION]",
    "ADPOSITION": "[POS_ADPOSITION]",
    "DEMONSTRATIVE": "% SUBCAT_Dem",
    "QUANTOR": "% SUBCAT_QUANTOR]",
    "PERSONAL": "% SUBCAT_PERSONAL]",
    "INDEFINITE": "% SUBCAT_Indef",
    "INTERROGATIVE": "% SUBCAT_INTERROGATIVE]",
    "REFLEXIVE": "% SUBCAT_REFLEXIVE]",
    "RELATIVE": "% SUBCAT_RELATIVE]",
    "RECIPROCAL": "% SUBCAT_RECIPROC]",
    "PL1": "[PERS_PL1]", "PL2": "[PERS_PL2]",
    "PL3": "[PERS_PL3]", "SG1": "[PERS_SG1]", "SG2": "[PERS_SG2]",
    "SG3": "[PERS_SG3]", "PE4": "[PERS_PE4]",
    "COMP": "[CMP_CMP]",
    "SUPERL": "[CMP_SUP]",
    "ARCHAIC": "[STYLE_ARCHAIC]",
    "DIALECTAL": "[STYLE_DIALECTAL]",
    "NONSTANDARD": "[STYLE_NONSTANDARD]",
    "RARE": "[STYLE_RARE]",
    "TITLE": "[SEM_TITLE]", "TIME": "[SEM_TIME]",
    "CURRENCY": "[SEM_CURRENCY]", "MEDIA": "[SEM_MEDIA]",
    "POLIT": "[SEM_POLIT]", "MEASURE": "[SEM_MEASURE]",
    "MALE": "[SEM_MALE]", "FEMALE": "[SEM_FEMALE]",
    "PROPER": "[PROPER_PROPER]",
    "CULTGRP": "[PROPER_CULTGRP]", "PRODUCT": "[PROPER_PRODUCT]",
    "ARTWORK": "[PROPER_ARTWORK]", "EVENT": "[PROPER_EVENT]",
    "FIRST": "[PROPER_FIRST]", "LAST": "[PROPER_LAST]",
    "GEO": "[PROPER_GEO]", "ORG": "[PROPER_ORG]",
    "MISC": "[PROPER_MISC]",
    "COUNTRY": "[SEM_COUNTRY]",
    "INHABITANT": "[SEM_INHABITANT]",
    "LANGUAGE": "[SEM_LANGUAGE]",
    "PUNCTUATION": "[POS_PUNCTUATION]",
    "DASH": "% SUBCAT_DASH]",
    "SPACE": "% SUBCAT_SPACE]",
    "CLAUSE-BOUNDARY": "[BOUNDARY_CLAUSE]",
    "SENTENCE-BOUNDARY": "[BOUNDARY_SENTENCE]",
    "INITIAL-QUOTE": "% SUBCAT_QUOTATION][POSITION_INITIAL]",
    "FINAL-QUOTE": "% SUBCAT_QUOTATION][POSITION_FINAL]",
    "INITIAL-BRACKET": "% SUBCAT_BRACKET][POSITION_INITIAL]",
    "FINAL-BRACKET": "% SUBCAT_BRACKET][POSITION_FINAL]",
    "UNSPECIFIED": "",
    "FTB3man": "",
    "LEMMA-START": "[WORD_ID_",
    "CONJUNCTIONVERB": "% V% SUBCAT_NEG",
    "": ""}


def format_tag_tdt(stuff, format):
    if stuff == '0':
        return "0"
    if stuff in stuff2tdt:
        return stuff2tdt[stuff]
    else:
        print("Missing from tdt mapping: ", stuff, file=stderr)
        return ""


def format_analysis_lexc_tdt(anals, format):
    tdtstring = ''
    for tag in anals.split('|'):
        tdtstring += format_tag_tdt(tag, format)
    return tdtstring


def format_continuation_lexc_tdt(anals, surf, cont, format):
    tdtstring = ''
    if 'DIGITS_' in cont and not ('BACK' in cont or 'FRONT' in cont):
        tdtstring = lexc_escape(surf)
        if anals and anals != 'LEMMA-START':
            tdtstring += ']'

    # Collapse DRV_Der=NUT/TU and PCP=NUT to PCP=NUT with full inflection
    if anals == 'Dnut':
        anals = 'Vact|Cnut'
    elif anals == 'Dtu':
        anals = 'Vpss|Cnut'
    # Collapse DRV_Der=VA/TAVA and PCP=VA to PCP=VA with full inflection
    elif anals == 'Dva':
        anals = 'Vact|Cva'
    elif anals == 'Dtava':
        anals = 'Vpss|Cva'
    # Collapse DRV_Der=MA and PCP=AGENT to PCP=AGENT with full inflection
    elif anals == 'Dma':
        anals = 'Cma'
    # Collapse DRV_Der=MATON and PCP=NEG to PCP=NEG with full inflection
    elif anals == 'Dmaton':
        anals = 'Cmaton'
    elif ('Cnut' in anals or 'Cva' in anals or 'Cma' in anals or 'Cmaton' in anals) and \
         (anals.endswith('Npl') or anals.endswith('Nsg')):
        anals = anals + '|Xnom'

    tags = anals.split('|')
    for tag in tags:
        tdtstring += format_tag_tdt(tag, format)
    surf = lexc_escape(surf)
    return "%s:%s\t%s ;\n" % (tdtstring, surf, cont)


def format_lexc_tdt(wordmap, format):
    '''
    format string for canonical tdt format for morphological analysis
    '''
    if wordmap['stub'] == ' ':
        # do not include normal white space for now
        return ""
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    wordmap['analysis'] = "[WORD_ID=%s]" % (lexc_escape(wordmap['lemma']))
    wordmap['particle'] = wordmap['particle'].replace('QUALIFIER', 'ADJECTIVE')
    if wordmap['pos'] != 'PARTICLE' or not wordmap['particle'].startswith('AD'):
        wordmap['analysis'] += format_tag_tdt(wordmap['pos'], format)
    if wordmap['is_suffix']:
        wordmap['analysis'] += format_tag_tdt('SUFFIX', format)
    if wordmap['is_prefix']:
        wordmap['analysis'] += format_tag_tdt('PREFIX', format)
        if wordmap['pos'] == 'ADJECTIVE':
            wordmap['analysis'] += format_tag_tdt('Cpos', format)

    if wordmap['particle']:
        for pclass in wordmap['particle'].split('|'):
            wordmap['analysis'] += format_tag_tdt(pclass, format)

    if wordmap['symbol']:
        for subcat in wordmap['symbol'].split('|'):
            wordmap['analysis'] += format_tag_tdt(subcat, format)

    if wordmap['subcat']:
        for subcat in wordmap['subcat'].split('|'):
            wordmap['analysis'] += format_tag_tdt(subcat, format)

    if wordmap['is_proper']:
        if '+propers' in format and wordmap['proper_noun_class']:
            for prop in wordmap['proper_noun_class'].split(','):
                wordmap['analysis'] += format_tag_tdt(prop, format)
        else:
            wordmap['analysis'] += format_tag_tdt('PROPER', format)

    if '+semantics' in format and wordmap['sem']:
        for sem in wordmap['sem'].split(','):
            wordmap['analysis'] += format_tag_tdt(sem, format)

    if wordmap['style']:
        wordmap['analysis'] += format_tag_tdt(wordmap['style'], format)

    if '+ktnkav' in format and wordmap['pos'] != 'ACRONYM':
        tag = "[KTN=%s]" % (lexc_escape(wordmap['kotus_tn']))
        if tag in OmorFormatter.ktnkav_multichars:
            wordmap['analysis'] += tag
            if wordmap['kotus_av']:
                wordmap['analysis'] += "[KAV=%(kotus_av)s]" % (wordmap)
    elif '+newparas' in format:
        wordmap['analysis'] += "[NEWPARA=%s]" % (wordmap['new_para'])

    # match WORD_ID= with epsilon, then stub and lemma might match
    lex_stub = '0' + wordmap['stub']
    return "%s:%s\t%s\t;" % (wordmap['analysis'], lex_stub,
                             wordmap['new_para'])


def format_multichars_lexc_tdt():
    multichars = ''
    for mcs in tdt_multichars:
        multichars += mcs + "\n"
    return multichars


# self test
if __name__ == '__main__':
    fail = False
    for stuff, tdt in stuff2tdt.items():
        if len(tdt) < 2:
            continue
        elif tdt not in tdt_multichars:
            print("There are conflicting formattings in here!", tdt,
                  "is not a valid defined tdt multichar_symbol!")
            fail = True
    if fail:
        exit(1)
