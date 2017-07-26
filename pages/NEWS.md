---
layout: page
title: "News"
category: meta
date: 2016-02-08 18:23:58
---


# NEWS

This file lists noteworthy changes between releases, for full list of changes,
see git log and then `ChangeLog.old`.

## Significant changes in 20150904

* allomorphy can be tagged again to distinguish e.g. *-iden* and *-itten* when
  generating
* FinnTreeBank-1 format provided by Miikka Silfverberg is available but not
  built by default since it lacks a test set
* lexicalised inflections can have separate tag, e.g. *kännissä* can be lexical
  inessive distinguished from regular inessive
* preliminary VISL CG-3 support, with original grammar by Fred Karlsson;
  convenience bash scripts available for disambiguated parsing
* preliminary support for conllu and conllx analysis formats
* paradigm categorisation is now verified by regular expressions
* lots of paradigm fixes and some added words

## Significant changes in 20150326

* speed is up to >20,000 tokens per second from ~500
* coverages are up to:
  europarl (99 %) gutenberg (97 %), JRC Acquis (94 %) and fiwiki (93 %)
* moses factored model format supported
* segmentation supported
* Java API
* Python hacks packaged to API and module
* Rest of hand-written Xerox legacy data removed; all is script-generated
* github migration since google code is EOL'd
* file naming for automata changed to include omorfi prefix for all file
  names in case they are distributed separately.

## Significant changes in 20141014

* The regressions are also set on coverage over popular corpora:
  Europarl (98 %), FTB 3.1 (97 %), gutenberg (96 %), JRC Acquis (93 %) and
  fiwiki (90 %)
* sti derivation tentatively added
* number of new paradigms and paradigm moves, esp. in old and archaic styles
* some new words manually added
* apertium formats updated totally
* interjection chaining
* rest of hand-written lexc removed: everything in db and python code now
* more strict building and testing altogether (no more dangling references or
  missing tags allowed)
* morphological segmentation should be usable now
* lots of other classifications and attributes added

## Significant changes in 20130829

* Default tag format is now FTB3.1. Recall is 90 % and the format is stable and
  easy to read by humans, which is now the main target for computational
  morphologies.
* The omor tagsets are now permanently unstable and subject to change any day.
  To use them, python scripts have been provided.
* Lots of proper nouns and semantics from Uni Hel projects
* speller build support for new voikko versions
* New regression tests for stuffs
* Most of legacy lexc sources removed; they are now generated from TSV
  "databases".
* The morphological classes now follow 3 main classes with some subclasses that
  are less morphological
* Twol rules and flag diacritics have been eliminated
* Lots of support scripts to verify and extend classifications
* Lots of new word-forms, inflections and changes to derivations
* Some python support scripts for omor formats

## Significant changes in 20121226

* Added fi.wiktionary.org as lexical source (much thanks to students of my unix
  tools course for scripting)
* Added first batch of new proper nouns from a project in Univ. Helsinki
* Lexc data is now rebuild from lexical sources as standard processing;
    * requiring python3
* Minor bug fixes to man pages, special boundaries (e.g. in arkki_tehti)

## Significant changes in 20120401

* Fixed some twol rules w.r.t. new features that blocked compiling
* Autogenerate lexicons from csv data all the time
* Moved to git and googlecode -> chopped most of the documentation and such
* Fixed scripts a bit, added man pages
* Made very crude tests to have at least something back in.

## Significant changes in 20110505

* whole new finntreebank tagset for forthcoming finntreebank work
* uppercasing is noted in the analysis level
* the word boundaries of lexicalised compounds may be available for more cases
  (depending on the tagset)
* whole new lemmatizer tagset is available
* some dozens of new words added and fixed
* combine corpus analysis script with apertium's preprocessors
* causative derivation chain added
* bbreviations, adpositions, prefixes and suffixes are no longer pos but subcat
  analyses


## Significant changes since 20100401

* Include deverbal nouns in compounding system

* Start marking compound and strong morpheme boundaries

* New lexical data handling systems

* Implement generator from analyser

* Subcategorize lots of classes for CG and apertium

* Write documentation in booklet format

* New URI and digit string guessers

* New tagging style colorterm for interactive use

* Include weighting scheme in default build

* Demote SUFFIX from POS reading to SUBCAT

## Significant changes since 20100111

* Added marginal enclitics kA, kAs

* Added LEMMA= structure

* re-organized source code to modules

* Added tagging schemes, weighting schemes and suggestion algorithms

## Significant changes since 0.5

* completely new morphology built on traditional lexc-twolc model

* easier route to add new lexical data via simple CSV format

* lots of new lexical data from Joukahainen project as well as extended
  from kotus-sanalista semi-automatically and *by hand*.

* titlecasing filter for regular words

* š filter for old orthography variants

* compounding much less haphazard concoction

* parts of speech classified and included

* pronouns, interjections, numerals, proper nouns

* much closer to real full fledged morphology

* movement from SFST to HFST toolset with lots of new cool toys (SFST support
  is retained in HFST)

* towards full-scale automatic test suite

<!-- vim: set ft=markdown: -->
