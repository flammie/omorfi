---
layout: page
title: "Python API"
category: api
date: 2016-02-08 18:23:58
---


# Introduction #

`Omorfi.py` provides a simple interface for python applications to interact with installed omorfi lexicons. Consider it as a standard python entry-point to omorfi. N.B. python module provides slightly different analyses and more functionality than the raw automaton.

# Current interface #

There will be apidoc generated.

  * module omorfi:
    * class Omorfi:
      * init(self, verbosity)
      * load\_filename(self, path)
      * load\_from\_dir(self, path=None)
      * tokenise(self, line)
      * analyse(self, token)
      * ...
      * analysers: dict of analysis automata
      * ...

## load\_from\_dir(self, path=None) ##

Loads omorfi automata into memory. If `path` is given it should point to the automaton, otherwise standard installation paths are tried, currently standard linux install paths are tried in order:

  1. `/usr/local/share/hfst/fi/morphology.omor.hfst`
  1. `/usr/share/hfst/fi/morphology.omor.hfst`
  1. `/usr/local/share/omorfi/morphology.omor.hfst`
  1. `/usr/share/omorfi/morphology.hfst`
  1. `$HOME/.hfst/fi/morphology.omor.hfst`
  1. `$HOME/.omorfi/morphology.omor.hfst`

Last two paths require an accessible HOME env.var. Returned value is a handle to the analyser, currently a swig object pointing to HFST automaton.

## analyse(self, token) ##

Look up `token` from morphological analyser(s) loaded. If `self.can_titlecase` does not evaluate to `False`, and the token cannot be analysed, the analysis will be retried with first letter's case variants. If `self.can_uppercase` evaluates to not `False` and the token cannot be analysed, the words casing will be swapped and retried. The analyses with case mangling will have an additional element to them identifying the casing.

## main() ##

If invoked from command-line, `omorfi.py` can be used as simple lookup tool. Invoke with `--help` for more info.
