#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to format Xerox style regexes from omorfi data."""

# Author: Omorfi contributors <omorfi-devel@groups.google.com> 2015

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# utils to format xerox regexes from omor's lexical data sources.

from .settings import fin_orth_pairs, fin_lowercase, fin_uppercase, \
        word_boundary, deriv_boundary, morph_boundary, newword_boundary, \
        deriv_boundary, stub_boundary, weak_boundary, optional_hyphen
from .twolc_formatter import twolc_escape

def format_rules_regex(formatter, ruleset):
    regexstring = ''
    if ruleset == 'orthographic-variations':
        regexstring += '[ '
        for p in fin_orth_pairs:
            regexstring += twolc_escape(p[0]) + ':' + twolc_escape(p[1]) + \
                    ' | ' + twolc_escape(p[0]) + ' | '
        regexstring += '? ]* ;'
    elif ruleset == 'zh':
        regexstring += '[ ž | ž:z 0:h | ž:z::1 ] ;'
    elif ruleset == 'sh':
        regexstring += '[ š | š:s 0:h | š:s::1 ] ;'
    elif ruleset == 'rewrite-tags':
        if format == 'ftb3':
            regexstring += '# Remove before compounds:\n'
            regexstring += '[ '
            regexstring += ' -> 0,\n '.join([formatter.stuff2lexc(tag, format) for tag in \
                    ['ADJ', 'NOUN', 'VERB', 'ACRONYM', 'ABBREVIATION', 'NUM', 'PROPER', 'DIGIT', 'Xnom', 'Xpar', 'Xgen', 'Xine', 'Xela', 'Xill', 'Xade', 'Xabl', 'Xall', 'Xess', 'Xins', 'Xabe', 'Xtra', 'Xcom', 'Nsg', 'Npl']])
            regexstring += '-> 0 || _ ?* %# ]\n'
            regexstring += '.o.\n'
            regexstring += '# Remove V before Prc\n'
            regexstring += '[ ' + formatter.stuff2lexc('VERB', format) + ' -> 0 || _  [ '
            regexstring += ' | '.join([formatter.stuff2lexc(tag, format) for tag in \
                    ['Cma', 'Cmaisilla', 'Cnut', 'Cva', 'Cmaton', 'Dma','Dnut', 'Dtu', 'Dva', 'Dtava']])
            regexstring += '] ]\n'
            regexstring += '.o.\n'
            regexstring += '# ftb3.1 all pr are optional po\n'
            regexstring += '[ ' + formatter.stuff2lexc('ADP', format) + ' (->) ' +\
                            formatter.stuff2lexc('PREPOSITION', format) \
                            + ']\n'
            regexstring += '.o.\n'
            regexstring += '# stem mangling rules:\n'
            regexstring += '[ %<Del%>→ [ ' + ' | '.join(fin_lowercase) + \
                    ' ]* ←%<Del%> -> 0 || _ [ ? - %#]* %# ]\n'
            regexstring += '.o.\n'
            regexstring += '[ ←%<Del%> -> 0, %<Del%>→ -> 0 ]\n'
            regexstring += '.o.\n'
            regexstring += '[ ' + ' | '.join(fin_lowercase) + ']* -> 0 || ' +\
                    '[ ' + formatter.stuff2lexc('NOUN', format) + \
                    ' | ' + formatter.stuff2lexc('NUM', format) + \
                    '] [? - %#]* _ [? - %#]* .#. \n'
            regexstring += '.o.\n'
            regexstring += '# Puncts without nom case\n'
            regexstring += '[ ' + formatter.stuff2lexc('Xnom', format) +\
                    ' ' + formatter.stuff2lexc('Nsg', format) + ' ] -> 0 || ' +\
                    formatter.stuff2lexc('PUNCTUATION', format) + ' _ \n'
            regexstring += '.o.\n'
            regexstring += '# random puncts are abbr\n'
            regexstring += formatter.stuff2lexc('PUNCTUATION', format) +\
                    ' (->) ' + formatter.stuff2lexc('ABBREVIATION', format) +\
                    ' || _ '
            regexstring += '.o.\n'
            regexstring += '# abbrs are nom sg’s too\n' 
            regexstring += formatter.stuff2lexc('ABBREVIATION', format) +\
                    ' (->) ' + formatter.stuff2lexc('ABBREVIATION', format) +\
                    ' ' + formatter.stuff2lexc('Xnom', format) +\
                    ' ' + formatter.stuff2lexc('Nsg', format) +\
                    ' || _ '
            regexstring += '.o.\n'
            regexstring += '# suffixes unmarked why of course\n'
            regexstring += '%# %- -> %# || _ \n'
            regexstring += '.o.\n'
            regexstring += '# FTB is a bit silly with dashes\n'
            regexstring += '% Dash -> % EmDash || — ?* _ \n'
            regexstring += '.o.\n'
            regexstring += '% Dash -> % EnDash || – ?* _ \n'
            regexstring += ';\n'
    elif ruleset == 'lemmatise':
        if format == 'ftb3':
            regexstring += '# Remove everything:\n'
            regexstring += '[ '
            regexstring += ' -> 0,\n'.join([formatter.stuff2lexc(tag, format) for tag in \
                    ['ADJ', 'NOUN', 'VERB', 'ACRONYM', 'ABBREVIATION', 'NUM', 'PROPER', 'DIGIT', 'COORDINATING', 'ADVERBIAL', 'ORDINAL', 'DEMONSTRATIVE', 'PERSONAL', 'INDEFINITE', 'QUANTOR', 'INTERROGATIVE', 'REFLEXIVE', 'RELATIVE', 'PUNCTUATION', 'DASH', 'ROMAN', 'PL1', 'PL2', 'PL3', 'SG1', 'SG2', 'SG3', 'PE4', 'COMP', 'SUPERL', 'UNSPECIFIED', 'PRON', 'INTJ',
                        'Xnom', 'Xpar', 'Xgen', 'Xine', 'Xela', 'Xill',
                        'Xade', 'Xabl', 'Xall', 'Xess', 'Xins', 'Xabe',
                        'Xtra', 'Xcom', 'Nsg', 'Npl',
                        'Osg1', 'Osg2', 'O3', 'Opl1', 'Opl2',
                        'Qka', 'Qs', 'Qpa', 'Qko', 'Qkin', 'Qkaan', 'Qhan',
                        'Vact', 'Vpss',
                        'Ncon', 'Nneg', 'Dnut', 'Dtu', 'Dva', 'Dtava',
                        'Ia', 'Ie', 'Ima',
                        'Tcond', 'Timp', 'Tpast', 'Tpot', 'Tpres', 'Topt'] if formatter.stuff2lexc(tag, format)])
            regexstring += '-> 0 || _ ] ;\n'
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
    elif ruleset == 'token-separator':
        regexstring += '0:"\\n" ;'
    else:
        print("Unknown ruleset", ruleset)
        return None
    return regexstring

