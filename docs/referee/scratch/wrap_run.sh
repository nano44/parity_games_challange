#!/usr/bin/env bash
# REFEREE s33: main sets of wrap_replay.py (no control). Logs: wrap_logs/main_<mode>_<family>_<seed>_p<PERM>.out
cd "$(dirname "$0")"; mkdir -p wrap_logs
jobs=()
for mode in xi spec; do for fam in rand dup even odd twin; do for perm in 0 1; do
  for spec in "3301 5000 8" "3302 2000 12" "3303 500 24" "3304 100 40"; do
    set -- $spec
    jobs+=("PERM=$perm python3 -I wrap_replay.py $mode $fam $1 $2 $3 > wrap_logs/main_${mode}_${fam}_$1_p${perm}.out 2>&1")
  done; done; done; done
printf '%s\n' "${jobs[@]}" | xargs -P 4 -I{} bash -c "{}"
echo "jobs ${#jobs[@]} done $(date -u +%Y-%m-%dT%H:%M:%SZ)"
