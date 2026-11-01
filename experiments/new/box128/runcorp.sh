#!/bin/bash
# L-NEW box 128: pcount.py on the 813 DISTINCT (game, start) pairs of si/anc58/corpus_fixed.lst (Erratum E-1: 1,132 lines, 319 repeats).
cd "$(dirname "$0")/../.."
one() { timeout 900 python3 -I new/box128/pcount.py "$@" 2>&1 | grep '^PCOUNT\|Error\|error' | sed "s|^|GAME $* |"; }; export -f one
sort -u si/anc58/corpus_fixed.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box128/c_corpus.txt
