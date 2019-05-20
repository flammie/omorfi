---
layout: default
title: "omorfi-vislcg(1)"
category: man
date: 2016-12-06 03:23:58
---


```
OMORFI-VISLCG(1)                  User Commands                 OMORFI-VISLCG(1)



NAME
       omorfi-vislcg - Analyse Finnish in Constraint Grammar VISL CG-3 format

SYNOPSIS
       omorfi-vislcg.py [OPTION] [FILENAME...]

DESCRIPTION
       Analyses running text using omorfi automata and hfst python library. This
       script is mainly for VISL CG-3 and apertium pipelines.

       -h, --help
              show this help message and exit

       -f FSAPATH, --fsa FSAPATH
              Path to directory of HFST format automata

       -i INFILE, --input INFILE
              source of analysis data

       -v, --verbose
              print verbosely while processing

       -o OUTFILE, --output OUTFILE
              print conll-u into OUTFILE

       -x STATFILE, --statistics STATFILE
              print statistics into STATFILE

       If no INFILE is given, input is read from standard input. If  no  OUTFILE
       is given, output is written to standard output.

EXAMPLES
       The following command

           omorfi-vislcg.py -i rautatie.txt -o rautatie.visl-cg3text

       analyses a corpus.

COPYRIGHT
       Copyright  ©  2016  Omorfi  contributors Licence GPLv3: GNU GPL version 3
       <http://gnu.org/licenses/gpl.html>
       This is free software: you are free to change and redistribute it.  There
       is NO WARRANTY, to the extent permitted by law.



OMORFI                            December 2016                 OMORFI-VISLCG(1)
```

