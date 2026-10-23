#!/usr/bin/env bash
# All hard families at L-NEW's sizes (docs/new/N8d-single.md §2), R1 + R2 seeds 1..10, via bench.py.
# Output: experiments/n8d-second/results/<family>.kl2.csv. Usage: run_families.sh [FAMILY ...]
set -u
cd "$(dirname "$0")/../.."
B=experiments/n8d-second/bench.py
R=experiments/n8d-second/results
mkdir -p "$R"
OK=tools/oink/build
HF="python3 experiments/hard-families/pgsolver_port.py"
declare -A GEN SIZES
GEN[famF]="python3 experiments/red/kl/famgen.py F {N}";      SIZES[famF]="0 1 2 3 4"
GEN[famG]="python3 experiments/red/kl/famgen.py G {N}";      SIZES[famG]="0 1 2 3 4"
GEN[famH]="python3 experiments/red/kl/famgen.py H {N}";      SIZES[famH]="0 1 2 3 4 5"
GEN[famL]="python3 experiments/new/kl/gen_lk.py {N}";        SIZES[famL]="0 2 3 4 5 6"
GEN[tc]="$OK/tc {N}";                                        SIZES[tc]="1 2 4 6 8 10 12 14"
GEN[tc+]="$OK/tc+ {N}";                                      SIZES[tc+]="1 2 3 4 5 6"
GEN[switchallexp]="$HF switchallexp {N}";                    SIZES[switchallexp]="1 2 3 4 5 6 7 8 9 10"
GEN[switchbestexp]="$HF switchbestexp {N}";                  SIZES[switchbestexp]="1 2 3 4 5 6 7 8 10 12"
GEN[counter_qpt]="$OK/counter_qpt {N}";                      SIZES[counter_qpt]="2 4 8 12 16 20"
GEN[counter_m]="$OK/counter_m {N}";                          SIZES[counter_m]="2 4 8 12 16 20"
GEN[counter_rr]="$OK/counter_rr {N}";                        SIZES[counter_rr]="2 4 8 12 16 20"
GEN[counter_dp]="$OK/counter_dp {N}";                        SIZES[counter_dp]="2 4 8 12 16 20"
GEN[counter_core]="$OK/counter_core {N}";                    SIZES[counter_core]="2 4 6 8 10"
GEN[counter_ortl]="$OK/counter_ortl {N}";                    SIZES[counter_ortl]="2 4 6 8 10"
GEN[counter_rob]="$OK/counter_rob {N}";                      SIZES[counter_rob]="1 2 3 4 5"
GEN[counter_symsi]="$OK/counter_symsi {N}";                  SIZES[counter_symsi]="1 2 3 4 6"
GEN[recursiveladder]="$HF recursiveladder {N}";              SIZES[recursiveladder]="2 4 6 8 10"
FAMS="${*:-famF famG famH famL counter_qpt counter_m counter_rr counter_ortl counter_symsi recursiveladder counter_dp counter_core counter_rob tc+ tc switchbestexp switchallexp}"
for f in $FAMS; do
  python3 $B family "$f" --gen "${GEN[$f]}" --sizes ${SIZES[$f]} --seeds 1 2 3 4 5 6 7 8 9 10 --jobs "${JOBS:-2}" \
    --timeout 7200 --out "$R/$f.kl2.csv" > "$R/$f.kl2.log" 2>&1
  echo "$f exit $? $(tail -1 "$R/$f.kl2.log")"
done
