#!/bin/bash
# L-NEW box 135: dmerge.py on the 813 DISTINCT (game, start) pairs of si/anc58/corpus_fixed.lst (Erratum E-1).
cd "$(dirname "$0")/../.."
one() { timeout 900 python3 -I new/box135/dmerge.py "$@" 2>&1 | grep '^DMERGE\|Error\|error' | sed "s|^|GAME $* |"; }; export -f one
sort -u si/anc58/corpus_fixed.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box135/m_corpus.txt
