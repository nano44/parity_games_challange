#!/usr/bin/env bash
# N1 bench sweep: anneal.py $FLAGS --check on every family in out/inst, N ascending, $TO s per run, stop a family at its
# first timeout/failure. Baseline: plain VJ switch-all (vjfast, best start). Ablation: anneal.py --j0 J (no annealing,
# straight at the final discount), 120 s cap. Output out/anneal/summary$TAG.csv.
cd "$(dirname "$0")"; mkdir -p out/anneal; FLAGS=${FLAGS:---nocompress}; TO=${TO:-600}; out=out/anneal/summary$TAG.csv
echo "family,N,n,switchall_plain,phases,even_iters,odd_iters,max_phase,secs,check,ablation_even_iters" > $out
for fam in ${FAMS:-switchallexp zadehexp randomfacetsubexp dlmm_ML dlmm_bland cunninghamexp gated_bland recursiveladder counter_dp counter_core counter_ortl counter_qpt counter_symsi tc fhz_padded gated_zadehexp gated_switchallexp counter_m counter_rr counter_rob tc+ switchbestexp gated_switchbestexp}; do
 for N in 1 2 3 4 5 6 7 8 9 10 11 12; do
  f=out/inst/${fam}_$N.pg; [ -s $f ] || continue
  base=$(timeout 60 ./vjfast switch-all $f /dev/null 2>&1 | grep -o "with [0-9]*" | grep -o "[0-9]*"); [ -z "$base" ] && base=TO
  res=$(timeout $TO python3 anneal.py $f $FLAGS --check 2>&1 | grep RESULT)
  if [ -z "$res" ]; then echo "$fam,$N,,$base,,,,,TIMEOUT,," >> $out; break; fi
  g() { echo "$res" | grep -o "$1=[^ ]*" | cut -d= -f2; }
  chk=$(echo "$res" | grep -o "zielonka.*"); J=$(g phases)
  abl=$(timeout 120 python3 anneal.py $f $FLAGS --j0 $J 2>&1 | grep -o "even_iters=[0-9]*" | cut -d= -f2); [ -z "$abl" ] && abl=TO120
  echo "$fam,$N,$(g n),$base,$J,$(g even_iters),$(g odd_iters),$(g max_phase),$(g secs),$chk,$abl" >> $out
 done
done
echo SWEEP DONE >> $out
