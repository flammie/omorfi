---
layout: default
title: "API Design"
---

# Omorfi language binding APIs

Omorfi provides very simple bindings for using the language models without
having to write your own shell scripts around e.g. HFST shell commands. The APIs
provide typically some minor additional features, such as case folding or
heuristic word-tokenisations based on the dictionary, depending on the features
of the API host language (python has more advanced string mangling than C or
bash).

# Design

The APIs are tied around concept of an omorfi object or handle, that can be
used to load and apply the language models without dealing with too much of the
FST internals. These are roughly the functionalities:

* loading a model for specific task from a specific file
* applying a function supported by currently loaded model(s):
    * tokenise a multi-token string
    * analyse a token
    * analyse a multi-token sentence
    * guess more analyses
    * check if word is OK without analysing
    * segment word into words, morphs or syllables
    * spell correction suggestions without context
    * ...
* converting between different formats / getting printable information

That is all.

Here is a UML chart I drew about the design:

![UML chart of omorfi API]({{ site.baseurl }}/doc/omorfi-API.svg)

# Language specific APIs

The language specific APIs are generated with doc comment system of the host
language, e.g. javadoc, doxygen or docutils. You may find them from the [omorfi
doxygen pages]({{ site.baseurl }}/doc/html/). Except for bash, that doesn't
really have a doxygen or real API stuff.


**Rest of the page may be more out of date than the doxygen manuals**

## Python API specialties

I have used a module omorfi, which exposes class Omorfi. The other omorfi
related stuff lives in the same package, but is not meant for public consumption
yet. Eventually the access to lexical database and conversions will be used more
efficiently too. The tokens are currently handled as tuples, but some functions
also work on strings.

  * module omorfi:
    * class Omorfi:
      * init(self, verbosity)
      * load\_analyser(self, path)
      * tokenise(self, line)
      * analyse(self, token)
      * guess(self, token)
      * ...
      * analyser: analysis automata
      * ...
    * class Token:
      * get_nbest(self, i)
      * printable_XXX(self, which="1best")
    * class Analysis:
      * printable_XXX(self)

### tokenise(self, string)

Tokenises a string based on language models, with some punctuation-stripping
heuristics. The result will be a list of tokens.

### analyse(self, token)

Look up `token` from morphological analyser(s) loaded. If `self.can_...case`
do not evaluate to `False`, and the token cannot be analysed, the analysis
will be retried with recasing. Result will be provided as an ambiguous list of
analyses.

## Java API

The java API to omorfi uses hfst-optimized-lookup-java. This is preliminary, I
basically made it to test if I can use omorfi on android. It turns out, yes I
can. There's some javadoc included.

### Class Omorfi

The Omorfi object holds the loaded models and can apply them to strings.
The java code can perform minimal string munging.

* Omorfi::Omorfi(): *construct empty omorfi holder.*
* Omorfi::loadAnalyser(String) *Load omorfi analyser model.*
* Omorfi::analyse(String) *Perform a simple morphological analysis
  lookup.* Performs case folding.
* Omorfi::tokenise(String) *Perform tokenisation or split.*

* * *

## Bash "API"

`Omorfi.bash` provides the basic functionality as bash functions as used by
the bash convenience commands, plus some bash scripts common to these
commands, such as automaton searching and error messaging. To use omorfi
bash API, simply source the file.


### Current interface

* `omorfi_find(function, tagset)`
* `omorfi_find_help(function, tagset)`
* `apertium_cleanup()`
* `omorfi_analyse_text(tagset)`
* `omorfi_analyse_tokens(tagset)`
* `omorfi_disambiguate_text(tagset)`
* `omorfi_generate(tagset)`
* `omorfi_hyphenate(tagset)`
* `omorfi_segment(marker, markre, unmarkre)`
* `omorfi_spell()`

### omorfi\_find(function, tagset) ##

Tries to locate omorfi from standard paths, which are currently following:

  1. `$OMORFI_PATH`
  1. `@prefix@/share/omorfi`
  1. `$HOME/.omorfi/`
  1. `.`
  1. `./generated/`
  1. `./src/generated/`
  1. `../src/generated/`
  1. `$(dirname $0)/../share/omorfi

If environment variables are missing, the component is skipped. The last resort
will try to find omorfi relative to the `omorfi.bash` or the app sourcing it.

The optional arguments are:

* `function` for testing existence of given functional automata instead of just
  omorfi directory. `function` should be one of {generate, analyse, segment,
  etc.}
* `tagset` if function is generate or analyse, to check for an automaton for
  that tagset only

Prints directory or file of first match on success or nothing if nothing is
found.

### omorfi\_find\_help(function, tagset)

A helper to print informative message after `omorfi_find` fails. Will tell
user about the search path.

### apertium\_cleanup()

Reformats text in stdin for apertium's lt-proc or hfst's hfst-proc. Will use
apertium tools if available, or sed if available, or cat. The last two will
undoubtedly break more than the first one.

### omorfi\_analyse\_text(tagset)

Analyse running text with omorfi. Uses tagset if given, defaults to whatever
is found in search order otherwise. Reads unformatted normal text files on
stdin.

### omorfi\_analyse\_tokens(tagset)

Analyse pre-processed text with omorfi. Uses tagset if given, defaults to
whatever is found in search order otherwise. Reads one token per line on
stdin.

### omorfi\_segment(marker, markre, unmarkre)

Morphologically segment texts. Optional parameters are: segment marker,
regexes for marking and umarking boundaries. marker is string to use for the
segment separator, by default → ←. If present the first regex is replaced
with marker and second with empty string. Expressions are sed basic regexes
and applied over output of the omorfi.segment.hfst automaton.

### omorfi\_spell()

Applies spell-checking and correction to stdin.

