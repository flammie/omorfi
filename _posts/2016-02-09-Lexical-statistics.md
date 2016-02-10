---
layout: page
title: "Lexical statistics"
category: stats
date: 2016-02-08 18:23:58
---


# Statistics from the database as of (stable release version 20150904)

Lexemes:

```
$ wc -l src/lexemes.tsv 
424259 src/lexemes.tsv
```

of which, proper nouns:

```
$ wc -l src/attributes/proper-classes.tsv 
273612 src/attributes/proper-classes.tsv
```

Lexemes per origin:

```
$ cut -f 4 src/lexemes.tsv | sort | uniq -c | sort -nr
 265048 unihu
  96563 kotus
  31392 finnwordnet
  23193 unk
   7704 ftb3
    214 fiwiktionary
    136 omorfi
      8 joukahainen
```

Lexemes per morphological word-class:

```
$ cut -f 3 src/lexemes.tsv | sed -e 's/_.*//' | sort | uniq -c
  18791 A
   3499 ACRO
 380315 N
      1 new
    901 NUM
   9643 PCLE
     85 PRON
      2 PUNCT
     59 SYMBOL
  10955 V
      8 X
```

Lexemes in different particle classes:

```
$ cut -f 4 src/attributes/particle-classes.tsv | sed -e 's/|.*//' |sort | uniq -c
    485 abbreviation
    477 adposition
   5680 adverb
     81 conjunction
    364 interjection
      1 particle
     14 qualifier
    458 unspecified
```

Paradigms per morphological word-class:

```
$ cut -f 3 src/lexemes.tsv | sort | uniq | sed -e 's/_.*//' | sort | uniq -c
    130 A
     46 ACRO
    679 N
      1 new
    730 NUM
     24 PCLE
     52 PRON
      1 PUNCT
      2 SYMBOL
    224 V
      8 X
```

Stem variations per class:

```
$ wc -l src/continuations/*-stems.tsv  20729 src/continuations/51-stems.tsv
     85 src/continuations/acronym-stems.tsv
    713 src/continuations/adjective-stems.tsv
    669 src/continuations/digit-stems.tsv
   1950 src/continuations/noun-stems.tsv
     89 src/continuations/numeral-stems.tsv
     30 src/continuations/particle-stems.tsv
    424 src/continuations/pronoun-stems.tsv
     61 src/continuations/symbol-stems.tsv
   1145 src/continuations/verb-stems.tsv
  25895 total
```

Inflectional affix sets:

```
$ wc -l src/continuations/*-inflections.tsv
   207 src/continuations/acro-inflections.tsv
   347 src/continuations/adjective-inflections.tsv
    81 src/continuations/digit-inflections.tsv
   334 src/continuations/noun-inflections.tsv
   197 src/continuations/numeral-inflections.tsv
    99 src/continuations/particle-inflections.tsv
   381 src/continuations/pronoun-inflections.tsv
    83 src/continuations/symbol-inflections.tsv
   544 src/continuations/verb-inflections.tsv
  2273 total
```
