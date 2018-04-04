#!/bin/bash

function test1 {
    # https://github.com/flammie/omorfi/issues/44
    fsa="../src/generated/omorfi-ftb3.analyse.hfst"
    if test -r "$fsa" ; then
	# this test only applies to FTB3 version of morphology
	res=$(echo "123" | \
		   hfst-lookup --pipe $fsa \
		   | head -1 | cut -f2 | cut --delimiter=" " -f1)
	# In the buggy case this is 112233
	if [ "123" != "$res" ] ; then
	    return 1
	fi
    fi
}

test1
