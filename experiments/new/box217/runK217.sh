#!/bin/bash
# Box 217 track B (L-NEW successor 76): the decisive question (Lead 09:15Z): extend full key enumeration from k = 7 to 8. Climb on
# (k(G), T_key) from the towers lifted by TOP-ADD, every genome field mutable (W-targets, Xi-targets, beta ranks / parities, e-order, start).
# Resumable; FINAL lines to out/climbK217.out.
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1 CLIMB217_OBJ=enum; IT=${1:-100000}; mkdir -p out/rec
run() {  # TOWER LIFT SEED
  d=$(python3 -I -c "import json;G=json.load(open('../box212/inst/$1.json'));G=G.get('genome',G);print(max(G['lev'])+1+$2)")
  [ -f out/rec/rec_w2_d${d}_D2_s$3_enum.json ] && return
  timeout 5400 python3 -I climb217.py 2 0 2 $3 $IT out/rec --from ../box212/inst/$1.json --lift $2 | grep '^FINAL' | sed "s/^/$1+$2 /" >> out/climbK217.out \
    || echo "TIMEOUT $1+$2 seed $3" >> out/climbK217.out
}
run HIT7_d28_F254 4 2001
run H6_d24_F126 4 2002
run HIT7_d28_F254 2 2003
