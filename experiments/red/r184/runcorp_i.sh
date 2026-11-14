#!/bin/bash
# L-RED R184: cnidx.py on the 813 DISTINCT (game, start) lines of si/anc58/corpus_fixed.lst (RESULTS Erratum E-1).
cd "$(dirname "$0")/../.."
one() { timeout 900 python3 -I red/r184/cnidx.py "$@" 2>&1 | grep '^CNIDX\|Error\|error' | sed "s|^|GAME $* |"; }; export -f one
sort -u si/anc58/corpus_fixed.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > red/r184/i_corpus.txt
