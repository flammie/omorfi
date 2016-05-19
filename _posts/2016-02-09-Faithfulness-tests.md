---
layout: page
title: "Faithfulness tests"
category: stats
date: 2016-02-08 18:23:58
---


# Introduction

One of the secondary goals for analysers built from omorfi data is to act as
free/libre open source way to reproduce analyses in "gold" corpora for Finnish.
Since most of the gold corpora have been made with commercial tools unavailable
to us, without specs, we use automated tests to gauge how well can we even
reproduce their results prior to disambiguation. This page lists automatic test
results for those tests and discussion of whether we want to get 100 % recall
or maintain correct readings in omorfi. We also provide ways to get to 100 %
easily when needed

These are in ascending order of time, since I just `>>` them to the end of this
file. For sheet view, see [omorfi progress sheet in google
 docs](https://docs.google.com/spreadsheets/d/1eTpUhCz0SzpRl3VYjuzI7etFB2N2bPrzyTV43ebYf6k/edit?usp=sharing)

## FTB 3.1 background

The standard versions of omorfi in 2013–2015 use so-called FTB3.1 standard as a
format for analyses. In this format, morphological analyses are encoded as
string composed of a reconstructed lemma, followed by analysis tags separated
by spaces. This document describes the differences from the official FTB3
format, the full description of the format can be found from [FTB web
site](http://www.ling.helsinki.fi/kieliteknologia/tutkimus/treebank/index.shtml).

The analysis of the first sentence of declaration of human rights in FTB3 mode in omorfi stable version 20141014:

```
Kaikki kaikki Pron Qnt Nom Sg

ihmiset ihminen N Nom Pl

syntyvät syntyä PrsPrc Act Pos Nom Pl
syntyvät syntyä PrsPrc Act Pl
syntyvät syntyä V Prs Act Pl3

vapaina vapaa A Pos Ess Pl
vapaina vapaa N Ess Pl

ja ja Adv
ja ja CC

tasavertaisina tasa#vertainen A Pos Ess Pl
tasavertaisina tasa#vertainen N Ess Pl

arvoltaan arvo N Abl Sg Px3

ja ja Adv
ja ja CC

oikeuksiltaan oikeus N Abl Pl Px3

. . Abbr Nom Sg
. . Punct
```


## FTB3.1 tags

Extracted from our implementation:

```
 >>>,  A,  Abbr,  Abe,  Abl,  Acc,  Act,  Ade,  Adp,  Adv,  AgPrc,
  All,  CC,  CS,  Com,  Comp,  ConNeg,  Cond,  Dem,  Ela,  Ess,
  Foc_hAn,  Foc_kA,  Foc_kAAn,  Foc_kO,  Foc_kin,  Foc_pA,  Foc_s,
  Gen,  Ill,  Impv,  Indef,  Ine,  Inf1,  Inf2,  Inf3,  Inf5,  Ins,
  Interj,  Interr,  Lat,  Man,  N,  Neg,  Nom,  Num,  Par,  Pass,
  Pe4,  Pers,  Pl,  Pl1,  Pl2,  Pl3,  Po,  Pos,  Pot,  Pr,  PrfPrc,
  Pron,  Prop,  Prs,  PrsPrc,  Pst,  Px3,  PxPl1,  PxPl2,  PxSg1,
  PxSg2,  Qnt,  Quote,  Refl,  Rel,  Sg,  Sg1,  Sg2,  Sg3,  Superl,
  Tra,  TrunCo,  V
```

## FTB3.1 Known differences #

The releases of omorfi follow a regression test of 90 % _recall_ for FTB3.1
tags. The results for 20141014 are (Work in Progress):


The errors come mainly from following classes (the order of popularity per word-form):

  1. _-sti_ adverbs are not analysed as ` Man` forms of their etymologically relevant adjectives
  1. word-forms _oli_ or _olivat_ are not analysed as present tense. This  should be done in the post-processing stage of the morphological analysis as needed. (Affects some other verbs too but in very small quantities)
  1. _eikä_ is either negation verb or conjunction, not both
  1. compounds that lack the boundary data from boundaries.csv will lack it in analyses (fixable bug: just go and do it :-)
  1. foreign languages are not analysed; this should be handled by the text processor at a higher level
  1. mismatches from lexicalised vs. non-lexicalised (maybe fixable, consider if the lexicalisation is or isn't reasonable)

Examples with counts (totals etc. as in table above)

| **Count** | **Mismatch type** | FTB3 version | Omorfi readings |
|:----------|:------------------|:-------------|:----------------|
| 89588 | (1) Mismatched | erityisesti `erityinen Adv Pos Man` | erityisesti `erityisesti Adv` |
| 66198 | (2) Lemma matches | oli `olla V Prt Act Sg3` | oli `olla V Pst Act Sg3`  |
| 46144 | (3) Lemma matches | eikä `ei CC Neg Sg3 Foc_kA` | eikä `ei V Neg Sg3 Foc_kA` / `eikä CC` |
| 37119 | (4) Analysis matches | perustamissopimuksen `perustamis#sopimus  N Gen Sg` | perustamissopimuksen `perustaa#sopimus N Gen Sg` / `perustaminen#sopimus N Gen Sg` / `perustamissopimus N Gen Sg` |
| 33216 | (5) No results | the `the Forgn Art` | – |
| 21843 | (6) Mismatched | koskevia `koskeva A Pos Par Pl` | koskevia `koskea PrsPrc Act Pos Par Pl` |

These are the top word-forms of the known mismatches, and the single word-forms
alone attribute for 2.7 % of the errors

## Getting 100 % recall for ftb3

If you are doing some stuff that requires 100 % recall, please collect the
strings from `ftb3.1.conllx` (with awk oneliner or whatever), compile them with
`hfst-fst2strings` and `hfst-disjunct` that to your morphology `.hfst`. Omorfi
will likely not support FTB3's all quirks e.g. the ones mentioned above. If you
find mismatch that can be reasonably fixed, report a bug preferably with `git
format-patch` included or use a github pull request.

# Automated test runs

## 2014-04-01 FTB 3.1 (manual test)

| **Lines** | **Full matches** | **Lemma matches** | **Analyses match** | **Mismatched** | **No results** |
|:----------|:-----------------|:------------------|:-------------------|:---------------|:---------------|
| 76,369,439 | 68,000,879 | 2,604,581 | 1,552,020 | 1,206,452 | 3,005,507 |
| 100.0 % | 89.0 % | 3.4 % | 2.0 % | 1.6 % | 3.9 % |

Some of the mismatches documented further down can be deducted from the scores:
  * `Forgn`: 285625
  * `Adv Pos Man`: 517824
  * `oli V Prt Act`: 86011

| **Lines** | **Full matches** | **Lemma matches** | **Analyses match** | **Mismatched** | **No results** |
|:----------|:-----------------|:------------------|:-------------------|:---------------|:---------------|
| 75,479,979 | 68,000,879 | 2,298,104 | 1,552,020 | 812,694 | 2,816,282 |
| 100.0 % | 90.1 % | 3.0 % | 2.0 % | 1.1 % | 3.7 % |
## 2015-03-26 faithfulness

### ftb3.1

| Feature | Missed | Faithfulness | All |
|:--------|-------:|---------:|----:|
| Tokens  | 3926544 |  95.3900 % | 85103349 |
| Types   | 370203 | 77.8800 % | 1673245 |

#### 100 most common mismatches 

| Mismatch TYPE | Frequency | Word form | FTB 3.1 | (First reading) |
|:--------------|----------:|:----------|:--------|:----------------|
| NOANALMATCH: | 46144 | eikä | CC Neg Sg3 Foc_kA | ei V Neg Sg3 Foc_kA |
| NOANALMATCH: | 22307 | ollen | V Inf2 Act Man | olla V Inf2 Act Ins |
| NOANALMATCH: | 14938 | täällä | Adv Ade | täällä Adv Dem Ade |
| NOLEMMAMATCH: | 13472 | varmistamiseksi | varmistaminen | varmistaa V N Tra Sg |
| NOANALMATCH: | 13353 | muassa | Adv | muassa Adp Po |
| NOANALMATCH: | 11331 | ollut | V Prt Act ConNeg Sg | olla PrfPrc Pass Pl |
| NOMATCH: | 10475 | talous- | talous- TrunCo N Nom Sg | talous N TrunCo |
| NOANALMATCH: | 9858 | huomattavasti | PrsPrc Pass Pos Man | huomata PrsPrc Pass |
| NOANALMATCH: | 9528 | joitakin | Pron Qnt Par Pl | joka Pron Rel Par Pl Foc_kin |
| NOMATCH: | 8797 | pidettävä | pidettävä A Pos Nom Sg | pidetä PrsPrc Pass Pos Nom Sg |
| NOANALMATCH: | 8692 | toisaalta | Adv Abl | toisaalta Adv |
| NOANALMATCH: | 8671 | 1. | Abbr Nom Sg | 1. Num Digit Ord |
| NOANALMATCH: | 8514 | ii | Abbr | ii Interj |
| NOMATCH: | 8454 | jatkuvasti | jatkua PrsPrc Act Pos Man | jatkuvasti Adv |
| NOMATCH: | 7998 | päätökseen | päättö N Tra Sg Px3 | päätös N Ill Sg |
| NOANALMATCH: | 7981 | jonkin | Pron Qnt Gen Sg | jokin Pron Qnt Indef Gen Sg |
| NOANALMATCH: | 7885 | hyväksyi | V Prt Act Sg3 | hyväksyä V Pst Act Sg3 |
| NOMATCH: | 7527 | riittävästi | riittää PrsPrc Act Pos Man | riittävästi Adv |
| NOANALMATCH: | 7340 | eivätkä | CC Neg Pl3 Foc_kA | ei V Neg Pl3 Foc_kA |
| NOANALMATCH: | 7172 | valitettavasti | PrsPrc Pass Pos Man | valitettavasti Adv |
| NOMATCH: | 7046 | merkittävästi | merkittää PrsPrc Act Pos Man | merkittävästi Adv |
| NOANALMATCH: | 6944 | tällainen | A Pos Nom Sg | tällainen A Dem Pos Nom Sg |
| NOLEMMAMATCH: | 6858 | täytäntöönpanoa | täytäntöön#pano | täytäntöönpano N Par Sg |
| NOANALMATCH: | 6847 | totesi | V Prt Act Sg3 | todeta V Pst Act Sg3 |
| NOANALMATCH: | 6810 | julkaistu | PrfPrc Pass Pos Nom Sg | julkaista PrfPrc Pass Sg |
| NOANALMATCH: | 6710 | siellä | Adv Ade | siellä Adv Dem |
| NOANALMATCH: | 6624 | saakka | Adv | saakka Adp Po |
| NOANALMATCH: | 6365 | Toinen | N Prop Gen Sg | toinen N Nom Sg |
| NOLEMMAMATCH: | 6264 | eteenpäin | eteen#päin | eteenpäin Adv |
| NOANALMATCH: | 6125 | sanoi | V Prt Act Sg3 | sanoa V Pst Act Sg3 |
| NOANALMATCH: | 6032 | tällaisen | A Pos Gen Sg | tällainen A Dem Pos Gen Sg |
| NOLEMMAMATCH: | 5981 | täytäntöönpanon | täytäntöön#pano | täytäntöönpano N Gen Sg |
| NOANALMATCH: | 5800 | tällaista | A Pos Par Sg | tällainen A Dem Pos Par Sg |
| NOANALMATCH: | 5747 | ainoa | Pron Qnt Nom Sg | aino A Pos Par Sg |
| NOLEMMAMATCH: | 5684 | parempi | hyvä | parempi A Comp Comp Pos Nom Sg |
| NOMATCH: | 5593 | laadittava | laadittaa PrsPrc Act Pos Nom Sg | laatia PrsPrc Pass Pos Nom Sg |
| NOLEMMAMATCH: | 5534 | johdanto-osan | johdanto-osa | johdanto#osa N Gen Sg |
| NOLEMMAMATCH: | 5398 | nimenomaan | nimen#omaan | nimenomaan Adv |
| NOLEMMAMATCH: | 5387 | yksinomaan | yksin#omaan | yksinomaan Adv |
| NOANALMATCH: | 5296 | totta | A Pos Par Sg | toi Pron Dem Abe Sg |
| NOANALMATCH: | 5285 | antoi | V Prt Act Sg3 | antaa V Pst Act Sg3 |
| NOANALMATCH: | 5281 | jokin | Pron Qnt Nom Sg | jokin Pron Qnt Indef Nom Sg |
| NOLEMMAMATCH: | 5264 | täytäntöönpanosta | täytäntöön#pano | täytäntöönpano N Ela Sg |
| NOMATCH: | 5111 | -hinnasta | -hinta TrunCo N Ela Sg | TrunCo hinta N Ela Sg |
| NOANALMATCH: | 4937 | kaikkialla | Adv Ade | kaikkialla Adv Qnt Ade |
| NOMATCH: | 4835 | nähden | nähden Adp Po | nähdä V Inf2 Act Ins |
| NOMATCH: | 4833 | sisältävät | sisältävä A Pos Nom Pl | sisältää V Prs Act Pl3 |
| NOANALMATCH: | 4817 | tällaisten | A Pos Gen Pl | tällainen A Dem Pos Gen Pl |
| NOANALMATCH: | 4771 | tällaisia | A Pos Par Pl | tällainen A Dem Pos Par Pl |
| NORESULTS: | 4751 | à | à |  |
| NOLEMMAMATCH: | 4715 | periaatteiden | peri#aate | periaate N Gen Pl |
| NOANALMATCH: | 4680 | soveltamista | AgPrc Ela Pl | soveltaa AgPrc Pos Ela Pl |
| NOANALMATCH: | 4606 | laatima | AgPrc Nom Sg | laatia AgPrc |
| NOANALMATCH: | 4571 | teki | V Prt Act Sg3 | tehdä V Pst Act Sg3 |
| NOANALMATCH: | 4511 | pikemminkin | Adv Foc_kin | pikemmin Adp Po Comp Foc_kin |
| NORESULTS: | 4489 | p.m | p.m |  |
| NOMATCH: | 4455 | pyrittävä | pyrittää PrsPrc Act Pos Nom Sg | pyrkiä PrsPrc Pass Pos Nom Sg |
| NOANALMATCH: | 4447 | UNIONIN | N Prop Gen Sg | unioni N Gen Sg |
| NOANALMATCH: | 4441 | joidenkin | Pron Qnt Gen Pl | joka Pron Rel Gen Pl Foc_kin |
| NOANALMATCH: | 4435 | iii | Abbr | iii Num Roman Nom Sg |
| NOLEMMAMATCH: | 4422 | täytäntöönpano | täytäntöön#pano | täytäntöönpano N Nom Sg |
| NORESULTS: | 4409 | 31.12.2008 | 31.12.2008 |  |
| NOANALMATCH: | 4321 | Toisaalta | Adv Abl | toisaalta Adv |
| NOANALMATCH: | 4310 | jotakin | Pron Qnt Par Sg | joka Pron Rel Par Sg Foc_kin |
| NOLEMMAMATCH: | 4259 | periaatteita | peri#aate | periaate N Par Pl |
| NOANALMATCH: | 4247 | esitti | V Prt Act Sg3 | esittää V Pst Act Sg3 |
| NOLEMMAMATCH: | 4203 | periaatteessa | peri#aate | periaate N Ine Sg |
| NOANALMATCH: | 4147 | hyväksyttiin | V Prt Pass Pe4 | hyväksyä V Pst Pass Pe4 |
| NORESULTS: | 4039 | http | http |  |
| NOANALMATCH: | 3965 | tehtiin | V Prt Pass Pe4 | tehdä V Pst Pass Pe4 |
| NOLEMMAMATCH: | 3955 | periaatetta | peri#aate | periaate N Par Sg |
| NOANALMATCH: | 3876 | emmekä | CC Neg Pl1 Foc_kA | ei V Neg Pl1 Foc_kA |
| NOANALMATCH: | 3865 | todettiin | V Prt Pass Pe4 | todeta V Pst Pass Pe4 |
| NOLEMMAMATCH: | 3809 | periaatteen | peri#aate | periaate N Gen Sg |
| NOANALMATCH: | 3806 | jotkut | Pron Qnt Nom Pl | joku Pron Qnt Indef Nom Pl |
| NOANALMATCH: | 3804 | jotain | Pron Qnt Par Sg | jokin Pron Qnt Indef Par Sg |
| NOANALMATCH: | 3758 | päätti | V Prt Act Sg3 | päättää V Pst Act Sg3 |
| NOLEMMAMATCH: | 3716 | määrien | määri | määrä N Gen Pl |
| NOANALMATCH: | 3702 | kohden | Adv | kohden Adp Po |
| NOANALMATCH: | 3634 | Tällainen | A Pos Nom Sg | tällainen A Dem Pos Nom Sg |
| NOMATCH: | 3634 | päätöstä | päättö N Ela Sg | päätös N Par Sg |
| NOANALMATCH: | 3590 | sai | V Prt Act Sg3 | saada V Pst Act Sg3 |
| NOLEMMAMATCH: | 3519 | Voimassaolo | voimassa#olo | voimassaolo N Nom Sg |
| NOANALMATCH: | 3510 | A. | Abbr Nom Sg | A. N Prop Nom Sg |
| NOANALMATCH: | 3429 | tällaiset | A Pos Nom Pl | tällainen A Dem Pos Nom Pl |
| NOANALMATCH: | 3404 | Valitettavasti | PrsPrc Pass Pos Man | valitettavasti Adv |
| NOMATCH: | 3399 | tuettava | tuettaa PrsPrc Act Pos Nom Sg | tukea PrsPrc Pass Pos Nom Sg |
| NOMATCH: | 3382 | sanottava | sanottaa PrsPrc Act Pos Nom Sg | sanoa PrsPrc Pass Pos Nom Sg |
| NORESULTS: | 3382 | PIC | PIC |  |
| NORESULTS: | 3349 | A01 | A01 |  |
| NORESULTS: | 3319 | Ltd | ltd |  |
| NOMATCH: | 3297 | tutkimus- | tutkimus- TrunCo N Nom Sg | tutkimus N TrunCo |
| NOLEMMAMATCH: | 3233 | periaatteet | peri#aate | periaate N Nom Pl |
| NOANALMATCH: | 3220 | 2. | Abbr Nom Sg | 2. Num Digit Ord |
| NOANALMATCH: | 3214 | tuli | V Prt Act Sg3 | tuli N Nom Sg |
| NOLEMMAMATCH: | 3172 | periaate | peri#aate | periaate N Nom Sg |
| NOANALMATCH: | 3131 | asti | Adv | asti Adp Po |
| NOANALMATCH: | 3115 | otettiin | V Prt Pass Pe4 | ottaa V Pst Pass Pe4 |
| NOLEMMAMATCH: | 3103 | sosiaalikomitean | sosiaali#komitea | sosiaali-#komitea N Gen Sg |
| NORESULTS: | 3101 | L02 | L02 |  |

## 2015-09-04 faithfulness

### ftb3.1

| Feature | Missed | Faithfulness | All |
|:--------|-------:|---------:|----:|
| Tokens  | 5722629 |  93.2800 % | 85103349 |
| Types   | 370130 | 77.8800 % | 1673245 |

#### 100 most common mismatches 

| Mismatch TYPE | Frequency | Word form | FTB 3.1 | (First reading) |
| NOANALMATCH: | 1796700 | `|` | Punct | `|` Part |
| NOANALMATCH: | 46144 | eikä | CC Neg Sg3 Foc_kA | ei V Neg Sg3 Foc_kA |
| NOANALMATCH: | 22307 | ollen | V Inf2 Act Man | olla V Inf2 Act Ins |
| NOANALMATCH: | 14938 | täällä | Adv Ade | täällä Adv Dem Ade |
| NOLEMMAMATCH: | 13472 | varmistamiseksi | varmistaminen | varmistaa V N Tra Sg |
| NOANALMATCH: | 13353 | muassa | Adv | muassa Adp Po |
| NOANALMATCH: | 11331 | ollut | V Prt Act ConNeg Sg | olla PrfPrc Pass Pl |
| NOMATCH: | 10475 | talous- | talous- TrunCo N Nom Sg | talous N TrunCo |
| NOANALMATCH: | 9858 | huomattavasti | PrsPrc Pass Pos Man | huomata PrsPrc Pass |
| NOANALMATCH: | 9528 | joitakin | Pron Qnt Par Pl | joka Pron Rel Par Pl Foc_kin |
| NOMATCH: | 8797 | pidettävä | pidettävä A Pos Nom Sg | pidetä PrsPrc Pass Pos Nom Sg |
| NOANALMATCH: | 8692 | toisaalta | Adv Abl | toisaalta Adv |
| NOANALMATCH: | 8671 | 1. | Abbr Nom Sg | 1. Num Digit Ord |
| NOANALMATCH: | 8514 | ii | Abbr | ii Interj |
| NOANALMATCH: | 8454 | jatkuvasti | PrsPrc Act Pos Man | jatkua PrsPrc Act Pos |
| NOMATCH: | 7998 | päätökseen | päättö N Tra Sg Px3 | päätös N Ill Sg |
| NOANALMATCH: | 7981 | jonkin | Pron Qnt Gen Sg | jokin Pron Qnt Indef Gen Sg |
| NOANALMATCH: | 7885 | hyväksyi | V Prt Act Sg3 | hyväksyä V Pst Act Sg3 |
| NOANALMATCH: | 7527 | riittävästi | PrsPrc Act Pos Man | riittävästi Adv |
| NOANALMATCH: | 7340 | eivätkä | CC Neg Pl3 Foc_kA | ei V Neg Pl3 Foc_kA |
| NOANALMATCH: | 7172 | valitettavasti | PrsPrc Pass Pos Man | valitettavasti Adv |
| NOANALMATCH: | 7046 | merkittävästi | PrsPrc Act Pos Man | merkittävästi Adv |
| NOANALMATCH: | 6944 | tällainen | A Pos Nom Sg | tällainen A Dem Pos Nom Sg |
| NOLEMMAMATCH: | 6858 | täytäntöönpanoa | täytäntöön#pano | täytäntöönpano N Par Sg |
| NOANALMATCH: | 6847 | totesi | V Prt Act Sg3 | todeta V Pst Act Sg3 |
| NOANALMATCH: | 6810 | julkaistu | PrfPrc Pass Pos Nom Sg | julkaista PrfPrc Pass Sg |
| NOANALMATCH: | 6710 | siellä | Adv Ade | siellä Adv Dem |
| NOANALMATCH: | 6624 | saakka | Adv | saakka Adp Po |
| NOANALMATCH: | 6365 | Toinen | N Prop Gen Sg | toinen N Nom Sg |
| NOLEMMAMATCH: | 6264 | eteenpäin | eteen#päin | eteenpäin Adv |
| NOANALMATCH: | 6125 | sanoi | V Prt Act Sg3 | sanoa V Pst Act Sg3 |
| NOANALMATCH: | 6032 | tällaisen | A Pos Gen Sg | tällainen A Dem Pos Gen Sg |
| NOLEMMAMATCH: | 5981 | täytäntöönpanon | täytäntöön#pano | täytäntöönpano N Gen Sg |
| NOANALMATCH: | 5800 | tällaista | A Pos Par Sg | tällainen A Dem Pos Par Sg |
| NOANALMATCH: | 5747 | ainoa | Pron Qnt Nom Sg | aino A Pos Par Sg |
| NOLEMMAMATCH: | 5684 | parempi | hyvä | parempi A Comp Pos Nom Sg |
| NOMATCH: | 5593 | laadittava | laadittaa PrsPrc Act Pos Nom Sg | laatia PrsPrc Pass Pos Nom Sg |
| NOLEMMAMATCH: | 5534 | johdanto-osan | johdanto-osa | johdanto#osa N Gen Sg |
| NOLEMMAMATCH: | 5398 | nimenomaan | nimen#omaan | nimenomaan Adv |
| NOLEMMAMATCH: | 5387 | yksinomaan | yksin#omaan | yksinomaan Adv |
| NOANALMATCH: | 5296 | totta | A Pos Par Sg | toi Pron Dem Abe Sg |
| NOANALMATCH: | 5285 | antoi | V Prt Act Sg3 | antaa V Pst Act Sg3 |
| NOANALMATCH: | 5281 | jokin | Pron Qnt Nom Sg | jokin Pron Qnt Indef Nom Sg |
| NOLEMMAMATCH: | 5264 | täytäntöönpanosta | täytäntöön#pano | täytäntöönpano N Ela Sg |
| NOMATCH: | 5111 | -hinnasta | -hinta TrunCo N Ela Sg | TrunCo hinta N Ela Sg |
| NOANALMATCH: | 4937 | kaikkialla | Adv Ade | kaikkialla Adv Qnt Ade |
| NOMATCH: | 4835 | nähden | nähden Adp Po | nähdä V Inf2 Act Ins |
| NOMATCH: | 4833 | sisältävät | sisältävä A Pos Nom Pl | sisältää PrsPrc Act Pos Nom Pl |
| NOANALMATCH: | 4817 | tällaisten | A Pos Gen Pl | tällainen A Dem Pos Gen Pl |
| NOANALMATCH: | 4771 | tällaisia | A Pos Par Pl | tällainen A Dem Pos Par Pl |
| NORESULTS: | 4751 | à | à |  |
| NOLEMMAMATCH: | 4715 | periaatteiden | peri#aate | periaate N Gen Pl |
| NOANALMATCH: | 4680 | soveltamista | AgPrc Ela Pl | soveltaa AgPrc Pos Ela Pl |
| NOANALMATCH: | 4606 | laatima | AgPrc Nom Sg | laatia AgPrc |
| NOANALMATCH: | 4571 | teki | V Prt Act Sg3 | tehdä V Pst Act Sg3 |
| NOANALMATCH: | 4511 | pikemminkin | Adv Foc_kin | pikemmin Adp Po Comp Foc_kin |
| NORESULTS: | 4489 | p.m | p.m |  |
| NOMATCH: | 4455 | pyrittävä | pyrittää PrsPrc Act Pos Nom Sg | pyrkiä PrsPrc Pass Pos Nom Sg |
| NOANALMATCH: | 4447 | UNIONIN | N Prop Gen Sg | unioni N Gen Sg |
| NOANALMATCH: | 4441 | joidenkin | Pron Qnt Gen Pl | joka Pron Rel Gen Pl Foc_kin |
| NOANALMATCH: | 4435 | iii | Abbr | iii Num Roman Nom Sg |
| NOLEMMAMATCH: | 4422 | täytäntöönpano | täytäntöön#pano | täytäntöönpano N Nom Sg |
| NORESULTS: | 4409 | 31.12.2008 | 31.12.2008 |  |
| NOANALMATCH: | 4321 | Toisaalta | Adv Abl | toisaalta Adv |
| NOANALMATCH: | 4310 | jotakin | Pron Qnt Par Sg | joka Pron Rel Par Sg Foc_kin |
| NOLEMMAMATCH: | 4259 | periaatteita | peri#aate | periaate N Par Pl |
| NOANALMATCH: | 4247 | esitti | V Prt Act Sg3 | esittää V Pst Act Sg3 |
| NOLEMMAMATCH: | 4203 | periaatteessa | peri#aate | periaate N Ine Sg |
| NOANALMATCH: | 4147 | hyväksyttiin | V Prt Pass Pe4 | hyväksyä V Pst Pass Pe4 |
| NORESULTS: | 4039 | http | http |  |
| NOANALMATCH: | 3965 | tehtiin | V Prt Pass Pe4 | tehdä V Pst Pass Pe4 |
| NOLEMMAMATCH: | 3955 | periaatetta | peri#aate | periaate N Par Sg |
| NOANALMATCH: | 3876 | emmekä | CC Neg Pl1 Foc_kA | ei V Neg Pl1 Foc_kA |
| NOANALMATCH: | 3865 | todettiin | V Prt Pass Pe4 | todeta V Pst Pass Pe4 |
| NOLEMMAMATCH: | 3809 | periaatteen | peri#aate | periaate N Gen Sg |
| NOANALMATCH: | 3806 | jotkut | Pron Qnt Nom Pl | joku Pron Qnt Indef Nom Pl |
| NOANALMATCH: | 3804 | jotain | Pron Qnt Par Sg | jokin Pron Qnt Indef Par Sg |
| NOANALMATCH: | 3758 | päätti | V Prt Act Sg3 | päättää V Pst Act Sg3 |
| NOLEMMAMATCH: | 3716 | määrien | määri | määrä N Gen Pl |
| NOANALMATCH: | 3702 | kohden | Adv | kohden Adp Po |
| NOANALMATCH: | 3634 | Tällainen | A Pos Nom Sg | tällainen A Dem Pos Nom Sg |
| NOMATCH: | 3634 | päätöstä | päättö N Ela Sg | päätös N Par Sg |
| NOANALMATCH: | 3590 | sai | V Prt Act Sg3 | saada V Pst Act Sg3 |
| NOLEMMAMATCH: | 3519 | Voimassaolo | voimassa#olo | voimassaolo N Nom Sg |
| NOANALMATCH: | 3510 | A. | Abbr Nom Sg | A. N Prop Nom Sg |
| NOANALMATCH: | 3429 | tällaiset | A Pos Nom Pl | tällainen A Dem Pos Nom Pl |
| NOANALMATCH: | 3404 | Valitettavasti | PrsPrc Pass Pos Man | valitettavasti Adv |
| NOMATCH: | 3399 | tuettava | tuettaa PrsPrc Act Pos Nom Sg | tukea PrsPrc Pass Pos Nom Sg |
| NOMATCH: | 3382 | sanottava | sanottaa PrsPrc Act Pos Nom Sg | sanoa PrsPrc Pass Pos Nom Sg |
| NORESULTS: | 3382 | PIC | PIC |  |
| NORESULTS: | 3349 | A01 | A01 |  |
| NORESULTS: | 3319 | Ltd | ltd |  |
| NOMATCH: | 3297 | tutkimus- | tutkimus- TrunCo N Nom Sg | tutkimus N TrunCo |
| NOLEMMAMATCH: | 3233 | periaatteet | peri#aate | periaate N Nom Pl |
| NOANALMATCH: | 3220 | 2. | Abbr Nom Sg | 2. Num Digit Ord |
| NOANALMATCH: | 3214 | tuli | V Prt Act Sg3 | tuli N Nom Sg |
| NOLEMMAMATCH: | 3172 | periaate | peri#aate | periaate N Nom Sg |
| NOANALMATCH: | 3131 | asti | Adv | asti Adp Po |
| NOANALMATCH: | 3115 | otettiin | V Prt Pass Pe4 | ottaa V Pst Pass Pe4 |
| NOLEMMAMATCH: | 3103 | sosiaalikomitean | sosiaali#komitea | sosiaali-#komitea N Gen Sg |


