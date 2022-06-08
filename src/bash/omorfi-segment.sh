#!/bin/bash

source $(dirname $0)/omorfi.bash
args=$@

while test $# -gt 0 ; do
    if test x$1 == x-h -o x$1 == x--help ; then
        omorfi_print_usage $0
        omorfi_print_help  "Analyses running text using omorfi automata and hfst tools"
        echo
        echo "  -m, --marker M         use M to mark segmentation points"
        echo
        echo "If no markers are specified, → ← is used."
        exit 0
    elif test x$1 == x-V -o x$1 == x--version ; then
        omorfi_print_version $0 0.9
        exit 0
    elif test x$1 == x-v -o x$1 == x--verbose ; then
        verbose=verbose
        shift 1
    elif test x$1 == x-m -o x$1 == x--marker ; then
        marker=$2
        shift 2
    elif test ! -r $1 ; then
        echo "Cannot read from $1"
        print_usage
        exit 1
    else
        break
    fi
done
cat $@ | omorfi_segment $marker
