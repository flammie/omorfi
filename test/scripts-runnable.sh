#!/bin/bash
for f in ../src/scripts/*sh ; do
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

