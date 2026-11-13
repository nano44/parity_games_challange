#!/bin/bash
# REFEREE successor 36: reproduces docs/referee/scratch/gkx_logs/*.out (first review of P-N5-EXP, l-red-b 350d84eb).
# Run from the repository root: bash docs/referee/scratch/gkx_logs/s36_run.sh   (resumable: a stage with its .out present is skipped)
# The frozen inputs are read from git objects into a temporary directory; nothing outside gkx_logs/ is written.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
T="$HERE/.."
C=350d84eb6602003172d0d3dd67e0ef2d0c72d2f8
TR=5d7aab0f19f664034567c3bf4f41bcf9e1684d20
W="$(mktemp -d)"
mkdir -p "$W/G" "$W/pg" "$W/src"
for k in 3 4 5 6 7 8 9 10 11 12 13 14; do git show $C:experiments/red-b/data/b6b/G/G_$k.json > "$W/G/G_$k.json"; done
for k in 3 4 5 6 7 8 9 10 11; do git show $C:experiments/red-b/data/b6b/pg/G_${k}_g3.pg > "$W/pg/G_${k}_g3.pg"; done
git show $C:docs/red-b/P-N5-EXP.md > "$W/P-N5-EXP.md"
git show $TR:docs/red/P-N5-REALIZE.md > "$W/src/P-N5-REALIZE.md"; git show $TR:docs/RESULTS.md > "$W/src/RESULTS.md"
git show $TR:docs/GAPS.md > "$W/src/GAPS.md"; git show $C:TARGET.md > "$W/src/TARGET.md"; git show $C:CLAUDE.md > "$W/src/CLAUDE.md"
P="python3 -I $T/gkx.py"
st() { [ -s "$HERE/$1.out" ] && { echo "skip $1"; return 1; }; echo "run $1"; return 0; }
st gen && { sha1sum "$W/P-N5-EXP.md" | cut -c1-40 | sed 's/^/packet sha1 /'; $P gen "$W/G" 3 4 5 6 7 8 9 10 11 12 13 14; } > "$HERE/gen.tmp" && mv "$HERE/gen.tmp" "$HERE/gen.out"
st member && $P member 3 4 5 6 7 8 9 10 11 12 13 14 > "$HERE/member.tmp" && mv "$HERE/member.tmp" "$HERE/member.out"
st run && $P run 3 4 5 6 7 8 9 10 11 12 13 14 > "$HERE/run.tmp" && mv "$HERE/run.tmp" "$HERE/run.out"
st facts_run && $P facts 3 4 5 6 7 8 9 10 > "$HERE/facts_run.tmp" && mv "$HERE/facts_run.tmp" "$HERE/facts_run.out"
st facts_arb && { $P facts 3 4 5 6 7 8 9 --arb 3000 1; $P facts 4 6 8 --arb 2000 2 --mode w0; $P facts 4 6 8 --arb 2000 3 --mode free; $P facts 4 6 8 --arb 2000 4 --mode u0; } > "$HERE/facts_arb.tmp" && mv "$HERE/facts_arb.tmp" "$HERE/facts_arb.out"
st facts_all && { $P facts 3 --all u0; $P facts 4 --all w0u0; } > "$HERE/facts_all.tmp" && mv "$HERE/facts_all.tmp" "$HERE/facts_all.out"
st facts_ctrl && { for c in 1 2 3 4 5 6 7 8 9 10; do $P facts 6 --ctrl $c; done; $P facts 6 --arb 500 5 --mode u0 --ctrl 11; } > "$HERE/facts_ctrl.tmp" && mv "$HERE/facts_ctrl.tmp" "$HERE/facts_ctrl.out"
st causal && { $P causal 3 4 5 6 7 8 9 10; $P causal 4 6 8 --arb 2000 9; $P causal 6 --arb 2000 9 --ctrl 1; $P causal 6 --arb 2000 9 --ctrl 2; } > "$HERE/causal.tmp" && mv "$HERE/causal.tmp" "$HERE/causal.out"
st abs && { $P abs 3 4 5 6 7 8 9; $P abs 6 --ctrl 1; $P abs 6 --ctrl 2; } > "$HERE/abs.tmp" && mv "$HERE/abs.tmp" "$HERE/abs.out"
st resp && { $P resp 3 4 5 6 7 8 9 10 11 12 13; for c in 1 2 3; do $P resp 6 --ctrl $c; done; } > "$HERE/resp.tmp" && mv "$HERE/resp.tmp" "$HERE/resp.out"
st orders && $P orders 3 4 5 6 7 8 --reps 200 > "$HERE/orders.tmp" && mv "$HERE/orders.tmp" "$HERE/orders.out"
st sizes && $P sizes "$W/pg" 3 4 5 6 7 8 9 10 11 > "$HERE/sizes.tmp" && mv "$HERE/sizes.tmp" "$HERE/sizes.out"
st quotes && python3 -I "$T/gkx_quotes.py" "$W/P-N5-EXP.md" R104P="$W/src/P-N5-REALIZE.md" R117="$W/src/RESULTS.md" TARGET="$W/src/TARGET.md" CLAUDE="$W/src/CLAUDE.md" GAPS="$W/src/GAPS.md" > "$HERE/quotes.tmp" && mv "$HERE/quotes.tmp" "$HERE/quotes.out"
N5="python3 -I $T/gkx_n5.py"
st n5_pg && $N5 gk 3 12 --pg "$W/pg" --pgonly > "$HERE/n5_pg.tmp" && mv "$HERE/n5_pg.tmp" "$HERE/n5_pg.out"
st n5_ctl && { for c in start win lastfb nonmover noesc rank revE; do $N5 gk 4 5 --ctl $c; done; } > "$HERE/n5_ctl.tmp" && mv "$HERE/n5_ctl.tmp" "$HERE/n5_ctl.out"
st lem && { python3 -I "$T/gkx_lem.py" 5 40 3; python3 -I "$T/gkx_lem.py" 7 30 4; } > "$HERE/lem.tmp" && mv "$HERE/lem.tmp" "$HERE/lem.out"
# the long stage last (k = 3..9: about 3 minutes on the engine; k = 10: about 4 more; pass N5MAX=10 to include it)
st n5 && $N5 gk 3 ${N5MAX:-9} --pg "$W/pg" > "$HERE/n5.tmp" && mv "$HERE/n5.tmp" "$HERE/n5.out"
rm -rf "$W"
echo done
