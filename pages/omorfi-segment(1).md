---
layout: default
title: "omorfi-segment(1)"
category: man
date: 2016-12-06 03:23:58
---


```
OMORFI-SEGMENT(1)                 User Commands                OMORFI-SEGMENT(1)



NAME
       omorfi-segment - manual page for omorfi-segment

SYNOPSIS
       omorfi-segment.py [OPTIONs]

DESCRIPTION
       Morphologically  segments  running  text  using  omorfi automata and hfst
       tools

       -h, --help
              Print this help dialog

       -V, --version
              Print version info

       -f FSAPATH, --fsa FSAPATH
              Path to directory of HFST format automata

       -i INFILE, --input INFILE
              source of analysis data

       -o OUTFILE, --output OUTFILE
              print segmented data into OUTFILE

       -O OUTFORMAT, --output-format OUTFORMAT
              use OUTFORMAT format to print output

       -v, --verbose
              Print verbosely while processing

       --no-split-words
              no splitting on word-word boundaries (compound)

       --no-split-new-words
              no splitting on dynamoc  word-word  boundaries  (prev.  unattested
              compounds)

       --no-split-morphs
              no splitting on morph-morph boundaries

       --split-derivs
              split on deriv-morph boundaries too

       --split-nonwords
              split on other boundaries

       --segment-marker SEG
              use SEG to mark segmentation points

       If  no  FILENAMEs  are  given,  input  is read from standard input. If no
       marker is specified, an appropriate marker for OUTFORMAT is selected. The
       OUTFORMAT  is one of {segments, moses-factors, labels-tsv} for plain-text
       splitted, Moses SMT style factors or labeled segments in TSV stream

COPYRIGHT
       Copyright © 2015 Tommi  A  Pirinen  Licence  GPLv3:  GNU  GPL  version  3
       <http://gnu.org/licenses/gpl.html>
       This is free software: you are free to change and redistribute it.  There
       is NO WARRANTY, to the extent permitted by law.

NOTICE
       This used to be a bash script but was promoted into python.



omorfi-segment                    December 2016                OMORFI-SEGMENT(1)
