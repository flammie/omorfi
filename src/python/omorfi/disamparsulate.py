#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Beta-testing a wack idea of not disambiguating and dependency parsing at the
same time. Pay no attention to the man behind the curtains and move along.
"""

from sys import argv
from copy import copy
# stuff
import xml.etree.ElementTree
from xml.etree.ElementTree import Element

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


def frobblesnizz(f):
    '''parse disampursalations from XML file.'''
    xmltree = xml.etree.ElementTree.parse(f)
    root = xmltree.getroot()
    if root.get("version") != "0.0.0":
        print("Unsupported version", root.get("version"))
    rules = list()
    for child in root:
        # parse stuff
        if child.tag == 'evidence':
            e = parse_evidence(child)
            rules.append(e)
        else:
            print("Unknown element disamparsulations:", child)
            exit(2)
    return rules


def parse_evidence(evidence: Element):
    '''Parse evidence element block.'''
    e = Evidence()
    e.name = evidence.get('name')
    for child in evidence:
        if child.tag == 'target':
            e.target = parse_target(child)
        elif child.tag == 'likelihood':
            e.probability = parse_likelihood(child)
        elif child.tag == 'depname':
            e.depname = parse_depname(child)
        elif child.tag == 'context':
            e.context = parse_context(child)
        else:
            print("Unknown element under evidence:", child)
            exit(2)
    return e


def parse_target(target: Element):
    '''Parse target definition element.'''
    t = dict()
    for child in target:
        if child.tag == 'upos':
            t['upos'] = parse_upos(child)
        elif child.tag == 'ufeats':
            t['ufeats'] = parse_ufeats(child)
        else:
            print("Unknown element under target:",
                  xml.etree.ElementTree.tostring(child))
    return t


def parse_likelihood(likelihood: Element):
    '''Parse likelihood element.'''
    if likelihood.text == 'usually':
        return 16.0
    elif likelihood.text == 'unlikely':
        return -16.0
    elif likelihood.text == 'probably':
        return 4.0
    elif likelihood.text == 'possibly':
        return 8.0
    else:
        print("Unknown likelihood:", likelihood.text)
        exit(2)


def parse_depname(depname: Element):
    '''Parse depname element.'''
    return depname.text


def parse_context(context: Element):
    '''Parse context element.'''
    c = dict()
    for child in context:
        if child.tag == 'location':
            c['location'] = parse_location(child)
        elif child.tag == 'upos':
            c['upos'] = parse_upos(child)
        elif child.tag == 'ufeats':
            c['ufeats'] = parse_ufeats(child)
        elif child.tag == 'context':
            c['context'] = parse_context(child)
        elif child.tag == 'barrier':
            c['barrier'] = parse_barrier(child)
        else:
            print("Unknown child for context", child)
            exit(2)
    return c


def parse_upos(upos: Element):
    '''Parse upos element.'''
    return upos.text


def parse_location(location: Element):
    '''Parse location element.'''
    return location.text


def parse_ufeats(ufeats: Element):
    '''Parse ufeats element.'''
    ufs = dict()
    for child in ufeats:
        if child.tag == 'ufeat':
            name, value = parse_ufeat(child)
            ufs[name] = value
        else:
            print("Unknown child for ufeats", child)
            exit(2)
    return ufs


def parse_ufeat(ufeat: Element):
    '''Parse ufeat element.'''
    return ufeat.get('name'), ufeat.text


def parse_barrier(barrier: Element):
    '''Parse barrier element.'''
    b = dict()
    for child in barrier:
        if child.tag == 'upos':
            b['upos'] = parse_upos(child)
        elif child.tag == 'ufeats':
            b['ufeats'] = parse_ufeats(child)
    return b


def linguisticate(sentence: list, rules: list):
    '''Not a parsing function.'''
    #
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
