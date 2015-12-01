#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Simple python interface for omorfi using libhfst-python. Consider this
class as a standard python interface to omorfi and standard reference for
scientific studies, as far as python use goes. For other interfaces, see
the standard shell scripts or java interface.
"""


import libhfst
from argparse import ArgumentParser

from sys import stderr, stdin
from os import getenv, access, F_OK
from glob import glob

from .settings import fin_punct_leading, fin_punct_trailing

class Omorfi:
    """
    An object holding omorfi automata for all the functions of omorfi.

    Each of the automata are accessible by their function and identifier.
    Some combinations of functionalities may be available that access more
    than one automaton in non-trivial ways. Currently supported automata
    functuions are:
    * analysis
    * tokenisation
    * generation
    * lemmatisation
    * segmentation
    * lookup

    These are followed by corresponding automaton sets as attributes:
        analysers: key is 'omorfi-' + tagset
        tokenisers: key is 'omorfi'
        generators: key is 'omorfi-' + tagset
        lemmatisers: key is 'omorfi'
        hyphenators: key is 'omorfi'
        segmenters: key is 'omorfi'

    The python code can perform minimal string munging controlled by bool
    attributes:
        can_lowercase: to use `str.lower()`
        can_titlecase: to use `str[0].upper() + str[1:]`
        can_uppercase: to use `str.upper()`
        can_detitlecase: to use `str[0].lower + str[1:]`

    The annotations will be changed if transformation has been applied.
    """
    analysers = dict()
    tokenisers = dict()
    generators = dict()
    lemmatisers = dict()
    hyphenators = dict()
    segmenters = dict()
    labelsegmenters = dict()
    acceptors = dict()
    can_lowercase = True
    can_titlecase = True
    can_detitlecase = True
    can_uppercase = False
    _verbosity = False

    _stdpaths = ['/usr/local/share/hfst/fi/',
            '/usr/share/hfst/fi/',
            '/usr/local/share/omorfi/',
            '/usr/share/omorfi/']

    def __init__(this, verbosity = False):
        """Construct Omorfi with given verbosity for printouts."""
        this._verbosity = verbosity

    def load_filename(this, path, **include):
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
        trans = None
        if len(include) == 0:
            include['analyse'] = True
            include['generate'] = True
            include['segment'] = True
            include['accept'] = True
        for ttype in ['analyse', 'generate', 'accept', 'tokenise', 'lemmatise',
                'hyphenate', 'segment', 'labelsegment']:
            if not ttype in include:
                include[ttype] = False
        if this._verbosity:
            print('Loading file', path)
        if access(path, F_OK):
            trans = libhfst.HfstTransducer(libhfst.HfstInputStream(path))
        else:
            # FIXME: should fail
            if this._verbosity:
                print('No access to ', path, file=stderr)
            pass
        parts = path[path.rfind('/') + 1:path.rfind('.')].split('.')
        if len(parts) < 2:
            if this._verbosity:
                print('not loaded', path)
        elif parts[1] == 'analyse' and include['analyse']:
            if this._verbosity:
                print('analyser', parts[0])
            this.analysers[parts[0]] = trans
        elif parts[1] == 'generate' and include['generate']:
            if this._verbosity:
                print('generator', parts[0])
            this.generators[parts[0]] = trans
        elif parts[1] == 'accept' and include['accept']:
            if this._verbosity:
                print('acceptor', parts[0])
            this.acceptors[parts[0]] = trans
        elif parts[1] == 'tokenise' and include['tokenise']:
            if this._verbosity:
                print('tokeniser', parts[0])
            this.tokenisers[parts[0]] = trans
        elif parts[1] == 'lemmatise' and include['lemmatise']:
            if this._verbosity:
                print('lemmatiser', parts[0])
            this.lemmatisers[parts[0]] = trans
        elif parts[1] == 'hyphenate' and include['hyphenate']:
            if this._verbosity:
                print('hyphenator', parts[0])
            this.hyphenators[parts[0]] = trans
        elif parts[1] == 'segment' and include['segment']:
            if this._verbosity:
                print('segmenter', parts[0])
            this.segmenters[parts[0]] = trans
        elif parts[1] == 'labelsegment' and include['labelsegment']:
            if this._verbosity:
                print('labelsegmenter', parts[0])
            this.labelsegmenters[parts[0]] = trans
        elif this._verbosity:
            print('skipped', parts)

    def load_from_dir(this, path=None, **include):
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
        res = None
        if getenv('HOME'):
            home = getenv('HOME')
            homepaths = [home + '/.hfst/fi/',
                          home + '/.omorfi/' ]
        loadable = []
        if path:
            if this._verbosity:
                print('adding', path + '/*.hfst')
            loadable = glob(path + '/*.hfst')
        else:
            for sp in this._stdpaths + homepaths:
                if this._verbosity:
                    print('adding', sp + '/*.hfst')
                loadable += glob(sp + '/*.hfst')
        for filename in loadable:
            this.load_filename(filename, **include)

    def _find_retokens(this, token):
        if this.accept(token):
            return [token]
        if this.can_lowercase and this.accept(token.lower()):
            return [token.lower()]
        if this.can_uppercase and this.accept(token.upper()):
            return [token.upper()]
        if token[-1] in fin_punct_trailing and this.accept(token[:-1]):
            return [token[:-1], token[-1]]
        if token[0] in fin_punct_leading and this.accept(token[1:]):
            return [token[0], token[1:]]
        if token[0] in fin_punct_leading and token[-1] in fin_punct_trailing and this.accept(token[1:-1]):
            return [token[0], token[1:-1], token[-1]]
        if len(token) > 2 and token[-1] in fin_punct_trailing and token[-2] in fin_punct_trailing and this.accept(token[:-2]):
            return [token[:-2], token[-2], token[-1]]
        if len(token) > 3 and token[-1] in fin_punct_trailing and token[-2] in fin_punct_trailing and token[-3] in fin_punct_trailing and this.accept(token[:-3]):
            return [token[:-3], token[-3], token[-2], token[-1]]
        return [token]



    def _retokenise(this, tokens):
        retokens = []
        for token in tokens:
            for retoken in this._find_retokens(token):
                retokens.append(retoken)
        return retokens

    def _tokenise(this, line, automaton):
        return None

    def tokenise(this, line):
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
        if 'omorfi' in this.tokenisers:
            tokens = this._tokenise(line, 'omorfi')
        if not tokens:
            tokens = this._retokenise(line.split())
        return tokens

    def _analyse(this, token, automaton):
        res = libhfst.detokenize_paths(this.analysers[automaton].lookup_fd(token))
        if len(token) > 2 and token[0].islower() and this.can_titlecase:
            tctoken = token[0].upper() + token[1:]
            if tctoken != token:
                tcres = libhfst.detokenize_paths(this.analysers[automaton].lookup_fd(tctoken))
                for r in tcres:
                    r.output = r.output + '[CASECHANGE=TITLECASED]'
                res = res + tcres
        if len(token) > 2 and token[0].isupper() and this.can_detitlecase:
            dttoken = token[0].lower() + token[1:]
            if dttoken != token:
                dtres = libhfst.detokenize_paths(this.analysers[automaton].lookup_fd(dttoken))
                for r in dtres:
                    r.output = r.output + '[CASECHANGE=DETITLECASED]'
                res = res + dtres
        if not token.isupper() and this.can_uppercase:
            uptoken = token.upper()
            if token != uptoken:
                upres = libhfst.detokenize_paths(this.analysers[automaton].lookup_fd(uptoken))
                for r in upres:
                    r.output = r.output + '[CASECHANGE=UPPERCASED]'
                res = res + upres
        if not token.islower() and this.can_lowercase:
            lowtoken = token.lower()
            if token !=  lowtoken:
                lowres = libhfst.detokenize_paths(this.analysers[automaton].lookup_fd(token.lower()))
                for r in lowres:
                    r.output = r.output + '[CASECHANGE=LOWERCASED]'
                res += lowres
        for r in res:
            r.output = r.output + '[WEIGHT=%f]' %(r.weight)
        return res

    def analyse(this, token):
        """Perform a simple morphological analysis lookup.

        If can_titlecase does not evaluate to False,
        the analysis will also be performed with first letter
        uppercased and rest lowercased.
        If can_uppercase evaluates to not False,
        the analysis will also be performed on all uppercase variant.
        If can_lowercase evaluates to not False,
        the analysis will also be performed on all lowercase variant.
        
        The analyses with case mangling will have an additional element to them
        identifying the casing.
        """
        anals = None
        if 'default' in this.analysers:
            anals = this._analyse(token, 'default')
        if not anals and 'omorfi-omor' in this.analysers:
            anals = this._analyse(token, 'omorfi-omor')
            if not anals:
                class FakeAnal():
                    pass
                anal = FakeAnal()
                anal.output = '[WORD_ID=%s][GUESS=UNKNOWN][WEIGHT=inf]' % (token)
                anal.weight = float('inf')
                anals = [anal]
        if not anals and len(this.analysers):
            anals = this._analyse(token, this.analysers.keys[0])
            if not anals:
                class FakeAnal():
                    pass
                anal = FakeAnal()
                anal.output = '[WORD_ID=%s]' % (token) + '[GUESS=UNKNOWN][WEIGHT=inf]'
                anal.weight = float('inf')
                anals = [anal]
        return anals

    def _lemmatise(this, token, automaton):
        res = libhfst.detokenize_paths(this.lemmatisers[automaton].lookup_fd(token))
        return res

    def lemmatise(this, token):
        lemmas = None
        if 'default' in this.lemmatisers:
            lemmas = this._lemmatise(token, 'default')
        if not lemmas and 'omorfi' in this.lemmatisers:
            lemmas = this._lemmatise(token, 'omorfi')
            if not lemmas:
                class FakeLemma():
                    pass
                lemma = FakeLemma()
                lemma.output = token
                lemma.weight = float('inf')
                lemmas = [lemma]
        return lemmas

    def _segment(this, token, automaton):
        res = libhfst.detokenize_paths(this.segmenters[automaton].lookup_fd(token))
        return res

    def segment(this, token):
        segments = None
        if 'default' in this.segmenters:
            segments = this._segment(token, 'default')
        if not segments and 'omorfi' in this.segmenters:
            segments = this._segment(token, 'omorfi')
            if not segments:
                class FakeSegment():
                    pass
                segment = FakeSegment()
                segment.output = token
                segment.weight = float('inf')
                segments = [segment]
        return segments

    def _labelsegment(this, token, automaton):
        res = libhfst.detokenize_paths(this.labelsegmenters[automaton].lookup_fd(token))
        return res

    def labelsegment(this, token):
        labelsegments = None
        if 'default' in this.labelsegmenters:
            labelsegments = this._labelsegment(token, 'default')
        if not labelsegments and 'omorfi' in this.labelsegmenters:
            labelsegments = this._labelsegment(token, 'omorfi')
            if not labelsegments:
                class FakeSegment():
                    pass
                labelsegment = FakeSegment()
                labelsegment.output = token
                labelsegment.weight = float('inf')
                labelsegments = [labelsegment]
        return labelsegments

    def _accept(this, token, automaton):
        res = libhfst.detokenize_paths(this.acceptors[automaton].lookup_fd(token))
        return res

    def accept(this, token):
        accept = False
        accepts = None
        if 'default' in this.acceptors:
            accepts = this._accept(token, 'default')
        if not accepts and 'omorfi' in this.acceptors:
            accepts = this._accept(token, 'omorfi')
        if accepts:
            accept = True
        return accept

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
            print(surf, end='')
            for anal in anals:
                print("\t", anal.output, sep='', end='')
            print()
    exit(0)

if __name__ == "__main__":
    main()
