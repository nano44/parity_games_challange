#!/usr/bin/env bash
# L-SI box 71 item (0): CONJECTURE PM (L-NEW box 165) in the frame. For m, K, T: every mover x and d = 0..2m-1: query desc(x) = d and
# moves(x) >= d + PLUS (PLUS = 2 tests PM; PLUS = 1 is the control: tight cases must be SAT somewhere). Prints one line per query.
m=$1; K=$2; T=$3; PLUS=${4:-2}; cd "$(dirname "$0")/../box70"
for x in $(seq 0 $((2*m-1))); do for d in $(seq 0 $((2*m-1))); do
  [ $((d+PLUS)) -gt $T ] && { echo "m $m K $K T $T x $x desc $d moves>=$((d+PLUS)) -> UNSAT (trivial: more than T moves)"; continue; }
  r=$(PMX=$x PMD=$d PMPLUS=$PLUS K=$K python3 frame.py $m pm $T | head -n 1 | grep -o -- "-> [A-Z]*.*")
  echo "m $m K $K T $T x $x desc $d moves>=$((d+PLUS)) $r"
done; done
