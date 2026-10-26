#!/bin/bash
# REFEREE-2 successor 17: EPC library runs and controls (restarted with the skip of configurations that have nothing to check).
cd "$(dirname "$0")"
export BUDGET=${BUDGET:-3000000}
python3 epc_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_noref_x3.txt 2>&1 &
python3 epc_check.py files ../R2-N5-KW/files.lst 2 > logs/c1o_503_x2.txt 2>&1 &
{ for M in plus2 nonC last noR0; do EPC_MUT=$M BUDGET=400000 python3 epc_check.py files ../R2-N5-STAU/lib41_noref.lst 1 > logs/mut_$M.txt 2>&1; done; } &
wait
