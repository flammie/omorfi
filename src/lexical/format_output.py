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
    elif wordmap['pos'] in ['ACRONYM', 'ABBREVIATION']:
        wordmap['analysis'] += "[POS=NOUN][SUBCAT=%(pos)s]" %(wordmap)
    elif wordmap['pos'] in ['CONJUNCTION', 'INTERJECTION']:
        wordmap['analysis'] += "[POS=PARTICLE][SUBCAT=%(pos)s]" %(wordmap)
    else:
        wordmap['analysis'] += "[POS=%(pos)s]" %(wordmap)

    if wordmap['subcat']:
        wordmap['analysis'] += "[SUBCAT=%(subcat)s]" %(wordmap)

    if wordmap['is_proper']:
        wordmap['analysis'] += "[SUBCAT=PROPER]"
        if wordmap['proper_noun_class']:
            for prop in wordmap['proper_noun_class'].split(','):
                wordmap['analysis'] += '[PROP=%s]' %(prop)

    if format == 'ktnkav' and tn < 99:
        wordmap['analysis'] += "[KTN=%(kotus_tn)s]" %(wordmap)
        if wordmap['kotus_av']:
            wordmap['analysis'] += "[KAV=%(kotus_av)s]" %(wordmap)
    elif format == 'newparas':
        wordmap['analysis'] += "[PARA=%(new_para)s]" %(wordmap)
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    # match WORD_ID= with epsilon, then stub and lemma might match
    wordmap['stub'] = '0' + wordmap['stub'] 
    return ("%(analysis)s:%(stub)s\t%(new_para)s\t;" % (wordmap))

def format_lexc_apertium(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['lemma'])
    if wordmap['is_suffix']:
        wordmap['analysis'] = "#" + wordmap['analysis']
    elif wordmap['is_prefix']:
        wordmap['analysis'] += "#"
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


def format_xml_kotus_sanalista(wordmap):
    if wordmap['kotus_av']:
        return ("<st><s>%(lemma)s</s><t><tn>%(kotus_tn)s</tn><av>%(kotus_av)s</av></t></st>" %(wordmap))
    else:
        return ("<st><s>%(lemma)s</s><t><tn>%(kotus_tn)s</tn></t></st>" %(wordmap))
