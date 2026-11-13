#!/bin/bash
# L-RED-B B6 attempt 2 / packet P-N5-EXP: runner for the rule G_k (resumable: a stage skips the lines its output file already holds).
# Usage (from anywhere): bash experiments/red-b/run_b6b.sh ROOT STAGE [KMAX]
#   ROOT  = a directory holding lnew/ (claude/l-new a143d406), lred/ (claude/l-red), trunk/ (trunk); rebuild commands in
#           docs/red-b/P-N5-EXP.md par. 10. Outputs in ROOT/out/; genomes in ROOT/G/ (the rule's output), ROOT/raw/ (gk.py --raw),
#           ROOT/norm/ (the raw files normalised by b6member.py: must be byte-equal to ROOT/G/); games in ROOT/pg/.
#   STAGE = gen | member | sim | lemma | one217 | ablate | bilad | ctrl | n5 | size | fit | all
#           (gen, member, lemma, ablate, bilad need no archive; sim, one217 need lnew (+ lred); ctrl, n5 need lnew + trunk)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$1"; STAGE="$2"; KMAX="${3:-10}"
mkdir -p "$ROOT/out" "$ROOT/G" "$ROOT/raw" "$ROOT/norm" "$ROOT/pg"
has() { [ -f "$1" ] && grep -q "^$2 " "$1"; }

gen() {
  for k in $(seq 3 "$KMAX"); do
    [ -f "$ROOT/G/G_$k.json" ] || (cd "$HERE" && python3 gk.py "$k" "$ROOT/G/G_$k.json" > /dev/null)
    [ -f "$ROOT/raw/G_$k.json" ] || (cd "$HERE" && python3 gk.py "$k" "$ROOT/raw/G_$k.json" --raw > /dev/null)
  done
}
member() {
  [ -f "$ROOT/trunk/docs/red/P-N5-REALIZE.md" ] && python3 "$HERE/b6member.py" --quote "$ROOT/trunk/docs/red/P-N5-REALIZE.md" > "$ROOT/out/member_quote.out"
  for k in $(seq 3 "$KMAX"); do
    has "$ROOT/out/member.out" "G_$k.json" || python3 "$HERE/b6member.py" "$ROOT/G/G_$k.json" >> "$ROOT/out/member.out"
    if ! has "$ROOT/out/member_raw.out" "G_$k.json"; then
      l=$(python3 "$HERE/b6member.py" --norm "$ROOT/norm" "$ROOT/raw/G_$k.json" | cut -d' ' -f1-23)
      cmp -s "$ROOT/norm/G_$k.json" "$ROOT/G/G_$k.json"; echo "$l normdiff $?" >> "$ROOT/out/member_raw.out"
    fi
  done
  : > "$ROOT/out/member_ctrl.out"
  for i in 1 2 3 4 5 6 7 8; do python3 "$HERE/b6member.py" --ctrl "$i" "$ROOT/G/G_5.json" | cut -d' ' -f1-23 >> "$ROOT/out/member_ctrl.out"; done
}
sim() {
  for k in $(seq 3 "$KMAX"); do
    has "$ROOT/out/sim.out" "G_$k.json" || python3 "$HERE/b6sim.py" "$ROOT/lnew" "$ROOT/lred" "$ROOT/G/G_$k.json" >> "$ROOT/out/sim.out"
  done
  B6SIM_CTRL=1 python3 "$HERE/b6sim.py" "$ROOT/lnew" "$ROOT/lred" "$ROOT/G/G_5.json" > "$ROOT/out/sim_ctrl.out"
}
lemma() {
  for k in $(seq 3 "$KMAX"); do
    has "$ROOT/out/lemma.out" "G_$k" || (cd "$HERE" && python3 b6lemma.py "$k") >> "$ROOT/out/lemma.out"
  done
  (cd "$HERE" && B6L_CTRL=1 python3 b6lemma.py 5 && B6L_CTRL=2 python3 b6lemma.py 5) > "$ROOT/out/lemma_ctrl.out"
}
one217() {
  for k in $(seq 3 "$KMAX"); do
    has "$ROOT/out/one217.out" "G_$k.json" || python3 "$ROOT/lnew/experiments/new/box217/one217.py" "$ROOT/G/G_$k.json" >> "$ROOT/out/one217.out"
  done
}
ablate() { (cd "$HERE" && python3 gkvar.py --all 4 5 6 7 8 9 10) > "$ROOT/out/ablate.out"; }
bilad() { (cd "$HERE" && python3 bilad.py 6 20000 1) > "$ROOT/out/bilad_d6.out"; }
n5() {
  for k in $(seq 3 "$KMAX"); do
    has "$ROOT/out/n5.out" "G_$k" || python3 "$HERE/b6n5.py" "$ROOT/lnew" "$ROOT/trunk" "$ROOT/pg" "$ROOT/G/G_$k.json" >> "$ROOT/out/n5.out"
  done
}
ctrl() {
  : > "$ROOT/out/n5_ctrl.out"
  B6N5_CTRL=1 python3 "$HERE/b6n5.py" "$ROOT/lnew" "$ROOT/trunk" "$ROOT/pg" "$ROOT/G/G_4.json" >> "$ROOT/out/n5_ctrl.out"
  B6N5_CTRL=2 python3 "$HERE/b6n5.py" "$ROOT/lnew" "$ROOT/trunk" "$ROOT/pg" "$ROOT/G/G_4.json" >> "$ROOT/out/n5_ctrl.out"
  B6N5_MODE=xi python3 "$HERE/b6n5.py" "$ROOT/lnew" "$ROOT/trunk" "$ROOT/pg" "$ROOT/G/G_4.json" "$ROOT/G/G_6.json" >> "$ROOT/out/n5_ctrl.out"
}
size() {
  python3 "$HERE/b6size.py" "$ROOT"/pg/G_*_g3.pg > "$ROOT/out/size.out"
  B6SIZE_CTRL=1 python3 "$HERE/b6size.py" "$ROOT/pg/G_3_g3.pg" > "$ROOT/out/size_ctrl.out"
}
fit() { python3 "$HERE/b6fit.py" "$ROOT/out/sim.out" "$ROOT/out/n5.out" > "$ROOT/out/fit.out"; }
case "$STAGE" in
  gen) gen ;; member) member ;; sim) sim ;; lemma) lemma ;; one217) one217 ;; ablate) ablate ;; bilad) bilad ;; n5) n5 ;;
  ctrl) ctrl ;; size) size ;; fit) fit ;;
  all) gen; member; sim; lemma; one217; ablate; bilad; ctrl; n5; size; fit ;;
esac
echo "run_b6b $STAGE KMAX $KMAX done $(date -u +%Y-%m-%dT%H:%M:%SZ)"
