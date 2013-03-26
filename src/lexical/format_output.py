#!/usr/bin/env python3
#
# utils to format lexc strings from omor's lexical data sources.

from sys import stderr
from lexc_string_utils import lexc_escape

def format_analysis_omor(wordmap, format, use_prop_subclasses):
    '''
    format analysis (lexc LHS) string for canonical omor format for 
    morphological analysis
    '''
    tn = int(wordmap['kotus_tn'])
    wordmap['analysis'] = "[WORD_ID=%(lemma)s]" %(wordmap)
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

    if wordmap['is_proper']:
        wordmap['analysis'] += "[SUBCAT=PROPER]" %(wordmap)
        if use_prop_subclasses and wordmap['proper_noun_class']:
            wordmap['proper_noun_class'].sort()
            wordmap['analysis'] = wordmap['analysis'].replace('[SUBCAT=PROPER]', '[SUBCAT=PROPER][PROP=' +
            ','.join(wordmap['proper_noun_class']) + ']')

    if format == 'ktnkav' and tn < 99:
        wordmap['analysis'] += "[KTN=%(kotus_tn)s]" %(wordmap)
        if wordmap['kotus_av']:
            wordmap['analysis'] += "[KAV=%(kotus_av)s]" %(wordmap)
    elif format == 'newparas':
        wordmap['analysis'] += "[PARA=%(new_para)s]" %(wordmap)
    return wordmap

def format_surface_omor(wordmap):
    return wordmap

def format_lexc_omor(wordmap):
    return ("%s:%s\t%s\t;" % (lexc_escape(wordmap['analysis']), 
        lexc_escape(wordmap['stub']), wordmap['new_para']))

