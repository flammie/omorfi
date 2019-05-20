---
layout: default
title: "Timeline"
category: meta
date: 2016-02-08 18:23:58
---


# Introduction #

Omorfi's development up until now has been mostly the traditional academic morphological dictionary project: single researcher, single purpose, no potential contributors. That does not fit well in open source development model and so forth. Now that it may gain some more serious use and contributions, it seems that the preferred development model is still forking and branching, so this timeline tries to document the history, and the future of all the branches and versions.

# Timeline or branch tree #

  1. Nykysuomen sanalista (LGPL) published in December 2006
  1. Master's thesis project to implement SFST-PL based analyser, published 2007 as version 0.1\_alpha (in gna.org), LGPL; thesis accepted 2008?
  1. Added Joukahainen (GPL) as lexical source
  1. Rewritten in Finite State Morphology style by 2009
  1. Included spell-checking (PhD thesis back project), automated test suites for release 20100111
  1. Move hard-to-read and write data away from lexc hell to csv databases (and release) 20100401
  1. New words, tagging and styles for sme-fin machine translation as seen in Apertium GSOC 2011
  1. released 20101026
  1. First stab towards modular design, as seen in Nodalida 2011
  1. Added common nonstandard and spoken words and forms, more derivations
  1. Removed optional supports for renaming and moving tags in automata, since it became a maintenance burden and significant slow-down in compilation
  1. Added finnwordnet (Princeton Wordnet, relicenced to GPL) words to lexical data
  1. Released 20110505
  1. Added few corpus scavenged words and weighting schemes before GNA went MIA for a while, and
  1. Moving to googlecode, and git, released 20120401
  1. Branched and removed finntreebank hacks in tree, branched separate version for them (not at all as seen in FTB 1, 2 or 3)
  1. Branched giellatekno to co-operate and follow standard Finite State Morphology
    1. Added CG ruleset from original contributions by Fred Karlsson's CG1 and Trond Trosterud's conversion work
    1. ... see up to date changes in https://victorio.uit.no/langtech/trunk/langs/fin/
  1. apertium branches:
    1. languages/apertium-fin generated and modified in [svn://svn.code.sf.net/p/apertium/svn/languages/apertium-fin]
  1. (..???..)
  1. Added a lot of proper nouns from Uni. Helsinki project and some other lexical data from [FinnTreeBank](http://www.ling.helsinki.fi/kieliteknologia/tutkimus/treebank/) 3
  1. ftb3.1 compatibility in master at 90 % (2013)
  1. Released 20130829
  1. Pure continuation-class morphology without flags
  1. Lexical data converted from Kotus classification to detailed model-word inflection classes
  1. Unification of morphology and lexicon with [FinnTreeBank](http://www.ling.helsinki.fi/kieliteknologia/tutkimus/treebank/) 1 (omor tagset only; ftb3 tagging may have regressed somewhat vs. FTB3)

[timeline maybe?](http://cdn.knightlab.com/libs/timeline/latest/embed/index.html?source=0AkmwtwYJPKaPdEQ3akh1Vzh5ZGZRUy1CM01MTTM2LVE&font=Bevan-PotanoSans&maptype=toner&lang=en&height=650)



&lt;iframe src='http://cdn.knightlab.com/libs/timeline/latest/embed/index.html?source=0AkmwtwYJPKaPdEQ3akh1Vzh5ZGZRUy1CM01MTTM2LVE&font=Bevan-PotanoSans&maptype=toner&lang=en&height=650' width='100%' height='650' frameborder='0'&gt;



&lt;/iframe&gt;

