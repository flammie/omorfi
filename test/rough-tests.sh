#!/bin/sh
hfst-lookup ../src/morphology.omor.hfst < wordforms.list > wordforms.anals
if grep '+?' wordforms.anals ; then
    echo "following known wordforms were missing from ../src/morphology.omor.hfst:"
    grep '+?' wordforms.anals
    exit 1
fi
