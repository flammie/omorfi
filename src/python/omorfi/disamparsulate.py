#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Beta-testing a wack idea of not disambiguating and dependency parsing at the
same time. Pay no attention to the man behind the curtains and move along.
"""

from sys import argv
from copy import copy

from .fileformats import next_conllu
from .token import Token
from .analysis import Analysis


class Evidence:
    """Not a rule."""

    def __init__(self):
        """Create a new evidence matching pattern."""
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

    @staticmethod
    def _matches(analysis: Analysis, query: dict):
        """Checks if token matches given params."""
        if "upos" in query:
            if analysis.upos != query['upos']:
                return False
        if "ufeats" in query:
            for feat, value in query["ufeats"].items():
                if feat not in analysis.ufeats:
                    return False
                elif analysis.ufeats[feat] != value:
                    return False
        return True

    def apply(self, token: Token, sentence: list):
        '''If suggestion applies to token in context.'''
        newdeps = list()
        for analysis in token.analyses:
            matched = True
            if not self._matches(analysis, self.target):
                matched = False
                continue
            heads = []
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
                        if analysis.udepname:
                            newdep = copy(analysis)
                            newdep.udepname = self.depname
                            newdep.udeppos = head['pos']
                            newdeps.append(newdep)
                        else:
                            analysis.udepname = self.depname
                            analysis.udeppos = head['pos']
                    # also reweight the head
                    for w in sentence:
                        if w.pos == head['pos']:
                            for a in w.analyses:
                                if a != head['a']:
                                    a.weight -= self.unlikelihood
        # append new stuff at the end to avoid eterbnal loops
        for anal in newdeps:
            token.analyses.append(anal)

    def find_context(self, target: Token, sentence: list):
        '''Traverse sentence to find contexts that match.'''
        if self.context['location'] == 'ROOT':
            return [{"pos": 0, "a": None}]
        heads = list()
        for head in sentence:
            if self.in_context(target, sentence, head):
                for analysis in head.analyses:
                    matched = True
                    if not self._matches(analysis, self.context):
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
            if self.barrier:
                for blocker in sentence:
                    if blocker.pos < head.pos or blocker.pos > target.pos:
                        continue
                    for anal in blocker.analyses:
                        if self._matches(anal, self.barrier):
                            return False
            return True
        elif self.context['location'] == 'right':
            if not head.pos > target.pos:
                return False
            if self.barrier:
                for blocker in sentence:
                    if blocker.pos > head.pos or blocker.pos < target.pos:
                        continue
                    for anal in blocker.analyses:
                        if self._matches(anal, self.barrier):
                            return False
            return True
        elif self.context['location'] == 'any':
            if self.barrier:
                for blocker in sentence:
                    if blocker.pos < min(head.pos, target.pos) or \
                            blocker.pos > max(target.pos, head.pos) or \
                            blocker.pos == target.pos:
                        continue
                    for anal in blocker.analyses:
                        if self._matches(anal, self.barrier):
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
    punctrule.unlikelihood = -8.0
    punctrule.depname = "punct"
    punctrule.context = {"location": "any", "upos": "VERB"}
    punctrule.barrier = {"upos": "PUNCT"}
    rules.append(punctrule)
    rootrule = Evidence()
    rootrule.name = "verbs can be roots"
    rootrule.target = {"upos": "VERB"}
    rootrule.unlikelihood = -8.0
    rootrule.depname = "root"
    rootrule.context = {"location": "ROOT"}
    rules.append(rootrule)
    ccrule = Evidence()
    ccrule.name = "cnjcoo coordinates +1"
    ccrule.target = {"upos": "CCONJ"}
    ccrule.unlikelihood = -1.0
    ccrule.depname = "cc"
    ccrule.context = {"location": "+1"}
    rules.append(ccrule)
    amodrule = Evidence()
    amodrule.name = "adj agrees +1"
    amodrule.target = {"upos": "ADJ", "ufeats": {"Case": "Ela"}}
    amodrule.unlikelihood = -1.0
    amodrule.depname = "amod"
    amodrule.context = {"location": "+1", "ufeats": {"Case": "Ela"}}
    rules.append(amodrule)
    minärule = Evidence()
    minärule.name = "I subjects agree verb"
    minärule.target = {"upos": "PRON", "ufeats":
                       {"PronType": "Prs", "Number": "Sing", "Person": "1",
                        "Case": "Nom"}}
    minärule.unlikelihood = -1.0
    minärule.depname = "nsubj"
    minärule.context = {"location": "any", "upos": "VERB", "ufeats":
                        {"Person": "1", "Number": "Sing"}}
    rules.append(minärule)
    numprule = Evidence()
    numprule.name = "Numeral phrase makes nom to par"
    numprule.target = {"upos": "NUM", "ufeats":
                       {"NumType": "Card", "Number": "Sing", "Case": "Nom"}}
    numprule.unlikelihood = -1.0
    numprule.depname = "nummod"
    numprule.context = {"location": "+1", "upos": "NOUN", "ufeats":
                        {"Number": "Sing", "Case": "Par"}}
    rules.append(numprule)
    objprule = Evidence()
    objprule.name = "Partitives are objects"
    objprule.target = {"upos": "NOUN", "ufeats":
                       {"Case": "Par"}}
    objprule.unlikelihood = -1.0
    objprule.depname = "obj"
    objprule.context = {"location": "left", "upos": "VERB"}
    objprule.barrier = {"upos": "PUNCT"}
    rules.append(objprule)
    negrule = Evidence()
    negrule.name = "Negation verb auxes conneg"
    negrule.target = {"upos": "AUX", "ufeats":
                      {"Polarity": "Neg"}}
    negrule.unlikelihood = -1.0
    negrule.depname = "aux"
    negrule.context = {"location": "any", "upos": "VERB", "ufeats":
                       {"Connegative": "Yes"}}
    negrule.barrier = {"upos": "VERB"}
    rules.append(negrule)
    advmodrule = Evidence()
    advmodrule.name = "adv mods v"
    advmodrule.target = {"upos": "ADV"}
    advmodrule.unlikelihood = -1.0
    advmodrule.depname = "advmod"
    advmodrule.context = {"location": "any", "upos": "VERB"}
    rules.append(advmodrule)
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
