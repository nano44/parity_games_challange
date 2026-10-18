#!/usr/bin/env bash
# Box 1 (i) sweep: renumbering hill climb for S5 (zadeh) and S6 (cunningham) on the bench families, N = 2..6.
# Output: out/renum/<fam>_<N>_<rule>.txt (log) and .pg (best renumbered game); summary out/renum/summary.csv.
cd "$(dirname "$0")"; mkdir -p out/renum
echo "family,N,n,rule,identity,best,secs" > out/renum/summary.csv
for fam in zadehexp cunninghamexp randomfacetsubexp dlmm_ML dlmm_bland gated_bland fhz_padded gated_zadehexp gated_switchallexp gated_switchbestexp switchallexp switchbestexp recursiveladder; do
 for N in 2 3 4 5 6; do
  f=out/inst/${fam}_$N.pg; n=$(head -1 $f | grep -o "[0-9]*"); n=$((n+1))
  [ $n -gt 400 ] && continue
  for rule in zadeh cunningham; do
   t0=$(date +%s)
   timeout 900 ./renum $rule $f --restarts 3 --steps 400 --seed $N --out out/renum/${fam}_${N}_$rule.pg > out/renum/${fam}_${N}_$rule.txt 2>&1
   t1=$(date +%s); r=$(grep RESULT out/renum/${fam}_${N}_$rule.txt)
   id=$(echo "$r" | grep -o "identity=[0-9]*" | cut -d= -f2); b=$(echo "$r" | grep -o "best=[0-9]*" | cut -d= -f2)
   [ -z "$r" ] && { id=$(head -1 out/renum/${fam}_${N}_$rule.txt | awk '{print $2}'); b="TIMEOUT>=$(grep -o ': [0-9]*$' out/renum/${fam}_${N}_$rule.txt | tail -1 | tr -d ': ')"; }
   echo "$fam,$N,$n,$rule,$id,$b,$((t1-t0))" >> out/renum/summary.csv
  done
 done
done
echo SWEEP DONE >> out/renum/summary.csv
