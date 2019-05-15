---
layout: default
title: "omorfi-disambiguate-text(1)"
category: man
date: 2016-02-08 18:23:58
---


```
OMORFI-DISAMBIGUATE-TEXT(1)     User Commands    OMORFI-DISAMBIGUATE-TEXT(1)

NAME
       omorfi-disambiguate-text - Analyse and disambiguate Finnish text with
       omorfi

SYNOPSIS
       omorfi-disambiguate-text.sh [OPTION] [FILENAME...]

DESCRIPTION
       Analyses running text using omorfi python interface and VISL CG 3.

       -h, --help
              Print this help dialog

       -V, --version
              Print version info

       -v, --verbose
              Print verbosely while processing

       If no FILENAMEs are given, input is read from standard  input.   This
       program uses omorfi-analyse.py.

EXAMPLES
       Analyse one text file:
              omorfi-disambiguate-text.sh       <       rautatie.txt       >
              rautatie.vislcg3anals

COPYRIGHT
       Copyright © 2015 Tommi A Pirinen Licence GPLv3:  GNU  GPL  version  3
       <http://gnu.org/licenses/gpl.html>
       This  is  free  software: you are free to change and redistribute it.
       There is NO WARRANTY, to the extent permitted by law.

omorfi-disambiguate-text 0.2     August 2015     OMORFI-DISAMBIGUATE-TEXT(1)
```

