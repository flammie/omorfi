#!/usr/bin/env python3
#
# utils to convert all tag formats with omor as pivot

omor2ftb3 = {
        '[WORD_ID=': '',
        '[SUBCAT=ADJECTIVE]': ' A',
        '[POS=VERB]': ' V',
        '[POS=NOUN]': ' N',
        '[POS=PARTICLE]': '',
        '[SUBCAT=PRONOUN]': ' Pron',
        '[SUBCAT=NUMERAL]': ' Num',
        '[SUBCAT=PROPER]': ' Prop',
        '[SUBCAT=ADVERB]': ' Adv',
        '[SUBCAT=ADPOSITION]': '',
        '[SUBCAT=QUALIFIER]': ' A',
        '[SUBCAT=INTERJECTION]': ' Interj',
        '[SUBCAT=DEMONSTRATIVE]': ' Dem',
        '[SUBCAT=PERSONAL]': ' Pers',
        '[SUBCAT=INTERROGATIVE]': ' Interr',
        '[SUBCAT=RELATIVE]': ' Rel',
        '[SUBCAT=QUANTOR]': ' Qu',
        '[SUBCAT=REFLEXIVE]': ' Reflex',
        '[SUBCAT=RECIPROCAL]': ' Rec',
        '[SUBCAT=INDEFINITE]': ' Ind',
        '[SUBCAT=CARDINAL]': '',
        '[SUBCAT=ORDINAL]': ' Ord',
        '[SUBCAT=CONJUNCTION]': '',
        '[SUBCAT=COORDINATING]': ' CC',
        '[SUBCAT=ADVERBIAL]': ' CS',
        '[SUBCAT=COMPARATIVE]': ' Comp',
        '[SUBCAT=POSTPOSITION]': ' Po',
        '[SUBCAT=PREPOSITION]': ' Pr',
        '[SUBCAT=PREFIX]': '',
        '[SUBCAT=SUFFIX]': '',
        '[SUBCAT=ABBREVIATION]': ' Abbr',
        '[SUBCAT=ACRONYM]': ' Abbr',
        '[SUBCAT=PUNCTUATION]': ' Punct',
        '[SUBCAT=SYMBOL]': '',
        '[SUBCAT=SPACE]': '',
        '[SUBCAT=QUOTATION]': '',
        '[SUBCAT=BRACKET]': '',
        '[SUBCAT=DASH]': '',
        '[SUBCAT=CURRENCY]': '',
        '[SUBCAT=MATH]': '',
        '[SUBCAT=OPERATION]': '',
        '[SUBCAT=RELATION]': '',
        '[SUBCAT=INITIAL]': '',
        '[SUBCAT=FINAL]': '',
        '[CASE=NOMINATIVE]': ' Nom',
        '[CASE=PARTITIVE]': ' Par',
        '[CASE=GENITIVE]': ' Gen',
        '[CASE=INESSIVE]': ' Ine',
        '[CASE=ELATIVE]': ' Ela',
        '[CASE=ILLATIVE]': ' Ill',
        '[CASE=ADESSIVE]': ' Ade',
        '[CASE=ABLATIVE]': ' Abl',
        '[CASE=ALLATIVE]': ' All',
        '[CASE=ESSIVE]': ' Ess',
        '[CASE=INSTRUCTIVE]': ' Ins',
        '[CASE=ABESSIVE]': ' Abe',
        '[CASE=TRANSLATIVE]': ' Tra',
        '[CASE=COMITATIVE]': ' Com',
        '[CASE=LATIVE]': ' Lat',
        '[CASE=ACCUSATIVE]': ' Acc',
        '[NUMBER=SINGULAR]': ' Sg',
        '[NUMBER=PLURAL]': ' Pl',
        '[POSSESSIVE=1STSINGULAR]': ' PxSg1',
        '[POSSESSIVE=2NDSINGULAR]': ' PxSg2',
        '[POSSESSIVE=3RDSINGULAR]': ' PxSg3',
        '[POSSESSIVE=1STPLURAL]': ' PxPl1',
        '[POSSESSIVE=2NDPLURAL]': ' PxPl2',
        '[POSSESSIVE=3RDPLURAL]': ' PxPl3',
        '[POSSESSIVE=3RDAMBIGUOUS]': ' Px3',
        '[BOUNDARY=COMPOUND]': '#',
        '[COMPOUND_FORM=S]': '',
        '[COMPOUND_FORM=OMIT]': ' TrunCo', 
        '[TENSEMOOD=PRESENTINDICATIVE]': ' Prt',
        '[TENSEMOOD=PASTINDICATIVE]': ' Pst',
        '[TENSEMOOD=CONDITIONAL]': ' Cond',
        '[TENSEMOOD=POTENTIAL]': ' Pot',
        '[TENSEMOOD=IMPERATIVE]': ' Imp',
        '[TENSEMOOD=OPTATIVE]': ' Opt',
        '[TENSEMOOD=EVENTIVE]': '',
        '[PERSON=1STSINGULAR]': ' Sg1',
        '[PERSON=2NDSINGULAR]': ' Sg2',
        '[PERSON=3RDSINGULAR]': ' Sg3',
        '[PERSON=1STPLURAL]': ' Pl1',
        '[PERSON=2NDPLURAL]': ' Pl2',
        '[PERSON=3RDPLURAL]': ' Pl3',
        '[PERSON=IMPERSONAL]': ' Pe4',
        '[NEGATION=CON]': ' ConNeg',
        '[SUBCAT=NEGATIONVERB]': ' Neg',
        '[VOICE=ACTIVE]': ' Act',
        '[VOICE=PASSIVE]': ' Pass',
        '[INFINITIVE=A]': ' Inf1',
        '[INFINITIVE=E]': ' Inf2',
        '[INFINITIVE=MA]': ' Inf3',
        '[DERIVATION=MINEN]': ' Inf4',
        '[DERIVATION=MAISILLA]': ' Inf5',
        '[PARTICIPLE=NUT]': ' PrfPrc',
        '[PARTICIPLE=AGENT]': ' AgPrc',
        '[PARTICIPLE=VA]': ' PrtPrc',
        '[PARTICIPLE=NEGATION]': 'NegPrc',
        '[DERIVATION=NUT]': '',
        '[DERIVATION=TU]': '',
        '[DERIVATION=MA]': '',
        '[DERIVATION=VA]': '',
        '[DERIVATION=MATON]': '',
        '[COMPARISON=POSITIVE]': ' Pos',
        '[COMPARISON=COMPARATIVE]': ' Comp',
        '[COMPARISON=SUPERLATIVE]': ' Super',
        '[DERIVATION=MPI]': '',
        '[DERIVATION=IN]': '', 
        '[CLITIC=HAN]': ' Foc_hAn',
        '[CLITIC=KAAN]': ' Foc_kAAn',
        '[CLITIC=KIN]': ' Foc_kin',
        '[CLITIC=KO]': ' Foc_kO',
        '[CLITIC=PA]': ' Foc_pA',
        '[CLITIC=S]': ' Foc_s',
        '[CLITIC=KA]': ' Foc_kA',
        '[DERIVATION=STI]': ' Man', 
        '[DERIVATION=JA]': '',
        '[DERIVATION=INEN]': '', 
        '[DERIVATION=LAINEN]': '',
        '[DERIVATION=TAR]': '',
        '[DERIVATION=LLINEN]': '',
        '[DERIVATION=TON]': '',
        '[DERIVATION=TSE]': '',
        '[DERIVATION=OI]':'',
        '[DERIVATION=VS]': '',
        '[DERIVATION=U]': '',
        '[DERIVATION=TTAIN]': '',
        '[DERIVATION=TTAA]': '',
        '[DERIVATION=TATTAA]': '',
        '[DERIVATION=TATUTTAA]': '',
        '[DERIVATION=UUS]': '',
        '[DERIVATION=S]': '',
        '[DERIVATION=NUT]': '',
        '[STYLE=NONSTANDARD]': '',
        '[STYLE=RARE]': '',
        '[STYLE=DIALECTAL]': '',
        '[STYLE=ARCHAIC]': '',
        '[GUESS=COMPOUND]': '',
        '[GUESS=DERIVE]': '',
        '[ALLO=A]': '',
        '[ALLO=TA]': '',
        '[ALLO=HVN]': '',
        '[ALLO=IA]': '',
        '[ALLO=IDEN]': '',
        '[ALLO=ITA]': '',
        '[ALLO=ITTEN]': '',
        '[ALLO=IEN]': '',
        '[ALLO=IHIN]': '',
        '[ALLO=IIN]': '',
        '[ALLO=IN]': '',
        '[ALLO=ISIIN]': '',
        '[ALLO=IDEN]': '',
        '[ALLO=JA]': '',
        '[ALLO=JEN]': '',
        '[ALLO=SEEN]': '',
        '[ALLO=TEN]': '',
        '[ALLO=VN]': '',
        '[FILTER=NO_PROC]': '',
        '[PROP=FIRST]': '',
        '[PROP=GEO]': '',
        '[PROP=LAST]': '',
        '[PROP=MISC]': '',
        '[PROP=ORG]': '',
        '[PROP=PRODUCT]': '',
        '[PROP=EVENT]': '',
        '[PROP=MEDIA]': '',
        '[PROP=CULTGRP]': '',
        '[PROP=ARTWORK]': '',
        '[SEM=TITLE]': '',
        '[SEM=ORG]': '',
        '[SEM=EVENT]': '',
        '[SEM=POLIT]': '',
        '[SEM=MEDIA]': '',
        '[SEM=GEO]': '',
        '[SEM=MEASURE]': '',
        '[SEM=CURRENCY]': '',
        '[SEM=TIME]': ''}

omor2ftc = {
        '[WORD_ID=': '',
        '[SUBCAT=ADJECTIVE]': ' Adjective',
        '[POS=VERB]': ' Verb',
        '[POS=NOUN]': ' Noun',
        '[POS=PARTICLE]': '',
        '[SUBCAT=PRONOUN]': ' Pronoun',
        '[SUBCAT=NUMERAL]': ' Numeral',
        '[SUBCAT=PROPER]': ' Proper',
        '[SUBCAT=ADVERB]': ' Adverb',
        '[SUBCAT=ADPOSITION]': ' Preposition',
        '[SUBCAT=QUALIFIER]': ' Adjective',
        '[SUBCAT=INTERJECTION]': ' Interjection',
        '[SUBCAT=DEMONSTRATIVE]': ' Dem',
        '[SUBCAT=PERSONAL]': ' Pers',
        '[SUBCAT=INTERROGATIVE]': ' Interr',
        '[SUBCAT=RELATIVE]': ' Rel',
        '[SUBCAT=QUANTOR]': ' Qu',
        '[SUBCAT=REFLEXIVE]': ' Reflex',
        '[SUBCAT=RECIPROCAL]': ' Rec',
        '[SUBCAT=INDEFINITE]': ' Ind',
        '[SUBCAT=CARDINAL]': '',
        '[SUBCAT=ORDINAL]': ' Ord',
        '[SUBCAT=CONJUNCTION]': ' Conjunction',
        '[SUBCAT=COORDINATING]': ' CC',
        '[SUBCAT=ADVERBIAL]': ' CS',
        '[SUBCAT=COMPARATIVE]': ' Comp',
        '[SUBCAT=POSTPOSITION]': ' Po',
        '[SUBCAT=PREPOSITION]': ' Pr',
        '[SUBCAT=PREFIX]': '',
        '[SUBCAT=SUFFIX]': '',
        '[SUBCAT=ABBREVIATION]': ' Abbrev',
        '[SUBCAT=ACRONYM]': ' Abbrev',
        '[SUBCAT=PUNCTUATION]': ' Delimiter',
        '[SUBCAT=SYMBOL]': '',
        '[SUBCAT=SPACE]': '',
        '[SUBCAT=QUOTATION]': '',
        '[SUBCAT=BRACKET]': '',
        '[SUBCAT=DASH]': '',
        '[SUBCAT=CURRENCY]': '',
        '[SUBCAT=MATH]': '',
        '[SUBCAT=OPERATION]': '',
        '[SUBCAT=RELATION]': '',
        '[SUBCAT=INITIAL]': '',
        '[SUBCAT=FINAL]': '',
        '[CASE=NOMINATIVE]': ' Nom',
        '[CASE=PARTITIVE]': ' Part',
        '[CASE=GENITIVE]': ' Gen',
        '[CASE=INESSIVE]': ' In',
        '[CASE=ELATIVE]': ' El',
        '[CASE=ILLATIVE]': ' Ill',
        '[CASE=ADESSIVE]': ' Ad',
        '[CASE=ABLATIVE]': ' Abl',
        '[CASE=ALLATIVE]': ' All',
        '[CASE=ESSIVE]': ' Ess',
        '[CASE=INSTRUCTIVE]': ' Instr',
        '[CASE=ABESSIVE]': ' Ab',
        '[CASE=TRANSLATIVE]': ' Transl',
        '[CASE=COMITATIVE]': ' Com',
        '[CASE=LATIVE]': ' Lat',
        '[CASE=ACCUSATIVE]': ' Acc',
        '[NUMBER=SINGULAR]': ' SG',
        '[NUMBER=PLURAL]': ' PL',
        '[POSSESSIVE=1STSINGULAR]': ' S 1P',
        '[POSSESSIVE=2NDSINGULAR]': ' S 2P',
        '[POSSESSIVE=3RDSINGULAR]': ' 3P',
        '[POSSESSIVE=1STPLURAL]': ' P 1P',
        '[POSSESSIVE=2NDPLURAL]': ' P 2P',
        '[POSSESSIVE=3RDPLURAL]': ' 3P',
        '[POSSESSIVE=3RDAMBIGUOUS]': ' 3P',
        '[BOUNDARY=COMPOUND]': '',
        '[COMPOUND_FORM=S]': '',
        '[COMPOUND_FORM=OMIT]': '', 
        '[TENSEMOOD=PRESENTINDICATIVE]': ' Ind',
        '[TENSEMOOD=PASTINDICATIVE]': ' Ind',
        '[TENSEMOOD=CONDITIONAL]': ' Cond',
        '[TENSEMOOD=POTENTIAL]': ' Pot',
        '[TENSEMOOD=IMPERATIVE]': ' Imper',
        '[TENSEMOOD=OPTATIVE]': '',
        '[TENSEMOOD=EVENTIVE]': '',
        '[PERSON=1STSINGULAR]': ' S 1P',
        '[PERSON=2NDSINGULAR]': ' S 2P',
        '[PERSON=3RDSINGULAR]': ' S 3P',
        '[PERSON=1STPLURAL]': ' P 1P',
        '[PERSON=2NDPLURAL]': ' P 2P',
        '[PERSON=3RDPLURAL]': ' P 3P',
        '[PERSON=IMPERSONAL]': '',
        '[NEGATION=CON]': '',
        '[SUBCAT=NEGATIONVERB]': '',
        '[VOICE=ACTIVE]': ' Act',
        '[VOICE=PASSIVE]': ' Pass',
        '[INFINITIVE=A]': ' Iinf',
        '[INFINITIVE=E]': ' IIinf',
        '[INFINITIVE=MA]': ' IIIinf',
        '[DERIVATION=MINEN]': ' Inf4',
        '[DERIVATION=MAISILLA]': ' Inf5',
        '[PARTICIPLE=NUT]': ' IIpartic',
        '[PARTICIPLE=AGENT]': '',
        '[PARTICIPLE=VA]': ' Ipartic',
        '[PARTICIPLE=NEGATION]': '',
        '[DERIVATION=NUT]': '',
        '[DERIVATION=TU]': '',
        '[DERIVATION=MA]': '',
        '[DERIVATION=VA]': '',
        '[DERIVATION=MATON]': '',
        '[COMPARISON=POSITIVE]': '',
        '[COMPARISON=COMPARATIVE]': ' Comp',
        '[COMPARISON=SUPERLATIVE]': ' Sup',
        '[DERIVATION=MPI]': '',
        '[DERIVATION=IN]': '', 
        '[CLITIC=HAN]': '',
        '[CLITIC=KAAN]': '',
        '[CLITIC=KIN]': '',
        '[CLITIC=KO]':  '',
        '[CLITIC=PA]': '',
        '[CLITIC=S]': '',
        '[CLITIC=KA]': '',
        '[DERIVATION=STI]': '', 
        '[DERIVATION=JA]': '',
        '[DERIVATION=INEN]': '', 
        '[DERIVATION=LAINEN]': '',
        '[DERIVATION=TAR]': '',
        '[DERIVATION=LLINEN]': '',
        '[DERIVATION=TON]': '',
        '[DERIVATION=TSE]': '',
        '[DERIVATION=OI]':'',
        '[DERIVATION=VS]': '',
        '[DERIVATION=U]': '',
        '[DERIVATION=TTAIN]': '',
        '[DERIVATION=TTAA]': '',
        '[DERIVATION=TATTAA]': '',
        '[DERIVATION=TATUTTAA]': '',
        '[DERIVATION=UUS]': '',
        '[DERIVATION=S]': '',
        '[DERIVATION=NUT]': '',
        '[STYLE=NONSTANDARD]': '',
        '[STYLE=RARE]': '',
        '[STYLE=DIALECTAL]': '',
        '[STYLE=ARCHAIC]': '',
        '[GUESS=COMPOUND]': '',
        '[GUESS=DERIVE]': '',
        '[ALLO=A]': '',
        '[ALLO=TA]': '',
        '[ALLO=HVN]': '',
        '[ALLO=IA]': '',
        '[ALLO=IDEN]': '',
        '[ALLO=ITA]': '',
        '[ALLO=ITTEN]': '',
        '[ALLO=IEN]': '',
        '[ALLO=IHIN]': '',
        '[ALLO=IIN]': '',
        '[ALLO=IN]': '',
        '[ALLO=ISIIN]': '',
        '[ALLO=IDEN]': '',
        '[ALLO=JA]': '',
        '[ALLO=JEN]': '',
        '[ALLO=SEEN]': '',
        '[ALLO=TEN]': '',
        '[ALLO=VN]': '',
        '[FILTER=NO_PROC]': '',
        '[PROP=FIRST]': '',
        '[PROP=GEO]': '',
        '[PROP=LAST]': '',
        '[PROP=MISC]': '',
        '[PROP=ORG]': '',
        '[PROP=PRODUCT]': '',
        '[PROP=EVENT]': '',
        '[PROP=MEDIA]': '',
        '[PROP=CULTGRP]': '',
        '[PROP=ARTWORK]': '',
        '[SEM=TITLE]': '',
        '[SEM=ORG]': '',
        '[SEM=EVENT]': '',
        '[SEM=POLIT]': '',
        '[SEM=MEDIA]': '',
        '[SEM=GEO]': '',
        '[SEM=MEASURE]': '',
        '[SEM=CURRENCY]': '',
        '[SEM=TIME]': ''}


def convert_omor_tag(tag, fmt):
    """Convert single omor style tag in to target format
    """
    if fmt == 'omor':
        return tag
    elif fmt == 'ftc':
        if tag in omor2ftc:
            return omor2ftc[tag]
        elif tag.startswith('[WORD_ID='):
            return tag[len('[WORD_ID='):-1]
        elif tag.startswith('[WEIGHT='):
            return '\t' + tag[len('[WEIGHT='):-1]
        return _omor2ftc(tag)
    elif fmt == 'ftb3':
        if tag in omor2ftb3:
            return omor2ftb3[tag]
        elif tag.startswith('[WORD_ID='):
            return tag[len('[WORD_ID='):-1]
        elif tag.startswith('[WEIGHT='):
            return '\t' + tag[len('[WEIGHT='):-1]
        else:
            return ' Unkwn Tag ' + tag
    else:
        return '?' + fmt + '?:' + tag

def convert_omor_string(omorstring, fmt):
    """Convert from full omor analysis string to analysis string of other system

    This function uses convert_omor_tag(tag, fmt) repeatedly for each bracketed
    omor field, and additionally reorganises and combines results until it can
    be matched to the target analysis style.
    """
    if fmt == 'ftc':
        return _omor2ftc(omorstring)
    else:
        omors = omorstring.split('][')
        conv = convert_omor_tag(omors[0] + ']')
        for omor in omors[1:-1]:
            conv += convert_omor_tag('[' + omor + ']', fmt)
        conv += convert_omor_tag('[' + omors[-1])

def _omor2ftc(omorstring):
    """
    Convert omorfi's data to something that is comparable to FTC data. 

    This removes a lot of useful data from the analyses. Avoid using this
    function and Finnish Text Collection altogether, because of its low quality
    and confusingly un-free licencing policy.
    
    Example:

    >>> s = '[WORD_ID=talo][NUMBER=SINGULAR][CASE=INESSIVE]'
    >>> omor2ftc(s)
    ... 'talo In SG'

    """
    anals = dict()
    ftc = ''
    omors = omorstring.split("][")
    for omor in omors:
        kv = omor.split("=")
        k = kv[0].lstrip("[")
        v = kv[1].rstrip("]")
        if k in anals:
            anals[k] = anals[k] + [v]
        else:
            anals[k] = [v]
    # WORD ID comes first as lemma
    for w in anals['WORD_ID']:
        ftc += w
    # word Case NUM P POSS
    if 'CASE' in anals:
        ftc += convert_omor_tag(anals['CASE'][-1], 'ftc')
    if 'NUMBER' in anals:
        ftc += convert_omor_tag(anals['NUM'][-1], 'ftc')
    # Verb is Tense Genus Mood P PERS
    # Note always Tense
    if 'TENSEMOOD' in anals:
        if anals['TENSEMOOD'][-1] == 'PASTINDICATIVE':
            ftc += ' Imp'
        else:
            ftc += ' Pr'
    if 'VOICE' in anals:
        ftc += convert_omor_tag(anals['VOICE'][-1], 'ftc')
    if 'TENSEMOOD' in anals:
        ftc += convert_omor_tag(anals['TENSEMOOD'][-1], 'ftc')
    if 'PERSON' in anals:
        ftc += convert_omor_tag(anals['PERSON'][-1])
    if 'POSS' in anals:
        possfrom = [["SG1", "S 1P"], ["SG2", "S 2P"], ["SG3", "3P"], ["PL1", "P 1P"], ["PL2", "P 2P"], ["PL3", "3P"]]
        poss = anals['POSS'][-1].upper()
        for c in possfrom:
            poss = poss.replace(c[0], c[1])
        ftc += ' ' + poss
    if ftc == ':':
        ftc = '_COLON'
    elif ftc == ',':
        ftc = '_COMMA'
    elif ftc == '.':
        ftc = '_PERIOD'
    elif ftc == '(':
        ftc = '_LEFTPARENTH'
    elif ftc == '-':
        ftc = '_HYPHEN'
    elif ftc == ')':
        ftc = '_RIGHTPARENTH'
    elif ftc == '?':
        ftc = '_QUESTION'
    elif ftc == '+':
        ftc = '_PLUS'
    elif ftc == '/':
        ftc = '_SLASH'
    elif ftc == '!':
        ftc = '_EXCLAMATION'
    elif ftc == '*':
        ftc = '_ASTERISK'
    elif ftc == ';':
        ftc = '_SEMICOLON'
    elif ftc == '%':
        ftc = '_RIGHTP'
    elif ftc == '...':
        ftc = '_THREEPOINTS'
    return ftc


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
    if fail:
        exit(1)

