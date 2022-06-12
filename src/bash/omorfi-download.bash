#!/bin/bash

source $(dirname $0)/omorfi.bash
args=$@

downloadurl="https://github.com/flammie/omorfi/releases/download/v${omorfiapi/_alpha/-alpha}/omorfi-hfst-models-${omorfiapi}.tar.xz"

function print_help() {
    echo "Download or update omorfi binary models"
    echo
    echo "  -h, --help        Print this help dialog"
    echo "  -V, --version     Print version info"
    echo "  -v, --verbose     Print verbosely while processing"
    echo
    echo "If no FILENAMEs are given, input is read from standard input."
}

if test x$1 == x-h -o x$1 == x--help ; then
    omorfi_print_usage $0
    print_help
    exit 0
elif test x$1 == x-V -o x$1 == x--version ; then
    omorfi_print_version $0 0.9
    exit 0
elif test x$1 == x-v -o x$1 == x--verbose ; then
    verbose=verbose
    shift 1
fi
if ! ${wget} "${downloadurl}" ; then
    echo "Download failed"
    exit 1
fi
if ! ${tar} Jxvf omorfi-hfst-models-${omorfiapi}.tar.xz ; then
    echo "Unpacking failed"
    exit 1
fi
