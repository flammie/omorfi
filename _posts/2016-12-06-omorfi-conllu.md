---
layout: page
title: "omorfi-conllu(1)"
category: man
date: 2016-12-06 03:23:58
---


```
OMORFI-CONLLU(1)                  User Commands                 OMORFI-CONLLU(1)



NAME
       omorfi-conllu - Analyse Finnish in Universal Dependencies CONLL-U format

SYNOPSIS
       omorfi-conllu.py [OPTION] [FILENAME...]

DESCRIPTION
       Analyses tokenised text using omorfi automata and hfst python library.

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

       If  no  INFILE is given, input is read from standard input. If no OUTFILE
       is given, output is written to standard output.

EXAMPLES
       The following command

           omorfi-conllu.py -i fi-ud-dev.conllu -o omorfi-ud-dev.conllu

       analyses a tokenised corpus

COPYRIGHT
       Copyright © 2016 Omorfi contributors Licence GPLv3:  GNU  GPL  version  3
       <http://gnu.org/licenses/gpl.html>
       This is free software: you are free to change and redistribute it.  There
       is NO WARRANTY, to the extent permitted by law.



OMORFI                            December 2016                 OMORFI-CONLLU(1)
