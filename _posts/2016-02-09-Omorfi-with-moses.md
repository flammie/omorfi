---
layout: page
title: "Omorfi with moses"
category: design
date: 2016-02-08 18:23:58
---


# Omorfi as part of moses

Omorfi can be easily plugged into [statistical machine translation system moses](http://statmt.org/moses/) with semi-good results (no immediate BLEU increase or such, slight up in human evaluations).

## Factored stuff

You can use omorfi as a [factored model](http://www.statmt.org/moses/?n=Moses.FactoredTutorial). The helper script located in `src/python/omorfi-factorise.py` can produce output with four factors pulled from 1-best list of omorfi installation. The factors are:

  * (surface)
  * lemma
  * Google universal pos
  * full morphological analysis
  * suffix morphs

Apart from suffix morph factor, the things are standard. If you follow factored tutorial

## Segmenting as pre- or post-processing

You can use omorfi to turn [moses baseline phrase-based model](http://www.statmt.org/moses/?n=Moses.Baseline) into a morph-phrase machine translation by simply pre-processing the Finnish data with the helper script `src/python/omorfi-segment.sh`.
