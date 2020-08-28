# Lexical database structure and processing

Omorfi is in its core a *database* of *lexical data*, this page describes what
is contained and how it is stored.  The data is stored in tsv (tab separated
values) files. The specific dialect of TSV is determined by python at the
moment; see [csv.DictWriter](https://docs.python.org/3/library/csv.html).  In
the main database we store the [lemma field](#lemma) and a [homonym
field](#homonym), which form the *unique key* of each lexeme.  You can find this
in the file `lexemes.tsv`. These two fields are joined with a [paradigm
field](#new_para) and [origin field](#origin), which are required for each
lexeme.  All other lexical data is optional, joined on the unique key. You can
currently find the joins in `attributes/*.tsv`.

# The fields for lexemes

* **lemma** is the word's id / the _dictionary form_.
* **homonym** is a unique identifier.
* **new\_para** is our _full_ classification of the word.
* **origin** denotes the data source for the lexeme.

Optional fields at the time of writing include:

* **abbr** is type of abbreviation
* **adptype** is subclassification of an adjective
* **blacklist** marks words to be avoided
* **boundaries** marks word part boundaries for compounds and similar
* **lex** is lexicalised derivation etc.
* **numtype** is subclassification of a numeral
* **plurale\_tantum** determines if singular forms are used.
* **prontype** is a string of additional pronoun analyses
* **pronunciation** holds pronunciation information needed in guessing other
* **stem-vowel** holds pronunciation information needed in guessing other
* **proper\_noun\_class** determines proper noun's class
* **sem** determines optional semantic classes.
* **style** determines usage limitations of word.
* **symbol** is a punctuation and symbol subclassification
* **argument** is for argument structure of the lexeme

Fields described per paradigm:

* **UPOS** universal part-of-speech
* **POS** legacy part-of-speech
* *kotus_tn* paradigm number of KOTUS dictionary
* *kotus_av* gradation letter of KOTUS dictionary
* *plurale_tantum*
* *grade_dir* direction of consonant gradation
* *harmony* vowel harmony
* *stem_vowel* stem vowel
* *stem_diphthong* stem dipthong
* *possessive* optionality of possessives
* *clitics* optionality of clitics
* *suffix_regex* suffix RE that matches all words in the class
* *deletion* suffix of the word to delete to form invariant stem / stub

Fields guessed algorithmically:

* *stub*
* *bracket_stub*
* *twolstem*

## Lemma

A dictionary form serving also as unique-ish identifier of the word in the
dictionary. In case lemma is not unique, a homonym field *must* make any entry
in the database unique.

## Homonym

Homonym id is an arbitrary string with only requirement that for each non-unique
lemma the homonym field must be different. For purposes of stability in
morphological analysis in generation, we use numbers when no other uniqifying
feature is found; e.g. *viini_1* (wine) and *viini_2* (quiver) are distinguished
by number since there are no other distinguishing feature, for comparison, see
[viini on wiktionary](https://en.wiktionary.org/wiki/viini#Finnish). For words
of differing POS we no longer use numbering: FIXME an example here

The current homonym key is the UPOS field plus potentially the number when
necessary.

## Origin

Denotes the data source for the lexeme. This is necessary for copyright issues
and also used to generate the low coverage high precision dictionary

## Paradigm

Paradigm determines inflection of a word, in omorfi it also contains some other
information. The paradigm key is usually uppercased UPOS and an example word
from the category, e.g. `NOUN_TALO`. In database terms there is an additional
database under `paradigms.tsv` that is joined to lexemes.tsv on `new_para` field
to form a master database.


## UPOS

Universal POS is a POS value drawn from [Universal
dependencies](https://universaldependencies.org) standard. This is the main POS
value used in omorfi since 2015.

## POS

The legacy POS value used by omorfi is strictly limited to morphological
features that can be seen from the inflection of the word.
It works like this: Nouns inflect in case/number forms, Adjectives have
comparative derivation on top of that. Verbs inflect in tense/mood and person
forms among others. Particles do not inflect.

## Kotus TN

An official dictionary classification.

## Kotus AV

An official dictionary classification.

## Plurale tantum

Determines whether nominal is allowed to have singular forms.

## Possessive

Determines whether partially inflecting word can take up possessives or not.
## Clitic

Determines whether partially inflecting or non-inflecting word can take up
clitics.

## Proper class

A semantic class for proper noun, probably from FINER data so named entity
class.

## Style

Any arbitrary pragmatic usage limitation for word.

## Gradation direction

The gradation can be split in two cases depending what is the grade in the lemma
form.

## Harmony

The suffixes depend on the vowel frontness of the word.

## Stem diphthong

Determines variant of uo/yö/ie words.

## Stem vowel

Determines vowel of illative forms, if needed.

## Pronunciation

Pronunciation information from the stem or differing pre-defined pronunciation
is stored here for guessing other features (vowel harmony).

## Boundaries

For compounds, the lemma with word part boundaries is given here to help
determining the vowel harmony correctly. The boundaries are also used for
some non-compound boundaries.


## Particle / Noun class / Adjective class / pronoun / numeral class / verbal arguments ##

Determines additional analyses for words of given pos: these are used to inject
additional lexical data to analyses: e.g.: Particle -> adposition, preposition,
genitive complement, numeral -> ordinal roman digit, verb -> transitive with
elative argument.

## Sem

Determines optional semantic classes. There is no exhaustive use list yet.

## Stub

Stub is the part of word that does not undergo any alternations, and thus a good
starting point for many practical implementations of morphology.

## Bracketstub

For analysis styles like FTB 3.1, the lemmas for compound initial words are
different from compound final, to accommodate this a complex structure
containing both stub and stem is written into lexc files to avoid duplicating
all the lexicons.

## Gradestem ##

The original omorfi implementation used stem's with gradation marked but lots of
other variation in lexc stuff.

## Twolstem ##

This stem could use twol rules for all variations.
