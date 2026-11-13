#!/bin/bash
# L-COMP box 47: the PORT CHECK (chk47.py): one47 (C) vs one217.py (key / howard / seq) vs n5v spec, state by state, must-0 mism.
# Sets: towers (5), rand 200 (eg195 «acyc», seed 4701, half with a random e-permutation), mut (10 gen47 mutants per tower, seed 4702, 1-10
# mutations incl. the e-numbering); control ONE47_CTRL=1 on the towers and mut (seed 4703, 4 per tower): mism must fire.
# Builds bin/one47, bin/mut47 (gcc -O2). Output out/chk47_<set>.out (each file is written whole; a set is skipped when its file has a TOTAL line).
# env LNEW217 (archive of claude/l-new a32a588d: experiments/new experiments/si/si.py experiments/harness experiments/n5-second experiments/hard-families)
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p out bin
: "${LNEW217:?set LNEW217}"; export LNEW="$LNEW217"
gcc -O2 -Wno-unused-function -I. -o bin/one47 one47.c && gcc -O2 -Wno-unused-function -I. -o bin/mut47 mut47.c || exit 1
r() { local o=out/chk47_$1.out; shift; grep -q '^TOTAL' $o 2>/dev/null && return; python3 chk47.py "$@" > $o.tmp 2> $o.err && mv $o.tmp $o; }
r towers towers
r rand rand 4701 200
r mut mut 4702 10
ONE47_CTRL=1 r ctrl_towers towers
ONE47_CTRL=1 r ctrl_mut mut 4703 4
echo "run47b done"
