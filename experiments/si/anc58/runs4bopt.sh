#!/bin/bash
# L-SI box 63: s4bopt.py (CAP 1024) on anc58/corpus_fixed.lst; output anc58/s4bopt_corpus.txt
cd "$(dirname "$0")/../.."
one() { echo "GAME $* $(timeout 600 python3 -I si/anc58/s4bopt.py "$@" 1024 2>&1 | tail -1)"; }; export -f one
xargs -P 4 -L 1 bash -c 'one "$@"' _ < si/anc58/corpus_fixed.lst > si/anc58/s4bopt_corpus.txt
