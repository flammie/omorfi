#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to format LMF compatible XML from omorfi data."""

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

from xml.sax.saxutils import escape as xml_escape

from ftb3_formatter import Ftb3Formatter

from .settings import version_id_easter_egg


def make_xmlid(s):
    return s.replace("?", "_UNK").replace("→", "_right").replace("←", "left").replace(".", "_")


def format_multichars_lexc_xml():
    multichars = "  <Multichar_Symbols>\n"
    for key, value in Ftb3Formatter.stuff2ftb3.items():
        key = make_xmlid(key)
        if key != '':
            if value != '':
                multichars += "    <mcs id='" + key + \
                    "'>" + xml_escape(value) + "</mcs>\n"
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
    analysis = analysis.replace(
        '|', '<s mcs="wb"/>').replace('_', '<s mcs="mb"/>')
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
            (analysis, stub, wordmap['new_para']))


def format_continuation_lexicon_xml(tsvparts):
    xmlstring = '    <e>'
    if tsvparts[1] != '':
        xmlstring += '<a>'
        for anal in tsvparts[1].split('|'):
            if anal in Ftb3Formatter.stuff2ftb3:
                anal = make_xmlid(anal)
                xmlstring += '<s mcs="' + anal + '"/>'
            else:
                xmlstring += xml_escape(anal)
        xmlstring += '</a>'
    else:
        xmlstring += '<a/>'
    xmlstring += "<i>" + xml_escape(tsvparts[2]) + "</i>"
    xmlstring += '<cont lexica="' + \
        " ".join(tsvparts[3:]).replace("#", "_END") + '"/></e>\n'
    return xmlstring
