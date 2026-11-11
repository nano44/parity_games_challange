#!/bin/bash
# L-COMP box 38 item 2(a) sampled grid (resumable: samp38.py checkpoints; a finished (N, M) has its rows in out/samp38.jsonl).
cd "$(dirname "$0")"
for nm in "3 9" "4 8" "6 6" "4 12" "6 10" "8 8" "6 18" "8 16" "12 12" "8 24" "16 16" "12 36" "16 32"; do
  set -- $nm; grep -q "\"N\": $1, \"M\": $2," out/samp38.jsonl 2>/dev/null && continue
  python3 samp38.py $1 $2 20000 38 out/samp38.jsonl.part_N$1M$2 && cat out/samp38.jsonl.part_N$1M$2 >> out/samp38.jsonl
done; echo SAMPDONE
