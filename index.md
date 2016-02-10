---
layout: default
title: "Omorfi"
---

# Omorfi–Open morphology of Finnish

Omorfi is free and open source project containing various tools and data for
handling Finnish texts in a linguistically motivated manner. The main
components of this repository are:

1. _a lexical database_ containing hundreds of thousands of words (c.f.
   [lexical statistics](Lexical-statistics))
2. a collection of _scripts_ to convert lexical database into formats used by
   upstream NLP tools (c.f. [lexical processing](Database-processing))
3. an _autotools setup_ to build and install (or package, or deploy): the
   scripts, the database, and simple APIs / convenience processing tools
3. a collection of relatively _simple APIs_ for a selection of languages and
   scripts to apply the NLP tools and access the database

The formats we produce are (links to free open source implementations
included):

1. lexc, as processed by [HFST](//hfst.sf.net) and
   [foma](//code.google.com/p/foma), to be used for *morphological analysis*,
   *stemming*, *segmentation*, *natural language generation*, *hyphenation* and
   as a basis for *language models*,
2. [apertium](//sf.net/p/apertium), to be used for *machine translation*
3. [voikko](//voikko.puimula.org), to be used for *spell-checking* and
   *correction*
4. _kotus-sanalista_, _lexical markup framework_, _tab-separated values_, etc.
   for long and short term storage, intermediate formats.

## Documentation

The main point of up-to-date documentation is these webpages. You should find
list of all pages on the left.

Everyone should read at least versioning information and readme:

1. [Versions and download info](meta/Releases.html)
1. [README](https://github.com/flammie/omorfi#omorfiopen-morphology-of-finnish)

If you wish to use omorfi in a serious application you probably found out from
the README that a python or java API is the way to go:

1. [Python API](api/Python-API.html)
1. [Java API](api/Java-API.html)

There's a mass of automatically generated statistics from each version of 
omorfi:

1. [Lexical statistics](stats/Lexical-statistics.html)
1. [Coverage tests](stats/Coverages.html)
1. [Missing word-forms by corpora](stats/CoveragesTop100Deltas.html)
1. [Faithfulness tests](stats/Faithfulness-tests.html)
1. [Speed](stats/Speed-tests.html)
1. [Automata sizes](stats/Automata-sizes.html)

The design principles of morphological analysis have been changed a dozen of
times to accommodate various applications:

1. [Analysis tags](design/tag-formats.html)
1. [Design "principles" for tags](design/Tagging-possibilities.html)
1. [Internal keys and codes](design/Paradigms-and-stuffs.html)

More internal documentations:

1. [Directory layout](design/Directory-layout.html)
1. [Database struccture](design/Database-processing.html)

And more...

## Contact

If you want to discuss about omorfi in Finnish or English, the IRC channels
[#omorfi](irc://Freenode/#omorfi) and [#hfst](irc://Freenode/#hfst) on Freenode
are available for immediate chats ([Freenode webchat
here](https://webchat.freenode.net/)). The google group discussion list
omorfi-devel@groups.google.com ([Google groups web interface
here](https://groups.google.com/forum/#!forum/omorfi-devel)) can also be used,
it may require subscription but is very low volume. If, for some reason, you
wish to discuss in private, authors’ private emails can be used as contact, but
prefer public chats for general usage etc., questions as the archive of
frequently asked questions will surely benefit everyone. For bug reports use
the issue functionality on this site, or even pull requests.

## Alternatives of omorfi

If omorfi doesn’t suit your needs, you may want to try other similar products:
[suomi-malaga](http://voikko.puimula.org) of voikko fame is another
morphological analyser of Finnish. [Grammatical
Framework](http://www.grammaticalframework.org/) also has NLP components for
Finnish, and it’s written in _haskell_.

If you want to use commercial products, there are surely some available
somewhere.

<!-- vim: set ft=markdown -->
