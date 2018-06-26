#!/bin/bash

source $(dirname $0)/omorfi.bash
args=$@

function print_version() {
    echo "omorfi-segment 0.4 (using omorfi bash API $omorfiapi)"
    echo "Copyright (c) 2018 Tommi A Pirinen"
    echo "Licence GPLv3: GNU GPL version 3 <http://gnu.org/licenses/gpl.html>"
    echo "This is free software: you are free to change and redistribute it."
    echo "There is NO WARRANTY, to the extent permitted by law."

}

function print_usage() {
    echo "Usage: $0 [OPTION] [FILENAME...]"
}

function print_help() {
    echo "Analyses running text using omorfi automata and hfst tools"
    echo
    echo "  -h, --help             Print this help dialog"
    echo "  -V, --version          Print version info"
    echo "  -v, --verbose          Print verbosely while processing"
    echo "  -m, --marker M         use M to mark segmentation points"
    echo
    echo "If no FILENAMEs are given, input is read from standard input."
    echo "If no markers are specified, → ← is used."
}


while test $# -gt 0 ; do 
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
