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
    orcid: 0000-0003-1207-5395
    affiliation: 1
  - name: Inari Listenmaa
    affiliation: 2
  - name: Ryan Johnson
    affiliation: 3
  - name: Francis Tyers
    affiliation: 4
  - name: Juha Kuokkala
    affiliation: 5
affiliations:
 - name: University of Hamburg
   index: 1
 - name: Göteborg University
   index: 2
 - name: Arctic University of Norway
   index: 3
 - name: University of Indiana
   index: 4
 - name: University of Helsinki
   index: 5
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
[@beesley2004].

Omorfi project consists of few distinct parts:

1. _a lexical database_ containing hundreds of thousands of words, curated by
   langauge experts from open source repositories, such as wiktionary
2. a collection of _scripts_ to convert lexical database into formats used by
   upstream NLP tools
3. an _autotools setup_ to build, install, package, deploy or test the system
   easily
4. a collection of relatively bindings and libraries to programming languages
   popular within NLP community, such as python, Java and C++

The ``omorfi`` project is designed to be used by computer scientists who need a
reliable model of Finnish language for computational natural language
understanding software, or computational linguists wishing to study the
grammatical features of Finnish. It has been used to implement various natural
language processing software including spell-checking and correction, machine
translation and dependency syntax treebanking.

# Acknowledgements

We acknowledge all the professors, teachers and students who have been
instrumental to creation and continued development of the system, for up-to-date
list please view the THANKS file included with the system. At the time of
writing:

In chronological order of the project history:

- Inari Listenmaa
- Kimmo Koskenniemi
- Krister Lindén
- Erik Axelson
- Miikka Silfverberg
- Anssi Yli-Jyrä
- Inari Listenmaa
- Sjur Moshagen
- The courses clt260, clt270 and fullskaliga morfologiska lexikon students and
  staff for extensive testing.
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
