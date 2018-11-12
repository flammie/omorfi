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
        self.agrs = dict()

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
                    elif self.is_ufeat_agreement(feat):
                        if feat in self.agrs and \
                                self.agrs[feat] != analysis.ufeats[feat]:
                            foundall = False
                            break
                        else:
                            # OK, set agreement elsewhere
                            pass
                    elif analysis.ufeats[feat] != value:
                        foundall = False
                        break
                if foundall:
                    foundany = True
                    break
            if not foundany:
                return False
        return True

    def is_ufeat_agreement(self, feat):
        for ufeats in self.ufeatses:
            if feat in ufeats:
                if ufeats[feat] == "*AGREEMENT*":
                    return True
        return False

    def get_agreement_ufeats(self, anal: Analysis):
        agrs = dict()
        if self.ufeatses:
            for ufeats in self.ufeatses:
                for feat, value in ufeats.items():
                    if self.is_ufeat_agreement(feat):
                        if feat in anal.ufeats:
                            agrs[feat] = anal.ufeats[feat]
                        else:
                            # cannot return agreement for missing feat
                            return None
        return agrs

    def __str__(self):
        s = '"omorfi.disamparsulate.Matcher: {'
        s += '"lemmas": [' + ', '.join(self.lemmas) + '], '
        s += '"uposes": [' + ', '.join(self.uposes) + '], '
        s += '"ufeatses": ['
        for ufeats in self.ufeatses:
            s += str(ufeats)
        s += "]"
        return s
