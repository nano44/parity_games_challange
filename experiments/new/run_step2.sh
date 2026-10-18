#!/usr/bin/env bash
# N1 gauntlet step 2 (box 2): N1 = anneal_c (input priorities, no merging = --nocompress semantics) on hard-bench families.
# Every instance comes from a deterministic committed generator (no seeds): Oink tools at the pin in scripts/setup_oink.sh,
# or experiments/hard-families/pgsolver_port.py. The sha1 of each generated file is recorded, so a lost out/ loses no evidence:
# regenerate with the command in column gen and compare sha1. Solutions are checked by check_sol2.py (regions = Oink zlk, Zielonka in C++; tl only on zlk timeout, labelled; + harness/verify.py
# on both players' positional strategies). Output (COMMITTED): experiments/new/step2/<family>.csv. $TO s per run; a family stops
# at its first timeout. Usage: FAMS="tc+ counter_m" NMAX=40 TO=900 ./run_step2.sh
cd "$(dirname "$0")"; ROOT=$(cd ../.. && pwd); mkdir -p out/step2 step2; TO=${TO:-900}
for fam in ${FAMS:-tc+ counter_m counter_rr counter_rob switchbestexp}; do
 out=step2/$fam.csv
 [ -s $out ] || echo "family,N,n,gen,sha1,vj_switchall_plain,phases,even_iters,odd_iters,max_phase,secs,check" > $out
 for N in $(seq ${NMIN:-1} ${NMAX:-40}); do
  f=out/step2/${fam}_$N.pg
  case $fam in
   switchallexp|switchbestexp|recursiveladder) gen="python3 experiments/hard-families/pgsolver_port.py $fam $N";;
   *) gen="tools/oink/build/$fam $N";;
  esac
  (cd $ROOT && $gen) > $f 2>/dev/null || { echo "$fam,$N,,$gen,,,,,,,GENFAIL," >> $out; break; }
  sha=$(sha1sum $f | cut -c1-40)
  base=$(timeout 120 ./vjfast switch-all $f /dev/null 2>&1 | grep -o "with [0-9]*" | grep -o "[0-9]*"); [ -z "$base" ] && base=TO120
  res=$(timeout $TO ./anneal_c $f out/step2/cur_$fam.sol 2>&1 | grep RESULT)
  if [ -z "$res" ]; then echo "$fam,$N,,$gen,$sha,$base,,,,,TIMEOUT$TO," >> $out; break; fi
  g() { echo "$res" | grep -o "$1=[^ ]*" | cut -d= -f2; }
  chk=$(timeout 7200 python3 ${CHK:-check_sol2.py} $f out/step2/cur_$fam.sol); [ -z "$chk" ] && chk=CHECK_TIMEOUT
  echo "$fam,$N,$(g n),$gen,$sha,$base,$(g phases),$(g even_iters),$(g odd_iters),$(g max_phase),$(g secs),$chk" >> $out
 done
done
