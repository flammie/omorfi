---
layout: default
title: "omorfi-analyse-text(1)"
category: man
date: 2016-02-08 18:23:58
---


```
OMORFI-ANALYSE(1)                User Commands                OMORFI-ANALYSE(1)



NAME
       omorfi-analyse-text - Analyse running Finnish text with omorfi

SYNOPSIS
       omorfi-analyse-text.sh [OPTION] [FILENAME...]

DESCRIPTION
       Analyses  running text using omorfi automata and hfst tools. This script
       is not for interactive use, and it may not generate  analysis  instantly
       when  invoked  on  interactive shell; you may need to produce whole text
       including end-of-file  marker  to  analyse.  For  interactive  use,  see
       omorfi-analyse-tokenised.

       -h, --help
              Print this help dialog

       -V, --version
              Print version info

       -v, --verbose
              Print verbosely while processing

       If no FILENAMEs are given, input is read from standard input.  This pro‐
       gram uses hfst-apertium-proc and, if  found  apertium-destxt,  otherwise
       sed.

EXAMPLES
       Analyse one text file:
              omorfi-analyse-text.sh < rautatie.txt > rautatie.xanals

COPYRIGHT
       Copyright  ©  2015  Omorfi contributors Licence GPLv3: GNU GPL version 3
       <http://gnu.org/licenses/gpl.html>
       This is free software: you are  free  to  change  and  redistribute  it.
       There is NO WARRANTY, to the extent permitted by law.



OMORFI                             March 2015                 OMORFI-ANALYSE(1)
```
