#!/bin/bash
# Box 217 (b) tower-seeded climbs beyond N 56 (L-NEW successor 76), resumable (a record file that exists is skipped). FINAL lines to
# out/climbL217.out. Seeds: the box 212 towers lifted by TOP-ADD (climb217.lift, L-LOWER's l3/lift.py recipe), then climbed on T_key.
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; IT=${1:-100000}; mkdir -p out/rec
run() {  # TOWER LIFT SEED
  d=$(python3 -I -c "import json;G=json.load(open('../box212/inst/$1.json'));G=G.get('genome',G);print(max(G['lev'])+1+$2)")
  [ -f out/rec/rec_w2_d${d}_D2_s$3.json ] && return
  timeout 5400 python3 -I climb217.py 2 0 2 $3 $IT out/rec --from ../box212/inst/$1.json --lift $2 | grep '^FINAL' | sed "s/^/$1+$2 /" >> out/climbL217.out \
    || echo "TIMEOUT $1+$2 seed $3" >> out/climbL217.out
}
run HIT7_d28_F254 4 1001
run H6_d24_F126 8 1004
run HIT7_d28_F254 8 1003
run H5_d20_F62 12 1005
run HIT7_d28_F254 4 1002
