#!/usr/bin/env python3

from omorfi_settings import common_multichars, \
        fin_lowercase, fin_uppercase, fin_vowels, fin_consonants, \
        optional_hyphen

def format_copyright_twolc():
    return """
! This automatically generated twolc data is originated from 
! omorfi database.
! Copyright (c) 2014 Omorfi contributors

! This program is free software: you can redistribute it and/or modify
! it under the terms of the GNU General Public License as published by
! the Free Software Foundation, version 3 of the License

! This program is distributed in the hope that it will be useful,
! but WITHOUT ANY WARRANTY; without even the implied warranty of
! MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
! GNU General Public License for more details.

! You should have received a copy of the GNU General Public License
! along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

def twolc_escape(s):
    '''Escape symbols that have special meaning in twolc.'''
    s = s.replace("%", "__PERCENT__")
    for c in ' @<>0!:";_^(){}-[]/?+|&*=$,':
        s = s.replace(c, "%" + c)
    s = s.replace("%_%_PERCENT%_%_", "%%")
    return s

def format_alphabet_twolc(format, ruleset):
    twolcstring = 'Alphabet\n'
    if ruleset.startswith('recase'):
        twolcstring += '! Set of Finnish alphabets generated from python:\n'
        for c in fin_lowercase:
            twolcstring += c + '! allow lowercase as is\n'
            twolcstring += c + ':' + c.upper() + '! allow uppercasing\n'
        for c in fin_uppercase:
            twolcstring += c + '! allow uppercase as is\n'
            twolcstring += c + ':' + c.lower() + '! allow lowercasing\n'
        for mcs in common_multichars:
            twolcstring += twolc_escape(mcs) + '\n'
    elif ruleset.startswith('uppercase'):
        twolcstring += '! Set of Finnish alphabets generated from python:\n'
        for c in fin_lowercase:
            twolcstring += c + '! allow lowercase as is\n'
            twolcstring += c + ':' + c.upper() + '! allow uppercasing\n'
        for c in fin_uppercase:
            twolcstring += c + '! allow uppercase as is\n'
        for mcs in common_multichars:
            twolcstring += twolc_escape(mcs) + '\n'
    elif ruleset == 'hyphenate':
        twolcstring += ' '.join(fin_lowercase) + '! lower'
        twolcstring += ' '.join(fin_uppercase) + '! upper'
        for mcs in common_multichars:
            twolcstring += twolc_escape(mcs) + ':0 ! deleting all specials\n'
    if ruleset == 'hyphens':
        twolcstring += twolc_escape(optional_hyphen) + ':0  ! boundary can be zero\n'
        twolcstring += twolc_escape(optional_hyphen) + ':%- ! or (ASCII) hyphen\n'
    elif ruleset == 'apertium':
        for mcs in common_multichars:
            twolcstring += twolc_escape(mcs) + ':0 ! deleting all specials\n'
    else:
        print("Unknown ruleset", ruleset, file=stderr)
        exit(1)
    twolcstring += ';\n'
    return twolcstring

def format_sets_twolc(format, ruleset):
    twolcstring = 'Sets\n'
    if ruleset.startswith('uppercase') or ruleset.startswith('recase'):
        twolcstring += 'Lower = ' + ' '.join(fin_lowercase) + ' ;' + \
                '! Lowercase alphabets\n'
        twolcstring += 'Upper = ' + ' '.join(fin_uppercase) + ' ;' + \
                '! Uppercase alphabets\n'
    elif ruleset == 'hyphens':
        twolcstring += 'Vowels = ' + ' '.join(fin_vowels) + ' ;' + \
                '! Vowels\n'
        twolcstring += 'UpperOrSyms = ' + ' '.join(fin_uppercase) + \
                ' ' + ' '.join([twolc_escape(s) for s in fin_symbols]) +\
                '; ' + '! Symbols for likely hyphenated words\n'
    elif ruleset == 'hyphenate':
        twolcstring += 'Vowels = ' + ' '.join(fin_vowels) + ' ;' + \
                '! Vowels\n'
        twolcstring += 'Consonants = ' + ' '.join(fin_consonants) + ' ;' + \
                '! Consonants\n'
    elif ruleset == 'apertium':
        pass
    else:
        print("missing ruleset", ruleset)
        exit(1)
    twolcstring += 'DUMMYSETCANBEUSEDTOTESTBUGS = a b c ;\n'
    return twolcstring

def format_definitions_twolc(format, ruleset):
    twolcstring = 'Definitions\n'
    if ruleset == 'hyphenate':
        twolcstring += 'WordBoundary = [ %- | 0:%- |' \
                + word_boundary + ':0 ] ;\n'
    twolcstring += 'DUMMYDEFINITIONCANBEUSEDTOTESTBUGS = a | b | c ;\n'
    return twolcstring

def format_rules_twolc(format, ruleset):
    twolcstring = "Rules\n"
    if ruleset == 'stub-phon':
        twolcstring += '"Dummy rule"\na <= _ ;\n'
    elif ruleset == 'recase-any':
        twolcstring += '"Uppercase anywhere dummy rule"\n'
        twolcstring += twolc_escape(optional_hyphen) + " <= _ ;\n"
    elif ruleset == 'uppercase-first':
        twolcstring += '"Require uppercase in beginning"\n'
        twolcstring += 'LC:UC => .#. _ ;\n'
        twolcstring += '\twhere LC in Lower UC in Upper matched ;\n'
    elif ruleset == 'hyphens':
        twolcstring += '"Disallow no hyphen between equal vowels"\n'
        twolcstring += twolc_escape(optional_hyphen) + ':0 /<= ' + \
                "VOWEL :0* _ :0* VOWEL ; where VOWEL in Vowels matched ;\n"
    elif ruleset == 'hyphenate':
        twolcstring += '"Hyphenate Before consonant clusters"\n'
        twolcstring += "0:%- <=> Vowels Consonants* _ Consonants Vowels ;\n"
        twolcstring += '"Hyphenate between non-diphtongs"\n'
        twolcstring += "0:%- <=> Vx _ Vy ;\n"
        twolcstring += "\twhere Vx in (a a a a a e e e e i i i i o o o o o u u u u u y y y y y ä ä ä ä ä ö ö ö ö)\n"
        twolcstring += "\t\tVy in (e o y ä ö a o ä ö a o ä ö a e y ä ö a e y ä ö e ä a o u e ö a o u ä a o u) matched ;\n"
        twolcstring += '"Hyphenate diphtongs in latter syllables"\n'
        twolcstring += "0:%- <=> WordBoundary Consonants* [Vowels+ Consonants+]+ Vx _ Vy ;\n"
        twolcstring += "\twhere Vx in (a e o u y ä ö a e i o ä ö u y i e i)\n"
        twolcstring += "\t\tVy in (i i i i i i i u u u u y y o ö y y e) matched ;\n"
    elif ruleset == 'apertium':
        twolcstring += '"Remove stuffs"\n'
        twolcstring += "a <= _ ; ! remove everywhere\n"
    else:
        print("Unknown ruleset", ruleset, file=stderr)
        exit(1)
    return twolcstring
