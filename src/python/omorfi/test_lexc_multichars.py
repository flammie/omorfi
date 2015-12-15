#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unit test to check if Lexc multichar symbol declarations match."""

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

import unittest

from .omor_formatter import omor_multichars, stuff2omor

class LexcMulticharsTest(unittest.TestCase):
    def test_omor():
        for stuff, omor in stuff2omor.items():
            if len(omor) < 2:
                continue
            assertIn(omor, omor_multichars)


