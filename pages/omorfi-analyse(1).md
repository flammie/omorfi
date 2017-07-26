---
layout: page
title: "omorfi-analyse(1)"
category: man
date: 2016-02-08 18:23:58
---


```
OMORFI-ANALYSE(1)               User Commands              OMORFI-ANALYSE(1)

NAME
       omorfi-analyse - Analyse running Finnish text with omorfi python API

SYNOPSIS
       omorfi-analyse.py  [-h] [-f FSAPATH] [-i INFILE] [-v] [-o OUTFILE] -F
       FORMAT

DESCRIPTION
       Analyses running text using omorfi automata and hfst python library.

       -h, --help
              show this help message and exit

       -f FSAPATH, --fsa FSAPATH
              Path to directory of HFST format automata

       -i INFILE, --input INFILE
              source of analysis data

       -v, --verbose
              print verbosely while processing

       -f FORMAT, --format FORMAT
              output in format compatible with FORMAT

       If no INFILE is given, input is read from standard input. If no  OUT‐
       FILE  is  given,  output  is  written  to  standard output. Format is
       required.

EXAMPLES
       Analyse corpus:
              omorfi-analyse.py    -F    vislcg3    -i    rautatie.txt    -o
              rautatie.vislcg3

COPYRIGHT
       Copyright © 2015 Omorfi contributors Licence GPLv3: GNU GPL version 3
       <http://gnu.org/licenses/gpl.html>
       This is free software: you are free to change  and  redistribute  it.
       There is NO WARRANTY, to the extent permitted by law.

OMORFI                           March 2015                OMORFI-ANALYSE(1)
```
