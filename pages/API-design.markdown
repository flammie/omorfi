---
layout: page
title: "API Design"
---

# Omorfi language binding APIs

Omorfi provides very simple bindings for using the language models without
having to write your own shell scripts around e.g. HFST shell commands. The APIs
provide typically some minor additional features, such as case folding or
heuristic word-tokenisations based on the dictionary, depending on the features
of the API host language (python has more advanced string mangling than C or
bash).

# Design

The APIs are tied around concept of an omorfi object or handle, that can be
used to load and apply the language models without dealing with too much of the
FST internals.

# Language specific APIs

The language specific APIs are generated with doc comment system of the host
language, e.g. javadoc, doxygen or docutils. You may find them from:


