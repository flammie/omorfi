#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Neat error handling for omorfi scripts"""

# Author: Tommi A Pirinen <flammie@iki.fi> 2015

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

from sys import stderr


def fail_formatting_missing_for(stuff, format, moar=None):
    print("\033[93mMissing tag!\033[0m Trying to format:", stuff, "for tagset:",
          format, file=stderr)
    if moar:
        print("\033[92mExplanation\033[0m:", moar, file=stderr)


def fail_guess_because(wordmap, matches, failures, moar=None):
    print("\033[93mUnguessable!\033[0m Following has been seen:", matches,
          "\nfollowing was tested and failed:", failures,
          "\nwhen trying: (",
          wordmap['lemma'], wordmap['pos'],
          wordmap['kotus_tn'], wordmap['kotus_av'],
          wordmap['harmony'], ")", file=stderr)
    if moar:
        print("\033[92mExplanation\033[0m:", moar, file=stderr)
    # This can be used to automate classifying plurales etc.
    # if wordmap['lemma'].endswith('t'):
    # if wordmap['is_proper']:
    #    print(wordmap['lemma'], wordmap['kotus_tn'], wordmap['kotus_av'])


def just_fail(because, file=stderr):
    print("\033[93mError!\033[0m ", because, file=stderr)
