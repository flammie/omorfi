#!/usr/bin/env pythom3

"""
File format I/O handlings
"""

from sys import stderr

from .token import Token


def next_plaintext(f):
    '''tokenise a line of text.

    @todo should get sentence from plaintext in the future.'''
    tokens = list()
    for line in f:
        surfs = line.strip().split()
        pos = 1
        for surf in surfs:
            token = Token(surf)
            if pos == 1:
                token.firstinsent = True
            else:
                token.firstinsent = False
            token.pos = pos
            pos += 1
            tokens.append(token)
        sep = Token()
        sep.nontoken = "separator"
        tokens.append(sep)
        return tokens
    eoft = Token()
    eoft.nontoken = "eof"
    tokens.append(eoft)
    return tokens


def next_conllu(f):
    '''tokenise a conllu sentence or comment.

    Should be used a file-like iterable that has CONLL-U sentence or
    comment or empty block coming up.'''
    tokens = list()
    for line in f:
        fields = line.strip().split('\t')
        token = Token()
        if len(fields) != 10:
            if line.startswith('#'):
                token.nontoken = "comment"
                token.comment = line.strip()
                tokens.append(token)
                return tokens
            elif line.strip() == '':
                token.nontoken = "separator"
                token.comment = ''
                tokens.append(token)
                return tokens
            else:
                token.nontoken = "error"
                token.error = line.strip()
                tokens = [token]
                return tokens
        token._conllu = fields
        try:
            index = int(fields[0])
        except ValueError:
            if '-' in fields[0]:
                # MWE
                continue
            elif '.' in fields[0]:
                # a ghost
                continue
            else:
                print("Cannot figure out token index", fields[0],
                      file=stderr)
                exit(1)
        token.pos = index
        if index == 1:
            token.firstinsent = True
        token.surf = fields[1]
        if fields[9] != '_':
            miscs = fields[9].split('|')
            for misc in miscs:
                k, v = misc.split('=')
                if k == 'SpaceAfter':
                    token.spaceafter = v
                elif k in ['Alt', 'FTB-PronType', 'FTB-Rel',
                           'Missed-Rel', 'FTB-rel', 'Join',
                           'Missed-SUBCAT', 'FTB-Sub', 'Prefix',
                           'FTB1-InfForm', 'Missed-POSITION']:
                    # FTB stuff
                    pass
                else:
                    print("Unknown MISC", k, file=stderr)
                    exit(1)
        tokens.append(token)
    eoft = Token()
    eoft.nontoken = "eof"
    tokens.append(eoft)
    return tokens


def next_vislcg(f):
    '''Tokenises a sentence from VISL-CG format data.

    Returns a list of tokens when it hits first non-token block, including
    a token representing this non-token block.
    '''
    tokens = list()
    pos = 1
    for line in f:
        token = Token()
        line = line.strip()
        if not line or line == '':
            token.nontoken = "separator"
            token.comment = ''
            tokens.append(token)
            return tokens
        elif line.startswith("#") or line.startswith("<"):
            # # comment, or
            # <TAG> </TAG>
            token.nontoken = "comment"
            token.comment = line.strip()
            tokens.append(token)
            return tokens
        elif line.startswith('"<') and line.endswith('>"'):
            # "<surf>"
            token = Token()
            token.surf = line[2:-2]
            if pos == 1:
                token.firstinsent = True
            tokens.append(token)
            pos += 1
        elif line.startswith('\t"'):
            # \t"lemma" ANAL ANAL ANAL
            fields = line.strip().split()
            token.lemma = fields[0].strip('"')
        elif line.startswith(';\t"'):
            # ;\t"lemma" ANAL ANAL ANAL KEYWORD:rulename
            token.nontoken = "gold"
            token.comment = line.strip()
        else:
            token.nontoken = "error"
            token.error = 'vislcg: ' + line.strip()
    eoft = Token()
    eoft.nontoken = "eof"
    tokens.append(eoft)
    return tokens

def next_omorfi(f):
    '''Read next block in omorfi internal stream format.'''
    tokens = []
    return tokens
