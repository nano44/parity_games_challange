#!/usr/bin/env bash
# All 17 families of L-NEW's N5 step-2 CSVs, 4 in parallel; logs out/<family>.log; BUDGET seconds of n5b time per family.
set -uo pipefail
cd "$(dirname "$0")"
BUDGET="${BUDGET:-600}"
FAMS="${*:-counter_core counter_dp counter_m counter_ortl counter_qpt counter_rob counter_rr counter_symsi recursiveladder switchallexp switchbestexp tc tc+ dlm1 dlm2 deeptrap padsae}"
printf '%s\n' $FAMS | xargs -P 4 -I{} sh -c "python3 cmp_family.py {} --budget $BUDGET --mode ${MODE:-orig} > out/{}_${MODE:-orig}.log 2>&1; tail -1 out/{}_${MODE:-orig}.log"
