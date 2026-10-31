#!/bin/bash
# L-SI box 59: escw.py on anc58/corpus_fixed.lst; output anc58/escw_corpus.txt
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 900 python3 -I si/anc58/escw.py "$@" 2>&1 | grep -v '^$' | tr '\n' ' ')"; }; export -f one
xargs -P 4 -L 1 bash -c 'one "$@"' _ < si/anc58/corpus_fixed.lst > si/anc58/escw_corpus.txt
