#!/usr/bin/env python3
#
# utils to format lexc strings from omor's lexical data sources.

from sys import stderr
from omor_strings_io import lexc_escape, twolc_escape, version_id_easter_egg, \
        word_boundary, deriv_boundary, morph_boundary, stub_boundary,\
        weak_boundary, optional_hyphen, fin_uppercase, fin_lowercase,\
        fin_vowels, fin_consonants, fin_symbols, fin_orth_pairs
from cgi import escape as xml_escape
from apertium_formatter import format_tag_apertium, \
        format_analysis_lexc_apertium, format_continuation_lexc_apertium, \
        format_lexc_apertium, format_multichars_lexc_apertium
from ftb3_formatter import format_tag_ftb3, \
        format_analysis_lexc_ftb3, format_continuation_lexc_ftb3, \
        format_lexc_ftb3, format_multichars_lexc_ftb3
from omor_formatter import format_tag_omor, \
        format_analysis_lexc_omor, format_continuation_lexc_omor, \
        format_lexc_omor, format_multichars_lexc_omor


# these extra symbols appear always


common_multichars={
        version_id_easter_egg,
        word_boundary,
        weak_boundary,
        deriv_boundary,
        morph_boundary,
        stub_boundary,
        optional_hyphen
        }



google_multichars = {"% NOUN", "% ADJ", "% VERB", "% ADV", "% X", "% PRON",
        '%<Del%>→', '←%<Del%>',
        "% NUM", "% ADP", "% CONJ", "% PRT", "% ."}

stuff2google = {
        ".sent": "",
        "Bc": "#",
        "B-": "",
        "B→": "",
        "B←": "",
        "Cma": "",
        "Cnut": "",
        "Cva": "",
        "Cmaton": "",
        "Cpos": "",
        "Ccmp": "",
        "Csup": "",
        "Dmaisilla": "% ADV",
        "Dminen": "% NOUN",
        "Dnut": "% ADJ", "Dtu": "% ADJ", "Dva": "% ADJ", "Dtava": "% ADJ",
        "Dmaton": "% NOUN",
        "Duus": "% NOUN", "Dttaa": "% VERB", "Dtattaa": "% VERB",
        "Dtatuttaa": "% VERB",
        "Dma": "% NOUN", "Dinen": "% ADJ", "Dja": "% NOUN", "Dmpi": "% ADJ",
        "Din": "% ADJ", "Ds": "", "Du": "% NOUN", "Dsti": "% ADV",
        "FTB3man": "",
        "Ia": "",
        "Ie": "",
        "Ima": "",
        "Iminen": "",
        "Ncon": "",
        "Nneg": "", 
        "Npl": "", 
        "Nsg": "", 
        "N??": "",
        "Osg1": "",
        "Osg2": "",
        "O3": "",
        "Opl1": "",
        "Opl2": "",
        "Ppl1": "", 
        "Ppl2": "",
        "Ppl3": "",
        "Psg1": "", 
        "Psg2": "",
        "Psg3": "",
        "Ppe4": "", 
        "Qka": "% CONJ",
        "Qs": "",
        "Qpa": "",
        "Qko": "",
        "Qkin": "",
        "Qkaan": "",
        "Qhan": "",
        "Tcond": "",
        "Timp": "", 
        "Tpast": "",
        "Tpot": "", 
        "Tpres": "",
        "Topt": "",
        "Uarch": "", "Udial": "", "Urare": "", "Unonstd": "",
        "Vact": "",
        "Vpss": "",
        "Xabe": "",
        "Xabl": "",
        "Xade": "",
        "Xall": "",
        "Xcom": "",
        "Xela": "",
        "Xess": "", 
        "Xgen": "",
        "Xill": "", 
        "Xine": "",
        "Xins": "",
        "Xnom": "",
        "Xpar": "", 
        "Xtra": "", 
        "Xlat": "",
        "Xacc": "",
        "X???": "",
        "NOUN": "% NOUN",
        "ADJECTIVE": "% ADJ", "QUALIFIER": "% ADJ",
        "VERB": "% VERB",
        "ADVERB": "% ADV",
        "INTERJECTION": "% X",
        "PRONOUN": "% PRON",
        "PARTICLE": "% PRT",
        "NUMERAL": "% NUM",
        "ADPOSITION": "% ADP",
        "CONJUNCTION": "% CONJ", "COORDINATING": "", "ADVERBIAL": "",
        "COMPARATIVE": "",
        "ABBREVIATION": "% PRT", "ACRONYM": "% NOUN",
        "PROPER": "",
        "CARDINAL": "", "ORDINAL": "",
        "DEMONSTRATIVE": "", "QUANTOR": "", "PERSONAL": "",
        "INDEFINITE": "", "INTERROGATIVE": "",
        "REFLEXIVE": "", "RELATIVE": "",
        "RECIPROCAL": "",
        "PL1": "", 
        "PL2": "",
        "PL3": "",
        "SG1": "", 
        "SG2": "",
        "SG3": "",
        "PE4": "",
        "COMP": "",
        "SUPERL": "",
        "UNSPECIFIED": "% X",
        "PUNCTUATION": "% .",
        "DASH": "",
        "SPACE": "",
        "CLAUSE-BOUNDARY": "",
        "SENTENCE-BOUNDARY": "",
        "INITIAL-QUOTE": "",
        "FINAL-QUOTE": "",
        "INITIAL-BRACKET": "",
        "FINAL-BRACKET": "",
        "LEMMA-START": "",
        "": ""
        }

def format_copyright_lexc():
    return """
! This automatically generated lexc data is originated from omorfi database.
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

def format_lexc(wordmap, format):
    if format.startswith("omor"):
        return format_lexc_omor(wordmap, format)
    elif format.startswith("ftb3"):
        return format_lexc_ftb3(wordmap, format)
    elif format.startswith("apertium"):
        return format_lexc_apertium(wordmap)
    elif format.startswith("google"):
        return format_lexc_google(wordmap)
    elif format.startswith("generic"):
        return format_lexc_generic(wordmap)
    else:
        print("missing format", format, file=stderr)

def format_continuation_lexc(fields, format):
    stuffs = ""
    for cont in fields[3:]:
        if format.startswith("omor"):
            stuffs += format_continuation_lexc_omor(fields[1], fields[2], cont, format)
        elif format.startswith("ftb3"):
            stuffs += format_continuation_lexc_ftb3(fields[1], fields[2], cont)
        elif format.startswith("google"):
            stuffs += format_continuation_lexc_google(fields[1], fields[2], cont)
        elif format.startswith("generic"):
            stuffs += format_continuation_lexc_generic(fields[1], fields[2], cont)
        elif format.startswith("apertium"):
            stuffs += format_continuation_lexc_apertium(fields[1], fields[2], cont)
        else:
            print("missing format", format, file=stderr)
    return stuffs

def format_analysis_lexc(analyses, format):
    stuffs = ''
    if format.startswith("omor"):
        stuffs += format_analysis_lexc_omor(analyses, format)
    elif format.startswith("ftb3"):
        stuffs += format_analysis_lexc_ftb3(analyses)
    elif format.startswith("google"):
        stuffs += format_analysis_lexc_google(analyses)
    elif format.startswith("apertium"):
        stuffs += format_analysis_lexc_apertium(analyses)
    elif format.startswith("generic"):
        stuffs += format_analysis_lexc_generic(analyses)
    else:
        print("missing format", format, file=stderr)
        exit(1)
    return stuffs

def format_tag(stuff, format):
    if format.startswith('omor'):
        return format_tag_omor(stuff, format)
    elif format.startswith('ftb3'):
        return format_tag_ftb3(stuff)
    elif format.startswith('google'):
        return format_tag_google(stuff)
    elif format.startswith('generic'):
        return ''
    elif format.startswith('apertium'):
        return format_tag_apertium(stuff)
    else:
        print("Wrong format for generic tag formatting:", format, file=stderr)
        exit(1)


def format_tag_google(stuff):
    if stuff == '0':
        return "0"
    elif stuff in stuff2google:
        return stuff2google[stuff]
    else:
        print("Missing from google mapping: ", stuff, file=stderr)
        return ""

def format_analysis_lexc_google(anals):
    googstring = ''
    for tag in anals.split('|'):
        googstring += format_tag_google(tag)
    return googstring

def format_analysis_generic(anals):
    return ''


def format_continuation_lexc_google(anals, surf, cont):
    ftbstring = format_analysis_lexc_google(anals)
    if 'COMPOUND' in cont:
        ftbstring =  surf.replace(morph_boundary, '').replace(deriv_boundary, '')
    if surf != '0':
        surf = lexc_escape(surf)
    return "%s:%s\t%s ;\n" %(ftbstring, surf, cont)


def format_continuation_lexc_generic(anals, surf, cont):
    surf = lexc_escape(surf)
    return "%s:%s\t%s ; \n" %(surf.replace(optional_hyphen, word_boundary),
            surf, cont)


def format_lexc_google(wordmap):
    '''
    format string for canonical google universal pos format for morphological analysis
    '''
    if wordmap['stub'] == ' ':
        # do not include normal white space for now
        return ""
    wordmap['stub'] = lexc_escape(wordmap['stub'])
    wordmap['analysis'] = "%s" %(lexc_escape(wordmap['bracketstub'].replace(word_boundary, '#')  + '←<Del>'))
    wordmap['analysis'] += format_tag_google(wordmap['pos'])
    if wordmap['particle']:
        for pclass in wordmap['particle'].split('|'):
            wordmap['analysis'] += format_tag_google(pclass)
    if wordmap['subcat']:
        for subcat in wordmap['subcat'].split('|'):
            wordmap['analysis'] += format_tag_google(subcat)
    if wordmap['is_proper']:
        wordmap['analysis'] += format_tag_google('PROPER')
    lex_stub = wordmap['stub']
    retvals = []
    for new_para in wordmap['new_paras']:
        retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, 
                new_para)]
    return "\n".join(retvals)

def format_lexc_generic(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['stub']) + '{STUB}'
    retvals = []
    lex_stub = lexc_escape(wordmap['stub'])
    for new_para in wordmap['new_paras']:
        retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, new_para)]
    return "\n".join(retvals)


def format_multichars_lexc(format):
    multichars = "Multichar_Symbols\n"
    if format.startswith("omor"):
        multichars += "!! OMOR set:\n"
        multichars += format_multichars_lexc_omor()
    elif format.startswith("ftb3"):
        multichars += format_multichars_lexc_ftb3()
    elif format.startswith("google"):
        multichars += "!! Google universal pos set:\n"
        for mcs in google_multichars:
            multichars += mcs + "\n"
    elif format.startswith("generic"):
        pass
    elif format.startswith("apertium"):
        multichars += format_multichars_lexc_apertium()
    else:
        print("missing format", format, file=stderr)
        exit(1)
    if "+ktnkav" in format:
        multichars += "!! KTNKAV set:\n"
        for mcs in ktnkav_multichars:
            multichars += mcs + "\n"
    if "+newparas" in format:
        multichars += """!! NEWPARA set:
[NEWPARA=
        """
    multichars += "!! Following specials exist in all versions of omorfi\n"
    for mcs in common_multichars:
        multichars += mcs + "\n"
    return multichars

def format_root_lexicon(format):
    root = "LEXICON Root\n"
    root += """!! ...
0   NOUN ;
0   ADJECTIVE ;
0   VERB    ;
0   NUMERAL ;
0   DIGITS ;
0   ACRONYM ;
0   PRONOUN    ;
0   PARTICLE    ;
0   INTERJECTION ;
0   PUNCTUATION ;
0   CONJUNCTIONVERB ;
"""
    if format != 'generic':
        root += format_tag('B→', format) + ':-   NOUN ;\n'
        root += format_tag('B→', format) + ':-   ADJECTIVE ;\n'
        root += format_tag('B→', format) + ':-   SUFFIX ;\n'
    root += version_id_easter_egg + ':0 # ;\n'
    if '+taggerhacks' in format:
        root += "0   TAGGER_HACKS    ;\n"
    return root

def format_xml_kotus_sanalista(wordmap):
    kotus_xml = '    <st><s>' + wordmap['lemma'] + '</s>'
    kotus_xml += '<t>'
    if wordmap['kotus_tn'] != '0':
        kotus_xml += '<tn>' + wordmap['kotus_tn'] + '</tn>'
    if wordmap['kotus_av'] and wordmap['kotus_av'] != 'False':
        kotus_xml += '<av>' + wordmap['kotus_av'] + '</av>'
    kotus_xml += '</t></st>'
    return kotus_xml

def make_xmlid(s):
    return s.replace("?", "_UNK").replace("→", "_right").replace("←", "left").replace(".", "_")

def format_multichars_lexc_xml():
    multichars = "  <Multichar_Symbols>\n"
    for key, value in stuff2ftb3.items():
        key = make_xmlid(key)
        if key != '':
            if value != '':
                multichars += "    <mcs id='" + key + "'>" + xml_escape(value) + "</mcs>\n"
            else:
                multichars += "    <mcs id='" + key + "'>" + key + "</mcs>\n"
        else:
            pass

    multichars += """<!-- Following specials exist in all versions of omorfi -->
    <mcs id="hyph">{hyph?}</mcs> 
    <mcs id="deriv">»</mcs>
    <mcs id="infl">&gt;</mcs>
    <mcs id="wb">|</mcs>
    """
    multichars += "    <mcs id='VERSION'>" + version_id_easter_egg + '</mcs>\n'
    multichars += "  </Multichar_Symbols>"
    return multichars

def format_root_lexicon_xml():
    root = '  <LEXICON id="Root">\n'
    root += """<!-- ... -->
    <e><a/><i/><cont lexica="NOUNS ADJECTIVES VERBS NUMERALS DIGITSS ACRONYMS PRONOUNS PARTICLES PUNCTUATIONS FIFTYONE"/></e>
"""
    root += '    <e><a><s mcs="B_right"/></a><i>-</i><cont lexica="NOUN ADJECTIVE SUFFIX"/></e>\n'
    root += '    <e><a><s mcs="VERSION"/></a><i/><cont lexica="_end"/></e>\n'
    root += '  </LEXICON>\n'
    return root

def format_lexc_xml(wordmap):
    analysis = xml_escape(wordmap['lemma'])
    analysis = analysis.replace('|', '<s mcs="wb"/>').replace('_', '<s mcs="mb"/>')
    analysis += '<s mcs="' + wordmap['pos'] + '"/>'
    if wordmap['is_proper']:
        analysis += '<s mcs="proper"/>'
    if wordmap['is_suffix']:
        analysis = "<s mcs='suffix'/>" + analysis
    if wordmap['is_prefix']:
        analysis += "<s mcs='prefix'/>"
    stub = xml_escape(wordmap['stub'])
    stub = stub.replace('|', '<s mcs="wb"/>').replace('_', '<s mcs="mb"/>')
    return ('    <e><a>%s</a><i>%s</i><cont lexica="%s"/></e>' % 
            (analysis, stub, " ".join(wordmap['new_paras'])))

def format_continuation_lexicon_xml(tsvparts):
    xmlstring = '    <e>'
    if tsvparts[1] != '':
        xmlstring += '<a>'
        for anal in tsvparts[1].split('|'):
            if anal in stuff2ftb3:
                anal = make_xmlid(anal)
                xmlstring += '<s mcs="' + anal + '"/>'
            else:
                xmlstring += xml_escape(anal)
        xmlstring += '</a>'
    else:
        xmlstring += '<a/>'
    xmlstring += "<i>" + xml_escape(tsvparts[2]) + "</i>"
    xmlstring += '<cont lexica="' + " ".join(tsvparts[3:]).replace("#", "_END") + '"/></e>\n'
    return xmlstring

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
    elif ruleset.startswith('uppercase'):
        twolcstring += '! Set of Finnish alphabets generated from python:\n'
        for c in fin_lowercase:
            twolcstring += c + '! allow lowercase as is\n'
            twolcstring += c + ':' + c.upper() + '! allow uppercasing\n'
        for c in fin_uppercase:
            twolcstring += c + '! allow uppercase as is\n'
    elif ruleset == 'hyphenate':
        twolcstring += ' '.join(fin_lowercase) + '! lower'
        twolcstring += ' '.join(fin_uppercase) + '! upper'
    for mcs in common_multichars:
        if ruleset == 'hyphens' and mcs == optional_hyphen:
            twolcstring += twolc_escape(mcs) + ':0  ! boundary can be zero\n'
            twolcstring += twolc_escape(mcs) + ':%- ! or (ASCII) hyphen\n'
        elif ruleset == 'hyphenate':
            twolcstring += twolc_escape(mcs) + ':0 ! deleting all specials\n'
        else:
            twolcstring += twolc_escape(mcs) + '\n'
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
    return twolcstring

def format_rules_regex(format, ruleset):
    regexstring = ''
    if ruleset == 'orthographic-variations':
        regexstring += '[ '
        for p in fin_orth_pairs:
            regexstring += twolc_escape(p[0]) + ':' + twolc_escape(p[1]) + \
                    ' | '
        regexstring += '? ]* ;'
    elif ruleset == 'zh':
        regexstring += '[ ž | ž:z 0:h | ž:z::1 ] ;'
    elif ruleset == 'sh':
        regexstring += '[ š | š:s 0:h | š:s::1 ] ;'
    elif ruleset == 'rewrite-tags':
        if format == 'ftb3':
            regexstring += '# Remove before compounds:\n'
            regexstring += '[ '
            regexstring += ' -> 0, '.join([format_tag(tag, format) for tag in \
                    ['ADJECTIVE', 'NOUN', 'VERB', 'ACRONYM', 'ABBREVIATION', 'NUMERAL', 'PROPER', 'DIGIT', 'Xnom', 'Xpar', 'Xgen', 'Xine', 'Xela', 'Xill', 'Xade', 'Xabl', 'Xall', 'Xess', 'Xins', 'Xabe', 'Xtra', 'Xcom', 'Nsg', 'Npl']])
            regexstring += '-> 0 || _ ?* %# ]\n'
            regexstring += '.o.\n'
            regexstring += '# Remove V before Prc\n'
            regexstring += '[ ' + format_tag('VERB', format) + ' -> 0 || _  [ '
            regexstring += ' | '.join([format_tag(tag, format) for tag in \
                    ['Cma', 'Cmaisilla', 'Cnut', 'Cva', 'Cmaton', 'Dma','Dnut', 'Dtu', 'Dtava']])
            regexstring += '] ]\n'
            regexstring += '.o.\n'
            regexstring += '# ftb3.1 all pr are optional po\n'
            regexstring += '[ ' + format_tag('ADPOSITION', format) + ' (->) ' +\
                            format_tag('PREPOSITION', format) \
                            + ']\n'
            regexstring += '.o.\n'
            regexstring += '# stem mangling rules:\n'
            regexstring += '[ %<Del%>→ [ ' + ' | '.join(fin_lowercase) + \
                    ' ]* ←%<Del%> -> 0 || _ [ ? - %#]* %# ]\n'
            regexstring += '.o.\n'
            regexstring += '[ ←%<Del%> -> 0, %<Del%>→ -> 0 ]\n'
            regexstring += '.o.\n'
            regexstring += '[ ' + ' | '.join(fin_lowercase) + ']* -> 0 || ' +\
                    '[ ' + format_tag('NOUN', format) + \
                    format_tag('NUMERAL', format) + \
                    ']+ [? - %#]* _ [? - %#]*\n'
            regexstring += '.o.\n'
            regexstring += '# Puncts without nom case\n'
            regexstring += '[ ' + format_tag('Xnom', format) +\
                    ' ' + format_tag('Nsg', format) + ' ] -> 0 || ' +\
                    format_tag('PUNCTUATION', format) + ' _ \n'
            regexstring += '.o.\n'
            regexstring += '# random puncts are abbr\n'
            regexstring += format_tag('PUNCTUATION', format) +\
                    ' (->) ' + format_tag('ABBREVIATION', format) +\
                    ' ' + format_tag('Xnom', format) +\
                    ' ' + format_tag('Nsg', format) +\
                    '|| _ '
            regexstring += ';\n'
    elif ruleset == 'remove-boundaries':
        regexstring += ' -> 0, '.join([twolc_escape(tag) for tag in \
                    [word_boundary, deriv_boundary, morph_boundary,\
                    stub_boundary, weak_boundary]]) + '-> 0 || _ ;'
    elif ruleset == 'token':
        regexstring += '[ [' + '|'.join(fin_lowercase) + '|' +\
                '|'.join(fin_uppercase) + \
                '| ’ | %\' | %- | %0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 ]*'\
                ' | ? ] ;'
    elif ruleset == 'between-tokens':
        regexstring += '[ %. | %, | %: | %; | %? | %! | %- | %  ] ;'
    else:
        print("Unknown ruleset", ruleset)
        return None
    return regexstring

