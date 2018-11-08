#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Beta-testing a wack idea of not disambiguating and dependency parsing at the
same time. Pay no attention to the man behind the curtains and move along.
"""

from copy import deepcopy
# stuff

from ..token import Token
from .matcher import Matcher


class Evidence:
    """Not a rule."""

    def __init__(self):
        """Create a new evidence matching pattern."""
        self.name = "Unnamed"
        self.target = Matcher()
        # ± tokens = stuff
        self.context = dict()
        # when 0 is also
        self.dispute = dict()
        # dep to add
        self.depname = dict()
        # from:
        # -inf: quasi-always (grammatical, CG style SELECT) to
        # -1.0: weak evidence, last resort tie break
        # 1.0: unlikely
        # inf: nearly never (ungrammatical, CG REMOVE)
        self.unlikelihood = -1.0

    def apply(self, token: Token, sentence: list):
        '''If suggestion applies to token in context.'''
        newdeps = list()
        depless = None
        for analysis in token.analyses:
            matched = True
            if not self.target.matches(analysis):
                matched = False
                continue
            else:
                agrs = self.target.get_agreement_ufeats(analysis)
                if 'matcher' in self.context:
                    self.context['matcher'].agrs = agrs
            heads = []
            if self.context:
                heads = self.find_context(token, sentence)
                if not heads:
                    matched = False
            if matched and "negated" not in self.context and not self.depname:
                if self.unlikelihood > 0:
                    analysis.weight += self.unlikelihood
                elif self.unlikelihood < 0:
                    for b in token.analyses:
                        if b != analysis:
                            b.weight -= self.unlikelihood
            if not matched and "negated" in self.context and not self.depname:
                if self.unlikelihood > 0:
                    analysis.weight += self.unlikelihood
                elif self.unlikelihood < 0:
                    for b in token.analyses:
                        if b != analysis:
                            b.weight -= self.unlikelihood
            if matched and heads:
                for head in heads:
                    # we actually want to copy analysis per head
                    distance = abs(token.pos - head['pos'])
                    if distance == 0:
                        distance = 1
                    if self.depname:
                        depless = analysis
                        newdep = deepcopy(analysis)
                        analysis.weight -= self.unlikelihood * distance * 0.1
                        newdep.udepname = self.depname
                        newdep.udeppos = head['pos']
                        newdeps.append(newdep)
                        for b in token.analyses:
                            if b != analysis and b.udepname != self.depname:
                                b.weight -= self.unlikelihood * distance * 0.1
                    # also reweight the head
                    for w in sentence:
                        if w.pos == head['pos']:
                            for a in w.analyses:
                                if a != head['a']:
                                    a.weight -= self.unlikelihood * \
                                        distance * 0.1
        # append new stuff at the end to avoid eterbnal loops
        for anal in newdeps:
            token.analyses.append(anal)
        if depless:
            token.analyses.remove(depless)

    def find_context(self, target: Token, sentence: list):
        '''Traverse sentence to find contexts that match.'''
        if self.context['location'] == 'ROOT':
            return [{"pos": 0, "a": None}]
        heads = list()
        for head in sentence:
            if self.in_context(target, sentence, head):
                for analysis in head.analyses:
                    matched = True
                    if 'matcher' not in self.context:
                        pass
                    elif not self.context['matcher'].matches(analysis):
                        matched = False
                    if matched:
                        heads.append({"pos": head.pos, "a": analysis})
        return heads

    def in_context(self, target: Token, sentence: list, head: Token):
        '''Check if head is within context and no barrier blocks it.

        Does note check if head is valid head, just that it is in context
        position.
        '''
        if self.context['location'] == 'ROOT':
            return True
        elif self.context['location'] == 'left':
            if not head.pos < target.pos:
                return False
            if 'barrier' in self.context:
                for blocker in sentence:
                    if blocker.pos < head.pos or blocker.pos > target.pos:
                        continue
                    for anal in blocker.analyses:
                        if self.context['barrier'].matches(anal):
                            return False
            return True
        elif self.context['location'] == 'right':
            if not head.pos > target.pos:
                return False
            if 'barrier' in self.context:
                for blocker in sentence:
                    if blocker.pos > head.pos or blocker.pos < target.pos:
                        continue
                    for anal in blocker.analyses:
                        if self.context['barrier'].matches(anal):
                            return False
            return True
        elif self.context['location'] == 'any':
            if 'barrier' in self.context:
                for blocker in sentence:
                    if blocker.pos < min(head.pos, target.pos) or \
                            blocker.pos > max(target.pos, head.pos) or \
                            blocker.pos == target.pos:
                        continue
                    for anal in blocker.analyses:
                        if self.context['barrier'].matches(anal):
                            return False
            return True
        elif self.context['location'].isdigit() or\
                self.context['location'][0] in '+-' and \
                self.context['location'][1:].isdigit():
            if head.pos == target.pos + int(self.context['location']):
                return True
            else:
                return False
        else:
            print("Broken context defionition:", self.context)
            exit(1)
