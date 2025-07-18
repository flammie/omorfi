#!/bin/bash
if ! test -d generated ; then
    echo "Usage: $0 PATH-TO-APERTIUM-FIN"
    echo must be used in src/ dir such that ./generated exists
    exit 1
fi
if test $# != 1 ; then
    echo "Usage: $0 PATH-TO-APERTIUM-FIN"
    exit 1
fi
rm -v generated/apertium-fin.fin.lexc generated/apertium-fin.fin.rlx
make generated/apertium-fin.fin.lexc generated/apertium-fin.fin.rlx
if ! diff -u "$1/apertium-fin.fin.lexc" generated/apertium-fin.fin.lexc ; then
    echo "apply changes??"
    select a in yes no ; do
        if test $a = yes ;then
            cp -v generated/apertium-fin.fin.lexc "$1/"
        fi
        break
    done
fi
if ! diff -u "$1/apertium-fin.fin.rlx" generated/apertium-fin.fin.rlx ; then
    echo "apply changes ?"
    select a in yes no ; do
        if test $a = yes ; then
            cp -v generated/apertium-fin.fin.rlx "$1/"
        fi
        break
    done
fi
