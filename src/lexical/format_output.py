#!/usr/bin/env python3

def format_analysis_omor(wordmap):
    tn = int(wordmap['analysis_tn'])
    if wordmap['pos'] == 'PROPER':
        if tn < 99 and wordmap['kotus_av']:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=%(pos)s][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
        elif tn < 99:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=%(pos)s][KTN=%(analysis_tn)s]" %(wordmap)
        else:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=%(pos)s]" %(wordmap)
    elif wordmap['lexicon'] == 'Suffixes':
        if tn < 99 and wordmap['kotus_av']:
            wordmap['analysis'] = "%(lemma)s'][POS=%(pos)s][SUBCAT=SUFFIX][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
        elif tn < 99:
            wordmap['analysis'] = "%(lemma)s'][POS=%(pos)s][SUBCAT=SUFFIX][KTN=%(analysis_tn)s]" %(wordmap)
        else:
            wordmap['analysis'] = "%(lemma)s'][POS=%(pos)s][SUBCAT=SUFFIX]" %(wordmap)
    elif wordmap['lexicon'] == 'Prefixes':
        if tn < 99 and wordmap['kotus_av']:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=PREFIX][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
        elif tn < 99:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=PREFIX][KTN=%(analysis_tn)s]" %(wordmap)
        else:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=PREFIX]" %(wordmap)
    elif wordmap['pos'] == 'ACRONYM':
        if tn < 99 and wordmap['kotus_av']:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=%(pos)s][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
        elif tn < 99:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=%(pos)s][KTN=%(analysis_tn)s]" %(wordmap)
        else:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=%(pos)s]" %(wordmap)
    elif wordmap['pos'] == 'ABBREVIATION':
        if tn < 99 and wordmap['kotus_av']:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=%(pos)s][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
        elif tn < 99:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=%(pos)s][KTN=%(analysis_tn)s]" %(wordmap)
        else:
            wordmap['analysis'] = "%(lemma)s'][POS=NOUN][SUBCAT=%(pos)s]" %(wordmap)
    elif tn < 99 and wordmap['kotus_av']:
        wordmap['analysis'] = "%(lemma)s'][POS=%(pos)s][KTN=%(analysis_tn)s][KAV=%(kotus_av)s]" %(wordmap)
    elif tn < 99:
        wordmap['analysis'] = "%(lemma)s'][POS=%(pos)s][KTN=%(analysis_tn)s]" %(wordmap)
    else:
        wordmap['analysis'] = "%(lemma)s'][POS=%(pos)s]" %(wordmap)
    wordmap['analysis'] = lexc_escape(wordmap['analysis'])
    return wordmap

def format_surface_omor(wordmap):
    return wordmap

def format_lexc_omor(wordmap):
    return ("%s:%s   %s  ;" % (lexc_escape(wordmap['analysis']), 
        lexc_escape(wordmap['stub']), wordmap['lexicon']))

