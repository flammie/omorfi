---
layout: default
title: "omorfi-tokenise(1)"
category: man
date: 2016-12-06 03:23:58
---


```
OMORFI-TOKENISE(1)                User Commands               OMORFI-TOKENISE(1)



NAME
       omorfi-tokenise  -  Tokenise Finnish text with help of morphological dic‐
       tionary

SYNOPSIS
       omorfi-tokenise.py [OPTION] [FILENAME...]

DESCRIPTION
       Tokenises text using dictionary in addition to  your  average  whitespace
       splitting and punctuation stripping

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

       -O OUTFORMAT, --output-format OUTFORMAT
              format output for OUTFORMAT

       If  no  INFILE is given, input is read from standard input. If no OUTFILE
       is given, output is written to standard output. OUTFORMAT should  be  one
       of  the  supported  end  applications, e.g. conllu for CONLL-U, moses for
       Moses SMT.

EXAMPLES
       The following command

           omorfi-tokenise.py -i rautatie.text -o rautatie.tokens

       tokenise a raw text corpus

COPYRIGHT
       Copyright © 2016 Omorfi contributors Licence GPLv3:  GNU  GPL  version  3
       <http://gnu.org/licenses/gpl.html>
       This is free software: you are free to change and redistribute it.  There
       is NO WARRANTY, to the extent permitted by law.



OMORFI                            December 2016               OMORFI-TOKENISE(1)
```
