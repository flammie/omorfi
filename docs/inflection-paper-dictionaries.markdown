# Omorfi inflection v. other dictionaries

*Outdated*

# Introduction #

> _This is a technical documentation, for people who want to understand omorfi's
> implementation of morphology and contribute word-lists that are not suitable
> for omorfi's lexical sources. The general audience should use wiktionary and
> joukahainen instead._

Omorfi is implementation of _morphology_, and it relies on large amount of
available word lists, currently it supports following open source word lists:

* [Nykysuomen sanalista, *nssl* in short](http://kaino.kotus.fi/sanat/nykysuomi)
* [Joukahainen](http://joukahainen.puimula.org)
* [Finnish wiktionary, *fiwikt* in short](http://fi.wiktionary.org/)

If you think that words are missing from omorfi, you should first contribute
them into one of the above sources.

In top of that we need to collect and extend our word lists whenever there is
need for words, that do not fit in the requirements of above resources. This
happens for example with _rare_ proper nouns or not very lexicalised _compound
forms_, which are useful for many applications but are not allowed in any of
abovementioned lists.

For those word lists it would be ideal to have them classified so that we can
use them more or less directly. This document specifies both the ideal
classification and the process of automatically guessing the classification from
non-ideal data.

# Short background #

In order to use words in omorfi, they need to be classified. Assume a new loan
word or neologism _xaxös_ is about to enter the language, we cannot use it in
omorfi before we know:

* (whether it's a verb or nominal, though verb stems end in a or ä so this
  one's nominal here)
* whether its genitive singular is _xaxösin_, _xaxöksen_, or _xaxöden_ or
_xaxöön_. (or something more unexpected)
* whether it typically has comparatives (_xaxöksempi_, _xaxöksin_), i.e. is
  adjective rather than noun
* whether its vowel harmony really is front (_xaxöstä_) or not (_xaxösta_)
* whether it'll have consonant gradation in the stem
* etc. etc.

Lot of this can be guessed, the guesses will go right 99 % of the time. But...
we shouldn't guess things that are easy to know. A native speaker, without any
special education in linguistics, who knows the word can tell us this
immediately. We just need a way to gather people's opinions here. One such a way
is [Finnish wiktionary](http://fi.wiktionary.org). Notably though, neologisms
are not allowed in wiktionary :-/

Why it is problematic is, that everyone has different idea of what the classes
should be, what features should be combined and how and when, or if. As a basis,
omorfi will support all reasonable classifications and tries to guess missing
facts if possible. The below tables show the allowed class names and the
guessing algorithms in lack of those. We have adapted a classification that is
based on current dictionaries plus so that the classification tells everything
needed for inflectional morphology. Other classifications leave more or less to
be guessed, which we also will try if needed.

## The official dictionary system–_nssl_ ##

Official dictionary uses numbers for classes, which should tell something of
stem variation and a bit of suffix allomorph selection, then a letter to tell a
bit more about gradation. Numbers 1 to 49 for nominals (no distinction made
between adjectives and nouns), 50 for hiding the real inflection class of
regular compounds, 51 for compounds with agreeing inflection pattern for each
part, 52 to 78 for verbs and orthogonally A to M for the additional gradation.
In some classes this classification ~~hides~~ generalises over few features,
such as nasal assimilation or triphtong simplification so you have to guess it
from the stem, also, vowel harmony is unmarked.

### The older official system-_nssk_ ###

The first(?) official dictionary, _nykysuomen sanakirja_ in early 1900's had a
few more classes and less generalisations, but it also has few that have become
obsolete. And the inflection tables have numerous unusual forms from modern
standard pov.

## Joukahainen system ##

Joukahainen uses system based on example words instead of numbers, but it's more
or less mixture of classification of the official dictionaries. The example
words are a good system, way better than code numbers, however, the gradation
that is coded separately is slightly confusing. For example, the word _iäkäs_ is
not in class _iäkäs_, but _iäkäs-av1_.

## Finnish Wiktionary system ##

Finnish wiktionary is still evolving, breathing, living crowd-sourced project,
we currently use some sort of mishmash of the official systems and example words
as well. Check the rules and examples when you start.

## The final classification in omorfi ##

Omorfi uses even more explicit classification, that spells out the
part-of-speech, the stem changes (including gradation type), the allomorph
selection, the vowel harmony, the lenghtening stem vowel, and other features of
inflectional morphology. We provide both code for this and proper uniquely
identifying example word that actually reflects the class. This means that each
combination of stem changes and suffix sets gets its own class here,  e.g.
_talo_ and _asu_ have different classes since illative suffixes are _-on_ and
_-un_ respectively; so are _kivi_ and _ravi_ as their partitives are _ä_ and _a_
respectively. So just to be clear here, we make **no morphophonological
generalisations** whatsoever.

The system we use will get rid of all the classifications where words kind of
belong into two or even three classes in other systems, if word has forms of two
inflection patterns then it is a new inflection pattern, not two separate words.
Also the class 49 which kind of has two sets of stems and inflections is broken
a bit, since it has two dictionary entries per word, one of which is could be in
class 48 and other is just defective.

If you compare this system to the _nssl_ one, we add stem vowel as classifier,
as it selects the vowel harmony and illative vowel, thus paradigm class 1 is now
4 times more classes 1o, 1u, 1y and 1y. On gradation side, D consists really of
three different gradations: after consonant it is the same as A, between single
vowels it is `k~0~’`, and between vowel triplets with equal vowels on sides it's
`k~’`, this is orthographical convention but since it must be implemented in
morphology we must classify this.

But all of the old systems are also recognised. If you provide your contributed
words in whatever format we can surely make use of it.


# Exact, full classification #

The classification shown here assigns separate class for each different
combination of five features of the word, shown in the first five columns of the
table:

* Suffix allomorph set number. Variants are detailed in a table on another wiki
  page, but based on kotus classes atm.
* The gradating pair in form of _X~Y_ where _X_ is the form in dictionary form,
  _Y_ an inflected form. 0 if no gradation.
* The stem variations and stem vowel in form of _(V)_ _A~B..._, where _V_ is the
  stem vowel if relevant, and _A_, _B_ a set of variations.
* vowel harmony class, F for front and B for back, for other classes it is 0.

The uniqueness of the combinations of these is what determines whether we have a
unique paradigm or not.

The suffix allomorphs are partially dependent on stem variation, the vowel
harmony can be defined by stem variations and so on, so the features are not
independent except for few cases (if they were independent, the number of
classes would directly be number of all combinations of values).

In the below table, the first columns are abovementioned classification features
(you can use them as a shorthand for the class if you don't remember the example
word) . The class to use is the example word from the last column, e.g. _talo_
for the first class.

The middle columns of the table show the classification class that might be the
closest in the other systems. The last column is our example word, which should
be usd as the classification. The example words prefixed with question marks are
subject to change in the future, since they are not most typical examples (e.g.
because they are two-syllable words in primarily three syllable classe) of their
respective classes or are easily confused (e.g. they are more likely to be
adjectives than nouns).

## Nouns (and proper nouns) ##

| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |
|:---------------|:--------------|:------------|:------------|:-------|:----------|:------|:-----|:----------|:-----------------------------------|
| 1 | 0 | o | B | 1 | valo | valo | 1 | valo | **talo**  |
| 1 | 0 | u | B | 1 | valo | valo | 1 | valo | **asu**  |
| 1 | 0 | y | F | 1 | valo | valo | 1 | valo | **kärry**  |
| 1 | 0 | ö | F | 1 | valo | valo | 1 | valo | **mömmö**  |
| 1 | kk~k | o | B | 1-A | valo | valo | 1 | valo | **ukko**  |
| 1 | kk~k | u | B | 1-A | valo | valo | 1 | valo | **tikku**  |
| 1 | kk~k | y | F | 1-A | valo | valo | 1 | valo | **myrkky**  |
| 1 | kk~k | ö | F | 1-A | valo | valo | 1 | valo | **yökkö**  |
| 1 | pp~p | o | B | 1-B | valo | valo | 1 | valo | **happo**  |
| 1 | pp~p | u | B | 1-B | valo | valo | 1 | valo | **lippu**  |
| 1 | pp~p | y | F | 1-B | valo | valo | 1 | valo | **ryyppy**  |
| 1 | pp~p | ö | F | 1-B | valo | valo | 1 | valo | **törppö**  |
| 1 | tt~t | o | B | 1-C | valo | valo | 1 | valo | **hirtto**  |
| 1 | tt~t | u | B | 1-C | valo | valo | 1 | valo | **torttu**  |
| 1 | tt~t | y | F | 1-C | valo | valo | 1 | valo | **pytty**  |
| 1 | tt~t | ö | F | 1-C | valo | valo | 1 | valo | **pönttö**  |
| 1 | k~0 | o | B | 1-D | valo | valo | 1 | valo | **pelko**  |
| 1 | k~0 | u | B | 1-D | valo | valo | 1 | valo | **alku**  |
| 1 | k~0 | y | F | 1-D | valo | valo | 1 | valo | **hylky**  |
| 1 | k~0 | ö | F | 1-D | valo | valo | 1 | valo | **mörkö**  |
| 1 | k~0~’ | o | B | 1-D | valo | valo | 1 | valo | **teko**  |
| 1 | k~0~’ | u | B | 1-D | valo | valo | 1 | valo | **maku**  |
| 1 | k~0~’ | y | F | 1-D | valo | valo | 1 | valo | **näky**  |
| 1 | k~0~’ | ö | F | 1-D | valo | valo | 1 | valo | **näkö**  |
| 1 | k~0~’ | o~0 | B | 1-D | valo | valo | 1 | valo | **koko**  |
| 1 | k~’ | o | B | 1-D | valo | valo | 1 | valo | **ruoko**  |
| 1 | k~’ | u | B | 1-D | valo | valo | 1 | valo | **liuku**  |
| 1 | p~v | o | B | 1-E | valo | valo | 1 | valo | **hepo**  |
| 1 | p~v | u | B | 1-E | valo | valo | 1 | valo | **apu**  |
| 1 | p~v | y | F | 1-E | valo | valo | 1 | valo | **käpy**  |
| 1 | p~v | ö | F | 1-E | valo | valo | 1 | valo | **löpö**  |
| 1 | t~d | o | B | 1-F | valo | valo | 1 | valo | **veto**  |
| 1 | t~d | u | B | 1-F | valo | valo | 1 | valo | **kuitu**  |
| 1 | t~d | y | F | 1-F | valo | valo | 1 | valo | **vety**  |
| 1 | t~d | ö | F | 1-F | valo | valo | 1 | valo | **häätö**  |
| 1 | k~g | o | B | 1-G | valo | valo | 1 | valo | **runko**  |
| 1 | k~g | u | B | 1-G | valo | valo | 1 | valo | **vinku**  |
| 1 | k~g | y | F | 1-G | valo | valo | 1 | valo | **sänky**  |
| 1 | k~g | ö | F | 1-G | valo | valo | 1 | valo | ?**ylänkö**  |
| 1 | p~m | o | B | 1-H | valo | valo | 1 | valo | **sampo**  |
| 1 | p~m | u | B | 1-H | valo | valo | 1 | valo | **rumpu**  |
| 1 | p~m | ö | F | 1-H | valo | valo | 1 | valo | **lämpö**  |
| 1 | t~l | o | B | 1-I | valo | valo | 1 | valo | **kielto**  |
| 1 | t~l | u | B | 1-I | valo | valo | 1 | valo | ?**huoliteltu**  |
| 1 | t~l | y | F | 1-I | valo | valo | 1 | valo | ?**epäilty**  |
| 1 | t~l | ö | F | 1-I | valo | valo | 1 | valo | ?**sisältö**  |
| 1 | t~n | o | B | 1-J | valo | valo | 1 | valo | **tunto**  |
| 1 | t~n | u | B | 1-J | valo | valo | 1 | valo | **lintu**  |
| 1 | t~n | y | F | 1-J | valo | valo | 1 | valo | **mänty**  |
| 1 | t~n | ö | F | 1-J | valo | valo | 1 | valo | **kääntö**  |
| 1 | t~r | o | B | 1-K | valo | valo | 1 | valo | **siirto**  |
| 1 | t~r | u | B | 1-K | valo | valo | 1 | valo | **Mertu** |
| 1 | t~r | ö | F | 1-K | valo | valo | 1 | valo | **Värtö** |
| 1 | k~v | o | B | 1-M | valo | valo | 1 | valo | **Malko**  |
| 1 | k~v | u | B | 1-M | valo | valo | 1 | valo | **luku**  |
| 1 | k~v | y | F | 1-M | valo | valo | 1 | valo | **kyky**  |
| 2 | 0 | o | B | 2 | palvelu | arvelu | 2 | arvelu | **ruipelo**  |
| 2 | 0 | u | B | 2 | palvelu | arvelu | 2 | arvelu | **seikkailu**  |
| 2 | 0 | y | F | 2 | palvelu | arvelu | 2 | arvelu | **vehkeily**  |
| 2 | 0 | ö | F | 2 | palvelu | arvelu | 2 | arvelu | **jäätelö**  |
| 3 | 0 | o | B | 3 | valtio | autio | 3 | autio | **tuomio**  |
| 3 | 0 | ö | F | 3 | valtio | autio | 3 | autio | **häiriö**  |
| 3 | 0 | e | B | 3 | valtio | autio | 3 | autio | **zombie**  |
| 3 | 0 | e | F | 3 | valtio | autio | 3 | autio | **Bernie**  |
| 8~7 | 0 | e | B | - | - | - | - | - | **aamukolme** |
| 4 | kk~k | o | B | 4-A | laatikko | (valo) | (2) | (arvelu) | **lepakko**  |
| 4 | kk~k | ö | F | 4-A | laatikko | (valo) | (2) | (arvelu) | **yksikkö**  |
| 5 | 0 | i ~ e ~ 0 | B | 5 | risti | risti | 4 | risti | **ruuvi**  |
| 5 | 0 | i ~ e ~ 0 | F | 5 | risti | risti | 4 | risti | **tyyli**  |
| 5 | kk~k | i ~ e ~ 0 | B | 5-A | risti | risti | 4 | risti | **lokki**  |
| 5 | kk~k | i ~ e ~ 0 | F | 5-A | risti | risti | 4 | risti | **häkki**  |
| 5 | pp~p | i ~ e ~ 0 | B | 5-B | risti | risti | 4 | risti | **kuppi**  |
| 5 | pp~p | i ~ e ~ 0 | F | 5-B | risti | risti | 4 | risti | **tyyppi**  |
| 5 | tt~t | i ~ e ~ 0 | B | 5-C | risti | risti | 4 | risti | **kortti**  |
| 5 | tt~t | i ~ e ~ 0 | F | 5-C | risti | risti | 4 | risti | **skeitti**  |
| 5 | k~0~’ | i ~ e ~ 0 | B | 5-D | risti | risti | 4 | risti | **laki**  |
| 5 | p~v | i ~ e ~ 0 | B | 5-E | risti | risti | 4 | risti | **hupi**  |
| 5 | p~v | i ~ e ~ 0 | B | 5-E | risti | risti | 4 | risti | **Riipi**  |
| 5 | t~d | i ~ e ~ 0 | B | 5-F | risti | risti | 4 | risti | **tauti**  |
| 5 | t~d | i ~ e ~ 0 | F | 5-F | risti | risti | 4 | risti | **nihti**  |
| 5 | k~g | i ~ e ~ 0 | B | 5-G | risti | risti | 4 | risti | **vanki**  |
| 5 | k~g | i ~ e ~ 0 | F | 5-G | risti | risti | 4 | risti | **hämminki**  |
| 5 | p~m | i ~ e ~ 0 | B | 5-H | risti | risti | 4 | risti | **Lampi'** |
| 5 | p~m | i ~ e ~ 0 | F | 5-H | risti | risti | 4 | risti | **Rimpi'** |
| 5 | t~l | i ~ e ~ 0 | F | 5-I | risti | risti | 4 | risti | **pelti**  |
| 5 | t~n | i ~ e ~ 0 | B | 5-J | risti | risti | 4 | risti | **sointi**  |
| 5 | t~n | i ~ e ~ 0 | F | 5-J | risti | risti | 4 | risti | **vienti**  |
| 5 | 0 | 0 ~ i ~ e ~ 0 | B | 5 | risti | edam | 4 | risti | **punk** (~ punkki)  |
| 5 | 0 | 0 ~ i ~ e ~ 0 | F | 5 | risti | edam | 4 | risti | **zen** (~ zeni)  |
| 6 | 0 | i ~ e ~ 0 | B | 6 | paperi | paperi | 5 | paperi | **kanaali**  |
| 6 | 0 | i ~ e ~ 0 | F | 6 | paperi | paperi | 5 | paperi | **kehveli**  |
| 6 | 0 | 0 ~ i ~ e ~ 0 | B | 6 | paperi | kalsium | 7 | kalsium | **stadion** (~ stadioni) |
| 6 | 0 | 0 ~ i ~ e ~ 0 | F | 6 | paperi | kalsium | 7 | kalsium | **besserwisser** (besserwisseri)  |
| 6+ten | 0 | (i ~ 0) ~ e ~ 0 | B | 6 | paperi | paperi | 52 | sankari | **sankari** (~ sankar)  |
| 7 | 0 | i ~ e ~ 0 | B | 7 | ovi | lovi | 8 | lovi | **onni**  |
| 7 | 0 | i ~ e ~ 0 | F | 7 | ovi | lovi | 8 | lovi | **kivi**  |
| 7 | pp~p | i ~ e ~ 0 | B | 7-B | ovi | lovi | 8 | lovi | **happi**  |
| 7 | pp~p | i ~ e ~ 0 | F | 7-B | ovi | lovi | 8 | lovi | **typpi**  |
| 7 | k~0~’ | i ~ e ~ 0 | B | 7-D | ovi | lovi | 8 | lovi | **noki**  |
| 7 | k~0~’ | i ~ e ~ 0 | F | 7-D | ovi | lovi | 8 | lovi | **käki**  |
| 7 | p~v | i ~ e ~ 0 | B | 7-E | ovi | lovi | 8 | lovi | **korpi**  |
| 7 | p~v | i ~ e ~ 0 | F | 7-E | ovi | lovi | 8 | lovi | **kilpi**  |
| 7 | t~d | i ~ e ~ 0 | B | 7-F | ovi | lovi | 8 | lovi | **lahti**  |
| 7 | t~d | i ~ e ~ 0 | F | 7-F | ovi | lovi | 8 | lovi | **lehti**  |
| 7 | k~g | i ~ e ~ 0 | B | 7-G | ovi | lovi | 8 | lovi | **onki**  |
| 7 | k~g | i ~ e ~ 0 | F | 7-G | ovi | lovi | 8 | lovi | **henki**  |
| 7 | p~m | i ~ e ~ 0 | B | 7-H | ovi | lovi | 8 | lovi | **sampi**  |
| 7 | p~m | i ~ e ~ 0 | F | 7-H | ovi | lovi | 8 | lovi | **rimpi**  |
| 7 | k~j | i ~ e ~ 0 | B | 7-L | ovi | lovi | 8 | lovi | **arki**  |
| 7 | k~j | i ~ e ~ 0 | F | 7-L | ovi | lovi | 8 | lovi | **järki**  |
| 7+? | 0 | i ~ e ~ 0 | F | 7 | ovi | kiiski | 8 | lovi | ? (kiiski) |
| 7+? | p~m | i ~ e ~ 0 | B | 7-H | ovi | lampi | 8 | lovi | ? (lampi) |
| 7~29 | 0 | i ~ e ~ 0 | B | 7 | ovi | lovi | 46 | hapsi | **hapsi**  |
| 7~29 | 0 | i ~ e ~ 0 | B | 7 | ovi | lovi | 49 | suksi | **suksi**  |
| 7~29 | 0 | i ~ e ~ 0 | B | 7 | ovi | lovi | 50 | uksi | **uksi**  |
| 8 | 0 | 0 | B | 8 | nalle | nalle | 9 | nalle | **nalle**  |
| 8 | 0 | 0 | F | 8 | nalle | nalle | 9 | nalle | **nisse**  |
| 8 | kk~k | 0 | B | 8 | nalle | nalle | 9 | nalle | **nukke**  |
| 8 | kk~k | 0 | F | 8 | nalle | nalle | 9 | nalle | **Ekke**  |
| 8 | pp~p | 0 | B | 8 | nalle | nalle | 9 | nalle | **Rappe**  |
| 8 | pp~p | 0 | F | 8 | nalle | nalle | 9 | nalle | **jeppe**  |
| 8 | tt~t | 0 | B | 8 | nalle | nalle | 9 | nalle | **Lotte** |
| 8 | tt~t | 0 | F | 8 | nalle | nalle | 9 | nalle | **Mette** |
| 9 | 0 | a ~ o | B | 9 | kala | kala | 10 | kala | **kirja**  |
| 9 | 0 | ä ~ ö | F | 9 | kala | kala | 10 | kala | **ympärystä**  |
| 9 | kk~k | a ~ o | B | 9-A | kala | kala | 10 | kala | **politiikka**  |
| 9 | pp~p | a ~ o | B | 9-B | kala | kala | 10 | kala | **tippa**  |
| 9 | tt~t | a ~ o | B | 9-C | kala | kala | 10 | kala | **mitta**  |
| 9 | k~0 | a ~ o | B | 9-D | kala | kala | 10 | kala | **virka**  |
| 9 | k~0~’ | a ~ o | B | 9-D | kala | kala | 10 | kala | **vika**  |
| 9 | k~’ | a ~ o | B | 9-D | kala | kala | 10 | kala | **vaaka**  |
| 9 | p~v | a ~ o | B | 9-E | kala | kala | 10 | kala | **salpa**  |
| 9 | t~d | a ~ o | B | 9-F | kala | kala | 10 | kala | **pata**  |
| 9 | k~g | a ~ o | B | 9-G | kala | kala | 10 | kala | **lanka**  |
| 9 | p~m | a ~ o | B | 9-H | kala | kala | 10 | kala | **rampa**  |
| 9 | t~l | a ~ o | B | 9-I | kala | kala | 10 | kala | **valta**  |
| 9 | t~n | a ~ o | B | 9-J | kala | kala | 10 | kala | ?**kutsunta**  |
| 9 | t~n | ä ~ ö | F | 9-J | kala | kala | 10 | kala | ?**kysyntä**  |
| 9 | t~r | a ~ o | B | 9-K | kala | kala | 10 | kala | **kerta**  |
| 9 | t~n | a ~ o | B | 9-J | kala | veran|ta | 10 | kala | **veranta**  |
| 10 | 0 | a ~ 0 | B | 10 | koira | koira | 11 | koira | **voima**  |
| 10 | 0 | ä ~ 0 | F | 10 | koira | koira | 11 | koira | **höpöttäjä**  |
| 10 | kk~k | a ~ 0 | B | 10-A | koira | koira | 11 | koira | **luokka**  |
| 10 | kk~k | ä ~ 0 | F | 10-A | koira | koira | 11 | koira | **hölkkä**  |
| 10 | pp~p | a ~ 0 | B | 10-B | koira | koira | 11 | koira | **kuoppa**  |
| 10 | pp~p | ä ~ 0 | F | 10-B | koira | koira | 11 | koira | **seppä**  |
| 10 | tt~t | a ~ 0 | B | 10-C | koira | koira | 11 | koira | **rotta**  |
| 10 | tt~t | ä ~ 0 | F | 10-C | koira | koira | 11 | koira | **kenttä**  |
| 10 | k~0 | a ~ 0 | B | 10-D | koira | koira | 11 | koira | **sulka**  |
| 10 | k~0(~j) | ä ~ 0 | F | 10-D | koira | koira | 11 | koira | **nälkä**  |
| 10 | k~0~’ | a ~ 0 | B | 10-D | koira | koira | 11 | koira | **loka**  |
| 10 | k~0~’ | uo ~ uu, a ~ 0 | B | 10-D | koira | koira | 11 | koira | **ruoka**  |
| 10 | k~0~’ | ä ~ 0 | F | 10-D | koira | koira | 11 | koira | **reikä**  |
| 10 | k~j | ä ~ 0 | F | 10-L | koira | koira | 11 | koira | **Olka** |
| 10 | k~j | ä ~ 0 | F | 10-L | koira | koira | 11 | koira | **ylkä** |
| 10 | p~v | a ~ 0 | B | 10-E | koira | koira | 11 | koira | **lupa**  |
| 10 | p~v | ä ~ 0 | F | 10-E | koira | koira | 11 | koira | **leipä**  |
| 10 | t~d | a ~ 0 | B | 10-F | koira | koira | 11 | koira | **sota**  |
| 10 | t~d | ä ~ 0 | F | 10-F | koira | koira | 11 | koira | **pöytä**  |
| 10 | k~g | a ~ 0 | B | 10-G | koira | koira | 11 | koira | **honka**  |
| 10 | k~g | ä ~ 0 | F | 10-G | koira | koira | 11 | koira | **kenkä**  |
| 10 | p~m | a ~ 0 | B | 10-H | koira | koira | 11 | koira | **kompa**  |
| 10 | t~l | a ~ 0 | B | 10-I | koira | koira | 11 | koira | **multa**  |
| 10 | t~l | ä ~ 0 | F | 10-I | koira | koira | 11 | koira | **syltä**  |
| 10 | t~n | a ~ 0 | B | 10-J | koira | koira | 11 | koira | **kunta**  |
| 10 | t~n | ä ~ 0 | F | 10-J | koira | koira | 11 | koira | **häntä**  |
| 10 | t~r | a ~ 0 | B | 10-K | koira | koira | 11 | koira | **Horta** |
| 10+ata | 0 | a ~ 0 | B | 10 | koira | asema | 13 | asem|a | **asema**  |
| 10+ätä | 0 | ä ~ 0 | F | 10 | koira | asema | 13 | asem|a | **elämä**  |
| 10+ata+? | 0 | a ~ 0 (~o) | B | 10 | koira | asema | 16 | kantaj|a |  |
| 10+ten | 0 | a ~ 0 | B | 10 | koira | koira | 53 | jumala | **jumala** ~ jumal  |
| 10 | 0 | an ~ 0 | B | 10 | koira | - | - | - | **aamukahdeksan** |
| 10 | 0 | än ~ 0 | F | 10 | koira | - | - | - | **aamuyhdeksän** |
| 10 | k~0 | i ~ j, a ~ 0 | B | 10-D | koira |  poika |  11 | koira | **poika**  |
| 11 | 0 | a ~ 0 ~ o | B | 11 | omena | apaja | 12 | matala | **probleema**  |
| 11 | 0 | ä ~ 0 ~ ö | F | 11 | omena | apaja | 12 | matala | **käpälä**  |
| 12 | 0 | a ~ o | B | 12 | kulkija | kulkija | 14 | kulkija | **makkara**  |
| 12 | 0 | ä ~ ö | F | 12 | kulkija | kulkija | 14 | kulkija | **häkkyrä**  |
| 12+? | 0 | a ~ o | B | 12 | kulkija | peruna | 17 | peruna |  |
| 12+? | 0 | a ~ o | B | 12 | kulkija | herttua | 20 | herttua |  |
| 13 | 0 | a ~ o | B | 13 | katiska | karahka | 15 | karahka | **kitara**  |
| 13 | 0 | a ~ o | ö | 13 | katiska | karahka | 15 | karahka | **siivilä**  |
| 13+? | 0 | a ~ o (~0) | B | 13 | katiska | pasuuna | 18 | pasuuna | (rakuuna)  |
| 14 | kk~k | a ~ o | B | 14-A | solakka | (karahka) | (15) | (karahka) | **lusikka**  |
| 14 | kk~k | ä ~ ö | F | 14-A | solakka | (karahka) | (15) | (karahka) | **kämmekkä**  |
| 14 | pp~p | a ~ o | B | 14-B | solakka | (karahka) | (15) | (karahka) | **ulappa**  |
| 14 | tt~t | a ~ o | B | 14-C | solakka | (karahka) | (15) | (karahka) | **pohatta**  |
| 15 | 0 | a (~ e) ~ 0 | B | 15 | ? | korkea | 21 | korkea | **sokea** (~ soke|e)  |
| 15 | 0 | ä (~ e) ~ 0 | F | 15 | ? | korkea | 21 | korkea | **lipeä** (~ lipe|e)  |
| 15 | 0 | a ~ 0 | B | 15 | ? | korkea | 21 | korkea | **Piiroa**  |
| 15 | 0 | a ~ 0 | B | 15 | ? | korkea | 21 | korkea | **tanhua**  |
| 16 | 0 | pi ~ ma ~ pa ~ p | B | 16-H | vanhempi | suurempi | 22 | suurempi | **vanhempi**  |
| 17 | 0 | a ~ 0 | B | 17 | vapaa | vapaa | 23 | vainaa | **vainaa**  |
| 17 | 0 | e ~ 0 | B | 17 | vapaa | vapaa | 23 | vainaa | **tokee**  |
| 17 | 0 | e ~ 0 | F | 17 | vapaa | vapaa | 23 | vainaa | **Lenttee**  |
| 17 | 0 | e ~ 0 | B | 17 | vapaa | vapaa | 23 | vainaa | **Vaanii**  |
| 17 | 0 | e ~ 0 | F | 17 | vapaa | vapaa | 23 | vainaa | **Tihvii**  |
| 17 | 0 | o ~ 0 | B | 17 | vapaa | vapaa | 24 | tienoo | **tienoo**  |
| 17 | 0 | u ~ 0 | B | 17 | vapaa | vapaa | 25 | leikkuu | **leikkuu**  |
| 17 | 0 | ä ~ 0 | F | 17 | vapaa | vapaa | 23 | vainaa | **Pyhtää**  |
| 17 | 0 | y ~ 0 | F | 17 | vapaa | vapaa | 23 | vainaa | **Hyötyy**  |
| 17 | 0 | ö ~ 0 | F | 17 | vapaa | vapaa | 23 | vainaa | **Ylöö**  |
| 18 | 0 | a ~ 0 | B | 18 | maa | pii | 28  | maa | **maa**  |
| 18 | 0 | e ~ 0 | F | 18 | maa | pii | 28  | maa | **tee**  |
| 18 | 0 | i ~ 0 | B | 18 | maa | pii | 28  | maa | **hai**  |
| 18 | 0 | i ~ 0 | F | 18 | maa | pii | 27 | pii | **pii**  |
| 18 | 0 | o ~ 0 | B | 18 | maa | pii | 28  | maa | **ookoo**  |
| 18 | 0 | u ~ 0 | B | 18 | maa | pii | 29 | puu | **puu**  |
| 18 | 0 | y ~ 0 | F | 18 | maa | pii | 29 | puu | **pyy**  |
| 18 | 0 | ä ~ 0 | F | 18 | maa | pii | 29 | puu | **pää**  |
| 18 | 0 | ö ~ 0 | F | 18 | maa | pii | 29 | puu | **köö**  |
| 19 | 0 | uo ~ o | B | 19 | suo | suo | 30 | suo | **vuo**  |
| 19 | 0 | ie ~ e | F | 19 | suo | suo | 30 | suo | **tie**  |
| 19 | 0 | yö ~ ö | F | 19 | suo | suo | 30 | suo | **yö**  |
| 20 | 0 | a ~ 0 | B | 20 | filee | kamee | 26 | kamee | **nugaa**  |
| 20 | 0 | e ~ 0 | B | 20 | filee | kamee | 26 | kamee | **patee**  |
| 20 | 0 | e ~ 0 | F | 20 | filee | filee | 26 | kamee | **bidee**  |
| 20 | 0 | o ~ 0 | B | 20 | filee | kamee | 26 | kamee | **trikoo**  |
| 20 | 0 | u ~ 0 | B | 20 | filee | kamee | 26 | kamee | **raguu**  |
| 20 | 0 | y ~ 0 | F | 20 | filee | filee | 26 | kamee | **fondyy**  |
| 20 | 0 | ö ~ 0 | F | 20 | filee | filee | 26 | kamee | **miljöö**  |
| 21 | 0 | (a) | B | 21 | rosé | rosé | 31 | bébé | **chachacha** |
| 21 | 0 | (e) | B | 21 | rosé | rosé | 31 | bébé | **rosé** |
| 21 | 0 | (e) | F | 21 | rosé | bébé | 31 | bébé | **bébé** |
| 21 | 0 | (e) | B | 21 | rosé | rosé | 31 | bébé | **brasserie** |
| 21 | 0 | (e~i) | B~F | 21 | rosé | rosé | 31 | bébé | **reggae** |
| 21 | 0 | (e~i) | F | 21 | rosé | rosé | 31 | bébé | **brie** |
| 21 | 0 | (i~y) | B~F | 21 | rosé | rosé | 31 | bébé | **gay** |
| 21+a | 0 | (i~y) | B~F | 21 | rosé | rosé | 31 | bébé | **jockey** |
| 21 | 0 | (i~y) | B | 21 | rosé | rosé | 31 | bébé | **cowboy** |
| 21 | 0 | (o~u) | F | 21 | rosé | rosé | 31 | bébé | **esquimau** |
| 21 | 0 | (u) | B | 21 | rosé | rosé | 31 | bébé | **kungfu** |
| 21 | 0 | (y) | B | 21 | rosé | rosé | 31 | bébe | **kentucky** |
| 21 | 0 | (y) | F | 21 | rosé | rosé | 31 | bébé | **fondue** |
| 21 | 0 | (ö) | F | 21 | rosé | rosé | 31 | bébé | **Malmö** |
| 22 | 0 | (a) 0 ~ ’ | B | 22 | parfait | parfait | - | - | **nougat**  |
| 22 | 0 | (e) 0 ~ ’ | B | 22 | parfait | parfait | - | - | **parfait**  |
| 22 | 0 | (e) 0 ~ ’ | F | 22 | parfait | parfait | - | - | **beignet**  |
| 22 | 0 | (i) 0 ~ ’ | B | 22 | parfait | parfait | - | - | **Versailles** |
| 22 | 0 | (o) 0 ~ ’ | B | 22 | parfait | parfait | - | - | **bordeaux**  |
| 22 | 0 | (u) 0 ~ ’ | B | 22 | parfait | parfait | - | - | **show**  |
| 22 | 0 | (y) 0 ~ ’ | F | 22 | parfait | parfait | - | - | **Camus** |
| 22 | 0 | (ö) 0 ~ ’ | F | 22 | parfait | parfait | - | - | **monsieur**  |
| 23 | 0 | i ~ e ~ 0 | B | 23 | tiili | tuohi | 32 | tuohi | **tuli**  |
| 23 | 0 | i ~ e ~ 0 | F | 23 | tiili | tuohi | 32 | tuohi | **syli**  |
| 23+ten | 0 | i ~ e ~ 0 | B | 23 | tiili | tuohi | 33 | lohi | **jouhi**  |
| 23+ten | 0 | i ~ e ~ 0 | F | 23 | tiili | tuohi | 33 | lohi | **riihi**  |
| 24 | 0 | i ~ e ~ 0 | B | 24 | uni | huuli | - | - | **ruuhi**  |
| 24 | 0 | i ~ e ~ 0 | F | 24 | uni | huuli | - | - | **hiiri**  |
| 24 | 0 | i ~ e ~ 0 | F (a) | 24 | uni | meri | - | - |  **meri**  |
| 25~26 | 0 | mi ~ me ~ n ~ m | B | 25 | toimi | lumi | 35 | lumi | **taimi**  |
| 25~26 | 0 | mi ~ me ~ n ~ m | F | 25 | toimi | niemi | 37 | niemi | **liemi**  |
| 26 | 0 | i ~ e ~ 0 | B | 26 | pieni | pieni | - | - | **kaari**  |
| 26 | 0 | i ~ e ~ 0 | F | 26 | pieni | nuori | - | - | **mieli**  |
| 27 | t~d | si ~ te ~ s ~ t | B | 27 | käsi | susi | 40 | susi | **kausi**  |
| 27 | t~d | si ~ te ~ s ~ t | F | 27 | käsi | susi | 40 | susi | **köysi**  |
| 28 | t~n | si ~ te ~ s ~ t | B | 28 | kynsi | kansi | 44 | kansi | **ponsi**  |
| 28 | t~n | si ~ te ~ s ~ t | F | 28 | kynsi | kansi | 44 | kansi | **länsi**  |
| 28 | t~r | si ~ te ~ s ~ t | B | 28 | kynsi | kansi | 42 | hirsi | **varsi**  |
| 28 | t~r | si ~ te ~ s ~ t | F | 28 | kynsi | kansi | 42 | hirsi | **virsi**  |
| 28 | t~l | si ~ te ~ s ~ t | F | 28 | kynsi | kansi | 43 | jälsi | **jälsi**  |
| 29 | 0 | psi ~ pse ~ ps ~ s | B | 29 | lapsi | ? | 45 | lapsi | **lapsi**  |
| 30 | 0 | tsi ~ tse ~ ts ~ s | F | 30 | veitsi | ? | 47 | veitsi | **veitsi**  |
| 30+a | 0 | tsi ~ tse ~ ts ~ s |  F | 30 | veitsi | ? | 48 | peitsi | **peitsi**  |
| 31 | t~d | ksi ~ hte ~ ks ~ h | B | 31 | kaksi | ? | 51 | kaksi | **haaksi**  |
| 31 | t~d | ksi ~ hte ~ ks ~ h | F | 31 | kaksi | - | - | - | **aamuyksi** |
| 32 | 0 | 0 ~ e | B | 32 | sisar | ahven | 54 | sisar | **joutsen**  |
| 32 | 0 | 0 ~ e | F | 32 | sisar | ahven | 54 | sisar | **siemen**  |
| 32 | t~tt | 0 ~ e | B | 32-C | sisar | ahven | 54 | sisar | **ajatar**  |
| 32 | t~tt | 0 ~ e | F | 32-C | sisar | ahven | 54 | sisar | **tytär**  |
| 32 | 0~k | 0 ~ e | F | 32-D | sisar | ahven | 54 | sisar | **ien**  |
| 32+na | 0 | 0 ~ e | B | 32 | sisar | ahven | 55 | ahven | **ahven**  |
| 32 | 0 | en ~ e | F | 8 | nalle | - | - | - | **aamukymmenen** |
| 33 | 0 | n ~ me ~ m | B | 33 | kytkin | uistin | 56 | uistin | **puhelin**  |
| 33 | 0 | n ~ me ~ m | F | 33 | kytkin | uistin | 56 | uistin | **elin**  |
| 33 | k~kk | n ~ me ~ m | F | 33-A | kytkin | uistin | 56 | uistin | **härkin**  |
| 33 | t~tt | n ~ me ~ m | B | 33-C | kytkin | uistin | 56 | uistin | **suodatin** |
| 33 | t~tt | n ~ me ~ m | F | 33-C | kytkin | uistin | 56 | uistin | **heitin**  |
| 33 | 0~k | n ~ me ~ m | B | 33-D | kytkin | uistin | 56 | uistin | **puin**  |
| 33 | 0~k | n ~ me ~ m | F | 33-D | kytkin | uistin | 56 | uistin | **pyyhin**  |
| 33 | v~p | n ~ me ~ m | B | 33-E | kytkin | uistin | 56 | uistin | **raavin**  |
| 33 | v~p | n ~ me ~ m | F | 33-E | kytkin | uistin | 56 | uistin | **särvin**  |
| 33 | d~t | n ~ me ~ m | B | 33-F | kytkin | uistin | 56 | uistin | **vaadin**  |
| 33 | d~t | n ~ me ~ m | F | 33-F | kytkin | uistin | 56 | uistin | **säädin**  |
| 33 | d~t | n ~ me ~ m | B | 33-F | kytkin | uistin | 56 | uistin | **tahdon** |
| 33 | d~t | n ~ me ~ m | B | 33-F | kytkin | uistin | 56 | uistin | **laidun** |
| 33 | l~t | n ~ me ~ m | B | 33-I | kytkin | uistin | 56 | uistin | **askellin**  |
| 33 | l~t | n ~ me ~ m | F | 33-I | kytkin | uistin | 56 | uistin | **sivellin**  |
| 33 | n~t | n ~ me ~ m | B | 33-J | kytkin | uistin | 56 | uistin | **muunnin**  |
| 33 | n~t | n ~ me ~ m | F | 33-J | kytkin | uistin | 56 | uistin | **käännin**  |
| 33 | r~t | n ~ me ~ m | B | 33-K | kytkin | uistin | 56 | uistin | **kiharrin**  |
| 33 | r~t | n ~ me ~ m | F | 33-K | kytkin | uistin | 56 | uistin | **kerroin**  |
| 33 | r~t | n ~ me ~ m | F | 33-K | kytkin | uistin | 56 | uistin | **kierrin**  |
| 33 | j~k | n ~ me ~ m | B | 33-L | kytkin | uistin | 56 | uistin | **poljin**  |
| 33+nä | 0 | n ~ me ~ m | F | 33 | kytkin | sydän | 56 | uistin | **sydän**  |
| 34 | t~tt | o | B | 34-C | viaton | viaton | 57 | viaton | **Osaton**  |
| 34 | t~tt | ö | F | 34-C | viaton | viaton | 57 | viaton | **Nimetön**  |
| 34 | t~tt | oi ~ o | B | 34-C | viaton | viaton | 57 | viaton | **Kalatoin**  |
| 34 | t~tt | öi ~ ö | F | 34-C | viaton | viaton | 57 | viaton | **Nimetöin**  |
| 35 | m~p | n ~ mä ~ m | F | 35-H | lämmin | ? | 58 | lämmin | **lämmin**  |
| 36 | 0 | n ~ mpa ~ mma ~ mp ~ mm | B | 36 | - | - | - | - | **kylänvanhin** |
| 36 | 0 | n ~ mpä ~ mmä ~ mp ~ mm | F | 36 | - | - | - | - | **lähin** |
| 38 | 0 | nen ~ se ~ s | B | 38 | nainen | nainen | 63 | hevonen | **aakkostaminen**  |
| 38 | 0 | nen ~ se ~ s | F | 38 | nainen | nainen | 63 | hevonen | **kylkiäinen**  |
| 39 | 0 | s ~ kse ~ ks | B | 39 | vastaus | vastaus | 64 | vastaus | **vakuutus**  |
| 39 | 0 | s ~ kse ~ ks | F | 39 | vastaus | vastaus | 64 | vastaus | **räjäytys**  |
| 39~41 | 0 | s ~ kse ~ ks ~ o ~ 0 | B | 39 | vastaus | uros | 71 | uros | **uros**  |
| 39~21 | 0 | s ~ kse ~ 0 | B | 39 | vastaus | vastaus | 64 | vastaus | **Kreus**  |
| 40 | t~d | s ~ te ~ ks | B | 40 | kalleus | kalleus | 65 | kalleus | **aakkosellisuus**  |
| 40 | t~d | s ~ te ~ ks | F | 40 | kalleus | kalleus | 65 | kalleus | **köyhyys**  |
| 41 | 0 | s ~ a ~ 0 | B | 41 | vieras | vieras | 66 | vieras | **patsas**  |
| 41 | 0 | s ~ ä ~ 0 | F | 41 | vieras | vieras | 66 | vieras | **äyräs** |
| 41 | 0 | s ~ e ~ 0 | B | 41 | vieras | vieras | 67 | kirves | **Aristoteles** |
| 41 | 0 | s ~ e ~ 0 | F | 41 | vieras | vieras | 67 | kirves | **kirves** |
| 41 | 0 | s ~ i ~ 0 | B | 41 | vieras | vieras | 68 | kauris | **ruumis** |
| 41 | 0 | s ~ i ~ 0 | F | 41 | vieras | vieras | 68 | kauris | **Dimitris** |
| 41 | k~kk | s ~ a ~ 0 | B | 41-A | vieras | vieras | 66 | vieras | **asukas**  |
| 41 | k~kk | s ~ ä ~ 0 | F | 41-A | vieras | vieras | 66 | vieras | **kärsäkäs** |
| 41 | p~pp | s ~ a ~ 0 | B | 41-B | vieras | vieras | 66 | vieras | **saapas**  |
| 41 | p~pp | s ~ ä ~ 0 | F | 41-B | vieras | vieras | 66 | vieras | **rypäs**  |
| 41 | t~tt | s ~ a ~ 0 | B | 41-C | vieras | vieras | 66 | vieras | **ratas**  |
| 41 | t~tt | s ~ e ~ 0 | B | 41-C | vieras | vieras | 66 | vieras | **Kortes**  |
| 41 | t~tt | s ~ i ~ 0 | B | 41-C | vieras | vieras | 66 | vieras | **Altis**  |
| 41 | t~tt | s ~ i ~ 0 | F | 41-C | vieras | vieras | 66 | vieras | **keltis**  |
| 41 | t~tt | s ~ u ~ 0 | B | 41-C | vieras | vieras | 66 | vieras | **vantus**  |
| 41 | t~tt | s ~ ä ~ 0 | F | 41-C | vieras | vieras | 66 | vieras | **mätäs**  |
| 41 | 0~k | s ~ a ~ 0 | B | 41-D | vieras | vieras | 66 | vieras | **varas**  |
| 41 | 0~k | s ~ e ~ 0 | F | 41-D | vieras | vieras | 66 | vieras | **ies**  |
| 41 | 0~k | s ~ i ~ 0 | B | 41-D | vieras | vieras | 66 | vieras | **ruis**  |
| 41 | v~p | s ~ a ~ 0 | B | 41-E | vieras | vieras | 66 | vieras | **varvas**  |
| 41 | v~p | s ~ ä ~ 0 | F | 41-E | vieras | vieras | 66 | vieras | **seiväs**  |
| 41 | d~t | s ~ a ~ 0 | B | 41-F | vieras | vieras | 66 | vieras | **tehdas**  |
| 41 | d~t | s ~ e ~ 0 | B | 41-F | vieras | vieras | 66 | vieras | **Luodes**  |
| 41 | d~t | s ~ e ~ 0 | F | 41-F | vieras | vieras | 66 | vieras | **Lähdes**  |
| 41 | d~t | s ~ a ~ 0 | B | 41-G | vieras | vieras | 66 | vieras | **kangas**  |
| 41 | d~t | s ~ ä ~ 0 | F | 41-G | vieras | vieras | 66 | vieras | **köngäs**  |
| 41 | m~p | s ~ a ~ 0 | B | 41-H | vieras | vieras | 66 | vieras | **hammas**  |
| 41 | l~t | s ~ a ~ 0 | B | 41-I | vieras | vieras | 66 | vieras | **allas**  |
| 41 | n~t | s ~ a ~ 0 | B | 41-J | vieras | vieras | 66 | vieras | **kinnas**  |
| 41 | n~t | s ~ ä ~ 0 | F | 41-J | vieras | vieras | 66 | vieras | **rynnäs**  |
| 41 | r~t | s ~ a ~ 0 | B | 41-K | vieras | vieras | 66 | vieras | **porras**  |
| 41~39 | 0 | s ~ a  ~ kse ~ 0 ~ ks |  a | 41 | vieras | koiras | 70 | koiras | **koiras**  |
| 42 | 0 | s ~ he ~ h | F | 42 | mies | mies | 72 | mies | **mies**  |
| 43 | 0 | t ~ e ~0 | B | 43 | ohut | ohut | 73 | airut | **olut**  |
| 43 | 0 | t ~ e ~ 0 | F | 43 | ohut | ohut | 73 | airut | **neitsyt**  |
| 43 | 0~k | t ~ e ~ 0 | B | 43-D | ohut | ohut | 73 | airut | **poiut**  |
| 43 | m~p | t ~ e ~ 0 | F | 43-H | ohut | ohut | 73 | airut | **immyt**  |
| 44 | 0 | t ~ ä ~ 0 | F | 44 | kevät | ? | 74 | kevät | **kevät**  |
| 44 | 0 | t ~ e ~ 0 | B | 44 | kevät | ? | 74 | kevät | **Kaaret**  |
| 44 | 0 | t ~ e ~ 0 | F | 44 | kevät | ? | 74 | kevät | **Hämet**  |
| 44 | d~t | t ~ e ~ 0 | F | 44-C | kevät | ? | 74 | kevät | **Kortet**  |
| 44 | 0~k | t ~ e ~ 0 | B | 44-D | kevät | ? | 74 | kevät | **Louet**  |
| 44 | d~t | t ~ e ~ 0 | B | 44-F | kevät | ? | 74 | kevät | **Ahdet**  |
| 44 | d~t | t ~ e ~ 0 | F | 44-F | kevät | ? | 74 | kevät | **Lähdet**  |
| 44 | g~k | t ~ e ~ 0 | F | 44-G | kevät | ? | 74 | kevät | **Inget**  |
| 44 | l~t | t ~ e ~ 0 | B | 44-I | kevät | ? | 74 | kevät | **Vuollet**  |
| 44 | r~t | t ~ e ~ 0 | F | 44-J | kevät | ? | 74 | kevät | **Lannet**  |
| 44 | r~t | t ~ e ~ 0 | F | 44-J | kevät | ? | 74 | kevät | **Rinnet**  |
| 44 | r~t | t ~ e ~ 0 | F | 44-K | kevät | ? | 74 | kevät | **Kaarret**  |
| 44 | r~t | t ~ e ~ 0 | F | 44-K | kevät | ? | 74 | kevät | **Viirret**  |
| 46 | t~n | t ~ nte ~ ns | B | 46 | tuhat | ? | 76 | tuhat | **vuosituhat**  |
| 47 | 0 | ut ~ ee ~ e |  a | 47 | kuollut | kuollut | 77 | kuollut | **aivokuollut**  |
| 47 | 0 | yt ~ ee ~ e | F | 47 | kuollut | kuollut | 77 | kuollut | **sivistynyt**  |
| 48 | 0 | 0 ~ e ~ t | B | 48 | hame | hame | 78 | hame | **aste** |
| 48 | 0 | 0 ~ e ~ t | F | 48 | hame | hame | 78 | hame | **piste** |
| 48 | k~kk | 0 ~ e ~ t | B | 48-A | hame | hame | 78 | hame | **kastike**  |
| 48 | k~kk | 0 ~ e ~ t | F | 48-A | hame | hame | 78 | hame | **lääke**  |
| 48 | p~pp | 0 ~ e ~ t | B | 48-B | hame | hame | 78 | hame | **ape**  |
| 48 | p~pp | 0 ~ e ~ t | F | 48-B | hame | hame | 78 | hame | **ripe**  |
| 48 | t~tt | 0 ~ e ~ t | B | 48-C | hame | hame | 78 | hame | **osoite**  |
| 48 | t~tt | 0 ~ e ~ t | F | 48-C | hame | hame | 78 | hame | **käsite**  |
| 48 | 0~k | 0 ~ e ~ t | B | 48-D | hame | hame | 78 | hame | **koe**  |
| 48 | 0~k | 0 ~ e ~ t | F | 48-D | hame | hame | 78 | hame | **pyyhe**  |
| 48 | v~p | 0 ~ e ~ t | B | 48-E | hame | hame | 78 | hame | **tarve**  |
| 48 | v~p | 0 ~ e ~ t | F | 48-E | hame | hame | 78 | hame | **viive**  |
| 48 | d~t | 0 ~ e ~ t | B | 48-F | hame | hame | 78 | hame | **luode**  |
| 48 | d~t | 0 ~ e ~ t | F | 48-F | hame | hame | 78 | hame | **kide**  |
| 48 | g~k | 0 ~ e ~ t | F | 48-G | hame | hame | 78 | hame | **Mielenge**  |
| 48 | m~p | 0 ~ e ~ t | B | 48-H | hame | hame | 78 | hame | **lumme**  |
| 48 | l~t | 0 ~ e ~ t | B | 48-I | hame | hame | 78 | hame | **vuolle**  |
| 48 | l~t | 0 ~ e ~ t | F | 48-I | hame | hame | 78 | hame | **mielle**  |
| 48 | l~n | 0 ~ e ~ t | B | 48-J | hame | hame | 78 | hame | **rakenne**  |
| 48 | l~n | 0 ~ e ~ t | F | 48-J | hame | hame | 78 | hame | **kiinne**  |
| 48 | r~t | 0 ~ e ~ t | B | 48-K | hame | hame | 78 | hame | **aarre** |
| 48 | r~t | 0 ~ e ~ t | F | 48-K | hame | hame | 78 | hame | **kierre** |
| 48 | j~k | 0 ~ e ~ t | B | 48-L | hame | hame | 78 | hame | **pohje**  |
| 48 | j~k | 0 ~ e ~ t | F | 48-L | hame | hame | 78 | hame | **hylje**  |
| 48 | 0 | 0 ~ i ~ t | B | 48 | hame | hame | 80 | ori | **ori** |
| 48 | 0 | 0 ~ u ~ t | B | 48 | hame | hame | 81 | kiiru | **kiiru** |
| 49 | 0 | 0 ~ e | B | 49 | askel | askel | 82 | askel | **askar** |
| 49 | 0 | 0 ~ e | F | 49 | askel | askel | 82 | askel | **kyynel**  |
| 49 | 0~k | 0 ~ e | F | 49-D | askel | askel | 82 | askel | **säen**  |
| 49 | v~p | 0 ~ e | B | 49-E | askel | askel | 82 | askel | **taival**  |
| 49 | d~t | 0 ~ e | B | 49-F | askel | askel | 82 | askel | **udar**  |
| 49 | g~k | 0 ~ e | B | 49-G | askel | askel | 82 | askel | **penger**  |
| 49 | m~p | 0 ~ e | B | 49-H | askel | askel | 82 | askel | **ommel**  |
| 49 | m~p | 0 ~ e | B | 49-H | askel | askel | 82 | askel | **Lommol**  |
| 49 | m~p | 0 ~ e | F | 49-H | askel | askel | 82 | askel | **vemmel**  |
| 49 | n~t | 0 ~ e | B | 49-J | askel | askel | 82 | askel | **piennar**  |
| 49 | n~t | 0 ~ e | B | 49-J | askel | askel | 82 | askel | **manner**  |
| 49 | n~t | 0 ~ e | B | 49-J | askel | askel | 82 | askel | **kannel**  |
| 49 | n~t | 0 ~ e | F | 49-J | askel | askel | 82 | askel | **kinner**  |
| 49 | 0~t | 0 ~ e | F | 49 | askel | askel | 82 | askel | **auer**  |
| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |

## Adjectives ##

| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |
|:---------------|:--------------|:------------|:------------|:-------|:----------|:------|:-----|:----------|:-----------------------------------|
| 1 | 0 | o | B | 1 | valo | valo | 1 | valo | ?**tummahko**  |
| 1 | 0 | u | B | 1 | valo | valo | 1 | valo | ?**valkaistu**  |
| 1 | 0 | y | F | 1 | valo | valo | 1 | valo | ?**häpäisty**  |
| 1 | 0 | ö | F | 1 | valo | valo | 1 | valo | **hölö**  |
| 1 | kk~k | o | B | 1-A | valo | valo | 1 | valo | **kolkko**  |
| 1 | kk~k | u | B | 1-A | valo | valo | 1 | valo | **virkku**  |
| 1 | kk~k | y | F | 1-A | valo | valo | 1 | valo | **säikky**  |
| 1 | kk~k | ö | F | 1-A | valo | valo | 1 | valo | **kökkö**  |
| 1 | pp~p | o | B | 1-B | valo | valo | 1 | valo | **suippo**  |
| 1 | pp~p | u | B | 1-B | valo | valo | 1 | valo | **ikäloppu**  |
| 1 | pp~p | ö | F | 1-B | valo | valo | 1 | valo | **lörppö**  |
| 1 | tt~t | o | B | 1-C | valo | valo | 1 | valo | **veltto**  |
| 1 | tt~t | u | B | 1-C | valo | valo | 1 | valo | ?**vimmattu**  |
| 1 | tt~t | y | F | 1-C | valo | valo | 1 | valo | ?**ylennetty**  |
| 1 | tt~t | ö | F | 1-C | valo | valo | 1 | valo | **kyyttö** |
| 1 | k~0~’ | o | B | 1-D | valo | valo | 1 | valo | **lako** |
| 1 | p~v | o | B | 1-E | valo | valo | 1 | valo | **kelpo**  |
| 1 | t~d | o | B | 1-F | valo | valo | 1 | valo | **mieto**  |
| 1 | t~d | u | B | 1-F | valo | valo | 1 | valo | ?**viipaloitu**  |
| 1 | t~d | y | F | 1-F | valo | valo | 1 | valo | ?**yksilöity**  |
| 1 | k~g | o | B | 1-G | valo | valo | 1 | valo | **lenko**  |
| 1 | t~l | o | B | 1-I | valo | valo | 1 | valo | **melto**  |
| 1 | t~l | u | B | 1-I | valo | valo | 1 | valo | ?**paranneltu**  |
| 1 | t~l | y | F | 1-I | valo | valo | 1 | valo | ?**vähätelty**  |
| 1 | t~n | o | B | 1-J | valo | valo | 1 | valo | **vento**  |
| 1 | t~n | u | B | 1-J | valo | valo | 1 | valo | ?**viraltapantu**  |
| 1 | t~r | o | B | 1-K | valo | valo | 1 | valo | **marto**  |
| 2 | 0 | o | B | 2 | palvelu | arvelu | 2 | arvelu | **kohelo**  |
| 2 | 0 | u | B | 2 | palvelu | arvelu | 2 | arvelu | ??**epäreilu**  |
| 2 | 0 | ö | F | 2 | palvelu | arvelu | 2 | arvelu | **löperö**  |
| 3 | 0 | o | B | 3 | valtio | autio | 3 | autio | **autio**  |
| 3 | 0 | ö | F | 3 | valtio | autio | 3 | autio | **riiviö**  |
| 4 | kk~k | o | B | 4-A | laatikko | (valo) | (2) | (arvelu) | **hupakko**  |
| 5 | 0 | i~e~0 | B | 5 | risti | risti | 4 | risti | **abnormi**  |
| 5 | 0 | i~e~0 | F | 5 | risti | risti | 4 | risti | **stydi**  |
| 5 | kk~k | i~e~0 | B | 5-A | risti | risti | 4 | risti | **opaakki**  |
| 5 | kk~k | i~e~0 | F | 5-A | risti | risti | 4 | risti | **pinkki**  |
| 5 | pp~p | i~e~0 | F | 5-B | risti | risti | 4 | risti | **sippi**  |
| 5 | tt~t | i~e~0 | B | 5-C | risti | risti | 4 | risti | **hurtti**  |
| 5 | tt~t | i~e~0 | F | 5-C | risti | risti | 4 | risti | **väärtti** |
| 5 | t~d | i~e~0 | B | 5-F | risti | risti | 4 | risti | **tuhti**  |
| 5 | t~d | i~e~0 | F | 5-F | risti | risti | 4 | risti | **rehti**  |
| 6 | 0 | i~e~0 | B | 6 | paperi | paperi | 5 | paperi | **abnormaali**  |
| 6 | 0 | i~e~0 | F | 6 | paperi | paperi | 5 | paperi | **öykkäri** |
| 8 | 0 | e | B | 8 | toope | toope | 9 | toope | **toope**  |
| 8 | 0 | e | F | 8 | nalle | nalle | 9 | nalle | **beige**  |
| 9 | 0 | a~o | B | 9 | kala | kala | 10 | kala | **aava**  |
| 9 | kk~k | a~o | B | 9-A | kala | kala | 10 | kala | **tarkka**  |
| 9 | tt~t | a~o | B | 9-C | kala | kala | 10 | kala | **matta**  |
| 9 | k~0 | a~o | B | 9-D | kala | kala | 10 | kala | **arka**  |
| 9 | k~0~’ | a~o | B | 9-D | kala | kala | 10 | kala | **raaka**  |
| 9 | p~v | a~o | B | 9-E | kala | kala | 10 | kala | **halpa**  |
| 9 | t~d | a~o | B | 9-F | kala | kala | 10 | kala | **ehta**  |
| 9 | p~m | a~o | B | 9-H | kala | kala | 10 | kala | **rampa** |
| 9 | t~n | a~o | B | 9-J | kala | kala | 10 | kala | ?**vihanta**  |
| 10 | 0 | a~0 | B | 10 | koira | koira | 11 | koira | **ruma**  |
| 10 | 0 | ä~0 | F | 10 | koira | koira | 11 | koira | **tyhmä**  |
| 10 | kk~k | a~0 | B | 10-A | koira | koira | 11 | koira | **hoikka**  |
| 10 | kk~k | ä~0 | F | 10-A | koira | koira | 11 | koira | **mykkä**  |
| 10 | pp~p | a~0 | B | 10-B | koira | koira | 11 | koira | **poppa**  |
| 10 | pp~p | ä~0 | F | 10-B | koira | koira | 11 | koira | **hömppä**  |
| 10 | k~0 | ä~0 | F | 10-D | koira | koira | 11 | koira | **märkä**  |
| 10 | p~v | a~0 | B | 10-E | koira | koira | 11 | koira | **voipa**  |
| 10 | p~v | ä~0 | F | 10-E | koira | koira | 11 | koira | **käypä**  |
| 10 | t~d | ä~0 | F | 10-F | koira | koira | 11 | koira | **mätä**  |
| 10 | k~g | a~0 | B | 10-G | koira | koira | 11 | koira | **sanka** |
| 10 | k~g | ä~0 | F | 10-G | koira | koira | 11 | koira | **vänkä**  |
| 10 | t~l | a~0 | B | 10-I | koira | koira | 11 | koira | **kulta**  |
| 10 | t~n | ä~0 | F | 10-J | koira | koira | 11 | koira | **läntä**  |
| 10 | t~r | a~0 | B | 10-K | koira | koira | 11 | koira | **turta**  |
| 10+ata | 0 | a~0 | B | 10 | koira | asema | 12 | matala | **matala**  |
| 10+ätä | 0 | ä~0 | B | 10 | koira | asema | 12 | matala | **terävä**  |
| 10+ata+? | 0 | a~0(~o) | B | 10 | koira | asema | 16 | kantaj|a |  |
| 11 | 0 | a~0~o | B | 11 | omena | apaja | 12 | matala | **hapera**  |
| 11 | 0 | ä~0~ö | F | 11 | omena | apaja | 12 | matala | **säkkärä**  |
| 12 | 0 | a~o | B | 12 | kulkija | kulkija | 14 | kulkija | **harmaja**  |
| 12 | 0 | ä~ö | F | 12 | kulkija | kulkija | 14 | kulkija | **höppänä**  |
| 12+? | 0 | a~o | B | 12 | kulkija | perun|a | 17 | perun|a |  |
| 12+? | 0 | a~o | B | 12 | kulkija | herttu|a | 20 | herttu|a |  |
| 13 | 0 | a~o | B | 13 | katiska | karahka | 15 | karahka | **latuska**  |
| 14 | kk~k | a~o | B | 14-A | solakka | (karahka) | (15) | (karahka) | **hailakka**  |
| 14 | kk~k | ä~ö| F | 14-A | solakka | (karahka) | (15) | (karahka) | **räväkkä**  |
| 15 | 0 | a(~o)~0 | B | 15 |  | korkea | 21 | korkea | **ainoa** (~ aino|o)  |
| 15 | 0 | ä(~e)~0 | F | 15 |  | korkea | 21 | korkea | **järeä** (~ järe|e)  |
| 15 | 0 | a(~e)~0 | B | 15 |  | korkea | 21 | korkea | **korkea**  |
| 16 | 0 | pi ~ ma ~ pa ~ p  | B | 16-H | vanhempi | suurempi | 22 | suurempi | **aiempi**  |
| 16 | 0 | pi ~ ma ~ pa ~ p  | F | 16-H | vanhempi | suurempi | 22 | suurempi | **lähempi**  |
| 17 | 0 | a~0 | B | 17 |  | vapaa | 23 | vapa|a | **vapaa**  |
| 18 | 0 | a~0 | B | 18 | peeaa | pii | 28  | peeaa | **peeaa**  |
| 18 | 0 | u~0 | B | 18 | maa | pii | 29 | puu | **muu**  |
| 18 | 0 | ä~0 | F | 18 | maa | pii | 29 | puu | **syypää**  |
| 26 | 0 | a ~ e ~ 0 | B | 26 | pieni | pieni | - | - | **suuri**  |
| 26 | 0 | ä ~ e ~ 0 | F | 26 | pieni | nuori | - | - | **pieni**  |
| 27 | 0 | si ~ te ~ s ~ t  | B | 27 | käsi | susi | 40 | susi | **uusi**  |
| 27 | 0 | si ~ te ~ s ~ t  | F | 27 | käsi | susi | 40 | susi | **täysi**  |
| 27+? | 0 | si ~ te ~ s ~ t  | B | 27 | käsi | susi | 41 | tosi | **tosi**  |
| 32 | 0 | 0 ~ e | F | 32 | sisar | ahven | 54 | sisar | **tyven**  |
| 33 | 0 | n ~ me ~ m | B | 33 | kytkin | uistin | 56 | uistin | **avoin**  |
| 34 | 0 | o (~ oi) | B | 34 | viaton | viaton | 57 | viaton | **alaston** (~ alastoin)  |
| 34 | p~pp | a | B | 34-B | viaton | viaton | 57 | viaton | **hapan**  |
| 34 | t~tt | o (~ oi) | B | 34-C | viaton | viaton | 57 | viaton | **viaton** (~ viatoin)  |
| 34 | t~tt | ö (~ öi) | F | 34-C | viaton | viaton | 57 | viaton | **kyvytön** (~ kyvytöin)  |
| 35 | m~p | n ~ mä ~ m | F | 35-H | lämmin | ? | 58 | lämmin | **lämmin**  |
| 36 | 0 | n ~ mpa ~ mma ~ mp ~ mm | B | 36 | sisin | sisin | 59 | pahin | **pahin**  |
| 36 | 0 | n ~ mpä ~ mmä ~ mp ~ mm | F | 36 | sisin | sisin | 59 | pahin | **sisin**  |
| 37 | 0 | n ~ mpa ~ mma ~ mp ~ mm | B | 37 | vasen | ? | 60 | vase|n | **vasen**  |
| 38 | 0 | nen ~ se ~ s  | B | 38 | nainen | nainen | 63 | hevonen | **aakkosellinen**  |
| 38 | 0 | nen ~ se ~ s  | F | 38 | nainen | nainen | 63 | hevonen | **kylmäjärkinen**  |
| 39 | 0 | s ~ kse ~ ks | F | 39 | vastaus | vastaus | 64 | vastaus | **symppis**  |
| 40 | 0 | s~de~te~ks | F | 40 | kalleus | kalleus | 65 | kalleus | **lähteisyys**  |
| 41 | 0 | s ~ a ~ 0 | B | 41 | vieras | vieras | 66 | vieras | **autuas**  |
| 41 | 0 | s ~ ä ~ 0 | F | 41 | vieras | vieras | 66 | vieras | **työläs**  |
| 41 | 0 | s ~ i ~ 0 | B | 41 | vieras | valmis | 69 | kaunis | **valmis**  |
| 41 | 0 | s ~ i ~ 0 | F | 41 | vieras | vieras | 69 | kirves | **tiivis** |
| 41 | k~kk | s ~ a ~ 0 | B | 41-A | vieras | vieras | 66 | vieras | **voimakas**  |
| 41 | k~kk | s ~ ä ~ 0 | F | 41-A | vieras | vieras | 66 | vieras | **tyylikäs**  |
| 41 | p~pp | s ~ a ~ 0 | B | 41-B | vieras | vieras | 66 | vieras | **reipas**  |
| 41 | t~tt | s ~ a ~ 0 | B | 41-C | vieras | vieras | 66 | vieras | **rietas**  |
| 41 | t~tt | s ~ i ~ 0 | B | 41-C | vieras | vieras | 66 | vieras | **raitis**  |
| 41 | d~t | s ~ a ~ 0 | B | 41-F | vieras | vieras | 66 | vieras | **hidas**  |
| 41 | r~t | s ~ a ~ 0 | B | 41-K | vieras | vieras | 66 | vieras | **harras**  |
| 41 | k~kk | s ~ ä ~ 0 | F | 41-A | vieras | iäkäs-av1 | 66 | kaunis  | (iäkäs)  |
| 41 | t~tt | s ~ i ~ 0 | B | 41-C | vieras | altis-avx | 69 | kaunis | (altis)  |
| 43 | 0 | t ~ e ~ 0 | B | 43 | ohut | ohut | 73 | airut | **ohut**  |
| 43 | 0 | t ~ e ~ 0 | F | 43 | ohut | ohut | 73 | airut | **ehyt**  |
| 47 | 0 | ut ~ ee ~ e | B | 47 | kuollut | kuollut | 77 | kuollut | **kulunut**  |
| 47 | 0 | yt ~ ee ~ e | F | 47 | kuollut | kuollut | 77 | kuollut | **ällistynyt**  |
| 48 | 0 | 0 ~ e ~ t | B | 48 | hame | hame | 78 | hame | **ahne**  |
| 48 | 0 | 0 ~ e ~ t | F | 48 | hame | hame | 78 | hame | **terve**  |
| 48 | d~t | 0 ~ e ~ t | B | 48-F | hame | hame | 78 | hame | **kade** |
| 48 | l~t | 0 ~ e ~ t | F | 48-I | hame | hame | 78 | hame | **helle** |
| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |

## Compounds ##

| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |
|:---------------|:--------------|:------------|:------------|:-------|:----------|:------|:-----|:----------|:-----------------------------------|
| 50 | - | – | - | 50 | isoäiti | - | 83 | pyhäpäivä | classify regular compounds under the last, inflecting part |
| 51 | - | - | - | 51 | nuoripari | - | 84 | omatunto | write out all forms of agreeing inflection compounds |
| - | - | - | - | – | – | – | 85 | harmaahanhi | combination of two above classes |
| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |

## Verbs ##

| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |
|:---------------|:--------------|:------------|:------------|:-------|:----------|:------|:-----|:----------|:-----------------------------------|
| 52 | 0 | u | B | 52 | sanoa | antautua | 1 | punoa | **kaunistua**  |
| 52 | 0 | o | B | 52 | sanoa | punoa | 1 | punoa | **punoa**  |
| 52 | 0 | y | F | 52 | sanoa | antautua | 1 | punoa | **ällistyä**  |
| 52 | 0 | ö | F | 52 | sanoa | punoa | 1 | punoa | **säilöä** |
| 52 | kk~k | o | B | 52-A | sanoa | antautua | 1 | punoa | **haukkoa** |
| 52 | k~0 | o | a | 52-D | sanoa | antautua | 1 | punoa | **velkoa** |
| 52 | kk~k | u | B | 52-A | sanoa | antautua | 1 | punoa | **nuokkua**  |
| 52 | kk~k | y | F | 52-A | sanoa | antautua | 1 | punoa | **kärkkyä**  |
| 52 | pp~p | o | B | 52-B | sanoa | antautua | 1 | punoa | **harppoa**  |
| 52 | pp~p | u | B | 52-B | sanoa | antautua | 1 | punoa | **loppua**  |
| 52 | pp~p | y | F | 52-B | sanoa | antautua | 1 | punoa | **leppyä**  |
| 52 | tt~t | o | B | 52-C | sanoa | antautua | 1 | punoa | **viittoa** |
| 52 | tt~t | u | B | 52-C | sanoa | antautua | 1 | punoa | **hermottua**  |
| 52 | tt~t | y | F | 52-C | sanoa | antautua | 1 | punoa | **kivettyä**  |
| 52 | k~’ | u | B | 52-D | sanoa | antautua | 1 | punoa | **maukua**  |
| 52 | k~0~’ | o | B | 52-D | sanoa | antautua | 1 | punoa | **takoa**  |
| 52 | k~0~’ | y | F | 52-D | sanoa | antautua | 1 | punoa | **mäikyä**  |
| 52 | p~v | o | B | 52-E | sanoa | ansilutua | 1 | punoa | **silpoa**  |
| 52 | p~v | u | B | 52-E | sanoa | antautua | 1 | punoa | **hiipua**  |
| 52 | p~v | y | F | 52-E | sanoa | antautua | 1 | punoa | **elpyä**  |
| 52 | t~d | o | B | 52-F | sanoa | ankieutua | 1 | punoa | **kietoa**  |
| 52 | t~d | u | B | 52-F | sanoa | antautua | 1 | punoa | **rohtua**  |
| 52 | t~d | y | F | 52-F | sanoa | antautua | 1 | punoa | **siliytyä**  |
| 52 | k~g | o | B | 52-G | sanoa | anpenutua | 1 | punoa | **penkoa**  |
| 52 | k~g | u | B | 52-G | sanoa | antautua | 1 | punoa | **vinkua**  |
| 52 | p~m | o | B | 52-H | sanoa | antemutua | 1 | punoa | **tempoa**  |
| 52 | p~m | u | B | 52-H | sanoa | antautua | 1 | punoa | **ampua**  |
| 52 | t~l | u | B | 52-I | sanoa | antautua | 1 | punoa | **humaltua**  |
| 52 | t~l | y | F | 52-I | sanoa | antautua | 1 | punoa | **mieltyä**  |
| 52 | t~n | u | B | 52-J | sanoa | antautua | 1 | punoa | **vakaantua**  |
| 52 | t~n | y | F | 52-J | sanoa | antautua | 1 | punoa | **tyhjentyä**  |
| 52 | t~r | o | B | 52-K | sanoa | antautua | 1 | punoa | **vartoa** |
| 52 | t~r | u | B | 52-K | sanoa | antautua | 1 | punoa | **pusertua**  |
| 52 | t~r | y | F | 52-K | sanoa | antautua | 1 | punoa | **pyörtyä**  |
| 53 | 0 | a | B | 53 | muistaa | aavistaa | 2 | muistaa | **mutristaa**  |
| 53 | 0 | ä | F | 53 | muistaa | aavistaa | 2 | muistaa | **kivistää**  |
| 53 | tt~t | a | B | 53-C | muistaa | aavistaa | 2 | muistaa | **vieroittaa**  |
| 53 | tt~t | ä | F | 53-C | muistaa | aavistaa | 2 | muistaa | **räpsyttää**  |
| 53 | k~0 | a | B | 53-D | muistaa | aavistaa | 2 | muistaa | **purkaa**  |
| 53 | t~d | a | B | 53-F | muistaa | aavistaa | 2 | muistaa | **mojahtaa**  |
| 53 | t~d | ä | F | 53-F | muistaa | aavistaa | 2 | muistaa | **yskähtää** |
| 53 | t~n | ä | F | 53-J | muistaa | aavistaa | 2 | muistaa | **kyntää**  |
| 53 | t~r | a | B | 53-K | muistaa | aavistaa | 2 | muistaa | **sortaa**  |
| 53+? | 0 | a | B | 53 | muistaa | hidastaa | 2 | muistaa | **hidastaa**  |
| 53+? | 0 | a | B | 53 | muistaa | loistaa | 2 | muistaa | **loistaa**  |
| 53+? | 0 | a | B | 53-C | muistaa | kirjoittaa | 2 | muistaa | **kirjoittaa**  |
| 53+? | 0 | ä | F | 53-C | muistaa | heittää | 2 | muistaa | **heittää**  |
| 53+? | 0 | ä | F | 53-C | muistaa | inttää | 2 | muistaa | **inttää**  |
| 53+? | 0 | a | B | 53 | muistaa | sulaa | 2 | muistaa | **sulaa**  |
| 53+? | 0 | a | B | 53-F | muistaa | hohtaa | 2 | muistaa | **hohtaa**  |
| 53+? | 0 | a | B | 53-F | muistaa | hujahtaa | 2 | muistaa | **hujahtaa**  |
| 53~54 | 0 | da | B | 53-F | muistaa | vuotaa | 2 | muistaa | **vuotaa**  |
| 54 | t~d | a | B | 54-F | huutaa | vuotaa | 3 | huutaa | **huutaa**  |
| 54 | t~d | ä | F | 54-F | huutaa | vuotaa | 3 | huutaa | **pyytää**  |
| 54 | t~l | a | B | 54-I | huutaa | vuotaa | 3 | huutaa | **sivaltaa**  |
| 54 | t~l | ä | F | 54-I | huutaa | vuotaa | 3 | huutaa | **viheltää**  |
| 54 | t~n | a | B | 54-J | huutaa | vuotaa | 3 | huutaa | **huonontaa**  |
| 54 | t~n | ä | F | 54-J | huutaa | vuotaa | 3 | huutaa | **hiventää**  |
| 54 | t~r | a | B | 54-K | huutaa | vuotaa | 3 | huutaa | **kuhertaa**  |
| 54 | t~r | ä | F | 54-K | huutaa | vuotaa | 3 | huutaa | **näpertää**  |
| 54+? | 0 | la | B | 54-I | huutaa | paleltaa | 3 | huutaa | **paleltaa**  |
| 54+? | 0 | la | B | 54-I | huutaa | sukeltaa | 5 | puoltaa | **sukeltaa**  |
| 54+? | 0 | na | B | 54-J | huutaa | juontaa | 8 | pahentaa | **juontaa**  |
| 54+? | 0 | na | B | 54-J | huutaa | pahentaa | 8 | pahentaa | **pahentaa**  |
| 54+? | 0 | ra | B | 54-K | huutaa | murtaa | 6 | murtaa | **murtaa**  |
| 54+? | 0 | ra | B | 54-K | huutaa | murtaa | 7 | sortaa | **sortaa**  |
| 55 | t~d | a | B | 55-F | soutaa | soutaa | 4 | soutaa | **soutaa**  |
| 55 | t~d | ä | F | 55-F | soutaa | soutaa | 4 | soutaa | **kiitää**  |
| 55 | t~l | ä | F | 55-I | soutaa | soutaa | 4 | soutaa | **yltää**  |
| 55 | t~n | ä | F | 55-J | soutaa | soutaa | 4 | soutaa | **entää**  |
| 56 | 0 | a | B | 56 | kaivaa |  | 9 | kaivaa | **kasvaa**  |
| 56 | kk~k | a | B | 56-A | kaivaa |  | 9 | kaivaa | **virkkaa**  |
| 56 | pp~p | a | B | 56-B | kaivaa |  | 9 | kaivaa | **tappaa**  |
| 56 | tt~t | a | B | 56-C | kaivaa |  | 9 | kaivaa | **auttaa**  |
| 56 | k~0 | a | B | 56-D | kaivaa |  | 9 | kaivaa | **jakaa**  |
| 56 | t~d | a | B | 56-F | kaivaa |  | 9 | kaivaa | **sataa**  |
| 56 | t~n | a | B | 56-J | kaivaa |  | 9 | kaivaa | **kantaa**  |
| 56+? | 0 | a | B | 56 | kaivaa | haastaa | 9 | kaivaa | **kaivaa**  |
| 56+? | 0 | a | B | 56 | kaivaa | haastaa | 10 | haastaa | **haastaa**  |
| 56+? | 0 | a | B | 56 | kaivaa | paistaa | 11 | paistaa | **paistaa**  |
| 56+? | 0 | a | B | 56 | kaivaa | palaa | 11 | paistaa | **palaa**  |
| 56+? | 0 | ka | B | 56 | kaivaa | virkkaa | 11 | paistaa | **virkkaa**  |
| 56+? | 0 | ta | B | 56-C | kaivaa | laittaa | 11 | paistaa | **laittaa**  |
| 56+? | 0 | ta | B | 56-C | kaivaa | taittaa | 11 | paistaa | **taittaa**  |
| 56+? | 0 | da | B | 56-F | kaivaa | kaihtaa | 11 | paistaa | **kaihtaa**  |
| 56+? | 0 | da | B | 56-F | kaivaa | paahtaa | 11 | paistaa | **paahtaa**  |
| 57 | t~d | a | B | 57-F | saartaa | ? | 12 | saartaa | **kaataa**  |
| 57 | t~r | a | B | 57-K | saartaa | ? | 12 | saartaa | **saartaa**  |
| 58 | 0 | a | B | 58 | laskea | laskea | 13 | laskea | **sotkea**  |
| 58 | 0 | ä | F | 58 | laskea | laskea | 13 | laskea | **kytkeä**  |
| 58 | k~0 | a | B | 58-D | laskea | laskea | 13 | laskea | **pukea**  |
| 58 | p~v | ä | F | 58-E | laskea | laskea | 13 | laskea | **rypeä**  |
| 58 | t~d | a | B | 58-F | laskea | laskea | 13 | laskea | **kutea**  |
| 58 | t~d | ä | F | 58-F | laskea | laskea | 13 | laskea | **päteä**  |
| 58 | k~g | a | B | 58-G | laskea | laskea | 13 | laskea | **tunkea**  |
| 58 | k~j | a | B | 58-L | laskea | laskea | 13 | laskea | **polkea**  |
| 58 | k~j | ä | F | 58-L | laskea | laskea | 13 | laskea | **särkeä**  |
| 58 | t~d | a | B | 58-F | laskea | laskea-av1 | 15 | potea | **potea**  |
| 59 | t~n | a | B | 59-J | tuntea | tuntea | 14 | tuntea | **tuntea**  |
| 60 | t~d | ä | F | 60-F | lähteä | lähteä | 16 | lähteä | **lähteä**  |
| 61 | 0 | a | B | 61 | sallia | sallia | 17 | sallia | **kosia**  |
| 61 | 0 | ä | F | 61 | sallia  | sallia | 17 | sallia | **ryskiä**  |
| 61 | kk~k | a | B | 61-A | sallia  | sallia | 17 | sallia | **kukkia**  |
| 61 | kk~k | ä | F | 61-A | sallia  | sallia | 17 | sallia | **sörkkiä**  |
| 61 | pp~p | a | B | 61-B | sallia  | sallia | 17 | sallia | **kalppia**  |
| 61 | pp~p | ä | F | 61-B | sallia  | sallia | 17 | sallia | **hyppiä**  |
| 61 | tt~t | a | B | 61-C | sallia  | sallia | 17 | sallia | **moittia**  |
| 61 | tt~t | ä | F | 61-C | sallia  | sallia | 17 | sallia | **miettiä**  |
| 61 | k~0 | a | B | 61-D | sallia  | sallia | 17 | sallia | **sukia**  |
| 61 | k~0 | ä | F | 61-D | sallia  | sallia | 17 | sallia | **määkiä**  |
| 61 | p~v | a | B | 61-E | sallia  | sallia | 17 | sallia | **raapia**  |
| 61 | p~v | ä | F | 61-E | sallia  | sallia | 17 | sallia | **riipiä**  |
| 61 | t~d | a | B | 61-F | sallia  | sallia | 17 | sallia | **ahnehtia**  |
| 61 | t~d | ä | F | 61-F | sallia  | sallia | 17 | sallia | **ehtiä**  |
| 61 | k~g | a | B | 61-G | sallia  | sallia | 17 | sallia | **onkia**  |
| 61 | k~g | ä | F | 61-G | sallia  | sallia | 17 | sallia | **mönkiä**  |
| 61 | p~m | ä | F | 61-H | sallia  | sallia | 17 | sallia | **tympiä**  |
| 61 | t~n | a | B | 61-J | sallia  | sallia | 17 | sallia | **kontia**  |
| 61 | k~j | ä | F | 61-L | sallia  | sallia | 17 | sallia | **hylkiä**  |
| 62 | 0 | a | B | 62 | voida | kanavoida | 18 | naida | **kopioida**  |
| 62 | 0 | ä | F | 62 | voida | kanavoida | 18 | naida | **öykkäröidä**  |
| 63 | 0 | a | B | 63 | saada | saada | 19 | saada | **saada**  |
| 63 | 0 | ä | F | 63 | saada |  saada | 20 | myydä | **myydä**  |
| 63 | 0 | ä | F | 63 | saada |  saada | 20 | myydä | **jäädä**  |
| 64 | 0 | uo | B | 64 | juoda | juoda | 21 | juoda | **tuoda**  |
| 64 | 0 | ie | F | 64 | juoda | juoda | 22 | viedä | **viedä**  |
| 64 | 0 | ye | F | 64 | juoda | juoda | 22 | viedä | **syödä**  |
| 65 | 0 | ä | F | 64 | käydä | käydä | 23 | käydä | **käydä**  |
| 66 | 0 | a | B | 66 | rohkaista | nuolaista | 24 | nuolaista | **marista**  |
| 66 | 0 | ä | F | 66 | rohkaista | nuolaista | 24 | nuolaista | **äristä**  |
| 66 | v~p | ä | F | 66-E | rohkaista | nuolaista | 24 | nuolaista | **häväistä**  |
| 66 | v~p | a | B | 66-E | rohkaista | nuolaista | 24 | nuolaista | **vavista**  |
| 66 | g~k | a | B | 66-G | rohkaista | nuolaista | 24 | nuolaista | **rangaista**  |
| 66+aja | 0 | ä | F | 66 | rohkaista | kihistä | 41 | kihistä | **kihistä**  |
| 66+? | 0 | ä | F | 66 | rohkaista | kitistä | 24 | nuolaista | **kitistä**  |
| 67 | 0 | la | B | 67 | tulla | tulla | 25 | tulla | **etuilla**  |
| 67 | 0 | lä | F | 67 | tulla | tulla | 25 | tulla | **äksyillä**  |
| 67 | 0 | la | B | 67 | tulla | kirjoitella | 29 | arvailla | **arvailla** ~ arvaella  |
| 67 | 0 | la | B | 67 | tulla | kirjoitella | 29 | arvailla | **lepäillä** ~ lepäellä  |
| 67 | 0 | ra | B | 67 | tulla | tulla | 26 | purra | **purra**  |
| 67 | 0 | nä | F | 67 | tulla | mennä | 27 | mennä | **mennä**  |
| 67 | k~kk | la | B | 67-A | tulla | tulla | 25 | tulla | **nakella**  |
| 67 | k~kk | lä | F | 67-A | tulla | tulla | 25 | tulla | **leikellä**  |
| 67 | p~pp | la | B | 67-B | tulla | tulla | 25 | tulla | **tapella**  |
| 67 | p~pp | lä | F | 67-B | tulla | tulla | 25 | tulla | **hypellä**  |
| 67 | t~tt | la | B | 67-C | tulla | tulla | 25 | tulla | **sulatella**  |
| 67 | t~tt | lä | F | 67-C | tulla | tulla | 25 | tulla | **herätellä**  |
| 67 | 0~k | la | B | 67-D | tulla | tulla | 25 | tulla | **jaella**  |
| 67 | d~t | la | B | 67-F | tulla | tulla | 25 | tulla | **tipahdella**  |
| 67 | d~t | lä | F | 67-F | tulla | tulla | 25 | tulla | **säpsähdellä**  |
| 67 | m~p | la | B | 67-H | tulla | tulla | 25 | tulla | **ommella**  |
| 67 | l~t | la | B | 67-I | tulla | tulla | 25 | tulla | **vaellella**  |
| 67 | l~t | lä | F | 67-I | tulla | tulla | 25 | tulla | **kiillellä**  |
| 67 | n~t | la | B | 67-J | tulla | tulla | 25 | tulla | **komennella**  |
| 67 | n~t | lä | F | 67-J | tulla | tulla | 25 | tulla | **käännellä**  |
| 67 | r~t | la | B | 67-K | tulla | tulla | 25 | tulla | **nakerrella**  |
| 67 | r~t | lä | F | 67-K | tulla | tulla | 25 | tulla | **kiherrellä**  |
| 67 | t~tt | la | B | 67-C | tulla | kirjoitella | 28 | katsella | **kirjoitella**  |
| 67 | 0 | olla ~ lie | B | 67 | tulla | poikkeava | 25 | tulla | **olla**  |
| 68 | 0 | a | B | 68 | tupakoida | haravoida | 30 | haravoida | **mellakoida**  |
| 68 | 0 | ä | F | 68 | tupakoida | haravoida | 30 | haravoida | **isännöidä**  |
| 69 | 0 | a | B | 69 | valita | valita | 31 | valita | **palkita**  |
| 69 | 0 | a | F | 69 | valita | valita | 31 | valita | **merkitä**  |
| 69 | d~t | a | B | - | - | poikkeava | - | - |  **kudita**  |
| 70 | 0 | a | B | 70 | juosta | poikkeava | 32 | juosta | **juosta**  |
| 70 | 0 | a | F | 70 | juosta | poikkeava | 32 | juosta | **piestä**  |
| 71 | 0 | ä | F | 71 | nähdä | poikkeava | 33 | nähdä | **nähdä**  |
| 72 | 0 | ea | B | 72 | vanheta | aleta | 34 | aleta | **karheta**  |
| 72 | 0 | eä | F | 72 | vanheta | aleta | 34 | aleta | **vähetä**  |
| 72 | k~kk | ea | B | 72-A | vanheta | aleta | 34 | aleta | **niuketa**  |
| 72 | k~kk | eä | F | 72-A | vanheta | aleta | 34 | aleta | **jyrketä**  |
| 72 | k~kk | oa | B | 72-A | vanheta | aleta | 34 | aleta | **heikota**  |
| 72 | p~pp | a | B | 72-B | vanheta | aleta | 34 | aleta | **hapata**  |
| 72 | p~pp | ea | B | 72-B | vanheta | aleta | 34 | aleta | **supeta**  |
| 72 | p~pp | eä | F | 72-B | vanheta | aleta | 34 | aleta | **tylpetä**  |
| 72 | p~pp | o | B | 72-B | vanheta | aleta | 34 | aleta | **helpota**  |
| 72 | t~tt | o | B | 72-C | vanheta | aleta | 34 | aleta | **loitota**  |
| 72 | 0~k | e | B | 72-D | vanheta | aleta | 34 | aleta | **erata**  |
| 72 | 0~k | ea | B | 72-D | vanheta | aleta | 34 | aleta | **toeta**  |
| 72 | 0~k | eä | F | 72-D | vanheta | aleta | 34 | aleta | **kyetä**  |
| 72 | 0~k | o | B | 72-D | vanheta | aleta | 34 | aleta | **ulota**  |
| 72 | v~p | ea | B | 72-E | vanheta | aleta | 34 | aleta | **kaveta**  |
| 72 | d~t | o | B | 72-F | vanheta | aleta | 34 | aleta | **leudota**  |
| 72 | d~t | eä | F | 72-F | vanheta | aleta | 34 | aleta | **pidetä**  |
| 72 | d~t | ä | F | 72-F | vanheta | aleta | 34 | aleta | **mädätä**  |
| 72 | m~p | eä | F | 72-H | vanheta | aleta | 34 | aleta | **lämmetä**  |
| 72 | n~t | eä | F | 72-I | vanheta | aleta | 34 | aleta | **kiinnetä**  |
| 72 | j~k | ea | B | 72-L | vanheta | aleta | 34 | aleta | **juljeta**  |
| 72 | j~k | eä | F | 72-L | vanheta | aleta | 34 | aleta | **iljetä**  |
| 73 | 0 | a | B | 73 | salata | salata | 35 | salata | **arvata**  |
| 73 | 0 | ä | F | 73 | salata | salata | 35 | salata | **ynnätä**  |
| 73 | k~kk | a | B | 73-A | salata | salata | 35 | salata | **morkata**  |
| 73 | k~kk | ä | F | 73-A | salata | salata | 35 | salata | **yökätä**  |
| 73 | p~pp | a | B | 73-B | salata | salata | 35 | salata | **siepata**  |
| 73 | p~pp | ä | F | 73-B | salata | salata | 35 | salata | **välpätä**  |
| 73 | t~tt | a | B | 73-C | salata | salata | 35 | salata | **luntata**  |
| 73 | t~tt | ä | F | 73-C | salata | salata | 35 | salata | **läntätä**  |
| 73 | 0~k | a | B | 73-D | salata | salata | 35 | salata | **liata**  |
| 73 | 0~k | ä | F | 73-D | salata | salata | 35 | salata | **hylätä**  |
| 73 | v~p | a | B | 73-E | salata | salata | 35 | salata | **kaivata**  |
| 73 | v~p | ä | F | 73-E | salata | salata | 35 | salata | **levätä**  |
| 73 | d~t | a | B | 73-F | salata | salata | 35 | salata | **jahdata**  |
| 73 | d~t | ä | F | 73-F | salata | salata | 35 | salata | **tähdätä**  |
| 73 | g~k | a | B | 73-G | salata | salata | 35 | salata | **vongata**  |
| 73 | g~k | ä | F | 73-G | salata | salata | 35 | salata | **vängätä**  |
| 73 | m~p | a | B | 73-H | salata | salata | 35 | salata | **temmata**  |
| 73 | l~t | a | B | 73-I | salata | salata | 35 | salata | **mullata**  |
| 73 | n~t | a | B | 73-J | salata | salata | 35 | salata | **suunnata**  |
| 73 | n~t | ä | F | 73-J | salata | salata | 35 | salata | **rynnätä**  |
| 73 | r~t | a | B | 73-K | salata | salata | 35 | salata | **virrata**  |
| 73 | k~j | ä | F | 73-M | salata | salata | 35 | salata | **hyljätä**  |
| 73 | b~bb | a | B | 73 | salata | salata | 35 | salata | **lobata**  |
| 73 | g~gg | a | B | 73 | salata | salata | 35 | salata | **digata**  |
| 73+? | 0 | a | B | 73 | salata | saneerata | 35 | salata | **saneerata**  |
| 73+j | 0 | a | B | 73 | salata | palata | 40 | palata | **palata**  |
| 74 | 0 | a | B | 74 | katketa | kohota | 38 |  kohota | **karhuta**  |
| 74 | 0 | ä | F | 74 | katketa | kohota | 38 |  kohota | **tähytä**  |
| 74 | k~kk | ea | B | 74-A | katketa | kohota | 38 |  kohota | **poiketa**  |
| 74 | k~kk | o | B | 74-A | katketa | kohota | 38 |  kohota | **kaikota**  |
| 74 | k~kk | u | B | 74-A | katketa | kohota | 38 |  kohota | **koukuta**  |
| 74 | p~pp | o | B | 74-B | katketa | kohota | 38 |  kohota | **upota**  |
| 74 | p~pp | u | B | 74-B | katketa | kohota | 38 |  kohota | **pulputa**  |
| 74 | t~tt | u | B | 74-C | katketa | kohota | 38 |  kohota | **luututa**  |
| 74 | t~tt | o | B | 74-C | katketa | kohota | 38 |  kohota | **lotota**  |
| 74 | 0~k | ea | B | 74-D | katketa | kohota | 38 |  kohota | **noeta**  |
| 74 | 0~k | eä | F | 74-D | katketa | kohota | 38 |  kohota | **keretä**  |
| 74 | 0~k | o | B | 74-D | katketa | kohota | 38 |  kohota | **seota**  |
| 74 | v~p | ea | B | 74-E | katketa | kohota | 38 |  kohota | **korveta**  |
| 74 | v~p | eä | F | 74-E | katketa | kohota | 38 |  kohota | **revetä**  |
| 74 | v~p | o | B | 74-E | katketa | kohota | 38 |  kohota | **kirvota**  |
| 74 | v~p | u | B | 74-E | katketa | kohota | 38 |  kohota | **kivuta**  |
| 74 | d~t | ea | B | 74-F | katketa | kohota | 38 |  kohota | **todeta**  |
| 74 | d~t | eä | F | 74-F | katketa | kohota | 38 |  kohota | **vyyhdetä**  |
| 74 | d~t | o | B | 74-F | katketa | kohota | 38 |  kohota | **kadota**  |
| 74 | d~t | u | B | 74-F | katketa | kohota | 38 |  kohota | **liiduta**  |
| 74 | g~k | ea | B | 74-G | katketa | kohota | 38 |  kohota | **tungeta**  |
| 74 | g~k | eä | F | 74-G | katketa | kohota | 38 |  kohota | **ängetä**  |
| 74 | g~k | o | B | 74-G | katketa | kohota | 38 |  kohota | **pingota**  |
| 74 | m~p | ea | B | 74-H | katketa | kohota | 38 |  kohota | **kammeta**  |
| 74 | m~p | o | B | 74-H | katketa | kohota | 38 |  kohota | **sammota**  |
| 74 | m~p | u | B | 74-H | katketa | kohota | 38 |  kohota | **kummuta**  |
| 74 | n~t | o | B | 74-H | katketa | kohota | 38 |  kohota | **innota**  |
| 74 | r~t | o | B | 74-I | katketa | kohota | 38 |  kohota | **irrota**  |
| 74 | g~k | ea | B | 74-G | katketa | kohota | 38 |  kohota | **haljeta**  |
| 74 | g~k | eä | F | 74-G | katketa | kohota | 38 |  kohota | **iljetä**  |
| 74+e | 0 | a | B | 74 | katketa | katketa | 36 | katketa | **katketa**  |
| 74+u | 0 | u | B | 74 | katketa | juoruta | 39 | haluta | **juoruta**  |
| 74+o | 0 | o | B | 74 | katketa | siivota | 38 | kohota | **siivota**  |
| 75 | 0 | a | B | 75 | selvitä | haluta | 39 | haluta | **lassota**  |
| 75 | 0 | ä | F | 75 | selvitä | haluta | 39 | haluta | **myrskytä**  |
| 75 | p~pp | y | F | 75-B | selvitä | haluta | 39 | haluta | **ryöpytä**  |
| 75 | t~tt | o | B | 75-C | selvitä | haluta | 39 | haluta | **peitota**  |
| 75 | 0~k | y | F | 75-D | selvitä | haluta | 39 | haluta | **keritä**  |
| 75 | d~t | o | B | 75-F | selvitä | haluta | 39 | haluta | **muodota**  |
| 75 | m~p | y | F | 75-G | selvitä | haluta | 39 | haluta | **lämmitä**  |
| 75 | l~t | o | B | 75-H | selvitä | haluta | 39 | haluta | **aallota**  |
| 75 | l~t | y | F | 75-I | selvitä | haluta | 39 | haluta | **hellitä**  |
| 75+i | 0 | ä | F | 75 | selvitä | haluta | 37 | selvitä | **selvitä**  |
| 76 | t~d | a | B | 76-F | taitaa |  | 43 | taitaa | **taitaa**  |
| 76 | t~d | ä | F | 76-F | taitaa |  | 43 | taitaa | **tietää**  |
| 77 | 0 | a | B | 77 | kumajaa | - | - | - | **vipajaa** |
| 77 | 0 | ä | F | 77 | kumajaa | - | - | - | **heläjää** |
| 78 | k~0 | a | B | 78 | kaikaa | kaikaa | - | - | **raikaa** |
| 78 | k~0 | ä | F | 78 | kaikaa | kaikaa | - | - | **ähkää** |
| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |

## Numerals ##

| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |
|:---------------|:--------------|:------------|:------------|:-------|:----------|:------|:-----|:----------|:-----------------------------------|
| 31 | 0 | ä | B | 31 | kaksi | ? | 51 | kaksi | **yksi**  |
| 31 | 0 | a | F | 31 | kaksi | ? | 51 | kaksi | **kaksi**  |
| 8~7 | 0 | a | B | - | - | - | - | - | **kolme**  |
| 10 | 0 | ä | F | 10 | koira | koira | 11 | koira | **neljä**  |
| 27 | 0 | ä | F | 27 | käsi | susi | 40 | susi | **viisi**  |
| 27 | 0 | a | B | 27 | käsi | susi | 40 | susi | **kuusi**  |
| ?? | 0 | ä | F | ??10 | koira | - | 62 | seitsemän | **seitsemän**  |
| ?? | 0 | a | B | ??10 | koira | - | - | - | **kahdeksan**  |
| ?? | 0 | ä | F | ??10 | koira | - | - | - | **yhdeksän**  |
| 32 | 0 | ä | F | 32 | sisar | ahven | 54 | sisar | **kymmenen**  |
| 9 | t~d | a | B | 9-F | kala | kala | 10 | kala | **sata**  |
| 46 | 0 | a | B | 46 | tuhat | ? | 76 | tuhat | **tuhat**  |
| 10 | 0 | a | B | 10 | koira | koira | 11 | koira | **miljoona**  |
| 5 | 0 | ia | F | 5 | risti | risti | 4 | risti | **miljardi**  |
| 38 | 0 | ä | F | 38 | nainen | nainen | 63 | hevonen | **ensimmäinen**  |
| 38 | 0 | a | B | 38 | nainen | nainen | 63 | hevonen | **toinen**  |
| 45 | 0 | a | B | 45 | kahdeksas | - | 75 | kahdeksas | **kolmas**  |
| 45 | 0 | ä | F | 45 | kahdeksas | - | 75 | kahdeksas | **neljäs**  |
| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |

## Pronouns ##

| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |
|:---------------|:--------------|:------------|:------------|:-------|:----------|:------|:-----|:----------|:-----------------------------------|
| 101 | - | nä ~ nu  | F | - | - | - | - | - | **minä**  |
| 101 | - | n ~ ne | F | - | - | - | - | - | **hän**  |
| 101 | - | e | F | - | - | - | - | - | **me**  |
| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |

## Acronyms ##

When the last letter determines inflection pattern:

| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |
|:---------------|:--------------|:------------|:------------|:-------|:----------|:------|:-----|:----------|:-----------------------------------|
| 1 | 0 | 0 ~ : | F | - | - | - | - | - | 1 |
| 2 | 0 | 0 ~ : | B | - | - | - | - | - | 2 |
| 3 | 0 | 0 ~ : | B | - | - | - | - | - | 3 |
| 4 | 0 | 0 ~ : | F | - | - | - | - | - | 4 |
| 5 | 0 | 0 ~ : | F | - | - | - | - | - | 5 |
| 6 | 0 | 0 ~ : | B | - | - | - | - | - | 6 |
| 7 | 0 | 0 ~ : | F | - | - | - | - | - | 7 |
| 8 | 0 | 0 ~ : | B | - | - | - | - | - | 8 |
| 9 | 0 | 0 ~ : | F | - | - | - | - | - | 9 |
| 0 | 0 | 0 ~ : | B | - | - | - | - | - | 0 |
| AA | 0 | 0 ~ : | B | - | - | - | - | - | A |
| EE | 0 | 0 ~ : | F | - | - | - | - | - | B |
| II | 0 | 0 ~ : | F | - | - | - | - | - | I |
| ÄKS | 0 | 0 ~ : | F | - | - | - | - | - | L |
| OO | 0 | 0 ~ : | B | - | - | - | - | - | O |
| UU | 0 | 0 ~ : | B | - | - | - | - | - | U |
| ZET | 0 | 0 ~ : | B | - | - | - | - | - | Z |
| YY | 0 | 0 ~ : | F | - | - | - | - | - | Y |
| ÄÄ | 0 | 0 ~ : | F | - | - | - | - | - | Ä |
| ÖÖ | 0 | 0 ~ : | F | - | - | - | - | - | Ö |
| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |

Word-by-word inflection patterns corresponding to the whole-word readings of the
acronyms are optionally used in conjunction with the letter-reading based ones.
The paradigms are currently only partly implemented.  In general they use class
names representing an example word, e.g. **gramma** for acronym ending in a word
that inflects like _gramma_.

| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |
|:---------------|:--------------|:------------|:------------|:-------|:----------|:------|:-----|:----------|:-----------------------------------|
| 1 | 0 | 0 ~ : | B | - | - | - | - | - | € (euro) |
| 2 | 0 | 0 ~ : | B | - | - | - | - | - | MpO (opisto) |
| 2 | 0 | 0 ~ : | F | - | - | - | - | - | OAJ (järjestö) |
| 3 | 0 | 0 ~ : | F | - | - | - | - | - | Gy (gray) |
| 5 | 0 | 0 ~ : | B | - | - | - | - | - | Ω (ohmi) |
| 5 | 0 | 0 ~ : | F | - | - | - | - | - | m (metri) |
| 6 | 0 | 0 ~ : | B | - | - | - | - | - | $ (dollari) |
| 6 | 0 | 0 ~ : | F | - | - | - | - | - | Wb (weber) |
| 7 | 0 | 0 ~ : | F | - | - | - | - | - | IL (lehti) |
| 8 | 0 | 0 ~ : | B | - | - | - | - | - | J (joule) |
| 9 | 0 | 0 ~ : | B | - | - | - | - | - | g (gramma) |
| 10 | 0 | 0 ~ : | B | - | - | - | - | - | £ (punta) |
| 10 | 0 | 0 ~ : | F | - | - | - | - | - | § (pykälä) |
| 12 | 0 | 0 ~ : | B | - | - | - | - | - | cd (kandela) |
| 13 | 0 | 0 ~ : | B | - | - | - | - | - | HYKS (sairaala) |
| 14 | 0 | 0 ~ : | B | - | - | - | - | - | rkl (lusikka) |
| 18 | 0 | 0 ~ : | B | - | - | - | - | - | ok (ookoo) |
| 27 | 0 | 0 ~ : | B | - | - | - | - | - | v (vuosi) |
| 39 | 0 | 0 ~ : | B | - | - | - | - | - | °C (celsius) |
| 39 | 0 | 0 ~ : | F | - | - | - | - | - | RAY (yhdistys) |
| 40 | 0 | 0 ~ : | B | - | - | - | - | - | KKO (oikeus) |
| 41 | 0 | 0 ~ : | B | - | - | - | - | - | yo (oppilas) |
| 45 | 0 | 0 ~ : | B | - | - | - | - | - | III (kolmas) |
| 45 | 0 | 0 ~ : | F | - | - | - | - | - | IV (neljäs) |
| 48 | 0 | 0 ~ : | B | - | - | - | - | - | bkt (tuote) |
| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |


## Particles ##

Particles in general do not inflect, but sometimes they are classified as having
possessives or clitics. It seems to be preferred in many sources to treat each
actually used possessive or clitic with its root as a separate lexeme.

| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |
|:---------------|:--------------|:------------|:------------|:-------|:----------|:------|:-----|:----------|:-----------------------------------|
| 99 | 0 | 0 | 0 | - | - | - | - | - | **vaan** |
| 99+C | 0 | 0 | B | - | - | - | - | - | **nopeasti** |
| 99+C | 0 | 0 | F | - | - | - | - | - | **tyhmästi** |
| 99+C+kA | 0 | 0 | B | - | - | - | - | - | **jonne** |
| 99+C+kA+s | 0 | 0 | B | - | - | - | - | - | **kuhun** |
| 99+C+kA+s | 0 | 0 | F | - | - | - | - | - | **miten** |
| 99+P+C | 0 | a | B | - | - | - | - | - | **kotona** |
| 99+P+C | 0 | ä | F | - | - | - | - | - | **ikinä** |
| 99+P+C | 0 | e | B | - | - | - | - | - | **alle** |
| 99+P+C | 0 | e | F | - | - | - | - | - | **ylle** |
| 99+P+C | 0 | i~e | B | - | - | - | - | - | **vuoksi** |
| 99+P+C | 0 | i~e | F | - | - | - | - | - | **lisäksi** |
| 99+P+C | 0 | n~0 | B | - | - | - | - | - | **valtaan** |
| 99+P+C | 0 | n~0 | F | - | - | - | - | - | **näkyviin** |
| 99+P+C | 0 | den~te | B | - | - | - | - | - | **nähden** |
| 99=P+C | 0 | an~0 | B | - | - | - | - | - | **ilkosillaan** |
| 99=P+C | 0 | än~0 | F | - | - | - | - | - | **hyvillään** |
| 99=P+C | 0 | en~0 | B | - | - | - | - | - | **istualleen** |
| 99=P+C | 0 | en~0 | F | - | - | - | - | - | **levälleen** |
| 99=Pnsa+C | 0 | nsa~0 | B | - | - | - | - | - | **aikansa** |
| 99=Pnsa+C | 0 | nsä~0 | F | - | - | - | - | - | ?**ylipäänsä** |
| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example | omorfi **Class name** example word |

## Obsoleted, archaic, collapsed and wrong classes ##

Mainly, the tables above ended up being a super set of existing classifications.
The following classes are however deprecated for:

1. not being unique (by oversight in original classification) or
1. all unique forms are sufficiently archaic or
1. the missing forms have been adapted from neighboring classes to standard
   language.

| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example |
|:---------------|:--------------|:------------|:------------|:-------|:----------|:------|:-----|:----------|
| 6 | 0 | i | B | 6 | paperi | banaali | 6 | banaali |
| 23+ta | t~d | i ~ e ~ 0 | B | 23-F | ovi | lovi | 34 | lahti |
| 23+tä | t~d | i ~ e ~ 0 | F | 23-F | risti | neiti | 34 | lahti |
| 24 | 0 | i ~ e ~ 0 | B | 24 | uni | huuli | - | - |
| 24 | 0 | i ~ e ~ 0 | F | 24 | uni | huuli | - | - |
| 25 | 0 | mi | F | 25 | toimi | tuomi | 37 | niemi |
| 25 | 0 | mi | B | 25 | toimi | tuomi | 36 | tuomi |
| 26 | 0 | i ~ e ~ 0 | B | 26 | pieni | pieni | - | - |
| 26 | 0 | i ~ e ~ 0 | F | 26 | pieni | nuori | - | - |
| - | - | - | – | – | – | – | 61 | muudan |
| 49 | 0 | 0 ~ e ~ t | B | 49 | askel | askel | 82 | askel |
| 49 | 0 | 0 ~ e ~ t | F | 49 | askel | askel | 82 | askel |
| 52+ta | t~d | u | B | 52-F | sanoa | antautua | 44 | antautua |
| 54+ta | 0 | na | B | 54-J | huutaa | pahentaa | 42 | rakentaa |
| - | - | - | – | – | – | – | 45 | kaata |
| **suffix set** | **gradation** | **stem(s)** | **harmony** | _Nssl_ | - example | _Jou_ | Nssk | - example |

The _nssk_ class 6 _banaali_ differs from class 5 _paperi_ only by saying that
plural genitive allomorphs _-eiden_, _-eitten_ are unlikely. This is no longer
accurate description, and all words in both classes are commonly using both
forms. More fine-grained probabilities are made in our systems using real corpus
training data per word form.

The _nssk_ class 34 for lahti has additional consnant stem singular essives and
partitivies _lahta_, _neittä_ that are most likely beyond contemporary use.

The _nssk_ classes 37 _niemi_, and 36 _tuomi_ differ from 35 _lumi_ by
probability of consonant and vowel stem variants of singular partitive and
plural genitive, this distinction is no longer recognisable in contemporary
language use.

The _nssk_ class 61 _muudan_ is now considered to be an adverb and its paradigm
defective (s.v. _muutama_ << analogically from genitive stem).

The classes 24 and 26 of _nssl_ are equals, except by ordering of the allomorphs
_-ien_ and _-ten_, our system does not make use of such a priori probability
information and I'm very doubtful that people classifying their words will make
good judgements on this case; the better information of probabilities of these
allomorphs per wordform can be acquired by simple unigram training.

The dual paradigm class 49 of _nssl_ contains words ending in e, which inflect
as words in class 48 instead. It is unclear if these words should be analysed
under their consonant stem variant or not.

The verb paradigms 42 _rakentaa_, 44 _antautua_ and 45 _kaata_ of _nssk_ are
obsoleted for the parts that differ from their regular counter parts.


