# Notes about ambiguity in Omorfi analysis scheme

Natural languages are full of ambiguities, words mean many things and sometimes
irrelevant word forms overlap each other by accident. Sometimes ambiguities are
introduced by questionable design in the dictionary or grammar. I am trying to
list some of the ambiguities that you will commonly run into when using omorfi,
and explain where they come from. One common source is that we include data from
number of differently produced dictionaries with different policies, we do
always go through the words by hand and exclude some, but it is not very common,
we generally only exclude what seems to be genuine mistakes or what doesn't work
with our implementation.

Omorfi comes with some scripts and codes to eliminate ambiguity by default that
can be used, the first part of this document explains the ambiguity that is hard
to eliminate: systematic ambiguities in morphosyntactic system, the homonymies
and idiosyncratig tagging. The second part of the document also explains
the ambiguities you will only see if you do not use the disambiguation we
provide: low frequency loan words and proper nouns, dynamic compounding and
derivation and such.

A thing that engineers need to keep in mind that it is not always even in realms
of possibility to "perfectly" disambiguate natural language texts; some
ambiguities can only be resolved with world knowledge and some texts do not
concern real world or world that we can observe anymore; in English there is a
classical sentence of "they see a man on the hill with a telescope", which has
several plausible readings and the only way one is more correct than another is
if you can observe a man, a hill and a telescope; the telescope can be on a
*them*, on the man, or on the hill.

## Plurale tantum

*Plurale tantum* is a nominal that mainly appears only in plural forms, like
*sakset* (scissors). The lemma id or dictionary form is then the plural
nominative and not a singular nominative. Common problem people have with
plurale tantums is that not all of them are super clear cut, even *saksi* (a
scissor) appears in real world data on its own. This leads into all plurale
tantums are duplicated into a singular lexeme with singular id, a lot of extra
analyses.

The data sources like *fiwikt* and *finnwordnet* include all species of animals
and plants in plural form as a separate lexeme, based on translations I've seen
the logic behind this is is, that it points to a kind of a scientific taxonomy
instead of just multitude of animals or plants, i.e. lexeme *sudet* (wolves)
would mean *canis lupus* specie, not just few wolves wandering about. It causes
annoying ambiguity everywhere.

## Adverbs vs nominal forms

A lot of adverbs are essentially forms of nouns or adjectives, there's a fully
productive class of *-sti* adverbs roughly corresponding to English *-ly*
adverbs, data sources like wiktionaries will include these as separate lexemes
and the derivational morphology is not fully implemented in omorfi either.

Adverbs that are some locative forms of nouns will generally be ambiguous,
sometimes the root nouns are archaic or semantically far from each other, e.g.
*päällä* (turned on) is hardly related to *päällä* (on the head). On the other
hand *lukossa* (locked) is quite close to *lukossa* (inside the lock), but still
relatively easy to disambiguate as a human. Sometimes the English translation
does not provide enough clue to disambiguate, e.g. *maahan* (to the ground) is
same whether you ‘fall to the ground’ (illative of the noun) or
‘drive/burn it to the ground’ (adverb).

There is a large group of noun forms tagged as adverbs where we have not found a
good linguistic evidence for selecting one or the other, as basically all
nominals in non-core cases act like adverbs. The most common ones in the
dictionary are temporals like *yöllä* (at night / lit. on the night) or
*talvella* (during winter / on the winter), and spatial like *pohjoiseen*
(northward / to north).

Some feelings and such can be analyse either as adverbs or forms of nouns, e.g.
*raivoissaan* (in their rage / enraged) or *humalassa* (drunk / under
influence).

## Verbs and auxiliary verbs

This is a distinction that is common and traditional in other languages and not
as usual in Finnish, but for compatibility of other standards, several verbs can
be analysed as auxiliary instead of verb. For compatibility with Universal
parts-of-speech and Universal Dependencies, auxiliary reading is used at least
for copula verb *olla* (to be) and the negation verb *ei*. Negation verb is
usually not a main verb, perhaps if you need to promote it to main verb in
conjunction or ellipsis type of clauses. Copula verb's use cases
can be split between auxiliary and non-auxiliary with various criteria. If
auxiliary readings are used the main meaning of non-auxiliary copula is
existential (to exist / there is). The main use case of auxiliary in universal
schemes is that auxiliary verb is linked to another verb in a structure where it
merely gives grammatical or more abstract information to the main verb: in past
or perfect participle it is the tense of copula verb that gives the tense to the
main verb. Modal verbs are often but not always thought of as auxiliary verbs,
they generally appear chained with other verbs and mainly contribute the
modality to the main verb's semantics: (may, should, must and so on). Modal
verbs, like copula, can exist as main verbs in Finnish.  We are not sure that
the auxiliary readings are necessary for most NLP applications, but
interoperability and comparability with other languages and standards is useful.

## Possessive nominatives

Possessive nominatives are systematically ambigous between singular and plural
nominative (and singular genitive) in Finnish grammar. This is not an easy
ambiguity to resolve since it really often requires world knowledge; you can
sometimes guess that *äitinsä* (their mother/mothers) is more often singular and
*kätensä* (their hand/hands) are more often plural, but this is not a 100 % rule
and therefore not in the automatic disambiguations.

* * *


## Compound words

Compunding is a process where you put two words together to create a new word,
in many of world's languages you can do this very creatively to come up with new
words as needed. Finnish does this a lot too. Unfortunately new compound words
are written together without space or hyphen or so, which leads to a lot of
ambiguity, as analyser needs to support creative combinations but also most
longer words could plausibly be pieced together from shorter words. If you use
omorfi's default analysis pipelines with disambiguation you will not likely see
many creative suggestions since they are filtered out by simply hiding analyses
that have more compound boundaries, this is coupled with keeping known and
attested compound words in the dictionaries. Only time you see unattested and
creative compound analyses is when nnnone of the dictionary words would be
plausible analysis of the surface form. For an example, first word I found today
not having a dictionary reading in today's news for current version of omorfi is
‘cricket field’; attested forms that have been added before include:
‘golf field,’ ‘gravitational field,’ ‘search field,’ ‘helicopter field,’ ‘sand
field,’ ‘coal field,’ ‘football field,’ ‘ice field,’ ‘ice hockey field,’ etc.
and in next version probably also ‘cricket field.’

## Proper nouns

Proper nouns or names of things can be problematic in a modern dictionary based
analyser, since there is an endless amount of names used in the world. Large
coverage omorfi uses several name databases (e.g. Finnish census data and
Finnish map data), this includes foreign names that are common (appear more than
five times) in Finland. Luckily vast majority of names are spelled according to
Finnish orthography with an uppercase first letter, even when they overlap with
common words, just the basic disambiguation strategy that discounts name reading
unless it's uppercased in the middle of the sentence solves most of the
problems.

For named entity recognition purposes, proper nouns often have analyses for
type: first name, last name, place name or other names. It is not uncommon to
have ambiguities between first names, last names and place names in Finnish.
This ambiguity can be unnecessary for most applications and can be removed
easily.
