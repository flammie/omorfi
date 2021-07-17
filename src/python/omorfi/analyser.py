#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Omorfi analyser logic is contained in this class. Uses the HFST model,
optionally udpipe and frequencies if they can be loaded.
"""

from math import log

from .token import Token
from .analysis import Analysis
from .hfst import load_hfst
from .error_logging import just_fail

CAN_UDPIPE = True
try:
    from ufal.udpipe import Model, Pipeline, ProcessingError
except ImportError:
    CAN_UDPIPE = False


class Analyser:

    """
    An object for omorfi’s morphological analysis.
    """

    #: magic number for penalty weights
    PENALTY = 28021984

    def __init__(self):
        """Initialise an empty analyser."""
        self.analyser = None
        self.udpiper = None
        self.udpipeline = None
        self.uderror = None
        self.can_udpipe = False
        self.lexlogprobs = dict()
        self.taglogprobs = dict()

    def load_analyser(self, hfstfile: str):
        """Load analyser model from a file.

        Args
            f: containing single hfst automaton binary.
        """
        self.analyser = load_hfst(hfstfile)

    def load_udpipe(self, filename: str):
        """Load UDPipe model for statistical parsing.

        UDPipe can be used as extra information source for OOV symbols
        or all tokens. It works best with sentence-based analysis, token
        based does not keep track of context.

        @param filename  path to UDPipe model
        """
        if not CAN_UDPIPE:
            just_fail('importing udpipe failed, cannot load udpipe')
            return
        self.udpiper = Model.load(filename)
        # use pipeline for now, ugly but workable
        self.udpipeline = Pipeline(self.udpiper, 'horizontal',
                                   Pipeline.DEFAULT, Pipeline.DEFAULT,
                                   'conllu')
        self.uderror = ProcessingError()
        ## udpipe is loaded
        self.can_udpipe = True

    def load_lexical_frequencies(self, lexfile):
        """Load a frequency list for lemmas. Experimental.
        Currently in uniq -c format, subject to change.

        Args:
            lexfile: file with frequencies.
        """
        lextotal = 0
        lexcounts = dict()
        for line in lexfile:
            fields = line.split('\t')
            lexcount = int(fields[0])
            lexcounts[fields[1]] = lexcount
            lextotal += lexcount
        for lex, freq in lexcounts.items():
            if freq != 0:
                self.lexlogprobs[lex] = log(freq / lextotal)
            else:
                # XXX: hack hack, should just use LM count stuff with
                # discounts
                self.lexlogprobs[lex] = log(1 / (lextotal + 1))

    def load_omortag_frequencies(self, omorfile):
        """Load a frequenc list for tags. Experimental.
        Currently in uniq -c format. Subject to change.

        Args:
            omorfile: path to file with frequencies.
        """
        omortotal = 0
        omorcounts = dict()
        for line in omorfile:
            fields = line.split('\t')
            omorcount = int(fields[0])
            omorcounts[fields[1]] = omorcount
            omortotal += omorcount
        for omor, freq in omorcounts.items():
            if freq != 0:
                self.taglogprobs[omor] = log(freq / omortotal)
            else:
                # XXX: hack hack, should just use LM count stuff with
                # discounts
                self.taglogprobs[omor] = log(1 / (omortotal + 1))

    def _analyse(self, token: Token):
        '''Analyse token using HFST, detitle-cases if token is first in sent.

        Args:
            token: token to analyse'''
        # use real surface case
        newanals = list()
        res = self.analyser.lookup(token.surf)
        for r in res:
            omor = r[0] + '[WEIGHT=%f]' % (r[1])
            weight = r[1]
            newanals.append(Analysis.fromomor(omor, weight))
        if token.pos == 1 and token.surf[0].isupper()\
                and len(token.surf) > 1:
            res = self.analyser.lookup(token.surf[0].lower()
                                       + token.surf[1:])
            for r in res:
                omor = r[0] + '[WEIGHT=%f]' % (r[1])
                weight = r[1]
                newanals.append(Analysis.fromomor(omor, weight))
        for a in newanals:
            token.analyses.append(a)
        return newanals

    def analyse(self, token: Token):
        """Perform a simple morphological analysis lookup.

        The analysis will be performed for re-cased variants based on the
        state of the member variables. The re-cased analyses will have more
        penalty weight and additional analyses indicating the changes.

        Side-Effects:
            The analyses are stored in the token, and only the new analyses
            are returned.

        Args:
            token: token to be analysed.

        Returns:
            An HFST structure of raw analyses, or None if there are no matches
            in the dictionary.
        """
        if isinstance(token, str):
            token = Token(token)
        anals = self._analyse(token)
        if not anals:
            omor = '[WORD_ID=' + token.surf.replace('=', '.EQ.') \
                   + '][UPOS=X][GUESS=UNKNOWN][WEIGHT=inf]'
            weight = float('inf')
            anal = Analysis.fromomor(omor, weight)
            anal.manglers.append('GUESSER=NONE')
            token.analyses.append(anal)
            return [anal]
        return anals

    def analyse_sentence(self, tokens):
        """Analyse a full tokenised sentence.

        for details of analysis, see @c analyse(self, token).
        If further models like udpipe are loaded, may fill in gaps with that.
        """
        analysis_lists = []
        i = 0
        for token in tokens:
            i += 1
            analysis_lists[i] += [self.analyse(token)]
        if self.can_udpipe:
            # N.B: I used the vertical input here
            udinput = '\n'.join([token.surf for token in tokens])
            uds = self._udpipe(udinput)
            if len(uds) == len(analysis_lists):
                for i, ud in enumerate(uds):
                    analysis_lists[i] += [ud]
        return tokens

    def _accept(self, token: Token):
        """Look up token from acceptor model.

        Args:
            token: token to accept

        Returns:
            analyses of token"""
        if self.analyser:
            res = self.analyser.lookup(token.surf)
        else:
            res = None
        return res

    def accept(self, token):
        '''Check if the token is in the dictionary or not.

        Returns:
            False for OOVs, True otherwise. Note, that this is not
        necessarily more efficient than bool(analyse(token))
        '''
        return bool(self._accept(token))

    def _udpipe(self, udinput: str):
        """Pipes input to  udpipe model.

        Args:
            udinput: input for udpipe

        Returns:
            tokens with udpipe analyses
        """
        conllus = self.udpipeline.process(udinput, self.uderror)
        if self.uderror.occurred():
            return None
        tokens = []
        for conllu in conllus.split('\n'):
            if conllu.startswith('#'):
                continue
            elif conllu.strip() == '':
                continue
            tokens += [Token.fromconllu(conllu)]
        return tokens


def main():
    """Invoke a simple CLI analyser."""
    exit(0)


if __name__ == "__main__":
    main()
