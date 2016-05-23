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

from .apertium_formatter import ApertiumFormatter
from .ftb3_formatter import Ftb3Formatter
from .giella_formatter import GiellaFormatter
from .no_tags_formatter import NoTagsFormatter
from .omor_formatter import OmorFormatter


class LexcMulticharsTest(unittest.TestCase):
    """Unit tests for Lexc multichars compatibility of formatters."""
    def test_multichars():
        formatter = OmorFormatter(False)
        formatter.format_multichars_lexc()
        formatter = ApertiumFormatter(False)
        formatter.format_multichars_lexc()
        formatter = Ftb3Formatter(False)
        formatter.format_multichars_lexc()
        formatter = GiellaFormatter(False)
        formatter.format_multichars_lexc()
        formatter = NoTagsFormatter(False)
        formatter.format_multichars_lexc()
