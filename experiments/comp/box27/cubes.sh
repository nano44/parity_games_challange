#!/bin/bash
# L-COMP box 27: resumable cube driver for cnf.py. Usage: cubes.sh TAG d L [P] ; env W, P, SOLVER passed through; PAR (default 4).
# Cubes: SYM=1 (s_0(u_0) = s_0(v_0) = 0, a sound relabelling) x every assignment of the start bits of movers 2..2d-1.
# State: cubes/TAG/<id>.res holds the solver's RESULT line once a cube is finished; a relaunch skips finished cubes (idempotent).
# A SAT cube writes its model to cubes/TAG/<id>.json. Summary: cubes.sh TAG d L summary
TAG=$1; d=$2; L=$3; DIR=cubes/$TAG; mkdir -p $DIR
n=$((2*d-2))
if [ "$4" = "summary" ]; then
  tot=$((1<<n)); done_=$(ls $DIR/*.res 2>/dev/null | wc -l); sat=$(grep -l ": SAT" $DIR/*.res 2>/dev/null | wc -l)
  echo "TAG $TAG d $d L $L cubes $tot finished $done_ SAT $sat UNSAT $(grep -l ": UNSAT" $DIR/*.res 2>/dev/null | wc -l)"; exit 0; fi
for ((c=0; c<(1<<n); c++)); do
  [ -f $DIR/$c.res ] && continue
  cube=""; for ((i=0;i<n;i++)); do cube="$cube$((i+2)):$(( (c>>i)&1 )),"; done
  echo "$c $cube"
done | xargs -P ${PAR:-4} -L 1 bash -c 'SYM=1 CUBE=$1 python3 cnf.py '$d' '$L' '$DIR'/$0.json > '$DIR'/$0.log 2>&1 && grep RESULT '$DIR'/$0.log > '$DIR'/$0.res.tmp && mv '$DIR'/$0.res.tmp '$DIR'/$0.res'
