#!/bin/bash
# REFEREE successor 37: reproduces docs/referee/scratch/gkx_logs/s37_*.out (stage 5a of R-P-N5-EXP.md, section 13: the lane's fixes
# entries 2, 3, 5, 6 at claude/l-red-b 0c8fdf9e; supplementary direct tests of entry 4).
# Run from the repository root: bash docs/referee/scratch/gkx_logs/s37_run.sh
# Resumable: a stage with its .out present is skipped. About 5 minutes (stage 5a's logs and, below, stage 5b's). Needs the commits named in gkx5_quotes.py in the object
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
# ---- stage 5b (section 14): line L-3 and fixes entries 7, 8 at claude/l-red-b 10dfedb6 (needs claude/referee-2 f17a2708 in the object store)
P6="python3 -I $T/gkx6.py"
Q6="python3 -I $T/gkx6_quotes.py"
st s37_gloss && $P6 gloss 3 4 5 6 7 8 9 10 11 12 > "$HERE/s37_gloss.tmp" && mv "$HERE/s37_gloss.tmp" "$HERE/s37_gloss.out"
st s37_r3 && { $P6 r3 3 4 5 6 7 8 9 10 11 12 13 14; $P6 r3 5 6 --ctrl 1; } > "$HERE/s37_r3.tmp" && mv "$HERE/s37_r3.tmp" "$HERE/s37_r3.out"
st s37_xt && $P6 xt 3 4 5 6 7 8 9 10 11 12 13 14 > "$HERE/s37_xt.tmp" && mv "$HERE/s37_xt.tmp" "$HERE/s37_xt.out"
st s37_e7_quotes && { $Q6 entries; $Q6 spoil | tail -n 1; } > "$HERE/s37_e7_quotes.tmp" && mv "$HERE/s37_e7_quotes.tmp" "$HERE/s37_e7_quotes.out"
st s37_e7_pins && $Q6 pins > "$HERE/s37_e7_pins.tmp" && mv "$HERE/s37_e7_pins.tmp" "$HERE/s37_e7_pins.out"
st s37_e7_facts && $Q6 facts > "$HERE/s37_e7_facts.tmp" && mv "$HERE/s37_e7_facts.tmp" "$HERE/s37_e7_facts.out"
st s37_linedata && $Q6 linedata > "$HERE/s37_linedata.tmp" && mv "$HERE/s37_linedata.tmp" "$HERE/s37_linedata.out"
st s37_line_L3 && $Q6 line L3 > "$HERE/s37_line_L3.tmp" && mv "$HERE/s37_line_L3.tmp" "$HERE/s37_line_L3.out"
# ---- stage 5b part (ii) (section 15): lines L-4, L-5, L-6 and fixes entries 9, 10, 11 at claude/l-red-b 91d30d95
C7=91d30d95a
O7="--commit $C7 --from 1181 --labels REF1E=9ec40ff968ddc4a1c7f41a95d20aa6db6dbe40c3:docs/referee/R-P-N5-EXP.md,R104=5d7aab0f:docs/RESULTS.md --chain 35f14318a:1271,abde91635:1368,91d30d95a:1443 --pinfiles SHA1SUMS_b6b_fixes6,SHA1SUMS_b6b_fixes7,SHA1SUMS_b6b_fixes8"
st s37_gloss2 && $P6 gloss2 3 4 5 6 7 8 9 10 11 12 > "$HERE/s37_gloss2.tmp" && mv "$HERE/s37_gloss2.tmp" "$HERE/s37_gloss2.out"
st s37_e9_quotes && { $Q6 $O7 entries; $Q6 $O7 spoil | tail -n 1; } > "$HERE/s37_e9_quotes.tmp" && mv "$HERE/s37_e9_quotes.tmp" "$HERE/s37_e9_quotes.out"
st s37_e9_pins && $Q6 $O7 pins > "$HERE/s37_e9_pins.tmp" && mv "$HERE/s37_e9_pins.tmp" "$HERE/s37_e9_pins.out"
st s37_e9_facts && $Q6 --commit $C7 facts9 > "$HERE/s37_e9_facts.tmp" && mv "$HERE/s37_e9_facts.tmp" "$HERE/s37_e9_facts.out"
st s37_linechain && $Q6 --commit $C7 linechain L3 L4 L5 L6 > "$HERE/s37_linechain.tmp" && mv "$HERE/s37_linechain.tmp" "$HERE/s37_linechain.out"
st s37_line_L6 && $Q6 --commit $C7 line L6 > "$HERE/s37_line_L6.tmp" && mv "$HERE/s37_line_L6.tmp" "$HERE/s37_line_L6.out"
st s37_linedata_L6 && $Q6 --commit $C7 linedata > "$HERE/s37_linedata_L6.tmp" && mv "$HERE/s37_linedata_L6.tmp" "$HERE/s37_linedata_L6.out"
st s37_termxi && $Q6 --commit aeb90ac199aff97b7189666965d7fd7d7119cf29 termxi > "$HERE/s37_termxi.tmp" && mv "$HERE/s37_termxi.tmp" "$HERE/s37_termxi.out"
echo done
