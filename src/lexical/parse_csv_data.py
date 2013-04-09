#!/usr/bin/env python3

from lexc_string_utils import replace_rightmost
from sys import stderr

def parse_defaults_from_csv(wordmap, csv_parts):
    wordmap['lexicon'] = ''
    wordmap['continuation'] = ''
    # first field is lemma
    wordmap['lemma'] = csv_parts[0].strip('"')
    wordmap['stub'] = wordmap['lemma']
    wordmap['gradestem'] = wordmap['lemma']
    # second field is KOTUS paradigm class
    try:
        wordmap['kotus_tn'] = int(csv_parts[1].strip('"'))
    except ValueError:
        print("Confusing paradigm on", csv_parts, "Retarding to 99", file=stderr)
        wordmap['kotus_tn'] = 99
    wordmap['analysis_tn'] = int(wordmap['kotus_tn'])
    if wordmap['kotus_tn'] < 1 or (wordmap['kotus_tn'] > 78 and wordmap['kotus_tn'] < 99):
        print("Bad paradigm", csv_parts[1], "in", csv_parts, file=stderr)
    # third field is KOTUS gradation class
    grad = csv_parts[2].strip('"')
    if grad == '0':
        wordmap['kotus_av'] = False
    elif grad in 'ABCDEFGHIJKLMNOPT':
        wordmap['kotus_av'] = csv_parts[2].strip('"')
    else:
        wordmap['kotus_av'] = False
        print("Unknown gradation field", csv_parts[2], "in", csv_parts,
                file=stderr)
    # fourth field is morphosyntactic POS
    wordmap['is_proper'] = False
    wordmap['pos'] = csv_parts[3].strip('"')
    if wordmap['pos'] == 'A':
        wordmap['pos'] = 'ADJECTIVE'
    elif wordmap['pos'] == 'N':
        wordmap['pos'] = 'NOUN'
    elif wordmap['pos'] == 'V':
        wordmap['pos'] = 'VERB'
    elif wordmap['pos'] == 'P':
        wordmap['pos'] = 'PARTICLE'
    elif wordmap['pos'] == 'Prop':
        wordmap['pos'] = 'NOUN'
        wordmap['is_proper'] = True
    elif wordmap['pos'] == 'Adv':
        wordmap['pos'] = 'ADVERB'
    elif wordmap['pos'] == 'Adp':
        wordmap['pos'] = 'ADPOSITION'
    elif wordmap['pos'] == 'Intj':
        wordmap['pos'] = 'INTERJECTION'
    elif wordmap['pos'] == 'Conj':
        wordmap['pos'] = 'CONJUNCTION'
    elif wordmap['pos'] == 'Pre':
        wordmap['pos'] = 'NOUN'
        wordmap['is_prefix'] = True
    elif wordmap['pos'] == 'Abbr':
        wordmap['pos'] = 'ABBREVIATION'
    elif wordmap['pos'] == 'Acro':
        wordmap['pos'] = 'ACRONYM'
    elif wordmap['pos'] == 'Num':
        wordmap['pos'] = 'NUMERAL'
    elif wordmap['pos'] == 'Pron':
        wordmap['pos'] = 'PRONOUN'
    else:
        print("Unrecognised POS", csv_parts[3], "in", csv_parts)

    # basic compatibility checking
    tn = wordmap['kotus_tn'] % 1000
    if (tn < 52 and wordmap['pos'] == 'VERB') \
            or (52 <= tn <= 78 and wordmap['pos'] in ['NOUN','ADJECTIVE','PRONOUN','NUMERAL']):
        print("Incompatible paradigm class and POS in", csv_parts, file=stderr)

    # this is all the optional extra data we found useful
    wordmap['plurale_tantum'] = False
    wordmap['proper_noun_class'] = []
    wordmap['possessive'] = False
    wordmap['harmony'] = False
    wordmap['stem_vowel'] = False
    wordmap['stem_diphtong'] = False
    wordmap['extra_i'] = False
    wordmap['extra_e'] = False
    return wordmap


def parse_extras_from_csv(wordmap, csv_parts):
    if len(csv_parts) >= 5:
        for csv_extra in csv_parts[4:]:
            extra_fields = csv_extra.split("=")
            if extra_fields[0] == 'plt':
                wordmap['plurale_tantum'] = extra_fields[1]
            elif extra_fields[0] == 'prop':
                if wordmap['is_proper'] or wordmap['pos'] == 'ACRONYM':
                    wordmap['proper_noun_class'].append( extra_fields[1].upper() )
                    wordmap['is_proper'] = True
                else:
                    print("Warning: Ignoring attribute", csv_extra, "for", wordmap['lemma'], file=stderr)
            elif extra_fields[0] == 'poss':
                wordmap['possessive'] = extra_fields[1]
            elif extra_fields[0] == 'stem-vowel':
                wordmap['stem_vowel'] = extra_fields[1]
            elif extra_fields[0] == 'style':
                wordmap['style'] = extra_fields[1]
            elif extra_fields[0] == 'boundaries':
                wordmap['stub'] = extra_fields[1].replace("|", "{#}").replace("_", "{_}")
            else:
                print("Unrecognised extra field", csv_extra, "in CSV", file=stderr)
    wordmap['proper_noun_class'].sort()
    wordmap['proper_noun_class'] = ','.join(wordmap['proper_noun_class']) or False
    return wordmap

def parse_conts(wordmap):
    tn = wordmap['kotus_tn']
    if (0 < tn and tn < 50) or (51 < tn and tn < 99):
        wordmap['lexicon'] = 'kotus_' + str(tn)
        wordmap['continuation'] = wordmap['lexicon']
    elif tn > 1000:
        if tn < 2000:
            cont_tn = tn - 1000
            if wordmap['analysis_tn'] > 1000:
                wordmap['analysis_tn'] = cont_tn
        else:
            cont_tn = wordmap['analysis_tn']
        wordmap['lexicon'] = "exceptional_" + str(cont_tn)
        wordmap['continuation'] = wordmap['lexicon']
    elif tn == 99:
        if wordmap['lexicon'] == '':
            wordmap['lexicon'] = 'kotus_99_' + wordmap['pos']
            wordmap['continuation'] = 'Ennd'
    elif tn == 101:
        wordmap['lexicon'] = wordmap['lexicon']
    else:
        print('Unrecognised tn', tn, 'in', wordmap['lemma'], file=stderr)
    return wordmap

def finetune_conts(wordmap):
    if wordmap['extra_i']:
        wordmap['continuation'] += 'i'
    elif wordmap['extra_e']:
        wordmap['continuation'] += 'e'
    elif wordmap['stem_diphtong']:
        wordmap['continuation'] += wordmap['stem_diphtong']
    elif wordmap['kotus_tn'] in [28, 54, 55, 57] and wordmap['kotus_av']:
        wordmap['continuation'] += wordmap['kotus_av']
    # more continuation finetuning
    if wordmap['kotus_tn'] < 99 or wordmap['kotus_tn'] > 1000:
        wordmap['continuation'] += '_' + wordmap['pos']
        wordmap['lexicon'] += '_' + wordmap['pos']
        wordmap['lexicon'] += '/stub'
        wordmap['continuation'] += '/stemfiller'
    elif wordmap['pos'] == "ACRONYM":
        wordmap['continuation'] += '/' + wordmap['stub'][-1]
    elif wordmap['pos'] in ["ADPOSITION","ADVERB"]  and wordmap['possessive']:
        if wordmap['possessive'] == 'opt':
            wordmap['continuation'] = 'Possessive/Optional+Vn'
        elif wordmap['possessive'] == 'obl':
            wordmap['continuation'] = 'Possessive/Obligatory+Vn'
        else:
            print("Odd possessive in", wordmap['lemma'], file=stderr)
    return wordmap

def add_extras(wordmap):
    if wordmap['stem_vowel']:
        wordmap['gradestem'] += '{^' + wordmap['stem_vowel'] + '}'
    if wordmap['harmony']:
        wordmap['gradestem'] += '{^' + wordmap['harmony'] + '}'
    if wordmap['kotus_av']:
        wordmap['gradestem'] += '{' + wordmap['kotus_av'] + '}'
    if wordmap['plurale_tantum'] == 'obligatory':
        wordmap['gradestem'] += '@U.PLURALE.TANTUM@'
    elif wordmap['plurale_tantum'] == 'common':
        wordmap['gradestem'] += '{PLT?}'
    if wordmap['is_prefix']:
        wordmap['stub'] = replace_rightmost(wordmap['stub'], '-', '')
    elif wordmap['is_suffix']:
        wordmap['stub'] = wordmap['stub'][1:]
    return wordmap

def parse_from_tsv(wordmap, fields):
    wordmap['lemma'] = fields[0]
    wordmap['new_para'] = fields[1]
    wordmap['pos'] = fields[2]
    wordmap['kotus_tn'] = fields[3]
    wordmap['kotus_av'] = fields[4]
    wordmap['plurale_tantum'] = fields[5]
    wordmap['possessive'] = fields[6]
    wordmap['clitics'] = fields[7]
    wordmap['is_proper'] = fields[8]
    wordmap['proper_noun_class'] = fields[9]
    wordmap['style'] = fields[10]
    wordmap['stub'] = fields[11]
    wordmap['gradestem'] = fields[12]
    wordmap['twolstem'] = fields[13]
    wordmap['grade_dir'] = fields[14]
    wordmap['harmony'] = fields[15]
    wordmap['is_suffix'] = fields[16]
    wordmap['is_prefix'] = fields[17]
    wordmap['stem_vowel'] = fields[18]
    wordmap['stem_diphthong'] = fields[19]
    for k,v in wordmap.items():
        if v == 'False':
            wordmap[k] = False
        if v == 'None':
            wordmap[k] = None
    return wordmap

