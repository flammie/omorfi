---
layout: page
title: "Java API"
category: api
date: 2016-02-08 18:23:58
---


The java API to omorfi uses hfst-optimized-lookup-java. This is preliminary, I basically made it to test if I can use omorfi on android. It turns out, yes I can. There's some javadoc included.

# package com.github.flammie.omorfi;

## Omorfi.java

Simple java interface for omorfi using hfst optimised lookup java.


## Class Omorfi

*An object holding automata for all functions of omorfi.* Each of the automata are accessible by their function and identifier. Some combinations of functionalities may be available that access more than one automaton in non-trivial ways. Currently supported automata functions are:

* analysis
* tokenisation
* generation
* lemmatisation
* segmentation
* lookup

These are followed by corresponding automaton sets as attributes:
*       analysers: key is 'omorfi-' + tagset
*       tokenisers: key is 'omorfi'
*       generators: key is 'omorfi-' + tagset
*       lemmatizers: key is 'omorfi'
*       hyphenators: key is 'omorfi'
*       segmenters: key is 'omorfi'

The java code can perform minimal string munging.

### Omorfi::Omorfi()

*construct empty omorfi holder.*

### Omorfi::load(String)

*Load omorfi automaton from filename and guess its use.* A file name should consist of three parts separated by full stop. The second part must be a keyword describing the use of the automaton, first part is parsed as an identifier typically starting with the word omorfi, followed by any extras, such as the tagset for analysis or generation.

### Omorfi::loadAll(String)

*load all recognisable automata in given path.*

### Omorfi::loadAll()

*load all automata in standard system locations.*

### Omorfi::analyse(String, String)

*Perform a simple morphological analysis lookup.* If can_titlecase does not evaluate to False, the analysis will also be performed with first letter uppercased and rest lowercased. If can_uppercase evaluates to not False, the analysis will also be performed on all uppercase variant. If can_lowercase evaluates to not False, the analysis will also be performed on all lowercase variant. 

The analyses with case mangling will have an additional element to them identifying the casing.

### Omorfi::analyse(String)

*perform analysis with any loaded automaton.*

### Omorfi::tokenise(String, String)

*Perform tokenisation with specific automaton.*

### Omorfi::tokenise(String)

*Perform tokenisation with loaded tokeniser if any, or split.* If tokeniser is available, it is applied to input line and if result is achieved, it is split to tokens according to tokenisation strategy and returned as a list.

If no tokeniser are present, or none give results, the line will be tokenised using java's basic string functions.

