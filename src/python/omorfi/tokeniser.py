#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Omorfi tokeniser logic is contained in this class. There is a less
object oriented version that doesn't use language models or such stuff.
"""

from .settings import fin_punct_leading, fin_punct_trailing
from .analyser import Analyser
from .token import Token
from .hfst import load_hfst
from .error_logging import just_fail


class Tokeniser:

    """
    An object for omorfi’s morphological analysis.
    """

    def __init__(self):
        """Load analysis model from a file.

        Args
            f: containing single hfst automaton binary.
        """
        self.analyser = None
        self.tokeniser = None
        self.try_titlecase = True
        self.try_detitlecase = True
        self.try_uppercase = True
        self.try_lowercase = True

    def use_analyser(self, analyser: Analyser):
        self.analyser = analyser

    def load_tokeniser(self, hfstfile: str):
        self.tokeniser = load_hfst(hfstfile)

    def _find_retoken_recase(self, token: Token):
        """Checks if token is acceptable when case is ignored.

        Used case-ignorations depend on the settings.

        Args:
            token: token to recase

        Returns:
            recased token or False if no retoken is possible
        """
        if self.accept(token):
            return token
        if len(token.surf) > 1:
            # we test len to just use 1: slice...
            if self.try_titlecase and not token.surf[0].isupper():
                if self.accept(Token(token.surf[0].upper()
                                     + token.surf[1:].lower())):
                    return token
            if self.try_detitlecase and not token.surf[0].islower():
                if self.accept(Token(token.surf[0].lower() + token.surf[1:])):
                    return token
        if self.try_lowercase:
            if self.accept(Token(token.surf.lower())):
                return token
        if self.try_uppercase:
            if self.accept(Token(token.surf.upper())):
                return token
        return False

    def _find_retokens(self, token: Token):
        """Finds list of acceptable sub-tokens from a token.

        Tries to strip punct tokens from left and right.

        Args:
            token: token to retokenise

        Returns:
            list of tokens giving best retokenisation
        """
        retoken = self._find_retoken_recase(token)
        if retoken:
            return [retoken]
        pretokens = []
        posttokens = []
        for i in range(4):
            for j in range(4):
                if len(token.surf) > (i + j):
                    if j == 0:
                        resurf = token.surf[i:]
                        presurfs = token.surf[:i]
                        postsurfs = ''
                    else:
                        resurf = token.surf[i:-j]
                        presurfs = token.surf[:i]
                        postsurfs = token.surf[-j:]
                    pretrailpuncts = True
                    for c in presurfs:
                        if c in fin_punct_leading:
                            pretoken = Token(c)
                            pretoken.spaceafter = 'No'
                            pretokens.append(pretoken)
                        else:
                            pretrailpuncts = False
                            break
                    for c in postsurfs:
                        if c in fin_punct_trailing:
                            posttoken = Token(c)
                            posttoken.spacebefore = 'No'
                            posttokens.append(posttoken)
                        else:
                            pretrailpuncts = False
                            break
                    if not pretrailpuncts:
                        continue
                    retoken = Token(resurf)
                    reretoken = self._find_retoken_recase(retoken)
                    if reretoken:
                        return pretokens + [reretoken] + posttokens
        # no acceptable substring inside, just strip puncts
        return [token]

    def _retokenise(self, tokens: list):
        """Takes list of string from and produces list of tokens.

        May change number of tokens. Should be used with result of split().

        Args:
            tokens: list of tokens to retokenise

        Returns:
            list of tokens representing best tokenisations of tokens
        """
        retokens = []
        for s in tokens:
            token = Token(s)
            for retoken in self._find_retokens(token):
                retokens.append(retoken)
        return retokens

    def fsa_tokenise(self, line: str):
        """Tokenise with FSA.

        Args:
            line:  string to tokenise

        Todo:
            Not implemented (needs pmatch python support)
        """
        if self.tokeniser:
            res = self.tokeniser.lookup(line)
            return res
        return None

    def python_tokenise(self, line: str):
        """Tokenise with python's basic string functions.

        Args:
            line:  string to tokenise
        """
        return self._retokenise(line.split())

    def tokenise(self, line: str):
        """Perform tokenisation with loaded tokeniser if any, or `split()`.

        If tokeniser is available, it is applied to input line and if
        result is achieved, it is split to tokens according to tokenisation
        strategy and returned as a list.

        If no tokeniser are present, or none give results, the line will be
        tokenised using python's basic string functions. If analyser is
        present, tokeniser will try harder to get some analyses for each
        token using hard-coded list of extra splits.

        Args:
            line: a string to be tokenised, should contain a line of text or a
                  sentence

        Returns:
            A list of tokens based on the line. List may include boundary
            non-tokens if e.g. sentence boundaries are recognised. For empty
            line a paragraph break non-token may be returned.
        """
        tokens = None
        if self.tokeniser:
            tokens = self.fsa_tokenise(line)
        if not tokens:
            tokens = self.python_tokenise(line)
        return tokens

    def accept(self, token):
        '''Check if the token is in the dictionary or not.

        Returns:
            False for OOVs, True otherwise. Note, that this is not
        necessarily more efficient than bool(analyse(token))
        '''
        if self.analyser:
            return self.analyser.accept(token)
        else:
            return False

    def tokenise_sentence(self, sentence: str):
        '''tokenise a sentence.

        To be used when text is already sentence-splitted. If the
        text is plain text with sentence boundaries within lines,
        use

        Args:
            sentence: a string containing one sentence

        Returns:
            list of tokens in sentence
        '''
        if not sentence or sentence == '':
            token = Token()
            token.nontoken = 'separator'
            token.comment = ''
            return [token]
        tokens = self.tokenise(sentence)
        pos = 1
        for token in tokens:
            token.pos = pos
            pos += 1
        return tokens

    def tokenise_plaintext(self, f):
        '''tokenise a whole text.

        Args:
            f: filelike object with iterable strings

        Returns:
            list of tokens
        '''
        tokens = list()
        for line in f:
            tokens = self.tokenise(line.strip())
            pos = 1
            for token in tokens:
                token.pos = pos
                pos += 1
            sep = Token()
            sep.nontoken = 'separator'
            tokens.append(sep)
            return tokens
        eoft = Token()
        eoft.nontoken = 'eof'
        tokens.append(eoft)
        return tokens

    def tokenise_conllu(self, f):
        '''tokenise a conllu sentence or comment.

        Should be used a file-like iterable that has CONLL-U sentence or
        comment or empty block coming up.

        Args:
            f: filelike object with iterable strings

        Returns:
            list of tokens
        '''
        tokens = list()
        for line in f:
            fields = line.strip().split('\t')
            token = Token()
            if len(fields) != 10:
                if line.startswith('#'):
                    token.nontoken = 'comment'
                    token.comment = line.strip()
                    tokens.append(token)
                    return tokens
                elif line.strip() == '':
                    token.nontoken = 'separator'
                    token.comment = ''
                    tokens.append(token)
                    return tokens
                else:
                    token.nontoken = 'error'
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
                    just_fail('Cannot figure out token index', fields[0])
                    exit(1)
            token.pos = index
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
                               'FTB1-InfForm', 'Missed-POSITION',
                               'Was18']:
                        # FTB stuff
                        pass
                    else:
                        just_fail('Unknown MISC', k)
                        exit(1)
            tokens.append(token)
        eoft = Token()
        eoft.nontoken = 'eof'
        tokens.append(eoft)
        return tokens

    def tokenise_vislcg(self, f):
        '''Tokenises a sentence from VISL-CG format data.

        Returns a list of tokens when it hits first non-token block, including
        a token representing this non-token block.

        Args:
            f: filelike object to itrate strings of vislcg data

        Returns:
            list of tokens
        '''
        tokens = list()
        pos = 1
        for line in f:
            token = Token()
            line = line.strip()
            if not line or line == '':
                token.nontoken = 'separator'
                token.comment = ''
                tokens.append(token)
                return tokens
            elif line.startswith('#') or line.startswith('<'):
                # # comment, or
                # <TAG> </TAG>
                token.nontoken = 'comment'
                token.comment = line.strip()
                tokens.append(token)
                return tokens
            elif line.startswith('"<') and line.endswith('>"'):
                # "<surf>"
                token = Token()
                token.surf = line[2:-2]
                tokens.append(token)
                pos += 1
            elif line.startswith('\t"'):
                # \t"lemma" ANAL ANAL ANAL
                fields = line.strip().split()
                token.lemma = fields[0].strip('"')
            elif line.startswith(';\t"'):
                # ;\t"lemma" ANAL ANAL ANAL KEYWORD:rulename
                token.nontoken = 'gold'
                token.comment = line.strip()
            else:
                token.nontoken = 'error'
                token.error = 'vislcg: ' + line.strip()
        eoft = Token()
        eoft.nontoken = 'eof'
        tokens.append(eoft)
        return tokens
