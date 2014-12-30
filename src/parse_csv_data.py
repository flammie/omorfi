#!/usr/bin/env python3

from omor_strings_io import replace_rightmost
from sys import stderr
from ast import literal_eval

def parse_defaults_from_tsv(wordmap, tsv_parts):
    '''Parse default data from 2+ field tsv with new para and lemma.'''
    # first field is lemma; start all deep, shallow and surface forms from that
    wordmap['lemma'] = tsv_parts[0]
    wordmap['stub'] = wordmap['lemma']
    wordmap['bracketstub'] = wordmap['lemma']
    wordmap['gradestem'] = wordmap['lemma']
    # second field is new paradigm class set
    wordmap['new_para'] = tsv_parts[1]
    return wordmap


def parse_extras_from_tsv(wordmap, tsv_parts):
    '''Parse extra fields form >3 fields of 2+ field tsv.'''
    if len(tsv_parts) >= 3:
        for tsv_extra in tsv_parts[2:]:
            extra_fields = tsv_extra.split("=")
            if extra_fields[0] == 'plurale_tantum':
                wordmap['plurale_tantum'] = extra_fields[1]
            elif extra_fields[0] == 'proper_noun_class':
                wordmap['proper_noun_class'].append( extra_fields[1].upper() )
                wordmap['is_proper'] = True
            elif extra_fields[0] == 'adjective_class':
                wordmap['adjective_class'] =  extra_fields[1].upper()
            elif extra_fields[0] == 'noun_class':
                wordmap['noun_class'] =  extra_fields[1].upper() 
            elif extra_fields[0] == 'numeral_class':
                wordmap['numeral_class'] =  extra_fields[1].upper() 
            elif extra_fields[0] == 'possessive':
                wordmap['possessive'] = extra_fields[1]
            elif extra_fields[0] == 'clitics':
                wordmap['clitics'] = extra_fields[1]
            elif extra_fields[0] == 'stem-vowel':
                wordmap['stem_vowel'] = extra_fields[1]
            elif extra_fields[0] == 'style':
                wordmap['style'] = extra_fields[1].upper()
            elif extra_fields[0] == 'boundaries':
                wordmap['stub'] = extra_fields[1]
                wordmap['boundaries'] = extra_fields[1]
            elif extra_fields[0] == 'subcat':
                wordmap['subcat'] = extra_fields[1].upper()
            elif extra_fields[0] == 'sem':
                wordmap['sem'].append(extra_fields[1].upper())
            elif extra_fields[0] == 'particle':
                wordmap['particle'] = extra_fields[1].upper()
            elif extra_fields[0] == 'pronunciation':
                wordmap['pronunciation'] = extra_fields[1]
            elif extra_fields[0] == 'origin':
                wordmap['origin'] = extra_fields[1]
            elif extra_fields[0] == 'symbol':
                wordmap['symbol'] = extra_fields[1].upper()
            elif extra_fields[0] == 'argument':
                wordmap['argument'] = extra_fields[1].upper()
            elif extra_fields[0] == 'pronoun':
                wordmap['pronoun'] = extra_fields[1].upper()
            elif extra_fields[0] == 'homonym':
                wordmap['homonym'] = int(extra_fields[1])
            else:
                print("Unrecognised extra field", tsv_extra, "in TSV", file=stderr)
                exit(1)
    wordmap['proper_noun_class'].sort()
    wordmap['proper_noun_class'] = ','.join(wordmap['proper_noun_class'])
    wordmap['sem'].sort()
    wordmap['sem'] = ','.join(wordmap['sem'])
    
    return wordmap

