#!/bin/bash

source $(dirname $0)/omorfi.bash
args=$@
hyphen="-"


if test x$1 == x-h -o x$1 == x--help ; then
    omorfi_print_usage $0
    omorfi_print_help "Hyphenates word-forms using omorfi as compound breaker"
    exit 0
elif test x$1 == x-V -o x$1 == x--version ; then
    print_version
    exit 0
elif test x$1 == x-v -o x$1 == x--verbose ; then
    verbose=verbose
    shift 1
elif test x$1 == x--hyphen ; then
    hyphen=$2
    shift 2
fi
cat $@ | omorfi_hyphenate $hyphen
