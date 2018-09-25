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
        # ± tokens = stuff
        self.context = None
        # when 0 is also
        self.dispute = None
        # dep to add
        self.depname = None
        # from:
        # ~inf: quasi-always (grammatical, CG style) to
        # 1.0: weak evidence, last resort tie break
        self.likelihood = 1.0

    def matches(self, token: Token, sentence: list):
        '''If suggestion applies to token in context.'''
        return False

    def apply(self, token: Token, sentence: list):
        '''Draw an arc and redistribute some weights.'''
        return


def linguisticate(sentence: list):
    '''Not a parsing function.'''
    #
    rules = list()
    for token in sentence:
        for rule in rules:
            if rule.matches(token, sentence):
                rule.apply(token, sentence)


def main():
    """Invoke a simple CLI analyser."""
    exit(0)


if __name__ == "__main__":
    main()
