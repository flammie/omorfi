# Database processing

**This document is outdated**

This page is _hacking_ instructions for some scripts in `src/` that handle and
facilitate lexical database usage in omorfi. The current version of the _lexical
database_ is just a loosely structured collection of scripts and data. The data
is stored in tsv files roughly as is understood by python's `csv.writer` and
`csv.DictWriter` classes.

<aside>(I'd like to rewrite this part in SQLite or something that maintains
consistency of data on updates, stay tuned for updates in OmorfiLexicalDatabase.
I would appreciate help of someone who actually likes database even though I
studied this stuff decade ago and know how to do it I am not awfully excited
about it anymore.)</aside>

# Introduction

Lot of omorfi's functionality is based on having a large database of lexical
data, that is, information about words. This data is stored in what we call
_lexical database_, basically a collection of lexical entries associated to
additional pieces of information that is required for different applications and
research. The main entries are stored in database of lexemes, which is used as
unique key for the word concept, i.e. currently just the dictionary form and a
(running) homonym number. You can find this in the `lexemes.tsv`. This is
combined with additional data based on the unique key, you can currently find
them in `attributes/*.tsv`. Currently all word entries are required to have a
_paradigm_ key `new_para`, this points to additional set of information joined
to the lexical entry.

# Data sources and guessing

Data from different sources has different kinds of information, and often
lacking lot of explicit knowledge of the word's morphophonological structures,
so we have some python scripts to figure these data out semi-automatically. This
process is also called _guessing_. Ideally most data sources should have all
this data available verified by humans so that we wouldn't have to guess, but
new words come up all the time and this set of scripts is done to help people in
classification. The data is set up in a python's `dict()` structure.


# Details #

The map that we collect into python contains following fields. These main fields
can form unique keys:

  * **lemma** is the word's id / the _dictionary form_.
  * **homonym** is a number denoting different lexemes with same lemma.
  * **new\_para** is our _full_ classification of the word.
  * **origin** denotes the data source for the lexeme.

These are used for compatibility with official dictionaries

  * **kotus\_tn** is a _combined_ classification is the _kotus_ (RILF)
    dictionaries.
  * **kotus\_av** is the _gradation_ classification from the same dictionaries.

These are used to tweak morphological features:

  * **plurale\_tantum** determines if singular forms are used.
  * **possessive** determines if possessives are used.
  * **clitics** determines if clitics are used.

These are used in applications, for semantics, pragmatics, whatever:

  * **is\_proper** determines if word is proper noun.
  * **proper\_noun\_class** determines proper noun's class
  * **particle** is a string of additional particle analyses
  * **sem** determines optional semantic classes.
  * **noun\_class** is a string for additional noun analyses
  * **adjective\_class** is a string for additional adjective analyses
  * **numeral\_class** is a string for additional numeral analyses
  * **pronoun** is a string of additional pronoun analyses
  * **style** determines usage limitations of word.
  * **upos** is _universal_ part-of-speech.
  * **pos** is _legacy_ part-of-speech.

These are used by implementations for morphographemics, etc.:

  * **stub** is the _prefix_ of the word that does not alternate.
  * **gradestem** is the stub of the word with gradation morphophonemes.
  * **twolstem** is the _stem_ of word with alternations marked as special symbols
  * **grade\_dir** determines direction of gradation.
  * **harmony** determines the variant of vowel harmony.
  * **is\_suffix** determines if word is bound morpheme after host root.
  * **is\_prefix** determines if word is bound morpheme before host root.
  * **stem\_diphthong** determines stem's diphthong for diphthong variation.
  * **stem\_vowel** determines stem vowel for lengthening and copying.
  * **extra\_e** determines whether stem ends in e or consonant.
  * **extra\_i** determines whether stem ends in i or consonant.
  * **pronunciation** holds pronunciation information needed in guessing other
    features.
  * **boundaries** marks word part boundaries for compounds.
  * **bracketstub** is a combination of stub and stem used to generate complex
    readings for certain analysis styles


## Lemma ##

It is not fully unique, but almost. This is **required** for guessing, we cannot
do anything without it. This is encoded as a `string`.

## New para ##

Is our classification to the word that contains _all_ the information that is
required to inflect it properly in _omorfi_ systems. **Not guessable**. This
classification is detailed in other wiki pages: . This is encoded as a `string`.

Note that this encodes all the information of other variables so it can be
expanded to all other variables, or other variables can be used to guess this
one.

## UPOS

Universal POS is a POS value drawn from [Universal
dependencies](https://universaldependencies.org) standard. This is the main POS
value used in omorfi since 2015.

## POS ##

The legacy POS value used by omorfi is strictly limited to morphological
features that can be seen from the inflection of the word.  **Not guessable**.
It works like this: Nouns inflect in case/number forms, Adjectives have
comparative derivation on top of that. Verbs inflect in tense/mood and person
forms among others. Particles do not inflect. This is encoded as `string in
['N', 'A', 'V', 'P']`

## Homonym ##

Homonym numbering is used for separating words with same dictionary form from
each other. **Not guessable**. A basis for differentiation needs be evidenced by
real world use: two separate inflectional paradigms is acceptable for homonym
numbering, although one may consider adding a new combined paradigm if the
semantics are clearly indistinct. An evidence for different semantics can be
e.g. translation: if two words have systematically different translations it is
a good reason to believe they are homonyms. Should be encoded as a positive
`int` running number from 1; numbers shall be given in the order database is
sorted.

## Kotus TN ##

An official dictionary classification. **Not guessable**. We can infer a lot of
useful information on it, so it is possible to donate us databases containing
only lemma and kotus\_tn and we can guess the rest. Should be a string encoding
an `int in range(1,102)`.

## Kotus AV ##

An official dictionary classification. **Not guessable** It removes need of
guessing gradation beyond one specific pair of letters. should be a `string in
[False, '0ABCDEFGHIJKLMNOPT']`.

## Plurale tantum ##

Determines whether nominal is allowed to have singular forms. **Can be guessed**
for all nominals, when dictionary form is plural and differs significantly from
singular form.

## Possessive ##

Determines whether partially inflecting word can take up possessives or not.
**Not guessable** in general case.

## Clitic ##

Determines whether partially inflecting or non-inflecting word can take up
clitics. **Not guessable** in general case.

## Proper? ##

Determines if noun is a proper noun. **Mostly guessable** from uppercased lemma.

## Proper class ##

A semantic class for proper noun, **not guessable** at all, comes from other
systems.

## Style ##

Any arbitrary pragmatic usage limitation for word. **Not guessable** at all,
comes from other systems.

## Stub ##

Stub the part of word that does not undergo any alternations, and thus a good
starting point for many practical implementations of morphology. **Fully
guessable**.

## Gradestem ##

The original omorfi implementation used stem's with gradation marked but lots of
other variation in lexc stuff. This is legacy stem for that and is **fully
guessable**.

## Twolstem ##

This stem could use twol rules for all variations. **Fully guessable**.

## Gradation direction ##

The gradation can be split in two cases depending what is the grade in the lemma
form. **Guessable** in most cases.

## Harmony ##

The suffixes depend on the vowel frontness of the word. **Fully guessable** most
of the time, a few words need to override this or relax.

## Suffix? Prefix? ##

Some words in dictionary do not appear without compound parts, this is most
typically marked with hyphen in lemma and is thus **Fully guessable**.

## Stem diphthong ##

Determines variant of uo/yö/ie words. Guessable. Was needed for few kotus
classes collapsing all stuff nastily. **Fully guessable**

## Stem vowel ##

Determines vowel of illative forms, if needed. Guessable from last vowel of
lemma, unless the pronunciation differs from the writing (in foreign loans).
**Guessable** in most cases.

## Extra E, I ##

Determines variant of singular nominative. Was needed to overcome kotus classes
5, 6 and 49 collapsing all sorts of lemmas in on place. **Fully guessable**

## Pronunciation ##

Pronunciation information from the stem or differing pre-defined pronunciation
is stored here for guessing other features (vowel harmony).

## Boundaries ##

For compounds, the lemma with word part boundaries is given here to help
determining the vowel harmony correctly.

## Bracketstub ##

For analysis styles like FTB 3.1, the lemmas for compound initial words are
different from compound final, to accommodate this a complex structure
containing both stub and stem is written into lexc files to avoid duplicating
all the lexicons.

## Particle / Noun class / Adjective class / pronoun / numeral class / verbal arguments ##

Determines additional analyses for words of given pos: these are used to inject
additional lexical data to analyses: e.g.: Particle -> adposition, preposition,
genitive complement, numeral -> ordinal roman digit, verb -> transitive with
elative argument.

## Sem ##

Determines optional semantic classes.

## Origin ##

Denotes the data source for the lexeme. One of `{omorfi, kotus, joukahainen,
finnwordnet, fiwikt, omegawiki, unihu}`
