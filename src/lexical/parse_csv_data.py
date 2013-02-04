#!/usr/bin/env python3

from lexc_string_utils import replace_rightmost
from sys import stderr

def parse_defaults_from_csv(wordmap, csv_parts):
    wordmap['lexicon'] = ''
    wordmap['continuation'] = ''
    # first field is lemma
    wordmap['lemma'] = csv_parts[0].strip('"')
    wordmap['stub'] = wordmap['lemma']
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
        wordmap['lexicon'] = 'Particles'
        wordmap['continuation'] = 'Particle+Clitic/Optional'
    elif wordmap['pos'] == 'Prop':
        wordmap['pos'] = 'NOUN'
        wordmap['is_proper'] = True
    elif wordmap['pos'] == 'Adv':
        wordmap['pos'] = 'ADVERB'
        wordmap['lexicon'] = 'Adverbs'
        wordmap['continuation'] = 'Adverb+Clitic/Optional'
    elif wordmap['pos'] == 'Adp':
        wordmap['pos'] = 'ADPOSITION'
        wordmap['lexicon'] = 'Adpositions'
        wordmap['continuation'] = 'Adposition+Clitic/Optional'
    elif wordmap['pos'] == 'Intj':
        wordmap['pos'] = 'INTERJECTION'
        wordmap['lexicon'] = 'Interjections'
        wordmap['continuation'] = 'Interjection+Ennd'
    elif wordmap['pos'] == 'Conj':
        wordmap['pos'] = 'CONJUNCTION'
        wordmap['lexicon'] = 'Conjunctions'
        wordmap['continuation'] = 'Conjunction+Ennd'
    elif wordmap['pos'] == 'Pre':
        wordmap['pos'] = 'PREFIX'
        wordmap['lexicon'] = 'Prefixes'
        wordmap['continuation'] = 'Prefix+Compounding'
    elif wordmap['pos'] == 'Abbr':
        wordmap['pos'] = 'ABBREVIATION'
        wordmap['lexicon'] = 'Abbreviations'
        wordmap['continuation'] = 'Abbreviation+Ennd'
    elif wordmap['pos'] == 'Acro':
        wordmap['pos'] = 'ACRONYM'
        wordmap['lexicon'] = 'Acronyms'
        wordmap['continuation'] = 'AcronymStem'
    elif wordmap['pos'] == 'Num':
        wordmap['pos'] = 'NUMERAL'
        wordmap['lexicon'] = 'Numerals'
        wordmap['continuation'] = 'Numeral+Ennd'
    elif wordmap['pos'] == 'Pron':
        wordmap['pos'] = 'PRONOUN'
        wordmap['lexicon'] = 'Pronouns'
        wordmap['continuation'] = 'Pronoun+Ennd'
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
            if extra_fields[0] == '"plt':
                wordmap['plurale_tantum'] = extra_fields[1].strip('"')
            elif extra_fields[0] == '"prop':
                wordmap['proper_noun_class'].append( extra_fields[1].strip('"').upper() )
            elif extra_fields[0] == '"poss':
                wordmap['possessive'] = extra_fields[1].strip('"')
            elif extra_fields[0] == '"stem-vowel':
                wordmap['stem_vowel'] = extra_fields[1].strip('"')
            elif extra_fields[0] == '"original-ktn':
                wordmap['analysis_tn'] = int(extra_fields[1].strip('"'))
            elif extra_fields[0] == '"style':
                wordmap['style'] = extra_fields[1].strip('"')
            elif extra_fields[0] == '"stub':
                wordmap['explicit_stub'] = extra_fields[1].strip('"')
            elif extra_fields[0] == '"stem':
                wordmap['explicit_stem'] = extra_fields[1].strip('"')
            elif extra_fields[0] == '"boundaries':
                wordmap['stub'] = extra_fields[1].strip('"').replace("|", "{#}").replace("_", "{_}").replace(" ", " {#}")
                wordmap['lemma'] = extra_fields[1].strip('"').replace("|", "'|'").replace("_", "'_'")
            else:
                print("Unrecognised extra field", csv_extra, "in CSV", file=stderr)
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
        wordmap['stub'] += '{^' + wordmap['stem_vowel'] + '}'
    if wordmap['harmony']:
        wordmap['stub'] += '{^' + wordmap['harmony'] + '}'
    if wordmap['kotus_av']:
        wordmap['stub'] += '{' + wordmap['kotus_av'] + '}'
    if wordmap['plurale_tantum'] == 'obligatory':
        wordmap['stub'] += '@U.PLURALE.TANTUM@'
    elif wordmap['plurale_tantum'] == 'common':
        wordmap['stub'] += '{PLT?}'
    if wordmap['pos'] == 'PREFIX':
        wordmap['stub'] = replace_rightmost(wordmap['stub'], '-', '')
        wordmap['analysis'] = replace_rightmost(wordmap['analysis'], '-', '')
    elif wordmap['pos'] == 'SUFFIX':
        wordmap['stub'] = wordmap['stub'][1:]
        wordmap['analysis'] = wordmap['analysis'][1:]
    return wordmap


