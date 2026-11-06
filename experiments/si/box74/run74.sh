#!/usr/bin/env bash
# L-SI box 74: resumable queue of frame «flips» queries (>= F key-order flips of the top pair (A_m, B_m) in a run of <= T steps with
# <= K external-bit changes). Job = "K m T F" -> log/fl_K<K>_m<m>_T<T>_F<F>.log (skipped if finished). No DIMACS kept.
cd "$(dirname "$0")"; mkdir -p log
for job in "$@"; do
  set -- $job; f=log/fl_K$1_m$2_T$3_F$4.log
  if [ -f "$f" ] && grep -q -- "-> \(SAT\|UNSAT\)" "$f"; then echo "skip $f"; continue; fi
  K=$1 python3 ../box70/frame.py $2 flips $3 $4 > "$f.part" 2>&1; mv "$f.part" "$f"
done
