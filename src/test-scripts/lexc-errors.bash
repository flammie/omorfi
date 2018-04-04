#!/bin/bash
if fgrep ERRORMACRO generated/omorfi.lexc ; then
    echo lexc is broken
    exit 1
fi
exit 0
