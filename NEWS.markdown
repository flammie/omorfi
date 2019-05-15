# NEWS

This file lists noteworthy changes between releases, for full list of changes,
see git log and then `ChangeLog.old`.

## Significant changes in 20180511

* Universal dependencies version 2.2 is now used as target
* At least 226 new words: 239 additions and 13 deletions in lexeme database
* Most changes are in development infra, so not visible to end users...
* Started rewriting CG from the scratch
* The APIs for programming language deprecate load(filename) and load(dir) forms
  of filename guessing functions in favour of forthcoming loadAnalyser(file),
  loadLemmatiser(file), loadUDPipe(file) etc. etc. functions
* Working towards more general tokenise-analyse-disambiguate pipelines maybe,
  or just refactoring
* lots more automated tests -> lots less human errors
* By popular request: there are two analysers now, one with small dictionary
  and one with full, use the smaller one when you do not want to see birds or
  languages or tribes analysed. The smaller one replaces the old default, but
  the new tools will require you to select one explicitly anyways
* fixes and workarounds: java and c++ can now be disabled partially or totally
* adopted SG0 as possible verb form analysis from UD data
* The end users are now provided with bash-scripts wrappers for all
  functionalities, whereas the typically python versions allow more control
  of parametres


## Significant changes in 20170515

* Universal Dependencies version 2 is now used, still mainly lemma, UPOS,
  features fields are analysed
* At least 2,336 new words (based on diffstat: 38886 additions, 3655 deletions)
* Preliminary support for various guessing models: python-based, finite-state
  and UDPipe. This means that it is possibly to get analyses for all tokens,
  albeit quality of guesses varies.
* A minimal C++ library version has been made to match java and python bindings.
  C++-11 and libhfst are required.
* The dix version can now be compiled with lttoolbox with a lot of memory
* A restricted "gold" dictionary mode has been added. This is good for both end
  users with limited memory and end users who require higher quality lexemes
  (i.e., only research institute approved, no wiktionary words or other weird
   stuffs)
* Documentations and automatic testing much reworked with the new modern toys
  from github: travis-ci, jekyll
* Started weeding the ADP/ADV jungle...
* Fixed a horrible bug in the corpus coverage testing that terribly
  under-estimated our coverage for corpora where hapax legomena etc. were
  ignored
* Lot of documentation has been semi-automated, therefore many changes can be
  viewed at the new gh-pages site: https://flammie.github.io/omorfi/

## Significant changes in 20161115

* Started drafting more blacklists and *known good* lexemes subsets for people
  who struggle with rare words and productive compounding, derivation
* Updated to Universal Dependencies version 1.4
* A lot of new derivations by the way
* Preliminary guessers
* More loopy guessery things for punctuation and digit combos
* Minor fixes to UD feature sorting
* Homonym numbers used in some applications
* Added timeouts where downstream tools support them, so tools don't seem like
  they are freezing at random
* moved old documentations to github-pages
* added preliminary hfst-pmatch-based tokeniser

## Significant changes in 20160515

* Universal Dependencies for Finnish is the new standard format we now follow:
    * POS is now UPOS and classes were changed accordingly (new classes: AUX,
      PROPN, DET, CONJ, SCONJ, PUNCT, SYM, and VERB, NOUN, ADP, ADV as before)
    * other features mostly match the feature field in UD documentation
    * release cycle aims to be same six month cycle as with UD
    * the automatic tests verify compatibility with UD; 92 % of lemmas, primary
      POS tags and morphological features are the same as Finnish UD corpus,
      75 % same as Finnish FTB UD corpus
    * analyser for reading and writing CONLL-U format
* tokenisation as script and more hacks to token stripping in corner cases
* continuous integration with travis-ci, currently only testing basic script
  programming conventions
* added a lot of high coverage words and forms by hand
* by popular request, some of the words can now be blacklisted, when you don't
  want that guy named Mutta to ambiguate your conjunction analyses or the odd
  new guinean bird to clash with some common verb
* the "database" is now only keyed on lemma + homonym number; paradigm is extra
  information like anything else
* a lot of work on morphological segmentation towards statistical machine
  translation; check proceedings of WMT shared tasks 2015 and 2016 to see why
* started refactoring some python code into classes

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
