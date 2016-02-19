---
layout: page
title: "omorfi-disambiguate-factorise(1)"
category: man
date: 2016-02-08 18:23:58
---


```
OMORFI-FACTORISE(1)              User Commands              OMORFI-FACTORISE(1)



NAME
       omorfi-factorise - Factorise running Finnish text with omorfi for moses

SYNOPSIS
       omorfi-factorise.py [OPTION] [FILENAME...]

DESCRIPTION
       Factorises  running  text using omorfi automata and hfst python library.
       This script is mainly for moses pipelines between tokenise and training.

       -h, --help
              show this help message and exit

       -f FSAPATH, --fsa FSAPATH
              Path to directory of HFST format automata

       -i INFILE, --input INFILE
              source of analysis data

       -v, --verbose
              print verbosely while processing

       -o OUTFILE, --output OUTFILE
              print factors into OUTFILE

       If no INFILE is given, input is read from standard input. If no  OUTFILE
       is given, output is written to standard output.

EXAMPLES
       Factorise corpus:
              omorfi-factorise.py -i rautatie.txt -o rautatie.factors

COPYRIGHT
       Copyright  ©  2015  Omorfi contributors Licence GPLv3: GNU GPL version 3
       <http://gnu.org/licenses/gpl.html>
       This is free software: you are  free  to  change  and  redistribute  it.
       There is NO WARRANTY, to the extent permitted by law.



OMORFI                             March 2015               OMORFI-FACTORISE(1)
```

