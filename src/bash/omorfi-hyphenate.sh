#!/bin/bash

args=$@
hyphen="-"
function print_version() {
    echo "omorfi-hyphenate 0.1"
    echo "Copyright (c) 2012 Tommi A Pirinen"
    echo "Licence GPLv3: GNU GPL version 3 <http://gnu.org/licenses/gpl.html>"
    echo "This is free software: you are free to change and redistribute it."
    echo "There is NO WARRANTY, to the extent permitted by law."

}

function print_usage() {
    echo "Usage: $0 [OPTION] [FILENAME...]"
}

function print_help() {
    echo "Hyphenates word-forms using omorfi as compound breaker"
    echo
    echo "  -h, --help      Print this help dialog"
    echo "  -V, --version   Print version info"
    echo "  -v, --verbose   Print verbosely while processing"
    echo
    echo "If no FILENAMEs are given, input is read from standard input."
}


function hyphenate() {
    cat $@ | hfst-lookup -x "$omorfifile" |\
        sed -e "s/-1/$hyphen/g" -e "s/-2/$hyphen/g" -e "s/-3/$hyphen/g" \
            -e "s/-4/$hyphen/g"
}

if test x$1 == x-h -o x$1 == x--help ; then
    print_usage
    print_help
    exit 0
elif test x$1 == x-V -o x$1 == x--version ; then
    print_version
    exit 0
elif test x$1 == x-v -o x$1 == x--verbose ; then
    verbose=verbose
    shift 1
elif test ! -r $1 ; then
    echo "Cannot read from $1"
    print_usage
    exit 1
fi
omorfifile=$(find_omorfi hyphenate)
hyphenate $@
