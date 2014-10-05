#!/usr/bin/env python3
#
# utils to format apertium style data from omorfi database values

from omor_strings_io import lexc_escape, word_boundary, weak_boundary, \
        optional_hyphen, fail_formatting_missing_for

monodix_sdefs= {
        'abbr',
        'abe',
        'abl',
        'acc',
        'actv',
        'ade',
        'adj',
        'agent',
        'all',
        'ant',
        'card',
        'cmp',
        'cnjcoo',
        'cnjsub',
        'com' ,
        'comp',
        'cond',
        'conneg' ,
        'dem',
        'ela',
        'enc',
        'ess',
        'f',
        'gen',
        'ij',
        'ill',
        'imp',
        'impers',
        'ind',
        'indv',
        'ine',
        'infa',
        'infe',
        'infma',
        'infminen',
        'ins',
        'itg',
        'lat',
        'm',
        'mf',
        'n',
        'neg',
        'nom',
        'np',
        'nt',
        'num',
        'ord',
        'p1',
        'p2',
        'p3',
        'par',
        'part',
        'past',
        'pasv',
        'pl',
        'pneg',
        'pos',
        'post',
        'pot',
        'pp',
        'pprs',
        'pr',
        'pres',
        'prn',
        'pxpl1',
        'pxpl2',
        'pxsg1',
        'pxsg2',
        'pxsp3',
        'qst',
        'rec',
        'reflex',
        'rel',
        'sg',
        'sup',
        'top',
        'tra',
        'vblex',
        'ND'}

apertium_multichars =  {
 "-",
 "",
 "+",
 "adj",
 "abbr",
 "abe",
 "abl",
 "acc",
 "actv",
 "ade",
 "adv",
 "agent",
 "all",
 "ant",
 "card",
 "cnjcoo",
 "cnjcoo><vblex",
 "cnjsub",
 "cnjadv",
 "com",
 "cond",
 "conneg",
 "def",
 "dem",
 "ela",
 "enc",
 "ess",
 "f",
 "gen",
 "guio",
 "ij",
 "ill", 
 "imp", 
 "impers", 
 "ind",
 "ine",
 "infa",
 "infe",
 "infma",
 "infminen",
 "ins",
 "itg",
 "lat",
 "lpar",
 "lquot",
 "m",
 "mf",
 "n",
 "ND",
 "neg", 
 "nom",
 "np",
 "num",
 "ord",
 "p1", 
 "p2",
 "p3",
 "p1><pl", 
 "p1><sg", 
 "p2><pl",
 "p2><sg",
 "p3><pl",
 "p3><sg",
 "par", 
 "part",
 "past",
 "pasv",
 "pers",
 "pl", 
 "pneg",
 "pos",
 "post",
 "pot", 
 "pp",
 "pprs",
 "pri",
 "prn",
 "pxpl1",
 "pxpl2",
 "pxsg1",
 "pxsg2",
 "pxsp3",
 "qst",
 "qu",
 "rec",
 "reflex",
 "rel",
 "rpar",
 "rquot",
 "sent",
 "sg", 
 "sup",
 "top",
 "tra", 
 "vaux",
 "vblex",
 "v→a",
 "v→adv",
 "v→n"
        }
stuff2monodix =  {
        "ABBREVIATION": "abbr",
        "ACRONYM": "abbr",
        "ADJECTIVE": "adj",
        "ADPOSITION": "post",
        "ADVERB": "adv",
        "ADVERBIAL": "cnjadv",
        "AINF_arg": "vaux",
        "ARTWORK": "",
        "B-": "-",
        "B←": "-",
        "B→": "-",
        "Bc": "+",
        "CARDINAL": "card",
        "Ccmp": "com",
        "CLAUSE-BOUNDARY": "",
        "Cma": "agent",
        "Cmaton": "pneg",
        "Cnut": "pp",
        "COMPARATIVE": "cnjsub",
        "COMP": "com",
        "CONJUNCTION": "",
        "CONJUNCTIONVERB": "cnjcoo><vblex",
        "COORDINATING": "cnjcoo",
        "Cpos": "pos",
        "Csup": "sup",
        "CULTGRP": "",
        "Cva": "pprs",
        "DASH": "guio",
        "DECIMAL": "",
        "DEMONSTRATIVE": "dem",
        "DIGIT": "",
        "Din": "v→n", "Ds": "", "Du": "", "Dtava": "v→a",
        "Dma": "v→a", "Dinen": "", "Dja": "v→n", "Dmpi": "",
        "Dmaisilla": "v→adv",
        "Dminen": "v→n",
        "Dnut": "v→a", "Dtu": "v→a", "Duus": "", "Dva": "v→a", "Dmaton": "v→a",
        "Dttaa": "", "Dtattaa": "", "Dtatuttaa": "",
        "EVENT": "",
        "FINAL-BRACKET": "rpar",
        "FINAL-QUOTE": "rquot",
        "FIRST": "ant",
        "GEO": "top",
        "Ia": "infa",
        "Ie": "infe",
        "Ima": "infma",
        "Iminen": "infminen",
        "INDEFINITE": "ind",
        "INITIAL-BRACKET": "lpar",
        "INITIAL-QUOTE": "lquot",
        "INTRANSITIVE_arg": "vblex",
        "INTERJECTION": "ij",
        "INTERROGATIVE": "itg",
        "LAST": "ant",
        "LEMMA-START": "",
        "MAINF_arg": "vaux",
        "MEDIA": "",
        "MISC": "",
        "Ncon": "conneg",
        "N??": "ND",
        "Nneg": "neg", 
        "NOUN": "n",
        "Npl": "pl", 
        "Nsg": "sg", 
        "NUMERAL": "num",
        "O3": "pxsp3",
        "Opl1": "pxpl1",
        "Opl2": "pxpl2",
        "ORDINAL": "ord",
        "ORG": "",
        "Osg1": "pxsg1",
        "Osg2": "pxsg2",
        "PARTICLE": "part",
        "PERSONAL": "pers",
        "PL1": "p1", 
        "PL2": "p2",
        "PL3": "p3",
        "Ppe4": "impers", 
        "Ppl1": "p1><pl", 
        "Ppl2": "p2><pl",
        "Ppl3": "p3><pl",
        "PRONOUN": "prn",
        "PRODUCT": "",
        "PROPER": "np",
        "Psg1": "p1><sg", 
        "Psg2": "p2><sg",
        "Psg3": "p3><sg",
        "PUNCTUATION": "",
        "Qhan": "+han<enc",
        "Qkaan": "+kaan<enc",
        "Qka": "+ka<enc",
        "Qkin": "+kin<enc",
        "Qko": "+ko<qst",
        "Qpa": "+pa<enc",
        "Qs": "+s<enc",
        "QUALIFIER": "adj",
        "QUANTOR": "qu",
        "RECIPROCAL": "rec",
        "REFLEXIVE": "reflex",
        "RELATIVE": "rel",
        "ROMAN": "",
        ".sent": "",
        "SG1": "p1", 
        "SG2": "p2",
        "SG3": "p3",
        "SENTENCE-BOUNDARY": "sent",
        "SPACE": "",
        "SUPERL": "sup",
        "Tcond": "cond",
        "Timp": "imp", 
        "Topt": "",
        "Tpast": "past",
        "Tpot": "pot", 
        "Tpres": "pri",
        "Uarch": "",
        "Udial": "",
        "Unonstd": "",
        "UNSPECIFIED": "part",
        "Urare": "",
        "Vact": "actv",
        "VERB": "vblex",
        "Vpss": "pasv",
        "X???": "",
        "Xabe": "abe",
        "Xabl": "abl",
        "Xacc": "acc",
        "Xade": "ade",
        "Xall": "all",
        "Xcom": "com",
        "Xela": "ela",
        "Xess": "ess", 
        "Xgen": "gen",
        "Xill": "ill", 
        "Xine": "ine",
        "Xins": "ins",
        "Xlat": "lat",
        "Xnom": "nom",
        "Xpar": "par", 
        "Xtra": "tra", 
        "": ""
        }
stuff2apertium = stuff2monodix

def format_tag_apertium(stuff):
    if len(stuff) == 0:
        return ""
    elif stuff in stuff2monodix:
        if stuff2monodix[stuff] in ['+', '-', '#', '0', '']:
            return stuff2monodix[stuff]
        elif stuff2monodix[stuff].startswith('+'):
            return (lexc_escape(stuff2monodix[stuff]) + '%>')
        else:
            return ('%<' + lexc_escape(stuff2monodix[stuff]) + '%>')
    else:
        fail_formatting_missing_for(stuff, "apertium")
        return ""

def format_analysis_lexc_apertium(anals):
    apestring = ''
    for i in anals.split('|'):
        apestring += format_tag_apertium(i)
    return apestring

def format_continuation_lexc_apertium(anals, surf, cont):
    analstring = format_analysis_lexc_apertium(anals)
    if 'DIGITS_' in cont and not ('BACK' in cont or 'FRONT' in cont):
        analstring = lexc_escape(surf) + analstring
    surf = lexc_escape(surf)
    return "%s:%s\t%s ;\n" %(analstring, surf, cont)

def format_lexc_apertium(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['lemma'])
    wordmap['analysis'] = wordmap['analysis'].replace(word_boundary, '+').replace(weak_boundary, '')
    if wordmap['is_suffix']:
        wordmap['analysis'] = "+" + wordmap['analysis']
    elif wordmap['is_prefix']:
        wordmap['analysis'] += "+"
     
    if wordmap['pos'] == 'NOUN':
        if wordmap['is_proper']:
            wordmap['analysis'] += '%<np%>'
            for pc in wordmap['proper_noun_class'].split(','):
                wordmap['analysis'] += format_tag_apertium(pc)
        else:
            wordmap['analysis'] += '%<n%>'
    elif wordmap['pos'] == 'VERB':
        if wordmap['argument']:
            wordmap['analysis'] += format_tag_apertium(wordmap['argument'] + '_arg')
        else:
            wordmap['analysis'] += format_tag_apertium(wordmap['pos'])
    elif wordmap['pos'] == 'CONJUNCTIONVERB':
        if wordmap['lemma'] == 'eikä':
            wordmap['lemma'] = 'ei'
            wordmap['analysis'] = 'ja' + \
                    format_tag_apertium('COORDINATING') + \
                    '+ei' + \
                    format_tag_apertium('Nneg')
        else:
            wordmap['analysis'] = wordmap['lemma'][:-2] +\
                    format_tag_apertium('ADVERBIAL') + \
                    '+' + wordmap['lemma'][-2:] + \
                    format_tag_apertium('Nneg')
    elif wordmap['particle']:
        for pclass in wordmap['particle'].split('|'):
            wordmap['analysis'] += format_tag_apertium(pclass)
    else:
        wordmap['analysis'] += format_tag_apertium(wordmap['pos'])

    if wordmap['subcat']:
        for subcat in wordmap['subcat'].split('|'):
            wordmap['analysis'] += format_tag_apertium(subcat)
    if wordmap['symbol']:
        for subcat in wordmap['symbol'].split('|'):
            wordmap['analysis'] += format_tag_apertium(subcat)
    retvals = ""
    wordmap['stub'] = wordmap['stub'].replace(word_boundary, optional_hyphen)
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    for new_para in wordmap['new_paras']:
        retvals += "%s:%s\t%s\t;\n" %(wordmap['analysis'], wordmap['stub'], new_para)
    return retvals

def format_multichars_lexc_apertium():
    multichars = "!! Apertium standard tags:\n"
    for mcs in apertium_multichars:
        if not '><' in mcs and not mcs in ['', '+', '-', '#', '0']:
            multichars += '%<' + lexc_escape(mcs) + "%>\n"
    return multichars

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
        return s.replace(' ', '<b/>').replace(word_boundary, '')
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
        fail_formatting_missing_for(stuff, "monodix")
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
        e += '<p><l>' + wordmap['stub'].replace(word_boundary, '').replace('&', '&amp;')  +  '</l>'
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
    for stuff, ape in stuff2apertium.items():
        if len(ape) < 2:
            continue
        elif ape.startswith('+'):
            if not ape[ape.find('+'):]:
                print("There are conflicting formattings in here!", 
                        ape[ape.find('+'):],
                        "is not a valid apertium multichar_symbol!")
                fail = True
        elif not ape in apertium_multichars:
            print("There are conflicting formattings in here!", ape, 
                    "is not a valid apertium multichar_symbol!")
            fail = True
    if fail:
        exit(1)

