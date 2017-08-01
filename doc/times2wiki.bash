#!/bin/bash

echo "## $(date --iso) times"
echo
for f in *.timeslog; do
    corpus=${f%.timeslog}
    echo "## ${corpus} "
    echo
    avgtime=$(awk '{SUM+=$2;} END {print SUM/NR;}' < ${f})
    rate=$(awk '{SUM+=$2;} END {print 1000000/(SUM/NR);}' < ${f})
    echo "* 1M tokens in $avgtime equals $rate tokens per second"
    echo
done
