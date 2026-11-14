#!/bin/bash
# L-RED R214 (b) «support» query (Lead 01:22Z): least d at which a level-l mover (z = 2l; sigma_l covers 2l+1) moves >= r times.
# move.py d H z r with TMIN 0: SAT = witness (then certM); UNSAT is exact only for runs of <= H steps (exact iff H >= T^R(d)).
# Usage (any cwd): support.sh d H l r cap. Log out/support_d<d>_l<l>_r<r>_H<H>.log; an answered query is skipped.
cd "$(dirname "$0")/../r213"; d=$1; H=$2; l=$3; r=$4; log=../r214/out/support_d${d}_l${l}_r${r}_H${H}.log
grep -q "SAT solve" "$log" 2>/dev/null && exit 0
timeout ${5:-7200} python3 move.py $d $H $((2*l)) $r ../r214/out/support_d${d}_l${l}_r${r}_H${H}.json >> "$log" 2>&1 || echo "rc $? (124 = TIMEOUT cap ${5:-7200})" >> "$log"
