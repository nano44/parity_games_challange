#!/bin/bash
# L-NEW box 132: dcyc2.py on the 813 DISTINCT (game, start) pairs of si/anc58/corpus_fixed.lst (Erratum E-1).
cd "$(dirname "$0")/../.."
one() { timeout 900 python3 -I new/box132/dcyc2.py "$@" 2>&1 | grep '^DCYC2\|Error\|error' | sed "s|^|GAME $* |"; }; export -f one
sort -u si/anc58/corpus_fixed.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box132/d2_corpus.txt
