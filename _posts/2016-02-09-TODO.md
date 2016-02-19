---
layout: page
title: "TODO"
category: meta
date: 2016-02-08 18:23:58
---


# Introduction #

This is an informal document about possible future developments of omorfi lexical data and stuffs. Please check the date of this document to see it isn't out of date when contrasting to the actual source code.


# Inflections #

  * Alternating vowel harmony cases (_analyysi-a_ ~ _analyysi-ä_)


# Compounding and derivation #

  * Some compounds with digits/acros and (possible) complex parts do not analyze (_5-vuotissyntymäpäivä_)


# Compounds with multiple inflected parts #

Paradigms of this type of words (e.g. _uusivuosi_ : _uudenvuoden_) are currently spelled out lexeme-by-lexeme in 51-stems.tsv. There are probably still some errors in the semi-automatically generated paradigms which should be checked for consistency.
Also, we could investigate possibilities for a mechanism for generating these paradigms from the inflected forms of each compound part as they are found in the omorfi lexicon, to ensure consistency and ease the maintenance of lexicon.


# Obsolete/archaic forms #

May be needed for analysing older texts?

  * Weak-grade plural plural forms of type _avannoita_, _avannoiden_ etc.
  * Reflexive inflection (_heitä(i)kse(n)_, _heittihe(n)_)
  * ...

# Lexeme classifications #

  * _Verbs_ need to be classified by their valency and argument structure: intransitive, transitive, more arguments. Also, the argument cases need to be recorded. Also for verbs with unusual argument structures, such as necessives that have accusative subjects and verb phrase objects.
  * _Particles_ need to be classified etymologically by the case or such suffix where relevant. E.g. _kotona_, _kotoa_ pair might usefully have general locative and separative case information for many apps, even moreso for really transparent cases like _lähellä_, _läheltä_, _lähelle_.


# Conformity with [FinnTreeBank](http://www.ling.helsinki.fi/kieliteknologia/tutkimus/treebank/) 1 - 3 #

  * Omorfi's morphology in omor [brac=ket] format has been unified with a thoroughly revised version of FTB1. The next steps would be to develop a variant of tagging from Omorfi's ftb3 format that complies to FTB1, and ultimately, to re-tag the FTB3 corpus according to this standard.

# Fixing miscellaneous defects #

  * See the [Issues](http://code.google.com/p/omorfi/issues/list) tab for details.
