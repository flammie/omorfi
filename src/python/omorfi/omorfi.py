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

import libhfst

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

    def __init__(self, verbosity=False):
        """Construct Omorfi with given verbosity for printouts."""
        self._verbosity = verbosity

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
                      'hyphenate', 'segment', 'labelsegment']:
            if ttype not in include:
                include[ttype] = False
        his = None
        if self._verbosity:
            print('Opening file', path)
        if access(path, F_OK):
            his = libhfst.HfstInputStream(path)
        else:
            # FIXME: should fail
            if self._verbosity:
                print('No access to ', path, file=stderr)
            pass
        parts = path[path.rfind('/') + 1:path.rfind('.')].split('.')
        if len(parts) != 2:
            if self._verbosity:
                print('not loaded', path)
        elif not parts[0].startswith('omorfi'):
            if self._verbosity:
                print('not omorfi', path)
        elif parts[1] == 'analyse' and include['analyse']:
            if self._verbosity:
                print('analyser', parts[0])
            self.analysers[parts[0]] = his.read()
        elif parts[1] == 'generate' and include['generate']:
            if self._verbosity:
                print('generator', parts[0])
            self.generators[parts[0]] = his.read()
        elif parts[1] == 'accept' and include['accept']:
            if self._verbosity:
                print('acceptor', parts[0])
            self.acceptors[parts[0]] = his.read()
        elif parts[1] == 'tokenise' and include['tokenise']:
            if self._verbosity:
                print('tokeniser', parts[0])
            self.tokenisers[parts[0]] = his.read()
        elif parts[1] == 'lemmatise' and include['lemmatise']:
            if self._verbosity:
                print('lemmatiser', parts[0])
            self.lemmatisers[parts[0]] = his.read()
        elif parts[1] == 'hyphenate' and include['hyphenate']:
            if self._verbosity:
                print('hyphenator', parts[0])
            self.hyphenators[parts[0]] = his.read()
        elif parts[1] == 'segment' and include['segment']:
            if self._verbosity:
                print('segmenter', parts[0])
            self.segmenters[parts[0]] = his.read()
        elif parts[1] == 'labelsegment' and include['labelsegment']:
            if self._verbosity:
                print('labelsegmenter', parts[0])
            self.labelsegmenters[parts[0]] = his.read()
        elif self._verbosity:
            print('skipped', parts)

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
            self.load_filename(filename, **include)

    def _find_retoken_recase(self, token):
        if self.accept(token):
            return (token, "ORIGINALCASE")
        if self.can_lowercase and self.accept(token.lower()):
            return (token.lower(), "LOWERCASED=" + token)
        if self.can_uppercase and self.accept(token.upper()):
            return (token.upper(), "UPPERCASED=" + token)
        if len(token) > 1:
            if self.can_titlecase and self.accept(token[0].upper() + token[1:]):
                return (token[0].upper() + token[1:], "TITLECASED=" + token)
            if self.can_detitlecase and self.accept(token[0].lower() + token[1:]):
                return (token[0].lower() + token[1:], "DETITLECASED=" + token)
        return False

    def _find_retokens(self, token):
        retoken = self._find_retoken_recase(token)
        if retoken:
            return [retoken]
        # Word.
        if token[-1] in fin_punct_trailing:
            retoken = self._find_retoken_recase(token[:-1])
            if retoken:
                return[(retoken[0], retoken[1] + "|SpaceAfter=No"),
                       (token[-1], "SpaceBefore=No")]
        # -Word
        if token[0] in fin_punct_leading:
            retoken = self._find_retoken_recase(token[1:])
            if retoken:
                return [(token[0], "SpaceAfter=No"),
                        (retoken[0], retoken[1] + "|SpaceBefore=No")]
        # "Word"
        if token[0] in fin_punct_leading and token[-1] in fin_punct_trailing:
            retoken = self._find_retoken_recase(token[1:-1])
            if retoken:
                return [
                    (token[0], "SpaceAfter=No"),
                    (retoken[0], retoken[1] + "|SpaceBefore=No|SpaceAfter=No"),
                    (token[-1], "SpaceBefore=No")]
        # word." or word",
        if len(token) > 2 and token[-1] in fin_punct_trailing and token[-2] in fin_punct_trailing:
            retoken = self._find_retoken_recase(token[:-2])
            if retoken:
                return [
                    (retoken[0], retoken[1] + "|SpaceAfter=No"),
                    (token[-2], "SpaceBefore=No|SpaceAfter=No"),
                    (token[-1], "SpaceBefore=No")]
        # word.",
        if len(token) > 3 and token[-1] in fin_punct_trailing and token[-2] in fin_punct_trailing and token[-3] in fin_punct_trailing:
            retoken = self._find_retoken_recase(token[:-3])
            if retoken:
                return [
                    (retoken[0], retoken[1] + "|SpaceAfter=No"),
                    (token[-3], "SpaceBefore=No|SpaceAfter=No"),
                    (token[-2], "SpaceBefore=No|SpaceAfter=No"),
                    (token[-1], "SpaceBefore=No")]
        # "word."
        if len(token) > 3 and token[-1] in fin_punct_trailing and token[-2] in fin_punct_trailing and token[0] in fin_punct_leading:
            retoken = self._find_retoken_recase(token[1:-2])
            if retoken:
                return [
                    (token[0], "SpaceAfter=No"),
                    (retoken[0], retoken[1] + "|SpaceBefore=No|SpaceAfter=No"),
                    (token[-2], "SpaceBefore=No|SpaceAfter=No"),
                    (token[-1], "SpaceBefore=No")]
        # "word.",
        if len(token) > 4 and token[-1] in fin_punct_trailing and token[-2] in fin_punct_trailing and token[-3] in fin_punct_trailing and token[0] in fin_punct_leading:
            retoken = self._find_retoken_recase(token[1:-3])
            if retoken:
                return [
                    (token[0], "SpaceAfter=No"),
                    (retoken[0], retoken[1] + "|SpaceBefore=No|SpaceAfter=No"),
                    (token[-3], "SpaceBefore=No|SpaceAfter=No"),
                    (token[-2], "SpaceBefore=No|SpaceAfter=No"),
                    (token[-1], "SpaceBefore=No")]
        return [(token, "UNTOKENISED")]

    def _retokenise(self, tokens):
        retokens = []
        for token in tokens:
            for retoken in self._find_retokens(token):
                retokens.append(retoken)
        return retokens

    def _tokenise(self, line, automaton):
        return None

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
        if 'omorfi' in self.tokenisers:
            tokens = self._tokenise(line, 'omorfi')
        if not tokens:
            tokens = self._retokenise(line.split())
        return tokens

    def _analyse_str(self, s, automaton):
        token = (s, "")
        res = self._analyse_token(token, automaton)
        if len(s) > 2 and s[0].islower() and self.can_titlecase:
            tcs = s[0].upper() + s[1:]
            if s != tcs:
                tctoken = (tcs, 'TitleCased=' + s)
                tcres = self._analyse_token(tctoken, automaton)
                res = res + tcres
        if len(token) > 2 and token[0].isupper() and self.can_detitlecase:
            dts = s[0].lower() + s[1:]
            if dts != s:
                dttoken = (dts, "DetitleCased=" + s)
                dtres = self._analyse_token(dttoken, automaton)
                res = res + dtres
        if not s.isupper() and self.can_uppercase:
            ups = s.upper()
            if s != ups:
                uptoken = (ups, "UpperCased=" + s)
                upres = self._analyse_token(uptoken, automaton)
                res = res + upres
        if not s.islower() and self.can_lowercase:
            lows = s.lower()
            if s != lows:
                lowtoken = (lows, "LowerCased=" + s)
                lowres = self._analyse_token(lowtoken, automaton)
                res += lowres
        return res

    def _analyse_token(self, token, automaton):
        res = self.analysers[automaton].lookup(token[0])
        for r in res:
            r = (r[0] + '[WEIGHT=%f]' % (r[1]), r[1])
        return res

    def analyse(self, token):
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
        if 'default' in self.analysers:
            if isinstance(token, str):
                anals = self._analyse_str(token, 'default')
            else:
                anals = self._analyse_token(token, 'default')
        if not anals and 'omorfi-omor' in self.analysers:
            if isinstance(token, str):
                anals = self._analyse_str(token, 'omorfi-omor')
            else:
                anals = self._analyse_token(token, 'omorfi-omor')
            if not anals:
                anal = ('[WORD_ID=%s][GUESS=UNKNOWN][WEIGHT=inf]' % (token[0]),
                        float('inf'))
                anals = [anal]
        if not anals and len(self.analysers):
            anals = self._analyse(token, self.analysers.keys[0])
            if not anals:
                anal = ('[WORD_ID=%s]' % (token[0]) + '[GUESS=UNKNOWN][WEIGHT=inf]',
                        float('inf'))
                anals = [anal]
        return anals

    def _lemmatise(self, token, automaton):
        res = self.lemmatisers[automaton].lookup(token)
        return res

    def lemmatise(self, token):
        lemmas = None
        if 'default' in self.lemmatisers:
            lemmas = self._lemmatise(token, 'default')
        if not lemmas and 'omorfi' in self.lemmatisers:
            lemmas = self._lemmatise(token, 'omorfi')
            if not lemmas:
                lemma = (token, float('inf'))
                lemmas = [lemma]
        return lemmas

    def _segment(self, token, automaton):
        res = self.segmenters[automaton].lookup(token)
        return res

    def segment(self, token):
        segments = None
        if 'default' in self.segmenters:
            segments = self._segment(token, 'default')
        if not segments and 'omorfi' in self.segmenters:
            segments = self._segment(token, 'omorfi')
            if not segments:
                segment = (token, float('inf'))
                segments = [segment]
        return segments

    def _labelsegment(self, token, automaton):
        res = self.labelsegmenters[automaton].lookup(token)
        return res

    def labelsegment(self, token):
        labelsegments = None
        if 'default' in self.labelsegmenters:
            labelsegments = self._labelsegment(token, 'default')
        if not labelsegments and 'omorfi' in self.labelsegmenters:
            labelsegments = self._labelsegment(token, 'omorfi')
            if not labelsegments:
                labelsegment = (token, float('inf'))
                labelsegments = [labelsegment]
        return labelsegments

    def _accept(self, token, automaton):
        res = self.acceptors[automaton].lookup(token)
        return res

    def accept(self, token):
        accept = False
        accepts = None
        if 'default' in self.acceptors:
            accepts = self._accept(token, 'default')
        if not accepts and 'omorfi' in self.acceptors:
            accepts = self._accept(token, 'omorfi')
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
                print("\t", anal[0], sep='', end='')
            print()
    exit(0)

if __name__ == "__main__":
    main()
