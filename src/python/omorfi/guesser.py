#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Omorfi guesser logic is contained in this class. Can use HFST model but
falls back to basic python heuristics.
"""


from .token import Token
from .analyser import Analyser
from .analysis import Analysis
from .hfst import load_hfst


class Guesser:

    """
    An object for omorfi’s morphological guessing.
    """

    #: magic number for penalty weights
    PENALTY = 28021984

    def __init__(self):
        """Load analysis model from a file.

        Args
            f: containing single hfst automaton binary.
        """
        self.guesser = None
        self.analyser = None
        self.try_titlecase = True
        self.try_lowercase = True
        self.try_uppercase = True
        self.try_detitlecase = True

    def use_analyser(self, analyser: Analyser):
        self.analyser = analyser

    def load_guesser(self, hfstfile: str):
        self.guesser = load_hfst(hfstfile)

    def _guess_fsa(self, token: Token):
        '''Guess token reading using language models.

        Args:
            token: token to guess'''
        res = self.guesser.lookup(token.surf)
        for r in res:
            anal = r[0] + '[GUESS=FSA][WEIGHT=%f]' % (r[1])
            weight = float(r[1])
            guess = Analysis.fromomor(anal, weight)
            guess.manglers.append('GUESSER=FSA')
            token.analyses.append(guess)
        return res

    def _guess_heuristic(self, token: Token):
        '''Heuristic guessing function written fully in python.

        This is kind of last resort, but has some basic heuristics that may
        be always useful.

        Args:
            token: token to guess

        Returns:
            list: new analyses guessed
        '''
        # woo advanced heuristics!!
        newanals = list()
        newanals = self._guess_recased(token)
        if not newanals:
            newanals = self._guess_misc(token)
        for anal in newanals:
            token.analyses.append(anal)
        return newanals

    def _guess_recased(self, token: Token):
        '''Guess recased versions with analyser.'''
        newanals = list()
        s = token.surf
        trieds = {s}
        if len(s) > 2 and (s[0].islower() or s[1].isupper()) and \
                self.try_titlecase:
            tcs = s[0].upper() + s[1:].lower()
            if tcs not in trieds:
                tcres = self.analyser.analyse(tcs)
                for anal in tcres:
                    anal.manglers.append('Titlecased')
                    anal.analsurf = tcs
                    anal.weight = anal.weight + self.PENALTY
                    newanals.append(anal)
                trieds.add(tcs)
        if len(s) > 2 and s[0].isupper() and self.try_detitlecase:
            dts = s[0].lower() + s[1:]
            if dts not in trieds:
                dtres = self.analyser.analyse(dts)
                for anal in dtres:
                    anal.manglers.append('dETITLECASED')
                    anal.analsurf = dts
                    if token.pos != 1:
                        anal.weight = anal.weight + self.PENALTY
                    newanals.append(anal)
                trieds.add(dts)
        if not s.isupper() and self.try_uppercase:
            ups = s.upper()
            if ups not in trieds:
                upres = self.analyser.analyse(ups)
                for anal in upres:
                    anal.manglers.append('UPPERCASED')
                    anal.analsurf = ups
                    anal.weight = anal.weight + self.PENALTY
                    newanals.append(anal)
                trieds.add(ups)
        if not s.islower() and self.try_lowercase:
            lows = s.lower()
            if lows not in trieds:
                lowres = self.analyser.analyse(lows)
                for anal in lowres:
                    anal.manglers.append('lowercased')
                    anal.analsurf = lows
                    anal.weight = anal.weight + self.PENALTY
                    newanals.append(anal)
                trieds.add(lows)
        return newanals

    def _guess_misc(self, token: Token):
        '''Guess based on form of the word.

        Following guesses are made:

        * length == 1 -> SYM
        * first letter upper case -> PROPN Case=Nom|Num=Sing
        * else -> NOUN Case=Nom|Num=Sing
        '''
        newanals = list()
        if len(token.surf) == 1:
            omor = '[WORD_ID=' + token.surf +\
                '][UPOS=SYM][GUESS=HEUR]' +\
                '[WEIGHT=%f]' % (self.PENALTY)
            weight = self.PENALTY
            guess = Analysis.fromomor(omor, weight)
            guess.manglers.append('GUESSER=PYTHON_LEN1')
            newanals.append(guess)
        elif token.surf[0].isupper() and len(token.surf) > 1:
            omor = '[WORD_ID=' + token.surf +\
                '][UPOS=PROPN][NUM=SG][CASE=NOM][GUESS=HEUR]' +\
                '[WEIGHT=%f]' % (self.PENALTY)
            weight = self.PENALTY
            guess = Analysis.fromomor(omor, weight)
            guess.manglers.append('GUESSER=PYTHON_0ISUPPER')
            newanals.append(guess)
        else:
            omor = '[WORD_ID=' + token.surf +\
                '][UPOS=NOUN][NUM=SG][CASE=NOM][GUESS=HEUR]' +\
                '[WEIGHT=%f]' % (self.PENALTY)
            weight = self.PENALTY
            guess = Analysis.fromomor(omor, weight)
            guess.manglers.append('GUESSER=PYTHON_ELSE')
            newanals.append(guess)
        return newanals

    def guess(self, token: Token):
        '''Speculate morphological analyses of OOV token.

        This method may use multiple information sources, but not the actual
        analyser. Therefore a typical use of this is after the analyse(token)
        function has failed. Note that some information sources perform badly
        when guessing without context, for these the analyse_sentence(sent) is
        the only option.

        Side-effect:
            This operation stores guesses in token for future use as well as
            returning them.

        Args:
            token: token to analyse with guessers.

        Returns:
            New guesses as a list of Analysis objects.
        '''
        if self.guesser:
            guesses = self._guess_fsa(token)
        else:
            guesses = self._guess_heuristic(token)
        return guesses
