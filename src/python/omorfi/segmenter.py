#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Omorfi segmenter logic is contained in this class. Uses a HFST model
made for segmenting.
"""

from .token import Token
from .analysis import Analysis
from .hfst import load_hfst


class Segmenter:

    """
    An object for omorfi’s segmentation.
    """

    def __init__(self):
        """Initialise empty segmenter."""
        self.segmenter = None

    def load_segmenter(self, hfstfile: str):
        """Load analysis model from a file.

        Args
            f: containing single hfst automaton binary.
        """
        self.segmenter = load_hfst(hfstfile)

    def _segment(self, token: Token):
        '''Intenal segmenting using HFST automaton.

        Args:
            token: token to segment.'''
        res = self.segmenter.lookup(token.surf)
        newsegs = list()
        for r in res:
            segments = r[0]
            weight = float(r[1])
            anal = Analysis()
            anal.raw = segments
            anal.weight = weight
            anal.rawtype = "segments"
            newsegs.append(anal)
        for segment in newsegs:
            token.segmentations.append(segment)
        return newsegs

    def segment(self, token: Token):
        '''Segment token into morphs, words and other string pieces.

        Side-effect:
            this operation stores segments in the token for future
        use and only returns the HFST structures. To get pythonic data use
        Token's methods afterwards.

        Args:
            token: token to segment

        Returns:
            New segmentations in analysis list
        '''
        segments = None
        segments = self._segment(token)
        if not segments or len(segments) < 1:
            segments = token.surf
            weight = float("inf")
            guess = Analysis()
            guess.raw = segments
            guess.weight = weight
            guess.rawtype = "segments"
            guess.manglers.append("GUESSER=SURFISSEGMENT")
            token.segmentations.append(guess)
            segments = [guess]
        return segments
