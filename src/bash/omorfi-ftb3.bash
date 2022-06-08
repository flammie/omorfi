#!/bin/bash

source $(dirname $0)/omorfi.bash
args=$@
dict=describe

if test x$1 == x-h -o x$1 == x--help ; then
    omorfi_print_usage $0
    omorfi_print_help "Analyse Finnish into FTB3.1 (CONLL-X) format using omorfi"
    exit 0
elif test x$1 == x-V -o x$1 == x--version ; then
    omorfi_print_version $0 0.9
    exit 0
elif test x$1 == x-v -o x$1 == x--verbose ; then
    verbose=verbose
    shift 1
elif test x$1 == x-X -o x$2 == x--all-words ; then
    dict=describe
    shift 1
elif test x$1 == x-Z -o x$2 == x--mini ; then
    dict=analyse
    shift 1
fi
cat $@ | omorfi_ftb3 $dict
