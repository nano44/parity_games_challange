#!/bin/bash
# REFEREE successor 37: reproduces docs/referee/scratch/gkx_logs/s37_*.out (stage 5a of R-P-N5-EXP.md, section 13: the lane's fixes
# entries 2, 3, 5, 6 at claude/l-red-b 0c8fdf9e; supplementary direct tests of entry 4).
# Run from the repository root: bash docs/referee/scratch/gkx_logs/s37_run.sh
# Resumable: a stage with its .out present is skipped. About 4 minutes. Needs the commits named in gkx5_quotes.py in the object
# store (git fetch origin claude/l-red-b claude/l-new claude/l-comp claude/l-red claude/referee-2 claude/vibrant-johnson-nxvvxo).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
T="$HERE/.."
P="python3 -I $T/gkx.py"
P5="python3 -I $T/gkx5.py"
Q5="python3 -I $T/gkx5_quotes.py"
E6=0c8fdf9ea
st() { [ -s "$HERE/$1.out" ] && { echo "skip $1"; return 1; }; echo "run $1"; return 0; }
st s37_quotes && { $Q5; $Q5 --spoil | tail -n 1; } > "$HERE/s37_quotes.tmp" && mv "$HERE/s37_quotes.tmp" "$HERE/s37_quotes.out"
st s37_pins && $Q5 --pins > "$HERE/s37_pins.tmp" && mv "$HERE/s37_pins.tmp" "$HERE/s37_pins.out"
st s37_facts && $Q5 --facts > "$HERE/s37_facts.tmp" && mv "$HERE/s37_facts.tmp" "$HERE/s37_facts.out"
# entry 6: the lane's k = 13 game against the game this lane's builder makes from this lane's genome (no N5 run)
st s37_pg13 && { W="$(mktemp -d)"; git show $E6:experiments/red-b/data/b6b/pg/G_13_g3.pg > "$W/G_13_g3.pg"; sha1sum "$W/G_13_g3.pg" | cut -c1-40 | sed 's/^/G_13_g3.pg sha1 /'; python3 -I "$T/gkx_n5.py" gk 13 13 --pg "$W" --pgonly; rm -rf "$W"; } > "$HERE/s37_pg13.tmp" && mv "$HERE/s37_pg13.tmp" "$HERE/s37_pg13.out"
# supplementary (entry 4; section 13.6): LEMMA' at every triple, exhaustive states, random states, re-runs, the lane's pinned outputs
st s37_all && { $P5 all 3 4 5 6 7 8 9 10 11 12 13; $P5 all 5 --ctrl 2; $P5 all 6 --ctrl 2; $P5 all 3 4 5 6 7 8 9 10 11 12 13 --frozen; } > "$HERE/s37_all.tmp" && mv "$HERE/s37_all.tmp" "$HERE/s37_all.out"
st s37_exh && { $P5 exh 3 4; for c in 1 2 3 4 5; do $P5 exh 4 --ctrl $c; done; } > "$HERE/s37_exh.tmp" && mv "$HERE/s37_exh.tmp" "$HERE/s37_exh.out"
st s37_arb && { $P5 arb 5 6 7 8 9 --n 3000 --seed 1; $P5 arb 5 6 7 8 9 --n 3000 --seed 2; $P5 arb 6 --n 3000 --seed 1 --ctrl 1; $P5 arb 6 --n 3000 --seed 1 --ctrl 2; } > "$HERE/s37_arb.tmp" && mv "$HERE/s37_arb.tmp" "$HERE/s37_arb.out"
st s37_rerun && {
  W="$(mktemp -d)"
  { $P unit 7; $P unit 7 --ctrl 1; } > "$W/unit.out"
  { $P abs 3 4 5 6 7 8 9; $P abs 6 --ctrl 1; $P abs 6 --ctrl 2; } > "$W/abs.out"
  { $P resp 3 4 5 6 7 8 9 10 11 12 13; for c in 1 2 3; do $P resp 6 --ctrl $c; done; } > "$W/resp.out"
  { $P causal 3 4 5 6 7 8 9 10; $P causal 4 6 8 --arb 2000 9; $P causal 6 --arb 2000 9 --ctrl 1; $P causal 6 --arb 2000 9 --ctrl 2; } > "$W/causal.out"
  for f in unit abs resp causal; do
    if cmp -s "$W/$f.out" "$HERE/$f.out"; then e=1; else e=0; fi
    echo "rerun $f: lines $(wc -l < "$W/$f.out") sha1 $(sha1sum "$W/$f.out" | cut -c1-40) byte-equal to the committed gkx_logs/$f.out: $e"
  done
  rm -rf "$W"
} > "$HERE/s37_rerun.tmp" && mv "$HERE/s37_rerun.tmp" "$HERE/s37_rerun.out"
st s37_lanecmp && $Q5 --lanecmp > "$HERE/s37_lanecmp.tmp" && mv "$HERE/s37_lanecmp.tmp" "$HERE/s37_lanecmp.out"
echo done
