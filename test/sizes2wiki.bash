#!/bin/bash

echo "## $(date --iso) sizes"
echo
for f in ../src/generated/omorfi-{omor,ftb3}.*.hfst ../src/generated/omorfi.{accept,lemmatise,segment,tokenise}.hfst; do
    size=$(ls -lh $f | awk '{print $5;}') 
    hfst-summarize -v $f > summary
    echo "### ${f} "
    echo
    echo "| *Feature* | *Value* |"
    echo "|:----------|--------:|"
    echo "| file size | $size |"
    fgrep "# of states" < summary | sed -e 's/# of /| /' -e 's/:/ | /' -e 's/$/ |/'
    fgrep "# of arcs" < summary | sed -e 's/# of /| /' -e 's/:/ | /' -e 's/$/ |/'
    fgrep 'average ' < summary | sed -e 's/^/| /' -e 's/:/ | /' -e 's/$/ |/'
    echo
done
rm summary -f
