---
layout: default
title: "Tag formats"
category: data
date: 2016-02-08 18:23:58
---


# Different tag, analysis and output formats in omorfi

This document explains some correspondences of the analyses in different
formats. The linguistic backgrounds can be found in the [analysis 
possibilities](Tagging-possibilities) document. 

The formats are generated from common source in two different ways: _during
compilation_ to create easy-to-use, separate distributable automata, and
_during run-time_, which allows more freedom to tweak the analyses,
tokenisations, recasing, etc., but is tied to our APIs for corpus data
processing. [This
figure](https://github.com/flammie/omorfi/blob/master/doc/omorfi-tagchart.svg)
shows the interactions.

The core tagsets currently supported and backed up with automatic test suites
are: _omor_ and _ftb3.1_. The _omor_ tagset is semi-internal to omorfi, will
change between releases, and may be rewritten at any time. It is not _nice to
read_ for humans. FTB3.1 is governed by an external standard and thus will not
change between our releases.

The auxiliary formats used include: _apertium_ for RBMT with apertium software,
_giella_, for integration with _giellatekno / UiT / divvun_ infra, _vislcg3_
for integration with VISL CG3 software and TDT for Turku Dependency Treebank
compatibility.


## Main tagset table

| **FTB 3.1** | **omor** | **apertium** | **gtdivvun** | **Explanation** |
|:------------|:---------|:-------------|:-------------|:----------------|
| `<<<` | – | – | – | FTB3.1: Initial symbol |
| `>>>` | – | – | – | FTB3.1: Final symbol |
| `A` | `[POS=ADJECTIVE]` | `<adj>` | +Adj | Adjective |
| `Abbr` | `[SUBCAT=ABBREVIATION]` | – | `+Abbr` | Abbreviation |
| `Abe` | `[CASE=ABE]` | `<abe>` | +Abe | Abessive |
| `Abl` | `[CASE=ABL]` | `<abl>` | +Abl | Ablative |
| `Acc` | `[CASE=ACC]` | `<acc>` | +Acc | Accusative |
| `Act` | `[VOICE=ACT]` | `<actv>` | +Act | Active voice |
| `Ade` | `[CASE=ADE]` | `<ade>` | +Ade | Adessive |
| `Adp` | `[POS=ADPOSITION]` | – | – | Adposition |
| `Adv` | `[POS=ADVERB]` | `<adv>` | +Adv | Adverb |
| `AgPrc` | `[PCP=MA]` | `<agent>` | +AgPrc | Participle with suffix _ma_ |
| `All` | `[CASE=ALL]` | `<all>` | +All | Allative |
| `CC` | `[SUBCAT=COORD]` | `<cnjcoo>` | +CC | Coordinating conjunction |
| `Com` | `[CASE=COM]` | `<com>` | +Com | Comitative |
| `Comp` | `[CMP=CMP]` | `<comp>` | +Comp | Comparitive |
| `Cond` | `[MOOD=COND]` | `<cond>` | +Cond | Conditional |
| `ConNeg` | `[NEG=CON]` | `<conneg>` | +ConNeg | Con negative form of verb |
| `CS` | `[SUBCAT=ADVERBIAL]` | `<cnjadv>` | +CS | Adverbial conjunction |
| `Dem` | `[SUBCAT=DEMONSTRATIVE]` | `<dem>` | +Dem | Demonstrative |
| `Ela` | `[CASE=ELA]` | `<ela>` | +Ela | Elative |
| `Ess` | `[CASE=ESS]` | `<ess>` | +Ess | Essive |
| `Foc_hAn` | `[CLIT=HAN]` | `+han<enc>` | +Foc/han | Focus clitic with suffix _han_ |
| `Foc_kA` | `[CLIT=KA]` | `+ka<enc>` | +Foc/ka | Focus clitic with suffix _ka_ |
| `Foc_kAAn` | `[CLIT=KAAN]` | `+kaan<enc>` | +Foc/kaan | Focus clitic with suffix _kaan_ |
| `Foc_kin` | `[CLIT=KIN]` | `+kin<enc>` | +Foc/kin | Focus clitic with suffix _kin_ |
| `Foc_kO` | `[CLIT=KO]` | `<qst>` | +Qst | Question clitic |
| `Foc_pA` | `[CLIT=PA]` | `+pa<enc>` | +Foc/pa | Focus clitic with suffix _pa_ |
| `Foc_s` | `[CLIT=S]` | `+s<enc>` | +Foc/s | Focus clitic with suffix _s_ |
| `Gen` | `[CASE=GEN]` | `<gen>` | +Gen | Genitive |
| `Ill` | `[CASE=ILL]` | `<ill>` | +Ill | Illative |
| `Impv` | `[MOOD=IMPV]` | `<impv>` | +Imprt | Imperative mood|
| `Indef` | `[SUBCAT=INDEF]` | `<ind>` | +Ind | Indefinite |
| `Ine` | `[CASE=INE]` | `<ine>` | +Ine | Inessive |
| `Inf1` | `[INF=A]` | `<infa>` | +InfA | Infinitive with suffix _a_ |
| `Inf2` | `[INF=E]` | `<infe>` | +InfE | Infinitive with suffix _e_ |
| `Inf3` | `[INF=MA]` | `<infma>` | +InfMa | Infinitive with suffix _ma_ |
| `Inf5` | `[INF=MINEN]` | – | – | Infinitive with suffix _minen_ |
| `Ins` | `[CASE=INS]` | `<ins>` | +Ins | Instructive |
| `Interj` | `[SUBCAT=INTERJECTION]` | `<ij>` | +Interj | Interjection |
| `Interr` | `[SUBCAT=INTERROGATIVE]` | `<itg>` | +Interr | Interrogative |
| `Lat` | `[CASE=LAT]` | `<lat>` | +Lat | Lative |
| `Man` | – | – | – | FTB3.1: some instructives, adverb forms |
| `N` | `[POS=NOUN]` | `<n>` | `+N` | Noun |
| `Neg` | `[SUBCAT=NEG]` | `<neg>` | `+Neg` | Negation verb|
| `NegPrc` | `[PCP=NEG]` | `<pneg>` | `+NegPrc` | Participle with suffix _maton_ |
| `Nom` | `[CASE=NOM]` | `<nom>` | `+Nom` | Nominative |
| `Num` | `[POS=NUMERAL]` | `<num>` | `+Num` | Numeral |
| `Opt` | `[MOOD=OPT]` | – | – | Optative |
| `Ord` | `[SUBCAT=ORD]` | `<ord>` | `+Ord` | Ordinal |
| `Par` | `[CASE=PAR]` | `<par>` | `+Par` | Partitive |
| `Pass` | `[VOICE=PSS]` | `<pasv>` | `+Pass` | Passive voice |
| `Pe4` | `[PRS=PE4]` | `<impers>` | – | Impersonal |
| `Pers` | `[SUBCAT=PERSONAL]` | `<pers>` | `+Pers` | `ersonal |
| `Pl` | `[NUM=PL]` | `<pl>` | `+Pl` | Plural |
| `Pl1` | `[PRS=PL1]` | `<p1><pl>` | `+Pl1` | 1st plural |
| `Pl2` | `[PRS=PL2]` | `<p2><pl>` | `+Pl2` | 2nd plural |
| `Pl3` | `[PRS=PL3]` | `<p3><pl>` | `+Pl3` | 3rd plural |
| `Po` | `[SUBCAT=POSTPOSITION]` | `<post>` | `+Po` | Postposition |
| `Pos` | `[CMP=POS]` | `<pos>` | `+Pos` | Positive/neutral comparison |
| `Pot` | `[MOOD=POTN]` | `<pot>` | `+Pot` | Potential mood |
| `Pr` | `[SUBCAT=PREPOSITION]` | `<pr>` | `+Pr` | Preposition |
| `PrfPrc` | `[PCP=NUT]` | `<pp>` | `+PrfPrc` | Participle with suffix _nut_ |
| `Pron` | `[POS=PRONOUN]` | `<pron>` | `+Pron` | Pronoun |
| `Prop` | `[PROPER=PROPER]` | `<np>` | `+Prop+N` | Proper noun |
| `Prs` | `[TENSE=PRESENT]` | `<pres>` | `+Pres` | Non-past tense |
| `PrsPrc` | `[PCP=VA]` | `<pprs>` | `+PrsPrc` | Participle with suffix _va_ |
| `Pst` | `[TENSE=PAST]` | `<past>` | `+Past` | Past tense|
| `Punct` | `[POS=PUNCTUATION]` | – | – | Punctuation marks |
| `Px3` | `[POSS=3]` | `<px3sp>` | `+Px3` | 3rd singular/plural possessive |
| `PxPl1` | `[POSS=PL1]` | `<px1pl>` | `+PxPl1` | 1st plural possesive |
| `PxPl2` | `[POSS=PL2]` | `<px2pl>` | `+PxPl2` | 2nd plural possessive |
| `PxSg1` | `[POSS=SG1]` | `<px1sg>` | `+PxSg1` | 1st singular possessive |
| `PxSg2` | `[POSS=SG2]` | `<px2sg>` | `+PxSg2` | 2nd singular possessive |
| `Qnt` | `[SUBCAT=QUANTOR]` | – | `+Qu` | Quantifier |
| `Quote` | `[SUBCAT=QUOTATION]` | – | – | Quotation marks |
| `Refl` | `[SUBCAT=REFLEXIVE]` | `<ref>` | `+Refl` | reflexive |
| `Rel` | `[SUBCAT=RELATIVE]` | `<rel>` | `+Rel` | relative |
| `Sg` | `[NUM=SG]` | `<sg>` | `+Sg` | `singular` |
| `Sg1` | `[PERS=SG1]` | `<p1><sg>` | `+Sg1` | 1st singular |
| `Sg2` | `[PERS=SG2]` | `<p2><sg>` | `+Sg2` | 2nd singular |
| `Sg3` | `[PERS=SG3]` | `<p3><sg>` | `+Sg3` | 3rd singular |
| `Superl` | `[CMP=SUP]` | `<sup>` | `+Sup` | Superlative |
| `Tra` | `[CASE=TRA]` | `<tra>` | `+Tra` | Translative |
| `TrunCo` | `[COMPOUND_FORM=OMIT]` | – | – | Coordinated compound fragment |
| `(TruncPrefix)` | `[POSITION=PREFIX]` | – | – | Coordinated compound fragment left |
| `(TruncSuffix)` | `[POSITION=SUFFIX]` | – | – | Coordinated compound fragment right |
| `V` | `[POS=VERB]` | `<vblex>` | `+V` | Verb |
| – | `[WORD_ID= ]` | – | – | Omor: feature for lemma |
| – | `[SUBCAT=SPACE]` | – | – | Spaces (often not used as tokens) |
| – | `[SUBCAT=QUOTATION]` | `<lquot>`, `<rquot>` | – | Quotation marks |
| – | `[SUBCAT=BRACKET]` | – | – | Brackets and parentheses |
| – | `[SUBCAT=DASH]` | `<guio>` | – | Hyphens and dashes |
| – | `[SUBCAT=CURRENCY]` | – | – | Currency symbol |
| – | `[SUBCAT=MATH]` | - | – | Math symbol |
| – | `[SUBCAT=OPERATION]` | – | – | Operation symbol |
| – | `[SUBCAT=RELATION]` | – | – | Relation symbol |
| – | `[POSITION=INITIAL]` | – | `-` | Initial part of paired symbol |
| – | `[POSITION=FINAL]` | – | – | Final part of paired symbol |
| `#` | `[BOUNDARY=COMPOUND]` | `+` | `#` | Word boundary |
| – | `[COMPOUND_FORM=S]` | – | – | `Compositive` |
| – | `[DRV=MINEN]` | – | `+Der/minen` | Derivation with suffix _minen_ |
| – | `[DRV=MAISILLA]` | – | `+Der/maisilla` | Derivation with suffix _maisilla_ |
| – | `[DRV=NUT]` | – | `+Der/nut` | Derivation with suffix _nut_ |
| – | `[DRV=TU]` | – | `+Der/tu` | Derivation with suffix _tu_ |
| – | `[DRV=MA]` | – | `+Der/ma` | Derivation with suffix _ma_ |
| – | `[DRV=VA]` | – | `+Der/va` | Derivation with suffix _va_ |
| – | `[DRV=MATON]` | – | `+Der/maton` | Derivation with suffix _maton_ |
| – | `[DRV=INEN]` | – | `+Der/inen` | Derivation with suffix _inen_ |
| – | `[DRV=LAINEN]` | – | `+Der/lainen` | Derivation with suffix _lainen_ |
| – | `[DRV=TAR]` | – | `+Der/tar` | Derivation with suffix _tar_ |
| – | `[DRV=LLINEN]` | – | `+Der/llinen` | Derivation with suffix _llinen_ |
| – | `[DRV=TON]` | – | `+Der/ton` | Derivation with suffix _ton_ |
| – | `[DRV=TSE]` | – | `+Der/tse` | Derivation with suffix _tse_ |
| – | `[DRV=OI]` | – | `+Der/oi` | Derivation with suffix _oi_ |
| – | `[DRV=VS]` | – | `+Der/Vs` | Derivation with suffix _Vs_ |
| – | `[DRV=U]` | - | `+Der/u` | Derivation with suffix _u_ |
| – | `[DRV=TTAIN]` | – | `+Der/ttain` | Derivation with suffix _ttain_ |
| – | `[DRV=TTAA]` | – | `+Der/ttaa` | Derivation with suffix _ttaa_ |
| – | `[DRV=TATTAA]` | – | `+Der/tattaa` | Derivation with suffix _tattaa_ |
| – | `[DRV=TATUTTAA]` | – | `+Der/tatuttaa` | Derivation with suffix _tatuttaa_ |
| – | `[DRV=UUS]` | – | `+Der/uus` | Derivation with suffix _uus_ |
| – | `[DRV=S]` | – | `+Der/s` | Derivation with suffix _s_ |
| – | `[DRV=NUT]` | – | `+Der/nut` | Derivation with suffix _nut_ |
| – | `[DRV=TAVA]` | – | `+Der/tava` | Derivation with suffix _tava_ |
| – | `[STYLE=NONSTANDARD]` | – | `+Use/-Spell` | Non-standard spelling or form |
| – | `[STYLE=RARE]` | – | `+Use/` | Rare form or word |
| – | `[STYLE=DIALECTAL]` | – | `+Use/dial` | Dialectal form or word |
| – | `[STYLE=ARCHAIC]` | – | `+Use/arch` | Archaic form or word |
| – | `[GUESS=COMPOUND]` | - | – | Omor: root is dynamically compounded |
| – | `[GUESS=DERIVE]` | – | – | Omor: root is dynamically derived |

Some tags are only available for special applications with specific configure
options.

## Analysis for allomorph variation within morpheme

This is required to have bijective 1:1 mapping between surface strings and
analyses, for when generation needs to generate only one form or the generated
form needs to be fine-tuned. E.g.: _omenia_ ~ _omenoita_ are both `omena N Pl
Par` but some applications need to tell them apart.

> - `[ALLO=A]`
> - `[ALLO=TA]`
> - `[ALLO=HVN]`
> - `[ALLO=IA]`
> - `[ALLO=IDEN]`
> - `[ALLO=ITA]`
> - `[ALLO=ITTEN]`
> - `[ALLO=IEN]`
> - `[ALLO=IHIN]`
> - `[ALLO=IIN]`
> - `[ALLO=IN]`
> - `[ALLO=ISIIN]`
> - `[ALLO=IDEN]`
> - `[ALLO=JA]`
> - `[ALLO=JEN]`
> - `[ALLO=SEEN]`
> - `[ALLO=TEN]`
> - `[ALLO=VN]`
> - `[FILTER=NO_PROC]`

## Proper noun classification

More detailed proper noun classification to be used e.g. in Named Entity Recognition.
Can be enabled with `configure --enable-tagset=omor+propers`.

> - `[PROPER=FIRST]`
> - `[PROPER=GEO]`
> - `[PROPER=LAST]`
> - `[PROPER=MISC]`
> - `[PROPER=ORG]`
> - `[PROPER=PRODUCT]`
> - `[PROPER=EVENT]`
> - `[PROPER=MEDIA]`
> - `[PROPER=CULTGRP]`
> - `[PROPER=ARTWORK]`

## Semantics

Some semantic tags may be used in constraint grammars, etc.
Can be enabled with `configure --enable-tagset=omor+semantics`.

> - `[SEM=TITLE]`
> - `[SEM=ORG]`
> - `[SEM=EVENT]`
> - `[SEM=POLIT]`
> - `[SEM=MEDIA]`
> - `[SEM=GEO]`
> - `[SEM=COUNTRY]`
> - `[SEM=INHABITANT]`
> - `[SEM=LANGUAGE]`
> - `[SEM=MEASURE]`
> - `[SEM=CURRENCY]`
> - `[SEM=TIME]`
> - `[SEM=MALE]`
> - `[SEM=FEMALE]`

## Old dictionary classification

If you are interested in the paradigms as they are in the official dictionary,
an `omor` based tagset with KTN (paradigm) and KAV (gradation) codes can be
enabled with `configure --enable-tagset=omor+ktnkav`.

> - `[KTN=1]`
> - `[KTN=2]`
> - `[KTN=3]`
> - `[KTN=4]`
> - `[KTN=5]`
> - `[KTN=6]`
> - `[KTN=7]`
> - `[KTN=8]`
> - `[KTN=9]`
> - `[KTN=10]`
> - `[KTN=11]`
> - `[KTN=12]`
> - `[KTN=13]`
> - `[KTN=14]`
> - `[KTN=15]`
> - `[KTN=16]`
> - `[KTN=17]`
> - `[KTN=18]`
> - `[KTN=19]`
> - `[KTN=20]`
> - `[KTN=21]`
> - `[KTN=22]`
> - `[KTN=23]`
> - `[KTN=24]`
> - `[KTN=25]`
> - `[KTN=26]`
> - `[KTN=27]`
> - `[KTN=28]`
> - `[KTN=29]`
> - `[KTN=30]`
> - `[KTN=31]`
> - `[KTN=32]`
> - `[KTN=33]`
> - `[KTN=34]`
> - `[KTN=35]`
> - `[KTN=36]`
> - `[KTN=37]`
> - `[KTN=38]`
> - `[KTN=39]`
> - `[KTN=40]`
> - `[KTN=41]`
> - `[KTN=42]`
> - `[KTN=43]`
> - `[KTN=44]`
> - `[KTN=45]`
> - `[KTN=46]`
> - `[KTN=47]`
> - `[KTN=48]`
> - `[KTN=49]`
> - `[KTN=50]`
> - `[KTN=51]`
> - `[KTN=52]`
> - `[KTN=53]`
> - `[KTN=54]`
> - `[KTN=55]`
> - `[KTN=56]`
> - `[KTN=57]`
> - `[KTN=58]`
> - `[KTN=59]`
> - `[KTN=60]`
> - `[KTN=61]`
> - `[KTN=62]`
> - `[KTN=63]`
> - `[KTN=64]`
> - `[KTN=65]`
> - `[KTN=66]`
> - `[KTN=67]`
> - `[KTN=68]`
> - `[KTN=69]`
> - `[KTN=70]`
> - `[KTN=71]`
> - `[KTN=72]`
> - `[KTN=73]`
> - `[KTN=74]`
> - `[KTN=75]`
> - `[KTN=76]`
> - `[KTN=77]`
> - `[KTN=78]`
> - `[KAV=A]`
> - `[KAV=B]`
> - `[KAV=C]`
> - `[KAV=D]`
> - `[KAV=E]`
> - `[KAV=F]`
> - `[KAV=G]`
> - `[KAV=H]`
> - `[KAV=I]`
> - `[KAV=J]`
> - `[KAV=K]`
> - `[KAV=L]`
> - `[KAV=M]`
> - `[KAV=N]`
> - `[KAV=O]`
> - `[KAV=P]`
> - `[KAV=T]`

