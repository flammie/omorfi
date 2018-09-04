---
layout: default
title: "Contributing or helping"
category: meta
date: 2016-02-08 18:23:58
---


# Introduction #

Omorfi is a knowledge-driven analyser of Finnish language. A lot of manual labour is required to keep currently around 300,000 word entries in database up-to-date. Here are some ways to participate.

# Wiktionary #

Word data from [Finnish Wiktionary](http://fi.wiktionary.org/) is drawn to our database every once in a while. If the word(s) you want added to omorfi are in accordance to [Finnish Wiktionary's guidelines](http://fi.wiktionary.org/wiki/), you are best off adding it there first. Please ensure that you specify inflectional classification.

# Send patches directly to databases #

The word data in omorfi is currently stored in tsv format databases that you can modify directly using text editors or office calc apps. The basic tasks have also been automated with shell scripts. To add a word, use `add-word.bash` and to modify existing word entry, use `change-class.bash`. The obligatory arguments to the scripts are word's lemma and the inflectional class. To edit these manually, the lemmas are in first field of the database and inflectional classes in the second. The word list is in one master database and optional attributes are collected in files in `attributes` directory. If you do not have write permission to git, use git's format-patch and/or send-mail capabilities to provide patch to the project.

Note that tsv databases obviously do not maintain data properly so you need to use `make && make check` to ensure that results are consistent before sending patches.
