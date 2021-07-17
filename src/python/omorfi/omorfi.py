#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Simple python interface for omorfi using libhfst-python. Consider this
class as a standard python interface to omorfi and standard reference for
scientific studies, as far as python use goes. For other interfaces, see
the standard shell scripts or java interface.
"""

import sys

from argparse import ArgumentParser

from .token import Token
from .analyser import Analyser
from .generator import Generator
from .segmenter import Segmenter
from .tokeniser import Tokeniser
from .labelsegmenter import LabelSegmenter
from .lemmatiser import Lemmatiser
from .hyphenator import Hyphenator
from .guesser import Guesser


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
        self.analyser = Analyser()
        ## tokeniser
        self.tokeniser = Tokeniser()
        ## generator model
        self.generator = Generator()
        ## lemmatising model
        self.lemmatiser = Lemmatiser()
        ## hyphenating model
        self.hyphenator = Hyphenator()
        ## segmenting model
        self.segmenter = Segmenter()
        ## label-segment model
        self.labelsegmenter = LabelSegmenter()
        ## acceptor
        self.acceptor = None
        ## guesser model
        self.guesser = Guesser()
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

    def load_labelsegmenter(self, f):
        """Load labeled segments model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.labelsegmenter.load_labeller(f)
        self.can_labelsegment = True

    def load_segmenter(self, f):
        """Load segmentation model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.segmenter.load_segmenter(f)
        self.can_segment = True

    def load_analyser(self, f):
        """Load analysis model from a file. Also sets up a basic tokeniser and
        lemmatiser using the analyser.

        Args
            f: containing single hfst automaton binary.
        """
        self.analyser.load_analyser(f)
        self.can_analyse = True
        self.can_accept = True
        self.lemmatiser.use_analyser(self.analyser)
        self.can_lemmatise = True
        self.tokeniser.use_analyser(self.analyser)
        self.can_tokenise = True
        self.guesser.use_analyser(self.analyser)

    def load_generator(self, f):
        """Load generation model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.generator = Generator(f)
        self.can_generate = True

    def load_acceptor(self, f):
        """Load acceptor model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.acceptor = Analyser(f)
        self.can_accept = True

    def load_tokeniser(self, f):
        """Load tokeniser model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.tokeniser = Tokeniser(f)
        self.can_tokenise = True

    def load_lemmatiser(self, f):
        """Load lemmatiser model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.lemmatiser = Lemmatiser(f)
        self.can_lemmatise = True

    def load_hyphenator(self, f):
        """Load hyphenator model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.hyphenator = Hyphenator(f)
        self.can_hyphenate = True

    def load_guesser(self, f):
        """Load guesser model from a file.

        Args:
            f: containing single hfst automaton binary.
        """
        self.guesser = Guesser(f)
        self.can_guess = True

    def load_udpipe(self, filename: str):
        """Load UDPipe model for statistical parsing.

        UDPipe can be used as extra information source for OOV symbols
        or all tokens. It works best with sentence-based analysis, token
        based does not keep track of context.

        @param filename  path to UDPipe model
        """
        self.analyser.load_udpipe(filename)

    def fsa_tokenise(self, line: str):
        """Tokenise with FSA.

        Args:
            line:  string to tokenise

        Todo:
            Not implemented (needs pmatch python support)
        """
        return self.tokeniser.fsa_tokenise(line)

    def python_tokenise(self, line: str):
        """Tokenise with python's basic string functions.

        Args:
            line:  string to tokenise
        """
        return self.tokeniser.python_tokenise(line)

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
        return self.tokeniser.tokenise(line)

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
        return self.analyser.analyse(token)

    def analyse_sentence(self, s: str):
        """Analyse a full sentence with tokenisation and guessing.

        for details of tokenisation, see @c tokenise(self, s).
        for details of analysis, see @c analyse(self, token).
        If further models like udpipe are loaded, may fill in gaps with that.
        """
        tokens = self.tokeniser.tokenise_sentence(s)
        return self.analyser.analyse_sentence(tokens)

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
        return self.guesser.guess(token)

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
        return self.lemmatiser.lemmatise(token)

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
        return self.segmenter.segment(token)

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
        return self.labelsegmenter.labelsegment(token)

    def accept(self, token: Token):
        '''Check if the token is in the dictionary or not.

        Returns:
            False for OOVs, True otherwise. Note, that this is not
        necessarily more efficient than bool(analyse(token))
        '''
        return self.analyser.accept(token)

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
        return self.generator.generate(omorstring)

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
        return self.tokeniser.tokenise_sentence(sentence)

    def tokenise_plaintext(self, f):
        '''tokenise a whole text.

        Args:
            f: filelike object with iterable strings

        Returns:
            list of tokens
        '''
        return self.tokeniser.tokenise_plaintext(f)

    def tokenise_conllu(self, f):
        '''tokenise a conllu sentence or comment.

        Should be used a file-like iterable that has CONLL-U sentence or
        comment or empty block coming up.

        Args:
            f: filelike object with iterable strings

        Returns:
            list of tokens
        '''
        return self.tokenise_conllu(f)

    def tokenise_vislcg(self, f):
        '''Tokenises a sentence from VISL-CG format data.

        Returns a list of tokens when it hits first non-token block, including
        a token representing this non-token block.

        Args:
            f: filelike object to itrate strings of vislcg data

        Returns:
            list of tokens
        '''
        return self.tokeniser.tokenise_vislcg(f)


def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSA', required=True,
                   help='Path to FSA analyser')
    a.add_argument('-i', '--input', metavar='INFILE', type=open,
                   dest='infile', help='source of analysis data')
    a.add_argument('-v', '--verbose', action='store_true',
                   help='print verbosely while processing')
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    omorfi.load_analyser(options.fsa)
    if not options.infile:
        options.infile = sys.stdin
    if options.verbose:
        print('reading from', options.infile.name)
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
    sys.exit(0)


if __name__ == '__main__':
    main()
