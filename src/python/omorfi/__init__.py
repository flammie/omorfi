#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Omorfi API for python."""

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


__all__ = ["Omorfi", "Token"]

__version__ = "0.9.9"
__author__ = "Omorfi contributors"
__author_email__ = "omorfi-development@googlegroups.com"

import os
from .omorfi import Omorfi
from .token import Token


def load(filename: str) -> Omorfi:
    """Load omorfi analyser with specified FSA language model.

    This convenience function is provided as a generic fast entry point to
    omorfi python API. For further details, see the Omorfi class.

    Args:
        filename:  filename and path as string

    Returns:
        omorfi object, ready for analysis functions.
    """
    omorfi = Omorfi()
    omorfi.load_analyser(filename)
    return omorfi


def find_omorfi(large_coverage=False) -> str:
    """Search the usual paths for omorfi FSA language models.

    Returns first located filename in one of the typical omorfi installation
    paths or the current working directory, or omorfi source directory if it
    is relative to cwd.

    Args:
        large_coverage  set to true for loading large coverage language model

    Returns:
        string containing path of a file containing omorfi FSA language model.

    See also:
        http://flammie.github.io/omorfi/smaller-lexicons.html
    """
    dirs = ["/usr/local/share/omorfi/", "/usr/share/omorfi/"]
    if os.getenv("HOME"):
        dirs += [os.getenv("HOME") + "/.local/omorfi/"]
    if os.getcwd():
        cwd = os.getcwd()
        dirs += [cwd + "/src/generated/", cwd + "/generated/", cwd + "/"]
    for d in dirs:
        if large_coverage:
            filename = d + "/" + "omorfi.describe.hfst"
        else:
            filename = d + "/" + "omorfi.analyse.hfst"
        if os.path.isfile(filename):
            return filename
    raise FileNotFoundError()


if __name__ == "__main__":
    pass
