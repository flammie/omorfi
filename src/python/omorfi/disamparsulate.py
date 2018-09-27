#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Beta-testing a wack idea of not disambiguating and dependency parsing at the
same time. Pay no attention to the man behind the curtains and move along.
"""

from sys import argv

from .fileformats import next_conllu
from .token import Token


class Suggestion:
    """Not a rule."""

    def __init__(self):
        self.name = "Unnamed"
        self.target = dict()
        # ± tokens = stuff
        self.context = dict()
        # barrier for * contexts
        self.barrier = dict()
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
                heads = self.find_context(token, sentence)
                if not heads:
                    matched = False
                    continue
            if matched:
                if self.unlikelihood > 0:
                    analysis.weight += self.unlikelihood
                elif self.unlikelihood < 0:
                    for b in token.analyses:
                        if b != analysis:
                            b.weight += self.unlikelihood
                for head in heads:
                    if self.depname:
                        analysis.udep = {self.depname: head.pos}
                    # also reweight the head

    def find_context(self, token: Token, sentence: list):
        heads = list()
        for head in sentence:
            if self.in_context(token, sentence, head):
                for analysis in token.analyses:
                    matched = True
                    if "ufeats" in self.context:
                        for feat, value in self.context["ufeats"]:
                            if feat not in analysis.ufeats:
                                matched = False
                                break
                            elif analysis.ufeats[feat] != value:
                                matched = False
                                break
                    if matched:
                        heads.append({"pos": token.pos, "a": analysis})

    def in_context(self, token: Token, sentence: list, head: Token):
        if self.context['location'] == 'left' and head.pos < token.pos:
            if self.barrier:
                for blocker in sentence:
                    if blocker.pos < head.pos or blocker.pos > token.pos:
                        continue
                    for feat, value in self.barrier['ufeats']:
                        for anal in blocker.analyses:
                            if feat in anal.ufeats and \
                                    anal.ufeats[feat] == value:
                                return False
            return True
        elif self.context['location'] == 'right' and head.pos > token.pos:
            if self.barrier:
                for blocker in sentence:
                    if blocker.pos > head.pos or blocker.pos < token.pos:
                        continue
                    for feat, value in self.barrier['ufeats']:
                        for anal in blocker.analyses:
                            if feat in anal.ufeats and \
                                    anal.ufeats[feat] == value:
                                return False
            return True
        elif self.context['location'] == 'any':
            if self.barrier:
                for blocker in sentence:
                    if blocker.pos < min(head.pos, token.pos) or \
                            blocker.pos < max(token.pos, head.pos):
                        continue
                    for feat, value in self.barrier['ufeats']:
                        for anal in blocker.analyses:
                            if feat in anal.ufeats and \
                                    anal.ufeats[feat] == value:
                                return False
            return True
        elif self.context['location'].isdigit() or\
                self.context['location'][0] in '+-' and \
                self.context['location'][1:].isdigit():
            if head.pos == token.pos + int(self.context):
                return True
            else:
                return False
        else:
            print("Broken context defionition:", self.context)
            exit(1)


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
    if len(argv) < 2:
        print("Usage:", argv[0], "CONLLU")
        exit(1)
    infile = open(argv[1])
    eoffed = False
    while not eoffed:
        sent = next_conllu(infile)
        if not sent:
            continue
        for token in sent:
            if token.error == "eof":
                eoffed = True
                continue
        linguisticate(sent)
        for token in sent:
            print(token.printable_conllu())
    exit(0)


if __name__ == "__main__":
    main()
