#!/bin/bash
source $(dirname $0)/omorfi.bash
args=$@

if test x$1 == x-h -o x$1 == x--help ; then
    omorfi_print_usage $0
    omorfi_print_help "Generates word-forms from line separated omorfi definitions"
    exit 0
elif test x$1 == x-V -o x$1 == x--version ; then
    omorfi_print_version $0 0.9
    exit 0
elif test x$1 == x-v -o x$1 == x--verbose ; then
    verbose=verbose
    shift 1
fi

cat $@ | omorfi_generate
