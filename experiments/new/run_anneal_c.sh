#!/usr/bin/env bash
# N1 bench sweep with the C++ port (anneal_c; cross-checked against anneal.py on 1,000 games by xcheck_c.py). Per instance:
# plain VJ switch-all (vjfast), N1 (anneal_c, solution checked by check_sol.py: Zielonka + harness/verify.py), ablation
# (anneal_c --j0 J). $TO s per run; a family stops at its first timeout. Output out/anneal/summary_c.csv.
cd "$(dirname "$0")"; mkdir -p out/anneal; TO=${TO:-900}; out=out/anneal/summary_c$TAG.csv
echo "family,N,n,switchall_plain,phases,even_iters,odd_iters,max_phase,secs,check,ablation_even_iters" > $out
for fam in ${FAMS:-switchallexp switchbestexp zadehexp randomfacetsubexp dlmm_ML dlmm_bland cunninghamexp gated_bland recursiveladder tc tc+ counter_symsi counter_rr counter_dp counter_m counter_core counter_rob counter_ortl counter_qpt fhz_padded gated_zadehexp gated_switchallexp gated_switchbestexp}; do
 for N in $(seq 1 ${NMAX:-16}); do
  f=out/inst/${fam}_$N.pg; [ -s $f ] || continue
  base=$(timeout 120 ./vjfast switch-all $f /dev/null 2>&1 | grep -o "with [0-9]*" | grep -o "[0-9]*"); [ -z "$base" ] && base=TO
  res=$(timeout $TO ./anneal_c $f out/anneal/cur.sol 2>&1 | grep RESULT)
  if [ -z "$res" ]; then echo "$fam,$N,,$base,,,,,TIMEOUT,," >> $out; break; fi
  g() { echo "$res" | grep -o "$1=[^ ]*" | cut -d= -f2; }
  chk=$(timeout 1800 python3 check_sol.py $f out/anneal/cur.sol); J=$(g phases)
  abl=$(timeout 300 ./anneal_c $f --j0 $J 2>&1 | grep -o "even_iters=[0-9]*" | cut -d= -f2); [ -z "$abl" ] && abl=TO300
  echo "$fam,$N,$(g n),$base,$J,$(g even_iters),$(g odd_iters),$(g max_phase),$(g secs),$chk,$abl" >> $out
 done
done
echo SWEEP DONE >> $out
