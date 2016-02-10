---
layout: page
title: "Finnish morphosyntax"
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

## Lemma form?

In morphological analyses, it is customary to identify the word somehow, with a
*lemma*, a *dictionary form*, an id *number* (e.g. in wordnet?) or such.
Omorfi by default uses a *word id* to denote a word-form that is in the lexical
database.
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

For some applications it is detrimental to know how word is formed and that it
is in the database, those will not use word id's, but hypothetical lemma.

```
> talonmies
talon#mies N Nom Sg
talon#mies N Nom Sg
```

I (flammie) find this more problematic, for one, there's no information left
of what *talon* is anymore, could be Engl. 'talon' for all we know.

## Adverb or adposition

Adverbs and adpositions are quite heterogeneous set of words altogether. The
main difference in syntax is that adpositions will have nominal complements,
adverbs may have verb, adjective, adverb or even sentence complements, or no
clear complements at all. Adpositions’ complements are typically genitives or
partitives, often found nearby, but not necessarily. Adpositions’ complements
may be encoded with possessive suffix attached to adposition itself. Adverbs
typically would not have possessive suffixes, but some actually do.

## Participle or derivation

Participles are verb forms, that become derivations when they turn into
adjectives. A participle is a participle if it is part of a verb chain, phrase
or structure, that cannot be replaced with an adjective, e.g., syntactic tense
or such construction. A participle can also be a past connegative form,
dependent of negation verb. While participle can only appear in singular and
plural, the derived adjective can appear in all case and comparative forms.

## Infinitive or derivation

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
