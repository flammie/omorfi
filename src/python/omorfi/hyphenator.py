#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Omorfi hyphenateer logic is contained in this class. Uses a HFST model
made for hyphenateing.
"""

from .token import Token
from .analysis import Analysis
from .hfst import load_hfst


class Hyphenator:

    """
    An object for omorfi’s hyphenateation.
    """

    def __init__(self, hfstfile: str):
        """Load analysis model from a file.

        Args
            f: containing single hfst automaton binary.
        """
        self.hyphenator = load_hfst(hfstfile)

    def _hyphenate(self, token: Token):
        '''Intenal hyphenateing using HFST automaton.

        Args:
            token: token to hyphenate.'''
        res = self.hyphenator.lookup(token.surf)
        newsegs = list()
        for r in res:
            hyphens = r[0]
            weight = float(r[1])
            anal = Analysis()
            anal.raw = hyphens
            anal.weight = weight
            anal.rawtype = "hyphens"
            newsegs.append(anal)
        for hyphen in newsegs:
            token.hyphenations.append(hyphen)
        return newsegs

    def hyphenate(self, token: Token):
        '''Segment token into morphs, words and other string pieces.

        Side-effect:
            this operation stores hyphenates in the token for future
        use and only returns the HFST structures. To get pythonic data use
        Token's methods afterwards.

        Args:
            token: token to hyphenate

        Returns:
            New hyphenateations in analysis list
        '''
        hyphens = None
        hyphens = self._hyphenate(token)
        if not hyphens or len(hyphens) < 1:
            hyphenates = token.surf
            weight = float("inf")
            guess = Analysis()
            guess.raw = hyphenates
            guess.weight = weight
            guess.rawtype = "hyphenates"
            guess.manglers.append("GUESSER=SURFISSEGMENT")
            token.hyphenations.append(guess)
            hyphens = [guess]
        return hyphens
