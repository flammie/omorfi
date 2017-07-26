---
layout: page
title: "Tagging possibilities"
category: data
date: 2016-02-08 18:23:58
---


# Introduction #

*This is a development documentation, includes rationale and annotation guideline for Finnish, kind of, if you are interested in how's and why's of omorfi's tag sets.*

This documentation describes all available data in the database that can be turned into analysis tags using e.g. python scripting. This is a superset of tags needed for applications we create, and standard or historical tag formats we support. To support a lot of applications there's a lot of data, some is linguistically relevant, some related to historical software, to one specific application, and so on. Each application user will decide which data to use and how to format the analyses, if data is lacking for what you would want to create, send a _bug report_.

The actual tag sets in the omorfi analysers are configurable using `configure` options, for details, use `--help` switch. Depending on versions, a number of formats are supported: ftb3.1 for FinnTreeBank standard, ftb1 for some other FinnTreeBank standard, apertium for apertium exports and giella for giellatekno exports. For apertium style analysis tags the exported lexc's are in the apertium-fin project in [github apertium-fin](https://github.com/flammie/apertium-fin). The [fin in giellatekno repository at Tromsø University](http://giellatekno.uit.no) will probably be most familiar to those who have learnt the tradtional style finite-state morphologies.

The data that is available for use in the analyses is stored in database that is currently a set of tsv files. Main database is just lemmas with inflectional class, optional data is collection of details added to individual word entries. The analyses that are coming from suffixes (or morphological processes) are stored in another bunch of databases, currently tsv files just as well.



# Analysis approaches #

There are few different ways to approach morphological analysis that affect both how the data is arranged and how it is serialised. When one form of word or certain suffix lacks information that is present in other words, i.e. the information is underdefined. E.g. if _foo_ could be analysed either as `A` form of word _foo_ or `B` form of word _foo_, it depends on the application whether to analyse it as one result `foo A-or-B`, or two results `foo A`, `foo B`. To support both approaches the data that can be used to define analysis strings in here may have duplicated lines, fields or entries, and it is up to tag set writer to discard, or duplicate, the data in the pre-processing or post-processing phase.

If the surface form for the analyses A and B are the same, the evidence for different analyses can come from different sources: analogy from another related word class or inflectional pattern, syntax, semantics, or history of Finnish grammars. We try to describe the problem cases here with examples.

# Word ID or Lemma #

In the analyses used with omorfi, the lemma systematically refers to root form of word as it is presented in original lexical data source. For data of Nykysuomen sanalista this means the word form you can use to look it up from Kielitoimiston sanakirja, i.e. the official dictionary. This is not a unique string since there are some words of different origins that share the same base form (or all forms).

It is possible to get multiple word entry references in one analysis because of compounding. Some analysis formats may choose to hide the compounding by making compounds appear like non-compound words.

For both derivations and compounding it is possible to reveal or hide the original formation in the analysis level, for example a compund _banaaninkuljetus_ is
composed of two words, _banaani_ and _kuljetus_, former being genitive and latter either a regular noun, or derived from verb _kuljettaa_. It depends largely on the application what information is needed, e.g. the potential analyses might have references to any of the word-forms {banaaninkuljetus, banaanin#kuljetus, banaani, kuljetus, kuljettaa}.

**The rationale** for prefering the forms found in the database is clear: with most systems you cannot encode endless amount of data in the actual analyser, so using the word's base form as a reference will be a way to query additional information. Most real-world applications will need this, on the contrary, having invented base forms only benefits the human readability of the analyses, which is at best quite contrived use case. The applications that can make use of proper base forms as reference: intelligent dictionaries, syntactic analysis, machine translation, information extraction, ... 

# POS and other lexical features #

Part of speech is a generic classification of a word in morphological analyser. There are different approaches to parts-of-speech depending on format, so there's a lot of data to support these analyses. There can be anything from 0 to dozen of these analyses, they are relate to the lexeme itself, the root morph, and typically an analyser will display them next to the word-form.

The _coarse_ POS analyses are drawn from inflectional data, this would consist three classes: **verbal**, **nominal** and **particle** (anything else). The verbs are identified by personal, temporal, modal and infinite inflection. The nominals are identified by numeral and case inflection. The others are, apart from being **the rest**, identified by defective or missing inflection.

These three classes are often divided to more classes. Some of these can be drawn from inflection or derivation, others are syntactic, semantic or based on traditions.

Somewhat morphologically we can do following quite traditional classification:

_Nominals_ consist of **nouns** (substantiivi), **adjectives**, **pronouns** and **numerals**. Nouns have the basic set of case affixes, possessives and clitics and can compound. Adjectives can have all suffixes that nouns, and also comparative derivations. Adjective possessives and adjective initial compounds are rare. _Adjectives that do not inflect are particles in the inflection classes_. Pronouns have limited set of cases, usually only singulars or plurals per word id. Pronouns do not compound, usually do not have possessives and so on. Pronouns are morphologically heterogeneous group. Numerals form rather peculiar compounds, but are otherwise do not have morphological features apart from nominal features. 

_Verbs_ are homogeneous and clear cut morphological group. Only real exception is the negation verb _ei_ with limited inflection. 

_Particles_ is very heterogeneous class of words, but morphologically there is little variation. **Adpositions** commonly have possessive suffixes, **adverbs** rarely, **interjections** can do whatever. Most of **conjunctions** do not have even clitics. Many of **adverbs** and **adpositions** are forms of current or historical nominals, this is why they have some inflections too. And **-sti** adverbs have an inflection pattern completely different from the rest. All of these little details can be used as tags in the analyser. Also: there are **pro** words thar are strictly speaking not pronouns, but pro-adverbs (siten) and pro-adjectives (sellainen), the pro feature in Finnish is quite independent of the part of speech.

Some classifications can replace or extend noun category with class of **proper** nouns, or names. Proper nouns do have full inflectional morphology exactly as other nouns, but work slightly differently in derivation and compounding. Some capitalised nouns may also lose capitalisation in derivation.


Numerals have functional subcategories for semantics. Commonly used is classes of **cardinals** and **ordinals**. Some debate that ordinal numerals are adjectives.

Pronouns are divided into semantic classes by use. The classifications available are fully copied from the VISK: **personal**, **demonstrative**, **interrogative**, **relative**, **quantifier**, **reflexive**, **reciprocal**, **indefinite**, **interrogative**. Indefinite is used differently in old and new grammars.

**Warning**: Some grammars use even more classes for semantics.

The shortened word-forms can be marked with **acronym** or **abbreviation** analyses. Acronyms generally are letter initialisms and inflected with a colon, abbreviations often end in full stop and cannot be inflected. Acronyms and abbreviations may also be analysed as a form of underlying read-out form.

Ad words are typically derived or inflected word forms with lexicalised meanings and defective inflection patterns; the apparent inflectional endings can be used as lexicalised tags. **Manner** adverbs (e.g. mainly **sti** derivation, but not all) have comparation and clitics, **locative** adverbs have partial locative cases, possessives and clitics, **temporal** adverbs have only clitics.  **Prolatives** (_teitse_) and similar (e.g. _yli_ ~ _ylitse_) may only have clitics as well.  Lots of inflected forms of ad words is further lexicalised into more ad words.  **Intensifying** ad words might not assume clitics at all.

Ad words are all morphologically particles. Syntactically, adpositions must have a complement or possessive suffix, usually a genitive, as in: _puun takana_,
_talon edessä_. Adverbs modify verbs as an adjunct, and it is imaginable that they do not relate to any other specific word in the clause, or even the verb. ad words that modify something beyond noun phrase, verb or _clause_, can be analysed as adadjectives, adadverbs (ada) etc

The adpositions are further sub-categorised along their syntactic behaviour, to prepositions and postposition. The prepositions appear in front of the adpositional phrase and postpositions in back. Many of the adpositions can appear in both.

Conjunctions are non-inflecting words that join syntactic structures together.  The conjunstions have two subcategories according the type of syntactic relation they make.  The conjunctions are divided into two classes depending on whether they act as **subordinating** or **co-ordinating** their respective syntactic units.

**Warning**: The terminology of conjunctions has changed in the VISK grammar, if you wish to use old systems, replace all but `COORD` with `SUBORD`.

Interjections are usually characterisations of speech acts, and may often consist of more or less arbitrary series of characters, sometimes onomatopoetic. Also minimal turns in dialogue, mumbling, swearing, and so on are interjections.


**References:**
  * [VISK > S > Sanaluokka](http://scripta.kotus.fi/cgi-bin/visktermit/visktermit.cgi?h_id=sCACBIDAI)
  * [VISK § 438](http://scripta.kotus.fi/visk/sisallys.php?p=438)
  * [§ 63 onwards](http://scripta.kotus.fi/visk/sisallys.php?p=63) explains morphological features of parts of speech.
  * [VISK § 98](http://scripta.kotus.fi/visk/sisallys.php?p=98)
  * [VISK § 101–104](http://scripta.kotus.fi/visk/sisallys.php?p=101)
  * [VISK § 678 on discriminating adverb and adposition](http://scripta.kotus.fi/visk/sisallys.php?p=678)
  * [VISK § 816](http://scripta.kotus.fi/visk/sisallys.php?p=816)
  * [VISK § 856](http://scripta.kotus.fi/visk/sisallys.php?p=856)


Note that currently these features must be serialised next to the lemma as analysis tags. To move them further away in finite-state automaton analyser you must use flag diacritic trickery, rules or post-processing.

It is also possible to use the classes which define the stem variations and suffix allomorphy as an analysis. The historical format for this is used in official dictionaries in form of <sup>number-letter</sup> pair. We have noticed that none of these classifications cover all stem variation and allomorphy we need.

## Examples of classifications ##

These examples are from the databases, extracted on February 2014. Dictionary word _talo_ has a POS class `NOUN` and new inflection class is `N_TALO`, kotus-tn is `1`. Dictionary word _ruma_ has a POS class `ADJECTIVE`, new inflection class is `A_RUMA` and kotus-tn is `10`. And the dictionary word _kutoa_ has POS class `VERB`, new inflection class `V_KIETOA`, kotus-tn and kotus-av is `52-F`. An analyser might just serialise these such as `talo+N`, `ruma+A` and `kietoa+V`.

The additional information is encoded to the words like this. For example a _proper_ noun of dictionary word _Joensuu_ will have data like POS `NOUN`, new inflection class of `N_PUU`, and kotus-tn of `18`, but additionally a list of _proper classifications_ `GEO,LAST`. An analyser might serialise this data as `Joensuu+PropN+Geo`. A conjunction with dictionary entry _jos_, would have POS of `PARTICLE`, and new inflection class of `PCLE_VAAN`, it didn't used to have kotus-tn but `99` has been conventional. The additional _particle classification_ states `CONJUNCTION|ADVERBIAL`. Maybe some analyser might serialise this all as `jos+CS`.

The examples used here with plus signs are actually from giellatekno-divvun standards. There are many others, using whitespace, brackets or more complex structures.

# Analysis of inflection: suffixes and their meanings #

The analyses of suffixes are mostly kept separated from the the classifications we talked of above, for practical purposes. For most analysers the visual representation does not have distinctions though. By default the suffixes’ analyses follow the word classification analyses in order, however, there are many cases where they are rearranged in some tagsets.

## Nominal inflection ##

Nominal parts of speech (and nominal derivations) have common nominal declination consisting more than 15 cases in singular and plural, combined with any possessive suffix, combined with any clitics. Total is some thousands of word forms per word. The nominal parts of speech include nouns, adjectives, numerals and pronouns, however their analyses can be changed independently. Some common deverbal derivations that may include nominal inflection include participles and few very productive derivations.

In current version of morphology the number and case are in same section and thus easily rearrangeable.

### Nominal inflection in numbers ###

Nominals inflect in number, to mark plurality of the word.  It is either **singular** or **plural**, or in some cases (e.g. comitatives, abbreviations) under-specified.

**Reference**:
  * [VISK § 79–80](http://scripta.kotus.fi/visk/sisallys.php?p=79)

### Nominal cases ###


Nominals have at least 15 cases: **nominative**, **genitive** / **accusative**, **partitive**, **inessive**, **elative**, **illative**, **adessive**, **ablative**, **allative**, **essive**, **translative**, **abessive**, **comitative**, **instructive** are the ones commonly found in text books, last three being rather marginal, and the marginal ones not given in textbooks are such as **prolative**, **distributive**, **temporal** etc. Some marginal cases can be considered adverb derivations more or less. Conversely, some adverbs may have case analyses. Common syntactic cases are usually marked in analyses, as are most common cases.

**Reference**:
  * [VISK § 81](http://scripta.kotus.fi/visk/sisallys.php?p=81)

### Possessive suffixes ###

Possessive ending indicates ownership and can attaches always after a case ending. There are six possible values from **singular** and **plural**, **first**, **second** and **third** person references, where third person form is always ambiguous over plurality. Some tagsets analyse third singulars and plurals separately and some together.

**Reference**:
  * [VISK § 95–97](http://scripta.kotus.fi/visk/sisallys.php?p=95)


### Allomorphy ###

Certain nominal cases have multiple surface forms, which some applications need to tell apart. This is especially useful for form selection in applications that _generate_ word-forms instead of analysing them. The variation can be used as tags. Variants for singular partitive are **a**, **ta**, singular illative **Vn**, **hVn**, **seen**, plural partitive **ita**, **ja**, **ia**, plural gentive **ien**, **jen**, **iden**, **itten**, **in** and plural illative **iin**, **ihin**, **isiin**.

### Examples of nominal suffixes ###

The fields in inflectional data now have combinations like `Nsg|Xnom` for singular nominative without affix, `Npl|Xall` alongside _i>lle_ for plural allative and `ND|Xcom` for underspecified comitative. These might be serialised in the word-forms _talo_, _taloille_, _taloine_ as `talo+N+Sg+Nom`, `talo+N+Pl+All` and `talo+N+Com`. Here the tag set designer has decided not to write anything in underdefined case; it could've been duplicated as two analyses `talo+N+Sg+Com`, `talo+N+Pl+Com`, if next software in pipeline was e.g. disambiguator, or explicitly stated as `talo+N+ND+Com`, if next software in pipeline was able to realise underspecified tags.

The possessives are in separate part of the implementation. There's no distinction between singular or plural third possessive, therefore `Opl3`, `Osg3` or `O3` may be serialised as needed, that is, a word-form _talonsa_ might only have analysis like `talo+N+Sg+Nom+Px3` or both analyses `talo+N+Sg+Nom+PxSg3`, `talo+N+Sg+Nom+PxPl3`.

The allomorphs are rarely seen in analyses, but they may have their use in maintaining bijective mapping in the analyser-generator pair.

## Adjectives ##

Adjectives are effectively inflected as nouns, with additional level of comparison forms before regular nominal inflection.

**Warning**: adjectives that do not inflect may not appear in this class. Adjectives that do not have comparatives may not appear in this class.

### Comparison derivations ###

Comparison has three levels that can be used as analyses. Some tag sets omit marking the positive form as analysis. Some descriptions consider comparative forms derivations. The comparative forms have full nominal inflection, but it would be unusual to have two comparison suffixes in one word-form.

**Reference**:
  * [VISK § 300](http://scripta.kotus.fi/visk/sisallys.php?p=300)

### Comparison examples ###

The derivation is currently in the affix system separately before regular inflection with empty suffix for positive, _mpi_ (with variations) for comparative and
_in_ (with variations) for superlatives. The derivation version is now `Dmpi` and comparative `Ccmp`. Surface form such as _rumempi_ will potentially have analyses like `ruma+A+Comp+Sg+Nom` or `ruma+A+Der/mpi+Sg+Nom`.

## Numerals ##

Numerals do not have any specific inflection different from other nominals.

**Warning**: Some configurations may allow nonsensical numeral combinations, e.g. descending-ascending loops.

**Reference**:
  * [VISK § 99](http://scripta.kotus.fi/visk/sisallys.php?p=99)

## Pronouns ##

Pronouns inflect mostly like nouns, but are also only nouns to have explicit phonemically distinct accusative markers. Many of pronouns have defective pattern, e.g. only singulars or plurals, or heteroclitical paradigms.

**Reference**:
  * [VISK § 100](http://scripta.kotus.fi/visk/sisallys.php?p=100)

### Case inflection specific to pronouns: Accusative ###

Some of the pronouns have **accusative** as separate case.

## Verb conjugation ##

Verb's conjugation includes voice (in Finnish grammars also verbal genus), tense (tempus), moods (modus), personal endings or negation marker and clitics. The infinite verb forms have more limited inflection, participles and some historical infinitives are practically derivations but may also be analysed either way. Verb conjugation has more duplicated and understated information than nominal declinatin and therefore the analysers will have greater variation, and the possibilities to serialise same explicit suffixes are larger.

**Reference**:
  * [VISK § 105](http://scripta.kotus.fi/visk/sisallys.php?p=105)

### Verbal genus / voice ###

Verb inflection has two categories for **active** and **passive** voice. For finite forms passive voice only appears without other personal suffix. Some forms may lack voice because it's unclear if it's underdefined or not at the moment.

**Reference**:
  * [VISK § 110 on passive](http://scripta.kotus.fi/visk/sisallys.php?p=110)

### Finite verbs' inflection ###

The finite inflection of verbs concerns actual verbal inflection in person, mood, tense.


#### Personal inflection ####

Personal ending of verb defines the seven possible values, six for the **singular** and **plural** groups of **first**, **second** and **third** person forms, and one specifically for passive. The passive personal form is encoded as **fourth person**, which had been the common practice in past systems and is accurate naming.

**Reference:**
  * [VISK § 106–107](http://scripta.kotus.fi/visk/sisallys.php?p=106)

#### Tempus or Modus ####

Verbs may inflect to mark up tense or mood, which is mutually exclusive. The generic passed time is **past** and generic non-past is **present**. Finite verb forms inflect to mark up moods. Mood can be included in analyses, even with unmarked **indicative**. Other moods are **imperative**, **potential** and **conditional**. It is possible to include archaic and marginal moods like **optative** and **eventive** too. Present and past tense appear only in indicative, so their combined tags may be collapsed to create systematic tagset with complementary distribution of forms and tags.

**References**:
  * [VISK § 112](http://scripta.kotus.fi/visk/sisallys.php?p=112)
  * [VISK § 111 on tenses and moods collectively](http://scripta.kotus.fi/visk/sisallys.php?p=111)
  * [VISK § 115–118](http://scripta.kotus.fi/visk/sisallys.php?p=115)


#### Examples of finite verb forms ####

The verb suffixes commonly combine few potential tags, e.g. first singular
suffix _n_ will have `Vact|Tind|Tpres|Psg1` that analyser might serialise word-form like _kudon_ as `kutoa+V+Act+Indv+Prs+Sg1` but another one might opt to squeeze duplicated information like this `kutoa+V+Pres+Sg1`. The passive forms contain similar duplicated data, like suffix _taan_ with `Vpss|Tind|Tpres|Ppe4`, again the possible serialised tags for _kudotaan_ range from `kutoa+V+Pss+Indv+Prs+Pe4` to `kutoa+V+Pass+Pres`.

### Infinite forms of verbs ###

Infinite verb forms are in principle nominal derivations from verb, included in morphology as inflection by long linguistic tradition. Especially notable is that verb form A infinitive with **lative** case marking is still considered the dictionary form of the verb.

#### Infinitives ####

There are 3 to 5 infinitives that can be used as analyses. In traditional grammars the infinitive forms were called I, II, III, IV and V infinitive, the modern grammar replaces the first three with **a**, **e and**ma**infinitive respectively. The IV infinitive, which has _-minen_ suffix marker, can also be analysed as derivation. The V infinitive can also be analysed as derivation.**

The short form of **A infinitive** is in **lative** case which is extinct from nominal conjugation. The long form of A infinitive is **translative**, and it requires possessive suffix.

For **E infinitive**, the possible cases are **inessive** and **instructive**, the possessive suffix is optional for both, but rare for instructive form.

For **MA infinitive** the possible cases are **abessive**, **adessive**, **elative**, **illative**, **inessive** and **instructive**, the possessive ending is very rare since it usually indicates agent participle instead.

The _-mAisillA_ derivation is theoretically already in adessive case  and therefore has no case inflection, the possessive endings are optional but common.

The _-minen_ derivation creates a noun root form, and has standard nominal inflection and the analyses are reused from there. It can be seen as infinitive in certain negated verb chains, this infinitive will only have **nominative** and **partitive** forms.

**References**:
  * [VISK § 120](http://scripta.kotus.fi/visk/sisallys.php?p=120)
  * [VISK § 119 for all infinite forms collectively](http://scripta.kotus.fi/visk/sisallys.php?p=119)

**Warning:** In some tagsets mA infinitive instructive as well as some other forms use special analysis tag unknown to contemprary linguistics in form of `+Man`, to accomodate this we also have custom tag available in few places of form `FTB3Man`.

#### Participles ####

There are 4 participle forms. Like infinitives, participles in traditional grammars were named I and II where **NUT** and **VA** are used in modern grammars.  The other participls are **agent** and **negation** participle. In some grammars the NUT and VA participles have been called past and present participles respectively, drawing parallels from other languages, and some tagsets follow this logic. The participle forms can also be analysed as past con negs. The participle forms can also be seen as derivations. In case separation between derivations and participles is made, the participles (and con negs) that participate in syntactic structures will only apply for singular and plural nominative forms.

**Warning:** Be aware that some traditional commercial software for Finnish morphology mistakenly analyse agent participles as MA infinitives which result in different taggings in some reference corpora you may see. To distinguish agent participle from MA infinitive, apart from semantics, agent participle often requires possessive suffix, and only rarely specifies agent via syntactic means or omit it.  Also, participles allow all cases whereas set of cases used with infinitives are limited.

**References**:
  * [VISK § 122](http://scripta.kotus.fi/visk/sisallys.php?p=122)
  * [VISK § 119 for all infinite forms collectively](http://scripta.kotus.fi/visk/sisallys.php?p=119).

#### Negated verb forms ####

Verbs have specific and non-specific forms going together with negation verb (which has partial inflection itself). These forms can be marked with a **con negative** analysis. The present con negative forms can be unique or ambiguous with imperative. The past con negative form is ambiguous with nut participle.

(Well, is negated infinite or finite really, who knows, the present conneg is same as one finite form and past conneg is same as one infinite form.)

**Reference**:
  * [VISK § 109](http://scripta.kotus.fi/visk/sisallys.php?p=109)


#### Examples of infinite verb form versions ####

The nut participle forms are notable examples since they can plausibly be analysed at least three ways, giving three duplicate strings for suffixes _nut_ and _neet_, that is `Dnut|Nsg|Xnom`, `Dnut|Npl|Xnom`; `Vact|Cnut|Nsg` , `Vact|Cnut|Npl`; `Vact|Tpast|NCon|NSg`, `Vact|Tpast|Ncon|Npl`. However, suffixes in form of _neille_ would only apply to `Dnut|Npl|Xall` since it cannot participate in conneg or participle constructions. The tag sets that do not use the distinctions will only serialise `Dnut` series and realise other possibilities later in the pipeline. Then for example word-form _kutonut_ could be analysed in three ambiguous possibilities like `kutoa+V+Der/nut+Sg+Nom`, `kutoa+V+Act+PrcPrs+Sg` and `kutoa+V+Act+Past+ConNeg+Sg`, or just one, e.g. `kutoa+NutPcp+Sg+Nom`.

## Enclitic discourse particles ##

Clitics are suffixes which can attach almost anywhere in the ends of word-forms, both verb forms and nominals. They also attach on end of other clitics, forming theoretically infinite chains.  In practice it is usual to see at most three in one word form. The clitics are **-han**, **-ko**, **-pa**, **-s**, **-ka**, **-kin**, **-kaan**. Two clitics have limited use: **-s** only appears in few verb forms and combined to other clitics and **-kA** only appears with few adverbs and negation verb.

**Reference**:
  * [VISK § 126–](http://scripta.kotus.fi/visk/sisallys.php?p=126)
  * [VISK § 131 on combinatorics](http://scripta.kotus.fi/visk/sisallys.php?p=131)

### Clitic examples ###

Clitics are rather straight-forward to serialise as analyses, they are unambiguous and there's simple connection to suffixes. The clitics stack so that's only complication. So for suffix _han_ with you have analysis `Qhan` and _ko_ you have `Qko` and their combination _kohan_ there's `Qhan|Qko` to serialise. For _talohan_, _taloko_ and _talokohan_, more or less will be analysed `talo+N+Sg+Nom+Foc/han`, `talo+N+Sg+Nom+Foc/ko` and `talo+N+Sg+Nom+Foc/ko+Foc/han` respectively.

## Non-inflecting parts of speech: particles ##

There are several, closed, parts of speech in omorfi that do not have any inflection and do not participate in derivation or compounding. The official grammar uses name particle for all of the non-inflecting words, here the syntactic and semantic division for conjunctions, interjections and the rest (named as particles here and in old grammars) has also been included. The analyses for all this comes from lexical data, and is described in the beginning of this page.

Some particles have partial inflection and transparent suffixes that may be analysed. Clitics are quite common. Possessives occasional.

Some particles have identifiable cases and derivations that can be written as analyses. They are currently treated as classifications for specific word.

### Particle examples ###



## Derivations ##

Derivations are suffixes that make new root from existing word and can be analysed. A derivation usually resets bunch of earlier analyses and occasionally is marked in analyses or not. It can also modify the lemma in some tagsets. The derivations are commonly identified by their markers though some have other names too. Some forms of analysers will disable all derivations.

  * [VISK § 155](http://scripta.kotus.fi/visk/sisallys.php?p=155)

### Derivation examples ###

For example common deverbal nominaliser _ja_ would have `Dja` and word form like _kutoja_ could be analysed with `kutoa+V+Der/ja+Sg+Nom`, many analysers will have specific requirements to rebuild new lemma forms for analyses and replay the derived analyses to reach `kutoja+N+Sg+Nom` immediately. The _preferable_ approach is often to insert this new word into database instead. There's a bunch of python code to pre-process forms like this but it is not very neat.

## Compounding ##

Compounding is productive morphological process in Finnish language. Typically any nominals can be joined to form ad hoc compounds as needed. There are many restrictions to the word forms allowed in compounds. The productive nominal compounds are always formed by chain of nominals in genitive, nominative or special compound form, followed by final nominal word holding the inflectional suffixes. The nominals may also be nominalised verb forms.

There are also less productive compounds, where initial parts of compound may have other forms than those listed above, these should be added to lexical data since they are typically lexicalised. There is also set of adjective initial compounds where inflection in standard Finnish is said to agree for all parts of compound, these cases are not many and becoming more rare in general use, so they should be listed in exceptions.

The compound words will have multiple word identifiers or lemmas, some tagsets will mangle these lemmas to look like other dictionary words while others point to original data base entries.

  * [VISK § 398](http://scripta.kotus.fi/visk/sisallys.php?p=398)

### Compounding examples ###

Compounding is created in two separate places, one for the compound suffixes and one for the optional hyphen part. The suffixes creating compounds are like regular singular nominatives and genitives. The compounding part can have analyses made from `Bc`  for regular compounds with optional hyphen and `B-` with compulsory hyphen. So combination of _talo_, _n_, compound boundary and _mies_ would have the _NOUN_, _Nsg_, _Xgen_, _Bc_ and _NOUN_, _Nsg_, _Xnom_ in that order for the parts, the easiest serialisation would be `talo+N+Sg+Gen#mies+N+Sg+Nom`, but many analysers will want to invent the word of final form `talonmies+N+Sg+Nom` instead. There's some slightly complex python code to implement this if needed.

## Guesses ##

Some analyses include indication that word does not have a dictionary based root form, but contains a root that is generated morphologically.
Other tagsets do not show guesses.

## Style, usage, special terminology or such ##

Many lexical sources seem to record notes of style or area of usage with the words. This kind of lexical data may be indicated in analyses.

## Other dictionary classifications ##

Some analysers use other dictionary classifications, e.g. one in official dictionary uses numbers and letters that can be included in these analyses. Also homonym number can be used to tell words with same lemma apart.

  * **References**: [a short introduction to inflection and paradigms of Finnish](http://scripta.kotus.fi/visk/sisallys.php?p=63)**

## Semantics ##

Some semantic tags can be turned on from configuration. These are collected in database on per lemma basis.

## Named entity classifications ##

Some proper noun classes can be turned on from configuration. These are collected in database on per lemma basis.

## Other analyses ##
