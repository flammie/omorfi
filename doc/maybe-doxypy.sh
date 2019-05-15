#!/bin/bash

case $1 in
    *.py)
    doxypy $@;;
*)
    cat $@;;
esac
