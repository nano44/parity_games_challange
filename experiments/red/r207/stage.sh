#!/bin/bash
# L-RED R207 staged ladder climbs (T^R lower bounds): for d = $1..$2, K seeds of forkclimb MODE=free SEEDT=<best of d-1>, I iters each,
# then keep the best (by T) as r207/best/R_d<d>.json. Usage: bash r207/stage.sh d_from d_to K I seedbase   (cwd experiments/red)
set -u
for d in $(seq $1 $2); do
  prev=r207/best/R_d$((d-1)).json
  for s in $(seq 1 $3); do
    MODE=free SEEDT=$prev python3 r197/forkclimb.py $d 2 $4 $(( $5 + s )) r207/out/R_d${d}_s$(( $5 + s )).json > r207/out/R_d${d}_s$(( $5 + s )).log 2>&1
  done
  python3 - $d <<'PY'
import json, sys, os, glob, shutil
sys.path[:0] = ['r187', 'r178']; import ideal
d = int(sys.argv[1]); best = None
for f in glob.glob(f'r207/out/R_d{d}_s*.json') + ([f'r207/best/R_d{d}.json'] if os.path.exists(f'r207/best/R_d{d}.json') else []):
    G = json.load(open(f)); T = len(ideal.traj(G)[0]) - 1
    if best is None or T > best[0]: best = (T, f)
print('STAGE d', d, 'best T', best[0], best[1]); G = json.load(open(best[1])); json.dump(G, open(f'r207/best/R_d{d}.json.tmp', 'w')); os.replace(f'r207/best/R_d{d}.json.tmp', f'r207/best/R_d{d}.json')
PY
done
