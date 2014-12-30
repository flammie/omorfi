#!/usr/bin/env python3

# functions for formatting the database data to lexc

from omorfi_settings import common_multichars, version_id_easter_egg, \
        optional_hyphen, word_boundary

def lexc_escape(s):
    '''Escape symbols that have special meaning in lexc.'''
    s = s.replace("%", "__PERCENT__")
    s = s.replace(" ", "% ")
    s = s.replace("<", "%<")
    s = s.replace(">", "%>")
    s = s.replace("0", "%0")
    s = s.replace("!", "%!")
    s = s.replace(":", "%:")
    s = s.replace('"', '%"')
    s = s.replace(";", "%;")
    s = s.replace("__PERCENT__", "%%")
    return s


def format_copyright_lexc():
    return """
! This automatically generated lexc data is originated from 
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



from apertium_formatter import format_stuff_apertium, \
        format_analysis_lexc_apertium, format_continuation_lexc_apertium, \
        format_wordmap_lexc_apertium, format_multichars_lexc_apertium
from ftb3_formatter import format_stuff_ftb3, \
        format_analysis_lexc_ftb3, format_continuation_lexc_ftb3, \
        format_wordmap_lexc_ftb3, format_multichars_lexc_ftb3
from omor_formatter import format_stuff_omor, \
        format_analysis_lexc_omor, format_continuation_lexc_omor, \
        format_wordmap_lexc_omor, format_multichars_lexc_omor

def format_stuff(stuff, format):
    if format.startswith('omor'):
        return format_stuff_omor(stuff, format)
    elif format.startswith('ftb3'):
        return format_stuff_ftb3(stuff)
    elif format.startswith('google'):
        return format_stuff_google(stuff)
    elif format.startswith('generic'):
        return ''
    elif format.startswith('apertium'):
        return format_stuff_apertium(stuff)
    else:
        print("Wrong format for generic stuff formatting:", format,
                file=stderr)
        exit(1)

def format_wordmap_lexc(wordmap, format):
    if format.startswith("omor"):
        return format_wordmap_lexc_omor(wordmap, format)
    elif format.startswith("ftb3"):
        return format_wordmap_lexc_ftb3(wordmap, format)
    elif format.startswith("apertium"):
        return format_wordmap_lexc_apertium(wordmap)
    elif format.startswith("google"):
        return format_wordmap_lexc_google(wordmap)
    elif format.startswith("generic"):
        return format_wordmap_lexc_generic(wordmap)
    else:
        print("Wrong format for generic stuff formatting:", format,
                file=stderr)
        exit(1)

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

def format_root_lexicon_lexc(format):
    root = "LEXICON Root\n"
    root += """!! LEXICONS per class
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
        root += "!! LEXICONS that can be co-ordinated hyphen -compounds\n"
        root += format_stuff('B→', format) + ':-   NOUN ;\n'
        root += format_stuff('B→', format) + ':-   ADJECTIVE ;\n'
        root += format_stuff('B→', format) + ':-   SUFFIX ;\n'
    root += version_id_easter_egg + ':0 # ;\n'
    if '+taggerhacks' in format:
        root += "0   TAGGER_HACKS    ;\n"
    return root

# generics
def format_continuation_lexc_generic(anals, surf, cont):
    surf = lexc_escape(surf)
    return "%s:%s\t%s ; \n" %(surf.replace(optional_hyphen, word_boundary),
            surf, cont)


def format_wordmap_lexc_generic(wordmap):
    wordmap['analysis'] = lexc_escape(wordmap['stub']) + '{STUB}'
    retvals = []
    lex_stub = lexc_escape(wordmap['stub'])
    retvals += ["%s:%s\t%s\t;" %(wordmap['analysis'], lex_stub, wordmap['new_para'])]
    return "\n".join(retvals)

