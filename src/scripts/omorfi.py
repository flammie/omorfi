#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple python interface for omorfi using libhfst-python.
"""


import libhfst
from argparse import ArgumentParser

from sys import stderr, stdin
from os import getenv, access, F_OK
from glob import glob

from convert_tag_format import convert_omor_tag

class Omorfi:
    """
    An object holding omorfi automata for all the functions of omorfi.
    """
    analysers = dict()
    tokenisers = dict()
    generators = dict()
    lemmatizers = dict()
    hyphenators = dict()
    segmenters = dict()
    can_lowercase = True
    can_titlecase = True
    can_uppercase = False
    _verbosity = False

    _stdpaths = ['/usr/local/share/hfst/fi/',
            '/usr/share/hfst/fi/',
            '/usr/local/share/omorfi/',
            '/usr/share/omorfi/']

    def __init__(this, verbosity = False):
        this._verbosity = verbosity

    def load_filename(this, path):
        """Load omorfi automaton from filename and guess its use.

        The current version uses filename to guess the use of automaton,
        future versions should use HFST header for that.
        """
        trans = None
        if this._verbosity:
            print('Loading file', path)
        if access(path, F_OK):
            trans = libhfst.HfstTransducer(libhfst.HfstInputStream(path))
        else:
            # FIXME: should fail
            if this._verbosity:
                print('No access')
            pass
        parts = path[path.rfind('/') + 1:path.rfind('.')].split('.')
        if this._verbosity:
            print('loaded', parts[0], "type", parts[1], 'identifying...')
        if parts[0] == 'morphology':
            this.analysers[parts[1]] = trans
        elif parts[0] == 'generate':
            this.generators[parts[1]] = trans
        elif parts[0] == 'dictionary':
            pass
        elif parts[0] == 'tokeniser':
            this.tokenisers[parts[1]] = trans
        elif parts[0] == 'lemmatize':
            this.lemmatizers[parts[1]] = trans
        elif parts[0] == 'hyphenate':
            this.hyphenators[parts[1]] = trans

    def load_from_dir(this, path=None):
        """Load omorfi automata from given or known locations.
        
        If path is given it should point to directory of automata,
        otherwise standard installation paths are tried. Currently standard
        linux install paths are all globbed in following order:

        /usr/local/share/hfst/fi/*.hfst
        /usr/share/hfst/fi/*.hfst
        /usr/local/share/omorfi/*.hfst
        /usr/share/omorfi/*.hfst
        getenv('HOME') + /.hfst/fi/*.hfst
        getenv('HOME') + /.omorfi/*.hfst

        Last two paths require getenv('HOME'). All automata matching
        glob *.hfst are loaded and stored in part of omorfi class appropriate
        for their usage.
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
            this.load_filename(filename)

    def _tokenise(this, line, automaton):
        return None

    def tokenise(this, line):
        """Perform tokenisation with loaded tokeniser if any, or split.

        If tokeniser is available, it is applied to input line and if
        result is achieved, it is split to tokens according to tokenisation
        strategy and returned as a list.

        If no tokeniser are present, or none give results, the line will be
        tokenised using python's basic string functions.
        """
        tokens = None
        if 'default' in this.tokenisers:
            tokens = this._tokenise(line, 'default')
        if not tokens:
            tokens = line.replace('.', ' .').split()
        return tokens

    def _analyse(this, token, automaton):
        res = libhfst.detokenize_paths(this.analysers[automaton].lookup_fd(token))
        if len(token) > 2 and token[0].islower() and not token[1:].islower() and this.can_titlecase:
            tcres = libhfst.detokenize_paths(this.analysers[automaton].lookup_fd(token[0].lower() + token[1:].lower()))
            for r in tcres:
                r.output = r.output + convert_omor_tag('[CASECHANGE=TITLECASED]',
                        automaton)
            res = res + tcres
        if not token.isupper() and this.can_uppercase:
            upres = libhfst.detokenize_paths(this.analysers[automaton].lookup_fd(token.upper()))
            for r in tupes:
                r.output = r.output + convert_omor_tag('[CASECHANGE=UPPERCASED]'.
                        automaton)
            res = res + tcres
        if not token.islower() and this.can_lowercase:
            lowres = libhfst.detokenize_paths(this.analysers[automaton].lookup_fd(token.lower()))
            for r in lowres:
                r.output = r.output + convert_omor_tag('[CASECHANGE=LOWERCASED]',
                        automaton)
            res += lowres
        for r in res:
            r.output = r.output + convert_omor_tag('[WEIGHT=%f]' %(r.weight),
                    automaton)
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
        identifying the casing, assuming the analyser variant has opening for
        one.
        """
        anals = None
        if 'default' in this.analysers:
            anals = this._analyse(token, 'default')
        if not anals and 'omor' in this.analysers:
            anals = this._analyse(token, 'omor')
        if not anals and 'ftb3' in this.analysers:
            anals = this._analyse(token, 'ftb3')
        if not anals:
            class FakeAnal():
                pass
            anal = FakeAnal()
            anal.output = '[GUESS=UNKNOWN]'
            anal.weight = float('inf')
            anals = [anal]
        return anals

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
