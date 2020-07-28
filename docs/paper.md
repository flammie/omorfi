---
title: 'Omorfi: Open morphology of Finnish'
tags:
  - Python
  - Finnish
  - NLP
  - morphological analysis
  - language modelling
authors:
  - name: Tommi A Pirinen
    affiliation: 1
affiliations:
 - name: University of Hamburg
   index: 1
date: 4 February 2020
bibliography: paper.bib
---

# Summary

Finnish is a natural language spoken mainly in Finland by ca. 6 million people
as of 2020. Unlike many European languages, it has rich morphological system,
which makes it slightly more complicated to use in computational systems, for
example, a single word may be inflected in thousands of acceptable word-forms,
making naive list- or statistics-based language models less effective. In
omorfi, we solve this problem by generating inflecting dictionaries to be used
in conjunction with finite-state automata-based morphological analysis software
[@beesley:2003], available as open source from [@hfst:2013].

Omorfi project consists of few distinct parts:

1. _a lexical database_ containing hundreds of thousands of words, curated by
   langauge experts from open source repositories, such as wiktionary
2. a collection of _scripts_ to convert lexical database into formats used by
   upstream NLP tools
3. an _autotools setup_ to build, install, package, deploy or test the system
   easily
4. a collection of relatively bindings and libraries to programming languages
   popular within NLP community, such as python, Java and C++

The omorfi project is designed to be used by computer scientists who need a
reliable model of Finnish language for computational natural language
understanding software, or computational linguists wishing to study the
grammatical features of Finnish. It has been used to implement various natural
language processing software including spell-checking and correction, machine
translation and dependency syntax treebanking.

# Background

Omorfi has been developed since 2008, and is relatively stable lexical database
for Finnish. It aggregates lexical data from various open source word-lists of
Finnish into one big database:

* [Nykysuomen sanalista](//kaino.kotus.fi) (LGPL),
* [Joukahainen](//joukahainen.lokalisointi.org) (GPL) and
* [FinnWordNet](//www.ling.helsinki.fi/research/finnwordnet) (Princeton
  Wordnet licence / GPL; relicenced with kind permission from University of
  Helsinki)
* [Finnish Wiktionary](//fi.wiktionary.org) and
* [English
   Wiktionary](//en.wiktionary.org) (Creative Commons Attribution–ShareAlike).

Some words have also been collected by omorfi developers and contributors and
are GPLv3 like the rest of the software package. All words have been manually
verified by omorfi contributors.

Omorfi has been used in number of research projects and applications, some of
which are listed in the [official documentation under
articles](//flammie.github.io/omorfi/articles.html). Few of the more
notable recent research include: machine translation [@rubino:2015],
OCR [@silfverberg:2015], semantic web [@makela:2014], named
entity resolution [@ruokolainen:2019] and spell-checking and correction
[@pirinen:2014].

# Functionalities

Omorfi provides the functionalities directly through the underlying
morphological analysis engines, such as [@hfst:2013], but also through APIs for
popular programming languages such as python, java and C++. For less advanced
users, another project [@hamalainen:2019], provides user-friendly interfaces.

The interfaces provide all the main functionalities of natural language
processing pipelines: given a string containing Finnish text, the text can be
tokenised into words and punctuation or similar units, for each token a list of
potential analyses can be retrieved, as well as potential morphological
segmentations, hyphenations or spelling corrections. For example, given a
string: ``tässä on "sanoja."``, the tokenisation may return a list of tokens:
``[tässä, on, ", sanoja, ., "]``, analysis of the first token might return a set
of potential analyses: ``{tämä PRON|PronType=Dem|Number=Sing|Case=Ine, tässä
ADV}``, whereas the morphological segmentation would produce set of
potential answers: ``{tä ssä, tässä}``. The exact representation may vary
between programming languages and API versions.

Omorfi contains a continuous integration test suite to guarantee the quality of
lexical database after each contribution is integrated, this is especially
crucial since contributions from wiktionary imported at regular intervalls.

# Acknowledgements

We acknowledge all the professors, teachers and students who have been
instrumental to creation and continued development of the system, for up-to-date
list please view the THANKS file included with the system.

In chronological order of the project history:

- Inari Listenmaa
- Kimmo Koskenniemi
- Krister Lindén
- Erik Axelson
- Miikka Silfverberg
- Anssi Yli-Jyrä
- Inari Listenmaa
- Sjur Moshagen
- Ryan Johnson
- Francis Tyers
- Juha Kuokkala
- The students and staff ast Uni. Helsinki for extensive testing.
- University of Turku bio-NLP group (a lot of resources have been exchanged
  back and forth)
- Research institute of languages in Finland for Finnish wordlists
- Joukahainen / Voikko contributors
- GF contributors
- fi.wiktionary.org contributors
- Universal Dependencies (Finnish) contributors
- Unimorph contributors
- en.wiktionary.org contributors


# References
