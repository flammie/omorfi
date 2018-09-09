#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A lightweight container for whole texts. Contains tokens.
"""

from .token import Token


class Doc:
    """Doc contains tokens consisting a text or corpus.

    Doc is typically e.g. one file tokenised and/or parsed. Contains tokens,
    which make up sentences and stuff.
    """

    def __init__(self):
        """Create an empty document"""
        ## underlying raw omor analysis
        self.tokens = []
        ## sentences
        self.sents = []

    def __getitem__(self, index):
        """Just pick token from the list."""
        return self.tokens[index]

    def __str__(self):
        s = 'Doc: '
        if len(self.tokens) > 10:
            s += self.tokens[:10] + ', ...'
        else:
            s += self.tokens
        return s

    def get_sentence(self, index):
        '''Get a sentence from doc.

        If doc contains nontokens separating sentences...
        '''
        offsets = self.sents[index]
        return self.tokens[offsets[0]:offsets[1]]

    def add(self, tokens):
        '''Add tokens to the documentation.

        Adds sentences if they are separated by proper nontokens.
        '''
        sent_start = False
        sent_end = -1
        for token in tokens:
            self.tokens.append(token)
            if not token.nontoken:
                if not sent_start or sent_start < sent_end:
                    sent_start = len(self.tokens)
            else:
                if sent_start:
                    sent_end = len(self.tokens)
                    self.sents.append([sent_start, sent_end])

    def write(self, f):
        '''Writes self in some format into a file-like object.

        Experimental.
        '''
        print('"omorfi.Doc": { "tokens": [', file=f)
        first = True
        for token in self.tokens:
            if not first:
                print(",", file=f)
            print(token, end='', file=f)
            first = False
        print('\n], "sents": [', file=f)
        first = True
        for sent in self.sents:
            if not first:
                print(",", file=f)
            print('[', sent[0], ', ', sent[1], ']', end='', file=f)
            first = False
        print('\n]}', file=f)

    @staticmethod
    def read(f):
        '''Reads self from a file-like object.'''
        line = next(f)
        if line.strip() != '"omorfi.Doc": { "tokens": [':
            print("Error blerb:", line.strip())
            exit(1)
        doc = Doc()
        in_sents = False
        for line in f:
            if line.strip().endswith("]}"):
                continue
            elif in_sents:
                first, last = line.strip().rstrip(",").rstrip("]"). \
                    strip("[").strip().split(", ")
                doc.sents.append([first, last])
            elif '"sents":' in line:
                in_sents = True
            elif '"omorfi.Token":' in line:
                token = Token.fromstr(line.strip().rstrip(","))
                doc.tokens.append(token)
        return doc
