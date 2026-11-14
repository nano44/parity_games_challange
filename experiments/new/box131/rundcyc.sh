#!/bin/bash
# L-NEW box 131: dcyc.py (CASC digraph per FL run) on the 813 DISTINCT (game, start) pairs of si/anc58/corpus_fixed.lst (Erratum E-1).
cd "$(dirname "$0")/../.."
one() { timeout 900 python3 -I new/box131/dcyc.py "$@" 2>&1 | grep '^DCYC\|Error\|error' | sed "s|^|GAME $* |"; }; export -f one
sort -u si/anc58/corpus_fixed.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box131/d_corpus.txt
