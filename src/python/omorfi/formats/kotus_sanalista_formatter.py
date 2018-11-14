#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to format kotus sanalista XML from omorfi data."""

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


def format_wordmap_kotus_sanalista(wordmap):
    kotus_xml = '    <st><s>' + wordmap['lemma'] + '</s>'
    if wordmap['homonym'] != '0':
        kotus_xml += '<hn>' + wordmap['homonym'] + '<hn>'
    kotus_xml += '<t>'
    if wordmap['kotus_tn'] != '0':
        kotus_xml += '<tn>' + wordmap['kotus_tn'] + '</tn>'
    else:
        kotus_xml += '<tn>99</tn>'
    if wordmap['kotus_av'] and wordmap['kotus_av'] != 'False':
        kotus_xml += '<av>' + wordmap['kotus_av'] + '</av>'
    kotus_xml += '</t></st>'
    return kotus_xml
