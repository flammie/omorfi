#!/usr/bin/env python3
#
# utils to format lexc strings from omor's lexical data sources.

from sys import stderr
from omor_strings_io import lexc_escape

version_id_easter_egg='OMORFI_VERSION_≥_14_©_GNU_GPL_V3'

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
        '[WORD_ID=', '[SEGMENT=',
        '[SUBCAT=ADJECTIVE]', '[POS=VERB]', '[POS=NOUN]',
        '[POS=PARTICLE]', '[SUBCAT=PRONOUN]', '[SUBCAT=NUMERAL]',
        '[PROPER=PROPER]', '[POS=ADVERB]', '[POS=ADPOSITION]',
        '[SUBCAT=QUALIFIER]', '[SUBCAT=INTERJECTION]',
        '[SUBCAT=DEMONSTRATIVE]', '[SUBCAT=PERSONAL]', '[SUBCAT=INTERROGATIVE]',
        '[SUBCAT=RELATIVE]', '[SUBCAT=QUANTOR]', '[SUBCAT=REFLEXIVE]',
        '[SUBCAT=RECIPROCAL]', '[SUBCAT=INDEFINITE]',
        '[SUBCAT=CARDINAL]', '[SUBCAT=ORDINAL]',
        '[SUBCAT=CONJUNCTION]', '[CONJ=COORDINATING]', '[CONJ=ADVERBIAL]',
        '[CONJ=COMPARATIVE]', '[SUBCAT=POSTPOSITION]', '[SUBCAT=PREPOSITION]',
        '[SUBCAT=PREFIX]', '[SUBCAT=SUFFIX]', '[SUBCAT=ABBREVIATION]',
        '[SUBCAT=ACRONYM]', 
        '[POS=PUNCTUATION]', '[POS=SYMBOL]',
        '[SUBCAT=SPACE]', '[SUBCAT=QUOTATION]', '[SUBCAT=BRACKET]',
        '[SUBCAT=DASH]', '[SUBCAT=CURRENCY]', '[SUBCAT=MATH]',
        '[SUBCAT=OPERATION]', '[SUBCAT=RELATION]', '[SUBCAT=INITIAL]',
        '[SUBCAT=FINAL]',
        '[CASE=NOMINATIVE]',
        '[CASE=PARTITIVE]', '[CASE=GENITIVE]', '[CASE=INESSIVE]',
        '[CASE=ELATIVE]',
        '[CASE=ILLATIVE]',
        '[CASE=ADESSIVE]', '[CASE=ABLATIVE]', '[CASE=ALLATIVE]',
        '[CASE=ESSIVE]',
        '[CASE=INSTRUCTIVE]',
        '[CASE=ABESSIVE]',
        '[CASE=TRANSLATIVE]',
        '[CASE=COMITATIVE]',
        '[CASE=LATIVE]',
        '[CASE=ACCUSATIVE]',
        '[NUMBER=SINGULAR]', '[NUMBER=PLURAL]',
        '[POSSESSIVE=1STSINGULAR]', '[POSSESSIVE=2NDSINGULAR]',
        '[POSSESSIVE=3RDSINGULAR]', '[POSSESSIVE=1STPLURAL]',
        '[POSSESSIVE=2NDPLURAL]', '[POSSESSIVE=3RDPLURAL]',
        '[POSSESSIVE=3RDAMBIGUOUS]',
        '[BOUNDARY=COMPOUND]', '[COMPOUND_FORM=S]', '[COMPOUND_FORM=OMIT]', 
        '[TENSEMOOD=PRESENTINDICATIVE]',
        '[TENSEMOOD=PASTINDICATIVE]',
        '[TENSEMOOD=CONDITIONAL]',
        '[TENSEMOOD=POTENTIAL]',
        '[TENSEMOOD=IMPERATIVE]',
        '[TENSEMOOD=OPTATIVE]',
        '[TENSEMOOD=EVENTIVE]',
        '[PERSON=1STSINGULAR]', '[PERSON=2NDSINGULAR]',
        '[PERSON=3RDSINGULAR]', '[PERSON=1STPLURAL]',
        '[PERSON=2NDPLURAL]', '[PERSON=3RDPLURAL]',
        '[PERSON=IMPERSONAL]',
        '[NEGATION=CON]' , '[SUBCAT=NEGATIONVERB]',
        '[VOICE=ACTIVE]', '[VOICE=PASSIVE]',
        '[INFINITIVE=A]', '[INFINITIVE=E]', '[INFINITIVE=MA]', '[INFINITIVE=MINEN]',
        '[DERIVATION=MINEN]', '[DERIVATION=MAISILLA]',
        '[PARTICIPLE=NUT]', '[PARTICIPLE=AGENT]', '[PARTICIPLE=VA]',
        '[PARTICIPLE=NEGATION]',
        '[DERIVATION=NUT]', '[DERIVATION=TU]', '[DERIVATION=MA]',
        '[DERIVATION=VA]', '[DERIVATION=MATON]',
        '[DERIVATION=TAVA]',
        '[COMPARISON=POSITIVE]', '[COMPARISON=COMPARATIVE]',
        '[COMPARISON=SUPERLATIVE]',
        '[DERIVATION=MPI]', '[DERIVATION=IN]', 
        '[CLITIC=HAN]', '[CLITIC=KAAN]', '[CLITIC=KIN]', '[CLITIC=KO]',
        '[CLITIC=PA]', '[CLITIC=S]', '[CLITIC=KA]', '[DERIVATION=STI]', 
        '[DERIVATION=JA]',
        '[DERIVATION=INEN]', '[DERIVATION=LAINEN]', '[DERIVATION=TAR]',
        '[DERIVATION=LLINEN]', '[DERIVATION=TON]',
        '[DERIVATION=TSE]', '[DERIVATION=OI]', '[DERIVATION=VS]',
        '[DERIVATION=U]', '[DERIVATION=TTAIN]',
        '[DERIVATION=TTAA]', '[DERIVATION=TATTAA]', '[DERIVATION=TATUTTAA]',
        '[DERIVATION=UUS]',
        '[DERIVATION=S]', '[DERIVATION=NUT]',
        '[STYLE=NONSTANDARD]', '[STYLE=RARE]', '[STYLE=DIALECTAL]',
        '[STYLE=ARCHAIC]', '[GUESS=COMPOUND]', '[GUESS=DERIVE]', '[ALLO=A]',
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
        '[POS=NOUN][SUBCAT=ABBREVIATION]', 
        '[POSITION=PREFIX]', '[POSITION=SUFFIX]'}

omor_short_multichars = {
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
        '[SUBCAT=FINAL]', '[SUBCAT=REFLEXIVE]',
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
        '[PERS=SG1]', '[PERS=SG2]', '[PERS=SG3]', 
        '[PERS=PL1]', '[PERS=PL2]', '[PERS=PL3]', '[PERS=PE4]',
        '[NEG=CON]' , '[SUBCAT=NEG]', '[VOICE=ACT]', '[VOICE=PSS]',
        '[INF=A]', '[INF=E]', '[INF=MA]', '[INF=MINEN]',
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
        '[DRV=S]', '[DRV=NUT]', '[DRV=TAVA]',
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
        '[MOOD=INDV][TENSE=PAST]'}

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
        '[KAV=A]', '[KAV=B]', '[KAV=C]', '[KAV=D]', '[KAV=E]',
        '[KAV=F]', '[KAV=G]', '[KAV=H]', '[KAV=I]', '[KAV=J]',
        '[KAV=K]', '[KAV=L]', '[KAV=M]',
        '[KAV=N]', '[KAV=O]', '[KAV=P]', '[KAV=T]'}

stuff2ftb3 = {"Bc": "#",
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
        "Din": "", "Ds": "", "Du": "",
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
        "PL1": "% Pl1", 
        "PL2": "% Pl2",
        "PL3": "% Pl3",
        "SG1": "% Sg1", 
        "SG2": "% Sg2",
        "SG3": "% Sg3",
        "PE4": "% Pe4",
        "COMP": "% Comp",
        "SUPERL": "% Superl",
        "UNSPECIFIED": ""
        }

stuff2omor = {"Bc": "[BOUNDARY=COMPOUND]",
        "B-": "[COMPOUND_FORM=OMIT]",
        "B→": "[POSITION=SUFFIX]",
        "B←": "[POSITION=PREFIX]",
        "Cma": "[PARTICIPLE=AGENT]",
        "Cmaton": "[PARTICIPLE=NEGATION]",
        "Cnut": "[PARTICIPLE=NUT]",
        "Cva": "[PARTICIPLE=VA]",
        "Cpos": "",
        #"Cpos": "[COMPARISON=POSITIVE]",
        "Ccmp": "[COMPARISON=COMPARATIVE]",
        "Csup": "[COMPARISON=SUPERLATIVE]",
        "Dinen": "[DERIVATION=INEN]",
        "Dja": "[DERIVATION=JA]",
        "Dmaisilla": "[INFINITIVE=MAISILLA]",
        #"Dmaisilla": "[DERIVATION=MAISILLA]",
        "Dminen": "[DERIVATION=MINEN]",
        "Dtu": "[DERIVATION=TU]",
        "Dnut": "[DERIVATION=NUT]",
        "Dva": "[DERIVATION=VA]",
        "Dtava": "[DERIVATION=TAVA]",
        "Dma": "[DERIVATION=MA]",
        "Dmaton": "[DERIVATION=MATON]", 
        "Ds": "[DERIVATION=S]",
        "Dttaa": "[DERIVATION=TTAA]",
        "Dtattaa": "[DERIVATION=TATTAA]",
        "Dtatuttaa": "[DERIVATION=TATUTTAA]",
        "Du": "[DERIVATION=U]",
        "Duus": "[DERIVATION=UUS]",
        "Dmpi": "",
        #"Dmpi": "[DERIVATION=MPI]",
        "Din": "",
        #"Din": "[DERIVATION=IN]",
        "Ia": "[INFINITIVE=A]",
        "Ie": "[INFINITIVE=E]",
        "Ima": "[INFINITIVE=MA]",
        "Iminen": "[INFINITIVE=MINEN]",
        "Ncon": "[NEGATION=CON]",
        "Nneg": "[SUBCAT=NEGATIONVERB]", 
        "Npl": "[NUMBER=PLURAL]", 
        "Nsg": "[NUMBER=SINGULAR]", 
        "N??": "",
        "Osg1": "[POSSESSIVE=1STSINGULAR]",
        "Osg2": "[POSSESSIVE=2NDSINGULAR]",
        "O3": "[POSSESSIVE=3RDAMBIGUOUS]",
        "Opl1": "[POSSESSIVE=1STPLURAL]",
        "Opl2": "[POSSESSIVE=2NDPLURAL]",
        "Ppl1": "[PERSON=1STPLURAL]", 
        "Ppl2": "[PERSON=2NDPLURAL]",
        "Ppl3": "[PERSON=3RDPLURAL]",
        "Psg1": "[PERSON=1STSINGULAR]", 
        "Psg2": "[PERSON=2NDSINGULAR]",
        "Psg3": "[PERSON=3RDSINGULAR]",
        "Ppe4": "[PERSON=IMPERSONAL]", 
        "Qka": "[CLITIC=KA]",
        "Qs": "[CLITIC=S]",
        "Qpa": "[CLITIC=PA]",
        "Qko": "[CLITIC=KO]",
        "Qkin": "[CLITIC=KIN]",
        "Qkaan": "[CLITIC=KAAN]",
        "Qhan": "[CLITIC=HAN]",
        "Tcond": "[TENSEMOOD=CONDITIONAL]",
        "Timp": "[TENSEMOOD=IMPERATIVE]", 
        "Tpast": "[TENSEMOOD=PASTINDICATIVE]",
        "Tpot": "[TENSEMOOD=POTENTIAL]", 
        "Topt": "[TENSEMOOD=OPTATIVE]",
        "Tpres": "[TENSEMOOD=PRESENTINDICATIVE]",
        "Uarch": "[STYLE=ARCHAIC]",
        "Udial": "[STYLE=DIALECTAL]",
        "Unonstd": "[STYLE=NONSTANDARD]",
        "Urare": "[STYLE=RARE]",
        "Vact": "[VOICE=ACTIVE]",
        "Vpss": "[VOICE=PASSIVE]",
        "Xabe": "[CASE=ABESSIVE]",
        "Xabl": "[CASE=ABLATIVE]",
        "Xade": "[CASE=ADESSIVE]",
        "Xall": "[CASE=ALLATIVE]",
        "Xcom": "[CASE=COMITATIVE]",
        "Xela": "[CASE=ELATIVE]",
        "Xess": "[CASE=ESSIVE]", 
        "Xgen": "[CASE=GENITIVE]",
        "Xill": "[CASE=ILLATIVE]", 
        "Xine": "[CASE=INESSIVE]",
        "Xins": "[CASE=INSTRUCTIVE]",
        "Xnom": "[CASE=NOMINATIVE]",
        "Xpar": "[CASE=PARTITIVE]", 
        "Xtra": "[CASE=TRANSLATIVE]", 
        "Xlat": "[CASE=LATIVE]",
        "Xacc": "[CASE=ACCUSATIVE]",
        "X???": "",
        "NOUN": "[POS=NOUN]", 
        "PARTICLE": "[POS=PARTICLE]", 
        "VERB": "[POS=VERB]",
        "ADVERB": "[POS=ADVERB]",
        "ADJECTIVE": "[SUBCAT=ADJECTIVE]",
        "CONJUNCTION": "[SUBCAT=CONJUNCTION]",
        "COORDINATING": "[CONJ=COORDINATING]",
        "COMPARATIVE": "[CONJ=COMPARATIVE]",
        "PRONOUN": "[SUBCAT=PRONOUN]",
        "ADVERBIAL": "[CONJ=ADVERBIAL]",
        "NUMERAL": "[SUBCAT=NUMERAL]",
        "CARDINAL": "[SUBCAT=CARDINAL]", 
        "ORDINAL": "[SUBCAT=ORDINAL]",
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
        #"INDEFINITE": "[SUBCAT=INDEFINITE]", 
        "INTERROGATIVE": "[SUBCAT=INTERROGATIVE]",
        "REFLEXIVE": "[SUBCAT=REFLEXIVE]", 
        "RELATIVE": "[SUBCAT=RELATIVE]",
        "RECIPROCAL": "[SUBCAT=RECIPROCAL]",
        "PL1": "[PERSON=1STPLURAL]", 
        "PL2": "[PERSON=2NDPLURAL]",
        "PL3": "[PERSON=3RDPLURAL]",
        "SG1": "[PERSON=1STSINGULAR]", 
        "SG2": "[PERSON=2NDSINGULAR]",
        "SG3": "[PERSON=3RDSINGULAR]",
        "PE4": "[PERSON=IMPERSONAL]", 
        "COMP": "[COMPARISON=COMPARATIVE]",
        "SUPERL": "[COMPARISON=SUPERLATIVE]",
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
        "COUNTRY": "[SEM=COUNTRY]",
        "INHABITANT": "[SEM=INHABITANT]",
        "LANGUAGE": "[SEM=LANGUAGE]",
        "MISC": "[PROPER=MISC]",
        "UNSPECIFIED": "",
        "FTB3man": ""}

stuff2omor_short = {
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
        "COUNTRY": "[SEM=COUNTRY]",
        "INHABITANT": "[SEM=INHABITANT]",
        "LANGUAGE": "[SEM=LANGUAGE]",
        "MISC": "[PROPER=MISC]",
        "UNSPECIFIED": "",
        "FTB3man": ""}

monodix_sdefs= {
        'adj', 'vblex', 'n',
        'abbr', 'prn', 'num', 'pn',
        'ij', 'dem', 'itg',
        'rel', 'reflex',
        'rec', 'part',
        'ind', 'card', 'ord',
        'cnjcoo', 'cnjsub', 'post', 'pr',
        'infa', 'infma', 'infe',
        'nom', 'par', 'gen', 'ine', 'ela',
        'ill', 'ade', 'abl', 'all', 'ess',
        'ins', 'abe', 'tra', 'com' , 'lat',
        'acc', 'sg', 'pl', 'pxsg1', 'pxsg2',
        'pxpl1', 'pxpl2', 'pxsp3',
        'pres', 'past',
        'indv', 'cond', 'pot',
        'imp',
        'p1', 'p2', 'p3', 'impers',
        'conneg' , 'neg', 
        'actv', 'pasv',
        'pp', 'pprs', 'agent', 'pneg',
        'pos', 'comp','sup',
        'qst',
        'enc',
        'cmp',
        'ND'}

stuff2monodix =  {"Bc": "+",
        "B-": "-",
        "B→": "-",
        "B←": "-",
        "Cma": "agent",
        "Cnut": "pp",
        "Cva": "pprs",
        "Cmaton": "pneg",
        "Cpos": "pos",
        "Ccmp": "com",
        "Csup": "sup",
        "Dmaisilla": "",
        "Dminen": "n",
        "Dnut": "", "Dtu": "", "Duus": "", "Dva": "", "Dmaton": "",
        "Dttaa": "", "Dtattaa": "", "Dtatuttaa": "",
        "Dma": "", "Dinen": "", "Dja": "", "Dmpi": "",
        "Din": "", "Ds": "", "Du": "",
        "Ia": "infa",
        "Ie": "infe",
        "Ima": "infma",
        "Ncon": "conneg",
        "Nneg": "neg", 
        "Npl": "pl", 
        "Nsg": "sg", 
        "N??": "ND",
        "Osg1": "pxsg1",
        "Osg2": "pxsg2",
        "O3": "pxsp3",
        "Opl1": "pxpl1",
        "Opl2": "pxpl2",
        "Ppl1": "p1><pl", 
        "Ppl2": "p2><pl",
        "Ppl3": "p3><pl",
        "Psg1": "p1><sg", 
        "Psg2": "p2><sg",
        "Psg3": "p3><sg",
        "Ppe4": "impers", 
        "Qka": "enc",
        "Qs": "enc",
        "Qpa": "enc",
        "Qko": "qst",
        "Qkin": "enc",
        "Qkaan": "enc",
        "Qhan": "enc",
        "Tcond": "cond",
        "Timp": "imp", 
        "Tpast": "past",
        "Tpot": "pot", 
        "Tpres": "pres",
        "Topt": "",
        "Uarch": "", "Udial": "", "Urare": "", "Unonstd": "",
        "Vact": "actv",
        "Vpss": "pasv",
        "Xabe": "abe",
        "Xabl": "abl",
        "Xade": "ade",
        "Xall": "all",
        "Xcom": "com",
        "Xela": "ela",
        "Xess": "ess", 
        "Xgen": "gen",
        "Xill": "ill", 
        "Xine": "ine",
        "Xins": "ins",
        "Xnom": "nom",
        "Xpar": "par", 
        "Xtra": "tra", 
        "Xlat": "lat",
        "Xacc": "acc",
        "X???": "",
        "NOUN": "n",
        "ADJECTIVE": "a", "QUALIFIER": "a",
        "VERB": "vblex",
        "ADVERB": "adv",
        "INTERJECTION": "ij",
        "PARTICLE": "part",
        "PRONOUN": "prn",
        "NUMERAL": "num",
        "ADPOSITION": "post",
        "CONJUNCTION": "", "COORDINATING": "cnjcoo", "ADVERBIAL": "cnjsub",
        "COMPARATIVE": "cnjsub",
        "ABBREVIATION": "abbr", "ACRONYM": "abbr",
        "PROPER": "pn",
        "CARDINAL": "card", "ORDINAL": "ord",
        "DEMONSTRATIVE": "dem", "QUANTOR": "", "PERSONAL": "pers",
        "INDEFINITE": "ind", "INTERROGATIVE": "itg",
        "REFLEXIVE": "reflex", "RELATIVE": "rel", "RECIPROCAL": "rec",
        "UNSPECIFIED": ""}



def format_lexc(wordmap, format):
    if format.startswith("omor") or format.startswith("ktnkav"):
        return format_lexc_omor(wordmap, format)
    elif format.startswith("ftb3"):
        return format_lexc_ftb3(wordmap, format)
    elif format.startswith("apertium"):
        return format_lexc_apertium(wordmap)

def format_continuation_lexc(fields, format):
    stuffs = ""
    for cont in fields[3:]:
        if format.startswith("omor") or format.startswith("ktnkav"):
            stuffs += format_continuation_lexc_omor(fields[1], fields[2], cont, format)
        elif format.startswith("ftb3"):
            stuffs += format_continuation_lexc_ftb3(fields[1], fields[2], cont)
    return stuffs

def format_analysis_lexc(analyses, format):
    stuffs = ''
    if format.startswith("omor") or format.startswith("ktnkav"):
        stuffs += format_analysis_lexc_omor(analyses, format)
    elif format.startswith("ftb3"):
        stuffs += format_analysis_lexc_ftb3(analyses)
    return stuffs

def format_tag(stuff, format):
    if format.startswith('omor') or format.startswith('ktnkav'):
        return format_tag_omor(stuff, format)
    elif format.startswith('ftb3'):
        return format_tag_ftb3(stuff)
    else:
        print("Wrong format for generic tag formatting:", format, file=stderr)

def format_tag_omor(stuff, format):
    if stuff == '0':
        return "0"
    elif format.startswith("omor-short") or format.startswith("ktnkav"):
        if stuff in stuff2omor_short:
            return stuff2omor_short[stuff]
        else:
            print("Missing from omor-short mapping: ", stuff, file=stderr)
            exit(1)
    elif stuff in stuff2omor:
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

def format_analysis_lexc_ftb3(anals):
    ftbstring = ""
    if 'Nneg|Vact' in anals:
        anals = anals.replace('|Vact', '')
    elif anals == 'Vact|Ia|Nsg|Xlat':
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

def format_continuation_lexc_ftb3(anals, surf, cont):
    ftbstring = format_analysis_lexc_ftb3(anals)
    if 'COMPOUND' in cont:
        ftbstring +=  surf.replace('%>', '').replace('»', '')
    return "%s:%s\t%s ;\n" %(ftbstring, surf, cont)

def format_analysis_lexc_omor(anals, format):
    omorstring = ''
    for i in anals.split('|'):
        omorstring += format_tag_omor(tags[i], format)
    return omortstring

def format_continuation_lexc_omor(anals, surf, cont, format):
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
    
    morphs = surf.split('>')
    tags = anals.split('|')
    omorstring = ''
    if 'no-segments' in format:
        for tag in tags:
            omorstring += format_tag_omor(tag, format)
    elif len(morphs) == len(tags):
        for i in range(len(tags)):
            if morphs[i] != '' and morphs[i] != '0':
                omorstring += "[SEGMENT=" + morphs[i] + "]"
            omorstring += format_tag_omor(tags[i], format)
    else:
        for morph in morphs:
            if morph != '' and morph != '0':
                print("Segment: ", morph, "!", sep='"')
                omorstring += '[SEGMENT=' + morph + ']'
        for tag in tags:
            omorstring += format_tag_omor(tag, format)
    return "%s:%s\t%s ;\n" %(omorstring, surf, cont)

def format_lexc_omor(wordmap, format):
    '''
    format string for canonical omor format for morphological analysis
    '''
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

    # XXX: use stuff2omor to ensure multichars but laziness
    if format.startswith("ktnkav") and tn < 99:
        wordmap['analysis'] += "[KTN=%(kotus_tn)s]" %(wordmap)
        if wordmap['kotus_av']:
            wordmap['analysis'] += "[KAV=%(kotus_av)s]" %(wordmap)
    elif format.startswith("newparas"):
        wordmap['analysis'] += "[NEWPARA=%(new_para)s]" %(wordmap)

    if wordmap['style']:
        wordmap['analysis'] += format_tag_omor(wordmap['style'], format)
    
    if not 'no-segments' in format:
        wordmap['analysis'] += '[SEGMENT=' + wordmap['stub'] + ']'
    # match WORD_ID= with epsilon, then stub and lemma might match
    lex_stub = '0' + wordmap['stub'][:1] + \
               wordmap['stub'][1:].replace('|', '{hyph?}').replace('_', '')
    retvals = []
    for new_para in wordmap['new_paras']:
        retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, 
                new_para)]
    return "\n".join(retvals)
    
def format_lexc_ftb3(wordmap, format):
    '''
    format string for canonical ftb3 format for morphological analysis
    '''
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    wordmap['analysis'] = "%s" %(lexc_escape(wordmap['bracketstub'].replace('|', '#')  + '←<Del>'))
    if wordmap['pos'] in ['NOUN', 'VERB', 'ADJECTIVE', 'PRONOUN', 'NUMERAL', 'ACRONYM']:
        wordmap['analysis'] += format_tag_ftb3(wordmap['pos'])
    elif wordmap['particle']:
        for pclass in wordmap['particle'].split('|'):
            wordmap['analysis'] += format_tag_ftb3(pclass)
    if wordmap['subcat']:
        for subcat in wordmap['subcat'].split('|'):
            wordmap['analysis'] += format_tag_ftb3(subcat)
    if wordmap['is_proper']:
        wordmap['analysis'] += format_tag_ftb3('PROPER')
    lex_stub = wordmap['stub'][:1] + wordmap['stub'][1:].replace('|', '{hyph?}').replace('_', '')
    retvals = []
    for new_para in wordmap['new_paras']:
        retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, 
                new_para)]
    return "\n".join(retvals)

def format_lexc_apertium(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['lemma'])
    wordmap['analysis'] = wordmap['analysis'].replace('|', '+').replace('_', '')
    if wordmap['is_suffix']:
        wordmap['analysis'] = "+" + wordmap['analysis']
    elif wordmap['is_prefix']:
        wordmap['analysis'] += "+"
    if wordmap['pos'] == 'NOUN':
        if wordmap['is_proper']:
            wordmap['analysis'] += '%<np%>'
        else:
            wordmap['analysis'] += '%<n%>'
    elif wordmap['pos'] == 'VERB':
        wordmap['analysis'] += '%<vblex%>'
    elif wordmap['pos'] == 'ADJECTIVE':
        wordmap['analysis'] += '%<adj%>'
    elif wordmap['pos'] in ['ACRONYM', 'ABBREVIATION']:
        wordmap['analysis'] += "%<abbr%>"
    elif wordmap['pos'] == 'CONJUNCTION':
        wordmap['analysis'] += "%<cnjcoo%>"
    elif wordmap['pos'] == 'INTERJECTION':
        wordmap['analysis'] += "%<interj%>"
    elif wordmap['pos'] == 'ADVERB':
        wordmap['analysis'] += "%<adv%>"
    elif wordmap['pos'] == 'ADPOSITION':
        wordmap['analysis'] += "%<pp%>"
    elif wordmap['pos'] == 'PARTICLE':
        wordmap['analysis'] += "%<adv%>"
    else:
        print("Missed this pose: %s(pos)" %(wordmap))
        wordmap['analysis'] += "%<errpos%>"


    wordmap['stub'] = lexc_escape(wordmap['stub'])
    return ("%(analysis)s:%(stub)s\t%(new_para)s\t;" % (wordmap))

def format_multichars_lexc(format):
    multichars = "Multichar_Symbols\n"
    if format.startswith("omor-short") or format.startswith("ktnkav"):
        multichars += "!! OMOR (short) set:\n"
        for mcs in omor_short_multichars:
            multichars += mcs + "\n"
    elif format.startswith("omor"):
        multichars += "!! OMOR set:\n"
        for mcs in omor_multichars:
            multichars += mcs + "\n"
    elif format.startswith("ftb3"):
        multichars += "!! FTB 3 set:\n"
        for mcs in ftb3_multichars:
            multichars += mcs + "\n"
    if format.startswith("ktnkav"):
        multichars += "!! KTNKAV set:\n"
        for mcs in ktnkav_multichars:
            multichars += mcs + "\n"
    if format.startswith("newparas"):
        multichars += """!! NEWPARA set:
[NEWPARA=
        """
    multichars += """!! Following specials exist in all versions of omorfi
    {hyph?} {»} {%>}
    """
    multichars += version_id_easter_egg + '\n'
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
0   PUNCTUATION ;
0   51 ;
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

def format_monodix_alphabet():
    """Finnish alphabet as in CLDR 24"""
    return ("<alphabet>abcdefghijklmnopqrsštuvwxyzžåäö"
            "ABCDEFGHIJKLMNOPQRSŠTUVWXYZŽ"
            "áàâãčçđéèêëǧǥȟíîïǩńñŋôõœřßŧúùûÿüʒǯæø"
            "ÁÀÂÃČÇÐÉÈÊËǦÍÎÏĸŃÑŊÔÕŘÚÙÛŸÜƷǮÆØ"
            "</alphabet>")

def format_monodix_sdefs():
    sdefs = '  <sdefs>\n'
    for sdef in monodix_sdefs:
        sdefs += '    <sdef n="' + sdef + '"/>\n'
    sdefs += '  </sdefs>\n'
    return sdefs

def format_monodix_l(s):
    if s != '0':
        return s.replace(' ', '<b/>').replace('%>', '').replace('%', '')
    else:
        return ''

def format_monodix_r(anals):
    r = ''
    if anals != '0':
        for anal in anals.split('|'):
            r += format_monodix_s(anal)
    return r

def format_monodix_s(stuff):
    s = ''
    if stuff in stuff2monodix:
        s += '<s n="' + stuff2monodix[stuff] + '"/>'
    else:
        print("Missing", stuff, "from monodix map",
                file=stderr)
    if '><' in s:
        s = s.replace('><', '"/><s n="')
    elif '"+"' in s:
        s = '+'
    elif '""' in s:
        s = ''
    elif '"-"' in s:
        s = '-'
    return s

def format_monodix_par(cont):
    return '<par n="'+  cont.lower().replace('_', '__') + '"/>'

def format_monodix_pardef(fields):
    pardef = ''
    for cont in fields[3:]:
        pardef += '      <e>'
        if fields[1] == fields[2]:
            pardef += '<i>' + format_monodix_l(fields[2]) + '</i>'
        else:
            pardef += '<p><l>' + format_monodix_l(fields[2]) + '</l>'
            pardef += '<r>' + format_monodix_r(fields[1]) + '</r></p>'
        if cont != '#':
            pardef += format_monodix_par(cont)
        pardef += '</e>\n'
    return pardef


def format_monodix_entry(wordmap):
    for cont in wordmap['new_paras']:
        e = '<e lm="' + wordmap['lemma'].replace('&', '&amp;') + '">'
        e += '<p><l>' + wordmap['stub'].replace('|', '').replace('&', '&amp;')  +  '</l>'
        e += '<r>'
        e += wordmap['lemma'].replace('&', '&amp;')
        e += format_monodix_s(wordmap['real_pos'] or wordmap['pos'])
        e += '</r></p>'
        e += format_monodix_par(cont)
        e += '</e>'
    return e

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
    for stuff, omor in stuff2omor_short.items():
        if len(omor) < 2:
            continue
        elif not omor in omor_short_multichars:
            print("There are conflicting formattings in here!", omor, 
                    "is not a valid defined omor-short multichar_symbol!")
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
        if not stuff in stuff2omor_short:
            print("There are conflicting formattings in here!", stuff, 
                    "has no mapping in omor_short!")
            fail = True
    if fail:
        exit(1)

