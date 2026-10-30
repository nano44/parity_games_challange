#!/bin/bash
# L-SI box 53: rsearch.py batches (biased and unbiased), 100k games each; outputs si/sb53/rs_out.txt, violating games in si/sb53/rs_bad/.
cd "$(dirname "$0")/../.."
one() { timeout 3000 python3 -I si/sb53/rsearch.py $1 100000 $2 $3 $4 si/sb53/rs_bad 2>&1 | tail -3; }; export -f one
printf '%s\n' "1 10 3 1" "2 12 3 1" "3 14 2 1" "4 16 3 1" "5 20 2 1" "6 12 3 0" "7 16 3 0" "8 10 2 1" "9 14 3 1" "10 20 3 1" | xargs -P 3 -L 1 bash -c 'one "$@"' _ > si/sb53/rs_out.txt
