#!/usr/bin/env python3
#
# utils to format lexc strings from omor's lexical data sources.

from sys import stderr
from lexc_string_utils import lexc_escape

def format_lexc(wordmap, format):
    if format in ["omor", "ktnkav"]:
        return format_lexc_omor(wordmap, format)
    elif format == "apertium":
        return format_lexc_apertium(wordmap)

def format_lexc_omor(wordmap, format):
    '''
    format string for canonical omor format for morphological analysis
    '''
    tn = int(wordmap['kotus_tn'])
    wordmap['analysis'] = "[WORD_ID=%s]" %(lexc_escape(wordmap['lemma']))
    if wordmap['is_suffix']:
        wordmap['analysis'] += "[POS=%(pos)s][SUBCAT=SUFFIX]" %(wordmap)
    elif wordmap['is_prefix']:
        wordmap['analysis'] += "[POS=NOUN][SUBCAT=PREFIX]" %(wordmap)
    elif wordmap['pos'] == 'ACRONYM':
        wordmap['analysis'] += "[POS=NOUN][SUBCAT=%(pos)s]" %(wordmap)
    else:
        wordmap['analysis'] += "[POS=%(pos)s]" %(wordmap)

    if wordmap['subcat']:
        wordmap['analysis'] += "[SUBCAT=%(subcat)s]" %(wordmap)
    
    if wordmap['particle']:
        pclasses = wordmap['particle'].split('|')
        for pclass in pclasses:
            wordmap['analysis'] += "[SUBCAT=%s]" %(pclass)

    if wordmap['is_proper']:
        wordmap['analysis'] += "[SUBCAT=PROPER]"
        if wordmap['proper_noun_class']:
            for prop in wordmap['proper_noun_class'].split(','):
                wordmap['analysis'] += '[PROP=%s]' %(prop)

    if wordmap['sem']:
        for sem in wordmap['sem'].split(','):
            wordmap['analysis'] += '[SEM=%s]' %(sem)

    if format == 'ktnkav' and tn < 99:
        wordmap['analysis'] += "[KTN=%(kotus_tn)s]" %(wordmap)
        if wordmap['kotus_av']:
            wordmap['analysis'] += "[KAV=%(kotus_av)s]" %(wordmap)
    elif format == 'newparas':
        wordmap['analysis'] += "[PARA=%(new_para)s]" %(wordmap)
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    # match WORD_ID= with epsilon, then stub and lemma might match
    wordmap['stub'] = '0' + wordmap['stub'] 
    retvals = []
    for new_para in wordmap['new_paras']:
        retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], wordmap['stub'], 
                new_para)]
    return "\n".join(retvals)

def format_lexc_apertium(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['lemma'])
    wordmap['analysis'] = wordmap['analysis'].replace('#', '+')
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
        multichars += """!! Lexical class: word entry id
[WORD_ID=
!! Lexical class: morphological POS
[POS=ADJECTIVE] [POS=VERB] [POS=NOUN] [POS=PARTICLE]
[POS=PRONOUN] [POS=NUMERAL]
!! Lexical classes: Misc.
[SUBCAT=PROPER]
[SUBCAT=DEMONSTR] [SUBCAT=PERSONAL] [SUBCAT=INTERROG]
[SUBCAT=RELATIVE] [SUBCAT=QUANTOR] [SUBCAT=REFLEX]
[SUBCAT=RECIPROC] [SUBCAT=INDEF]
[SUBCAT=CARD] [SUBCAT=ORD]
[SUBCAT=CONJUNCTION]
[SUBCAT=COORD] [SUBCAT=ADVERBIAL] [SUBCAT=COMPARATIVE]
[SUBCAT=POSTPOSITION] [SUBCAT=PREPOSITION]
[SUBCAT=PREFIX]
[SUBCAT=SUFFIX]
[SUBCAT=ABBREVIATION]
[SUBCAT=ACRONYM]
[SUBCAT=PUNCTUATION] [SUBCAT=SYMBOL]
[SUBCAT=SPACE] [SUBCAT=QUOTATION] [SUBCAT=BRACKET] [SUBCAT=DASH]
[SUBCAT=CURRENCY] [SUBCAT=MATH]
[SUBCAT=OPERATION] [SUBCAT=RELATION]
[SUBCAT=INITIAL] [SUBCAT=FINAL]
!! Lexical classes: Proper noun's semantics
[PROP=FIRST] [PROP=GEO] [PROP=LAST] [PROP=MISC] [PROP=ORG]
[PROP=PRODUCT] [PROP=EVENT] [PROP=MEDIA] [PROP=BAND] [PROP=ARTWORK]
!! Lexical classes: semantics
[SEM=TITLE] [SEM=ORG] [SEM=EVENT] [SEM=POLIT] [SEM=MEDIA]
[SEM=GEO] [SEM=MEASURE] [SEM=CURRENCY] [SEM=TIME]
!! Inflectional endings
[CASE=NOM] [CASE=PAR]            [CASE=GEN]
[CASE=INE] [CASE=ELA] [CASE=ILL] [CASE=ADE]
[CASE=ABL] [CASE=ALL] [CASE=ESS] [CASE=INS]
[CASE=ABE] [CASE=TRA] [CASE=CMT] 
[CASE=LAT]
[CASE=ACC]

[NUM=SG] [NUM=PL]
[POSS=SG1] [POSS=SG2] [POSS=SG3] [POSS=PL1] [POSS=PL2] [POSS=PL3] [POSS=SG3,PL3]
[COMPOUND_FORM=S]
[COMPOUND_FORM=OMIT]
[TENSE=PRES] [TENSE=PAST]
[MOOD=INDV] [MOOD=COND] [MOOD=POTN] [MOOD=IMPV]
[MOOD=OPTV] [MOOD=EVNV]

[PRS=SG1] [PRS=SG2] [PRS=SG3] [PRS=PL1] [PRS=PL2] [PRS=PL3]
[PRS=PE4]

[NEG=CON] 
[SUBCAT=NEG]
[VOICE=ACT] [VOICE=PSS]

[INF=A] [INF=E] [INF=MA] [DRV=MINEN] [DRV=MAISILLA]

[PCP=NUT] [PCP=MA] [PCP=VA] [PCP=NEG]

[CMP=POS] [CMP=CMP] [CMP=SUP]

[CLIT=HAN] [CLIT=KAAN] [CLIT=KIN] [CLIT=KO] [CLIT=PA]
[CLIT=S] [CLIT=KA]
!! Derivations
[DRV=STI] [DRV=JA] [DRV=INEN] [DRV=LAINEN] [DRV=TAR]
[DRV=LLINEN] [DRV=TON] [DRV=TSE] [DRV=OI] [DRV=VS] [DRV=U]
[DRV=TTAIN]
[DRV=TTAA] [DRV=TATTAA] [DRV=TATUTTAA]
[DRV=UUS]
!! Usage limitations
[STYLE=NONSTANDARD] [STYLE=RARE] [STYLE=DIALECTAL]
[STYLE=ARCHAIC]

!! Guessing
[GUESS=COMPOUND] [GUESS=DERIVE]
!! Allomorphs
[ALLO=A] [ALLO=TA] [ALLO=HVN] [ALLO=IA] [ALLO=IDEN] [ALLO=ITA] [ALLO=ITTEN]
[ALLO=IEN] [ALLO=IHIN] [ALLO=IIN] [ALLO=IN] [ALLO=ISIIN] [ALLO=IDEN]
[ALLO=JA] [ALLO=JEN] [ALLO=SEEN] [ALLO=TEN] [ALLO=VN]
!! Software limitations
[FILTER=NO_PROC]

!! Some boundaries
{##} {#} {_} {-}

"""
    if format == 'ktnkav':
        multichars += """!! Morphological classes from dictionary
[KTN=1] [KTN=2] [KTN=3] [KTN=4] [KTN=5]
[KTN=6] [KTN=7] [KTN=8] [KTN=9] [KTN=10]
[KTN=11] [KTN=12] [KTN=13] [KTN=14] [KTN=15]
[KTN=16] [KTN=17] [KTN=18] [KTN=19] [KTN=20]
[KTN=21] [KTN=22] [KTN=23] [KTN=24] [KTN=25]
[KTN=26] [KTN=27] [KTN=28] [KTN=29] [KTN=30]
[KTN=31] [KTN=32] [KTN=33] [KTN=34] [KTN=35]
[KTN=36] [KTN=37] [KTN=38] [KTN=39] [KTN=40]
[KTN=41] [KTN=42] [KTN=43] [KTN=44] [KTN=45]
[KTN=46] [KTN=47] [KTN=48] [KTN=49] [KTN=50]
[KTN=51] [KTN=52] [KTN=53] [KTN=54] [KTN=55]
[KTN=56] [KTN=57] [KTN=58] [KTN=59] [KTN=60]
[KTN=61] [KTN=62] [KTN=63] [KTN=64] [KTN=65]
[KTN=66] [KTN=67] [KTN=68] [KTN=69] [KTN=70]
[KTN=71] [KTN=72] [KTN=73] [KTN=74] [KTN=75]
[KTN=76] [KTN=77] [KTN=78]
[KAV=A] [KAV=B] [KAV=C] [KAV=D] [KAV=E]
[KAV=F] [KAV=G] [KAV=H] [KAV=I] [KAV=J]
[KAV=K] [KAV=L] [KAV=M]
[KAV=N] [KAV=O] [KAV=P] [KAV=T]
        """
    if format == 'newparas':
        multichars += """!! Morphological classes from omorfi
[NEWPARA=
        """
    return multichars

def format_root_lexicon(format):
    root = "LEXICON Root\n"
    root += """!! ...
0   NOMINAL ;
0   DIGITS ;
0   ACRONYM ;
0   PREFIX  ;
0   PRON    ;
0   PARTICLE    ;
0   PUNCTUATION ;
0   NUM ;
0   VERB    ;
[COMPOUND_FORM=OMIT]-:0-    SUFFIX  ;
    """
    return root

def format_xml_kotus_sanalista(wordmap):
    if wordmap['kotus_av']:
        return ("<st><s>%(lemma)s</s><t><tn>%(kotus_tn)s</tn><av>%(kotus_av)s</av></t></st>" %(wordmap))
    else:
        return ("<st><s>%(lemma)s</s><t><tn>%(kotus_tn)s</tn></t></st>" %(wordmap))
