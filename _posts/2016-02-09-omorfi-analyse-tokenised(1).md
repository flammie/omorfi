---
layout: page
title: "omorfi-analyse-tokenised(1)"
category: man
date: 2016-02-08 18:23:58
---


```
OMORFI-ANALYSE-TOKENISEd(1)      User Commands      OMORFI-ANALYSE-TOKENISEd(1)



NAME
       omorfi-analyse-tokenised - Analyse word-forms with omorfi

SYNOPSIS
       omorfi-analyse-tokenised.sh [OPTION] [FILENAME...]

DESCRIPTION
       Analyses  list  of word forms using omorfi automata. This script is used
       to analyse preprocessed text, or to test omorfi from interactive shells.
       To  analyse large texts with builtin pre-processing, use omorfi-analyse-
       text.

       -h, --help
              Print this help dialog

       -V, --version
              Print version info

       -v, --verbose
              Print verbosely while processing

       If no FILENAMEs are given, input is read from standard input.

EXAMPLES
       Invoke interactive mode to test omorfi:
              omorfi-analyse-tokenised.sh

       Analyse pre-processed word-list:
              omorfi-interactive.sh < test.words > test.results

COPYRIGHT
       Copyright © 2015 Omorfi contributors Licence GPLv3: GNU  GPL  version  3
       <http://gnu.org/licenses/gpl.html>
       This  is  free  software:  you  are  free to change and redistribute it.
       There is NO WARRANTY, to the extent permitted by law.



OMORFI                             March 2015       OMORFI-ANALYSE-TOKENISEd(1)
```

