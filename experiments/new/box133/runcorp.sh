#!/bin/bash
# L-NEW box 133: odxi.py on the 813 DISTINCT (game, start) pairs of si/anc58/corpus_fixed.lst (Erratum E-1).
cd "$(dirname "$0")/../.."
one() { timeout 900 python3 -I new/box133/odxi.py "$@" 2>&1 | grep '^ODXI\|Error\|error' | sed "s|^|GAME $* |"; }; export -f one
sort -u si/anc58/corpus_fixed.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box133/o_corpus.txt
