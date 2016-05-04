#!/bin/bash

source omorfi.bash
args=$@

marker=" "
markexpr=""
unmarkexpr='\({STUB}\|{WB}\|{MB}\|{DB}\|{XB}\|{wB}\)'

function print_version() {
    echo "omorfi-segment 0.2"
    echo "Copyright (c) 2015 Tommi A Pirinen"
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
    echo "  -s, --segment SPOINT   segment on SPOINTs [default=ALL-STUB]"
    echo "  -m, --marker M         use M to mark segmentation points [default= ]"
    echo
    echo "If no FILENAMEs are given, input is read from standard input."
    echo "If no SPOINTs are given, segmentation is done on all boundaries,"
    echo "except STUB. Possible values are: WORD, MORPH, DERIVATION, NEWWORD,"
    echo "ETYM, STUB or ALL, corresponding to wB, MB, DB, WB, XB, STUB and all"
    echo "of above."
    echo "If no markers are specified, a single ASCII white space is used."
    echo "Marker can be arbitrary string not containing colons or sed specials."
    echo "This program uses hfst-lookup"
}


function analyse() {
    cat $@ | @HLOOKUP@ "$omorfifile" |\
        sed -e "s:${markexpr}:${marker}:g" -e "s/${unmarkexpr}//g"
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
    elif test x$1 == x-s -o x$1 == x--segment ; then
        case "$2" in
            ALL)
                markexpr='\({WB}\|{MB}\|{DB}\|{wB}\|{XB}\|{STUB}\)';
                unmarkexpr='{_BOGUS_}';;
            WORD)
                markexpr="${markexpr}"'\|{wB}';
                unmarkexpr=${unmarkexpr/\\\|\{wB\}/};;
            MORPH)
                markexpr="${markexpr}"'\|{MB}';
                unmarkexpr=${unmarkexpr/\\\|\{MB\}/};;
            DERIVATION)
                markexpr="${markexpr}"'\|{DB}';
                unmarkexpr=${unmarkexpr/\\\|\{DB\}/};;
            NEWWORD)
                markexpr="${markexpr}"'\|{WB}';
                unmarkexpr=${unmarkexpr/\\\|\{WB\}/};;
            ETYM)
                markexpr="${markexpr}"'\|{XB}';
                unmarkexpr=${unmarkexpr/\\\|\{XB\}/};;
            STUB)
                markexpr="${markexpr}"'\|{STUB}';
                unmarkexpr=${unmarkexpr/\{STUB\}\\\|/};;
            *) echo "invalid argument for $1: $2"; print_help; exit 1;;
        esac
        shift 2
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
if test x${markexpr} = x ; then
    markexpr='\({WB}\|{MB}\|{DB}\|{XB}\|{wB}\)'
    unmarkexpr='{STUB}'
else
    markexpr='\('${markexpr#\\\|}'\)'
fi

omorfifile=$(find_omorfi segment)
if test -z "$omorfifile" ; then
    print_usage
    find_help segment
    exit 2
fi
analyse $@

