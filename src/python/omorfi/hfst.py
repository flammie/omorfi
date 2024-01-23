#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
HFST utils.
"""

import hfst


def load_hfst(f):
    """Load an HFST language model from file, with some error handling.

    Args:
        f:  containing single hfst automaton binary.

    Throws:
        FileNotFoundError if file is not found
    """
    try:
        his = hfst.HfstInputStream(f)
        return his.read()
    except hfst.exceptions.NotTransducerStreamException:
        raise IOError(2, f) from None
