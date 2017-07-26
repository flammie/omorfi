---
layout: page
title: "Paradigms and stuffs"
category: stats
date: 2016-02-08 18:23:58
---


# Introduction
This document was automatically generated from the omorfi 
            database. It describes some of the internal codes used in the
            database. Keys and values "_stuff_", and the _paradigms_ that
            define inflection patterns or so.

## Stuff 
Stuff are internal things, but they appear in database a lot, so
            you will want to know what they are if you are gonna modify database
            of affixes.

The stuff is typically used by the file format and/or analysis
        generators to either define analysis tags or decide whether or not to
        include the affected string into language model. The default renditions
        for a handful of omorfi tag formats are provided (only ones that have
        trivially0 mapped formatting are included.

### ` NOUN ` 

Noun

* omor:  [POS=NOUN]
* ftb3:  % N
* apertium-fin:  %<n%>
* giella:  %+N

### ` ADJECTIVE ` 

Adjective (comparable)

* omor:  [POS=ADJECTIVE]
* ftb3:  % A
* apertium-fin:  %<adj%>
* giella:  %+A

### ` QUALIFIER ` 

Qualifier (not comparable)

* omor:  [SUBCAT=QUALIFIER]
* ftb3:  % A
* apertium-fin:  %<adj%>
* giella:  %+A

### ` VERB ` 

Verb

* omor:  [POS=VERB]
* ftb3:  % V
* apertium-fin:  %<vblex%>
* giella:  %+V

### ` ADVERB ` 

Adverb

* omor:  [POS=ADVERB]
* ftb3:  % Adv
* apertium-fin:  %<adv%>
* giella:  %+Adv

### ` INTERJECTION ` 

Interjection

* omor:  [SUBCAT=INTERJECTION]
* ftb3:  % Interj
* apertium-fin:  %<ij%>
* giella:  %+Interj

### ` PRONOUN ` 

Pronoun

* omor:  [POS=PRONOUN]
* ftb3:  % Pron
* apertium-fin:  %<prn%>
* giella:  %+Pron

### ` NUMERAL ` 

Numeral

* omor:  [POS=NUMERAL]
* ftb3:  % Num
* apertium-fin:  %<num%>
* giella:  %+Num

### ` ADPOSITION ` 

Adposition

* omor:  [POS=ADPOSITION]
* ftb3:  % Adp% Po
* apertium-fin:  %<post%>
* giella:  %+Adp%+Po

### ` PREPOSITION ` 

Preposition

* omor:  
* ftb3:  % Adp% Pr
* apertium-fin:  
* giella:  %+Adp%+Pr

### ` POSTPOSITION ` 

Postposition

* omor:  
* ftb3:  
* apertium-fin:  
* giella:  

### ` CONJUNCTION ` 

Conjunction

* omor:  [SUBCAT=CONJUNCTION]
* ftb3:  
* apertium-fin:  
* giella:  

### ` COORDINATING ` 

Coordinating conjunction

* omor:  [CONJ=COORD]
* ftb3:  % CC
* apertium-fin:  %<cnjcoo%>
* giella:  %+CC

### ` ADVERBIAL ` 

Adverbial conjunction

* omor:  [CONJ=ADVERBIAL]
* ftb3:  % CS
* apertium-fin:  %<cnjadv%>
* giella:  %+CS

### ` COMPARATIVE ` 

Comparative conjunction

* omor:  [CONJ=COMPARATIVE]
* ftb3:  % CS
* apertium-fin:  %<cnjsub%>
* giella:  %+CS

### ` ABBREVIATION ` 

Abbreviation (non-inflecting, may end in full stop)

* omor:  [SUBCAT=ABBREVIATION]
* ftb3:  % Abbr
* apertium-fin:  %<abbr%>
* giella:  %+ABBR

### ` ACRONYM ` 

Acronym (inflects with colon)

* omor:  [POS=NOUN][SUBCAT=ABBREVIATION]
* ftb3:  % N% Abbr
* apertium-fin:  %<abbr%>
* giella:  %+ACR

### ` PROPER ` 

Proper noun

* omor:  [PROPER=PROPER]
* ftb3:  % Prop
* apertium-fin:  %<np%>
* giella:  %+Prop

### ` CARDINAL ` 

Cardinal

* omor:  [SUBCAT=CARD]
* ftb3:  
* apertium-fin:  %<card%>
* giella:  

### ` ORDINAL ` 

Ordinal

* omor:  [SUBCAT=ORD]
* ftb3:  % Ord
* apertium-fin:  %<ord%>
* giella:  %+Ord

### ` DEMONSTRATIVE ` 

Demonstrative

* omor:  [SUBCAT=DEMONSTRATIVE]
* ftb3:  % Dem
* apertium-fin:  %<dem%>
* giella:  %+Dem

### ` QUANTOR ` 

Quantifier (pronoun)

* omor:  [SUBCAT=QUANTOR]
* ftb3:  % Qnt
* apertium-fin:  %<qu%>
* giella:  %+Qnt

### ` PERSONAL ` 

Personal (pronoun)

* omor:  [SUBCAT=PERSONAL]
* ftb3:  % Pers
* apertium-fin:  %<pers%>
* giella:  %+Pers

### ` INDEFINITE ` 

Indefinite (pronoun)

* omor:  
* ftb3:  % Indef
* apertium-fin:  %<ind%>
* giella:  %+Indef

### ` INTERROGATIVE ` 

Interrogative

* omor:  [SUBCAT=INTERROGATIVE]
* ftb3:  % Interr
* apertium-fin:  %<itg%>
* giella:  %+Interr

### ` REFLEXIVE ` 

Reflexive (pronoun)

* omor:  [SUBCAT=REFLEXIVE]
* ftb3:  % Refl
* apertium-fin:  %<reflex%>
* giella:  %+Refl

### ` RELATIVE ` 

Relative

* omor:  [SUBCAT=RELATIVE]
* ftb3:  % Rel
* apertium-fin:  %<rel%>
* giella:  %+Rel

### ` RECIPROCAL ` 

Reciprocal

* omor:  [SUBCAT=RECIPROC]
* ftb3:  
* apertium-fin:  %<rec%>
* giella:  

### ` PUNCTUATION ` 

Punctuation

* omor:  [POS=PUNCTUATION]
* ftb3:  % Punct
* apertium-fin:  
* giella:  %+Punct

### ` DASH ` 

Dash

* omor:  [SUBCAT=DASH]
* ftb3:  % Dash
* apertium-fin:  %<guio%>
* giella:  %+Dash

### ` SPACE ` 

Space

* omor:  [SUBCAT=SPACE]
* ftb3:  
* apertium-fin:  
* giella:  

### ` DECIMAL ` 

Decimal digits

* omor:  [SUBCAT=DECIMAL]
* ftb3:  
* apertium-fin:  
* giella:  

### ` CLAUSE-BOUNDARY ` 

Clause final

* omor:  [BOUNDARY=CLAUSE]
* ftb3:  
* apertium-fin:  
* giella:  

### ` SENTENCE-BOUNDARY ` 

Sentence final

* omor:  [BOUNDARY=SENTENCE]
* ftb3:  
* apertium-fin:  %<sent%>
* giella:  

### ` INITIAL-QUOTE ` 

Left quotation mark

* omor:  [SUBCAT=QUOTATION][POSITION=INITIAL]
* ftb3:  % Quote
* apertium-fin:  %<lquot%>
* giella:  %+Quote

### ` FINAL-QUOTE ` 

Right quotation mark

* omor:  [SUBCAT=QUOTATION][POSITION=FINAL]
* ftb3:  % Quote
* apertium-fin:  %<rquot%>
* giella:  %+Quote

### ` INITIAL-BRACKET ` 

Left bracket

* omor:  [SUBCAT=BRACKET][POSITION=INITIAL]
* ftb3:  
* apertium-fin:  %<lpar%>
* giella:  

### ` FINAL-BRACKET ` 

Right bracket

* omor:  [SUBCAT=BRACKET][POSITION=FINAL]
* ftb3:  
* apertium-fin:  %<rpar%>
* giella:  

### ` DIGIT ` 

Digits

* omor:  
* ftb3:  % Digit
* apertium-fin:  
* giella:  %+Digit

### ` ROMAN ` 

Roman numerals

* omor:  [SUBCAT=ROMAN]
* ftb3:  % Roman
* apertium-fin:  
* giella:  %+Roman

### ` PL1 ` 

First plural" 

* omor:  [PERS=PL1]
* ftb3:  % Pl1
* apertium-fin:  %<p1%>
* giella:  %+Pl1

### ` PL2 ` 

Secod plural

* omor:  [PERS=PL2]
* ftb3:  % Pl2
* apertium-fin:  %<p2%>
* giella:  %+Pl2

### ` PL3 ` 

Third plural

* omor:  [PERS=PL3]
* ftb3:  % Pl3
* apertium-fin:  %<p3%>
* giella:  %+Pl3

### ` SG1 ` 

First singular" 

* omor:  [PERS=SG1]
* ftb3:  % Sg1
* apertium-fin:  %<p1%>
* giella:  %+Sg1

### ` SG2 ` 

Second singular

* omor:  [PERS=SG2]
* ftb3:  % Sg2
* apertium-fin:  %<p2%>
* giella:  %+Sg2

### ` SG3 ` 

Third singular

* omor:  [PERS=SG3]
* ftb3:  % Sg3
* apertium-fin:  %<p3%>
* giella:  %+Sg3

### ` PE4 ` 

Passive

* omor:  [PERS=PE4]
* ftb3:  % Pe4
* apertium-fin:  
* giella:  %+Pe4

### ` COMP ` 

Comparative

* omor:  [CMP=CMP]
* ftb3:  % Comp
* apertium-fin:  %<com%>
* giella:  %+Comp

### ` SUPERL ` 

Superlative

* omor:  [CMP=SUP]
* ftb3:  % Superl
* apertium-fin:  %<sup%>
* giella:  %+Superl

### ` UNSPECIFIED ` 

Unclassified particle

* omor:  
* ftb3:  % Adv
* apertium-fin:  %<part%>
* giella:  %+Pcle

### ` LEMMA-START ` 

Left marker for lemma

* omor:  [WORD_ID=
* ftb3:  
* apertium-fin:  
* giella:  

### ` Bc ` 

Compound boundary for generated compounds

* omor:  [BOUNDARY=COMPOUND]
* ftb3:  #
* apertium-fin:  +
* giella:  #

### ` .sent ` 

Sentence ?

* omor:  [BOUNDARY=SENTENCE]
* ftb3:  
* apertium-fin:  
* giella:  

### ` B- ` 

Marker for co-ordinated compound hyphen

* omor:  [COMPOUND_FORM=OMIT]
* ftb3:  % TrunCo
* apertium-fin:  -
* giella:  %+Trunc

### ` B→ ` 

Marker for left co-ordinated compound hyphen

* omor:  [POSITION=SUFFIX]
* ftb3:  TrunCo% 
* apertium-fin:  -
* giella:  TruncSuffix%+

### ` B← ` 

Marker for right co-ordinated compound hyphen

* omor:  [POSITION=PREFIX]
* ftb3:  % TrunCo
* apertium-fin:  -
* giella:  %+TruncPrefix

### ` Cma ` 

Agent participle

* omor:  [PCP=AGENT]
* ftb3:  % AgPrc
* apertium-fin:  %<agent%>
* giella:  %+AgPrc

### ` Cmaisilla ` 

Fifth infinitive

* omor:  
* ftb3:  % Adv
* apertium-fin:  
* giella:  %+Der/maisilla

### ` Cnut ` 

Nut participle

* omor:  [PCP=NUT]
* ftb3:  % PrfPrc
* apertium-fin:  %<pp%>
* giella:  %+PrfPrc

### ` Cva ` 

Va participle

* omor:  [PCP=VA]
* ftb3:  % PrsPrc
* apertium-fin:  %<pprs%>
* giella:  %+PrsPrc

### ` Cmaton ` 

Negation participle

* omor:  [PCP=NEG]
* ftb3:  % NegPrc
* apertium-fin:  %<pneg%>
* giella:  %+NegPrc

### ` Cpos ` 

Positive comparison

* omor:  
* ftb3:  % Pos
* apertium-fin:  %<pos%>
* giella:  %+Pos

### ` Ccmp ` 

Comparative comparison

* omor:  [CMP=CMP]
* ftb3:  % Comp
* apertium-fin:  %<com%>
* giella:  %+Comp

### ` Csup ` 

Superlative comparison

* omor:  [CMP=SUP]
* ftb3:  % Superl
* apertium-fin:  %<sup%>
* giella:  %+Superl

### ` Dmaisilla ` 

Deverbal -mAisillA

* omor:  [INF=MAISILLA]
* ftb3:  % Inf5
* apertium-fin:  +maisilla%<adv%>%>
* giella:  %+Der/maisilla

### ` Dminen ` 

Deverbal -minen

* omor:  [DRV=MINEN]
* ftb3:  % N
* apertium-fin:  +minen%<n%>%>
* giella:  %+N

### ` Dnut ` 

Deverbal -nUt

* omor:  [DRV=NUT]
* ftb3:  % PrfPrc% Act
* apertium-fin:  +nut%<adj%>%>
* giella:  %+PrfPrc%+Act

### ` Dtu ` 

Deverbal -tU

* omor:  [DRV=TU]
* ftb3:  % PrfPrc% Pass
* apertium-fin:  +tu%<adj%>%>
* giella:  %+PrfPrc%+Pass

### ` Dva ` 

Deverbal -vA

* omor:  [DRV=VA]
* ftb3:  % PrsPrc% Act
* apertium-fin:  +va%<adj%>%>
* giella:  %+PrsPrc%+Act

### ` Dtava ` 

Deverbal -tAvA

* omor:  [DRV=TAVA]
* ftb3:  % PrsPrc% Pass
* apertium-fin:  +tava%<adj%>%>
* giella:  %+PrsPrc%+Pass

### ` Dmaton ` 

Deverbal mAtOn

* omor:  [DRV=MATON]
* ftb3:  % NegPrc
* apertium-fin:  +maton%<adj%>%>
* giella:  %+NegPrc

### ` Duus ` 

Derivation -UUs

* omor:  [DRV=UUS]
* ftb3:  
* apertium-fin:  +uus%<adj%>%>
* giella:  %+Der/uus

### ` Dttaa ` 

Derivation -ttAA

* omor:  [DRV=TTAA]
* ftb3:  
* apertium-fin:  +ttaa%<vblex%>%>
* giella:  %+Der/ttaa

### ` Dtattaa ` 

Derivation -tAttAA

* omor:  [DRV=TATTAA]
* ftb3:  
* apertium-fin:  +tattaa%<vblex%>%>
* giella:  %+Der/tattaa

### ` Dtatuttaa ` 

Derivation -tAtUttAA

* omor:  [DRV=TATUTTAA]
* ftb3:  
* apertium-fin:  +tatuttaa%<vblex%>%>
* giella:  %+Der/tatuttaa

### ` Dma ` 

Derivation -mA

* omor:  [DRV=MA]
* ftb3:  % AgPrc
* apertium-fin:  +ma%<n%>%>
* giella:  %+AgPrc

### ` Dinen ` 

Derivation -inen

* omor:  [DRV=INEN]
* ftb3:  
* apertium-fin:  +inen%<n%>%>
* giella:  %+Der/inint

### ` Dja ` 

Derivation -jA

* omor:  [DRV=JA]
* ftb3:  
* apertium-fin:  +ja%<n%>%>
* giella:  %+Der/ja

### ` Dmpi ` 

Derivation -mpi

* omor:  
* ftb3:  
* apertium-fin:  +mpi%<adj%>%>
* giella:  %+Comp

### ` Din ` 

Derivation -in

* omor:  
* ftb3:  
* apertium-fin:  +in%<n%>%>
* giella:  %+Superl

### ` Ds ` 

Derivaiton -s

* omor:  [DRV=S]
* ftb3:  
* apertium-fin:  
* giella:  %+Cmp

### ` Du ` 

Derivation -u

* omor:  [DRV=U]
* ftb3:  
* apertium-fin:  +u%<n%>%>
* giella:  %+Der/u

### ` Dsti ` 

Derivation -sti

* omor:  [DRV=STI]
* ftb3:  
* apertium-fin:  +sti%<adv%>%>
* giella:  %+Der/sti

### ` FTB3man ` 

Manner adverbial (analysis for legacy support)

* omor:  
* ftb3:  % Man
* apertium-fin:  
* giella:  %+Man

### ` Ia ` 

A infinitive

* omor:  [INF=A]
* ftb3:  % Inf1
* apertium-fin:  %<infa%>
* giella:  %+Inf1

### ` Ie ` 

E infinitive

* omor:  [INF=E]
* ftb3:  % Inf2
* apertium-fin:  %<infe%>
* giella:  %+Inf2

### ` Ima ` 

mA infinitive

* omor:  [INF=MA]
* ftb3:  % Inf3
* apertium-fin:  %<infma%>
* giella:  %+Inf3

### ` Iminen ` 

Fourth infinitive

* omor:  [INF=MINEN]
* ftb3:  % N
* apertium-fin:  %<infminen%>
* giella:  %+N

### ` Ncon ` 

Conneg verb form (in negative constructions)

* omor:  [NEG=CON]
* ftb3:  % ConNeg
* apertium-fin:  %<conneg%>
* giella:  %+ConNeg

### ` Nneg ` 

Negation verb

* omor:  [SUBCAT=NEG]
* ftb3:  % Neg
* apertium-fin:  %<neg%>
* giella:  %+Neg

### ` Npl ` 

Plural" 

* omor:  [NUM=PL]
* ftb3:  % Pl
* apertium-fin:  %<pl%>
* giella:  %+Pl

### ` Nsg ` 

Singular" 

* omor:  [NUM=SG]
* ftb3:  % Sg
* apertium-fin:  %<sg%>
* giella:  %+Sg

### ` N?? ` 

Number to be determined

* omor:  
* ftb3:  % Sg
* apertium-fin:  %<ND%>
* giella:  %+Sg

### ` Osg1 ` 

First person singular possessive

* omor:  [POSS=SG1]
* ftb3:  % PxSg1
* apertium-fin:  %<pxsg1%>
* giella:  %+PxSg1

### ` Osg2 ` 

Second person singular possessive

* omor:  [POSS=SG2]
* ftb3:  % PxSg2
* apertium-fin:  %<pxsg2%>
* giella:  %+PxSg2

### ` Osg3 ` 

Third person singular possessive

* omor:  
* ftb3:  
* apertium-fin:  
* giella:  

### ` O3 ` 

Third person ambiguous possessive

* omor:  [POSS=3]
* ftb3:  % Px3
* apertium-fin:  %<pxsp3%>
* giella:  %+Px3

### ` Opl1 ` 

First person plural possessive

* omor:  [POSS=PL1]
* ftb3:  % PxPl1
* apertium-fin:  %<pxpl1%>
* giella:  %+PxPl1

### ` Opl2 ` 

Second person plural possessive

* omor:  [POSS=PL2]
* ftb3:  % PxPl2
* apertium-fin:  %<pxpl2%>
* giella:  %+PxPl2

### ` Opl3 ` 

Third person plural possessive

* omor:  
* ftb3:  
* apertium-fin:  
* giella:  

### ` Ppl1 ` 

First person plural actor

* omor:  [PERS=PL1]
* ftb3:  % Pl1
* apertium-fin:  %<p1%>%<pl%>
* giella:  %+Pl1

### ` Ppl2 ` 

Second person plural actor

* omor:  [PERS=PL2]
* ftb3:  % Pl2
* apertium-fin:  %<p2%>%<pl%>
* giella:  %+Pl2

### ` Ppl3 ` 

Third person plural actor

* omor:  [PERS=PL3]
* ftb3:  % Pl3
* apertium-fin:  %<p3%>%<pl%>
* giella:  %+Pl3

### ` Psg1 ` 

First person singular actor" 

* omor:  [PERS=SG1]
* ftb3:  % Sg1
* apertium-fin:  %<p1%>%<sg%>
* giella:  %+Sg1

### ` Psg2 ` 

Second person singular actor

* omor:  [PERS=SG2]
* ftb3:  % Sg2
* apertium-fin:  %<p2%>%<sg%>
* giella:  %+Sg2

### ` Psg3 ` 

Third person singular actor

* omor:  [PERS=SG3]
* ftb3:  % Sg3
* apertium-fin:  %<p3%>%<sg%>
* giella:  %+Sg3

### ` Ppe4 ` 

Passive" 

* omor:  [PERS=PE4]
* ftb3:  % Pe4
* apertium-fin:  %<impers%>
* giella:  %+Pe4

### ` Qka ` 

Focus clitic particle -kA

* omor:  [CLIT=KA]
* ftb3:  % Foc%_kA
* apertium-fin:  +ka%<enc%>
* giella:  %+Foc%_kA

### ` Qs ` 

Focus clitic particle -s

* omor:  [CLIT=S]
* ftb3:  % Foc%_s
* apertium-fin:  +s%<enc%>
* giella:  %+Foc%_s

### ` Qpa ` 

Focus clitic particle -pA

* omor:  [CLIT=PA]
* ftb3:  % Foc%_pA
* apertium-fin:  +pa%<enc%>
* giella:  %+Foc%_pA

### ` Qko ` 

Focus clitic particle -kO (question)

* omor:  [CLIT=KO]
* ftb3:  % Foc%_kO
* apertium-fin:  +ko%<qst%>
* giella:  %+Foc%_kO

### ` Qkin ` 

Focus clitic particle -kin

* omor:  [CLIT=KIN]
* ftb3:  % Foc%_kin
* apertium-fin:  +kin%<enc%>
* giella:  %+Foc%_kin

### ` Qkaan ` 

Focus clitic particle -kAAn

* omor:  [CLIT=KAAN]
* ftb3:  % Foc%_kAAn
* apertium-fin:  +kaan%<enc%>
* giella:  %+Foc%_kAAn

### ` Qhan ` 

Focus clitic particle -hAn

* omor:  [CLIT=HAN]
* ftb3:  % Foc%_hAn
* apertium-fin:  +han%<enc%>
* giella:  %+Foc%_hAn

### ` Tcond ` 

Conditional

* omor:  [MOOD=COND]
* ftb3:  % Cond
* apertium-fin:  %<cond%>
* giella:  %+Cond

### ` Timp ` 

Impertative" 

* omor:  [MOOD=IMPV]
* ftb3:  % Impv
* apertium-fin:  %<imp%>
* giella:  %+Impv

### ` Tpast ` 

Indicative past

* omor:  [MOOD=INDV][TENSE=PAST]
* ftb3:  % Pst
* apertium-fin:  %<past%>
* giella:  %+Pst

### ` Tpot ` 

Potential" 

* omor:  [MOOD=POTN]
* ftb3:  % Pot
* apertium-fin:  %<pot%>
* giella:  %+Pot

### ` Tpres ` 

Indicative Present

* omor:  [MOOD=INDV][TENSE=PRESENT]
* ftb3:  % Prs
* apertium-fin:  %<pri%>
* giella:  %+Prs

### ` Topt ` 

Optative

* omor:  [MOOD=OPT]
* ftb3:  % Opt
* apertium-fin:  
* giella:  %+Opt

### ` Uarch ` 

Archaic

* omor:  [STYLE=ARCHAIC]
* ftb3:  
* apertium-fin:  %<use_archaic%>
* giella:  

### ` Udial ` 

Dialect general

* omor:  [STYLE=DIALECTAL]
* ftb3:  
* apertium-fin:  %<use_nonstd%>
* giella:  %+Dial

### ` Urare ` 

Rare

* omor:  [STYLE=RARE]
* ftb3:  
* apertium-fin:  
* giella:  %+Use/Marg

### ` Unonstd ` 

Non-standard

* omor:  [STYLE=NONSTANDARD]
* ftb3:  
* apertium-fin:  %<use_nonstd%>
* giella:  %+Err/Orth

### ` Vact ` 

Active

* omor:  [VOICE=ACT]
* ftb3:  % Act
* apertium-fin:  %<actv%>
* giella:  %+Act

### ` Vpss ` 

Passive

* omor:  [VOICE=PSS]
* ftb3:  % Pass
* apertium-fin:  %<pasv%>
* giella:  %+Pass

### ` Xabe ` 

Abessive

* omor:  [CASE=ABE]
* ftb3:  % Abe
* apertium-fin:  %<abe%>
* giella:  %+Abe

### ` Xabl ` 

Ablative

* omor:  [CASE=ABL]
* ftb3:  % Abl
* apertium-fin:  %<abl%>
* giella:  %+Abl

### ` Xade ` 

Adessive

* omor:  [CASE=ADE]
* ftb3:  % Ade
* apertium-fin:  %<ade%>
* giella:  %+Ade

### ` Xall ` 

Allative

* omor:  [CASE=ALL]
* ftb3:  % All
* apertium-fin:  %<all%>
* giella:  %+All

### ` Xcom ` 

Comitative

* omor:  [CASE=COM]
* ftb3:  % Com
* apertium-fin:  %<com%>
* giella:  %+Com

### ` Xela ` 

Elative

* omor:  [CASE=ELA]
* ftb3:  % Ela
* apertium-fin:  %<ela%>
* giella:  %+Ela

### ` Xess ` 

Essive

* omor:  [CASE=ESS]
* ftb3:  % Ess
* apertium-fin:  %<ess%>
* giella:  %+Ess

### ` Xgen ` 

Genitive

* omor:  [CASE=GEN]
* ftb3:  % Gen
* apertium-fin:  %<gen%>
* giella:  %+Gen

### ` Xill ` 

Illative" 

* omor:  [CASE=ILL]
* ftb3:  % Ill
* apertium-fin:  %<ill%>
* giella:  %+Ill

### ` Xine ` 

Inessive

* omor:  [CASE=INE]
* ftb3:  % Ine
* apertium-fin:  %<ine%>
* giella:  %+Ine

### ` Xins ` 

Instructive

* omor:  [CASE=INS]
* ftb3:  % Ins
* apertium-fin:  %<ins%>
* giella:  %+Ins

### ` Xnom ` 

Nominative

* omor:  [CASE=NOM]
* ftb3:  % Nom
* apertium-fin:  %<nom%>
* giella:  %+Nom

### ` Xpar ` 

Partitive" 

* omor:  [CASE=PAR]
* ftb3:  % Par
* apertium-fin:  %<par%>
* giella:  %+Par

### ` Xtra ` 

Transtlative" 

* omor:  [CASE=TRA]
* ftb3:  % Tra
* apertium-fin:  %<tra%>
* giella:  %+Tra

### ` Xlat ` 

Lative

* omor:  [CASE=LAT]
* ftb3:  % Lat
* apertium-fin:  %<lat%>
* giella:  %+Lat

### ` Xacc ` 

Accusative

* omor:  [CASE=ACC]
* ftb3:  % Acc
* apertium-fin:  %<acc%>
* giella:  %+Acc

### ` X??? ` 

Case to be determined

* omor:  
* ftb3:  % Nom
* apertium-fin:  
* giella:  %+Nom

## Paradigms

### ` Root `

The start of the dictionary

### ` ACRONYM `

Acronyms are shortenings that inflect.

### ` ADJECTIVE `

Adjectives are words that are inflected like nouns plus comparisons.

### ` A_TUMMAHKO `

The words in this class ending in o belong here, the old dictionaries use class ¹. This class includes back vowel moderative derivations. N.B. the comparative derivation of moderatives is semantically awkward, but morphologically plausible.
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_VALKAISTU `

The stems ending in u are in class described here, and in old dictionaries the class is ¹. Common part of this class is formed by nut participle passive’s _back_ vowel versions after s stem verbs
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_HÄPÄISTY `

The stems ending in y are in class described here, and in old dictionaries the class is ¹. Common part of this class is formed by nut participle passive’s _front_ vowel versions after s stem verbs
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_HÖLÖ `

The words in this class ending in ö belong to described here, the old dictionaries use class ¹. This class includes front vowel moderative derivations.
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_TOOPE `

The new words with e stem have same allomorph selection as old short unchanging bisyllabic u, y, o and ö stems, and no stem-internal variation. The classification for the back vowel variant of this class is described here, and old dictionaries used the class ⁸. They also have slightly greater probability for archaic form of plural genitive
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_BEIGE `

The front variation of unchanging e stems is class described here, and in old dictionaries ⁸.
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_KOHELO `

The o final trisyllabic stems are in class described here, and the old dictionaries used ². 
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 2
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_LÖPERÖ `

And the trisyllabic ö stem is classified described here.
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 2
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_AUTIO `

The class for o final long vowel stems is described here, and old old dictionaries used ³. 
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 3
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_RIIVIÖ `

The front voweled stems with ö after vowels go to class described here, and used the old dictionary class ³.
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 3
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_KOLKKO `

The quantitative k gradations with o bisyllabic o stem use class described here, and old dictionaries use classes ¹⁻A and ¹⁻D.
* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_VIRKKU `

The quantitative k gradations with u bisyllabic o stem use class described here, and old dictionaries use classes ¹⁻A and ¹⁻D.
* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_SÄIKKY `

The quantitative k gradations with y bisyllabic o stem use class described here, and old dictionaries use classes ¹⁻A and ¹⁻D.
* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_KÖKKÖ `

The quantitative k gradations with o bisyllabic ö stem use class described here, and old dictionaries use classes ¹⁻A and ¹⁻D.
* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_SUIPPO `

The quantitative gradation of p before o is in class described here and old dictionaries would use ¹⁻B.
* kotus_av: B
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_IKÄLOPPU `

The quantitative gradation of p before u is in class described here and old dictionaries would use ¹⁻B. It is only a nominal compound based adjective that ends in u and has p ~ 0 gradation here:
* kotus_av: B
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_LÖRPPÖ `

The quantitative gradation of p before ö is in class described here and old dictionaries would use ¹⁻B.
* kotus_av: B
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_VELTTO `

The quantitative gradation of t before o is in class described here, which was ¹⁻C in the dictionary.
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_VIMMATTU `

The quantitative gradation of t before u is in class described here, which was ¹⁻C in the dictionary. The u stems with quantitative t gradation are commonest with nut participle passive derivation’s back form (-ttu).
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_YLENNETTY `

The quantitative gradation of t before y is in class described here, which was ¹⁻C in the dictionary. The u stems with quantitative t gradation are commonest with nut participle passive derivation’s front (-tty).
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_KYYTTÖ `

The quantitative gradation of t before y is in class described here, which was ¹⁻C in the dictionary. 
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_LAKO `

The class for o final bisyllabic stems with optional ’ is described here, this is a subset of dictionary class ¹⁻D. 
* kotus_av: D
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_KELPO `

The qualitative gradation of p between vowels in o stems goes to v, the class for this is described here, the dictionary class for this is ¹⁻E.
* kotus_av: E
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_MIETO `

The gradation of t ~ d after o is in class described here, the dictionary class for this is ¹⁻F.
* kotus_av: F
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_VIIPALOITU `

The gradation of t ~ d after u is in class described here, the dictionary class for this is ¹⁻F. The commonest t ~ d variation in u stems comes from nut participle’s passive’s back form (-tu).
* kotus_av: F
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_YKSILÖITY `

The gradation of t ~ d after u is in class described here, the dictionary class for this is ¹⁻F. The commonest t ~ d variation in u stems comes from nut participle’s passive’s front form (-ty).
* kotus_av: F
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_LENKO `

The adjectives with -nko stem belong to class described here, and the dictionary class was ¹⁻G.
* kotus_av: G
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_MELTO `

The quantitative gradation of t after l in o stems is in class described here, which corresponds to dictionary class ¹⁻I.
* kotus_av: I
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_PARANNELTU `

The quantitative gradation of t after l in o stems is in class described here, which corresponds to dictionary class ¹⁻I. The common u stem after l is in nut participles passive (-tu):
* kotus_av: I
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_VÄHÄTELTY `

The quantitative gradation of t after l in o stems is in class described here, which corresponds to dictionary class ¹⁻I. As with y and t:
* kotus_av: I
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_VENTO `

The quantitative gradation of t after n in o stems is in class described here, which corresponds to dictionary class ¹⁻J.
* kotus_av: J
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_PANTU `

The quantitative gradation of t after n in u stems is in class described here, which corresponds to dictionary class ¹⁻I. The common u stem after n is in nut participle’s passive’s back form (-tu):
* kotus_av: J
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_MENTY `

The quantitative gradation of t after n in y stems is in class described here, which corresponds to dictionary class ¹⁻I. The common u stem after n is in nut participle’s passive’s front form (-ty)

### ` A_MARTO `

The quantitative gradation of t after r in o stems is in class described here, which corresponds to dictionary class ¹⁻J.
* kotus_av: K
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_PURTU `

The quantitative gradation of t after r in u stems is in class described here, which corresponds to dictionary class ¹⁻J. The common u stem after r is in nut participle’s passive’s back form (-tu):

### ` A_PIERTY `

The quantitative gradation of t after r in y stems is in class described here, which corresponds to dictionary class ¹⁻J. The common u stem after r is in nut participle’s passive’s front fomr (-ty)

### ` A_HUPAKKO `

The class for trisyllabic -kko stems is described here, the corresponding dictionary class is ⁴⁻D. 
* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 4
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_ABNORMI `

The i finals with back vowel harmony go to class described here, where old dictionary classification was ⁵.
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_STYDI `

The i finals with front vowel harmony go to class described here, where old dictionary classification was ⁵.
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_OPAAKKI `

Stems with quantitative k gradation, i final and back harmony are in class described here and dictionary class ⁵⁻A or ⁵⁻D.
* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_PINKKI `

Stems with quantitative k gradation, i final and front harmony are in class described here and dictionary class ⁵⁻A or ⁵⁻D. There's no back vowel version of the bisyllabic gradating -ppi form.
* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_SIPPI `

Stems with quantitative p gradation, i final and front harmony are in class described here and dictionary class ⁵⁻B.
* kotus_av: B
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_HURTTI `

Stems with quantitative t gradation, i final and back harmony are in class described here and dictionary class ⁵⁻C.
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_VÄÄRTTI `

Stems with quantitative t gradation, i final and front harmony are in class described here and dictionary class ⁵⁻C. There are no bisyllabic adjectives ending in vowel and gradating -pi.
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_TUHTI `

Stems with t ~ d gradation, i final and back harmony are in class described here and dictionary class ⁵⁻F.
* kotus_av: F
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_REHTI `

Stems with t ~ d gradation, i final and front harmony are in class described here and dictionary class ⁵⁻F. There are no adjectives with i stems with other gradations.
* kotus_av: F
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_ABNORMAALI `

The i stems with trisyllabic allomorph sets have class described here, and dictionary class of ⁶.
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 6
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_ÖYKKÄRI `

The i stems with trisyllabic allomorph sets have class described here, and dictionary class of ⁶. There are no adjectives acting like nouns where i-final nominatives have singular e stems.
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 6
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_AAVA `

Bisyllabic a stems with e comparative and j plurals are in class described here, and dictionary class ⁹.
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_TARKKA `

The ka stem with e comparative and j plurals is described here, and the dictionary class is ⁹-A or ⁹⁻D.
* kotus_av: D
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_MATTA `

The ta stem with j plurals is described here, and the dictionary class is ⁹-C.
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_HALPA `

The pa : va stem with e comparative and j plurals is described here, and the dictionary class is ⁹⁻E.
* kotus_av: E
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_EHTA `

The ta : da stem with a comparative and j plurals is described here, and the dictionary class is ⁹⁻F. None with k:g gradation.
* kotus_av: F
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_RAMPA `

The pa : ma stem with e comparative and j plurals is described here, and the dictionary class is ⁹⁻H.
* kotus_av: H
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_VIHANTA `

The ta : na stem with a comparative and j plurals is described here, and the dictionary class is ⁹⁻J.
* kotus_av: J
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_AALTOILEVA `

The a : 0 stem is in class described here and the old dictionary used ¹⁰ as the paradigm class.

### ` A_TYÖLLISTETTÄVÄ `

The ä : 0 stem is in class described here and the old dictionary used ¹⁰ as the paradigm class.

### ` A_RUMA `

For a:e comparatives in a:0 class use described here. No dictionary classification or ~¹⁰, 
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_TYHMÄ `

For ä:e comparatives in a:0 class use described here. No dictionary classification or ~¹⁰, 
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_HOIKKA `


* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_MYKKÄ `


* kotus_av: D
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_POPPA `


* kotus_av: B
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_HÖMPPÄ `

The quantitative k and t gradations are not found for adjectives with this a stem.
* kotus_av: B
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_VOIPA `


* kotus_av: E
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_KÄYPÄ `


* kotus_av: E
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_MÄTÄ `


* kotus_av: F
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_SANKA `


* kotus_av: G
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_VÄNKÄ `


* kotus_av: G
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_KULTA `


* kotus_av: I
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_LÄNTÄ `


* kotus_av: J
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_TURTA `


* kotus_av: K
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_HAPERA `

Certain trisyllabic or longer a stems allow a lot of allomorphs and both a : o : 0 variations:
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 11
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_HÖPPÄNÄ `


* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 12
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_HARMAJA `


* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 12
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_LATUSKA `

Certain trisyllabic or longer a stems allow a lot of allomorphs and both a : o : 0 variations:
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 13
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_HAILAKKA `

The a : o stem variation combines with trisyllabic class of special illatives
* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 14
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_RÄVÄKKÄ `


* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 14
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_POHATTA `

A-final words with long vowels and syllable boundary
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 14
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_AINOA `


* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 15
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_KORKEA `


* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 15
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_JÄREÄ `


* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 15
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_AIEMPI `


* kotus_av: H
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 16
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_LÄHEMPI `


* kotus_av: H
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 16
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_VAPAA `

There are no other bisyllabic long vowel stems in adjectives
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 17
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_PEEAA `


* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` A_MUU `


* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: u
* grade_dir: weaken

### ` A_SYYPÄÄ `


* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_GAY `

Some loan words inflect irregularly, either more along the written form or the pronunciation. There are not many direct adjective loans in general.
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 21
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_SUURI `

Dictionary class 24~26 back
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 26
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_PIENI `

Dictionary class 24~26 front
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 26
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_UUSI `

Dictionary class 27 back
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 27
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_TÄYSI `

Dictionary class 27 front
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 27
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` A_TYVEN `

Dictionary class 32
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 32
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_AVOIN `

Dictionary class 33
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_ALASTON `

Dictionary class 34 back
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 34
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_VIATON `

Dictionary class 34 0~t back
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 34
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_KYVYTÖN `

Dictionary class 34 0~t front
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 34
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_HAPAN `

This one word, hapan, also takes the same variation as normative variant. The expected e variant is not normative, but used. Dictionary class 34 0~p back
* kotus_av: B
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_LÄMMIN `

Dictionary class 34 m~p front
* kotus_av: H
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 35
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_PAHIN `

Dictionary class 35 back
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 36
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_SISIN `

Dictionary class 35 front
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 36
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_VASEN `

Dictionary class 36
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 37
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_AAKKOSELLINEN `

Dictionary class 38 back
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 38
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_KYLMÄJÄRKINEN `

Dictionary class 38 front
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 38
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_SYMPPIS `

Dictionary class 39
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 39
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_LÄHTEISYYS `

Dictionary class 40
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 40
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_AUTUAS `

Dictionary class 41 as
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_VALMIS `

Dictionary class 41 is
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_TYÖLÄS `

Dictionary class 41 äs
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_VOIMAKAS `

Dictionary class 41 kas
* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_TYYLIKÄS `

Dictionary class 41 käs
* kotus_av: A
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_REIPAS `

Dictionary class 41 pas
* kotus_av: B
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_RIETAS `

Dictionary class 41 tas
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_RAITIS `

Dictionary class 41 tis
* kotus_av: C
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_HIDAS `

Dictionary class 41 das
* kotus_av: F
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_HARRAS `

Dictionary class 41 ras
* kotus_av: K
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_OHUT `

Dictionary class 43 back
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 43
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_EHYT `

Dictionary class 43 front
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 43
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_KULUNUT `

Dictionary class 47 back
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 47
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: u
* grade_dir: strengthen

### ` A_ÄLLISTYNYT `

Dictionary class 47 front
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 47
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: y
* grade_dir: strengthen

### ` A_AHNE `

Dictionary class 48 back
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_TERVE `

Dictionary class 48 front
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_KADE `

Dictionary class 48 d~t back
* kotus_av: F
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_HELLE `

Dictionary class 48 l~t back
* kotus_av: I
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` A_PITKÄ `

Adjective pitkä
* kotus_av: None
* pos: ADJECTIVE
* possessive: False
* kotus_tn: 1010
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` A_LEUATTOMAT `

Adjectives aren't typically plural words, but there are some in the dictionaries.

### ` DIGITS `

Digits are constructed as several cyclic structures: integers, decimals or roman numerals. Zero alone works quite differently

### ` DIGITS_INT_LOOP `

Integers can be constructed from any number of digits, ending in 1-9, followed by any number of 0's. Initial 0's are rare, but not totally unexpected

### ` DIGITS_ILLIARD_LOOP `

The digit strings that end in 10 to 12 + 6n 0's are inflected alike

### ` DIGITS_ILLION_LOOP `

The digit strings that end in 6 to 9 + 6n 0's are inflected alike

### ` DIGITS_DECIMAL_LOOP `

Decimal digit strings start with any number of digits 0 to 9, followed by decimal separator comma. The decimal dot may be allowed as substandard variant.

### ` DIGITS_DECIMAL_LOOP_FINAL `

The decimal digit strings end in any number of digits 0 to 9, inflected along the last part.

### ` DIGITS_DECIMAL_LOOP_FINAL_SUB `

The decimal digit strings with dot may be allowed as sub-standard option with respective analysis.

### ` DIGITS_ROMANS `

Roman numerals are composed the symbols M, D, C, L, X, V, I in ascending scale and some combinations, they denote ordinal numbers and inflect like ones.

### ` DIGITS_ROMANS_THOUSANDS `

Thousands can be followed by any of other parts

### ` DIGITS_ROMANS_HUNDREDS `

Hundreds can be followed by anything but thousands:

### ` DIGITS_ROMANS_TENS `

Tens can be followed by ones:

### ` DIGITS_ROMANS_ONES `

Ones come alone

### ` INTERJECTION `

Interjections are mainly parts of spoken language that are minimal turns in dialogue, curses, onomatopoeia and such.

### ` NOUN `

Noun is the part-of-speech for words which require declination in number and case.

### ` N_TALO `

The most basic noun stem does not have any stem internal variation and uses few commonest allomorphs. The words in this class are either bisyllabic or have one of common derivational suffixes: sto, .... The nouns in this class end in o, u, y or ö, which determines their illative suffix and therefore exact classification:
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_ASU `

The stems ending in u are also without variationm and the bisyllabic ones have the same simple allomorph pattern: Dictionary class 1u
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: u
* grade_dir: weaken

### ` N_KÄRRY `

Dictionary class 1y
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_MÖMMÖ `

Dictionary class 1ö
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_UKKO `

Dictionary class 1ko
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TIKKU `

Dictionary class 1ku
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_MYRKKY `

Dictionary class 1ky
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_YÖKKÖ `

Dictionary class 1kö
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HAPPO `

Dictionary class 1po
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LIPPU `

Dictionary class 1pu
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RYYPPY `

Dictionary class 1py
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TÖRPPÖ `

Dictionary class 1pö
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HIRTTO `

Dictionary class 1to
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TORTTU `

Dictionary class 1tu
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PYTTY `

Dictionary class 1ty
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PÖNTTÖ `

Dictionary class 1tö
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TEKO `

Between two vowels, the weak grade of k is optionally an apostrophe instead. For k that is not optionally ’, for example when it is after a consonant other than s, the variation is k ~ 0 instead (e.g. N_UKKO). Dictionary class 1ko
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_MAKU `

Dictionary class 1ku
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NÄKY `

Dictionary class 1ky
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NÄKÖ `

Dictionary class 1kö
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RUOKO `

Between three vowels where k is surrounded by same vowels the k becomes obligatorily ’. When the vowels are different, it becomes optionally ’ (as in N_TEKO), and after consonant other than s it is k ~ 0 (as in N_UKKO). Dictionary class 1ko
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LIUKU `

Dictionary class 1ko Other gradations can be more easily caught from the preceding context.
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HEPO `

Dictionary class 1po
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_APU `

Dictionary class 1pu
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KÄPY `

Dictionary class 1py
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LÖPÖ `

Dictionary class 1pö
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VETO `

Dictionary class 1to
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KUITU `

Dictionary class 1to
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VETY `

Dictionary class 1ty
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HÄÄTÖ `

Dictionary class 1tö
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RUNKO `

Dictionary class 1nko
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VINKU `

Dictionary class 1nku
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SÄNKY `

Dictionary class 1nky
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_YLÄNKÖ `

Dictionary class 1nkö
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SAMPO `

Dictionary class 1mpo
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RUMPU `

Dictionary class 1mpu
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LÄMPÖ `

Dictionary class 1mpö
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KIELTO `

Dictionary class 1lto
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HUOLITELTU `

Dictionary class 1ltu
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_EPÄILTY `

Dictionary class 1lty
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SISÄLTÖ `

Dictionary class 1ltö
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TUNTO `

Dictionary class 1nto
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LINTU `

Dictionary class 1ntu
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_MÄNTY `

Dictionary class 1nty
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KÄÄNTÖ `

Dictionary class 1ntö
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SIIRTO `

Dictionary class 1rto
* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LUKU `

Dictionary class 1cuku
* kotus_av: M
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KYKY `

Dictionary class 1cyky
* kotus_av: M
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RUIPELO `

Dictionary class 2o
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 2
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SEIKKAILU `

Dictionary class 2u
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 2
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VEHKEILY `

Dictionary class 2y
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 2
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_JÄÄTELÖ `

Dictionary class 2ö
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 2
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TUOMIO `

The words with stem vowel o, u, y, ö preceded by vowels still have no more stem variation than other cases, but give yet another pattern of allomorphs for plural partitives and genitives Dictionary class 3o There's plenty of imaginable non-standard allomorph forms after long vowels
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 3
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HÄIRIÖ `

Dictionary class 3ö
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 3
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_ZOMBIE `

Similar inflection exists in limited amounts in new loan words that are written as pronounced (thus taking no stem variation but still ending with long vowels with a syllable boundary) Dictionary class 3eta
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 3
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_BERNIE `

This class includes a set of new proper nouns that get nativised a bit Dictionary class 3etä
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 3
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LEPAKKO `

Dictionary class 4 kko
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 4
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_YKSIKKÖ `

Dictionary class 4 kkö
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 4
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RUUVI `

Dictionary class 5 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TYYLI `

Dictionary class 5 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LOKKI `

Dictionary class 5 back k~0
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HÄKKI `

Dictionary class 5 front k~0
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KUPPI `

Dictionary class 5 back p~0
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TYYPPI `

Dictionary class 5 front p~0
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PORTTI `

Dictionary class 5 back t~0

### ` N_SKEITTI `

Dictionary class 5 front t~0
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LAKI `

Dictionary class 5 back k~’~0
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HUPI `

Dictionary class 5 back p~v There is a gap in i final words for p:v variation and front harmony
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TAUTI `

Dictionary class 5 back t~d
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NIHTI `

Dictionary class 5 front t~d
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VANKI `

Dictionary class 5 back k~g
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HÄMMINKI `

Dictionary class 5 front k~g There is a gap in i final paradigm with t:l variation and back vowels.
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PELTI `

Dictionary class 5 front t~l
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SOINTI `

Dictionary class 5 back t~n
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VIENTI `

Dictionary class 5 front t~n
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PUNK `

New loan words ending in consonant may be inflected as i stem words Dictionary class 5 back no i
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_ZEN `

Dictionary class 5 front no i
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TANKKERI `

Dictionary class 6 back

### ` N_KEHVELI `

Dictionary class 6 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 6
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_STADION `

Dictionary class 6 back no i
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 6
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_BESSERWISSER `

Dictionary class 6 front no i
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 6
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_ONNI `

Dictionary class 7 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KIVI `

Dictionary class 7 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HAPPI `

Dictionary class 7 back p~0
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TYPPI `

Dictionary class 7 front p~0
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NOKI `

Dictionary class 7 back k~0
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KÄKI `

Dictionary class 7 front k~0
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KORPI `

Dictionary class 7 back p~v
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KILPI `

Dictionary class 7 front p~v
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LAHTI `

Dictionary class 7 back t~d
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LEHTI `

Dictionary class 7 front t~d
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_ONKI `

Dictionary class 7 back k~g
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HENKI `

Dictionary class 7 front k~g
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SAMPI `

Dictionary class 7 back p~m
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RIMPI `

Dictionary class 7 front p~m
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_ARKI `

Dictionary class 7 back k~j
* kotus_av: L
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_JÄRKI `

Dictionary class 7 front k~j
* kotus_av: L
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NALLE `

Dictionary class 8 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NISSE `

Dictionary class 8 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NUKKE `

Dictionary class 8 k~0 back
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_JEPPE `

Dictionary class 8 p~0 front
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LOTTE `

Dictionary class 8 t~0 back
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KIRJA `

Dictionary class 9 Notably, the basic a:o paradigm does not support many ä:ö cases.
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_POLITIIKKA `

Dictionary class 9 k~0
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_TIPPA `

Dictionary class 9 p~0
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_MITTA `

Dictionary class 9 t~0
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_VIKA `

Dictionary class 9 k~’~0
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_VAAKA `

Dictionary class 9 k~’
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_SALPA `

Dictionary class 9 p~v
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_PATA `

Dictionary class 9 t~d
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_LANKA `

Dictionary class 9 k~g
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_RAMPA `

Dictionary class 9 p~m
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_VALTA `

Dictionary class 9 t~l
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_KUTSUNTA `

Dictionary class 9 t~n
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_KYSYNTÄ `

Dictionary class 9 t~n front
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_KERTA `

Dictionary class 9 t~r
* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_SOITTAJA `

Dictionary class 10 back

### ` N_HÖPÖTTÄJÄ `

Dictionary class 10 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_LUOKKA `

Dictionary class 10 back k̃~0
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_HÖLKKÄ `

Dictionary class 10 front k̃~0
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_KUOPPA `

Dictionary class 10 back p~0
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_SEPPÄ `

Dictionary class 10 front p~0
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_ROTTA `

Dictionary class 10 back t~0
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_KENTTÄ `

Dictionary class 10 front t~0
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_VUOKA `

Dictionary class 10 back k~’~0

### ` N_IKÄ `

Dictionary class 10 front k~’~0

### ` N_REIKÄ `

Dictionary class 10 back k~’~0
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_LUPA `

Dictionary class 10 back p~v
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_LEIPÄ `

Dictionary class 10 front p~v
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_SOTA `

Dictionary class 10 back t~d
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_PÖYTÄ `

Dictionary class 10 front t~d
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_HONKA `

Dictionary class 10 back k~g
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_KENKÄ `

Dictionary class 10 frot k~g
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_KOMPA `

Dictionary class 10 back p~m
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_MULTA `

Dictionary class 10 back t~l
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_SYLTÄ `

Dictionary class 10 front t~l
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_KUNTA `

Dictionary class 10 back t~n
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_EMÄNTÄ `

Dictionary class 10 front t~n

### ` N_SELKÄ `

Dictionary class 10 front k~j

### ` N_PROBLEEMA `

Dictionary class 11 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 11
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_KÄPÄLÄ `

Dictionary class 11 front Some a stems with a:o variation have slightly different set of allomorphs
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 11
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_MAKKARA `

Dictionary class 12 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 12
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_HÄKKYRÄ `

Dictionary class 12 front There is a possible class for further variation of a:o in the old dictionary dictionary that is worth re-evaluating. There’s one more allomorph pattern.
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 12
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_SIIVILÄ `

Dictionary class 12++ front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 13
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_LUSIKKA `

Dictionary class 14 back
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 14
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_KÄMMEKKÄ `

Dictionary class 14 front
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 14
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_ULAPPA `

Dictionary class 14 back p̃0
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 14
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_POHATTA `

Dictionary class 14 back t0
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 14
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_SOKEA `

The a-final words ending in long vowels with syllable boundary have a:0 variation and more allomorphs for plyral genitive or illative. Dictionary class 15 ea
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 15
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_LIPEÄ `

Dictionary class 15 eä
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 15
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_VANHEMPI `

Dictionary class 16
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 16
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VAINAA `

Dictionary class 17 a
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 17
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_TIENOO `

Dictionary class 17 o
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 17
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: o
* grade_dir: weaken

### ` N_LEIKKUU `

Dictionary class 17 u Monosyllabic long vowel stems have illative suffixes of form -hVn.
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 17
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: u
* grade_dir: weaken

### ` N_MAA `

Dictionary class 18 a
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_TEE `

Dictionary class 18 e
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: e
* grade_dir: weaken

### ` N_HAI `

Dictionary class 18 i back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: i
* grade_dir: weaken

### ` N_PII `

Dictionary class 18 i
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: i
* grade_dir: weaken

### ` N_OOKOO `

Dictionary class 18 o
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: o
* grade_dir: weaken

### ` N_PUU `

Dictionary class 18 u
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: u
* grade_dir: weaken

### ` N_PYY `

Dictionary class 18 y
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: y
* grade_dir: weaken

### ` N_PÄÄ `

Dictionary class 18 ä
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_KÖÖ `

Dictionary class 18 ö
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ö
* grade_dir: weaken

### ` N_TIE `

Dictionary class 19 ie
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 19
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VUO `

Dictionary class 19 uo
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 19
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_YÖ `

Dictionary class 19 yö

### ` N_NUGAA `

Dictionary class 20 a
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 20
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_PATEE `

Dictionary class 20 e
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 20
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: e
* grade_dir: weaken

### ` N_BIDEE `

Dictionary class 20 e front There’s a gap in -ii final loan stems.
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 20
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: e
* grade_dir: weaken

### ` N_TRIKOO `

Dictionary class 20 o
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 20
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: o
* grade_dir: weaken

### ` N_RAGUU `

Dictionary class 20 u
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 20
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: u
* grade_dir: weaken

### ` N_FONDYY `

Dictionary class 20 y
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 20
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: y
* grade_dir: weaken

### ` N_HYVINKÄÄ `

Dictionary class 20 ä

### ` N_MILJÖÖ `

Dictionary class 20 ö
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 20
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ö
* grade_dir: weaken

### ` N_ROSÉ `

Dictionary class 21 e back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 21
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: é
* grade_dir: weaken

### ` N_BÉBÉ `

Dictionary class 21 e front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 21
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: é
* grade_dir: weaken

### ` N_BRASSERIE `

Dictionary class 21 i back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 21
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: í
* grade_dir: weaken

### ` N_BRIE `

Dictionary class 21 i front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 21
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: i
* grade_dir: weaken

### ` N_FONDUE `

Dictionary class 21 ye
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 21
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: Y
* grade_dir: weaken

### ` N_JOCKEY `

Dictionary class 21 yi
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 21
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: i
* grade_dir: weaken

### ` N_COWBOY `

Dictionary class 21 iy
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 21
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: i
* grade_dir: weaken

### ` N_KUNGFU `

Dictionary class 21 u back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 21
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: U
* grade_dir: weaken

### ` N_GAY `

Dictionary class 21 yi
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 21
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: i
* grade_dir: weaken

### ` N_KENTUCKY `

Dictionary class 21 yi

### ` N_CHACHACHA `

Dictionary class 21 a The loan words that end in consonant when written but vowel when pronounced are inflected with an apostrophe ’. With half-vowels the rule is a bit shaky, but officially apostrophe is the only way.
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 21
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: ą
* grade_dir: weaken

### ` N_NOUGAT `

Dictionary class 22 a
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 22
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PARFAIT `

Dictionary class 22 e
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 22
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: e
* grade_dir: weaken

### ` N_BEIGNET `

Dictionary class 22 e front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 22
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: i
* grade_dir: weaken

### ` N_VERSAILLES `

Dictionary class 22 i back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 22
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: i
* grade_dir: weaken

### ` N_SERGEJ `

Dictionary class 22 i front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 22
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_BORDEAUX `

Dictionary class 22 o
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 22
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: o
* grade_dir: weaken

### ` N_SHOW `

Dictionary class 22 u
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 22
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: u
* grade_dir: weaken

### ` N_CAMUS `

Dictionary class 22 y
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 22
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_MONSIEUR `

Dictionary class 22 ö
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 22
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ö
* grade_dir: weaken

### ` N_TULI `

Dictionary class 23
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 23
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VUOHI `

Dictionary class 23++

### ` N_RUUHI `

Dictionary class 24 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 26
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HIIRI `

Dictionary class 24 front It is noteworthy of the official dictionary classification, that classes with numbers 24 and 26 are identical. The distinction should probably not be retained in future versions.
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 26
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KAARI `

Dictionary class 26 back

### ` N_MIELI `

Dictionary class 24 front The -mi stems will rarely undego m:n variation for consonant stem forms.

### ` N_TAIMI `

Dictionary class 25 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 25
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LIEMI `

Dictionary class 25 front The -si words that originate from old -te stems have the consonant gradation patterns left in their stems. The si is only in nominative stem and this class mainly concerns stems that are old enough to have undergone ti>si transformation. 
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 25
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KAUSI `

Dictionary class 27 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 27
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KÖYSI `

Dictionary class 27 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 27
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PONSI `

Dictionary class 27 back t~n
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 28
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LÄNSI `

Dictionary class 27 front t~n
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 28
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VARSI `

Dictionary class 27 back t~r
* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 28
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VIRSI `

Dictionary class 27 front t~r
* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 28
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_JÄLSI `

Dictionary class 27 front t~l A few -psi, -ksi, -tsi stems have consonant simplification for consonant stems. Other variation with these stems is the selection of plural genitive allomorphs.
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 28
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LAPSI `

Dictionary class 27 psi
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 29
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_UKSI `

Dictionary class 27 ksi
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 29
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PEITSI `

Dictionary class 27 tsi back

### ` N_VEITSI `

Dictionary class 27 tsi front The -ksi stem in haaksi includes k:h variation.
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 30
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HAAKSI `

Dictionary class 27 ksi
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 31
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_AHVEN `

Dictionary class 32 back

### ` N_JOUTSEN `

Dictionary class 32 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 32
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SIEMEN `

Dictionary class 32 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 32
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_AJATAR `

Dictionary class 32 tar
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 32
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_TYTÄR `

Dictionary class 32 tär
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 32
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_IEN `

Dictionary class 32 ien Some of the n-final stems have n:m variation.
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 32
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PUHELIN `

Dictionary class 33 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ELIN `

Dictionary class 33 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SUODATIN `

Dictionary class 33 back tin
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_HEITIN `

Dictionary class 33 front tin
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PUIN `

Dictionary class 33 back k~in
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PYYHIN `

Dictionary class 33 front k~in
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KAAVIN `

Dictionary class 33 back vin

### ` N_SÄRVIN `

Dictionary class 33 front vin
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VAADIN `

Dictionary class 33 back din
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LAIDUN `

Dictionary class 33 back dun
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SÄÄDIN `

Dictionary class 33 fron din
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ASKELLIN `

Dictionary class 33 back lin
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SIVELLIN `

Dictionary class 33 frontlin
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KÄÄNNIN `

Dictionary class 33 frpnt nin
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_MUUNNIN `

Dictionary class 33 back nin
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KIHARRIN `

Dictionary class 33 back rin
* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KERROIN `

Dictionary class 33 back roin
* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KIERRIN `

Dictionary class 33 fron rin
* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_POLJIN `

Dictionary class 33 back jin
* kotus_av: L
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_OSATON `

Dictionary class 34 ton
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 34
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_NIMETÖN `

Dictionary class 34 tän
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 34
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VANHIN `

Dictionary class 35 back

### ` N_LÄHIN `

Dictionary class 35 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 36
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VASEN `

Dictionary class 35
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 37
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_AAKKOSTAMINEN `

Dictionary class 38 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 38
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KYLKIÄINEN `

Dictionary class 38 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 38
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VAKUUTUS `

Dictionary class 39 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 39
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RÄJÄYTYS `

Dictionary class 39 front Some of the s final stems have additional s:t:d variation in singular stems. Most notably, the UUs derivations are in this class.
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 39
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_AAKKOSELLISUUS `

Dictionary class 40 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 40
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KÖYHYYS `

Dictionary class 40 front Some s final words have special lengthening inflection.
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 40
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PATSAS `

Dictionary class 41 as
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RUUMIS `

Dictionary class 41 is
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ILMATIIVIS `

Dictionary class 41 is front

### ` N_ARISTOTELES `

Dictionary class 41 es back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KIRVES `

Dictionary class 41 es front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ÄYRÄS `

Dictionary class 41 äs
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ASUKAS `

Dictionary class 41 kas
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KÄRSÄKÄS `

Dictionary class 41 käs
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SAAPAS `

Dictionary class 41 pas
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RYPÄS `

Dictionary class 41 päs
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RATAS `

Dictionary class 41 tas
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_MÄTÄS `

Dictionary class 41 täs
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KELTIS `

Dictionary class 41 tis
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_IES `

Dictionary class 41 ies
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VARAS `

Dictionary class 41 as
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RUIS `

Dictionary class 41 is
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VARVAS `

Dictionary class 41 vas
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SEIVÄS `

Dictionary class 41 väs
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_TEHDAS `

Dictionary class 41 das
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KANGAS `

Dictionary class 41 gas
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KÖNGÄS `

Dictionary class 41 gäs
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_HAMMAS `

Dictionary class 41 mas
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ALLAS `

Dictionary class 41 las
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KINNAS `

Dictionary class 41 nas
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RYNNÄS `

Dictionary class 41 näs
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PORRAS `

Dictionary class 41 ras The word mies has special s:h variation pattern.
* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_MIES `

Dictionary class 42
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 42
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_OLUT `

Dictionary class 43 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 43
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_NEITSYT `

Dictionary class 43 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 43
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_IMMYT `

Dictionary class 43 myt Few t-final words have lengthening in singular stems
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 43
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KEVÄT `

Dictionary class 44 Nominalised nut participles have special inflection just as well.
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_AIVOKUOLLUT `

Dictionary class 47 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 47
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: u
* grade_dir: strengthen

### ` N_SIVISTYNYT `

Dictionary class 47 front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 47
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: y
* grade_dir: strengthen

### ` N_ASTE `

Dictionary class 48 back
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PISTE `

Dictionary class 48 Front
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KASTIKE `

Dictionary class 48 back ke
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LÄÄKE `

Dictionary class 48 front ke
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_APE `

Dictionary class 48 back pe
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RIPE `

Dictionary class 48 front pe
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LAITE `

Dictionary class 48 back te

### ` N_KÄSITE `

Dictionary class 48 front te
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KOE `

Dictionary class 48 back 0k
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PYYHE `

Dictionary class 48 front 0k
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_TARVE `

Dictionary class 48 back ve
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VIIVE `

Dictionary class 48 front ve
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KIDE `

Dictionary class 48 front de
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_JOHDE `

Dictionary class 48 back de

### ` N_LUMME `

Dictionary class 48 back me
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_MIELLE `

Dictionary class 48 front le
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VUOLLE `

Dictionary class 48 back le
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RAKENNE `

Dictionary class 48 back ne
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KIINNE `

Dictionary class 48 front ne
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_AARRE `

Dictionary class 48 back re
* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KIERRE `

Dictionary class 48 fron re
* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_HYLJE `

Dictionary class 48 front je
* kotus_av: L
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_POHJE `

Dictionary class 48 back je
* kotus_av: L
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ASKAR `

Dictionary class 49 ar
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KYYNEL `

Dictionary class 49 el
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SÄEN `

Dictionary class 49 en
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_TAIVAL `

Dictionary class 49 val
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_UDAR `

Dictionary class 49 dar
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PENGER `

Dictionary class 49 ger
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_OMMEL `

Dictionary class 49 mel
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VEMMEL `

Dictionary class 49 mel
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KINNER `

Dictionary class 49 ner
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KANNEL `

Dictionary class 49 nel
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_MANNER `

Dictionary class 49 ner
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PIENNAR `

Dictionary class 49 nar
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_AUER `

Dictionary class 49 auer
* kotus_av: T
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VERI `

Non-Dictionary class veri
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 1026
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_MERI `

Non-Dictionary class meri
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 1024
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_UROS `

Non-Dictionary class uros
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VELI `

Non-dictionary class veli
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 1007
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_AIKA `

Non-dictionary class aika
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 1009
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_POIKA `

Non-dictionary class poika
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 1010
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_AAMUYKSI `

Non-dictionary class for numeral compounds ending yksi
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 31
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_AAMUKOLME `

Non-dictionary class for numeral compounds ending kolme
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 3
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_AAMUKAHDEKSAN `

Non-dictionary class for numeral compounds ending 8
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_AAMUYHDEKSÄN `

Non-dictionary class for numeral compounds ending 9
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_AAMUKYMMENEN `

Non-dictionary class for numeral compounds ending 10
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VUOSITUHAT `

Non-dictionary class for numeral compounds ending 1000
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 46
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_AIVOT `

Dictionary class 1o plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PÖKSYT `

Dictionary class 1y plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HOUSUT `

Dictionary class 1u plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_JOUKOT `

Dictionary class 1ko plurale tantum
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_FARKUT `

Dictionary class 1ku plurale tantum
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TIEDOT `

Dictionary class 1dot plurale tantum

### ` N_TYTÖT `

Dictionary class 1töt plurale tantum
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PIDOT `

Dictionary class 1ot plurale tantum
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RAVUT `

Dictionary class 1vut plurale tantum
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_URUT `

Dictionary class 1ut plurale tantum

### ` N_RAPUT `

Dictionary class 1put plurale tantum
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KÄÄDYT `

Dictionary class 1dyt plurale tantum
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_AALLOT `

Dictionary class 1lot plurale tantum
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_OPINNOT `

Dictionary class 1not plurale tantum
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RAUNIOT `

Dictionary class 2iot plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 3
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PIPPALOT `

Dictionary class 3iot plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 2
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NEUVOTTELUT `

Dictionary class 3lut plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 2
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SÄÄNNÖT `

Dictionary class 1nöt plurale tantum
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LEHDET `

Dictionary class 7 front t~d plurale tantum
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TUNNIT `

Dictionary class 7 back t~n plurale tantum
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SUKAT `

Dictionary class xxx a front k0 plurale tantum
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KENGÄT `

Dictionary class xxx a front kg plurale tantum
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RAVET `

Dictionary class 8 plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_BÄNET `

Dictionary class 8 front plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_MARKKINAT `

Dictionary class xxx a front plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 12
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HIPAT `

Dictionary class xxx a front pp plurale tantum
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KUOPAT `

Dictionary class xxx a back p plurale tantum
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RAUDAT `

Dictionary class xxx dat plurale tantum
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TAVAT `

Dictionary class xxx vat plurale tantum
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VALLAT `

Dictionary class xxx lat plurale tantum
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VARAT `

Dictionary class xxx rrt plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_JUHLAT `

Dictionary class xxx t plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KIHARAT `

Dictionary class xxxihi t plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 11
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KÄRÄJÄT `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PAIKAT `

Dictionary class xxx kAt plurale tantum
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SILAKAT `

Dictionary class 14 kat plurale tantum
* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 14
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RINTSIKAT `

Dictionary class 14 kat2 plurale tantum

### ` N_TIETEET `

Dictionary class xxx teet plurale tantum
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_FARMARIT `

Dictionary class xxx it plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 6
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KASTANJETIT `

Dictionary class xxx tit plurale tantum
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TAUDIT `

Dictionary class xxx dit plurale tantum
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PIHDIT `

Dictionary class xxx dit front plurale tantum
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TONGIT `

Dictionary class xxx git plurale tantum
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SYÖMINGIT `

Dictionary class xxx git fornt plurale tantum
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LÄNGET `

Dictionary class xxx get plurale tantum
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LASIT `

Dictionary class xxx sit plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_BIKINIT `

Dictionary class xxx nit plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 6
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LIIVIT `

Dictionary class xxx iiiit plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HOPEAT `

Dictionary class xxx eat plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 15
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TIET `

Dictionary class 15 tiet plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 19
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TYÖT `

Dictionary class xxx työt plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 19
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VANHEMMAT `

Dictionary class xxx matt plurale tantum
* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 16
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_ITÄMAAT `

Dictionary class xxx maat plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PUUT `

Dictionary class xx puu t plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HÄÄT `

Dictionary class xxx äät plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TALKOOT `

Dictionary class xxx kooot plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 17
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SAKSET `

Dictionary class xxx sakset plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RIPSET `

Dictionary class xxx ripset plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KANNET `

Dictionary class xxx nnet plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 28
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VUODET `

Dictionary class 27 det plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 27
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TOIMET `

Dictionary class 25 t plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 25
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HÖYHENET `

Dictionary class 32 t plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 32
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ATERIMET `

Dictionary class 31 t plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KERITSIMET `

Dictionary class 31 t fr plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ANTIMET `

Dictionary class 31 nnin plurale tantum
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_HOKSOTTIMET `

Dictionary class 31 tin plurale tantum
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SYNNYTTIMET `

Dictionary class 31 tin front plurale tantum
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PUKIMET `

Dictionary class 31 puin plurale tantum
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_IKENET `

Dictionary class 31 ien plurale tantum
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 32
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LIITTOUTUNEET `

Dictionary class nut plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 47
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RAPPUSET `

Dictionary class 38 nen plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 38
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VIHKIÄISET `

Dictionary class 38 nen fornt plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 38
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VALJAAT `

Dictionary class jaat plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_TIKKAAT `

Dictionary class kaat plurale tantum
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RATTAAT `

Dictionary class taat plurale tantum
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RENKAAT `

Dictionary class gaat plurale tantum
* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RYNTÄÄT `

Dictionary class ntääaat plurale tantum
* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_HYNTTYYT `

Dictionary class ntyyaat plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 17
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RYNTTYYT `

Dictionary class ntyyt plurale tantum
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_MALTAAT `

Dictionary class ltaat plurale tantum
* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PORTAAT `

Dictionary class rtaat plurale tantum
* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SERKUKSET `

Dictionary class kset plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 39
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_YSTÄVYKSET `

Dictionary class kset fr plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 39
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_OIKEUDET `

Dictionary class sdet plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 40
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KAMPPEET `

Dictionary class mppt plurale tantum
* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_HYNTTEET `

Dictionary class ntteet plurale tantum
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PUKEET `

Dictionary class ukeet plurale tantum

### ` N_KUULOKKEET `

Dictionary class kkkeeet plurale tantum
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_VAATTEET `

Dictionary class teeeeet plurale tantum
* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PEITTEET `

Dictionary class taateee plurale tantum

### ` N_SUHTEET `

Dictionary class taad plurale tantum
* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LAUTEET `

Dictionary class daat plurale tantum

### ` N_SÄTEET `

Dictionary class daat plurale tantum

### ` N_SITEET `

Dictionary class trate plurale tantum

### ` N_TARPEET `

Dictionary class veat plurale tantum
* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_HIUTALEET `

Dictionary class leat plurale tantum
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ALKEET `

Dictionary class jeet plurale tantum
* kotus_av: L
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PERKEET `

Dictionary class jeat plurale tantum
* kotus_av: L
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_POJAT `

Dictionary class pojat plurale tantum
* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 1010
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KYNNET `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 28
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VARPAAT `


* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_INGET `


* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_JUOVAT `


* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_JYLKYT `


* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KAARRET `


* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KIRITTÄRET `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 32
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_HAIT `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KORTET `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KENTÄT `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_ROMPAAT `


* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LANNET `


* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LIPOTTARET `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 32
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LOUET `


* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LUODES `


* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LÄHDES `


* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LÄHDET `


* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_MURTEET `


* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_MERTU `


* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NIMETÖIN `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 34
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_HÄRKIN `


* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_MATEE `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 18
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: e
* grade_dir: weaken

### ` N_KYLÄNVANHIN `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 36
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_YMPÄRYSTÄ `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` N_PÖLHÄÄT `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 17
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_MATKUET `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 43
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ALTIS `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RINNET `


* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_MÄNNYT `


* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RUOPPAAT `


* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KAARET `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_HÄMET `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PÖLLÖT `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_HYÖTYY `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 17
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: y
* grade_dir: weaken

### ` N_KANKAHAT `


* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SAMMALET `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_PEIPOT `


* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_MÄTTÄÄT `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LAET `


* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RANGAT `


* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KYNNÄÄT `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_EKKE `


* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SILMÄKKEET `


* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SIUNAAMATTOMAT `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 34
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_METTE `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LINGOT `


* kotus_av: G
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VELJET `


* kotus_av: L
* pos: NOUN
* possessive: False
* kotus_tn: 1007
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SÄÄRET `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 26
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_PANKIT `


* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LUHDAT `


* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RIIPI `


* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SELENE `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 2
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_FÄNRIKIT `


* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KLUMPIT `


* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TYÖTTÖMÄT `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 34
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RÄMIÄT `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 12
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TÖLPÄT `


* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LAHDET `


* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SYLI `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 23
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RÄMEET `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_ONNET `


* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KALATOIN `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 34
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_HÄNNÄT `


* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KORVET `


* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RAPPE `


* kotus_av: B
* pos: NOUN
* possessive: False
* kotus_tn: 8
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LAMMET `


* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KOUVOT `


* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_MIEHET `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 42
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KAARROT `


* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RÄMEÄT `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 15
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VIIRRET `


* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RIMMIT `


* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TEHTAAT `


* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_EUGENE `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 2
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SELJÄT `


* kotus_av: L
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_AHDET `


* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_JÄRJESTÖT `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 2
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_JÄRVITAHDON `


* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 33
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KANAALI `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 6
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KARRAT `


* kotus_av: K
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KASTILJAT `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 13
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KITARA `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 13
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` N_KORTES `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 41
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_KORTTI `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KUMMUT `


* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KUNNAT `


* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KYDÖT `


* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_KÄRJET `


* kotus_av: L
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LAMMI `


* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LAMMIT `


* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_LENTTEE `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 17
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: e
* grade_dir: weaken

### ` N_LOMMOL `


* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 49
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LUODE `


* kotus_av: F
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_LUOLIKOT `


* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 4
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_MÄET `


* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NIEMET `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 25
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NIITUT `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_NIITYT `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_OSOITE `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RANNAT `


* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_REIÄT `


* kotus_av: D
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RIIVET `


* kotus_av: E
* pos: NOUN
* possessive: False
* kotus_tn: 7
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RIMMI `


* kotus_av: H
* pos: NOUN
* possessive: False
* kotus_tn: 5
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_RINTEET `


* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_RIUTAT `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 9
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_ROITOT `


* kotus_av: C
* pos: NOUN
* possessive: False
* kotus_tn: 1
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SAARET `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 26
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SALONTEET `


* kotus_av: J
* pos: NOUN
* possessive: False
* kotus_tn: 48
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_SUOT `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 19
* plurale_tantum: obligatory
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_SÄRKÄT `


* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 10
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_TÖLPÄKÖT `


* kotus_av: A
* pos: NOUN
* possessive: False
* kotus_tn: 4
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` N_VUOLLET `


* kotus_av: I
* pos: NOUN
* possessive: False
* kotus_tn: 44
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` N_YHTIÖT `


* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 3
* plurale_tantum: obligatory
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` NUMERAL `

Numerals are morphologically nominals, only exception to noun inflection is that they form compounds with special agreeing patterns. Syntactically and semantically numerals are clearly separate subset of nominals. Some of the numerals stem variation patterns are rare to non-existent for other nominal types. 

### ` NUM_YKSI `

Dictionary class31
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 31
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` NUM_KAKSI `

Dictionary class31 back§
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 31
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` NUM_KOLME `

Dictionary class8~5
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 1008
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` NUM_NELJÄ `

Dictionary class10
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: ä
* grade_dir: weaken

### ` NUM_VIISI `

Dictionary class27 front
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 27
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` NUM_KUUSI `

Dictionary class27 back
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 27
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` NUM_KAHDEKSAN `

Dictionary class10n
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` NUM_YHDEKSÄN `

Dictionary class10n front
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` NUM_KYMMENEN `

Dictionary class32
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 32
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` NUM_SATA `

Dictionary class9
* kotus_av: F
* pos: NUMERAL
* possessive: False
* kotus_tn: 9
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` NUM_TUHAT `

Dictionary class46
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 46
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` NUM_MILJOONA `

Dictionary class10
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 10
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: a
* grade_dir: weaken

### ` NUM_MILJARDI `

Dictionary class5
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 6
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` NUM_GOOGOL `

Dictionary class5 more

### ` NUM_PARI `

Dictionary class5 moremore
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 7
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` NUM_ENSIMMÄINEN `

Dictionary class38
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 38
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` NUM_TOINEN `

Dictionary class38 back
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 38
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` NUM_KOLMAS `

Dictionary class45
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 45
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` NUM_NELJÄS `

Dictionary class45 fron
* kotus_av: None
* pos: NUMERAL
* possessive: False
* kotus_tn: 45
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` PARTICLE `

The particles are all words that do not inflect at all.

### ` PRONOUN `

Pronouns are a closed special sub class of nouns.

### ` PUNCTUATION `

Punctuation characters are any symbols in text.

### ` VERB `

Verbs are the words that inflect in tense, mood, personal suffixes, and clitics, but verbs also have s.c. infinite inflection pattern which is basically nominal derivations.

### ` V_KAUNISTUA `

The u stems have no stem variation: Dictionary class52u
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_PUNOA `

The o stems have no stem variation: Dictionary class52o
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_SÄILÖÄ `

The ö stems have no stem variation: Dictionary class52ö
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_ÄLLISTYÄ `

The y stems have no stem variation: Dictionary class52y
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_HAUKKOA `

Dictionary class52 k~0 o
* kotus_av: A
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_NUOKKUA `

Dictionary class52 k~0 u
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KÄRKKYÄ `

Dictionary class52 k~0 y
* kotus_av: A
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_HARPPOA `

Dictionary class52 p~0 o
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_LOPPUA `

Dictionary class52 p~0 u
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_LEPPYÄ `

Dictionary class52 p~0 y
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KIVETTYÄ `

Dictionary class52 t~0 y
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_VIITTOA `

Dictionary class52 t~0 o
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_HERMOTTUA `

Dictionary class52 t~0 u
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_MÄIKYÄ `

Dictionary class52 k~0’ y
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_TAKOA `

Dictionary class52 k~0’ o
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_MAUKUA `

Dictionary class52 k~0’ u
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_ELPYÄ `

Dictionary class52 p~v y

### ` V_HIIPUA `

Dictionary class52 p~v u
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_SILPOA `

Dictionary class52 p~v o
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KIETOA `

Dictionary class52 t~d o
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_SILIYTYÄ `

Dictionary class52 t~d y
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_ROHTUA `

Dictionary class52 t~d u
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_VINKUA `

Dictionary class52 k~g u
* kotus_av: G
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_PENKOA `

Dictionary class52 k~g o
* kotus_av: G
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_TEMPOA `

Dictionary class52 p~m o
* kotus_av: H
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_AMPUA `

Dictionary class52 p~m u
* kotus_av: H
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_MIELTYÄ `

Dictionary class52 t~l y
* kotus_av: I
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_HUMALTUA `

Dictionary class52 t~l u
* kotus_av: I
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_VAKAANTUA `

Dictionary class52 t~n u
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_TYHJENTYÄ `

Dictionary class52 t~n y
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_PYÖRTYÄ `

Dictionary class52 t~r y

### ` V_VARTOA `

Dictionary class52 t~r o
* kotus_av: K
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_PUSERTUA `

Dictionary class52 t~r u
* kotus_av: K
* pos: VERB
* possessive: False
* kotus_tn: 52
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_MUTRISTAA `

Dictionary class53 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 53
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KIVISTÄÄ `

Dictionary class53 front
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 53
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_RÄPSYTTÄÄ `

Dictionary class53 front t~0
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 53
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_VIEROITTAA `

Dictionary class53 back t~0
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 53
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_PURKAA `

Dictionary class53 back k~0
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 53
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_YSKÄHTÄÄ `

Dictionary class53 front t~d
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 53
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_MOJAHTAA `

Dictionary class53 back t~d
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 53
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KYNTÄÄ `

Dictionary class53 front t~n
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 53
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_SORTAA `

Dictionary class53 back t~r
* kotus_av: K
* pos: VERB
* possessive: False
* kotus_tn: 53
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_HUUTAA `

Dictionary class54 back
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 54
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_PYYTÄÄ `

Dictionary class54 front
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 54
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_SIVALTAA `

Dictionary class54 back t~l
* kotus_av: I
* pos: VERB
* possessive: False
* kotus_tn: 54
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_VIHELTÄÄ `

Dictionary class54 front t~l
* kotus_av: I
* pos: VERB
* possessive: False
* kotus_tn: 54
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_HIVENTÄÄ `

Dictionary class54 front t~n
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 54
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_HUONONTAA `

Dictionary class54 back t~n
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 54
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KUHERTAA `

Dictionary class54 back t~r
* kotus_av: K
* pos: VERB
* possessive: False
* kotus_tn: 54
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_NÄPERTÄÄ `

Dictionary class54 front t~r
* kotus_av: K
* pos: VERB
* possessive: False
* kotus_tn: 54
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KIITÄÄ `

Dictionary class55 front
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 55
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_JOUTAA `

Dictionary class55 back
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 55
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_YLTÄÄ `

Dictionary class55 front t~l
* kotus_av: I
* pos: VERB
* possessive: False
* kotus_tn: 55
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_ENTÄÄ `

Dictionary class55 front t~n
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 55
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KASVAA `

Dictionary class56 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 56
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_VIRKKAA `

Dictionary class56 back k~0
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 56
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_TAPPAA `

Dictionary class56 back p~0
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 56
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_AUTTAA `

Dictionary class56 back t~0
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 56
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_SATAA `

Dictionary class56 back t~d
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 56
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KANTAA `

Dictionary class56 back t~n
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 56
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KAATAA `

Dictionary class57 back
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 57
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_SAARTAA `

Dictionary class57 back t~r
* kotus_av: K
* pos: VERB
* possessive: False
* kotus_tn: 57
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KYTKEÄ `

Dictionary class58 front
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 58
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_SOTKEA `

Dictionary class58 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 58
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_PUKEA `

Dictionary class58 back k~0
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 58
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_RYPEÄ `

Dictionary class58 front p~v
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 58
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_PÄTEÄ `

Dictionary class58 front t~d
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 58
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KUTEA `

Dictionary class58 back t~d
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 58
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_TUNKEA `

Dictionary class58 back k~g
* kotus_av: G
* pos: VERB
* possessive: False
* kotus_tn: 58
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_POLKEA `

Dictionary class58 back k~j
* kotus_av: L
* pos: VERB
* possessive: False
* kotus_tn: 58
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_SÄRKEÄ `

Dictionary class58 front k~j
* kotus_av: L
* pos: VERB
* possessive: False
* kotus_tn: 58
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_TUNTEA `

Dictionary class59
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 59
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_LÄHTEÄ `

Dictionary class60
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 60
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KOSIA `

Dictionary class61 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_RYSKIÄ `

Dictionary class61 front
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KUKKIA `

Dictionary class61 back k~0
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_SÖRKKIÄ `

Dictionary class61 front k~0
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KALPPIA `

Dictionary class61 back p~0
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_HYPPIÄ `

Dictionary class61 front p~0
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_MOITTIA `

Dictionary class61 back t~0
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_MIETTIÄ `

Dictionary class61 front t~0
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_RIIPIÄ `

Dictionary class61 front p~v
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_RAAPIA `

Dictionary class61 back p~v
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_AHNEHTIA `

Dictionary class61 back t~d
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_EHTIÄ `

Dictionary class61 front t~d
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_MÖNKIÄ `

Dictionary class61 front k~g
* kotus_av: G
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_ONKIA `

Dictionary class61 back k~g
* kotus_av: G
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_TYMPIÄ `

Dictionary class61 frontp~m
* kotus_av: H
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KONTIA `

Dictionary class61 back t~n
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_HYLKIÄ `

Dictionary class61 back k~j
* kotus_av: L
* pos: VERB
* possessive: False
* kotus_tn: 61
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_KOPIOIDA `

Dictionary class62 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 62
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_ÖYKKÄRÖIDÄ `

Dictionary class62 front
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 62
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_SAADA `

Dictionary class63 a
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 63
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_MYYDÄ `

Dictionary class63 y
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 63
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_JÄÄDÄ `

Dictionary class63 ä
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 63
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_VIEDÄ `

Dictionary class64 ie
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 64
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_TUODA `

Dictionary class64 uo
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 64
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_SYÖDÄ `

Dictionary class64 yö In past and conditional forms of käydä, the glide before suffix is marked even in normative orthography.
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 64
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KÄYDÄ `

Dictionary class65
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 65
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_MARISTA `

Dictionary class66 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 66
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_ÄRISTÄ `

Dictionary class66 front
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 66
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_HÄVÄISTÄ `

Dictionary class66 front v p
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 66
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_VAVISTA `

Dictionary class66 back v~p
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 66
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_RANGAISTA `

Dictionary class66 back k~g
* kotus_av: G
* pos: VERB
* possessive: False
* kotus_tn: 66
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_SURRA `

Dictionary class67 back r
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_PIERRÄ `

Dictionary class67 front r
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_PANNA `

Dictionary class67 back n
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_MENNÄ `

Dictionary class67 front n
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_VASTAILLA `

Dictionary class67 back l

### ` V_ÄKSYILLÄ `

Dictionary class67 frot l
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LEIKELLÄ `

Dictionary class67 front l 0k
* kotus_av: A
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_NAKELLA `

Dictionary class67 back l 0k
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_TAPELLA `

Dictionary class67 back l 0p
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_HYPELLÄ `

Dictionary class67 front l 0p
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_SULATELLA `

Dictionary class67 back l 0t
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_HERÄTELLÄ `

Dictionary class67 front l 0t
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_TIPAHDELLA `

Dictionary class67 back l d~t
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_SÄPSÄHDELLÄ `

Dictionary class67 front l d~t
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_OMMELLA `

Dictionary class67 back l m~p
* kotus_av: H
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_VAELLELLA `

Dictionary class67 back l l~t
* kotus_av: I
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KIILLELLÄ `

Dictionary class67 frpnt l l~t
* kotus_av: I
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KOMENNELLA `

Dictionary class67 back l n~t
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KÄÄNNELLÄ `

Dictionary class67 front l n~t
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_NAKERRELLA `

Dictionary class67 back l r~t
* kotus_av: K
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KIHERRELLÄ `

Dictionary class67 front l r~t
* kotus_av: K
* pos: VERB
* possessive: False
* kotus_tn: 67
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_ISÄNNÖIDÄ `

Dictionary class68 front
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 68
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_MELLAKOIDA `

Dictionary class68 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 68
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_PALKITA `

Dictionary class69 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 69
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_MERKITÄ `

Dictionary class69 front
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 69
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_JUOSTA `

Dictionary class70 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 70
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_PIESTÄ `

Dictionary class70 front
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 70
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_NÄHDÄ `

Dictionary class71
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 71
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KARHETA `

Dictionary class72 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_VÄHETÄ `

Dictionary class72 rfont
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_NIUKETA `

Dictionary class72 back 0~k
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_JYRKETÄ `

Dictionary class72 front 0~k
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_HAPATA `

Dictionary class72 back 0~p
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_SUPETA `

Dictionary class72 front 0~p
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_TYLPETÄ `

Dictionary class72 front 0~p
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_HELPOTA `

Dictionary class72 back 0~p o
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LOITOTA `

Dictionary class72 back 0~t
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_ULOTA `

Dictionary class72 back 0~k o
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KAVETA `

Dictionary class72 back v~p
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_MÄDÄTÄ `

Dictionary class72 front d~t
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LEUDOTA `

Dictionary class72 back d~t
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_PIDETÄ `

Dictionary class72 front d~t e
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LÄMMETÄ `

Dictionary class72 front m~p 
* kotus_av: H
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KIINNETÄ `

Dictionary class72 front n~t
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 72
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_JULJETA `

Dictionary class72 back j~k

### ` V_ARVATA `

Dictionary class73 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_YNNÄTÄ `

Dictionary class73 front
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_MORKATA `

Dictionary class73 back 0~k
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_YÖKÄTÄ `

Dictionary class73 front 0~k
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_SIEPATA `

Dictionary class73 back 0~p
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_VÄLPÄTÄ `

Dictionary class73 frot 0~p
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LUNTATA `

Dictionary class73 back 0~t
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LÄNTÄTÄ `

Dictionary class73 front 0~t
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KAIVATA `

Dictionary class73 back v~p
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LEVÄTÄ `

Dictionary class73 front v~p
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_JAHDATA `

Dictionary class73 back d~r
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_TÄHDÄTÄ `

Dictionary class73 front d~t
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_VONGATA `

Dictionary class73 back g~k
* kotus_av: G
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_VÄNGÄTÄ `

Dictionary class73 front g~k
* kotus_av: G
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_TEMMATA `

Dictionary class73 back m~p
* kotus_av: H
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_MULLATA `

Dictionary class73 back l~t
* kotus_av: I
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_SUUNNATA `

Dictionary class73 back n~t
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_RYNNÄTÄ `

Dictionary class73 front n~t
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_VIRRATA `

Dictionary class73 back r~t

### ` V_HYLJÄTÄ `

Dictionary class73 front j~k
* kotus_av: L
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_DIGATA `

Dictionary class73 back 0~g
* kotus_av: O
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LOBATA `

Dictionary class73 back 0~b
* kotus_av: P
* pos: VERB
* possessive: False
* kotus_tn: 73
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KARHUTA `

Dictionary class74 back 
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_TÄHYTÄ `

Dictionary class74 front 
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KAIKOTA `

Dictionary class74 back 0~k 
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_POIKETA `

Dictionary class74 back 0~k e 
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KERETÄ `

Dictionary class74 front 0~k e 
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KOUKUTA `

Dictionary class74 front 0~k u 
* kotus_av: A
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_PULPUTA `

Dictionary class74 back 0~p 
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_UPOTA `

Dictionary class74 back 0~p o 
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LOTOTA `

Dictionary class74 back 0~to
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LUUTUTA `

Dictionary class74 back 0~tu
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KIVUTA `

Dictionary class74 back v~p 
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KORVETA `

Dictionary class74 back v~pe
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_REVETÄ `

Dictionary class74 front v~pe
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KIRVOTA `

Dictionary class74 back v~po
* kotus_av: E
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KADOTA `

Dictionary class74 back d~t 

### ` V_TODETA `

Dictionary class74 back t~de
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_VYYHDETÄ `

Dictionary class74 front t~de
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LIIDUTA `

Dictionary class74 back d~tu
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_TUNGETA `

Dictionary class74 back g~ke
* kotus_av: G
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_PINGOTA `

Dictionary class74 back g~ko
* kotus_av: G
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_ÄNGETÄ `

Dictionary class74 front g~ke 
* kotus_av: G
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KUMMUTA `

Dictionary class74 back m~p 
* kotus_av: H
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KAMMETA `

Dictionary class74 back p~mu
* kotus_av: H
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_SAMMOTA `

Dictionary class74 back p~mu
* kotus_av: H
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_INNOTA `

Dictionary class74 back t~no
* kotus_av: J
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_IRROTA `

Dictionary class74 back t~to
* kotus_av: K
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_HALJETA `

Dictionary class74 back j~ke
* kotus_av: L
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_ILJETÄ `

Dictionary class74 front j~k 
* kotus_av: L
* pos: VERB
* possessive: False
* kotus_tn: 74
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_MYRSKYTÄ `

Dictionary class75 front

### ` V_LASSOTA `

Dictionary class75 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 75
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_SELVITÄ `

Dictionary class75 itä
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 75
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_RYÖPYTÄ `

Dictionary class75 pytä
* kotus_av: B
* pos: VERB
* possessive: False
* kotus_tn: 75
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_PEITOTA `

Dictionary class75 tota
* kotus_av: C
* pos: VERB
* possessive: False
* kotus_tn: 75
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_KERITÄ `

Dictionary class75 itä
* kotus_av: D
* pos: VERB
* possessive: False
* kotus_tn: 75
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_MUODOTA `

Dictionary class75 dota
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 75
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_LÄMMITÄ `

Dictionary class75 mitä
* kotus_av: H
* pos: VERB
* possessive: False
* kotus_tn: 75
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_AALLOTA `

Dictionary class75 lota
* kotus_av: I
* pos: VERB
* possessive: False
* kotus_tn: 75
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_HELLITÄ `

Dictionary class75 litä
* kotus_av: I
* pos: VERB
* possessive: False
* kotus_tn: 75
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: strengthen

### ` V_TAITAA `

Dictionary class76 back
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 76
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_TIETÄÄ `

Dictionary class76 front
* kotus_av: F
* pos: VERB
* possessive: False
* kotus_tn: 76
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_VIPAJAA `

Dictionary class77 back 
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 77
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_HELÄJÄÄ `

Dictionary class77 front
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 77
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_RAIKAA `

Dictionary class78 back
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 78
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_ÄHKÄÄ `

Dictionary class78 front
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 78
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` V_OLLA `

The verb olla has very peculiar and heteroclitic inflection with lot of common short forms in standard spoken Finnish
* kotus_av: None
* pos: VERB
* possessive: False
* kotus_tn: 1067
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: weaken

### ` ACRONYM `

Acronyms are shortenings inflected using a colon, followed by the inflectional endings.

### ` ACRO_YKSI `


* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_KAKSI `


* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_KOLME `

The acronyms ending in digit 3 pronounced as number
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_NELJÄ `


* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_VIISI `

The acronyms ending in digit 5 pronounced as number
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_KUUSI `


* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_SEITSEMÄN `


* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_KAHDEKSAN `


* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_YHDEKSÄN `


* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_AA `

acronyms ending in 'a' pronounced as a letter
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: back
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_EE `

acronyms ending in 'b', 'c', 'd', 'e', 'g', 'p', 'v', 'w' or 't' pronounced as a letter
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_II `

Acronyms that end in 'j' or 'i' pronoynced as letter
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_OO `

Acronyms that end in 'h', 'k' or 'o' that is pronounced as a letter
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_UU `

Acronyms that end in 'q', or 'u' pronounced as a letter
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_ÄKS `

Acronym that ends in 'f', 'l', 'm', 'n', 'r', 's', 'š' or 'x' pronounced as a letter
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_YY `

Acronym that ends in 'y' pronounced as letter
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_ZET `

Acronyms that end in 'z' pronounced as letter
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_ÄÄ `

Acronyms that end in 'ä' pronounced as letter
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_ÖÖ `

Acronyms that end in 'ö' pronounced as letter
* kotus_av: None
* pos: ACRONYM
* possessive: False
* kotus_tn: 0
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` ACRO_FRONT_POSS `

acronym's possessives, e.g. ':ni', to optional front clitics

### ` ACRO_BACK_POSS `

acronym's possessives, e.g. ':ni', to optional back clitics

### ` ACRO_BACK_POSS_AN `

acronym's possessives including ':an'

### ` ACRO_BACK_POSS_EN `

acronym's possessives including ':en', to back clitics

### ` ACRO_FRONT_POSS_EN `

acronym's possessives including ':en', to front clitics

### ` ACRO_FRONT_POSS_ÄN `

acronym's possessives including ':än'

### ` ACRO_BACK_CLIT `

acronym's back clitics, e.g. ':ko'

### ` ACRO_FRONT_CLIT `

acronym's back clitics, e.g. ':kö'

### ` ACRO_BACK_CLIT_OPT `

acronym's back clitics optionally

### ` ACRO_FRONT_CLIT_OPT `

acronym's front clitics optionall

### ` ACRO_BACK_POSS_AN_OPT `

acronym's back possessive incl. ':an' optionally

### ` ACRO_FRONT_POSS_ÄN_OPT `

acronym's front possessive incl. 'än' optionally

### ` ACRO_BACK_POSS_EN_OPT `

acronym's back possessive incl. 'en' optionally

### ` ACRO_FRONT_POSS_EN_OPT `

acronym's front possessive incl. 'en' optionally

### ` ACRO_BACK_POSS_CLIT_OPT `

acronym's back possessive or clitic optionally

### ` ACRO_FRONT_POSS_CLIT_OPT `

acronym's front possessive or clitic optionally

### ` ACRO_BACK_POSS_EN_OBL `

acronym's back possessive incl. 'en' obligatorily

### ` ACRO_FRONT_POSS_EN_OBL `

acronym's front possessive incl. 'en' obligatorily

### ` ACRO_COMPOUND `

acronym compounding with hyphen

### ` A_BACK_SUPERLATIVE `

The superlative derivation is formed by in suffix, which creates a new adjective baseform. This baseform is handled separately to avoid double superlatives.

### ` A_FRONT_SUPERLATIVE `

The superlative derivation is formed by in suffix, which creates a new adjective baseform. This baseform is handled separately to avoid double superlatives.

### ` A_BACK_COMPARATIVE `

The comparative derivation is formed by mpi suffix, which creates a new adjective baseform. This adjective is handled separately to avoid double comparative forms.

### ` A_FRONT_COMPARATIVE `

The comparative derivation is formed by mpi suffix, which creates a new adjective baseform. This adjective is handled separately to avoid double comparative forms.

### ` A_BACK_COMPARATIVE_STEMS `

This inflectional part attached to adjective comparative stems to avoid circularity in comparative derivations

### ` A_FRONT_COMPARATIVE_STEMS `

This inflectional part attached to adjective comparative stems to avoid circularity in comparative derivations

### ` A_BACK_SUPERLATIVE_STEMS `

This inflectional part is attached to adjective superlative stems to avoid circularity in superlative derivations

### ` A_FRONT_SUPERLATIVE_STEMS `

This inflectional part is attached to adjective superlative stems to avoid circularity in superlative derivations

### ` A_BACK_NOMINATIVE `

Adjective back nominative

### ` A_FRONT_NOMINATIVE `

Adjective front nominative

### ` A_BACK_PLNOM_CLIT `

Adjective back plural nominative

### ` A_FRONT_PLNOM_CLIT `

Adjective front plural nominative

### ` A_BACK_WEAK_SINGULARS `

Adjective back weak singular suffixes

### ` A_FRONT_WEAK_SINGULARS `

Adjective front weak singular suffixes

### ` A_BACK_STRONG_SINGULARS `

Adjective back strong singular suffixes

### ` A_FRONT_STRONG_SINGULARS `

Adjective front strong singular suffixes

### ` A_BACK_WEAK_PLURALS `

Adjective back weak plural suffixes

### ` A_FRONT_WEAK_PLURALS `

Adjective front weak plural suffixes

### ` A_FRONT_STRONG_PLURALS `

Adjective front strong plural suffixes

### ` A_BACK_STRONG_PLURALS `

Adjective back strong plural suffixes

### ` A_BACK_PARTITIVE_A `

Adjective partitive suffix a

### ` A_FRONT_PARTITIVE_Ä `

Adjective partitive suffix ä

### ` A_BACK_PARTITIVE_A_AN `

Adjective partitive suffix a w/ possessive aan

### ` A_FRONT_PARTITIVE_Ä_ÄN `

Adjective partitive suffix ä w/ possessive ään

### ` A_BACK_PARTITIVE_TA `

Adjective partitive suffix ta

### ` A_FRONT_PARTITIVE_TÄ `

Adjective partitive suffix tä

### ` A_BACK_ILLATIVE_HAN `

Adjective illative suffix han

### ` A_FRONT_ILLATIVE_HIN `

Adjective illative suffix hin

### ` A_BACK_ILLATIVE_HUN `

Adjective illative suffix hun

### ` A_FRONT_ILLATIVE_HYN `

Adjective illative suffix hyn

### ` A_FRONT_ILLATIVE_HÄN `

Adjective illative suffix hän

### ` A_BACK_ILLATIVE_SEEN `

Adjective illative suffix seen to back clitics

### ` A_FRONT_ILLATIVE_SEEN `

Adjective illative suffix seen to front clitics

### ` A_BACK_ILLATIVE_AN `

Adjective illative suffix an

### ` A_BACK_ILLATIVE_EN `

Adjective illative suffix en to back clitics

### ` A_FRONT_ILLATIVE_EN `

Adjective illative suffix en to front clitics

### ` A_BACK_ILLATIVE_IN `

Adjective illative suffix in to back clitics

### ` A_FRONT_ILLATIVE_IN `

Adjective illative suffix in to front clitics

### ` A_BACK_ILLATIVE_ON `

Adjective illative suffix on

### ` A_BACK_ILLATIVE_UN `

Adjective illative suffix un

### ` A_FRONT_ILLATIVE_YN `

Adjective illative suffix yn

### ` A_FRONT_ILLATIVE_ÄN `

Adjective illative suffix än

### ` A_FRONT_ILLATIVE_ÖN `

Adjective illative suffix ön

### ` A_BACK_PARTITIVE_IA `

Adjective partitive suffix ia

### ` A_FRONT_PARTITIVE_IÄ `

Adjective partitive suffix iä

### ` A_BACK_PARTITIVE_ITA `

Adjective partitive suffix ita

### ` A_FRONT_PARTITIVE_ITÄ `

Adjective partitive suffix itä

### ` A_BACK_PARTITIVE_JA `

Adjective partitive suffix 

### ` A_FRONT_PARTITIVE_JÄ `

Adjective partitive suffix 

### ` A_BACK_GENITIVE_IDEN `

Adjective genitive suffix 

### ` A_FRONT_GENITIVE_IDEN `

Adjective genitive suffix 

### ` A_BACK_GENITIVE_IEN `

Adjective genitive suffix 

### ` A_FRONT_GENITIVE_IEN `

Adjective genitive suffix 

### ` A_BACK_GENITIVE_ITTEN `

Adjective genitive suffix 

### ` A_FRONT_GENITIVE_ITTEN `

Adjective genitive suffix 

### ` A_BACK_GENITIVE_JEN `

Adjective genitive suffix 

### ` A_FRONT_GENITIVE_JEN `

Adjective genitive suffix 

### ` A_BACK_GENITIVE_TEN `

Adjective genitive suffix 

### ` A_FRONT_GENITIVE_TEN `

Adjective genitive suffix 

### ` A_BACK_GENITIVE_IN `

Adjective genitive suffix 

### ` A_FRONT_GENITIVE_IN `

Adjective genitive suffix 

### ` A_BACK_ILLATIVE_IHIN `

Adjective genitive suffix 

### ` A_FRONT_ILLATIVE_IHIN `

Adjective genitive suffix 

### ` A_BACK_ILLATIVE_IIN `

Adjective genitive suffix 

### ` A_FRONT_ILLATIVE_IIN `

Adjective genitive suffix 

### ` A_BACK_ILLATIVE_ISIIN `

Adjective genitive suffix 

### ` A_FRONT_ILLATIVE_ISIIN `

Adjective genitive suffix 

### ` A_FRONT_POSS `

Adjective possessive suffixes 

### ` A_BACK_POSS `

Adjective possessive suffixes 

### ` A_BACK_POSS_AN `

Adjective possessive suffixes 

### ` A_BACK_POSS_EN `

Adjective possessive suffixes 

### ` A_FRONT_POSS_EN `

Adjective possessive suffixes 

### ` A_FRONT_POSS_ÄN `

Adjective possessive suffixes 

### ` A_BACK_CLIT `

Adjective possessive clitics 

### ` A_FRONT_CLIT `

Adjective possessive clitics 

### ` A_BACK_CLIT_OPT `

Adjective possessive clitics optionally 

### ` A_FRONT_CLIT_OPT `

Adjective possessive clitics optionally 

### ` A_BACK_SINGULARS `

Adjective back singulars

### ` A_FRONT_SINGULARS `

Adjective front singulars

### ` A_BACK_PLURALS `

Adjective back plurals

### ` A_FRONT_PLURALS `

Adjective front plurals

### ` A_BACK_POSS_AN_CLIT_OPT `

Adjective possessives with an suffix and clitics optionally

### ` A_FRONT_POSS_ÄN_CLIT_OPT `

Adjective possessives with än suffix and clitics optionally

### ` A_BACK_POSS_EN_CLIT_OPT `

Adjective possessives with en suffix and back clitics optionally

### ` A_FRONT_POSS_EN_CLIT_OPT `

Adjective possessives with en suffix and front clitics optionally

### ` A_BACK_POSS_CLIT_OPT `

Adjective back possessives and clitics optionally

### ` A_FRONT_POSS_CLIT_OPT `

Adjective front possessives and clitics optionally

### ` A_BACK_POSS_EN_OBL `

Adjective possessives with en and back clitics optionally

### ` A_FRONT_POSS_EN_OBL `

Adjective possessives with en and front clitics optionally

### ` DIGITS `

Digit strings inflect with colons, lot like abbreviations.

### ` DIGITS_YKSI `

The digit strings ending in digit 1 pronounced as number

### ` DIGITS_KAKSI `

The digit strings ending in digit 2 pronounced as number

### ` DIGITS_KOLME `

The digit strings ending in digit 3 pronounced as number

### ` DIGITS_NELJÄ `

The digit strings ending in digit 4 pronounced as number

### ` DIGITS_VIISI `

The digit strings ending in digit 5 pronounced as number

### ` DIGITS_KUUSI `

The digit strings ending in digit 6 pronounced as number

### ` DIGITS_SEITSEMÄN `

The digit strings ending in digit 7 pronounced as number

### ` DIGITS_KAHDEKSAN `

The digit strings ending in digit 8 pronounced as number

### ` DIGITS_YHDEKSÄN `

The digit strings ending in digit 9 pronounced as number

### ` DIGITS_NOLLA `

The digit strings ending in digit 0 pronounced as number

### ` DIGITS_KYMMENEN `

The digit string ending in 0 pronounced as tens

### ` DIGITS_SATA `

The digit string ending in 00 pronounced as hundreds

### ` DIGITS_TUHAT `

The digit string ending in 000 pronounced as thousands

### ` DIGITS_MILJOONA `

The digit string ending in 0's pronounced as millions

### ` DIGITS_MILJARDI `

The digit string ending in 0's pronounced as milliards

### ` DIGITS_ENSIMMÄINEN `

The digit string ending in 1. pronounced as first

### ` DIGITS_TOINEN `

The digit string ending in 2. pronounced as second

### ` DIGITS_KOLMAS `

The digit string ending in 3, 6, 8, 00 or 2 pronounced as ordinal

### ` DIGITS_NELJÄS `

The digit string ending in 4, 5, 7, 9, 0, or 1. pronounced as ordinal

### ` DIGITS_ROMANS_TOINEN `

The roman digit string ending in II, III, VI, VIII, C, L or M

### ` DIGITS_ROMANS_ENSIMMÄINEN `

The roman digit string ending in I, IV, V, VII, IX, X or 

### ` DIGITS_FRONT_POSS `

Digits possessives after :

### ` DIGITS_BACK_POSS `

Digits possessives after :

### ` DIGITS_BACK_POSS_AN `

Digits possessives after : with an

### ` DIGITS_BACK_POSS_EN `

Digits possessives after : with en to back clitics

### ` DIGITS_FRONT_POSS_EN `

Digits possessives after : with en to front clitics

### ` DIGITS_FRONT_POSS_ÄN `

Digits possessives after : with än

### ` DIGITS_BACK_CLIT `

Digits clitics after : or possessive

### ` DIGITS_FRONT_CLIT `

Digits clitics after : or possessive

### ` DIGITS_BACK_CLIT_OPT `

Digits clitics after : or possessive optionally

### ` DIGITS_FRONT_CLIT_OPT `

Digits clitics after : or possessive optionally

### ` DIGITS_BACK_POSS_AN_OPT `

Digits possessives after : optionally

### ` DIGITS_FRONT_POSS_ÄN_OPT `

Digits possessives after : optionally

### ` DIGITS_BACK_POSS_EN_OPT `

Digits possessives after : optionally

### ` DIGITS_FRONT_POSS_EN_OPT `

Digits possessives after : optionally

### ` DIGITS_BACK_POSS_OPT `

Digits possessives after : optionally

### ` DIGITS_FRONT_POSS_OPT `

Digits possessives after : optionally

### ` DIGITS_BACK_POSS_AN_OBL `

Digits possessives after : obligatorily

### ` DIGITS_BACK_POSS_EN_OBL `

Digits possessives after : obligatorily

### ` DIGITS_FRONT_POSS_EN_OBL `

Digits possessives after : obligatorily

### ` DIGITS_FRONT_POSS_ÄN_OBL `

Digits possessives after : obligatorily

### ` DIGITS_COMPOUND `

Digits compounding with hyphen

### ` N_BACK_NOMINATIVE `

Noun singular nominative to back possessives and clitics

### ` N_FRONT_NOMINATIVE `

Noun singular nominative to front possessives and clitis

### ` N_BACK_PLNOM_CLIT `

The plural nominative attaches to singular stem. For plural words it is also the form that is used for dictionary lookups

### ` N_FRONT_PLNOM_CLIT `

The plural nominative attaches to singular stem. For plural words it is also the form that is used for dictionary lookups

### ` N_BACK_WEAK_SINGULARS `

Noun back weak singular suffixes

### ` N_FRONT_WEAK_SINGULARS `

Noun front weak singular suffixes

### ` N_BACK_STRONG_SINGULARS `

Noun back strong singular suffixes

### ` N_FRONT_STRONG_SINGULARS `

Noun front strong singular suffixes

### ` N_BACK_WEAK_PLURALS `

Noun back weak pluar suffixes

### ` N_FRONT_WEAK_PLURALS `

Noun front weak plural suffixes

### ` N_BACK_STRONG_PLURALS `

Noun back strong plural suffixes

### ` N_FRONT_STRONG_PLURALS `

Noun front strong plural suffixes

### ` N_BACK_PARTITIVE_A `

Noun partitive a suffix

### ` N_FRONT_PARTITIVE_Ä `

Noun partitive ä suffix

### ` N_BACK_PARTITIVE_A_AN `

Noun partitive a suffix with aan possessive

### ` N_FRONT_PARTITIVE_Ä_ÄN `

Noun partitive ä suffix with ään possessive

### ` N_BACK_PARTITIVE_TA `

Noun partitive ta suffix

### ` N_FRONT_PARTITIVE_TÄ `

Noun partitive tä suffix

### ` N_BACK_ILLATIVE_HAN `

Noun illative han suffix

### ` N_BACK_ILLATIVE_HEN `

Noun illative hen suffix to back possessives

### ` N_FRONT_ILLATIVE_HEN `

Noun illative hen suffix to front possessives

### ` N_BACK_ILLATIVE_HIN `

Noun illative hin suffix to back possessives

### ` N_FRONT_ILLATIVE_HIN `

Noun hin suffix to front possessives

### ` N_BACK_ILLATIVE_HON `

Noun illative hon suffix

### ` N_BACK_ILLATIVE_HUN `

Noun illative hun suffix

### ` N_FRONT_ILLATIVE_HYN `

Noun illative hyn suffix

### ` N_FRONT_ILLATIVE_HÄN `

Noun illative hän suffix

### ` N_FRONT_ILLATIVE_HÖN `

Noun illative hön suffix

### ` N_BACK_ILLATIVE_AN `

Noun illative an suffix

### ` N_BACK_ILLATIVE_EN `

Noun illative en suffix to back possessives

### ` N_FRONT_ILLATIVE_EN `

Noun illative en suffix to front possessives

### ` N_BACK_ILLATIVE_IN `

Noun illative in suffix to back possessives

### ` N_FRONT_ILLATIVE_IN `

Noun illative in suffix to front possessives

### ` N_BACK_ILLATIVE_ON `

Noun illative on suffix to back possessives

### ` N_BACK_ILLATIVE_UN `

Noun illative un suffix

### ` N_FRONT_ILLATIVE_YN `

Noun illative yn suffix

### ` N_FRONT_ILLATIVE_ÄN `

Noun illative än suffix

### ` N_FRONT_ILLATIVE_ÖN `

Noun illative suffix

### ` N_BACK_ILLATIVE_SEEN `

Noun illative seen suffix to back possessives

### ` N_FRONT_ILLATIVE_SEEN `

Noun illative seen suffix to front possessives

### ` N_BACK_GENITIVE_IDEN `

Noun genitive iden suffix to possessives

### ` N_FRONT_GENITIVE_IDEN `

Noun genitive iden suffix to possessives

### ` N_BACK_GENITIVE_ITTEN `

Noun genitive itten suffix to possessives

### ` N_FRONT_GENITIVE_ITTEN `

Noun genitive itten suffix to possessives

### ` N_BACK_GENITIVE_IEN `

Noun genitive ien suffix to possessives

### ` N_FRONT_GENITIVE_IEN `

Noun genitive ien suffix to possessives

### ` N_BACK_GENITIVE_JEN `

Noun genitive jen suffix to possessives

### ` N_FRONT_GENITIVE_JEN `

Noun genitive jen suffix to possessives

### ` N_BACK_GENITIVE_TEN `

Noun genitive ten suffix to back possessives

### ` N_FRONT_GENITIVE_TEN `

Noun genitive ten suffix to front possessives

### ` N_BACK_GENITIVE_IN `

Noun genitive in suffix to back possessives

### ` N_FRONT_GENITIVE_IN `

Noun genitive in suffix to front possessives

### ` N_BACK_PARTITIVE_IA `

Noun partitive ia suffix 

### ` N_FRONT_PARTITIVE_IÄ `

Noun partitive iä suffix

### ` N_BACK_PARTITIVE_ITA `

Noun partitive ita suffix

### ` N_FRONT_PARTITIVE_ITÄ `

Noun partitive itä suffix

### ` N_BACK_PARTITIVE_JA `

Noun partitive ja suffix

### ` N_FRONT_PARTITIVE_JÄ `

Noun partitive jä suffix

### ` N_BACK_ILLATIVE_IHIN `

Noun illative ihin suffix to back possessives

### ` N_FRONT_ILLATIVE_IHIN `

Noun illative ihin suffix to front possessives

### ` N_BACK_ILLATIVE_IIN `

Noun illative iin suffix to back possessives

### ` N_FRONT_ILLATIVE_IIN `

Noun illative iin suffix to front possessives

### ` N_BACK_ILLATIVE_ISIIN `

Noun illative isiin suffix to back possessives

### ` N_FRONT_ILLATIVE_ISIIN `

Noun illative isiin suffix to front possessives

### ` N_BACK_POSS `

Noun possessives

### ` N_FRONT_POSS `

Noun possessives

### ` N_BACK_POSS_AN `

Noun possessives with aan

### ` N_BACK_POSS_EN `

Noun possessives with een to back clitics

### ` N_FRONT_POSS_EN `

Noun possessives with een to front clitics

### ` N_FRONT_POSS_ÄN `

Noun possessives with ään

### ` N_BACK_CLIT `

Noun clitics

### ` N_FRONT_CLIT `

Noun clitics

### ` N_BACK_CLIT_OPT `

Noun clitics optionally

### ` N_FRONT_CLIT_OPT `

Noun clitics optionally

### ` N_BACK_SINGULARS `

Noun back suffixes

### ` N_FRONT_SINGULARS `

Noun front suffixes

### ` N_FRONT_PLURALS `

Noun front suffixes

### ` N_BACK_PLURALS `

Noun back suffixes

### ` N_BACK_POSS_AN_OPT `

Noun possessives with aan optionally

### ` N_FRONT_POSS_ÄN_OPT `

Noun possessives with ään optionally

### ` N_BACK_POSS_EN_OPT `

Noun possessives with een to back clitics optionally

### ` N_FRONT_POSS_EN_OPT `

Noun possessives with een to front clitics optionally

### ` N_BACK_POSS_OPT `

Noun possessives optionally

### ` N_FRONT_POSS_OPT `

Noun possessives optionally

### ` N_BACK_POSS_EN_OBL `

Noun possessives obligatorily

### ` N_FRONT_POSS_EN_OBL `

Noun possessives obligatorily

### ` N_COMPOUND_0 `

Noun compounds without linking element

### ` N_COMPOUND_N `

Noun compounds via singular genitive n

### ` N_COMPOUND_IEN `

Noun compounds via plural genitive ien

### ` N_COMPOUND_IDEN `

Noun compounds via plural genitive itten

### ` N_COMPOUND_IN `

Noun compounds via plural genitive in

### ` N_COMPOUND_ITTEN `

Noun compounds via plural genitive itten

### ` N_COMPOUND_JEN `

Noun compounds via plural genitive jen

### ` N_COMPOUND_TEN `

Noun compounds via plural genitive ten

### ` N_COMPOUND_S `

Noun compounds via linking compositive s

### ` N_COMPOUND `

Noun compounding optional hyphen
* kotus_av: None
* pos: NOUN
* possessive: False
* kotus_tn: 99
* plurale_tantum: False
* clitics: False
* harmony: front
* stem_diphthong: None
* stem_vowel: None
* grade_dir: False

### ` NUM_BACK_NOMINATIVE `

Numeral singular nominative to back possessives

### ` NUM_FRONT_NOMINATIVE `

Numeral singular nominative to front possessives

### ` NUM_BACK_PLNOM_CLIT `

Numeral plural nominative to back possessives

### ` NUM_FRONT_PLNOM_CLIT `

Numeral plural nominative to front possessives

### ` NUM_BACK_WEAK_SINGULARS `

Numeral weak back singular suffixes

### ` NUM_FRONT_WEAK_SINGULARS `

Numeral weak front singular suffixes

### ` NUM_BACK_STRONG_SINGULARS `

Numeral strong back singular suffixes

### ` NUM_FRONT_STRONG_SINGULARS `

Numeral strong front singular suffixes

### ` NUM_BACK_WEAK_PLURALS `

Numeral weak back plural suffixes

### ` NUM_FRONT_WEAK_PLURALS `

Numeral weak front plural suffixes

### ` NUM_FRONT_STRONG_PLURALS `

Numeral strong front plural suffixes

### ` NUM_BACK_STRONG_PLURALS `

Numeral strong back plural suffixes

### ` NUM_BACK_PARTITIVE_A `

Numeral partitive suffix a

### ` NUM_FRONT_PARTITIVE_Ä `

Numeral partitive suffix ä

### ` NUM_BACK_PARTITIVE_A_AN `

Numeral partitive suffix a with aan possessive

### ` NUM_BACK_PARTITIVE_TA `

Numeral partitive suffix ta

### ` NUM_FRONT_PARTITIVE_TÄ `

Numeral partitive suffix tä

### ` NUM_BACK_ILLATIVE_AN `

Numeral illative suffix an

### ` NUM_BACK_ILLATIVE_EN `

Numeral illative suffix en with back possessives

### ` NUM_FRONT_ILLATIVE_EN `

Numeral illative suffix en with front possessives

### ` NUM_BACK_ILLATIVE_IN `

Numeral illative suffix in with back possessives

### ` NUM_FRONT_ILLATIVE_ÄN `

Numeral illative suffix än

### ` NUM_BACK_PARTITIVE_IA `

Numeral partitive suffix ia

### ` NUM_FRONT_PARTITIVE_IÄ `

Numeral partitive suffix iä

### ` NUM_BACK_PARTITIVE_JA `

Numeral partitive suffix ja

### ` NUM_BACK_GENITIVE_IEN `

Numeral genitive suffix ien with back possessives

### ` NUM_FRONT_GENITIVE_IEN `

Numeral genitive suffix ien with front possessives

### ` NUM_BACK_GENITIVE_JEN `

Numeral genitive suffix jen

### ` NUM_BACK_GENITIVE_TEN `

Numeral genitive suffix ten with back possessives

### ` NUM_FRONT_GENITIVE_TEN `

Numeral genitive suffix ten with front possessives

### ` NUM_BACK_GENITIVE_IN `

Numeral genitive suffix in with back possessives

### ` NUM_FRONT_GENITIVE_IN `

Numeral genitive suffix in with front possessives

### ` NUM_BACK_ILLATIVE_IHIN `

Numeral illative suffix ihin

### ` NUM_BACK_ILLATIVE_IIN `

Numeral illative suffix iin with back possessives

### ` NUM_FRONT_ILLATIVE_IIN `

Numeral illative suffix iin with front possessives

### ` NUM_BACK_POSS `

Numeral back possessives

### ` NUM_FRONT_POSS `

Numeral front possessives

### ` NUM_BACK_POSS_AN `

Numeral back possessives with aan

### ` NUM_BACK_POSS_EN `

Numeral front possessives with een

### ` NUM_FRONT_POSS_EN `

Numeral back possessives with een

### ` NUM_FRONT_POSS_ÄN `

Numeral front possessives with ään

### ` NUM_BACK_CLIT `

Numeral back clitics 

### ` NUM_FRONT_CLIT `

Numeral front clitics

### ` NUM_BACK_CLIT_OPT `

Numeral back clitics

### ` NUM_FRONT_CLIT_OPT `

Numeral front clitics

### ` NUM_BACK_SINGULARS `

Numeral back singular suffixes

### ` NUM_FRONT_SINGULARS `

Numeral front singular suffixes

### ` NUM_FRONT_PLURALS `

Numeral front plural suffixes

### ` NUM_BACK_PLURALS `

Numeral back plural suffixes

### ` NUM_BACK_POSS_AN_OPT `

Numeral possessives with aan optionally

### ` NUM_FRONT_POSS_ÄN_OPT `

Numeral possessives with ään optionally

### ` NUM_BACK_POSS_EN_OPT `

Numeral possessives with een to back clitics optionally

### ` NUM_FRONT_POSS_EN_OPT `

Numeral possessives with een to front clitics optionally

### ` NUM_BACK_POSS_OPT `

Numeral possessives optionally

### ` NUM_FRONT_POSS_OPT `

Numeral possessives optionally

### ` NUM_BACK_POSS_EN_OBL `

Numeral possessives with een to back clitics obligatorily

### ` NUM_FRONT_POSS_EN_OBL `

Numeral possessives with een to front clitics obligatorily

### ` NUM_COMPOUND `

Numeral compounding

### ` PRON_FRONT_POSS `

Pronoun possessives

### ` PRON_BACK_POSS `

Pronoun possessives

### ` PRON_BACK_POSS_AN `

Pronoun possessives with aan

### ` PRON_BACK_POSS_EN `

Pronoun possessives with een to back clitics

### ` PRON_FRONT_POSS_EN `

Pronoun possessives with een to front clitics

### ` PRON_FRONT_POSS_ÄN `

Pronoun possessives with ään

### ` PRON_BACK_CLIT `

Pronoun back clitics

### ` PRON_FRONT_CLIT `

Pronoun front clitics

### ` PRON_BACK_CLIT_OPT `

Pronoun back clitics optionally

### ` PRON_FRONT_CLIT_OPT `

Pronoun front clitics optionally

### ` PRON_BACK_POSS_OPT `

Pronoun back possessives optionally

### ` PRON_FRONT_POSS_OPT `

Pronoun front possessives optionally

### ` PRON_BACK_POSS_AN_OPT `

Pronoun possessives with aan optionally

### ` PRON_BACK_POSS_EN_OPT `

Pronoun possessives with een to back clitics optionally

### ` PRON_FRONT_POSS_EN_OPT `

Pronoun possessives with een to front clitics optionally

### ` PRON_FRONT_POSS_ÄN_OPT `

Pronoun possessives with ään optionally

### ` V_BACK_WEAK_PRESENT `

Verb present suffixes

### ` V_FRONT_WEAK_PRESENT `

Verb present suffixes

### ` V_BACK_STRONG_PRESENT `

Verb present suffixes

### ` V_FRONT_STRONG_PRESENT `

Verb present suffixes

### ` V_BACK_3SG_A `

Verb 3rd singular suffix lengthened

### ` V_BACK_3SG_E `

Verb 3rd singular suffix lengthened

### ` V_FRONT_3SG_E `

Verb 3rd singular suffix lengthened

### ` V_BACK_3SG_I `

Verb 3rd singular suffix lengthened

### ` V_FRONT_3SG_I `

Verb 3rd singular suffix lengthened

### ` V_BACK_3SG_O `

Verb 3rd singular suffix lengthened

### ` V_BACK_3SG_U `

Verb 3rd singular suffix lengthened

### ` V_FRONT_3SG_Y `

Verb 3rd singular suffix lengthened

### ` V_FRONT_3SG_Ö `

Verb 3rd singular suffix lengthened

### ` V_FRONT_3SG_Ä `

Verb 3rd singular suffix lengthened

### ` V_BACK_WEAK_PAST `

Verb past suffixes

### ` V_FRONT_WEAK_PAST `

Verb past suffixes

### ` V_BACK_STRONG_PAST `

Verb past suffixes

### ` V_FRONT_STRONG_PAST `

Verb past suffixes

### ` V_BACK_IMPERATIVE `

Verb imperative suffixes

### ` V_FRONT_IMPERATIVE `

Verb imperative suffixes

### ` V_BACK_CONDITIONAL `

Verb conditional suffixes

### ` V_FRONT_CONDITIONAL `

Verb conditional suffixes

### ` V_BACK_POTENTIAL_N `

Verb potential suffixes assimilated to n

### ` V_FRONT_POTENTIAL_N `

Verb potential suffixes assimilated to n

### ` V_BACK_POTENTIAL_S `

Verb potential suffixes assimilated to s

### ` V_FRONT_POTENTIAL_S `

Verb potential suffixes assimilated to s

### ` V_BACK_POTENTIAL_L `

Verb potential suffixes assimilated to l

### ` V_FRONT_POTENTIAL_L `

Verb potential suffixes assimilated to l

### ` V_BACK_POTENTIAL_R `

Verb potential suffixes assimilated to r

### ` V_FRONT_POTENTIAL_R `

Verb potential suffixes assimilated to r

### ` V_BACK_PASSIVE `

Verb potential passives with t

### ` V_FRONT_PASSIVE `

Verb potential passives with t

### ` V_BACK_PASSIVE_T `

Verb potential passives with t

### ` V_FRONT_PASSIVE_T `

Verb potential passives with t

### ` V_BACK_PASSIVE_D `

Verb potential passives with d

### ` V_FRONT_PASSIVE_D `

Verb potential passives with d

### ` V_BACK_PASSIVE_L `

Verb potential passives with l

### ` V_FRONT_PASSIVE_L `

Verb potential passives with l

### ` V_BACK_PASSIVE_R `

Verb potential passives with r

### ` V_FRONT_PASSIVE_R `

Verb potential passives with r

### ` V_BACK_PASSIVE_N `

Verb potential passives with n

### ` V_FRONT_PASSIVE_N `

Verb potential passives with n

### ` V_BACK_AINF `

Verb A infinitive a

### ` V_FRONT_AINF `

Verb A infinitive ä

### ` V_BACK_EINF `

Verb E infinitive to clitics

### ` V_FRONT_EINF `

Verb E infinitive to clitics

### ` V_BACK_TUPCP_STRONG `

Verb passive participle without gradation

### ` V_FRONT_TUPCP_STRONG `

Verb passive participle without gradation

### ` V_BACK_TUPCP_0 `

Verb passive participle with t:0 gradation

### ` V_FRONT_TUPCP_0 `

Verb passive participle with t:0 gradation

### ` V_BACK_TUPCP_D `

Verb passive participle with t:d gradation

### ` V_FRONT_TUPCP_D `

Verb passive participle with t:d gradation

### ` V_BACK_TUPCP_L `

Verb passive participle with t:l gradation

### ` V_FRONT_TUPCP_L `

Verb passive participle with t:l gradation

### ` V_BACK_TUPCP_N `

Verb passive participle with t:n gradation

### ` V_FRONT_TUPCP_N `

Verb passive participle with t:n gradation

### ` V_BACK_TUPCP_R `

Verb passive participle with t:r gradation

### ` V_FRONT_TUPCP_R `

Verb passive participle with t:r gradation

### ` V_FRONT_POSS `

Verb possessives

### ` V_BACK_POSS `

Verb possessives

### ` V_BACK_POSS_AN `

Verb possessives with aan

### ` V_BACK_POSS_EN `

Verb possessives with een to back clitics

### ` V_FRONT_POSS_EN `

Verb possessives with een to front clitics

### ` V_FRONT_POSS_AN `

Verb possessives with ään

### ` V_BACK_CLIT `

Verb clitics

### ` V_FRONT_CLIT `

Verb clitics

### ` V_BACK_CLIT_OPT `

Verb clitics optionally

### ` V_FRONT_CLIT_OPT `

Verb clitics optionally

### ` V_BACK_POSS_EN_OBL `

Verb possessives obligatorily

### ` V_FRONT_POSS_EN_OBL `

Verb possessives obligatorily

### ` V_BACK_POSS_AN_OBL `

Verb possessives obligatorily

### ` V_BACK_POSS_OPT `

Verb possessives optionally

### ` V_BACK_POSS_AN_OPT `

Verb possessives optionally

### ` V_FRONT_POSS_AN_OBL `

Verb possessives obligatorily

### ` V_FRONT_POSS_OPT `

Verb possessives optionally

### ` V_FRONT_POSS_AN_OPT `

Verb possessives optionally

### ` V_BACK_DERIV_MINEN `

Verb minen derivation to back nominals

### ` V_FRONT_DERIV_MINEN `

Verb minen derivation to front nominals

### ` V_BACK_DERIV_PCPS `

Verb participle derivations to back adjectives

### ` V_FRONT_DERIV_PCPS `

Verb participle derivations to front adjectives
<!-- vim: set ft=markdown:-->
