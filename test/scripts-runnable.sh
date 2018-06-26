#!/bin/bash
for f in ../src/bash/omorfi-*.bash ; do
    if test -x "$f" ; then
        if ! "$f" --help ; then
            echo "broken help for $f"
            exit 1
        elif ! "$f" --version ; then
            echo "broken version for $f"
            exit 1
        fi
    fi
done
for f in ../src/python/omorfi-*.py ; do
    if test -x "$f" ; then
        if ! "$f" --help ; then
            echo "broken help for $f"
            exit 1
        fi
    fi
done
