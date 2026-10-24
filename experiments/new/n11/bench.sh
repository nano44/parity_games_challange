#!/bin/bash
# N11 kill bench (frozen rule: docs/new/N11-proposal.md FREEZE, n5ht.py sha1 598cc900...). One row per instance:
# family,N,n,iterations,fallback,conflicts,n5_iterations,verify. Every row verified by check_sol2.py (Oink zlk + verify.py).
# Usage: bench.sh FAMILY Ns...   (FAMILY: switchallexp switchbestexp dlm1 dlm2 hlg file:<path>[,start])
cd "$(dirname "$0")"; ROOT=../../..; T=${T:-1800}; OUT=${OUT:-results}; mkdir -p $OUT ${TMPD:-/tmp/claude-0/-home-user-parity-games-challange/22882c9d-2ba6-5532-8fcb-69495b6f2941/scratchpad/n11}
fam=$1; shift
for N in "$@"; do
  D=${TMPD:-/tmp/claude-0/-home-user-parity-games-challange/22882c9d-2ba6-5532-8fcb-69495b6f2941/scratchpad/n11}; g=$D/${fam}_$N.pg; st=""
  case $fam in
    switchallexp|switchbestexp) python3 $ROOT/experiments/hard-families/pgsolver_port.py $fam $N > $g ;;
    dlm1|dlm2) python3 $ROOT/experiments/new/dlm_gen.py ${fam#dlm} $N > $g 2> $g.start; st=$g.start ;;
    hlg) cp $ROOT/experiments/red/kl24/instances/HLg_$N.pg $g ;;
    file) src=${N%%,*}; st=${N#*,}; [ "$st" = "$N" ] && st=""; g=$D/$(basename $src); cp $src $g; N=$(basename $src .pg) ;;
  esac
  if [ -n "$st" ]; then
    r=$(timeout $T python3 n5ht.py $g $g.sol --start "$(sed -n 1p $st)" "$(sed -n 2p $st)"); r5=$(timeout $T python3 $ROOT/experiments/new/n5.py n5 $g $g.n5sol --start "$(sed -n 1p $st)" "$(sed -n 2p $st)")
  else
    r=$(timeout $T python3 n5ht.py $g $g.sol); r5=$(timeout $T python3 $ROOT/experiments/new/n5.py n5 $g $g.n5sol)
  fi
  v=$(timeout 900 python3 $ROOT/experiments/new/check_sol2.py $g $g.sol 2>&1 | tail -1)
  n=$(echo "$r" | sed -n 's/.* n=\([0-9]*\).*/\1/p'); it=$(echo "$r" | sed -n 's/.*iterations=\([0-9]*\).*/\1/p')
  fb=$(echo "$r" | sed -n 's/.*fallback=\([0-9]*\).*/\1/p'); cf=$(echo "$r" | sed -n 's/.*conflicts=\([0-9]*\).*/\1/p')
  it5=$(echo "$r5" | sed -n 's/.*iterations=\([0-9]*\).*/\1/p')
  echo "$fam,$N,$n,${it:-TIMEOUT},$fb,$cf,${it5:-TIMEOUT},$v" | tee -a $OUT/$fam.csv
done
