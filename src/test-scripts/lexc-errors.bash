#!/bin/bash
if fgrep ERRORMACRO generated/omorfi.lexc ; then
    echo lexc is broken
    exit 1
fi
if test -f generated/omorfi.dix ; then
    if fgrep '<s n="ERROR"' generated/omorfi.dix ; then
        echo dix is broken
        exit 1
    fi
fi
exit 0
