#!/usr/bin/env python3
#
# utils to format apertium style data from omorfi database values

from omor_strings_io import lexc_escape, word_boundary, weak_boundary, \
        morph_boundary, deriv_boundary, optional_hyphen, \
        fail_formatting_missing_for


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

def format_tag_omor(stuff, format):
    if stuff == '0':
        return "0"
    if stuff in stuff2omor:
        return stuff2omor[stuff]
    else:
        print("Missing from omor mapping: ", stuff, file=stderr)
        return ""


def format_analysis_lexc_omor(anals, format):
    omorstring = ''
    for tag in anals.split('|'):
        omorstring += format_tag_omor(tag, format)
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
        omorstring += format_tag_omor(tag, format)
    surf = lexc_escape(surf)
    return "%s:%s\t%s ;\n" %(omorstring, surf, cont)

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

def format_multichars_lexc_omor():
    multichars = ''
    for mcs in omor_multichars:
        multichars += mcs + "\n"
    return multichars


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
    if fail:
        exit(1)

