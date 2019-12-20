#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Simple python interface for omorfi using libhfst-python. Consider this
class as a standard python interface to omorfi and standard reference for
scientific studies, as far as python use goes. For other interfaces, see
the standard shell scripts or java interface.
"""


from argparse import ArgumentParser
from sys import stderr, stdin
from math import log

import libhfst

from .settings import fin_punct_leading, fin_punct_trailing
from .token import Token
from .analysis import Analysis

can_udpipe = True
try:
    from ufal.udpipe import Model, Pipeline, ProcessingError
except ImportError:
    can_udpipe = False


class Omorfi:

    """
    An object holding omorfi binaries for all the functions of omorfi.

    The following functionalities use automata binaries that need to be loaded
    separately:
    * analysis
    * tokenisation
    * generation
    * lemmatisation
    * segmentation
    * lookup
    * guess

    There is python code to perform basic string munging controlled by
    following bool attributes:
        try_lowercase: to use `str.lower()`
        try_titlecase: to use `str[0].upper() + str[1:]`
        try_uppercase: to use `str.upper()`
        try_detitlecase: to use `str[0].lower + str[1:]`

    The annotations will be changed when transformation has been applied.
    """

    #: magic number for penalty weights
    _penalty = 28021984

    def __init__(self, verbosity=False):
        """Construct Omorfi with given verbosity for printouts."""
        self._verbosity = verbosity
        ## analyser model
        self.analyser = None
        ## tokeniser
        self.tokeniser = None
        ## generator model
        self.generator = None
        ## lemmatising model
        self.lemmatiser = None
        ## hyphenating model
        self.hyphenator = None
        ## segmenting model
        self.segmenter = None
        ## label-segment model
        self.labelsegmenter = None
        ## acceptor
        self.acceptor = None
        ## guesser model
        self.guesser = None
        ## UDPipe model
        self.udpiper = None
        ## UDPipeline object :-(
        self.udpipeline = None
        ## UDError object :-(
        self.uderror = None
        ## database of lexical unigram probabilities
        self.lexlogprobs = dict()
        ## database of tag unigram probabilities
        self.taglogprobs = dict()
        ## whether to lowercase and re-analyse if needed
        self.try_lowercase = True
        ## whether to Titlecase and re-analyse if needed
        self.try_titlecase = True
        ## whether to dEtitlecase and re-analyse if needed
        self.try_detitlecase = True
        ## whether to dEtitlecase and re-analyse if needed
        self.try_detitle_firstinsent = True
        ## whether to UPPERCASE and re-analyse if needed
        self.try_uppercase = False
        ## whether accept model is loaded
        self.can_accept = False
        ## whether analyser model is loaded
        self.can_analyse = False
        ## whether tokenisr model is loaded
        self.can_tokenise = True
        ## whether generator model is loaded
        self.can_generate = False
        ## whether lemmatising model is loaded
        self.can_lemmatise = False
        ## whether hypenation model is loaded
        self.can_hyphenate = False
        ## whether segmentation model is loaded
        self.can_segment = False
        ## whether label segmentation model is loaded
        self.can_labelsegment = False
        ## whether guesser model is loaded
        self.can_guess = False
        ## whether UDPipe is loaded
        self.can_udpipe = False

    def _load_hfst(self, f):
        """Load an automaton from file.

        Args:
            f:  containing single hfst automaton binary.

        Throws:
            FileNotFoundError if file is not found
        """
        try:
            his = libhfst.HfstInputStream(f)
            return his.read()
        except libhfst.NotTransducerStreamException:
            raise IOError(2, f) from None

    def load_labelsegmenter(self, f):
        """Load labeled segments model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.labelsegmenter = self._load_hfst(f)
        self.can_labelsegment = True

    def load_segmenter(self, f):
        """Load segmentation model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.segmenter = self._load_hfst(f)
        self.can_segment = True

    def load_analyser(self, f):
        """Load analysis model from a file.

        Args
            f: containing single hfst automaton binary.
        """
        self.analyser = self._load_hfst(f)
        self.can_analyse = True
        self.can_accept = True
        self.can_lemmatise = True

    def load_generator(self, f):
        """Load generation model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.generator = self._load_hfst(f)
        self.can_generate = True

    def load_acceptor(self, f):
        """Load acceptor model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.acceptor = self._load_hfst(f)
        self.can_accept = True

    def load_tokeniser(self, f):
        """Load tokeniser model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.tokeniser = self._load_hfst(f)
        self.can_tokenise = True

    def load_lemmatiser(self, f):
        """Load lemmatiser model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.tokeniser = self._load_hfst(f)
        self.can_lemmatise = True

    def load_hyphenator(self, f):
        """Load hyphenator model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.hyphenator = self._load_hfst(f)
        self.can_hyphenate = True

    def load_guesser(self, f):
        """Load guesser model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.guesser = self._load_hfst(f)
        self.can_guess = True

    def load_udpipe(self, filename: str):
        """Load UDPipe model for statistical parsing.

        UDPipe can be used as extra information source for OOV symbols
        or all tokens. It works best with sentence-based analysis, token
        based does not keep track of context.

        @param filename  path to UDPipe model
        """
        if not can_udpipe:
            print("importing udpipe failed, cannot load udpipe xxx")
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
                if self.accept(Token(token.surf[0].upper() +
                                     token.surf[1:].lower())):
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
                        postsurfs = ""
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

    def _analyse(self, token: Token):
        '''Analyse token using HFST and perform recasings.

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
            res = self.analyser.lookup(token.surf[0].lower() +
                                       token.surf[1:])
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
            omor = '[WORD_ID=' + token.surf.replace("=", ".EQ.") + '][UPOS=X]' +\
                   '[GUESS=UNKNOWN][WEIGHT=inf]'
            weight = float('inf')
            anal = Analysis.fromomor(omor, weight)
            anal.manglers.append("GUESSER=NONE")
            token.analyses.append(anal)
            return [anal]
        return anals

    def analyse_sentence(self, s):
        """Analyse a full sentence with tokenisation and guessing.

        for details of tokenisation, see @c tokenise(self, s).
        for details of analysis, see @c analyse(self, token).
        If further models like udpipe are loaded, may fill in gaps with that.
        """
        tokens = self.tokenise_sentence(s)
        if not tokens:
            errortoken = Token()
            errortoken.nontoken = "error"
            errortoken.error = "cannot tokenise sentence"
            errortoken.comment = {"sentence": s,
                                  "location": "analyse_sentence"}
            return [errortoken]
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
        return None

    def _guess_token(self, token: Token):
        '''Guess token reading using language models.

        Args:
            token: token to guess'''
        res = self.guesser.lookup(token.surf)
        for r in res:
            anal = r[0] + '[GUESS=FSA][WEIGHT=%f]' % (r[1])
            weight = float(r[1])
            guess = Analysis.fromomor(anal, weight)
            guess.manglers.append("GUESSER=FSA")
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
        s = token.surf
        trieds = {s}
        if len(s) > 2 and (s[0].islower() or s[1].isupper()) and \
                self.try_titlecase:
            tcs = s[0].upper() + s[1:].lower()
            if tcs not in trieds:
                tcres = self.analyser.lookup(tcs)
                for r in tcres:
                    mangler = 'Titlecased'
                    omor = r[0] + \
                        '[CASECHANGE=TITLECASED]' + \
                        '[WEIGHT=%f]' % (r[1] + self._penalty)
                    weight = r[1] + self._penalty
                    anal = Analysis.fromomor(omor, weight)
                    anal.manglers.append(mangler)
                    anal.analsurf = tcs
                    newanals.append(anal)
                trieds.add(tcs)
        if len(s) > 2 and s[0].isupper() and self.try_detitlecase:
            dts = s[0].lower() + s[1:]
            if dts not in trieds:
                dtres = self.analyser.lookup(dts)
                for r in dtres:
                    mangler = 'dETITLECASED'
                    omor = r[0] + \
                        "[CASECHANGE=DETITLECASED]" + \
                        "[WEIGHT=%f]" % (r[1] + self._penalty)
                    weight = r[1]
                    if token.pos != 1:
                        weight += self._penalty
                    anal = Analysis.fromomor(omor, weight)
                    anal.manglers.append(mangler)
                    anal.analsurf = dts
                    newanals.append(anal)
                trieds.add(dts)
        if not s.isupper() and self.try_uppercase:
            ups = s.upper()
            if ups not in trieds:
                upres = self.analyser.lookup(ups)
                for r in upres:
                    mangler = 'UPPERCASED'
                    omor = r[0] + \
                        "[CASECHANGE=UPPERCASED]" + \
                        "[WEIGHT=%f]" % (r[1] + self._penalty)
                    weight = r[1] + self._penalty
                    anal = Analysis.fromomor(omor, weight)
                    anal.manglers.append(mangler)
                    anal.analsurf = ups
                    newanals.append(anal)
                trieds.add(ups)
        if not s.islower() and self.try_lowercase:
            lows = s.lower()
            if lows not in trieds:
                lowres = self.analyser.lookup(lows)
                for r in lowres:
                    mangler = 'lowercased'
                    omor = r[0] +\
                        "[CASECHANGE=LOWERCASED]" + \
                        "[WEIGHT=%f]" % (r[1] + self._penalty)
                    weight = r[1] + self._penalty
                    anal = Analysis.fromomor(omor, weight)
                    anal.manglers.append(mangler)
                    anal.analsurf = lows
                    newanals.append(anal)
                trieds.add(lows)
        if not newanals:
            if len(token.surf) == 1:
                omor = '[WORD_ID=' + token.surf +\
                    "][UPOS=SYM][GUESS=HEUR]" +\
                    "[WEIGHT=%f]" % (self._penalty)
                weight = self._penalty
                guess = Analysis.fromomor(omor, weight)
                guess.manglers.append('GUESSER=PYTHON_LEN1')
                newanals.append(guess)
            elif token.surf[0].isupper() and len(token.surf) > 1:
                omor = '[WORD_ID=' + token.surf +\
                    "][UPOS=PROPN][NUM=SG][CASE=NOM][GUESS=HEUR]" +\
                    "[WEIGHT=%f]" % (self._penalty)
                weight = self._penalty
                guess = Analysis.fromomor(omor, weight)
                guess.manglers.append('GUESSER=PYTHON_0ISUPPER')
                newanals.append(guess)
            else:
                omor = '[WORD_ID=' + token.surf +\
                    "][UPOS=NOUN][NUM=SG][CASE=NOM][GUESS=HEUR]" +\
                    "[WEIGHT=%f]" % (self._penalty)
                weight = self._penalty
                guess = Analysis.fromomor(omor, weight)
                guess.manglers.append('GUESSER=PYTHON_ELSE')
                newanals.append(guess)
        for anal in newanals:
            token.analyses.append(anal)
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
        guesses = self._guess_heuristic(token)
        if self.can_udpipe:
            guesses += [self._udpipe(token.surf)]
        if self.can_guess:
            guesses += self._guess_token(token)
        return guesses

    def _lemmatise(self, token):
        res = self.lemmatiser.lookup(token.surf)
        newlemmas = list()
        for r in res:
            lemma = r[0]
            weight = float(r[1])
            anal = Analysis()
            anal.raw = lemma
            anal.rawtype = "lemma"
            anal.weight = weight
            newlemmas.append(anal)
        for lemma in newlemmas:
            token.lemmatisations.append(lemma)
        return newlemmas

    def lemmatise(self, token: Token):
        '''Lemmatise token, splitting it into valid word id's from lexical db.

        Side-effect:
            This operation stores lemmas in the token for future use and only
            returns HFST structures. Use Token's method's to retrieve tokens
            in pythonic structures.

        Args:
            token: token to lemmatise

        Returns:
            New lemmas in analysis list
        '''
        lemmas = None
        lemmas = self._lemmatise(token)
        if not lemmas or len(lemmas) < 1:
            lemma = token.surf
            weight = float('inf')
            guess = Analysis()
            guess.raw = lemma
            guess.rawtype = "lemma"
            guess.ewight = weight
            guess.manglers.append("GUESSER=SURFISLEMMA")
            token.lemmatisations.append(guess)
            lemmas = [guess]
        return lemmas

    def _segment(self, token: Token):
        '''Intenal segmenting using HFST automaton.

        Args:
            token: token to segment.'''
        res = self.segmenter.lookup(token.surf)
        newsegs = list()
        for r in res:
            segments = r[0]
            weight = float(r[1])
            anal = Analysis()
            anal.raw = segments
            anal.weight = weight
            anal.rawtype = "segments"
            newsegs.append(anal)
        for ns in newsegs:
            token.segmentations.append(ns)
        return newsegs

    def segment(self, token: Token):
        '''Segment token into morphs, words and other string pieces.

        Side-effect:
            this operation stores segments in the token for future
        use and only returns the HFST structures. To get pythonic data use
        Token's methods afterwards.

        Args:
            token: token to segment

        Returns:
            New segmentations in analysis list
        '''
        segments = None
        segments = self._segment(token)
        if not segments or len(segments) < 1:
            segments = token.surf
            weight = float('inf')
            guess = Analysis()
            guess.raw = segments
            guess.weight = weight
            guess.rawtype = "segments"
            guess.manglers.append("GUESSER=SURFISSEGMENT")
            token.segmentations.append(guess)
            segments = [guess]
        return segments

    def _labelsegment(self, token: Token):
        '''Internal implementation of segment label lookup with FSA.

        Args:
            token: token to analyse

        Returns:
            list of new labelsegment analyses.'''
        res = self.labelsegmenter.lookup(token.surf)
        newlabels = list()
        for r in res:
            labelsegments = r[0]
            weight = float(r[1])
            anal = Analysis()
            anal.raw = labelsegments
            anal.weight = weight
            anal.rawtype = "labelsegments"
            newlabels.append(anal)
        for ls in newlabels:
            token.labelsegmentations.append(ls)
        return newlabels

    def labelsegment(self, token: Token):
        '''Segment token into labelled morphs, words and other string pieces.

        The segments are suffixed with their morphologically relevant
        informations, e.g. lexical classes for root lexemes and inflectional
        features for inflectional segments. This functionality is experimental
        due to hacky way it was patched together.

        Side-effect:
            Note that this operation stores the labelsegments in the token for
        future use, and only returns raw HFST structures. To get pythonic
        you can use Token's methods afterwards.

        Args:
            token: token to segment with labels

        Returns:
            New labeled segemntations in analysis list.
        '''
        labelsegments = None
        labelsegments = self._labelsegment(token)
        if not labelsegments or len(labelsegments) < 1:
            labelsegments = token.surf + "|UNK"
            lsweight = float('inf')
            guess = Analysis()
            guess. raw = labelsegments
            guess.weight = lsweight
            guess.rawtype = "labelsegments"
            guess.manglers.append("GUESSER=SURFISLABELS")
            token.labelsegmentations.append(guess)
            labelsegments = [guess]
        return labelsegments

    def _accept(self, token: Token):
        """Look up token from acceptor model.

        Args:
            token: token to accept

        Returns:
            analyses of token"""
        if self.acceptor:
            res = self.acceptor.lookup(token.surf)
        elif self.analyser:
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

    def _generate(self, s: str):
        '''Generate surface forms from string using FSA model.

        Args:
            s: string matching raw omor analysis

        Returns:
            string containing surface forms
        '''
        res = self.generator.lookup(s)
        generations = []
        for r in res:
            generations += [r[0]]
        return "/".join(generations)

    def generate(self, omorstring: str):
        '''Generate surface forms corresponding given token description.

        Currently only supports very direct omor style analysis string
        generation.

        Args:
            omorstring: Omorfi analysis string to generate

        Returns
            A surface string word-form, or the omorstring argument if
            generation fails. Or None if generator is not loaded.
        '''
        generated = None
        if self.can_generate:
            generated = self._generate(omorstring)
            if not generated:
                return []
        return generated

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
            token.nontoken = "separator"
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
            sep.nontoken = "separator"
            tokens.append(sep)
            return tokens
        eoft = Token()
        eoft.nontoken = "eof"
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
                        print("Unkonown MISC", k, file=stderr)
                        exit(1)
            tokens.append(token)
        eoft = Token()
        eoft.nontoken = "eof"
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


def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSA', required=True,
                   help="Path to FSA analyser")
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    omorfi.load_analyser(options.fsa)
    if not options.infile:
        options.infile = stdin
    if options.verbose:
        print("reading from", options.infile.name)
    for line in options.infile:
        line = line.strip()
        if not line or line == '':
            continue
        surfs = omorfi.tokenise(line)
        for surf in surfs:
            anals = omorfi.analyse(surf)
            for anal in anals:
                print(anal)
            print()
    exit(0)


if __name__ == "__main__":
    main()
