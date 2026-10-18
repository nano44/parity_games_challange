#!/usr/bin/env bash
# N5 SSI-GLOBAL sweep (box 3). Instances from deterministic committed generators (column gen; sha1 recorded): Oink tools at the
# scripts/setup_oink.sh pin, pgsolver_port.py, gen_deeptrap.sh, gen_padsae.sh, dlm_gen.py (DLM start pair used for dlm1/dlm2).
# Check per row: check_sol2.py (regions = Oink zlk, tl fallback labelled; harness/verify.py on both strategies).
# Output (COMMITTED): experiments/new/n5/<family>.csv. Usage: FAMS="..." NMAX=40 TO=600 BUDGET=600 ./run_n5.sh
cd "$(dirname "$0")"; ROOT=$(cd ../.. && pwd); mkdir -p out/n5 n5; TO=${TO:-600}
for fam in ${FAMS:-dlm1 dlm2}; do
 out=n5/$fam.csv; [ -s $out ] || echo "family,N,n,gen,sha1,n5_iterations,fallback,evals,secs,check" > $out; t0=$(date +%s)
 for N in $(seq ${NMIN:-1} ${NMAX:-40}); do
  if [ -n "$BUDGET" ] && [ $(( $(date +%s) - t0 )) -gt $BUDGET ]; then echo "$fam,$N,,,,,,,BUDGET${BUDGET}_REACHED," >> $out; break; fi
  f=out/n5/${fam}_$N.pg; st=()
  case $fam in
   dlm1|dlm2) gen="python3 experiments/new/dlm_gen.py ${fam#dlm} $N"; (cd $ROOT && $gen) > $f 2> out/n5/${fam}.start; st=(--start "$(sed -n 1p out/n5/${fam}.start)" "$(sed -n 2p out/n5/${fam}.start)");;
   deeptrap) gen="experiments/new/gen_deeptrap.sh $N"; (cd $ROOT && $gen) > $f;;
   padsae) gen="experiments/new/gen_padsae.sh $N"; (cd $ROOT && $gen) > $f;;
   switchallexp|switchbestexp|recursiveladder) gen="python3 experiments/hard-families/pgsolver_port.py $fam $N"; (cd $ROOT && $gen) > $f;;
   *) gen="tools/oink/build/$fam $N"; (cd $ROOT && $gen) > $f;;
  esac
  sha=$(sha1sum $f | cut -c1-40)
  res=$(timeout $TO python3 n5.py n5 $f out/n5/cur_$fam.sol "${st[@]}" 2>&1 | grep RESULT)
  if [ -z "$res" ]; then echo "$fam,$N,,$gen,$sha,,,,TIMEOUT$TO," >> $out; break; fi
  g() { echo "$res" | grep -o "$1=[^ ]*" | cut -d= -f2; }
  chk=$(timeout 3600 python3 check_sol2.py $f out/n5/cur_$fam.sol); [ -z "$chk" ] && chk=CHECK_CRASH
  echo "$fam,$N,$(g n),$gen,$sha,$(g iterations),$(g fallback),$(g evals),$(g secs),$chk" >> $out
 done
done
