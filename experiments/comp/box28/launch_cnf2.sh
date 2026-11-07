#!/bin/bash
# L-COMP box 28 (Lead 05:04Z): after regression (a) is complete (log/d3cnf2/done) with all 16 d 3 L 9 cubes UNSAT, stop the cnf.py
# d 4 roots and run cnf2 on the 8 PAIR-SWAP roots: R4_L14 (𝓛^R_4, T >= 14, PAR 2) and ISO_L13 (ISO, T >= 13, PAR 1), TLIM 4 h per cube
# then Xi-split (acube28.py, resumable). Idempotent: drivers already running are not doubled. Verdicts are DATA (cnf2 not audited).
cd "$(dirname "$0")"
until [ -f log/d3cnf2/done ]; do sleep 20; done
n=0; for c in $(seq 0 15); do grep -q "RESULT d 3 T >= 9 .*: UNSAT" log/d3cnf2/L9_c$c.log && n=$((n+1)); done
if [ "$n" != 16 ]; then echo "$(date -u +%FT%TZ) regression (a) NOT complete: $n/16 UNSAT; cnf2 d 4 NOT launched" >> log/launch_cnf2.out; exit 1; fi
echo "$(date -u +%FT%TZ) regression (a): 16/16 UNSAT; stopping cnf.py d 4 roots, launching cnf2" >> log/launch_cnf2.out
for p in $(pgrep -f "box27/cnf.py 4 14 log/sample/c"); do kill $p; done
for f in log/sample/cad_L14_c0.log log/sample/cad_L14_c42.log log/sample/cad_L14_c2.log; do grep -q RESULT $f || echo "stopped $(date -u +%FT%TZ): cores moved to cnf2 (Lead 05:04Z)" >> $f; done
start() { tag=$1; shift; [ -f cubes/$tag/RUNNING ] && kill -0 $(cat cubes/$tag/RUNNING) 2>/dev/null && { echo "$tag already running"; return; }
  mkdir -p cubes/$tag; env "$@" setsid nohup python3 acube28.py $tag 4 $L >> log/acube_$tag.out 2>&1 < /dev/null & echo $! > cubes/$tag/RUNNING; echo "$tag launched pid $!" >> log/launch_cnf2.out; }
L=14 start R4_L14 ENC=cnf2 TLIM=14400 PAR=2 ROOTS=40,0,42,2,8,10,32,34
L=13 start ISO_L13 ENC=cnf2 ISO=1 TLIM=14400 PAR=1 ROOTS=40,0,42,2,8,10,32,34
