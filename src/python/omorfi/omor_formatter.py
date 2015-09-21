#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to format omor style analyses from omorfi data."""

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


omor_multichars = {
        '[WORD_ID=',
        '[UPOS=ADJ]',
        '[UPOS=VERB]',
        '[UPOS=NOUN]',
        '[UPOS=PRON]',
        '[UPOS=NUM]',
        '[UPOS=ADV]',
        '[UPOS=ADP]',
        '[UPOS=PROPN]',
        '[UPOS=INTJ]'
        '[SUBCAT=QUALIFIER]',
        '[SUBCAT=INTERJECTION]',
        '[SUBCAT=DEMONSTR]',
        '[SUBCAT=PERSONAL]',
        '[SUBCAT=INTERROG]',
        '[SUBCAT=RELATIVE]',
        '[SUBCAT=QUANTOR]',
        '[SUBCAT=REFLEXIVE]',
        '[SUBCAT=RECIPROC]',
        '[SUBCAT=INDEF]',
        '[SUBCAT=DEMONSTRATIVE]',
        '[SUBCAT=INTERROGATIVE]',
        '[SUBCAT=CARD]',
        '[SUBCAT=ORD]',
        '[SUBCAT=CONJUNCTION]',
        '[CONJ=COORD]',
        '[CONJ=ADVERBIAL]',
        '[CONJ=COMPARATIVE]',
        '[SUBCAT=POSTPOSITION]',
        '[SUBCAT=PREPOSITION]',
        '[SUBCAT=PREFIX]',
        '[SUBCAT=SUFFIX]',
        '[SUBCAT=ABBREVIATION]',
        '[SUBCAT=ACRONYM]',
        '[POS=PUNCTUATION]',
        '[POS=SYMBOL]', 
        '[SUBCAT=SPACE]',
        '[SUBCAT=QUOTATION]',
        '[SUBCAT=BRACKET]',
        '[SUBCAT=DASH]',
        '[SUBCAT=CURRENCY]',
        '[SUBCAT=MATH]',
        '[SUBCAT=OPERATION]',
        '[SUBCAT=RELATION]',
        '[SUBCAT=INITIAL]',
        '[SUBCAT=FINAL]',
        '[SUBCAT=REFLEXIVE]',
        '[SUBCAT=DIGIT]',
        '[SUBCAT=ROMAN]',
        '[SUBCAT=DECIMAL]',
        '[CASE=NOM]',
        '[CASE=PAR]',
        '[CASE=GEN]',
        '[CASE=INE]',
        '[CASE=ELA]',
        '[CASE=ILL]',
        '[CASE=ADE]',
        '[CASE=ABL]',
        '[CASE=ALL]',
        '[CASE=ESS]',
        '[CASE=INS]',
        '[CASE=ABE]',
        '[CASE=TRA]',
        '[CASE=COM]',
        '[CASE=LAT]',
        '[CASE=ACC]',
        '[NUM=SG]',
        '[NUM=PL]',
        '[POSS=SG1]',
        '[POSS=SG2]',
        '[POSS=SG3]',
        '[POSS=PL1]',
        '[POSS=PL2]',
        '[POSS=PL3]',
        '[POSS=3]',
        '[BOUNDARY=COMPOUND]',
        '[COMPOUND_FORM=S]',
        '[COMPOUND_FORM=OMIT]',
        '[TENSE=PRESENT]',
        '[TENSE=PAST]',
        '[MOOD=INDV]',
        '[MOOD=COND]',
        '[MOOD=POTN]',
        '[MOOD=IMPV]',
        '[MOOD=OPT]',
        '[MOOD=EVNV]',
        '[MOOD=INDV][TENSE=PAST]',
        '[PERS=SG1]',
        '[PERS=SG2]',
        '[PERS=SG3]',
        '[PERS=PL1]',
        '[PERS=PL2]',
        '[PERS=PL3]',
        '[PERS=PE4]',
        '[NEG=CON]',
        '[SUBCAT=NEG]',
        '[VOICE=ACT]',
        '[VOICE=PSS]',
        '[INF=A]',
        '[INF=E]',
        '[INF=MA]',
        '[INF=MINEN]',
        '[INF=MAISILLA]',
        '[DRV=MINEN]',
        '[DRV=MAISILLA]',
        '[PCP=NUT]',
        '[PCP=AGENT]',
        '[PCP=VA]',
        '[PCP=NEG]',
        '[DRV=NUT]',
        '[DRV=TU]',
        '[DRV=MA]',
        '[DRV=VA]',
        '[DRV=MATON]',
        '[CMP=POS]',
        '[CMP=CMP]',
        '[CMP=SUP]',
        '[DRV=MPI]',
        '[DRV=IN]',
        '[CLIT=HAN]',
        '[CLIT=KAAN]',
        '[CLIT=KIN]',
        '[CLIT=KO]',
        '[CLIT=PA]',
        '[CLIT=S]',
        '[CLIT=KA]',
        '[DRV=INEN]',
        '[DRV=JA]',
        '[DRV=LAINEN]',
        '[DRV=LLINEN]',
        '[DRV=NUT]',
        '[DRV=OI]',
        '[DRV=S]',
        '[DRV=STI]',
        '[DRV=TAR]',
        '[DRV=TATTAA]',
        '[DRV=TATUTTAA]',
        '[DRV=TAVA]',
        '[DRV=TON]',
        '[DRV=TSE]',
        '[DRV=TTAA]',
        '[DRV=TTAIN]',
        '[DRV=U]',
        '[DRV=UUS]',
        '[DRV=VS]',
        '[STYLE=NONSTANDARD]',
        '[STYLE=RARE]',
        '[STYLE=DIALECTAL]',
        '[STYLE=ARCHAIC]', 
        '[GUESS=COMPOUND]',
        '[GUESS=DERIVE]',
        '[ALLO=A]',
        '[ALLO=TA]',
        '[ALLO=HVN]',
        '[ALLO=IA]',
        '[ALLO=IDEN]',
        '[ALLO=ITA]',
        '[ALLO=ITTEN]',
        '[ALLO=IEN]',
        '[ALLO=IHIN]',
        '[ALLO=IIN]',
        '[ALLO=IN]',
        '[ALLO=ISIIN]',
        '[ALLO=IDEN]',
        '[ALLO=JA]',
        '[ALLO=JEN]',
        '[ALLO=SEEN]',
        '[ALLO=TEN]',
        '[ALLO=VN]',
        '[FILTER=NO_PROC]',
        '[PROPER=FIRST]',
        '[PROPER=GEO]',
        '[PROPER=LAST]',
        '[PROPER=MISC]',
        '[PROPER=ORG]',
        '[PROPER=PRODUCT]',
        '[PROPER=EVENT]',
        '[PROPER=MEDIA]',
        '[PROPER=CULTGRP]',
        '[PROPER=ARTWORK]',
        '[SEM=TITLE]',
        '[SEM=ORG]',
        '[SEM=EVENT]',
        '[SEM=POLIT]',
        '[SEM=MEDIA]',
        '[SEM=GEO]',
        '[SEM=COUNTRY]',
        '[SEM=INHABITANT]',
        '[SEM=LANGUAGE]',
        '[SEM=MEASURE]',
        '[SEM=CURRENCY]',
        '[SEM=TIME]',
        '[SEM=MALE]',
        '[SEM=FEMALE]',
        '[POSITION=PREFIX]',
        '[POSITION=SUFFIX]',
        '[POS=NOUN][SUBCAT=ABBREVIATION]', 
        '[MOOD=INDV][TENSE=PRESENT]',
        '[MOOD=INDV][TENSE=PAST]'
        "[SUBCAT=DASH]",
        "[SUBCAT=SPACE]",
        "[BOUNDARY=CLAUSE]",
        "[BOUNDARY=SENTENCE]",
        "[SUBCAT=QUOTATION][POSITION=INITIAL]",
        "[SUBCAT=QUOTATION][POSITION=FINAL]",
        "[SUBCAT=BRACKET][POSITION=INITIAL]",
        "[SUBCAT=BRACKET][POSITION=FINAL]",
        "[POS=VERB][SUBCAT=NEG]",
        "[LEX=STI]",
        "[LEX=INE]",
        "[LEX=ELA]",
        "[LEX=ILL]",
        "[LEX=ADE]",
        "[LEX=ABL]",
        "[LEX=ALL]",
        "[LEX=TTAIN]"
        }

ktnkav_multichars = {
        '[KTN=1]', '[KTN=2]', '[KTN=3]', '[KTN=4]', '[KTN=5]',
        '[KTN=6]', '[KTN=7]', '[KTN=8]', '[KTN=9]', '[KTN=10]',
        '[KTN=11]', '[KTN=12]', '[KTN=13]', '[KTN=14]', '[KTN=15]',
        '[KTN=16]', '[KTN=17]', '[KTN=18]', '[KTN=19]', '[KTN=20]',
        '[KTN=21]', '[KTN=22]', '[KTN=23]', '[KTN=24]', '[KTN=25]',
        '[KTN=26]', '[KTN=27]', '[KTN=28]', '[KTN=29]', '[KTN=30]',
        '[KTN=31]', '[KTN=32]', '[KTN=33]', '[KTN=34]', '[KTN=35]',
        '[KTN=36]', '[KTN=37]', '[KTN=38]', '[KTN=39]', '[KTN=40]',
        '[KTN=41]', '[KTN=42]', '[KTN=43]', '[KTN=44]', '[KTN=45]',
        '[KTN=46]', '[KTN=47]', '[KTN=48]', '[KTN=49]', '[KTN=50]',
        '[KTN=51]', '[KTN=52]', '[KTN=53]', '[KTN=54]', '[KTN=55]',
        '[KTN=56]', '[KTN=57]', '[KTN=58]', '[KTN=59]', '[KTN=60]',
        '[KTN=61]', '[KTN=62]', '[KTN=63]', '[KTN=64]', '[KTN=65]',
        '[KTN=66]', '[KTN=67]', '[KTN=68]', '[KTN=69]', '[KTN=70]',
        '[KTN=71]', '[KTN=72]', '[KTN=73]', '[KTN=74]', '[KTN=75]',
        '[KTN=76]', '[KTN=77]', '[KTN=78]',
        '[KTN=1007]', '[KTN=1009]', '[KTN=1010]', '[KTN=1024]', '[KTN=1026]',
        '[KAV=A]', '[KAV=B]', '[KAV=C]', '[KAV=D]', '[KAV=E]',
        '[KAV=F]', '[KAV=G]', '[KAV=H]', '[KAV=I]', '[KAV=J]',
        '[KAV=K]', '[KAV=L]', '[KAV=M]',
        '[KAV=N]', '[KAV=O]', '[KAV=P]', '[KAV=T]'}

stuff2omor = {
        ".sent": "[BOUNDARY=SENTENCE]",
        "Aa": "[ALLO=A]",
        "Aja": "[ALLO=JA]",
        "Ana": "[ALLO=NA]",
        "Asa": "[ALLO=SA]",
        "Aia": "[ALLO=IA]",
        "Ata": "[ALLO=TA]",
        "Aita": "[ALLO=ITA]",
        "Atä": "[ALLO=TÄ]",
        "Aiä": "[ALLO=IÄ]",
        "Aita": "[ALLO=ITA]",
        "Aitä": "[ALLO=ITÄ]",
        "Aitten": "[ALLO=ITTEN]",
        "Aiden": "[ALLO=IDEN]",
        "Aiin": "[ALLO=IIN]",
        "Aihin": "[ALLO=IHIN]",
        "Aseen": "[ALLO=SEEN]",
        "Aisiin": "[ALLO=ISIIN]",
        "Aien": "[ALLO=IEN]",
        "Ajen": "[ALLO=JEN]",
        "Aten": "[ALLO=TEN]",
        "Aan": "[ALLO=AN]",
        "Aen": "[ALLO=EN]",
        "Ain": "[ALLO=IN]",
        "Aon": "[ALLO=ON]",
        "Aun": "[ALLO=UN]",
        "Ayn": "[ALLO=YN]",
        "Aän": "[ALLO=ÄN]",
        "Aön": "[ALLO=ÖN]",
        "Ahan": "[ALLO=HAN]",
        "Ahen": "[ALLO=HEN]",
        "Ahin": "[ALLO=HIN]",
        "Ahon": "[ALLO=HON]",
        "Ahun": "[ALLO=HUN]",
        "Ahyn": "[ALLO=HYN]",
        "Ahän": "[ALLO=HÄN]",
        "Ahön": "[ALLO=HÖN]",
        "Aten": "[ALLO=TEN]",
        "Ajä": "[ALLO=JÄ]",
        "Aä": "[ALLO=Ä]",
        "Bc": "[BOUNDARY=COMPOUND]", 
        "B-": "[COMPOUND_FORM=OMIT]",
        "B→": "[POSITION=SUFFIX]",
        "B←": "[POSITION=PREFIX]",
        "Cma": "[PCP=AGENT]",
        "Cmaton": "[PCP=NEG]", 
        "Cva": "[PCP=VA]",
        "Cnut": "[PCP=NUT]",
        "Cpos": "",
        #"Cpos": "[CMP=POS]", 
        "Ccmp": "[CMP=CMP]", 
        "Csup": "[CMP=SUP]", 
        "Dinen": "[DRV=INEN]", 
        "Dja": "[DRV=JA]",
        "Dmaisilla": "[INF=MAISILLA]", 
        #"Dmaisilla": "[DRV=MAISILLA]", 
        "Dminen": "[DRV=MINEN]",
        "Dtu": "[DRV=TU]", 
        "Dnut": "[DRV=NUT]",
        "Dva": "[DRV=VA]",
        "Dtava": "[DRV=TAVA]",
        "Dma": "[DRV=MA]", 
        "Dmaton": "[DRV=MATON]",
        "Ds": "[DRV=S]", 
        "Dsti": "[DRV=STI]",
        "Dttaa": "[DRV=TTAA]", 
        "Dtattaa": "[DRV=TATTAA]",
        "Dtatuttaa": "[DRV=TATUTTAA]", 
        "Dttain": "[DRV=TTAIN]", 
        "Du": "[DRV=U]",
        "Duus": "[DRV=UUS]",
        "Dmpi": "", 
        #"Dmpi": "[DRV=MPI]", 
        "Din": "",
        #"Din": "[DRV=IN]",
        "Ia": "[INF=A]", 
        "Ie": "[INF=E]", 
        "Ima": "[INF=MA]",
        "Iminen": "[INF=MINEN]",
        "Ncon": "[NEG=CON]",
        "Nneg": "[SUBCAT=NEG]", 
        "Npl": "[NUM=PL]",
        "Nsg": "[NUM=SG]",
        "N??": "",
        "Osg1": "[POSS=SG1]",
        "Osg2": "[POSS=SG2]",
        "O3": "[POSS=3]",
        "Opl1": "[POSS=PL1]",
        "Opl2": "[POSS=PL2]",
        "Ppl1": "[PERS=PL1]",
        "Ppl2": "[PERS=PL2]",
        "Ppl3": "[PERS=PL3]",
        "Psg1": "[PERS=SG1]",
        "Psg2": "[PERS=SG2]",
        "Psg3": "[PERS=SG3]",
        "Ppe4": "[PERS=PE4]",
        "Qka": "[CLIT=KA]",
        "Qs": "[CLIT=S]",
        "Qpa": "[CLIT=PA]",
        "Qko": "[CLIT=KO]",
        "Qkin": "[CLIT=KIN]",
        "Qkaan": "[CLIT=KAAN]", 
        "Qhan": "[CLIT=HAN]",
        "Tcond": "[MOOD=COND]", 
        "Timp": "[MOOD=IMPV]",
        "Tpast": "[MOOD=INDV][TENSE=PAST]", 
        "Tpot": "[MOOD=POTN]", 
        "Topt": "[MOOD=OPT]",
        "Tpres": "[MOOD=INDV][TENSE=PRESENT]", 
        "Uarch": "[STYLE=ARCHAIC]",
        "Udial": "[STYLE=DIALECTAL]", 
        "Unonstd": "[STYLE=NONSTANDARD]",
        "Urare": "[STYLE=RARE]",
        "Vact": "[VOICE=ACT]",
        "Vpss": "[VOICE=PSS]",
        "Xabe": "[CASE=ABE]",
        "Xabl": "[CASE=ABL]",
        "Xade": "[CASE=ADE]",
        "Xall": "[CASE=ALL]",
        "Xcom": "[CASE=COM]",
        "Xela": "[CASE=ELA]",
        "Xess": "[CASE=ESS]",
        "Xgen": "[CASE=GEN]",
        "Xill": "[CASE=ILL]",
        "Xine": "[CASE=INE]",
        "Xins": "[CASE=INS]",
        "Xnom": "[CASE=NOM]",
        "Xpar": "[CASE=PAR]",
        "Xtra": "[CASE=TRA]", 
        "Xlat": "[CASE=LAT]",
        "Xacc": "[CASE=ACC]",
        "X???": "",
        "NOUN": "[UPOS=NOUN]", 
        "VERB": "[UPOS=VERB]",
        "ADV": "[UPOS=ADV]",
        "ADP": "[UPOS=ADV]",
        "ADJ": "[UPOS=ADJ]",
        "INTJ": "[UPOS=INTJ]",
        "CONJ": "[UPOS=CONJ]",
        "PRON": "[UPOS=PRON]",
        "SYM": "[UPOS=SYM]",
        "NUM": "[UPOS=NUM]",
        "X": "[UPOS=X]",
        "PUNCT": "[UPOS=PUNCT]",
        "ABESSIVE": "[LEX=ABE]",
        "ABLATIVE": "[LEX=ABL]",
        "ADESSIVE": "[LEX=ADE]",
        "ALLATIVE": "[LEX=ALL]",
        "ELATIVE": "[LEX=ELA]",
        "LOCATIVE": "[LEX=LOC]", 
        "GENITIVE": "[LEX=GEN]",
        "ILLATIVE": "[LEX=ILL]", 
        "INESSIVE": "[LEX=INE]",
        "INSTRUCTIVE": "[LEX=INS]",
        "PARTITIVE": "[LEX=PAR]", 
        "SEPARATIVE": "[LEX=SEP]", 
        "LATIVE": "[LEX=LAT]",
        "DERSTI": "[LEX=STI]",
        "DERTTAIN": "[LEX=TTAIN]",
        "CONJUNCTION": "[UPOS=CONJ]",
        "COORDINATING": "[CONJ=COORD]",
        "COMPARATIVE": "[CONJ=COMPARATIVE]",
        "PRONOUN": "[POS=PRONOUN]",
        "ADVERBIAL": "[CONJ=ADVERBIAL]",
        "NUMERAL": "[POS=NUMERAL]",
        "CARDINAL": "[SUBCAT=CARD]", 
        "ORDINAL": "[SUBCAT=ORD]",
        # No [SUBCAT=DIGIT]: avoid multiple SUBCATs in one tagstring & comply with FTB1
        "DIGIT": "",
        "DECIMAL": "[SUBCAT=DECIMAL]",
        "ROMAN": "[SUBCAT=ROMAN]",
        "QUALIFIER": "[SUBCAT=QUALIFIER]",
        "ACRONYM": "[POS=NOUN][SUBCAT=ABBREVIATION]", 
        "ABBREVIATION": "[SUBCAT=ABBREVIATION]",
        "SUFFIX": "", 
        #"SUFFIX": "[SUBCAT=SUFFIX]", 
        "PREFIX": "",
        #"PREFIX": "[SUBCAT=PREFIX]",
        "INTERJECTION": "[SUBCAT=INTERJECTION]",
        "ADPOSITION": "[POS=ADPOSITION]",
        "DEMONSTRATIVE": "[SUBCAT=DEMONSTRATIVE]", 
        "QUANTOR": "[SUBCAT=QUANTOR]", 
        "PERSONAL": "[SUBCAT=PERSONAL]",
        "INDEFINITE": "", 
        #"INDEFINITE": "[SUBCAT=INDEF]", 
        "INTERROGATIVE": "[SUBCAT=INTERROGATIVE]",
        "REFLEXIVE": "[SUBCAT=REFLEXIVE]", 
        "RELATIVE": "[SUBCAT=RELATIVE]",
        "RECIPROCAL": "[SUBCAT=RECIPROC]",
        "PL1": "[PERS=PL1]",
        "PL2": "[PERS=PL2]",
        "PL3": "[PERS=PL3]",
        "SG1": "[PERS=SG1]",
        "SG2": "[PERS=SG2]",
        "SG3": "[PERS=SG3]",
        "PE4": "[PERS=PE4]",
        "COMP": "[CMP=CMP]",
        "SUPERL": "[CMP=SUP]",
        "ARCHAIC": "[STYLE=ARCHAIC]",
        "DIALECTAL": "[STYLE=DIALECTAL]",
        "NONSTANDARD": "[STYLE=NONSTANDARD]",
        "RARE": "[STYLE=RARE]",
        "TITLE": "[SEM=TITLE]",
        "TIME": "[SEM=TIME]", 
        "CURRENCY": "[SEM=CURRENCY]",
        "MEDIA": "[SEM=MEDIA]", 
        "POLIT": "[SEM=POLIT]",
        "MEASURE": "[SEM=MEASURE]", 
        "MALE": "[SEM=MALE]",
        "FEMALE": "[SEM=FEMALE]", 
        "PROPER": "[PROPER=PROPER]", 
        "CULTGRP": "[PROPER=CULTGRP]",
        "PRODUCT": "[PROPER=PRODUCT]",
        "ARTWORK": "[PROPER=ARTWORK]",
        "EVENT": "[PROPER=EVENT]", 
        "FIRST": "[PROPER=FIRST]",
        "LAST": "[PROPER=LAST]", 
        "GEO": "[PROPER=GEO]",
        "ORG": "[PROPER=ORG]", 
        "MISC": "[PROPER=MISC]",
        "COUNTRY": "[SEM=COUNTRY]",
        "INHABITANT": "[SEM=INHABITANT]",
        "LANGUAGE": "[SEM=LANGUAGE]",
        "PUNCTUATION": "[POS=PUNCTUATION]",
        "DASH": "[SUBCAT=DASH]",
        "SPACE": "[SUBCAT=SPACE]",
        "COMMA": "",
        "ARROW": "",
        "CLAUSE-BOUNDARY": "[BOUNDARY=CLAUSE]",
        "SENTENCE-BOUNDARY": "[BOUNDARY=SENTENCE]",
        "INITIAL-QUOTE": "[SUBCAT=QUOTATION][POSITION=INITIAL]",
        "FINAL-QUOTE": "[SUBCAT=QUOTATION][POSITION=FINAL]",
        "INITIAL-BRACKET": "[SUBCAT=BRACKET][POSITION=INITIAL]",
        "FINAL-BRACKET": "[SUBCAT=BRACKET][POSITION=FINAL]",
        "UNSPECIFIED": "",
        "FTB3man": "",
        "LEMMA-START": "[WORD_ID=",
        "CONJ|VERB": "[UPOS=VERB][SUBCAT=NEG]",
        "FTB3MAN": "",
        ".": "",
        "": ""}

def format_stuff_omor(stuff, format):
    if stuff == '0':
        return "0"
    if stuff in stuff2omor:
        return stuff2omor[stuff]
    else:
        fail_formatting_missing_for(stuff, format)
        return ""


def format_analysis_lexc_omor(anals, format):
    omorstring = ''
    for tag in anals.split('|'):
        omorstring += format_stuff_omor(tag, format)
    return omortstring

def format_continuation_lexc_omor(anals, surf, cont, format):
    omorstring = ''
    if 'DIGITS_' in cont and not ('BACK' in cont or 'FRONT' in cont):
        omorstring = lexc_escape(surf)
        if anals and anals != 'LEMMA-START':
            omorstring += ']'
    
    # Collapse DRV=NUT/TU and PCP=NUT to PCP=NUT with full inflection
    if anals == 'Dnut':
        anals = 'Vact|Cnut'
    elif anals == 'Dtu':
        anals = 'Vpss|Cnut'
    # Collapse DRV=VA/TAVA and PCP=VA to PCP=VA with full inflection
    elif anals == 'Dva':
        anals = 'Vact|Cva'
    elif anals == 'Dtava':
        anals = 'Vpss|Cva'
    # Collapse DRV=MA and PCP=AGENT to PCP=AGENT with full inflection
    elif anals == 'Dma':
        anals = 'Cma'
    # Collapse DRV=MATON and PCP=NEG to PCP=NEG with full inflection
    elif anals == 'Dmaton':
        anals = 'Cmaton'
    elif ('Cnut' in anals or 'Cva' in anals or 'Cma' in anals or 'Cmaton' in anals) and \
         (anals.endswith('Npl') or anals.endswith('Nsg')):
        anals = anals + '|Xnom'
    
    tags = anals.split('|')
    for tag in tags:
        omorstring += format_stuff_omor(tag, format)
    surf = lexc_escape(surf)
    return "%s:%s\t%s ;\n" %(omorstring, surf, cont)

def format_wordmap_lexc_omor(wordmap, format):
    '''
    format string for canonical omor format for morphological analysis
    '''
    if wordmap['stub'] == ' ':
        # do not include normal white space for now
        return ""
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    wordmap['analysis'] = "[WORD_ID=%s]" %(lexc_escape(wordmap['lemma']))
    wordmap['particle'] = wordmap['particle'].replace('QUALIFIER', 'ADJ')
    wordmap['analysis'] += format_stuff_omor(wordmap['upos'], format)
    if wordmap['is_suffix']:
        wordmap['analysis'] += format_stuff_omor('SUFFIX', format)
    if wordmap['is_prefix']:
        wordmap['analysis'] += format_stuff_omor('PREFIX', format)
        if wordmap['pos'] == 'ADJECTIVE':
            wordmap['analysis'] += format_stuff_omor('Cpos', format)

    if wordmap['particle']:
        for pclass in wordmap['particle'].split('|'):
            wordmap['analysis'] += format_stuff_omor(pclass, format)

    if wordmap['symbol']:
        for subcat in wordmap['symbol'].split('|'):
            wordmap['analysis'] += format_stuff_omor(subcat, format)
    
    if wordmap['pronoun']:
        for stuff in wordmap['pronoun'].split("|"):
            wordmap['analysis'] += format_stuff_omor(stuff, format)
    if wordmap['adjective_class']:
        for stuff in wordmap['adjective_class'].split("|"):
            wordmap['analysis'] += format_stuff_omor(stuff, format)
    if wordmap['noun_class']:
        for stuff in wordmap['noun_class'].split("|"):
            wordmap['analysis'] += format_stuff_omor(stuff, format)
    if wordmap['numeral_class']:
        for stuff in wordmap['numeral_class'].split("|"):
            wordmap['analysis'] += format_stuff_omor(stuff, format)
    
    if wordmap['is_proper']:
        if '+propers' in format and wordmap['proper_noun_class']:
            for prop in wordmap['proper_noun_class'].split(','):
                wordmap['analysis'] += format_stuff_omor(prop, format)
        else:
            wordmap['analysis'] += format_stuff_omor('PROPER', format)

    if '+semantics' in format and wordmap['sem']:
        for sem in wordmap['sem'].split(','):
            wordmap['analysis'] += format_stuff_omor(sem, format)

    if wordmap['style']:
        wordmap['analysis'] += format_stuff_omor(wordmap['style'], format)
    
    if '+ktnkav' in format and wordmap['pos'] != 'ACRONYM':
        tag = "[KTN=%s]" %(lexc_escape(wordmap['kotus_tn']))
        if tag in ktnkav_multichars:
            wordmap['analysis'] += tag
            if wordmap['kotus_av']:
                wordmap['analysis'] += "[KAV=%(kotus_av)s]" %(wordmap)
    elif '+newparas' in format:
        for new_para in wordmap['new_paras']:
            wordmap['analysis'] += "[NEWPARA=%s]" %(new_para)

    # match WORD_ID= with epsilon, then stub and lemma might match
    lex_stub = '0' + wordmap['stub']
    retvals = []
    retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, 
        wordmap['new_para'])]
    return "\n".join(retvals)

def format_multichars_lexc_omor():
    multichars = ''
    for mcs in omor_multichars:
        multichars += mcs + "\n"
    return multichars


# self test
if __name__ == '__main__':
    from sys import exit
    fail = False
    for stuff, omor in stuff2omor.items():
        if len(omor) < 2:
            continue
        elif not omor in omor_multichars:
            print("There are conflicting formattings in here!", omor, 
                    "is not a valid defined omor multichar_symbol!")
            fail = True
    if fail:
        exit(1)

