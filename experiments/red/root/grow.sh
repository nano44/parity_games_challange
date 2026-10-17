#!/usr/bin/env bash
# L-RED box 7 (produced on Opus 5.5): growth chain for #DIRTY per phase vs n (GAP-A-M §22c target (2a)).
# Stage i: dtl_search.py --fitness root (ROOTFIT=dirty) from the previous stage's best with --grow K fresh vertices,
# STEPS mutation steps; then one table row from root/rootfit.py (L-ALG dtl_rootmono.py unmodified) in BOTH orders.
# Usage (from experiments/red; LALGR_DIR set): root/grow.sh ORDER SEED START.pg STEPS K STAGES OUTDIR
set -uo pipefail
order=$1 seed=$2 cur=$3 steps=$4 k=$5 stages=$6 out=$7; mkdir -p "$out"
for i in $(seq 1 "$stages"); do
  nxt="$out/g${seed}_s$i.pg"
  ROOTFIT=dirty DTL_ORDER=$order python3 dtl/dtl_search.py x 1 --fitness root --seed $((seed * 100 + i)) --steps "$steps" \
    --hb 500 --from "$cur" --grow "$k" --out "$nxt" > "$out/g${seed}_s$i.log" 2>&1
  n=$(grep -c "^[0-9]" "$nxt"); n=$((n))
  ro=$(DTL_ORDER=oink python3 root/rootfit.py "$nxt" | sed 's/.*{/{/'); rs=$(DTL_ORDER=stable python3 root/rootfit.py "$nxt" | sed 's/.*{/{/')
  echo "ROW stage=$i n=$n climb_order=$order oink=$ro stable=$rs" ; cur="$nxt"
done
