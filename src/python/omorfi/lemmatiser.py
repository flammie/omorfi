#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Omorfi analyser logic is contained in this class. Uses the HFST model,
optionally udpipe and frequencies if they can be loaded.
"""

from .token import Token
from .analyser import Analyser
from .analysis import Analysis
from .hfst import load_hfst


class Lemmatiser:

    """
    An object for omorfi’s morphological analysis.
    """

    def __init__(self):
        """Load analysis model from a file.

        Args
            f: containing single hfst automaton binary.
        """
        self.lemmatiser = None
        self.analyser = None
        self.try_titlecase = True
        self.try_lowercase = True
        self.try_uppercase = True
        self.try_detitlecase = True

    def use_analyser(self, analyser: Analyser):
        self.analyser = analyser

    def load_lemmatiser(self, hfstfile: str):
        self.lemmatiser = load_hfst(hfstfile)

    def _lemmatise(self, token):
        if self.lemmatiser:
            res = self.lemmatiser.lookup(token.surf)
        else:
            res = self.analyser.analyse(token)
        newlemmas = list()
        for r in res:
            lemma = r[0]
            weight = float(r[1])
            anal = Analysis()
            anal.raw = lemma
            anal.rawtype = 'lemma'
            anal.weight = weight
            newlemmas.append(anal)
        for lemma in newlemmas:
            token.lemmatisations.append(lemma)
        return newlemmas

    def lemmatise(self, token: Token):
        lemmas = None
        lemmas = self._lemmatise(token)
        if not lemmas or len(lemmas) < 1:
            lemma = token.surf
            weight = float('inf')
            guess = Analysis()
            guess.raw = lemma
            guess.rawtype = 'lemma'
            guess.ewight = weight
            guess.manglers.append('GUESSER=SURFISLEMMA')
            token.lemmatisations.append(guess)
            lemmas = [guess]
        return lemmas
