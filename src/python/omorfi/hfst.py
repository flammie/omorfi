#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
HFST utils.
"""

import pyhfst


def load_hfst(f):
    """Load an HFST language model from file, with some error handling.

    Args:
        f:  containing single hfst automaton binary.

    Throws:
        FileNotFoundError if file is not found
    """
    his = pyhfst.HfstInputStream(f)
    return his.read()
