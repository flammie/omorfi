#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Beta-testing a wack idea of not disambiguating and dependency parsing at the
same time. Pay no attention to the man behind the curtains and move along.
"""

from ..analysis import Analysis


class Matcher:
    """Something to match some things."""

    def __init__(self):
        self.uposes = list()
        self.ufeatses = list()
        self.lemmas = list()

    def matches(self, analysis: Analysis):
        """Checks if token matches given params."""
        if self.lemmas:
            found = False
            for lemma in self.lemmas:
                if '#'.join(analysis.lemmas) == lemma:
                    found = True
                    break
            if not found:
                return False
        if self.uposes:
            found = False
            for upos in self.uposes:
                if analysis.upos == upos:
                    found = True
                    break
            if not found:
                return False
        if self.ufeatses:
            foundany = False
            for ufeats in self.ufeatses:
                foundall = True
                for feat, value in ufeats.items():
                    if feat not in analysis.ufeats:
                        foundall = False
                        break
                    elif analysis.ufeats[feat] != value:
                        foundall = False
                        break
                if foundall:
                    foundany = True
                    break
            if not foundany:
                return False
        return True
