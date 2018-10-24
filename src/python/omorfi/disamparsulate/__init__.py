#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Omorfi internal API for some parsings."""

# Author: Tommi A Pirinen <flammie@iki.fi> 2018

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


__all__ = ['Disamparsulator', 'Evidence', 'Matcher']

__version__ = "2018"
__author__ = "Omorfi contributors"
__author_email__ = "omorfi-development@googlegroups.com"

from .disamparsulator import Disamparsulator
from .evidence import Evidence
from .matcher import Matcher

if __name__ == "__main__":
    pass
