#!/bin/bash
# L-COMP box 46 item 2: use46.py (is a Ξ-cycle used by the key-rule run?) on every Ξ-cyclic genome of item 2: the tower variants, my frozen
# Ξ-cyclic sets (names from out/win46_x{mine,best}.out), L-NEW's 81 frozen (env LNEW212). Resumable per genome. Usage: run46e.sh
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
main() {
: "${LNEW212:?set LNEW212}"; N="$LNEW212/experiments/new"; O=out/use46.out; touch $O
one() { b=$(basename $1); grep -q "^$b " $O || python3 use46.py $1 >> $O 2>> $O.err; }
for f in inst/xtower/*.json; do one $f; done
for b in $(awk '{print $1}' out/win46_xmine.out); do f=$(ls ../box40/inst/$b ../box39/inst/$b ../box41/inst/$b ../box42/inst/$b ../box43/inst/$b ../box45/inst/$b 2>/dev/null | head -1); [ -n "$f" ] && one $f; done
for b in $(awk '{print $1}' out/win46_xbest.out); do f=$(ls ../box44/inst/$b ../box44/out/climb44/$b ../box45/out/climb45/$b 2>/dev/null | head -1); [ -n "$f" ] && one $f; done
for b in $(awk '{print $1}' out/win46_records.out out/win46_dead.out out/win46_corpus.out); do f=$(ls $N/box20[2-7]/inst/$b $N/box202/$b $N/box191/inst/$b 2>/dev/null | head -1); [ -n "$f" ] && one $f; done
echo "run46e done: $(wc -l < $O) rows"
}
main "$@"
