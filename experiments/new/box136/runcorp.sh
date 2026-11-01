#!/bin/bash
# L-NEW box 136: DOM=1 STRETCH=1 dmerge2.py on the 813 DISTINCT (game, start) pairs of si/anc58/corpus_fixed.lst (Erratum E-1).
cd "$(dirname "$0")/../.."
one() { DOM=1 STRETCH=1 timeout 900 python3 -I new/box136/dmerge2.py "$@" 2>&1 | grep '^DMERGE2SD\|Error\|error' | sed "s|^|GAME $* |"; }; export -f one
sort -u si/anc58/corpus_fixed.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box136/d_corpus.txt
