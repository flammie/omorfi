#!/usr/bin/env python3
#
# utils to format lexc strings from omor's lexical data sources.

from sys import stderr
from lexc_string_utils import lexc_escape

from lexc_string_utils import lexc_escape

def format_analysis_omor(wordmap):
    '''
    format analysis (lexc LHS) string for canonical omor format for 
    morphological analysis
    '''
    tn = int(wordmap['analysis_tn'])
    wordmap['analysis'] = "[WORD_ID=%(lemma)s]" %(wordmap)
    if wordmap['pos'] == 'PROPER':
        wordmap['analysis'] += "[POS=NOUN][SUBCAT=%(pos)s]" %(wordmap)
    elif wordmap['lexicon'] == 'Suffixes':
        wordmap['analysis'] += "[POS=%(pos)s][SUBCAT=SUFFIX]" %(wordmap)
    elif wordmap['lexicon'] == 'Prefixes':
        wordmap['analysis'] += "[POS=NOUN][SUBCAT=PREFIX]" %(wordmap)
    elif wordmap['pos'] in ['ACRONYM', 'ABBREVIATION']:
        wordmap['analysis'] += "[POS=NOUN][SUBCAT=%(pos)s]" %(wordmap)
    elif wordmap['pos'] in ['CONJUNCTION', 'INTERJECTION']:
        wordmap['analysis'] = "[POS=PARTICLE][SUBCAT=%(pos)s]" %(wordmap)
    else:
        wordmap['analysis'] = "[POS=%(pos)s]" %(wordmap)
    return wordmap

def format_analysis_omor_paralysed(wordmap):
    '''
    format analysis string for canonical omor format for kotus
    paradigm harvesting applications
    '''
    tn = int(wordmap['analysis_tn'])
    if wordmap['is_proper']:
        if tn < 99 and wordmap['kotus_av']:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=PROPER][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
        elif tn < 99:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=PROPER][KTN=%(analysis_tn)s]" %(wordmap)
        else:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=PROPER]" %(wordmap)
        if use_prop_subclasses and wordmap['proper_noun_class']:
            wordmap['proper_noun_class'].sort()
            wordmap['analysis'] = wordmap['analysis'].replace('[SUBCAT=PROPER]', '[SUBCAT=PROPER][PROP=' +
            ','.join(wordmap['proper_noun_class']) + ']')
    elif wordmap['lexicon'] == 'Suffixes':
        if tn < 99 and wordmap['kotus_av']:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=%(pos)s][SUBCAT=SUFFIX][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
        elif tn < 99:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=%(pos)s][SUBCAT=SUFFIX][KTN=%(analysis_tn)s]" %(wordmap)
        else:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=%(pos)s][SUBCAT=SUFFIX]" %(wordmap)
    elif wordmap['lexicon'] == 'Prefixes':
        if tn < 99 and wordmap['kotus_av']:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=PREFIX][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
        elif tn < 99:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=PREFIX][KTN=%(analysis_tn)s]" %(wordmap)
        else:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=PREFIX]" %(wordmap)
    elif wordmap['pos'] == 'ACRONYM':
        if tn < 99 and wordmap['kotus_av']:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=%(pos)s][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
        elif tn < 99:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=%(pos)s][KTN=%(analysis_tn)s]" %(wordmap)
        else:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=%(pos)s]" %(wordmap)
    elif wordmap['pos'] == 'ABBREVIATION':
        if tn < 99 and wordmap['kotus_av']:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=%(pos)s][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
        elif tn < 99:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=%(pos)s][KTN=%(analysis_tn)s]" %(wordmap)
        else:
            wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=NOUN][SUBCAT=%(pos)s]" %(wordmap)
    elif tn < 99 and wordmap['kotus_av']:
        wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=%(pos)s][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
    elif tn < 99:
        wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=%(pos)s][KTN=%(analysis_tn)s]" %(wordmap)
    else:
        wordmap['analysis'] = "[WORD_ID=%(lemma)s][POS=%(pos)s]" %(wordmap)
    return wordmap

def format_surface_omor(wordmap):
    return wordmap

def format_lexc_omor(wordmap):
    return ("%s:%s   %s  ;" % (lexc_escape(wordmap['analysis']), 
        lexc_escape(wordmap['stub']), wordmap['continuation']))

