---
layout: page
title: "Omorfi with moses"
category: design
date: 2016-02-08 18:23:58
---


# Using omorfi in moses pipeline

Omorfi can be easily plugged into [statistical machine translation system
moses](http://statmt.org/moses/) with semi-good results (no immediate BLEU
increase or such, slight improvement in human evaluations sometimes). There are
two ways I've tried and succeeded with, I will first describe them, then give
step-by-step tutorials for you to follow.

## Factored stuff

You can use omorfi as a [factored
model](http://www.statmt.org/moses/?n=Moses.FactoredTutorial). The helper script
located in `omorfi-factorise.py` can produce output with some factors
pulled from 1-best list of omorfi installation. The factors are:

  * (surface)
  * lemma
  * Google universal pos
  * full morphological analysis
  * suffix morphs

Apart from suffix morph factor, the things are standard.

## Segmenting as pre- or post-processing

You can use omorfi to turn [moses baseline phrase-based
model](http://www.statmt.org/moses/?n=Moses.Baseline) into a morph-phrase
machine translation by simply pre-processing the Finnish data with the helper
script `src/python/omorfi-segment.sh`. This way you can use omorfi to extract
compound parts, inflectional or derivational morphs from the word-forms to
improve 1:1 matchingness of the data and decrease OOV rate.


# Tutorials

Both of the tutorials use the [Moses baseline
setup](http://www.statmt.org/moses/?n=Moses.Baseline) with [Europarl-v8
 data](http://www.statmt,org/wmt16) from WMT 2016 shared task. You can obtain it
like so:

```
wget http://data.statmt.org/wmt16/translation-task/training-parallel-ep-v8.tgz
wget http://statmt.org/wmt15/europarl-v8.fi.tgz
```

There is some bug in `wget` with localisations and big files or speeds, if your
wget gets segfaulty like mine, invoke it with `LC_ALL=C`.


## Factorising data

Moses factored models can be generated with `omorfi-factorise.py`. The factors
you get depend on versions of automata that were installed and other random
factors in the code, so *check the results to determine which factors are
useful*.

```
$MOSES/scripts/tokenizer/tokenizer.perl -l fi < \
    training-parallel-ep-v8/europarl-v8.fi-en.fi > \
    training-parallel-ep-v8.fi-en.tok.fi
omorfi-factorise.py -i training-parallel-ep-v8.fi-en.tok.fi \
    -o training-parallel-ep-v8-fi-en.tok.factors.fi
```

If you are not operating on a cluster, or even if you are, you may want to use
the `split` command to process the data in smaller chunks. You can also
parallelise it all, since the factorisation picks 1-best tokens totally without
context at the moment. Even in near future it will probably not go much across
sentence boundaries.

After doing this you will want to ensure that the files line counts still match,
as moses is notoriously bad at handling even off-by-1 errors.

## Segmenting data

There's no special magic in using pre-segmented data in moses, you simply use
omorfi-segment.py to split words into sub-word components and moses treats them
like any other tokens. If you are translating towards Finnish and using the
segmented translation models you do have an extra step of de-segmenting, for
this reason the segmenting supports using special markers for segmented
substrings, by default → for a prefix / other token split from left and ← for
suffix or other token split on the right.

```

```
