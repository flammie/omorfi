#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formatter to de/format omor style analyses for omrfi."""

# (c) Omorfi contributors <omorfi-devel@groups.google.com> 2015
# see AUTHORS file in top-level dir of this project, or
# <https://github.com/flammie/omorfi/wiki/AUTHORS>

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

from .error_logging import fail_formatting_missing_for, just_fail
from .formatter import Formatter
from .string_manglers import regex_delete_surface, egrep2xerox, lexc_escape


class OmorFormatter(Formatter):
    common_multichars = {
        '[ABBR=ABBREVIATION]',
        '[ABBR=ACRONYM]',
        "[BOUNDARY=CLAUSE]",
        '[BOUNDARY=COMPOUND]',
        "[BOUNDARY=SENTENCE]",
        '[CASE=ABE]',
        '[CASE=ABL]',
        '[CASE=ACC]',
        '[CASE=ADE]',
        '[CASE=ALL]',
        '[CASE=COM]',
        '[CASE=ELA]',
        '[CASE=ESS]',
        '[CASE=GEN]',
        '[CASE=ILL]',
        '[CASE=INE]',
        '[CASE=INS]',
        '[CASE=LAT]',
        '[CASE=NOM]',
        '[CASE=PAR]',
        '[CASE=TRA]',
        '[CLIT=HAN]',
        '[CLIT=KA]',
        '[CLIT=KAAN]',
        '[CLIT=KIN]',
        '[CLIT=KO]',
        '[CLIT=PA]',
        '[CLIT=S]',
        '[CMP=CMP]',
        '[CMP=POS]',
        '[CMP=SUP]',
        '[COMPOUND_FORM=OMIT]',
        '[COMPOUND_FORM=S]',
        '[CONJ=ADVERBIAL]',
        '[CONJ=COMPARATIVE]',
        '[CONJ=COORD]',
        '[DRV=IN]',
        '[DRV=ISA]',
        '[DRV=INEN]',
        '[DRV=NEN]',
        '[DRV=JA]',
        '[DRV=LAINEN]',
        '[DRV=LA]',
        '[DRV=LLINEN]',
        '[DRV=MA]',
        '[DRV=MAISILLA]',
        '[DRV=MATON]',
        '[DRV=MINEN]',
        '[DRV=MAINEN]',
        '[DRV=LAINEN]',
        '[DRV=MPI]',
        '[DRV=NUT]',
        '[DRV=NUT]',
        '[DRV=OI]',
        '[DRV=HKO]',
        '[DRV=S]',
        '[DRV=STI]',
        '[DRV=TAR]',
        '[DRV=TATTAA]',
        '[DRV=TATUTTAA]',
        '[DRV=TUTTAA]',
        '[DRV=TAVA]',
        '[DRV=TON]',
        '[DRV=TSE]',
        '[DRV=TTAA]',
        '[DRV=TTAIN]',
        '[DRV=TU]',
        '[DRV=U]',
        '[DRV=UUS]',
        '[DRV=VA]',
        '[DRV=VS]',
        '[FILTER=NO_PROC]',
        '[GUESS=COMPOUND]',
        '[GUESS=DERIVE]',
        '[INF=A]',
        '[INF=E]',
        '[INF=MA]',
        '[INF=MAISILLA]',
        '[INF=MINEN]',
        "[LEX=ABE]",
        "[LEX=ABL]",
        "[LEX=ADE]",
        "[LEX=ALL]",
        "[LEX=ELA]",
        "[LEX=ILL]",
        "[LEX=INE]",
        "[LEX=INS]",
        "[LEX=PAR]",
        "[LEX=STI]",
        "[LEX=GEN]",
        "[LEX=LAT]",
        "[LEX=LOC]",
        "[LEX=SEP]",
        "[LEX=TTAIN]",
        '[MOOD=COND]',
        '[MOOD=EVNV]',
        '[MOOD=IMPV]',
        '[MOOD=INDV]',
        '[MOOD=INDV][TENSE=PAST]',
        '[MOOD=INDV][TENSE=PRESENT]',
        '[MOOD=OPT]',
        '[MOOD=POTN]',
        '[NEG=CON]',
        '[NUM=PL]',
        '[NUM=SG]',
        '[NUMTYPE=CARD]',
        '[NUMTYPE=ORD]',
        '[NUMTYPE=FRAC]',
        '[NUMTYPE=MULT]',
        '[PCP=AGENT]',
        '[PCP=NEG]',
        '[PCP=NUT]',
        '[PCP=VA]',
        '[PERS=PE4]',
        '[PERS=PL1]',
        '[PERS=PL2]',
        '[PERS=PL3]',
        '[PERS=SG1]',
        '[PERS=SG2]',
        '[PERS=SG3]',
        '[POSITION=PREFIX]',
        '[POSITION=SUFFIX]',
        '[POSS=3]',
        '[POSS=PL1]',
        '[POSS=PL2]',
        '[POSS=PL3]',
        '[POSS=SG1]',
        '[POSS=SG2]',
        '[POSS=SG3]',
        '[PRONTYPE=DEM]',
        '[PRONTYPE=IND]',
        '[PRONTYPE=INT]',
        '[PRONTYPE=PRS]',
        '[PRONTYPE=RCP]',
        '[PRONTYPE=REL]',
        '[PRONTYPE=REC]',
        '[PROPER=ARTWORK]',
        '[PROPER=CULTGRP]',
        '[PROPER=EVENT]',
        '[PROPER=FIRST]',
        '[PROPER=GEO]',
        '[PROPER=LAST]',
        '[PROPER=MEDIA]',
        '[PROPER=MISC]',
        '[PROPER=ORG]',
        '[PROPER=PRODUCT]',
        '[SEM=COUNTRY]',
        '[SEM=CURRENCY]',
        '[SEM=EVENT]',
        '[SEM=FEMALE]',
        '[SEM=GEO]',
        '[SEM=INHABITANT]',
        '[SEM=LANGUAGE]',
        '[SEM=MALE]',
        '[SEM=MEASURE]',
        '[SEM=MEDIA]',
        '[SEM=ORG]',
        '[SEM=POLIT]',
        '[SEM=TIME]',
        '[SEM=TITLE]',
        '[STYLE=ARCHAIC]',
        '[STYLE=DIALECTAL]',
        '[STYLE=NONSTANDARD]',
        '[STYLE=RARE]',
        '[SUBCAT=ARROW]',
        '[SUBCAT=BRACKET]',
        "[SUBCAT=BRACKET][POSITION=FINAL]",
        "[SUBCAT=BRACKET][POSITION=INITIAL]",
        '[SUBCAT=COMMA]',
        '[SUBCAT=CONJUNCTION]',
        '[SUBCAT=CURRENCY]',
        '[SUBCAT=DASH]',
        "[SUBCAT=DASH]",
        '[SUBCAT=DECIMAL]',
        '[SUBCAT=DEMONSTRATIVE]',
        '[SUBCAT=DIGIT]',
        '[SUBCAT=FINAL]',
        '[SUBCAT=INITIAL]',
        '[SUBCAT=INTERJECTION]',
        '[SUBCAT=INTERROGATIVE]',
        '[SUBCAT=MATH]',
        '[SUBCAT=NEG]',
        "[SUBCAT=NEG]",
        '[SUBCAT=OPERATION]',
        '[ADPTYPE=POST]',
        '[SUBCAT=PREFIX]',
        '[ADPTYPE=PREP]',
        '[SUBCAT=QUALIFIER]',
        '[SUBCAT=QUANTIFIER]',
        '[SUBCAT=QUOTATION]',
        "[SUBCAT=QUOTATION][POSITION=FINAL]",
        "[SUBCAT=QUOTATION][POSITION=INITIAL]",
        '[SUBCAT=REFLEXIVE]',
        '[SUBCAT=RELATION]',
        '[SUBCAT=ROMAN]',
        '[SUBCAT=SPACE]',
        '[SUBCAT=SUFFIX]',
        '[TENSE=PAST]',
        '[TENSE=PRESENT]',
        '[UPOS=ADJ]',
        '[UPOS=ADP]',
        '[UPOS=ADV]',
        '[UPOS=AUX]',
        '[UPOS=DET]',
        '[UPOS=INTJ]',
        '[UPOS=CCONJ]',
        '[UPOS=SCONJ]',
        '[UPOS=SCONJ][CONJ=COMPARATIVE]',
        '[UPOS=SCONJ][CONJ=ADVERBIAL]',
        '[UPOS=NOUN]',
        '[UPOS=NUM]',
        '[UPOS=PRON]',
        '[UPOS=PROPN]',
        '[UPOS=PUNCT]',
        '[UPOS=SYM]',
        '[UPOS=VERB]',
        '[UPOS=VERB][SUBCAT=NEG]',
        '[UPOS=X]',
        '[VOICE=ACT]',
        '[VOICE=PSS]',
        '[WORD_ID=',
        '[NEWPARA=',
        '[BLACKLIST=',
        "[FOREIGN=FOREIGN]"
    }

    old_poses = {
        '[POS=ADPOSITION]',
        '[POS=PUNCTUATION]',
        '[POS=PRONOUN]',
        '[POS=NUMERAL]',
        '[POS=SYMBOL]'
    }

    allo_multichars = {
        '[ALLO=A]',
        '[ALLO=AN]',
        '[ALLO=EN]',
        '[ALLO=HAN]',
        '[ALLO=HEN]',
        '[ALLO=HIN]',
        '[ALLO=HON]',
        '[ALLO=HUN]',
        '[ALLO=HVN]',
        '[ALLO=HYN]',
        '[ALLO=HÄN]',
        '[ALLO=HÖN]',
        '[ALLO=IA]',
        '[ALLO=IDEN]',
        '[ALLO=IDEN]',
        '[ALLO=IEN]',
        '[ALLO=IHIN]',
        '[ALLO=IIN]',
        '[ALLO=IN]',
        '[ALLO=ISIIN]',
        '[ALLO=ITA]',
        '[ALLO=ITTEN]',
        '[ALLO=ITÄ]',
        '[ALLO=IÄ]',
        '[ALLO=JA]',
        '[ALLO=JÄ]',
        '[ALLO=JEN]',
        '[ALLO=NA]',
        '[ALLO=ON]',
        '[ALLO=SA]',
        '[ALLO=SEEN]',
        '[ALLO=TA]',
        '[ALLO=TEN]',
        '[ALLO=TÄ]',
        '[ALLO=UN]',
        '[ALLO=VN]',
        '[ALLO=YN]',
        '[ALLO=Ä]',
        '[ALLO=ÄN]',
        '[ALLO=ÖN]'
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
        "Cpos": "[CMP=POS]",
        "Ccmp": "[CMP=CMP]",
        "Csup": "[CMP=SUP]",
        "Dhko": "[DRV=HKO]",
        "Dinen": "[DRV=NEN]",
        "Dnen": "[DRV=INEN]",
        "Dla": "[DRV=LA]",
        "Dlainen": "[DRV=LAINEN]",
        "Dllinen": "[DRV=LLINEN]",
        "Disa": "[DRV=ISA]",
        "Dja": "[DRV=JA]",
        "Dmaisilla": "[DRV=MAISILLA]",
        "Dminen": "[DRV=MINEN]",
        "Dmainen": "[DRV=MAINEN]",
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
        "Dtuttaa": "[DRV=TUTTAA]",
        "Dttain": "[DRV=TTAIN]",
        "Du": "[DRV=U]",
        "Duus": "[DRV=UUS]",
        "Dmpi": "[DRV=MPI]",
        "Dtar": "[DRV=TAR]",
        "Dton": "[DRV=TON]",
        "Din": "[DRV=IN]",
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
        "AUX": "[UPOS=AUX]",
        "DET": "[UPOS=DET]",
        "NOUN": "[UPOS=NOUN]",
        "VERB": "[UPOS=VERB]",
        "ADV": "[UPOS=ADV]",
        "ADP": "[UPOS=ADP]",
        "ADJ": "[UPOS=ADJ]",
        "INTJ": "[UPOS=INTJ]",
        "CCONJ": "[UPOS=CCONJ]",
        "SCONJ": "[UPOS=SCONJ]",
        "PRON": "[UPOS=PRON]",
        "SYM": "[UPOS=SYM]",
        "NUM": "[UPOS=NUM]",
        "PROPN": "[UPOS=PROPN]",
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
        "CONJUNCTION": "",
        "COORDINATING": "[UPOS=CCONJ]",
        "COMPARATIVE": "[UPOS=SCONJ][CONJ=COMPARATIVE]",
        "PRONOUN": "[POS=PRONOUN]",
        "ADVERBIAL": "[UPOS=SCONJ][CONJ=ADVERBIAL]",
        "NUMERAL": "[POS=NUMERAL]",
        "CARDINAL": "[NUMTYPE=CARD]",
        "ORDINAL": "[NUMTYPE=ORD]",
        # No [SUBCAT=DIGIT]: avoid multiple SUBCATs in one tagstring & comply
        # with FTB1
        "DIGIT": "",
        "DECIMAL": "[SUBCAT=DECIMAL]",
        "ROMAN": "[SUBCAT=ROMAN]",
        "QUALIFIER": "[SUBCAT=QUALIFIER]",
        "ACRONYM": "[ABBR=ACRONYM]",
        "ABBREVIATION": "[ABBR=ABBREVIATION]",
        "SUFFIX": "",
        # "SUFFIX": "[SUBCAT=SUFFIX]",
        "PREFIX": "",
        # "PREFIX": "[SUBCAT=PREFIX]",
        "INTERJECTION": "[SUBCAT=INTERJECTION]",
        "ADPOSITION": "[POS=ADPOSITION]",
        "DEMONSTRATIVE": "[PRONTYPE=DEM]",
        "QUANTOR": "[SUBCAT=QUANTIFIER]",
        "QUANTIFIER": "[SUBCAT=QUANTIFIER]",
        "PERSONAL": "[PRONTYPE=PRS]",
        "INDEFINITE": "[PRONTYPE=IND]",
        # "INDEFINITE": "[SUBCAT=INDEF]",
        "INTERROGATIVE": "[PRONTYPE=INT]",
        "REFLEXIVE": "[SUBCAT=REFLEXIVE]",
        "RELATIVE": "[PRONTYPE=REL]",
        "RECIPROCAL": "[PRONTYPE=REC]",
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
        "COMMA": "[SUBCAT=COMMA]",
        "ARROW": "[SUBCAT=ARROW]",
        "PREPOSITION": "[ADPTYPE=PREP]",
        "POSTPOSITION": "[ADPTYPE=POST]",
        "MULTIPLICATIVE": "[NUMTYPE=MULT]",
        "FRACTION": "[NUMTYPE=FRAC]",
        "CLAUSE-BOUNDARY": "[BOUNDARY=CLAUSE]",
        "SENTENCE-BOUNDARY": "[BOUNDARY=SENTENCE]",
        "INITIAL-QUOTE": "[SUBCAT=QUOTATION][POSITION=INITIAL]",
        "FINAL-QUOTE": "[SUBCAT=QUOTATION][POSITION=FINAL]",
        "INITIAL-BRACKET": "[SUBCAT=BRACKET][POSITION=INITIAL]",
        "FINAL-BRACKET": "[SUBCAT=BRACKET][POSITION=FINAL]",
        "UNSPECIFIED": "",
        "FTB3man": "",
        "LEMMA-START": "[WORD_ID=",
        "LEMMA-END": "]",
        "CCONJ|VERB": "[UPOS=VERB][SUBCAT=NEG]",
        "FTB3MAN": "",
        "XForeign": "[FOREIGN=FOREIGN]",
        "": ""}

    def __init__(self, verbose=False, **kwargs):
        for stuff, omor in self.stuff2omor.items():
            if len(omor) < 2:
                continue
            elif omor not in self.common_multichars | self.old_poses | \
                    self.allo_multichars:
                just_fail(
                    "There are conflicting formattings in here!\n" +
                    omor + " corresponding " + stuff +
                    " is not a valid defined omor multichar_symbol!")
        self.verbose = verbose
        self.semantics = True
        if 'sem' not in kwargs or not kwargs['sem']:
            for k, v in self.stuff2omor.items():
                if "SEM=" in v:
                    self.stuff2omor[k] = ""
            self.semantics = False
        self.allo = True
        if 'allo' not in kwargs or not kwargs['allo']:
            for k, v in self.stuff2omor.items():
                if "ALLO=" in v:
                    self.stuff2omor[k] = ""
            self.allo = False
        self.props = True
        if 'props' not in kwargs or not kwargs['props']:
            for k, v in self.stuff2omor.items():
                if "PROPER=" in v:
                    self.stuff2omor[k] = ""
            self.props = False
        self.ktnkav = True
        if 'ktnkav' not in kwargs or not kwargs['ktnkav']:
            for k, v in self.stuff2omor.items():
                if "KTN=" in v or "KAV=" in v:
                    self.stuff2omor[k] = ""
            self.ktnkav = False
        self.newparas = True
        if 'newparas' not in kwargs or not kwargs['newparas']:
            for k, v in self.stuff2omor.items():
                if "NEWPARA=" in v:
                    self.stuff2omor[k] = ""
            self.newparas = False

    def stuff2lexc(self, stuff):
        if stuff == '0':
            return "0"
        if stuff in self.stuff2omor:
            return self.stuff2omor[stuff]
        else:
            if self.verbose:
                fail_formatting_missing_for(stuff, "omor")
            return "ERRORMACRO"

    def analyses2lexc(self, anals, surf):
        omorstring = ''
        for tag in anals.split('|'):
            if tag == '@@COPY-STEM@@':
                omorstring += lexc_escape(surf)
            elif tag.startswith('@@LITERAL') and tag.endswith('@@'):
                omorstring += lexc_escape(tag[len('@@LITERAL'):-len('@@')])
            else:
                omorstring += self.stuff2lexc(tag)
        return omorstring

    def continuation2lexc(self, anals, surf, cont):
        tags = self.analyses2lexc(anals, surf)
        surf = lexc_escape(surf)
        return "%s:%s\t%s ;\n" % (tags, surf, cont)

    def guesser2lexc(self, regex, deletion, cont):
        if not regex:
            regex = ''
        regex = egrep2xerox(regex)
        regex = regex_delete_surface(regex, deletion)
        return "< ?* %s >\t%s ;\n" % (regex, cont)

    def wordmap2lexc(self, wordmap):
        '''
        format string for canonical omor format for morphological analysis
        '''
        if wordmap['stub'] == ' ':
            # do not include normal white space for now
            return ""
        wordmap['stub'] = lexc_escape(wordmap['stub'])
        if int(wordmap['homonym']) == 1:
            wordmap['analysis'] = "[WORD_ID=%s]" % (
                lexc_escape(wordmap['lemma']))
        else:
            wordmap['analysis'] = "[WORD_ID=%s_%s]" % (
                lexc_escape(wordmap['lemma']), wordmap['homonym'])
        wordmap['analysis'] += self.stuff2lexc(wordmap['upos'])
        if wordmap['is_suffix']:
            wordmap['analysis'] += self.stuff2lexc('SUFFIX')
        if wordmap['is_prefix']:
            wordmap['analysis'] += self.stuff2lexc('PREFIX')
            if wordmap['upos'] == 'ADJ':
                wordmap['analysis'] += self.stuff2lexc('Cpos')

        if wordmap['blacklist']:
            wordmap['analysis'] += self.stuff2lexc('BLACKLISTED') + \
                wordmap['blacklist'] + ']'
        if wordmap['particle']:
            for pclass in wordmap['particle'].split('|'):
                wordmap['analysis'] += self.stuff2lexc(pclass)

        if wordmap['symbol']:
            for subcat in wordmap['symbol'].split('|'):
                wordmap['analysis'] += self.stuff2lexc(subcat)

        if wordmap['prontype']:
            for stuff in wordmap['prontype'].split("|"):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['lex']:
            for stuff in wordmap['lex'].split("|"):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['abbr']:
            for stuff in wordmap['abbr'].split("|"):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['numtype']:
            for stuff in wordmap['numtype'].split("|"):
                wordmap['analysis'] += self.stuff2lexc(stuff)
        if wordmap['adptype']:
            for stuff in wordmap['adptype'].split("|"):
                wordmap['analysis'] += self.stuff2lexc(stuff)

        if self.props and wordmap['proper_noun_class']:
            wordmap['analysis'] += self.stuff2lexc(wordmap['proper_noun_class'])
        if self.semantics and wordmap['sem']:
            wordmap['analysis'] += self.stuff2lexc(wordmap['sem'])

        if wordmap['style']:
            wordmap['analysis'] += self.stuff2lexc(wordmap['style'])

        if self.ktnkav and wordmap['upos'] != 'ACRONYM':
            tag = "[KTN=%s]" % (lexc_escape(wordmap['kotus_tn']))
            if tag in self.ktnkav_multichars:
                wordmap['analysis'] += tag
                if wordmap['kotus_av']:
                    wordmap['analysis'] += "[KAV=%(kotus_av)s]" % (wordmap)
        if self.newparas:
            wordmap['analysis'] += "[NEWPARA=%s]" % (wordmap['new_para'],)

        # match WORD_ID= with epsilon, then stub and lemma might match
        lex_stub = '0' + wordmap['stub']

        lexc_line = "%s:%s\t%s\t;" % (wordmap['analysis'], lex_stub,
                                      wordmap['new_para'])
        if 'BLACKLISTED' in wordmap['new_para']:
            return "! ! !" + lexc_line
        else:
            return lexc_line

    def multichars_lexc(self):
        multichars = "Multichar_Symbols\n"
        multichars += "!! OMOR multichars:\n"
        for mcs in self.common_multichars:
            multichars += mcs + "\n"
        multichars += Formatter.multichars_lexc(self)
        return multichars

    def root_lexicon_lexc(self):
        root = Formatter.root_lexicon_lexc(self)
        if True:
            # want co-ordinated hyphens
            root += "!! LEXICONS that can be co-ordinated hyphen -compounds\n"
            root += self.stuff2lexc('B→') + ':-   NOUN ;\n'
            root += self.stuff2lexc('B→') + ':-   ADJ ;\n'
            root += self.stuff2lexc('B→') + ':-   SUFFIX ;\n'
        if False:
            root += "0   TAGGER_HACKS    ;\n"
        return root

# self test
if __name__ == '__main__':
    from sys import exit
    formatter = OmorFormatter()
    exit(0)
