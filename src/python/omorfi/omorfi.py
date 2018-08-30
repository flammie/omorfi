#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Simple python interface for omorfi using libhfst-python. Consider this
class as a standard python interface to omorfi and standard reference for
scientific studies, as far as python use goes. For other interfaces, see
the standard shell scripts or java interface.
"""


from argparse import ArgumentParser
from glob import glob
from os import F_OK, access, getenv
from sys import stderr, stdin
from math import log

from copy import copy

import libhfst

from .settings import fin_punct_leading, fin_punct_trailing
from .token import Token, is_tokenlist_oov

can_udpipe = True
try:
    from ufal.udpipe import Model, Pipeline, ProcessingError
except ImportError:
    can_udpipe = False


class Omorfi:

    """
    An object holding omorfi binariesfor all the functions of omorfi.

    The following functionalities use automata binaries that need to be loaded
    separately:
    * analysis
    * tokenisation
    * generation
    * lemmatisation
    * segmentation
    * lookup
    * guess

    There is python code to perform basic string munging controlled by following
    bool attributes:
        try_lowercase: to use `str.lower()`
        try_titlecase: to use `str[0].upper() + str[1:]`
        try_uppercase: to use `str.upper()`
        try_detitlecase: to use `str[0].lower + str[1:]`

    The annotations will be changed when transformation has been applied.
    """


    ## magic number for penalty weights
    _penalty = 28021984

    ## paths to search auto-detected models from
    _stdpaths = ['/usr/local/share/hfst/fi/',
                 '/usr/share/hfst/fi/',
                 '/usr/local/share/omorfi/',
                 '/usr/share/omorfi/',
                 './', 'generated/', 'src/generated/', '../src/generated/']

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

    def load_hfst(self, f):
        """Load an automaton from file.

        @param f containing single hfst automaton binary.
        """
        try:
            his = libhfst.HfstInputStream(f)
            return his.read()
        except libhfst.NotTransducerStreamException:
            raise IOError


    def load_labelsegmenter(self, f):
        """Load labeled segments model from a file.

        @param f containing single hfst automaton binary.
        @sa load_hfst(self, f)
        """
        self.labelsegmenter = self.load_hfst(f)
        self.can_labelsegment = True

    def load_segmenter(self, f):
        """Load segmentation model from a file.

        @param f containing single hfst automaton binary.
        @sa load_hfst(self, f)
        """
        self.segmenter = self.load_hfst(f)
        self.can_segment = True

    def load_analyser(self, f):
        """Load analysis model from a file.

        @param f containing single hfst automaton binary.
        @sa load_hfst(self, f)
        """
        self.analyser = self.load_hfst(f)
        self.can_analyse = True
        self.can_accept = True
        self.can_lemmatise = True

    def load_generator(self, f):
        """Load generation model from a file.

        @param f containing single hfst automaton binary.
        @sa load_hfst(self, f)
        """
        self.generator = self.load_hfst(f)
        self.can_generate = True

    def load_acceptor(self, f):
        """Load acceptor model from a file.

        @param f containing single hfst automaton binary.
        @sa load_hfst(self, f)
        """
        self.acceptor = self.load_hfst(f)
        self.can_accept = True

    def load_tokeniser(self, f):
        """Load tokeniser model from a file.

        @param f containing single hfst automaton binary.
        @sa load_hfst(self, f)
        """
        self.tokeniser = self.load_hfst(f)
        self.can_tokenise = True

    def load_lemmatiser(self, f):
        """Load lemmatiser model from a file.

        @param f containing single hfst automaton binary.
        @sa load_hfst(self, f)
        """
        self.tokeniser = self.load_hfst(f)
        self.can_lemmatise = True

    def load_hyphenator(self, f):
        """Load hyphenator model from a file.

        @param f containing single hfst automaton binary.
        @sa load_hfst(self, f)
        """
        self.hyphenator = self.load_hfst(f)
        self.can_hyphenate = True

    def load_guesser(self, f):
        """Load guesser model from a file.

        @param f containing single hfst automaton binary.
        @sa load_hfst(self, f)
        """
        self.guesser = self.load_hfst(f)
        self.can_guess = True

    def load_udpipe(self, filename):
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
        self.udpipeline = Pipeline(self.udpiper, 'horizontal', Pipeline.DEFAULT,
                                   Pipeline.DEFAULT, 'conllu')
        self.uderror = ProcessingError()
        ## udpipe is loaded
        self.can_udpipe = True

    def load_lexical_frequencies(self, lexfile):
        """Load a frequency list for lemmas. Experimental.
        Currently in uniq -c format, subject to change.

        @param filename path to file with frequencies.
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
                self.lexlogprobs[lex] = log(freq/lextotal)
            else:
                # XXX: hack hack, should just use LM count stuff with
                # discounts
                self.lexlogprobs[lex] = log(1/(lextotal + 1))

    def load_omortag_frequencies(self, omorfile):
        """Load a frequenc list for tags. Experimental.
        Currently in uniq -c format. Subject to change.

        @param filename path to file with frequencies.
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
                self.taglogprobs[omor] = log(freq/omortotal)
            else:
                # XXX: hack hack, should just use LM count stuff with
                # discounts
                self.taglogprobs[omor] = log(1/(omortotal + 1))


    def _find_retoken_recase(self, token):
        """Turns a string into a recased non-OOV token."""
        if self.accept(token):
            return token
        if len(token.surf) > 1:
            if self.try_titlecase and not token.surf[0].isupper():
                token.analsurf = token.surf[0].upper() + token[1:].lower()
                if self.accept(token):
                    token.recased = 'Titlecased'
                    return token
            if self.try_detitlecase and not token.surf[0].islower():
                token.analsurf = token.surf[0].lower() + token[1:]
                if self.accept(token):
                    token.recased = 'dETITLECASED'
                    return token
        if self.try_lowercase and token.surf.lower() != token.surf:
            token.analsurf = token.surf.lower()
            if self.accept(token):
                token.recased = 'lowercased'
                return token
        if self.try_uppercase and not token.surf.upper() != token.surf:
            token.analsurf = token.surf.upper()
            if self.accept(token):
                token.recased = 'UPPERCASED'
                return token
        return False

    def _find_retokens(self, token):
        """Turns a string into a list of likely tokens.

        Tries to strip punct tokens from left and right.
        """
        pretokens = []
        posttokens = []
        for i in range(4):
            for j in range(4):
                if len(token.surf) > (i + j):
                    if j == 0:
                        resurf = token.surf[i:]
                    else:
                        resurf = token.surf[i:-j]
                    presurfs = token.surf[:i]
                    postsurfs = token.surf[j:]
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
                    if self._find_retoken_recase(retoken):
                        return pretokens + [retoken] + posttokens
                    else:
                        continue
        # no acceptable substring inside, just strip puncts
        return [token]

    def _retokenise(self, tokens):
        """Takes list of string from and produces list of tokens.

        May change number of tokens. Should be used with result of split().
        """
        retokens = []
        for s in tokens:
            token = Token(s)
            for retoken in self._find_retokens(token):
                retokens.append(retoken)
        return retokens

    def fsa_tokenise(self, line):
        """Tokenise with FSA.

        @param line  string to tokenise
        """
        return None

    def python_tokenise(self, line):
        """Tokenise with python's basic string functions.

        @param line  string to tokenise
        """
        return self._retokenise(line.split())

    def tokenise(self, line):
        """Perform tokenisation with loaded tokeniser if any, or `split()`.

        If tokeniser is available, it is applied to input line and if
        result is achieved, it is split to tokens according to tokenisation
        strategy and returned as a list.

        If no tokeniser are present, or none give results, the line will be
        tokenised using python's basic string functions. If analyser is
        present, tokeniser will try harder to get some analyses for each
        token using hard-coded list of extra splits.
        """
        tokens = None
        if self.tokeniser:
            tokens = self.fsa_tokenise(line)
        if not tokens:
            tokens = self.python_tokenise(line)
        return tokens

    def _analyse_token(self, token):
        rv = []
        if token.firstinsent and self.try_detitle_firstinsent:
            # begin of sentence, etc. recasing extra
            res = self.analyser.lookup(token.surf[0].lower() + token.surf[1:])
            for r in res:
                rvtoken = copy(token)
                rvtoken.omor = r[0] + '[WEIGHT=%f]' % (r[1])
                rvtoken.weight = r[1]
                rv.append(rvtoken)
        if token.analsurf:
            # surface from already determined
            res = self.analyser.lookup(token.analsurf)
            for r in res:
                rvtoken = copy(token)
                rvtoken.omor = r[0] + '[WEIGHT=%f]' % (r[1])
                rvtoken.weight = r[1]
                rv.append(rvtoken)
        else:
            # use real surface case
            res = self.analyser.lookup(token.surf)
            for r in res:
                rvtoken = copy(token)
                rvtoken.analsurf = token.surf
                rvtoken.omor = r[0] + '[WEIGHT=%f]' % (r[1])
                rvtoken.omor = r[1]
                rv.append(rvtoken)
        if not token.analsurf and token.surf:
            # also guess other cases
            s = token.surf
            if len(s) > 2 and s[0].islower() and self.try_titlecase:
                tcs = s[0].upper() + s[1:].lower()
                if tcs != s:
                    tcres = self.analyser.lookup(tcs)
                    for r in tcres:
                        tctoken = copy(token)
                        tctoken.recased = 'Titlecased'
                        tctoken.analsurf = tcs
                        tctoken.omor = r[0] + \
                            '[CASECHANGE=TITLECASED][WEIGHT=%f]' % (r[1] +
                                                                    self._penalty)
                        tctoken.weight = r[1] + self._penalty
                        rv.append(tctoken)
            if len(s) > 2 and s[0].isupper() and self.try_detitlecase:
                dts = s[0].lower() + s[1:]
                if dts != s:
                    dtres = self.analyser.lookup(dts)
                    for r in dtres:
                        dttoken = copy(token)
                        dttoken.recased = 'dETITLECASED'
                        dttoken.analsurf = dts
                        dttoken.omor = r[0] + \
                                "[CASECHANGE=DETITLECASED][WEIGHT=%f]" % (r[1] +
                                                                          self._penalty)
                        dttoken.weight = r[1] + self._penalty
                        rv.append(dttoken)
            if not s.isupper() and self.try_uppercase:
                ups = s.upper()
                if ups != s:
                    upres = self.analyser.lookup(ups)
                    for r in upres:
                        uptoken = copy(token)
                        uptoken.recased = 'UPPERCASED'
                        uptoken.analsurf = ups
                        uptoken.omor = r[0] + \
                                "[CASECHANGE=UPPERCASED][WEIGHT=%f]" % (r[1] +
                                                                        self._penalty)
                        uptoken.weight = r[1] + self._penalty
                        rv.append(uptoken)
            if not s.islower() and self.try_lowercase:
                lows = s.lower()
                if lows != s:
                    lowres = self.analyser.lookup(lows)
                    for r in lowres:
                        lowtoken = copy(token)
                        lowtoken.recased = 'lowercased'
                        lowtoken.analsurf = lows
                        lowtoken.omor = r[0] +\
                                 "[CASECHANGE=LOWERCASED][WEIGHT=%f]" %(r[1] +
                                                                        self._penalty)
                        lowtoken.weight = r[1] + self._penalty
                        rv.append(lowtoken)
        return rv

    def analyse(self, token):
        """Perform a simple morphological analysis lookup.

        If try_titlecase does not evaluate to False,
        the analysis will also be performed with first letter
        uppercased and rest lowercased.
        If try_uppercase evaluates to not False,
        the analysis will also be performed on all uppercase variant.
        If try_lowercase evaluates to not False,
        the analysis will also be performed on all lowercase variant.

        The analyses with case mangling will have an additional element to them
        identifying the casing.
        """
        anals = self._analyse_token(token)
        if not anals:
            anal = copy(token)
            anal.omor = '[WORD_ID=%s][GUESS=UNKNOWN][WEIGHT=inf]' \
                        % (token.surf)
            anal.weight = float('inf')
            anal.oov = "Yes"
            anals = [anal]
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
            errortoken.error = "cannot tokenise sentence"
            errortoken.comment = {"sentence": s, "location": "analyse_sentence"}
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

    def _guess_token(self, token):
        res = self.guesser.lookup(token.surf)
        guesses = []
        for r in res:
            guesstoken = copy(token)
            guesstoken['anal'] = r[0] + '[GUESS=FSA][WEIGHT=%f]' % (r[1])
            guesstoken['weight'] = float(r[1])
            guesstoken['guess'] = 'FSA'
            guesses += [guesstoken]
        return guesses

    def _guess_heuristic(self, token):
        '''Heuristic guessing function written fully in python.

        This should always be the most simple basic backoff, e.g. noun singular
        nominative for everything.
        '''
        guesstoken = copy(token)
        if not token.surf:
            return [guesstoken]
        # woo advanced heuristics!!
        if token.surf[0].isupper() and len(token.surf) > 1:
            guesstoken.omor = '[WORD_ID=' + token.surf +\
                    "][UPOS=PROPN][NUM=SG][CASE=NOM][GUESS=HEUR]" +\
                     "[WEIGHT=%f]" %(self._penalty)
            guesstoken.weight = self._penalty
            guesstoken.guesser = 'PYTHON0ISUPPER'
        else:
            guesstoken.omor = '[WORD_ID=' + token.surf +\
                    "][UPOS=NOUN][NUM=SG][CASE=NOM][GUESS=HEUR]" +\
                     "[WEIGHT=%f]" %(self._penalty)
            guesstoken.weight = self._penalty
            guesstoken.guesser = 'PYTHONELSE'
        return [guesstoken]

    def guess(self, token):
        '''Speculate morphological analyses of OOV token.

        This method may use multiple information sources, but not the actual
        analyser. Therefore a typical use of this is after the analyse(token)
        function has failed. Note that some information sources perform badly
        when guessing without context, for these the analyse_sentence(sent) is
        the only option.
        '''
        guesses = self._guess_heuristic(token)
        if self.can_udpipe:
            guesses += [self._udpipe(token.surf)]
        if self.can_guess:
            guesses += self._guess_token(token)
        return guesses

    def _lemmatise(self, token):
        res = self.lemmatiser.lookup(token.surf)
        lemmas = []
        for r in res:
            lemmatoken = copy(token)
            lemmatoken.lemma = r[0]
            lemmatoken.lemmaweight = float(r[1])
            lemmas += [lemmatoken]
        return lemmas

    def lemmatise(self, token):
        '''Lemmatise a token, returning a dictionary ID.

        Like morphological analysis, can return more than one results, which
        are possible (combinations of) lexeme ids. If the token is not in the
        dictionary, the surface form is returned as most likely "lemma".
        '''
        lemmas = None
        lemmas = self._lemmatise(token)
        if not lemmas or len(lemmas) < 1:
            lemmatoken = copy(token)
            lemmatoken.lemma = lemmatoken.surf
            lemmatoken.lemmaweight = float('inf')
            lemmas = [lemmatoken]
        return lemmas

    def _segment(self, token):
        res = self.segmenter.lookup(token.surf)
        segmenteds = []
        for r in res:
            segmenttoken = copy(token)
            segmenttoken.segments = r[0]
            segmenttoken.segmentweight = float(r[1])
            segmenteds += [segmenttoken]
        return segmenteds

    def segment(self, token):
        '''Segment token into morphs, words and other string pieces.

        The segments come separated by some internal markers for different
        segment boundaries.
        '''
        segments = None
        segments = self._segment(token)
        if not segments or len(segments) < 1:
            segmenttoken = copy(token)
            segmenttoken.segments = segmenttoken.surf
            segments = [segmenttoken]
        return segments

    def _labelsegment(self, token):
        res = self.labelsegmenter.lookup(token.surf)
        lss = []
        for r in res:
            lstoken = copy(token)
            lstoken.labelsegments = r[0]
            lstoken.lsweight = float(r[1])
            lss += [lstoken]
        return lss

    def labelsegment(self, token):
        '''Segment token into labelled morphs, words and other string pieces.

        The segments are suffixed with their morphologically relevant
        informations, e.g. lexical classes for root lexemes and inflectional
        features for inflectional segments. This functionality is experimental
        due to hacky way it was patched together.
        '''
        labelsegments = None
        labelsegments = self._labelsegment(token)
        if not labelsegments or len(labelsegments) < 1:
            lstoken = copy(token)
            lstoken.labelsegments = lstoken['surf']
            lstoken.lsweight = float('inf')
            labelsegments = [lstoken]
        return labelsegments

    def _accept(self, token):
        """Look up token from acceptor model."""
        if self.acceptor:
            if token.analsurf:
                res = self.acceptor.lookup(token.analsurf)
            else:
                res = self.acceptor.lookup(token.surf)
        elif self.analyser:
            if token.analsurf:
                res = self.analyser.lookup(token.analsurf)
            else:
                res = self.analyser.lookup(token.surf)
        else:
            res = None
        return res

    def accept(self, token):
        '''Check if the token is in the dictionary or not.

        Returns False for OOVs, True otherwise. Note, that this is not
        necessarily more efficient than analyse(token)
        '''
        accept = False
        accepts = None
        accepts = self._accept(token)
        if accepts and len(accepts) > 0:
            accept = True
        else:
            accept = False
        return accept

    def _generate(self, token):
        res = self.generator.lookup(token.omor)
        generations = []
        for r in res:
            g = copy(token)
            g.surf = r[0]
            g.genweight = r[1]
            generations += [g]
        return generations

    def generate(self, omorstring):
        '''Generate surface forms corresponding given token description.

        Currently only supports very direct omor style analysis string
        generation. For round-tripping and API consistency you can also feed a
        token dict here.
        '''
        gentoken = Token()
        gentoken.omor = omorstring
        if self.can_generate:
            generated = self._generate(gentoken)
            if not generated:
                gentoken.surf = gentoken.omor
                gentoken.genweight = float('inf')
                generated = [gentoken]
        return generated

    def _udpipe(self, udinput):
        conllus = self.udpipeline.process(udinput, self.uderror)
        if self.uderror.occurred():
            return None
        tokens = []
        for conllu in conllus.split('\n'):
            if conllu.startswith('#'):
                continue
            elif conllu.strip() == '':
                continue
            tokens += [self._conllu2token(conllu)]
        return tokens

    def _conllu2token(self, conllu):
        return Token.fromconllu(conllu)


    def tokenise_sentence(self, sentence):
        '''tokenise a sentence.

        To be used when text is already sentence-splitted. If the
        text is plain text with sentence boundaries within lines,
        use

        @todo tokenise_text
        '''
        if not sentence or sentence == '':
            token = Token()
            token.nontoken = True
            token.comment = ''
            return [token]
        tokens = self.tokenise(sentence)
        pos = 1
        for token in tokens:
            if pos == 1:
                token.firstinsent = True
            else:
                token.firstinsent = False
            token.pos = pos
            pos += 1
        return tokens

    def tokenise_conllu(self, f):
        '''tokenise a conllu sentence or comment.

        Should be used a file-like iterable that has CONLL-U sentence or
        comment or empty block coming up.'''
        tokens = list()
        for line in f:
            fields = line.strip().split('\t')
            token = Token()
            if len(fields) != 10:
                if line.startswith('#'):
                    token.nontoken = True
                    token.comment = line.strip()
                    tokens.append(token)
                    return tokens
                elif line.strip() == '':
                    token.nontoken = True
                    token.comment = ''
                    tokens = [token]
                    return tokens
                else:
                    token.nontoken = True
                    token.error = line.strip()
                    tokens = [token]
                    return tokens
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
                    else:
                        print("Unknown MISC", k, file=stderr)
                        exit(1)
            tokens.append(token)
        return tokens

    def tokenise_vislcg(self, f):
        '''Tokenises a sentence from VISL-CG format data.'''
        tokens = list()
        pos = 1
        for line in f:
            token = Token()
            if not line or line == '':
                token.nontoken = True
                token.comment = ''
                tokens.append(token)
                return tokens
            elif line.startswith("#") or line.startswith("<"):
                token.nontoken = True
                token.comment = line.strip()
                tokens.append(token)
                return tokens
            elif line.startswith('"<') and line.endswith('>"'):
                token.surf = line[2:-2]
                if pos == 1:
                    token.firstinsent = True
                tokens.append(token)
                pos += 1
            elif line.startswith('\t"'):
                fields = line.strip().split()
                token.lemma = fields[1].strip('"')
            elif line.startswith(';\t"'):
                # gold?
                token.nontoken = True
                token.comment = line.strip()
            else:
                token.nontoken = True
                token.error = 'vislcg: ' + line.strip()


def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSAPATH',
                   help="Path to directory of HFST format automata")
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    if options.fsa:
        omorfi.load_from_dir(options.fsa)
    else:
        omorfi.load_from_dir()
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
