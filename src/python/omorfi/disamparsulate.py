#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Beta-testing a wack idea of not disambiguating and dependency parsing at the
same time. Pay no attention to the man behind the curtains and move along.
"""

from .token import Token


class Suggestion:
    """Not a rule."""

    def __init__(self):
        self.name = "Unnamed"
        self.target = None
        # ± tokens = stuff
        self.context = None
        # barrier for * contexts
        self,barrier = None
        # when 0 is also
        self.dispute = None
        # dep to add
        self.depname = None
        # from:
        # -inf: quasi-always (grammatical, CG style SELECT) to
        # -1.0: weak evidence, last resort tie break
        # 1.0: unlikely
        # inf: nearly never (ungrammatical, CG REMOVE)
        self.unlikelihood = -1.0

    def apply(self, token: Token, sentence: list):
        '''If suggestion applies to token in context.'''
        for analysis in token.analyses:
            matched = True
            if "ufeats" in self.target:
                for feat, value in self.target["ufeats"].items():
                    if feat not in analysis.ufeats:
                        matched = False
                        break
                    elif analysis.ufeats[feat] != value:
                        matched = False
                        break
                if not matched:
                    continue
            if self.context:
                head = self.find_context(token, sentence)
                if not head:
                    matched = False
                    continue
            if matched:
                if self.unlikelihood > 0:
                    analysis.weight += self.unlikelihood
                elif self.unlikelihood < 0:
                    for b in token.analyses:
                        if b != analysis:
                            b.weight += self.unlikelihood
                if head and self.dep:
                    analysis.ud = head


def linguisticate(sentence: list):
    '''Not a parsing function.'''
    #
    rules = list()
    insrule = Suggestion()
    insrule.name = "instructives unlikely"
    insrule.target = {"ufeats": {"Case": "Ins"}}
    insrule.unlikelihood = 16.0
    for token in sentence:
        for rule in rules:
            rule.apply(token, sentence)


def main():
    """Invoke a simple CLI analyser."""
    exit(0)


if __name__ == "__main__":
    main()
