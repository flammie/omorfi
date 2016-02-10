---
layout: page
title: "omorfi-segment(1)"
category: man
date: 2016-02-08 18:23:58
---


```
OMORFI-SEGMENT(1)                User Commands                OMORFI-SEGMENT(1)



NAME
       omorfi-segment - segment Finnish word-forms into morphs using omorfi

SYNOPSIS
       omorfi-segment.sh [OPTION] [FILENAME...]

DESCRIPTION
       Segments running text using omorfi automata and hfst tools

       -h, --help
              Print this help dialog

       -V, --version
              Print version info

       -v, --verbose
              Print verbosely while processing

       -s, --segment SPOINT
              segment on SPOINTs [default=ALL-STUB]

       -m, --marker M
              use M to mark segmentation points [default= ]

       If  no  FILENAMEs are given, input is read from standard input.
       If no SPOINTs are given, segmentation is  done  on  all  bound‐
       aries,  except  STUB. Possible values are: WORD, MORPH, DERIVA‐
       TION, NEWWORD, ETYM, STUB or ALL, corresponding to wB, MB,  DB,
       WB,  XB, STUB and all of above.  If no markers are specified, a
       single ASCII white space is  used.   Marker  can  be  arbitrary
       string  not  containing  colons  or sed specials.  This program
       uses hfst-lookup

COPYRIGHT
       Copyright © 2015 Omorfi contributors Licence GPLv3: GNU  GPL  version  3
       <http://gnu.org/licenses/gpl.html>
       This  is  free  software:  you  are  free to change and redistribute it.
       There is NO WARRANTY, to the extent permitted by law.



OMORFI                             March 2015                 OMORFI-SEGMENT(1)
```

