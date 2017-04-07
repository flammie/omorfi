---
layout: page
title: "Analyses and Morphosyntax FAQ"
category: design
date: 2016-02-08 18:23:58
---


# Finnish morphosyntax

This is one of many documents describing linguistic aspects of omorfi’s
morphological analysis part. I have written it as an FAQ related to common
discussions about certain tags or word-forms in omorfi analyses. It is meant to
complement the more computational / hacker documentation in this site. Other
references you might find interesting include [ISO suomen kielioppi,
verkkoversion "Finnish reference grammar"](http://kaino.kotus.fi/visk) and
[Universal dependencies for
Finnish](https://universaldependencies.github.io/docs/#language-fi), which are
two facets of the omorfi’s linguistic analysis form. However, omorfi’s analyses
are meant to be inclusive for all applications and traditions of analysing
language, so while this document argues for certain options, there will be
analysers with different versions in omorfi’s source tree for most of the
things (added on as-needed basis).

## Lemma form: valid database ID, pretty-printed dictionary entry, or ?

Morphological analysers will always refer to lexical units in some way,
typically it is a *lemma* or a *dictionary form*, but sometimes more machine
readable *id string/number*. For many traditional applications, users expect to
see a kind of an pretty-printed lemma: e.g. even when word is not in a
dictionary and found by a long chain of derivations and compounding, the
analyser acts as if it was any other word in the dictionary:
*kissatarkoirabanaanisalaatinkastikekulho* should work as well as *linja-auto*.

Omorfi by default uses a *word id’s* composed of what is pretty much classical
*lemmas* and optional *homonym number* (greater than 1) to denote a word-form
that is in the lexical database, and tags to denote derivation, furthermore
each lexeme in compound gets their own id.
```
> talon
[WORD_ID=talo][POS=NOUN][NUM=SG][CASE=GEN]
> mies
[WORD_ID=mies][POS=NOUN][NUM=SG][CASE=NOM]
> talonmies
[WORD_ID=talonmies][POS=NOUN][NUM=SG][CASE=NOM]
[WORD_ID=talo][POS=NOUN][NUM=SG][CASE=GEN][BOUNDARY=COMPOUND][WORD_ID=mies][POS=NOUN][NUM=SG][CASE=NOM]
```

This will tell us that all three words are in the dictionary: *talo* "house",
*mies* (man) and *talonmies* (janitor), as well as the fact that the compound
is made of just *talo+mies* (man of the house).

If you use legacy application automata, you will get more traditional style
readings, but these are not supported / tested by me (flammie), and depend on
user contributions.

```
> talonmies
talon#mies N Nom Sg
talon#mies N Nom Sg
```

To systematically get specific form of analyses for the lemma, consider
submitting a test set, automata building rules or a formatter module in
programming language of your choice. The most developed examples can be found
in the `python/` directories, e.g. conllu / Universal dependencies support.

## Adverb or adposition?

Adverbs and adpositions are quite heterogeneous set of words altogether. The
main difference in syntax is that adpositions will have nominal complements,
adverbs may have verb, adjective, adverb or even sentence complements, or no
clear complements at all. Adpositions’ complements are typically genitives or
partitives, often found nearby, but not necessarily. Adpositions’ complements
may be encoded with possessive suffix attached to adposition itself. Adverbs
typically would not have possessive suffixes, but some actually do.

## Participle or derivation?

Participles are verb forms, that become derivations when they turn into
adjectives. A participle is a participle if it is part of a verb chain, phrase
or structure, that cannot be replaced with an adjective, e.g., syntactic tense
or such construction. A participle can also be a past connegative form,
dependent of negation verb. While participle can only appear in singular and
plural, the derived adjective can appear in all case and comparative forms.

## Infinitive or derivation?

The three basic infinitives, i.e. first to third infinitive, or A, E, and MA
infinitives, do not have derivational use, they cannot replace nouns in
syntactic construction. While some grammars have taken the stance that
previously fourth infinitive is only a noun derivation, it retains some use
that cannot syntactically be replaced by any non-verbal noun, specifically as a
complement of negated equative clause. It would be quite difficult indeed to
syntactically analyse such structure without an infinitive reading.

## Particle?

The word particle has had different uses in different grammars of Finnish, none
of them particularly well-defined. The current grammar will use it as a
catch-all class for non-major parts-of-speech. This reading can be used in some
versions of omorfi as well. In universal parts-of-speech scheme, particle is
not used for Finnish and that practice has been followed in omorfi UPOS
readings as well.

## I don’t like this word or compound!!

One of the most common feedbacks I receive is: *what does this word mean*, *it
breaks my application*, *please stop adding rubbish words*. Omorfi’s word
database is build on inclusionist principle, the mere fact that *tai* is not
only a rather common conjunction, but also [the most widespread and best known
of the Kadai family of
languages](http://www.ling.helsinki.fi/cgi-bin/fiwn/search?wn=fi&w=tai&t=over&ver=&sm=Search)
is not basis of excluding the noun reading. There are plenty of methods to deal
with this kind of ambiguity: statistical, rule-based, ...

Sometimes words **do** get misclassified and out of order, if you find yourself
wondering a word-form, and cannot find it in
[finnwordnet](http://www.ling.helsinki.fi/cgi-bin/fiwn/search) or
[Wiktionary](https://fi.wiktionary.org/), or finally:
[Google](https://google.fi), you may report it to me.

There is an ongoing work to list particularly suspicious words to produce
limited vocabulary analysers.

## Adjective or noun?

There are groups of words that can be used both as adjectives and nouns. The most common
examples of this include inhabitants of region: *suomalainen* (a Finn, Finnish), 
*helsinkiläinen* (from Helsinki), etc. Also many colour words have this duality:
*punainen* (red), *purppura* (purple), but some have more or less strict divide between
a noun lexeme and adjectival one: *sini* (blue N) ~ *sininen* (blue N/A), *kulta* (gold N),
*kultainen* (golden A). To recognise adjectives, ...

## Proper noun as noun too?

There are also groups of proper nouns that systematically double as nouns. Most commonly,
names of languages: *Kiina* (China) and *kiina* (chinese), *Suomi* (Finland) and *suomi*
(Finnish). It is also true, that in the world at large, pretty much any combination of
characters will be used as a proper noun, and many of these found their way to omorfi
database. We have some manual annotations for worst overlaps, but it is always a good
thing to keep in mind, that most words can be proper nouns, especially when they end
in title-case position (however, some modern proper nouns are not even title-cased!).
