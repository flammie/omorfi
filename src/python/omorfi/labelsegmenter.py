#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Omorfi segmenter logic is contained in this class. Uses a HFST model
made for segmenting.
"""

from .token import Token
from .analysis import Analysis
from .hfst import load_hfst


class LabelSegmenter:

    """
    An object for omorfi’s segmentation.
    """

    def __init__(self):
        """Initialise empty labeller."""
        self.labelsegmenter = None

    def load_labeller(self, hfstfile: str):
        """Load analysis model from a file.

        Args
            f: containing single hfst automaton binary.
        """
        self.labelsegmenter = load_hfst(hfstfile)

    def _labelsegment(self, token: Token):
        '''Internal implementation of segment label lookup with FSA.

        Args:
            token: token to analyse

        Returns:
            list of new labelsegment analyses.'''
        res = self.labelsegmenter.lookup(token.surf)
        newlabels = list()
        for r in res:
            labelsegments = r[0]
            weight = float(r[1])
            anal = Analysis()
            anal.raw = labelsegments
            anal.weight = weight
            anal.rawtype = "labelsegments"
            newlabels.append(anal)
        for labels in newlabels:
            token.labelsegmentations.append(labels)
        return newlabels

    def labelsegment(self, token: Token):
        '''Segment token into labelled morphs, words and other string pieces.

        The segments are suffixed with their morphologically relevant
        informations, e.g. lexical classes for root lexemes and inflectional
        features for inflectional segments. This functionality is experimental
        due to hacky way it was patched together.

        Side-effect:
            Note that this operation stores the labelsegments in the token for
        future use, and only returns raw HFST structures. To get pythonic
        you can use Token's methods afterwards.

        Args:
            token: token to segment with labels

        Returns:
            New labeled segemntations in analysis list.
        '''
        labelsegments = None
        labelsegments = self._labelsegment(token)
        if not labelsegments or len(labelsegments) < 1:
            labelsegments = token.surf + "|UNK"
            lsweight = float("inf")
            guess = Analysis()
            guess. raw = labelsegments
            guess.weight = lsweight
            guess.rawtype = "labelsegments"
            guess.manglers.append("GUESSER=SURFISLABELS")
            token.labelsegmentations.append(guess)
            labelsegments = [guess]
        return labelsegments
