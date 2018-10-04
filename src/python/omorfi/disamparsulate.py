#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Beta-testing a wack idea of not disambiguating and dependency parsing at the
same time. Pay no attention to the man behind the curtains and move along.
"""

from sys import argv

from .fileformats import next_conllu
from .token import Token


class Evidence:
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
            if "upos" in self.target:
                if analysis.upos != self.target['upos']:
                    matched = False
                    continue
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
                            b.weight -= self.unlikelihood
                for head in heads:
                    # we actually want to copy analysis per head
                    if self.depname:
                        analysis.udepname = self.depname
                        analysis.udeppos = head['pos']
                    # also reweight the head

    def find_context(self, target: Token, sentence: list):
        '''Traverse sentence to find contexts that match.'''
        if self.context['location'] == 'ROOT':
            return [{"pos": 0, "a": None}]
        heads = list()
        for head in sentence:
            if self.in_context(target, sentence, head):
                for analysis in head.analyses:
                    matched = True
                    if "upos" in self.context:
                        if analysis.upos != self.context['upos']:
                            matched = False
                            break
                    if "ufeats" in self.context:
                        for feat, value in self.context["ufeats"]:
                            if feat not in analysis.ufeats:
                                matched = False
                                break
                            elif analysis.ufeats[feat] != value:
                                matched = False
                                break
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
        elif self.context['location'] == 'left' and head.pos < target.pos:
            if self.barrier:
                for blocker in sentence:
                    if blocker.pos < head.pos or blocker.pos > target.pos:
                        continue
                    if 'upos' in self.barrier:
                        for anal in blocker.analyses:
                            if anal.upos == self.barrier['upos']:
                                return False
                    if 'ufeats' in self.barrier:
                        for feat, value in self.barrier['ufeats']:
                            for anal in blocker.analyses:
                                if feat in anal.ufeats and \
                                        anal.ufeats[feat] == value:
                                    return False
            return True
        elif self.context['location'] == 'right' and head.pos > target.pos:
            if self.barrier:
                for blocker in sentence:
                    if blocker.pos > head.pos or blocker.pos < target.pos:
                        continue
                    if 'upos' in self.barrier:
                        for anal in blocker.analyses:
                            if anal.upos == self.barrier['upos']:
                                return False
                    if 'ufeats' in self.barrier:
                        for feat, value in self.barrier['ufeats']:
                            for anal in blocker.analyses:
                                if feat in anal.ufeats and \
                                        anal.ufeats[feat] == value:
                                    return False
            return True
        elif self.context['location'] == 'any':
            if self.barrier:
                for blocker in sentence:
                    if blocker.pos < min(head.pos, target.pos) or \
                            blocker.pos < max(target.pos, head.pos) or \
                            blocker.pos == target.pos:
                        continue
                    if 'upos' in self.barrier:
                        for anal in blocker.analyses:
                            if anal.upos == self.barrier['upos']:
                                return False
                    if 'ufeats' in self.barrier:
                        for feat, value in self.barrier['ufeats']:
                            for anal in blocker.analyses:
                                if feat in anal.ufeats and \
                                        anal.ufeats[feat] == value:
                                    return False
            return True
        elif self.context['location'].isdigit() or\
                self.context['location'][0] in '+-' and \
                self.context['location'][1:].isdigit():
            if head.pos == target.pos + int(self.context):
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
    insrule = Evidence()
    insrule.name = "instructives unlikely"
    insrule.target = {"ufeats": {"Case": "Ins"}}
    insrule.unlikelihood = 16.0
    rules.append(insrule)
    punctrule = Evidence()
    punctrule.name = "puncts to nearest main verb"
    punctrule.target = {"upos": "PUNCT"}
    punctrule.unlikelihood = -1.0
    punctrule.depname = "punct"
    punctrule.context = {"location": "any", "upos": "VERB"}
    punctrule.barrier = {"upos": "PUNCT"}
    rules.append(punctrule)
    rootrule = Evidence()
    rootrule.name = "verbs can be roots"
    rootrule.target = {"upos": "VERB"}
    rootrule.unlikelihood = -1.0
    rootrule.depname = "root"
    rootrule.context = {"location": "ROOT"}
    rules.append(rootrule)
    for token in sentence:
        for rule in rules:
            rule.apply(token, sentence)


def main():
    """Invoke a simple CLI analyser."""
    if len(argv) < 2:
        print("Usage:", argv[0], "ANALYSER INFILE")
        exit(1)
    from .omorfi import Omorfi
    omorfi = Omorfi(True)
    omorfi.load_analyser(argv[1])
    infile = open(argv[2])
    eoffed = False
    while not eoffed:
        sent = next_conllu(infile)
        if not sent:
            continue
        for token in sent:
            if token.error == "eof":
                eoffed = True
                break
            omorfi.analyse(token)
            omorfi.guess(token)
        linguisticate(sent)
        for token in sent:
            print(token.printable_conllu())
    exit(0)


if __name__ == "__main__":
    main()
