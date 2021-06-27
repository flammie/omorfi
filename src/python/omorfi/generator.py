#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Omorfi generator logic is contained in this class. Uses an HFST model.
"""

from .hfst import load_hfst


class Generator:

    """
    An object for omorfi’s morphological generation.
    """

    def __init__(self, hfstfile: str):
        """Load analysis model from a file.

        Args
            f: containing single hfst automaton binary.
        """
        self.generator = load_hfst(hfstfile)

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
        generated = self._generate(omorstring)
        if not generated:
            return []
        return generated
