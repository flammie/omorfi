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

import libhfst

from .settings import fin_punct_leading, fin_punct_trailing

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
        ## whether to UPPERCASE and re-analyse if needed
        self.try_uppercase = False
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
        try:
            his = libhfst.HfstInputStream(f)
            return his.read()
        except libhfst.NotTransducerStreamException:
            raise IOError


    def load_labelsegmenter(self, f):
        self.labelsegmenter = self.load_hfst(f)
        self.can_labelsegment = True

    def load_segmenter(self, f):
        self.segmenter = self.load_hfst(f)
        self.can_segment = True

    def load_analyser(self, f):
        self.analyser = self.load_hfst(f)
        self.can_analyse = True

    def load_filename(self, path, **include):
        """Load omorfi automaton from filename and guess its use.

        A file name should consist of three parts separated by full stop.
        The second part must be a keyword describing the use of the
        automaton, first part is parsed as an identifier typically starting
        with the word omorfi, followed by any extras, such as the tagset for
        analysis or generation.

        The named arguments can include a name of automaton type as name,
        and truth value as value, for types of automata allowed to load.
        By default, the names `analyse`, `generate` and `segment` are loaded.
        Names not included are defaulted to False. E.g.,
        `omorfi.load_filename(fn, analyse=True)`
        will only load file named fn if it can be identified as omorfi
        analyser. This is best used in conjunction with omorfi.load_from_dir.
        """
        if len(include) == 0:
            include['analyse'] = True
            include['generate'] = True
            include['segment'] = True
            include['accept'] = True
        for ttype in ['analyse', 'generate', 'accept', 'tokenise', 'lemmatise',
                      'hyphenate', 'segment', 'labelsegment', 'guesser',
                      'udpipe']:
            if ttype not in include:
                include[ttype] = False
        parts = path[path.rfind('/') + 1:path.rfind('.')].split('.')
        if len(parts) != 2:
            if self._verbosity:
                print('not loaded', path)
        elif not parts[0] == 'omorfi':
            if self._verbosity:
                print('not omorfi', path)
        elif parts[1] == 'analyse' and include['analyse']:
            if self._verbosity:
                print('analyser', parts[0])
            self.analyser = load_analyser(path)
            ## analyser is loaded
            self.can_analyse = True
            ## acceptor is loaded
            self.can_accept = True
            ## lemmatiser is loaded
            self.can_lemmatise = True
        elif parts[1] == 'generate' and include['generate']:
            if self._verbosity:
                print('generator', parts[0])
            self.generator = his.read()
            ## generator is loaded
            self.can_generate = True
        elif parts[1] == 'accept' and include['accept']:
            if self._verbosity:
                print('acceptor', parts[0])
            self.acceptor = his.read()
            self.can_accept = True
        elif parts[1] == 'tokenise' and include['tokenise']:
            if self._verbosity:
                print('tokeniser', parts[0])
            self.tokeniser = his.read()
            ## tokeniser is loaded
            self.can_tokenise = True
        elif parts[1] == 'lemmatise' and include['lemmatise']:
            if self._verbosity:
                print('lemmatiser', parts[0])
            self.lemmatiser = his.read()
            self.can_lemmatise = True
        elif parts[1] == 'hyphenate' and include['hyphenate']:
            if self._verbosity:
                print('hyphenator', parts[0])
            self.hyphenator = his.read()
            ## hyphenator is loaded
            self.can_hyphenate = True
        elif parts[1] == 'segment' and include['segment']:
            if self._verbosity:
                print('segmenter', parts[0])
            self.segmenter = his.read()
            ## segmenter is loaded
            self.can_segment = True
        elif parts[1] == 'guesser' and include['guesser']:
            if self._verbosity:
                print('guesser', parts[0])
            self.guesser = his.read()
            ## guesserr is loaded
            self.can_guess = True
        elif parts[1] == 'labelsegment' and include['labelsegment']:
            if self._verbosity:
                print('labelsegmenter', parts[0])
            self.labelsegmenter = his.read()
            self.can_segment = True
        elif self._verbosity:
            print('skipped', parts)

    def _maybe_str2token(self, s):
        if isinstance(s, str):
            return {"surf": s}
        elif isinstance(s, dict):
            return s
        else:
            return {"error": "not a string or dict",
                    "location": "maybe_str2token",
                    "data": s}

    def load_from_dir(self, path=None, **include):
        """Load omorfi automata from given or known locations.

        If path is given it should point to directory of automata,
        otherwise standard installation paths are tried. Currently standard
        linux install paths are all globbed in following order:

        * /usr/local/share/hfst/fi/*.hfst
        * /usr/share/hfst/fi/*.hfst
        * /usr/local/share/omorfi/*.hfst
        * /usr/share/omorfi/*.hfst
        * getenv('HOME') + /.hfst/fi/*.hfst
        * getenv('HOME') + /.omorfi/*.hfst

        Last two paths require getenv('HOME'). All automata matching
        glob *.hfst are loaded and stored in part of omorfi class appropriate
        for their usage.

        They keyword args can be used to limit loading of automata. The name
        is analyser type and value is True.
        """
        homepaths = []
        if getenv('HOME'):
            home = getenv('HOME')
            homepaths = [home + '/.hfst/fi/',
                         home + '/.omorfi/']
        loadable = []
        if path:
            if self._verbosity:
                print('adding', path + '/*.hfst')
            loadable = glob(path + '/*.hfst')
        else:
            for sp in self._stdpaths + homepaths:
                if self._verbosity:
                    print('adding', sp + '/*.hfst')
                loadable += glob(sp + '/*.hfst')
        for filename in loadable:
            try:
                self.load_filename(filename, **include)
            except:
                print("broken HFST", filename, file=stderr)

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
            return {"surf": token, "analsurf": token, "recase": "ORIGINALCASE"}
        if self.try_lowercase and self.accept(token.lower()):
            return {"surf": token, "analsurf": token.lower(),
                    "recase": "LOWERCASED"}
        if self.try_uppercase and self.accept(token.upper()):
            return {"surf": token, analsurf: "token.upper()",
                    "recase": "UPPERCASED"}
        if len(token) > 1:
            if self.try_titlecase and \
                    self.accept(token[0].upper() + token[1:].lower()):
                return {"surf": token,
                        "analsurf": token[0].upper() + token[1:].lower(),
                        "recase": "TITLECASED"}
            if self.try_detitlecase and \
                    self.accept(token[0].lower() + token[1:]):
                return {"surf": token,
                        "analsurf": token[0].lower() + token[1:],
                        "recase": "DETITLECASED"}
        return False

    def _find_retokens(self, token):
        """Turns a string into a list of likely tokens."""
        retoken = self._find_retoken_recase(token)
        if retoken:
            return [retoken]
        # Word.
        if token[-1] in fin_punct_trailing:
            retoken = self._find_retoken_recase(token[:-1])
            if retoken:
                retoken['SpaceAfter'] = "No"
                return[retoken, {"surf": token[-1], "SpaceBefore": "No"}]
        # -Word
        if token[0] in fin_punct_leading:
            retoken = self._find_retoken_recase(token[1:])
            if retoken:
                retoken['SpaceBefore'] = 'No'
                return [{"surf": token[0], "SpaceAfter": "No"},
                        retoken]
        # "Word"
        if token[0] in fin_punct_leading and token[-1] in fin_punct_trailing:
            retoken = self._find_retoken_recase(token[1:-1])
            if retoken:
                retoken['SpaceBefore'] = 'No'
                retoken['SpaceAfter'] = 'No'
                return [
                        {"surf": token[0], "SpaceAfter": "No"},
                        retoken,
                        {"surf": token[-1], "SpaceBefore": "No"}]
        # word." or word",
        if len(token) > 2 and token[-1] in fin_punct_trailing and token[-2] in fin_punct_trailing:
            retoken = self._find_retoken_recase(token[:-2])
            if retoken:
                retoken["SpaceAfter"] = "No"
                return [
                    retoken,
                    {"surf": token[-2], "SpaceBefore": "No", "SpaceAfter": "No"},
                    {"surf": token[-1], "SpaceBefore": "No"}]
        # word.",
        if len(token) > 3 and token[-1] in fin_punct_trailing and token[-2] in fin_punct_trailing and token[-3] in fin_punct_trailing:
            retoken = self._find_retoken_recase(token[:-3])
            if retoken:
                retoken["SpaceAfter"] = "No"
                return [
                    retoken,
                    {"surf": token[-3], "SpaceBefore": "No", "SpaceAfter": "No"},
                    {"surf": token[-2], "SpaceBefore": "No", "SpaceAfter": "No"},
                    {"surf": token[-1], "SpaceBefore": "No"}]
        # "word."
        if len(token) > 3 and token[-1] in fin_punct_trailing and token[-2] in fin_punct_trailing and token[0] in fin_punct_leading:
            retoken = self._find_retoken_recase(token[1:-2])
            if retoken:
                retoken["SpaceAfter"] = "No"
                retoken["SpaceBefore"] = "No"
                return [
                        {"surf": token[0], "SpaceAfter": "No"},
                        retoken,
                        {"surf": token[-2], "SpaceBefore": "No",
                            "SpaceAfter": "No"},
                        {"surf": token[-1], "SpaceBefore": "No"}]
        # "word.",
        if len(token) > 4 and token[-1] in fin_punct_trailing and token[-2] in fin_punct_trailing and token[-3] in fin_punct_trailing and token[0] in fin_punct_leading:
            retoken = self._find_retoken_recase(token[1:-3])
            if retoken:
                retoken["SpaceAfter"] = "No"
                retoken["SpaceBefore"] = "No"
                return [
                        {"surf": token[0], "SpaceAfter": "No"},
                        retoken,
                        {"surf": token[-3], "SpaceBefore": "No",
                            "SpaceAfter": "No"},
                        {"surf": token[-2], "SpaceBefore": "No",
                            "SpaceAfter": "No"},
                        {"surf": token[-1], "SpaceBefore": "No"}]
        # ...non-word...
        pretokens = []
        posttokens = []
        while len(token) > 1 and token[-1] in fin_punct_trailing:
            posttokens = ([{"surf": token[-1], "SpaceBefore": "No"}]
                          + posttokens)
            token = token[:-1]
        while len(token) > 1 and token[0] in fin_punct_leading:
            pretokens += [{"surf": token[0], "SpaceAfter": "No"}]
            token = token[1:]
        lastresort = {"surf": token}
        if len(pretokens) > 0:
            lastresort['SpaceBefore'] = 'No'
        if len(posttokens) > 0:
            lastresort['SpaceAfter'] = 'No'
        return pretokens + [lastresort] + posttokens

    def _retokenise(self, tokens):
        """Takes list of string from and produces list of tokens.

        May change number of tokens. Should be used with result of split().
        """
        retokens = []
        for token in tokens:
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

    def _analyse_str(self, s):
        """Legacy function if you really need to analyse a string.

        Turn it into a token and analyse a token instead. This is not even the
        standard string mangling. Do not touch."""
        token = {"surf": s}
        res = self._analyse_token(token)
        if len(s) > 2 and s[0].islower() and self.try_titlecase:
            tcs = s[0].upper() + s[1:].lower()
            if s != tcs:
                tctoken = {"surf": s, "analsurf": tcs, "recase": 'Titlecased'}
                tcres = self._analyse_token(tctoken)
                for r in tcres:
                    r['anal'] += '[CASECHANGE=TITLECASED]'
                res = res + tcres
        if len(token) > 2 and s[0].isupper() and self.try_detitlecase:
            dts = s[0].lower() + s[1:]
            if dts != s:
                dttoken = {"surf": s, "analsurf": dts, "recase": "dETITLECASED"}
                dtres = self._analyse_token(dttoken)
                for r in dtres:
                    r['anal'] += '[CASECHANGE=DETITLECASED]'
                res = res + dtres
        if not s.isupper() and self.try_uppercase:
            ups = s.upper()
            if s != ups:
                uptoken = {"surf": s, "analsurf": ups, "recase": "UPPERCASED"}
                upres = self._analyse_token(uptoken)
                for r in upres:
                    r['anal'] += '[CASECHANGE=UPPERCASED]'
                res = res + upres
        if not s.islower() and self.try_lowercase:
            lows = s.lower()
            if s != lows:
                lowtoken = {"surf": s, "analsurf": lows, "recase": "lowercased"}
                lowres = self._analyse_token(lowtoken)
                for r in lowres:
                    r['anal'] += '[CASECHANGE=LOWERCASED]'
                res += lowres
        return res

    def _analyse_token(self, token):
        rv = []
        if "analsurf_override" in token:
            # begin of sentence, etc. recasing extra
            res = self.analyser.lookup(token["analsurf_override"])
            for r in res:
                rvtoken = token.copy()
                rvtoken['anal'] = r[0] + '[WEIGHT=%f]' % (r[1])
                rvtoken['weight'] = r[1]
                rv.append(rvtoken)
        if "analsurf" in token:
            # surface from already determined
            res = self.analyser.lookup(token["analsurf"])
            for r in res:
                rvtoken = token.copy()
                rvtoken['anal'] = r[0] + '[WEIGHT=%f]' % (r[1])
                rvtoken["weight"] = r[1]
                rv.append(rvtoken)
        else:
            # use real surface case
            res = self.analyser.lookup(token["surf"])
            for r in res:
                rvtoken = token.copy()
                rvtoken['analsurf'] = token["surf"]
                rvtoken['anal'] = r[0] + '[WEIGHT=%f]' % (r[1])
                rvtoken["weight"] = r[1]
                rv.append(rvtoken)
        if not "analsurf_override" in token and not "analsurf" in token:
            # also guess other cases
            s = token['surf']
            if len(s) > 2 and s[0].islower() and self.try_titlecase:
                tcs = s[0].upper() + s[1:].lower()
                if tcs != s:
                    tcres = self.analyser.lookup(tcs)
                    for r in tcres:
                        tctoken = token.copy()
                        tctoken['recase'] = 'Titlecased'
                        tctoken['analsurf'] = tcs
                        tctoken['anal'] = r[0] + \
                            '[CASECHANGE=TITLECASED][WEIGHT=%f]' % (r[1] +
                                    self._penalty)
                        tctoken["weight"] = r[1] + self._penalty
                        rv.append(tctoken)
            if len(token) > 2 and s[0].isupper() and self.try_detitlecase:
                dts = s[0].lower() + s[1:]
                if dts != s:
                    dtres = self.analyser.lookup(dts)
                    for r in dtres:
                        dttoken = token.copy()
                        dttoken['recase'] = 'dETITLECASED'
                        dttoken['analsurf'] = dts
                        dttoken['anal'] = r[0] + \
                                "[CASECHANGE=DETITLECASED][WEIGHT=%f]" % (r[1] +
                                        self._penalty)
                        dttoken["weight"] = r[1] + self._penalty
                        rv.append(dttoken)
            if not s.isupper() and self.try_uppercase:
                ups = s.upper()
                if ups != s:
                    upres = self.analyser.lookup(ups)
                    for r in upres:
                        uptoken = token.copy()
                        uptoken['recase'] = 'UPPERCASED'
                        uptoken['analsurf'] = ups
                        uptoken['anal'] = r[0] + \
                                "[CASECHANGE=UPPERCASED][WEIGHT=%f]" % (r[1] +
                                        self._penalty)
                        uptoken["weight"] = r[1] + self._penalty
                        rv.append(uptoken)
            if not s.islower() and self.try_lowercase:
                lows = s.lower()
                if lows != s:
                    lowres = self.analyser.lookup(lows)
                    for r in lowres:
                        lowtoken = token.copy()
                        lowtoken['recase'] = 'lowercased'
                        lowtoken['analsurf'] = lows
                        lowtoken['anal'] = r[0] +\
                                 "[CASECHANGE=LOWERCASED][WEIGHT=%f]" %(r[1] +
                                         self._penalty)
                        lowtoken["weight"] = r[1] + self._penalty
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
        anals = None
        if isinstance(token, str):
            anals = self._analyse_str(token)
        elif isinstance(token ,dict):
            anals = self._analyse_token(token)
        else:
            anals = [{"error": "token is not str or dict",
                "token": token, "location": "analyse()"}]
        if not anals:
            if isinstance(token, str):
                anal = {"anal": '[WORD_ID=%s][GUESS=UNKNOWN][WEIGHT=inf]' \
                        % (token), "weight": float('inf'), "OOV": "Yes",
                        "guess": "None"}
            elif isinstance(token, dict):
                anal = token.copy()
                anal["anal"] = '[WORD_ID=%s][GUESS=UNKNOWN][WEIGHT=inf]' \
                        % (token['surf'])
                anal["weight"] = float('inf')
                anal["OOV"] = "Yes"
                anal["guess"] = "None"
            else:
                anal = {"error": "token is not str or dict",
                        "token": token, "location": "analyse()"}
            anals = [anal]
        return anals

    def analyse_sentence(self, s):
        """Analyse a full sentence with tokenisation and guessing.

        for details of tokenisation, see @c tokenise(self, s).
        for details of analysis, see @c analyse(self, token).
        If further models like udpipe are loaded, may fill in gaps with that.
        """
        tokens = self.tokenise(s)
        if not tokens:
            tokens = [{"error": "cannot tokenise sentence",
                "sentence": s, "location": "analyse_sentence"}]
        analysis_lists = []
        i = 0
        for token in tokens:
            i += 1
            analysis_lists[i] += [self.analyse(token)]
        if self.can_udpipe:
            # N.B: I used the vertical input here
            udinput = '\n'.join([token["surf"] for token in tokens])
            uds = self.udpipe(udinput)
        if len(uds) == len(analysis_lists):
            for i in range(len(uds)):
                analsysis_lists[i] += [uds[i]]
        return None

    def _guess_str(self, s):
        token = {"surf": s}
        return self._guess_token(token)

    def _guess_token(self, token):
        res = self.guesser.lookup(token['surf'])
        guesses = []
        for r in res:
            guesstoken = token.copy()
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
        guesstoken = token.copy()
        # woo advanced heuristics!!
        if token['surf'][0].isupper() and len(token['surf']) > 1:
            guesstoken['anal'] = '[WORD_ID=' + token['surf'] +\
                    "][UPOS=PROPN][NUM=SG][CASE=NOM][GUESS=HEUR]" +\
                     "[WEIGHT=%f]" %( self._penalty )
            guesstoken['weight'] = self._penalty
            guesstoken['guess'] = 'PYTHON0ISUPPER'
        else:
            guesstoken['anal'] = '[WORD_ID=' + token['surf'] +\
                    "][UPOS=NOUN][NUM=SG][CASE=NOM][GUESS=HEUR]" +\
                     "[WEIGHT=%f]" %( self._penalty )
            guesstoken['weight'] = self._penalty
            guesstoken['guess'] = 'PYTHONELSE'
        return [guesstoken]

    def guess(self, token):
        '''Speculate morphological analyses of OOV token.

        This method may use multiple information sources, but not the actual
        analyser. Therefore a typical use of this is after the analyse(token)
        function has failed. Note that some information sources perform badly
        when guessing without context, for these the analyse_sentence(sent) is
        the only option.
        '''
        realtoken = self._maybe_str2token(token)
        guesses = self._guess_heuristic(realtoken)
        if self.can_udpipe:
            guesses += [self._udpipe(realtoken['surf'])]
        if self.can_guess:
            guesses += self._guess_token(realtoken)
        return guesses

    def _lemmatise(self, token):
        res = self.lemmatiser.lookup(token['surf'])
        lemmas = []
        for r in res:
            lemmatoken = token.copy()
            lemmatoken['lemma'] = r[0]
            lemmatoken['lemmaweight'] = float(r[1])
            lemmas += [lemmatoken]
        return lemmas

    def lemmatise(self, token):
        '''Lemmatise a token, returning a dictionary ID.

        Like morphological analysis, can return more than one results, which
        are possible (combinations of) lexeme ids. If the token is not in the
        dictionary, the surface form is returned as most likely "lemma".
        '''
        realtoken = self._maybe_str2token(token)
        lemmas = None
        lemmas = self._lemmatise(realtoken)
        if not lemmas or len(lemmas) < 1:
            lemmatoken = realtoken.copy()
            lemmatoken['lemma'] = lemmatoken['surf']
            lemmatoken['lemmaweight'] = float('inf')
            lemmas = [lemmatoken]
        return lemmas

    def _segment(self, token):
        res = self.segmenter.lookup(token['surf'])
        segmenteds = []
        for r in res:
            segmenttoken = token.copy()
            segmenttoken['segments'] = r[0]
            segmenttoken['segmentweight'] = float(r[1])
            segmenteds += [segmenttoken]
        return segmenteds

    def segment(self, token):
        '''Segment token into morphs, words and other string pieces.

        The segments come separated by some internal markers for different
        segment boundaries.
        '''
        realtoken = self._maybe_str2token(token)
        segments = None
        segments = self._segment(realtoken)
        if not segments or len(segments) < 1:
            segmenttoken = realtoken.copy()
            segmenttoken['segments'] = segmenttoken['surf']
            segments = [segmenttoken]
        return segments

    def _labelsegment(self, token):
        res = self.labelsegmenter.lookup(token['surf'])
        lss = []
        for r in res:
            lstoken = token.copy()
            lstoken['labelsegments'] = r[0]
            lstoken['lsweight'] = float(r[1])
            lss += [lstoken]
        return lss

    def labelsegment(self, token):
        '''Segment token into labelled morphs, words and other string pieces.

        The segments are suffixed with their morphologically relevant
        informations, e.g. lexical classes for root lexemes and inflectional
        features for inflectional segments. This functionality is experimental
        due to hacky way it was patched together.
        '''
        realtoken = self._maybe_str2token(token)
        labelsegments = None
        labelsegments = self._labelsegment(realtoken)
        if not labelsegments or len(labelsegments) < 1:
            lstoken = realtoken.copy()
            lstoken['labelsegments'] = lstoken['surf']
            lstoken['lsweight'] = float('inf')
            labelsegments = [lstoken]
        return labelsegments

    def _accept(self, token):
        """Look up token from acceptor model."""
        if self.acceptor:
            res = self.acceptor.lookup(token['surf'])
        elif self.analyser:
            res = self.analyser.lookup(token['surf'])
        else:
            res = None
        return res

    def accept(self, token):
        '''Check if the token is in the dictionary or not.

        Returns False for OOVs, True otherwise. Note, that this is not
        necessarily more efficient than analyse(token)
        '''
        realtoken = self._maybe_str2token(token)
        accept = False
        accepts = None
        accepts = self._accept(realtoken)
        if accepts and len(accepts) > 0:
            accept = True
        else:
            accept = False
        return accept

    def _generate(self, token):
        res = self.generator.lookup(token['anal'])
        generations = []
        for r in res:
            g = token.copy()
            g['surf'] = r[0]
            g['genweight'] = r[1]
            generations += [g]
        return generations

    def generate(self, omorstring):
        '''Generate surface forms corresponding given token description.

        Currently only supports very direct omor style analysis string
        generation. For round-tripping and API consistency you can also feed a
        token dict here.
        '''
        gentoken = {}
        if isinstance(omorstring, str):
            gentoken['anal'] = omorstring
        elif isinstance(omorstring, dict):
            # for round-tripping
            gentoken = omorstring
        else:
            gentoken = {'error': 'token not dict or string',
                    'location': 'generate()'}
        generateds = None
        if self.can_generate:
            generated = self._generate(gentoken)
            if not generated:
                gentoken['surf'] = gentoken['anal']
                gentoken['genweight'] = float('inf')
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
        fields = conllu.split()
        if len(fields) != 10:
            print("conllu2token conllu fail", fields)
        upos = fields[3]
        wordid = fields[2]
        surf = fields[1]
        ufeats = fields[5]
        misc = fields[9]
        analysis = '[WORD_ID=%s][UPOS=%s]%s[GUESS=UDPIPE]' %(wordid, upos,
                self._ufeats2omor(ufeats))
        token = {'anal': analysis, 'misc': misc, 'upos': upos, 'surf': surf,
                 'ufeats': ufeats}
        return token

    def _ufeats2omor(self, ufeats):
        return '[' + ufeats.replace('|', '][') + ']'

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
