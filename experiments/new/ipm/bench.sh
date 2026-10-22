#!/bin/bash
# N6 bench: family sizes -> experiments/new/ipm/results/<family>.csv (committed); every solution checked by check_sol2.py
# (regions vs Oink zlk, strategies by harness/verify.py). Usage: [SOLVER=n6|n7] [N6PATH=central|weighted] bench.sh family "N1 N2 ..." [maxit]
cd "$(dirname "$0")/../../.."
F=$1; SIZES=$2; MAXIT=${3:-3000}
O=experiments/new/out/n6; R=experiments/new/ipm/results; mkdir -p $O $R
P=${N6PATH:-central}; export N6PATH=$P; SOLVER=${SOLVER:-n6}; [ $SOLVER = n7 ] && P=n7; CSV=$R/$F.$P.csv; [ -f $CSV ] || echo "family,N,sha1,n,nbin,d,bits,prec,it_cert,it_total,status,mu_final,secs,check" > $CSV
for N in $SIZES; do
  G=$O/$F-$N.pg; SOL=$O/$F-$N.$P.sol
  case $F in
    hij) python3 experiments/new/ipm/gen_hij.py $N > $G ;;
    switchallexp|switchbestexp|recursiveladder) python3 experiments/hard-families/pgsolver_port.py $F $N > $G ;;
    rand*) python3 experiments/harness/gen.py one $G $N ${F#rand} 2>/dev/null || exit 3 ;;
    *) tools/oink/build/$F $N > $G ;;
  esac
  SHA=$(sha1sum $G | cut -c1-12)
  LINE=$(N6STOPCERT=1 timeout 1800 python3 experiments/new/ipm/$SOLVER.py $G --maxit $MAXIT --sol $SOL)
  if [ -s $SOL ]; then CHK=$(python3 experiments/new/check_sol2.py $G $SOL 120 | tr ',' ';'); else CHK="no solution"; fi
  echo "$F,$N,$SHA,$LINE,$CHK" | tee -a $CSV
  rm -f $SOL
done
