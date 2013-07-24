#!/usr/bin/env python3
#
# utils to format lexc strings from omor's lexical data sources.

from sys import stderr
from lexc_string_utils import lexc_escape

ftb3_multichars= {
        '% A', '% V', '% N',
        '% Abbr', '% Pron', '% Num', '% Prop',
        '% Interj', '% Dem', '% Interr',
        '% Rel', '% Qnt', '% Refl',
        '% >>>',
        '% CS', '% CC', '% Adv',
        '% Adp', '% Po', '% Pr',
        '% Punct',
        '% Quote',
        '% Nom', '% Par', '% Gen', '% Ine', '% Ela',
        '% Ill', '% Ade', '% Abl', '% All', '% Ess',
        '% Ins', '% Abe', '% Tra', '% Com' , '% Lat',
        '% Acc', '% Sg', '% Pl', '% PxSg1', '% PxSg2',
        '% PxPl1', '% PxPl2', '% PxPl3',
        '% Px3',
        'TrunCo', 
        '% Prt', '% Prs',
        '% Pst', '% Cond', '% Pot',
        '% Impv',
        '% Sg1', '% Sg2',
        '% Sg3', '% Pl1', '% Pl2', '% Pl3', '% Pe4',
        '% ConNeg' , '% Neg', 
        '% Act', '% Pass',
        '% Inf1', '% Inf2', '% Inf3', '% Inf5',
        '% PrsPrc', '% PrfPrc', '% AgPrc',
        '% Pos', '% Comp','% Superl',
        '% Foc_hAn', '% Foc_kAAn', '% Foc_kin', '% Foc_kO',
        '% Foc_pA', '% Foc_s', '% Foc_kA'}
omor_multichars = {
        '[WORD_ID=', '[SUBCAT=ADJECTIVE]', '[POS=VERB]', '[POS=NOUN]',
        '[POS=PARTICLE]', '[SUBCAT=PRONOUN]', '[SUBCAT=NUMERAL]',
        '[SUBCAT=PROPER]', '[SUBCAT=ADVERB]', '[SUBCAT=ADPOSITION]',
        '[SUBCAT=QUALIFIER]', '[SUBCAT=INTERJECTION]',
        '[SUBCAT=DEMONSTRATIVE]', '[SUBCAT=PERSONAL]', '[SUBCAT=INTERROGATIVE]',
        '[SUBCAT=RELATIVE]', '[SUBCAT=QUANTOR]', '[SUBCAT=REFLEXIVE]',
        '[SUBCAT=RECIPROCAL]', '[SUBCAT=INDEFINITE]',
        '[SUBCAT=CARDINAL]', '[SUBCAT=ORDINAL]',
        '[SUBCAT=CONJUNCTION]', '[SUBCAT=COORDINATING]', '[SUBCAT=ADVERBIAL]',
        '[SUBCAT=COMPARATIVE]', '[SUBCAT=POSTPOSITION]', '[SUBCAT=PREPOSITION]',
        '[SUBCAT=PREFIX]', '[SUBCAT=SUFFIX]', '[SUBCAT=ABBREVIATION]',
        '[SUBCAT=ACRONYM]', '[SUBCAT=PUNCTUATION]', '[SUBCAT=SYMBOL]',
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
        '[INFINITIVE=A]', '[INFINITIVE=E]', '[INFINITIVE=MA]',
        '[DERIVATION=MINEN]', '[DERIVATION=MAISILLA]',
        '[PARTICIPLE=NUT]', '[PARTICIPLE=AGENT]', '[PARTICIPLE=VA]',
        '[PARTICIPLE=NEGATION]',
        '[DERIVATION=NUT]', '[DERIVATION=TU]', '[DERIVATION=MA]',
        '[DERIVATION=VA]', '[DERIVATION=MATON]',
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
        '[ALLO=TEN]', '[ALLO=VN]', '[FILTER=NO_PROC]'}
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
        "B-": "TrunCo",
        "Cma": "% AgPrc",
        "Cnut": "% PrfPrc",
        "Cva": "% PrsPrc",
        "Cmaton": "",
        "Cpos": "% Pos",
        "Ccmp": "% Comp",
        "Csup": "% Superl",
        "Dmaisilla": "% Inf5",
        "Dminen": "% N",
        "Dnut": "", "Dtu": "", "Duus": "", "Dva": "", "Dmaton": "",
        "Dttaa": "", "Dtattaa": "", "Dtatuttaa": "",
        "Dma": "", "Dinen": "", "Dja": "", "Dmpi": "",
        "Din": "", "Ds": "",
        "Ia": "% Inf1",
        "Ie": "% Inf2",
        "Ima": "% Inf3",
        "Ncon": "% ConNeg",
        "Nneg": "% Neg", 
        "Npl": "% Pl", 
        "Nsg": "% Sg", 
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
        "Topt": "",
        "Uarch": "", "Udial": "", "Urare": "",
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
        "NOUN": "% N",
        "ADJECTIVE": "% A", "QUALIFIER": "% A",
        "VERB": "% V",
        "ADVERB": "% Adv",
        "INTERJECTION": "% Interj",
        "PRONOUN": "% Pron",
        "NUMERAL": "% Num",
        "ADPOSITION": "% Adp",
        "CONJUNCTION": "", "COORDINATING": "% CC", "ADVERBIAL": "% CS",
        "COMPARATIVE": "% CS",
        "ABBREVIATION": "% Abbr",
        "PROPER": "% Prop"}
        

stuff2omor = {"Bc": "[BOUNDARY=COMPOUND]",
        "B-": "[COMPOUND_FORM=OMIT]",
        "Cma": "[PARTICIPLE=AGENT]",
        "Cmaton": "[PARTICIPLE=NEGATION]",
        "Cnut": "[PARTICIPLE=NUT]",
        "Cva": "[PARTICIPLE=VA]",
        "Cpos": "[COMPARISON=POSITIVE]",
        "Ccmp": "[COMPARISON=COMPARATIVE]",
        "Csup": "[COMPARISON=SUPERLATIVE]",
        "Dinen": "[DERIVATION=INEN]",
        'Dja': '[DERIVATION=JA]',
        "Dmaisilla": "[DERIVATION=MAISILLA]",
        "Dminen": "[DERIVATION=MINEN]",
        "Dtu": "[DERIVATION=TU]",
        "Dva": "[DERIVATION=TU]",
        "Dnut": "[DERIVATION=NUT]",
        "Dma": "[DERIVATION=MA]",
        "Dmaton": "[DERIVATION=MATON]", 
        "Ds": "[DERIVATION=S]",
        "Dttaa": "[DERIVATION=TTAA]",
        "Dtattaa": "[DERIVATION=TATTAA]",
        "Dtatuttaa": "[DERIVATION=TATUTTAA]",
        "Duus": "[DERIVATION=UUS]",
        "Dmpi": "[DERIVATION=MPI]",
        "Din": "[DERIVATION=IN]",
        "Ia": "[INFINITIVE=A]",
        "Ie": "[INFINITIVE=E]",
        "Ima": "[INFINITIVE=MA]",
        "Ncon": "[NEGATION=CON]",
        "Nneg": "[SUBCAT=NEGATIONVERB]", 
        "Npl": "[NUMBER=PLURAL]", 
        "Nsg": "[NUMBER=SINGULAR]", 
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
        "NOUN": "[POS=NOUN]", "PARTICLE": "[POS=PARTICLE]", 
        "VERB": "[POS=VERB]",
        "ADVERB": "[SUBCAT=ADVERB]",
        "ADJECTIVE": "[SUBCAT=ADJECTIVE]",
        "CONJUNCTION": "[SUBCAT=CONJUNCTION]",
        "COORDINATING": "[SUBCAT=COORDINATING]",
        "COMPARATIVE": "[SUBCAT=COMPARATIVE]",
        "PRONOUN": "[SUBCAT=PRONOUN]",
        "ADVERBIAL": "[SUBCAT=ADVERBIAL]",
        "NUMERAL": "[SUBCAT=NUMERAL]",
        "QUALIFIER": "[SUBCAT=QUALIFIER]",
        "ACRONYM": "[SUBCAT=ACRONYM]", "ABBREVIATION": "[SUBCAT=ABBREVIATION]",
        "SUFFIX": "[SUBCAT=SUFFIX]", "PREFIX": "[SUBCAT=PREFIX]",
        "INTERJECTION": "[SUBCAT=INTERJECTION]",
        "ADPOSITION": "[SUBCAT=ADPOSITION]",
        "TITLE": "", "TIME": "", "BAND": "", "PRODUCT": "", "CURRENCY": "",
        "MEDIA": "", "POLIT": "", "ARTWORK": "", "MEASURE": "", "EVENT": "",
        "PROPER": "", "GEO": "", "FIRST": "", "LAST": "", "ORG": "", "MISC": ""}

def format_lexc(wordmap, format):
    if format in ["omor", "ktnkav"]:
        return format_lexc_omor(wordmap, format)
    elif format.startswith("ftb3"):
        return format_lexc_ftb3(wordmap, format)
    elif format == "apertium":
        return format_lexc_apertium(wordmap)

def format_continuation_lexc(fields, format):
    stuffs = ""
    for cont in fields[3:]:
        if format in ["omor", "ktnkav"]:
            stuffs += format_continuation_lexc_omor(fields[1], fields[2], cont)
        elif format.startswith('ftb3'):
            stuffs += format_continuation_lexc_ftb3(fields[1], fields[2], cont)
    return stuffs

def format_tag_omor(stuff):
    if stuff == '0':
        return "0"
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

def format_continuation_lexc_ftb3(anals, surf, cont):
    ftbstring = ""
    parts = anals.split('|')
    reordered = []
    for part in parts:
        if part.startswith('X'):
            # Case X before Number N
            reordered.append(part)
        elif part.startswith('T'):
            # Tense T before Voice V
            reordered.append(part)
    parts = [x for x in parts if not x.startswith('X') and not x.startswith('T')]
    for part in parts:
        reordered.append(part)
    for anal in reordered:
        ftbstring += format_tag_ftb3(anal)
    return "%s:%s\t%s ;\n" %(ftbstring, surf, cont)

def format_continuation_lexc_omor(anals, surf, cont):
    omorstring = ""
    for anal in anals.split('|'):
        omorstring += format_tag_omor(anal)
    return "%s:%s\t%s ;\n" %(omorstring, surf, cont)

def format_lexc_omor(wordmap, format):
    '''
    format string for canonical omor format for morphological analysis
    '''
    tn = int(wordmap['kotus_tn'])
    wordmap['analysis'] = "[WORD_ID=%s]" %(lexc_escape(wordmap['lemma']))
    wordmap['analysis'] += format_tag_omor(wordmap['pos'])
    if wordmap['is_suffix']:
        wordmap['analysis'] += format_tag_omor('SUFFIX')
    elif wordmap['is_prefix']:
        wordmap['analysis'] += format_tag_omor('PREFIX')

    if wordmap['subcat']:
        wordmap['analysis'] += format_tag_omor(wordmap['subcat'])
    
    if wordmap['particle']:
        pclasses = wordmap['particle'].split('|')
        for pclass in pclasses:
            wordmap['analysis'] += format_tag_omor(pclass)

    if wordmap['is_proper']:
        wordmap['analysis'] += format_tag_omor('PROPER')
        if wordmap['proper_noun_class']:
            for prop in wordmap['proper_noun_class'].split(','):
                wordmap['analysis'] += format_tag_omor(prop)

    if wordmap['sem']:
        for sem in wordmap['sem'].split(','):
            wordmap['analysis'] += format_tag_omor(sem)

    # XXX: use stuff2omor to ensure multichars but laziness
    if format == 'ktnkav' and tn < 99:
        wordmap['analysis'] += "[KTN=%(kotus_tn)s]" %(wordmap)
        if wordmap['kotus_av']:
            wordmap['analysis'] += "[KAV=%(kotus_av)s]" %(wordmap)
    elif format == 'newparas':
        wordmap['analysis'] += "[PARA=%(new_para)s]" %(wordmap)
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    # match WORD_ID= with epsilon, then stub and lemma might match
    wordmap['stub'] = '0' + wordmap['stub'].replace('|', '%-%0', 32).replace('_', '', 32)
    retvals = []
    for new_para in wordmap['new_paras']:
        retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], wordmap['stub'], 
                new_para)]
    return "\n".join(retvals)

def format_lexc_ftb3(wordmap, format):
    '''
    format string for canonical ftb3 format for morphological analysis
    '''
    tn = int(wordmap['kotus_tn'])
    wordmap['analysis'] = "%s" %(lexc_escape(wordmap['lemma']))
    if wordmap['pos'] in ['NOUN', 'VERB', 'ADJECTIVE', 'PRONOUN', 'NUMERAL']:
        wordmap['analysis'] += format_tag_ftb3(wordmap['pos'])
    elif wordmap['particle']:
        pclasses = wordmap['particle'].split('|')
        for pclass in pclasses:
            wordmap['analysis'] += format_tag_ftb3(pclass)
    if wordmap['subcat']:
        wordmap['analysis'] += format_tag_ftb3(wordmap['subcat'])
    if wordmap['is_proper']:
        wordmap['analysis'] += format_tag_ftb3('PROPER')
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    # match WORD_ID= with epsilon, then stub and lemma might match
    wordmap['stub'] = wordmap['stub'].replace('|', '%-%0', 32).replace('_', '', 32)
    retvals = []
    for new_para in wordmap['new_paras']:
        retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], wordmap['stub'], 
                new_para)]
    return "\n".join(retvals)

def format_lexc_apertium(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['lemma'])
    wordmap['analysis'] = wordmap['analysis'].replace('|', '+', 32).replace('_', '', 32)
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
    if format in ['ktnkav', 'omor']:
        multichars += "!! OMOR set:\n"
        for mcs in omor_multichars:
            multichars += mcs + "\n"
    if format == 'ktnkav':
        multichars += "!! KTNKAV set:\n"
        for mcs in omor_multichars_ktnkav:
            multichars += mcs + "\n"
    if format == 'newparas':
        multichars += """!! NEWPARA set:
[NEWPARA=
        """
    multichars += """!! optional boundary hyphen inconditionally
    %-%0
    """
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
    return root

def format_xml_kotus_sanalista(wordmap):
    if wordmap['kotus_av']:
        return ("<st><s>%(lemma)s</s><t><tn>%(kotus_tn)s</tn><av>%(kotus_av)s</av></t></st>" %(wordmap))
    else:
        return ("<st><s>%(lemma)s</s><t><tn>%(kotus_tn)s</tn></t></st>" %(wordmap))

# self test
if __name__ == '__main__':
    for stuff, omor in stuff2omor.items():
        if len(omor) < 2:
            continue
        elif not omor in omor_multichars:
            print("There are conflicting formattings in here!", omor, 
                    "is not a valid defined multichar_symbol!")
            exit(1)
    for stuff, ftb3 in stuff2ftb3.items():
        if len(ftb3) < 2:
            continue
        elif not ftb3 in ftb3_multichars:
            print("There are conflicting formattings in here!", ftb3, 
                    "is not a valid defined multichar_symbol!")
            exit(1)

