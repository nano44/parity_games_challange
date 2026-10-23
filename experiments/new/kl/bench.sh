#!/bin/bash
# N8a bench: kl.py on family sizes -> experiments/new/kl/results/<family>.<rule>.csv; every solution checked by ../check_sol2.py.
# Usage: bench.sh family "N1 N2 ..." rule [timeout_s]
cd "$(dirname "$0")/../../.."
F=$1; SIZES=$2; RULE=$3; TO=${4:-1800}
O=experiments/new/out/kl; R=experiments/new/kl/results; mkdir -p $O $R
CSV=$R/$F.$RULE.csv; [ -f $CSV ] || echo "family,N,sha1,n,d,h,rule,iterations,iterations_dual,checks,verify,secs,oink_check" > $CSV
for N in $SIZES; do
  G=$O/$F-$N.pg; SOL=$O/$F-$N.$RULE.sol
  case $F in
    switchallexp|switchbestexp|recursiveladder) [ -f $G ] || python3 experiments/hard-families/pgsolver_port.py $F $N > $G ;;
    *) [ -f $G ] || tools/oink/build/$F $N > $G ;;
  esac
  SHA=$(sha1sum $G | cut -c1-12)
  LINE=$(timeout $TO python3 experiments/new/kl/kl.py $G --rule $RULE --sol $SOL 2>&1 | tail -1 | tr ',' ';')
  case "$LINE" in *verified*) LINE=$(echo "$LINE" | tr ';' ',');; *) LINE="$(grep -c . $G),,,$RULE,TIMEOUT-or-ERROR,,,${LINE:0:60},$TO";; esac
  if [ -s $SOL ]; then CHK=$(python3 experiments/new/check_sol2.py $G $SOL 120 | tr ',' ';'); else CHK="no solution"; fi
  echo "$F,$N,$SHA,$LINE,$CHK" | tee -a $CSV
  rm -f $SOL
done
