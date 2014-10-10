#!/usr/bin/env python3
#
# utils to format lexc strings from omor's lexical data sources.

from sys import stderr
from omor_strings_io import lexc_escape, version_id_easter_egg, \
        word_boundary, deriv_boundary, morph_boundary, stub_boundary,\
        weak_boundary, optional_hyphen
from cgi import escape as xml_escape
from apertium_formatter import format_tag_apertium, \
        format_analysis_lexc_apertium, format_continuation_lexc_apertium, \
        format_lexc_apertium, format_multichars_lexc_apertium

# these extra symbols appear always


common_multichars={
        version_id_easter_egg,
        word_boundary,
        weak_boundary,
        deriv_boundary,
        morph_boundary,
        stub_boundary,
        optional_hyphen
        }

ftb3_multichars= {
        '% A', '% V', '% N',
        '% Abbr', '% Pron', '% Num', '% Prop',
        '% Interj', '% Dem', '% Interr',
        '% Rel', '% Qnt', '% Refl',
        '% N% Abbr',
        '% %>%>%>',
        '% CS', '% CC', '% Adv',
        '% Adp', '% Po', '% Pr', '% Adp% Po',
        '% Punct',
        '% Quote',
        '% Dash',
        '% Digit',
        '% Roman',
        '% Nom', '% Par', '% Gen', '% Ine', '% Ela',
        '% Ill', '% Ade', '% Abl', '% All', '% Ess',
        '% Ins', '% Abe', '% Tra', '% Com' , '% Lat',
        '% Acc', '% Sg', '% Pl', '% PxSg1', '% PxSg2',
        '% PxPl1', '% PxPl2', '% PxPl3',
        '% Px3',
        '% TrunCo', 'TrunCo% ', '% TruncPrefix', 'TruncSuffix% ',
        '% Prt', '% Prs',
        '% Pst', '% Cond', '% Pot',
        '% Impv', '% Opt',
        '% Sg1', '% Sg2',
        '% Sg3', '% Pl1', '% Pl2', '% Pl3', '% Pe4',
        '% ConNeg' , '% Neg', 
        '% Act', '% Pass',
        '% Inf1', '% Inf2', '% Inf3', '% Inf5',
        '% PrsPrc', '% PrfPrc', '% AgPrc', '% NegPrc',
        '% Pos', '% Comp','% Superl',
        "% Dem", "% Qnt", "% Pers", "% Indef", "% Interr", "% Refl", "% Rel",
        '% Ord',
        '% Foc_hAn', '% Foc_kAAn', '% Foc_kin', '% Foc_kO',
        '% Foc_pA', '% Foc_s', '% Foc_kA', 
        '% Man', '%<Del%>→', '←%<Del%>'}

omor_multichars = {
        '[WORD_ID=', '[POS=ADJECTIVE]', '[POS=VERB]', '[POS=NOUN]',
        '[POS=PARTICLE]', '[POS=PRONOUN]', '[POS=NUMERAL]',
        '[PROPER=PROPER]', '[POS=ADVERB]', '[POS=ADPOSITION]',
        '[SUBCAT=QUALIFIER]', '[SUBCAT=INTERJECTION]',
        '[SUBCAT=DEMONSTR]', '[SUBCAT=PERSONAL]', '[SUBCAT=INTERROG]',
        '[SUBCAT=RELATIVE]', '[SUBCAT=QUANTOR]', '[SUBCAT=REFLEXIVE]',
        '[SUBCAT=RECIPROC]', '[SUBCAT=INDEF]', '[SUBCAT=DEMONSTRATIVE]',
        '[SUBCAT=INTERROGATIVE]',
        '[SUBCAT=CARD]', '[SUBCAT=ORD]',
        '[SUBCAT=CONJUNCTION]', '[CONJ=COORD]', '[CONJ=ADVERBIAL]',
        '[CONJ=COMPARATIVE]', '[SUBCAT=POSTPOSITION]', '[SUBCAT=PREPOSITION]',
        '[SUBCAT=PREFIX]', '[SUBCAT=SUFFIX]', '[SUBCAT=ABBREVIATION]',
        '[SUBCAT=ACRONYM]', 
        '[POS=PUNCTUATION]', '[POS=SYMBOL]', 
        '[SUBCAT=SPACE]', '[SUBCAT=QUOTATION]', '[SUBCAT=BRACKET]',
        '[SUBCAT=DASH]', '[SUBCAT=CURRENCY]', '[SUBCAT=MATH]',
        '[SUBCAT=OPERATION]', '[SUBCAT=RELATION]', '[SUBCAT=INITIAL]',
        '[SUBCAT=FINAL]', '[SUBCAT=REFLEXIVE]', '[SUBCAT=DIGIT]',
        '[SUBCAT=ROMAN]', '[SUBCAT=DECIMAL]',
        '[CASE=NOM]','[CASE=PAR]', '[CASE=GEN]', '[CASE=INE]', '[CASE=ELA]',
        '[CASE=ILL]', '[CASE=ADE]', '[CASE=ABL]', '[CASE=ALL]', '[CASE=ESS]',
        '[CASE=INS]', '[CASE=ABE]', '[CASE=TRA]', '[CASE=COM]' , '[CASE=LAT]',
        '[CASE=ACC]', '[NUM=SG]', '[NUM=PL]', '[POSS=SG1]', '[POSS=SG2]',
        '[POSS=SG3]', '[POSS=PL1]', '[POSS=PL2]', '[POSS=PL3]',
        '[POSS=3]',
        '[BOUNDARY=COMPOUND]', '[COMPOUND_FORM=S]', '[COMPOUND_FORM=OMIT]',
        '[TENSE=PRESENT]',
        '[TENSE=PAST]', '[MOOD=INDV]', '[MOOD=COND]', '[MOOD=POTN]',
        '[MOOD=IMPV]', '[MOOD=OPT]', '[MOOD=EVNV]',
        '[MOOD=INDV][TENSE=PAST]',
        '[PERS=SG1]', '[PERS=SG2]', '[PERS=SG3]', 
        '[PERS=PL1]', '[PERS=PL2]', '[PERS=PL3]', '[PERS=PE4]',
        '[NEG=CON]' , '[SUBCAT=NEG]', '[VOICE=ACT]', '[VOICE=PSS]',
        '[INF=A]', '[INF=E]', '[INF=MA]', '[INF=MINEN]', '[INF=MAISILLA]',
        '[DRV=MINEN]', '[DRV=MAISILLA]',
        '[PCP=NUT]', '[PCP=AGENT]', '[PCP=VA]', '[PCP=NEG]',
        '[DRV=NUT]', '[DRV=TU]', '[DRV=MA]', '[DRV=VA]', '[DRV=MATON]',
        '[CMP=POS]', '[CMP=CMP]','[CMP=SUP]',
        '[DRV=MPI]', '[DRV=IN]',
        '[CLIT=HAN]', '[CLIT=KAAN]', '[CLIT=KIN]', '[CLIT=KO]',
        '[CLIT=PA]', '[CLIT=S]', '[CLIT=KA]', '[DRV=STI]', '[DRV=JA]',
        '[DRV=INEN]', '[DRV=LAINEN]', '[DRV=TAR]', '[DRV=LLINEN]', '[DRV=TON]',
        '[DRV=TSE]', '[DRV=OI]', '[DRV=VS]', '[DRV=U]', '[DRV=TTAIN]',
        '[DRV=TTAA]', '[DRV=TATTAA]', '[DRV=TATUTTAA]', '[DRV=UUS]',
        '[DRV=S]', '[DRV=STI]', '[DRV=NUT]', '[DRV=TAVA]',
        '[STYLE=NONSTANDARD]', '[STYLE=RARE]', '[STYLE=DIALECTAL]',
        '[STYLE=ARCHAIC]', 
        '[GUESS=COMPOUND]', '[GUESS=DERIVE]', '[ALLO=A]',
        '[ALLO=TA]', '[ALLO=HVN]', '[ALLO=IA]', '[ALLO=IDEN]', '[ALLO=ITA]',
        '[ALLO=ITTEN]', '[ALLO=IEN]', '[ALLO=IHIN]', '[ALLO=IIN]', '[ALLO=IN]',
        '[ALLO=ISIIN]', '[ALLO=IDEN]', '[ALLO=JA]', '[ALLO=JEN]', '[ALLO=SEEN]',
        '[ALLO=TEN]', '[ALLO=VN]', '[FILTER=NO_PROC]',
        '[PROPER=FIRST]', '[PROPER=GEO]', '[PROPER=LAST]',
        '[PROPER=MISC]', '[PROPER=ORG]', '[PROPER=PRODUCT]', '[PROPER=EVENT]',
        '[PROPER=MEDIA]', '[PROPER=CULTGRP]', '[PROPER=ARTWORK]', '[SEM=TITLE]',
        '[SEM=ORG]', '[SEM=EVENT]', '[SEM=POLIT]', '[SEM=MEDIA]', '[SEM=GEO]',
        '[SEM=COUNTRY]', '[SEM=INHABITANT]', '[SEM=LANGUAGE]',
        '[SEM=MEASURE]', '[SEM=CURRENCY]', '[SEM=TIME]', '[SEM=MALE]', '[SEM=FEMALE]',
        '[POSITION=PREFIX]', '[POSITION=SUFFIX]',
        '[POS=NOUN][SUBCAT=ABBREVIATION]', 
        '[MOOD=INDV][TENSE=PRESENT]',
        '[MOOD=INDV][TENSE=PAST]'
        "[SUBCAT=DASH]", "[SUBCAT=SPACE]",
        "[BOUNDARY=CLAUSE]", "[BOUNDARY=SENTENCE]",
        "[SUBCAT=QUOTATION][POSITION=INITIAL]",
        "[SUBCAT=QUOTATION][POSITION=FINAL]",
        "[SUBCAT=BRACKET][POSITION=INITIAL]",
        "[SUBCAT=BRACKET][POSITION=FINAL]",
        "[POS=VERB][SUBCAT=NEG]"
        }

ktnkav_multichars = {
        '[KTN=1]', '[KTN=2]', '[KTN=3]', '[KTN=4]', '[KTN=5]',
        '[KTN=6]', '[KTN=7]', '[KTN=8]', '[KTN=9]', '[KTN=1%0]',
        '[KTN=11]', '[KTN=12]', '[KTN=13]', '[KTN=14]', '[KTN=15]',
        '[KTN=16]', '[KTN=17]', '[KTN=18]', '[KTN=19]', '[KTN=2%0]',
        '[KTN=21]', '[KTN=22]', '[KTN=23]', '[KTN=24]', '[KTN=25]',
        '[KTN=26]', '[KTN=27]', '[KTN=28]', '[KTN=29]', '[KTN=3%0]',
        '[KTN=31]', '[KTN=32]', '[KTN=33]', '[KTN=34]', '[KTN=35]',
        '[KTN=36]', '[KTN=37]', '[KTN=38]', '[KTN=39]', '[KTN=4%0]',
        '[KTN=41]', '[KTN=42]', '[KTN=43]', '[KTN=44]', '[KTN=45]',
        '[KTN=46]', '[KTN=47]', '[KTN=48]', '[KTN=49]', '[KTN=5%0]',
        '[KTN=51]', '[KTN=52]', '[KTN=53]', '[KTN=54]', '[KTN=55]',
        '[KTN=56]', '[KTN=57]', '[KTN=58]', '[KTN=59]', '[KTN=6%0]',
        '[KTN=61]', '[KTN=62]', '[KTN=63]', '[KTN=64]', '[KTN=65]',
        '[KTN=66]', '[KTN=67]', '[KTN=68]', '[KTN=69]', '[KTN=7%0]',
        '[KTN=71]', '[KTN=72]', '[KTN=73]', '[KTN=74]', '[KTN=75]',
        '[KTN=76]', '[KTN=77]', '[KTN=78]',
        '[KTN=1%0%07]', '[KTN=1%0%09]', '[KTN=1%01%0]', '[KTN=1%024]', '[KTN=1%026]',
        '[KAV=A]', '[KAV=B]', '[KAV=C]', '[KAV=D]', '[KAV=E]',
        '[KAV=F]', '[KAV=G]', '[KAV=H]', '[KAV=I]', '[KAV=J]',
        '[KAV=K]', '[KAV=L]', '[KAV=M]',
        '[KAV=N]', '[KAV=O]', '[KAV=P]', '[KAV=T]'}

stuff2ftb3 = {"Bc": "#",
        ".sent": "",
        "B-": "% TrunCo",
        "B→": "TrunCo% ",
        "B←": "% TrunCo",
        "Cma": "% AgPrc",
        "Cnut": "% PrfPrc",
        "Cva": "% PrsPrc",
        "Cmaton": "% NegPrc",
        "Cpos": "% Pos",
        "Ccmp": "% Comp",
        "Csup": "% Superl",
        "Dmaisilla": "% Inf5",
        "Dminen": "% N",
        "Dnut": "% A", "Dtu": "% A", "Dva": "% A", "Dtava": "% A",
        "Dmaton": "% N",
        "Duus": "", "Dttaa": "", "Dtattaa": "", "Dtatuttaa": "",
        "Dma": "", "Dinen": "", "Dja": "", "Dmpi": "",
        "Din": "", "Ds": "", "Du": "", "Dsti": "",
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

stuff2omor = {
        ".sent": "[BOUNDARY=SENTENCE]",
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
        "Osg1": "[POSS=SG1]", "Osg2": "[POSS=SG2]", "O3": "[POSS=3]",
        "Opl1": "[POSS=PL1]", "Opl2": "[POSS=PL2]",
        "Ppl1": "[PERS=PL1]", "Ppl2": "[PERS=PL2]",
        "Ppl3": "[PERS=PL3]", "Psg1": "[PERS=SG1]", "Psg2": "[PERS=SG2]",
        "Psg3": "[PERS=SG3]", "Ppe4": "[PERS=PE4]",
        "Qka": "[CLIT=KA]", "Qs": "[CLIT=S]",
        "Qpa": "[CLIT=PA]", "Qko": "[CLIT=KO]",
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
        "Vact": "[VOICE=ACT]", "Vpss": "[VOICE=PSS]",
        "Xabe": "[CASE=ABE]", "Xabl": "[CASE=ABL]",
        "Xade": "[CASE=ADE]", "Xall": "[CASE=ALL]",
        "Xcom": "[CASE=COM]", "Xela": "[CASE=ELA]",
        "Xess": "[CASE=ESS]", "Xgen": "[CASE=GEN]",
        "Xill": "[CASE=ILL]", "Xine": "[CASE=INE]",
        "Xins": "[CASE=INS]", "Xnom": "[CASE=NOM]",
        "Xpar": "[CASE=PAR]", "Xtra": "[CASE=TRA]", 
        "Xlat": "[CASE=LAT]", "Xacc": "[CASE=ACC]",
        "X???": "",
        "NOUN": "[POS=NOUN]", 
        "PARTICLE": "[POS=PARTICLE]", 
        "VERB": "[POS=VERB]",
        "ADVERB": "[POS=ADVERB]",
        "ADJECTIVE": "[POS=ADJECTIVE]",
        "CONJUNCTION": "[SUBCAT=CONJUNCTION]",
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
        "PL1": "[PERS=PL1]", "PL2": "[PERS=PL2]",
        "PL3": "[PERS=PL3]", "SG1": "[PERS=SG1]", "SG2": "[PERS=SG2]",
        "SG3": "[PERS=SG3]", "PE4": "[PERS=PE4]",
        "COMP": "[CMP=CMP]",
        "SUPERL": "[CMP=SUP]",
        "ARCHAIC": "[STYLE=ARCHAIC]",
        "DIALECTAL": "[STYLE=DIALECTAL]",
        "NONSTANDARD": "[STYLE=NONSTANDARD]",
        "RARE": "[STYLE=RARE]",
        "TITLE": "[SEM=TITLE]", "TIME": "[SEM=TIME]", 
        "CURRENCY": "[SEM=CURRENCY]", "MEDIA": "[SEM=MEDIA]", 
        "POLIT": "[SEM=POLIT]", "MEASURE": "[SEM=MEASURE]", 
        "MALE": "[SEM=MALE]", "FEMALE": "[SEM=FEMALE]", 
        "PROPER": "[PROPER=PROPER]", 
        "CULTGRP": "[PROPER=CULTGRP]", "PRODUCT": "[PROPER=PRODUCT]",
        "ARTWORK": "[PROPER=ARTWORK]", "EVENT": "[PROPER=EVENT]", 
        "FIRST": "[PROPER=FIRST]", "LAST": "[PROPER=LAST]", 
        "GEO": "[PROPER=GEO]", "ORG": "[PROPER=ORG]", 
        "MISC": "[PROPER=MISC]",
        "COUNTRY": "[SEM=COUNTRY]",
        "INHABITANT": "[SEM=INHABITANT]",
        "LANGUAGE": "[SEM=LANGUAGE]",
        "PUNCTUATION": "[POS=PUNCTUATION]",
        "DASH": "[SUBCAT=DASH]",
        "SPACE": "[SUBCAT=SPACE]",
        "CLAUSE-BOUNDARY": "[BOUNDARY=CLAUSE]",
        "SENTENCE-BOUNDARY": "[BOUNDARY=SENTENCE]",
        "INITIAL-QUOTE": "[SUBCAT=QUOTATION][POSITION=INITIAL]",
        "FINAL-QUOTE": "[SUBCAT=QUOTATION][POSITION=FINAL]",
        "INITIAL-BRACKET": "[SUBCAT=BRACKET][POSITION=INITIAL]",
        "FINAL-BRACKET": "[SUBCAT=BRACKET][POSITION=FINAL]",
        "UNSPECIFIED": "",
        "FTB3man": "",
        "LEMMA-START": "[WORD_ID=",
        "CONJUNCTIONVERB": "[POS=VERB][SUBCAT=NEG]", 
        "": ""}


google_multichars = {"% NOUN", "% ADJ", "% VERB", "% ADV", "% X", "% PRON",
        '%<Del%>→', '←%<Del%>',
        "% NUM", "% ADP", "% CONJ", "% PRT", "% ."}

stuff2google = {
        ".sent": "",
        "Bc": "#",
        "B-": "",
        "B→": "",
        "B←": "",
        "Cma": "",
        "Cnut": "",
        "Cva": "",
        "Cmaton": "",
        "Cpos": "",
        "Ccmp": "",
        "Csup": "",
        "Dmaisilla": "% ADV",
        "Dminen": "% NOUN",
        "Dnut": "% ADJ", "Dtu": "% ADJ", "Dva": "% ADJ", "Dtava": "% ADJ",
        "Dmaton": "% NOUN",
        "Duus": "% NOUN", "Dttaa": "% VERB", "Dtattaa": "% VERB",
        "Dtatuttaa": "% VERB",
        "Dma": "% NOUN", "Dinen": "% ADJ", "Dja": "% NOUN", "Dmpi": "% ADJ",
        "Din": "% ADJ", "Ds": "", "Du": "% NOUN", "Dsti": "% ADV",
        "FTB3man": "",
        "Ia": "",
        "Ie": "",
        "Ima": "",
        "Iminen": "",
        "Ncon": "",
        "Nneg": "", 
        "Npl": "", 
        "Nsg": "", 
        "N??": "",
        "Osg1": "",
        "Osg2": "",
        "O3": "",
        "Opl1": "",
        "Opl2": "",
        "Ppl1": "", 
        "Ppl2": "",
        "Ppl3": "",
        "Psg1": "", 
        "Psg2": "",
        "Psg3": "",
        "Ppe4": "", 
        "Qka": "% CONJ",
        "Qs": "",
        "Qpa": "",
        "Qko": "",
        "Qkin": "",
        "Qkaan": "",
        "Qhan": "",
        "Tcond": "",
        "Timp": "", 
        "Tpast": "",
        "Tpot": "", 
        "Tpres": "",
        "Topt": "",
        "Uarch": "", "Udial": "", "Urare": "", "Unonstd": "",
        "Vact": "",
        "Vpss": "",
        "Xabe": "",
        "Xabl": "",
        "Xade": "",
        "Xall": "",
        "Xcom": "",
        "Xela": "",
        "Xess": "", 
        "Xgen": "",
        "Xill": "", 
        "Xine": "",
        "Xins": "",
        "Xnom": "",
        "Xpar": "", 
        "Xtra": "", 
        "Xlat": "",
        "Xacc": "",
        "X???": "",
        "NOUN": "% NOUN",
        "ADJECTIVE": "% ADJ", "QUALIFIER": "% ADJ",
        "VERB": "% VERB",
        "ADVERB": "% ADV",
        "INTERJECTION": "% X",
        "PRONOUN": "% PRON",
        "PARTICLE": "% PRT",
        "NUMERAL": "% NUM",
        "ADPOSITION": "% ADP",
        "CONJUNCTION": "% CONJ", "COORDINATING": "", "ADVERBIAL": "",
        "COMPARATIVE": "",
        "ABBREVIATION": "% PRT", "ACRONYM": "% NOUN",
        "PROPER": "",
        "CARDINAL": "", "ORDINAL": "",
        "DEMONSTRATIVE": "", "QUANTOR": "", "PERSONAL": "",
        "INDEFINITE": "", "INTERROGATIVE": "",
        "REFLEXIVE": "", "RELATIVE": "",
        "RECIPROCAL": "",
        "PL1": "", 
        "PL2": "",
        "PL3": "",
        "SG1": "", 
        "SG2": "",
        "SG3": "",
        "PE4": "",
        "COMP": "",
        "SUPERL": "",
        "UNSPECIFIED": "% X",
        "PUNCTUATION": "% .",
        "DASH": "",
        "SPACE": "",
        "CLAUSE-BOUNDARY": "",
        "SENTENCE-BOUNDARY": "",
        "INITIAL-QUOTE": "",
        "FINAL-QUOTE": "",
        "INITIAL-BRACKET": "",
        "FINAL-BRACKET": "",
        "LEMMA-START": "",
        "": ""
        }

def format_copyright_lexc():
    return """
! This automatically generated lexc data is originated from omorfi database.
! Copyright (c) 2014 Omorfi contributors

! This program is free software: you can redistribute it and/or modify
! it under the terms of the GNU General Public License as published by
! the Free Software Foundation, version 3 of the License

! This program is distributed in the hope that it will be useful,
! but WITHOUT ANY WARRANTY; without even the implied warranty of
! MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
! GNU General Public License for more details.

! You should have received a copy of the GNU General Public License
! along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

def format_lexc(wordmap, format):
    if format.startswith("omor"):
        return format_lexc_omor(wordmap, format)
    elif format.startswith("ftb3"):
        return format_lexc_ftb3(wordmap, format)
    elif format.startswith("apertium"):
        return format_lexc_apertium(wordmap)
    elif format.startswith("google"):
        return format_lexc_google(wordmap)
    elif format.startswith("segment"):
        return format_lexc_segments(wordmap)
    else:
        print("missing format", format, file=stderr)

def format_continuation_lexc(fields, format):
    stuffs = ""
    for cont in fields[3:]:
        if format.startswith("omor"):
            stuffs += format_continuation_lexc_omor(fields[1], fields[2], cont, format)
        elif format.startswith("ftb3"):
            stuffs += format_continuation_lexc_ftb3(fields[1], fields[2], cont)
        elif format.startswith("google"):
            stuffs += format_continuation_lexc_google(fields[1], fields[2], cont)
        elif format.startswith("segment"):
            stuffs += format_continuation_lexc_segments(fields[1], fields[2], cont)
        elif format.startswith("apertium"):
            stuffs += format_continuation_lexc_apertium(fields[1], fields[2], cont)
        else:
            print("missing format", format, file=stderr)
    return stuffs

def format_analysis_lexc(analyses, format):
    stuffs = ''
    if format.startswith("omor"):
        stuffs += format_analysis_lexc_omor(analyses, format)
    elif format.startswith("ftb3"):
        stuffs += format_analysis_lexc_ftb3(analyses)
    elif format.startswith("google"):
        stuffs += format_analysis_lexc_google(analyses)
    elif format.startswith("apertium"):
        stuffs += format_analysis_lexc_apertium(analyses)
    elif format.startswith("segment"):
        stuffs += format_analysis_lexc_segments(analyses)
    else:
        print("missing format", format, file=stderr)
    return stuffs

def format_tag(stuff, format):
    if format.startswith('omor'):
        return format_tag_omor(stuff, format)
    elif format.startswith('ftb3'):
        return format_tag_ftb3(stuff)
    elif format.startswith('google'):
        return format_tag_google(stuff)
    elif format.startswith('segment'):
        return ''
    elif format.startswith('apertium'):
        return format_tag_apertium(stuff)
    else:
        print("Wrong format for generic tag formatting:", format, file=stderr)

def format_tag_omor(stuff, format):
    if stuff == '0':
        return "0"
    if stuff in stuff2omor:
        return stuff2omor[stuff]
    else:
        print("Missing from omor mapping: ", stuff, file=stderr)
        return ""


def format_tag_ftb3(stuff):
    if stuff == '0':
        return "0"
    elif stuff in stuff2ftb3:
        return stuff2ftb3[stuff]
    else:
        print("Missing from ftb3 mapping: ", stuff, file=stderr)
        return ""

def format_tag_google(stuff):
    if stuff == '0':
        return "0"
    elif stuff in stuff2google:
        return stuff2google[stuff]
    else:
        print("Missing from google mapping: ", stuff, file=stderr)
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

def format_analysis_lexc_omor(anals, format):
    omorstring = ''
    for tag in anals.split('|'):
        omorstring += format_tag_omor(tag, format)
    return omortstring

def format_analysis_lexc_google(anals):
    googstring = ''
    for tag in anals.split('|'):
        googstring += format_tag_google(tag)
    return googstring

def format_analysis_segments(anals):
    return ''


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


def format_continuation_lexc_google(anals, surf, cont):
    ftbstring = format_analysis_lexc_google(anals)
    if 'COMPOUND' in cont:
        ftbstring =  surf.replace(morph_boundary, '').replace(deriv_boundary, '')
    if surf != '0':
        surf = lexc_escape(surf)
    return "%s:%s\t%s ;\n" %(ftbstring, surf, cont)

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
        omorstring += format_tag_omor(tag, format)
    surf = lexc_escape(surf)
    return "%s:%s\t%s ;\n" %(omorstring, surf, cont)

def format_continuation_lexc_segments(anals, surf, cont):
    surf = lexc_escape(surf)
    return "%s:%s\t%s ; \n" %(surf.replace(optional_hyphen, word_boundary),
            surf, cont)

def format_lexc_omor(wordmap, format):
    '''
    format string for canonical omor format for morphological analysis
    '''
    if wordmap['stub'] == ' ':
        # do not include normal white space for now
        return ""
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    wordmap['analysis'] = "[WORD_ID=%s]" %(lexc_escape(wordmap['lemma']))
    wordmap['particle'] = wordmap['particle'].replace('QUALIFIER', 'ADJECTIVE')
    if wordmap['pos'] != 'PARTICLE' or not wordmap['particle'].startswith('AD'):
        wordmap['analysis'] += format_tag_omor(wordmap['pos'], format)
    if wordmap['is_suffix']:
        wordmap['analysis'] += format_tag_omor('SUFFIX', format)
    if wordmap['is_prefix']:
        wordmap['analysis'] += format_tag_omor('PREFIX', format)
        if wordmap['pos'] == 'ADJECTIVE':
            wordmap['analysis'] += format_tag_omor('Cpos', format)

    if wordmap['particle']:
        for pclass in wordmap['particle'].split('|'):
            wordmap['analysis'] += format_tag_omor(pclass, format)

    if wordmap['symbol']:
        for subcat in wordmap['symbol'].split('|'):
            wordmap['analysis'] += format_tag_omor(subcat, format)
    
    if wordmap['subcat']:
        for subcat in wordmap['subcat'].split('|'):
            wordmap['analysis'] += format_tag_omor(subcat, format)
    
    if wordmap['is_proper']:
        if '+propers' in format and wordmap['proper_noun_class']:
            for prop in wordmap['proper_noun_class'].split(','):
                wordmap['analysis'] += format_tag_omor(prop, format)
        else:
            wordmap['analysis'] += format_tag_omor('PROPER', format)

    if '+semantics' in format and wordmap['sem']:
        for sem in wordmap['sem'].split(','):
            wordmap['analysis'] += format_tag_omor(sem, format)

    if wordmap['style']:
        wordmap['analysis'] += format_tag_omor(wordmap['style'], format)
    
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
    for new_para in wordmap['new_paras']:
        retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, 
                new_para)]
    return "\n".join(retvals)

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

def format_lexc_google(wordmap):
    '''
    format string for canonical google universal pos format for morphological analysis
    '''
    if wordmap['stub'] == ' ':
        # do not include normal white space for now
        return ""
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    wordmap['analysis'] = "%s" %(lexc_escape(wordmap['bracketstub'].replace(word_boundary, '#')  + '←<Del>'))
    wordmap['analysis'] += format_tag_google(wordmap['pos'])
    if wordmap['particle']:
        for pclass in wordmap['particle'].split('|'):
            wordmap['analysis'] += format_tag_google(pclass)
    if wordmap['subcat']:
        for subcat in wordmap['subcat'].split('|'):
            wordmap['analysis'] += format_tag_google(subcat)
    if wordmap['is_proper']:
        wordmap['analysis'] += format_tag_google('PROPER')
    lex_stub = wordmap['stub']
    retvals = []
    for new_para in wordmap['new_paras']:
        retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, 
                new_para)]
    return "\n".join(retvals)

def format_lexc_segments(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['stub']) + '{STUB}'
    retvals = []
    lex_stub = lexc_escape(wordmap['stub'])
    for new_para in wordmap['new_paras']:
        retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, new_para)]
    return "\n".join(retvals)


def format_multichars_lexc(format):
    multichars = "Multichar_Symbols\n"
    if format.startswith("omor"):
        multichars += "!! OMOR set:\n"
        for mcs in omor_multichars:
            multichars += mcs + "\n"
    elif format.startswith("ftb3"):
        multichars += "!! FTB 3 set:\n"
        for mcs in ftb3_multichars:
            multichars += mcs + "\n"
    elif format.startswith("google"):
        multichars += "!! Google universal pos set:\n"
        for mcs in google_multichars:
            multichars += mcs + "\n"
    elif format.startswith("segments"):
        pass
    elif format.startswith("apertium"):
        multichars += format_multichars_lexc_apertium()
    else:
        print("missing format", format, file=stderr)
        exit(1)
    if "+ktnkav" in format:
        multichars += "!! KTNKAV set:\n"
        for mcs in ktnkav_multichars:
            multichars += mcs + "\n"
    if "+newparas" in format:
        multichars += """!! NEWPARA set:
[NEWPARA=
        """
    multichars += "!! Following specials exist in all versions of omorfi\n"
    for mcs in common_multichars:
        multichars += mcs + "\n"
    return multichars

def format_root_lexicon(format):
    root = "LEXICON Root\n"
    root += """!! ...
0   NOUN ;
0   ADJECTIVE ;
0   VERB    ;
0   NUMERAL ;
0   DIGITS ;
0   ACRONYM ;
0   PRONOUN    ;
0   PARTICLE    ;
0   INTERJECTION ;
0   PUNCTUATION ;
0   CONJUNCTIONVERB ;
"""
    root += format_tag('B→', format) + ':-   NOUN ;\n'
    root += format_tag('B→', format) + ':-   ADJECTIVE ;\n'
    root += format_tag('B→', format) + ':-   SUFFIX ;\n'
    root += version_id_easter_egg + ':0 # ;\n'
    if '+taggerhacks' in format:
        root += "0   TAGGER_HACKS    ;\n"
    return root

def format_xml_kotus_sanalista(wordmap):
    kotus_xml = '    <st><s>' + wordmap['lemma'] + '</s>'
    kotus_xml += '<t>'
    if wordmap['kotus_tn'] != '0':
        kotus_xml += '<tn>' + wordmap['kotus_tn'] + '</tn>'
    if wordmap['kotus_av'] and wordmap['kotus_av'] != 'False':
        kotus_xml += '<av>' + wordmap['kotus_av'] + '</av>'
    kotus_xml += '</t></st>'
    return kotus_xml

def make_xmlid(s):
    return s.replace("?", "_UNK").replace("→", "_right").replace("←", "left").replace(".", "_")

def format_multichars_lexc_xml():
    multichars = "  <Multichar_Symbols>\n"
    for key, value in stuff2ftb3.items():
        key = make_xmlid(key)
        if key != '':
            if value != '':
                multichars += "    <mcs id='" + key + "'>" + xml_escape(value) + "</mcs>\n"
            else:
                multichars += "    <mcs id='" + key + "'>" + key + "</mcs>\n"
        else:
            pass

    multichars += """<!-- Following specials exist in all versions of omorfi -->
    <mcs id="hyph">{hyph?}</mcs> 
    <mcs id="deriv">»</mcs>
    <mcs id="infl">&gt;</mcs>
    <mcs id="wb">|</mcs>
    """
    multichars += "    <mcs id='VERSION'>" + version_id_easter_egg + '</mcs>\n'
    multichars += "  </Multichar_Symbols>"
    return multichars

def format_root_lexicon_xml():
    root = '  <LEXICON id="Root">\n'
    root += """<!-- ... -->
    <e><a/><i/><cont lexica="NOUNS ADJECTIVES VERBS NUMERALS DIGITSS ACRONYMS PRONOUNS PARTICLES PUNCTUATIONS FIFTYONE"/></e>
"""
    root += '    <e><a><s mcs="B_right"/></a><i>-</i><cont lexica="NOUN ADJECTIVE SUFFIX"/></e>\n'
    root += '    <e><a><s mcs="VERSION"/></a><i/><cont lexica="_end"/></e>\n'
    root += '  </LEXICON>\n'
    return root

def format_lexc_xml(wordmap):
    analysis = xml_escape(wordmap['lemma'])
    analysis = analysis.replace('|', '<s mcs="wb"/>').replace('_', '<s mcs="mb"/>')
    analysis += '<s mcs="' + wordmap['pos'] + '"/>'
    if wordmap['is_proper']:
        analysis += '<s mcs="proper"/>'
    if wordmap['is_suffix']:
        analysis = "<s mcs='suffix'/>" + analysis
    if wordmap['is_prefix']:
        analysis += "<s mcs='prefix'/>"
    stub = xml_escape(wordmap['stub'])
    stub = stub.replace('|', '<s mcs="wb"/>').replace('_', '<s mcs="mb"/>')
    return ('    <e><a>%s</a><i>%s</i><cont lexica="%s"/></e>' % 
            (analysis, stub, " ".join(wordmap['new_paras'])))

def format_continuation_lexicon_xml(tsvparts):
    xmlstring = '    <e>'
    if tsvparts[1] != '':
        xmlstring += '<a>'
        for anal in tsvparts[1].split('|'):
            if anal in stuff2ftb3:
                anal = make_xmlid(anal)
                xmlstring += '<s mcs="' + anal + '"/>'
            else:
                xmlstring += xml_escape(anal)
        xmlstring += '</a>'
    else:
        xmlstring += '<a/>'
    xmlstring += "<i>" + xml_escape(tsvparts[2]) + "</i>"
    xmlstring += '<cont lexica="' + " ".join(tsvparts[3:]).replace("#", "_END") + '"/></e>\n'
    return xmlstring

# self test
if __name__ == '__main__':
    fail = False
    for stuff, omor in stuff2omor.items():
        if len(omor) < 2:
            continue
        elif not omor in omor_multichars:
            print("There are conflicting formattings in here!", omor, 
                    "is not a valid defined omor multichar_symbol!")
            fail = True
    for stuff, ftb3 in stuff2ftb3.items():
        if len(ftb3) < 2:
            continue
        elif not ftb3 in ftb3_multichars:
            print("There are conflicting formattings in here!", ftb3, 
                    "is not a valid defined ftb3 multichar_symbol!")
            fail = True
    for stuff, ftb3 in stuff2ftb3.items():
        if len(ftb3) < 2:
            continue
        if not stuff in stuff2omor:
            print("There are conflicting formattings in here!", stuff, 
                    "has no mapping in omor!")
            fail = True
    if fail:
        exit(1)

