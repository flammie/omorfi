# Omorfi file formats

*Outdated*

# Introduction

Handling file formats and taggings in NLP programs is troublesome.  In omorfi we
have used a lot of small python scripts and snippets for this.  Eventually we
will converge towards doing conversions n:1 and 1:m  formats, instead of n:m
directly pairwise...

Formats already found in real world and need to be supported are following:

* text/plain: raw text comes in different formats:
  * max 80. characters per line,
  * paragraphs and headings separated by empty lines
  * pre-tokenised with spaces
  * one sentence per line
* VISL CG 3 cg-like format
* CONLL-U format (Universal dependencies)
* CONLL-X format (FinnTreeBank)
* Apertium format (anti-regexing line noise)
* other legacy (FITWOL, Xerox, ...)

Formats that are nice or easy but not found in real world:

* json
* TEI

And then some...

And this is not even considering the differences in the analysis formats, e.g.:
`+N` ~ ` N` ~ `<n>` ~ `NOUN` ~ `UPOS=NOUN` ~ `N-------`.
