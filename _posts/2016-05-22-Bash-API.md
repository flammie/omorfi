---
layout: page
title: "Bash API"
category: api
date: 2016-02-08 18:23:58
---


# Introduction #

`Omorfi.bash` provides the basic functionality as bash functions as used by
the bash convenience commands, plus some bash scripts common to these
commands, such as automaton searching and error messaging. To use omorfi
bash API, simply source the file.

# Current interface #

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

## omorfi\_find(function, tagset) ##

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


## omorfi\_find\_help(function, tagset)

A helper to print informative message after `omorfi_find` fails. Will tell
user about the search path.

## apertium\_cleanup()

Reformats text in stdin for apertium's lt-proc or hfst's hfst-proc. Will use
apertium tools if available, or sed if available, or cat. The last two will
undoubtedly break more than the first one.

## omorfi\_analyse\_text(tagset)

Analyse running text with omorfi. Uses tagset if given, defaults to whatever
is found in search order otherwise. Reads unformatted normal text files on
stdin.

## omorfi\_analyse\_tokens(tagset)

Analyse pre-processed text with omorfi. Uses tagset if given, defaults to
whatever is found in search order otherwise. Reads one token per line on
stdin.

## omorfi\_segment(marker, markre, unmarkre)

Morphologically segment texts. Optional parameters are: segment marker,
regexes for marking and umarking boundaries. marker is string to use for the
segment separator, by default → ←. If present the first regex is replaced
with marker and second with empty string. Expressions are sed basic regexes
and applied over output of the omorfi.segment.hfst automaton.

## omorfi\_spell()

Applies spell-checking and correction to stdin.

