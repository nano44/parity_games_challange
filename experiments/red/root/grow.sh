#!/usr/bin/env bash
# L-RED box 7 (produced on Opus 5.5): growth chain for #DIRTY per phase vs n (GAP-A-M §22c target (2a)).
# Stage i: TRIES random growths of the previous stage's best (--grow K fresh vertices, --steps 0), keep the best-scoring
# one (a single blind growth destroyed the dirty phase: score 0 at every stage of the first run), then dtl_search.py
# --fitness root (ROOTFIT=dirty) for STEPS mutation steps from it; then one table row from root/rootfit.py (L-ALG dtl_rootmono.py unmodified) in BOTH orders.
# Usage (from experiments/red; LALGR_DIR set): root/grow.sh ORDER SEED START.pg STEPS K STAGES OUTDIR [TRIES=40]
set -uo pipefail
order=$1 seed=$2 cur=$3 steps=$4 k=$5 stages=$6 out=$7 tries=${8:-40}; mkdir -p "$out"
for i in $(seq 1 "$stages"); do
  nxt="$out/g${seed}_s$i.pg"
  bs=-2; gb="$out/g${seed}_s${i}_grown.pg"
  for t in $(seq 1 "$tries"); do
    sc=$(ROOTFIT=dirty DTL_ORDER=$order python3 dtl/dtl_search.py x 1 --fitness root --seed $((seed * 10000 + i * 100 + t)) \
      --steps 0 --from "$cur" --grow "$k" --out "$out/try.pg" 2>&1 | sed -n 's/^start: \([-0-9]*\) .*/\1/p')
    if [[ -n "$sc" ]] && (( sc > bs )); then bs=$sc; cp "$out/try.pg" "$gb"; fi
  done
  echo "GROWN stage=$i best_of_$tries=$bs"
  ROOTFIT=dirty DTL_ORDER=$order python3 dtl/dtl_search.py x 1 --fitness root --seed $((seed * 100 + i)) --steps "$steps" \
    --hb 500 --from "$gb" --out "$nxt" > "$out/g${seed}_s$i.log" 2>&1
  n=$(grep -c "^[0-9]" "$nxt"); n=$((n))
  ro=$(DTL_ORDER=oink python3 root/rootfit.py "$nxt" | sed 's/.*{/{/'); rs=$(DTL_ORDER=stable python3 root/rootfit.py "$nxt" | sed 's/.*{/{/')
  echo "ROW stage=$i n=$n climb_order=$order oink=$ro stable=$rs" ; cur="$nxt"
done
