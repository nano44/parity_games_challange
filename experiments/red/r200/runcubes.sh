#!/bin/bash
# L-RED R200: resumable cube-and-conquer over extra-level gate bits + extra start bits (256 cubes), 4 parts; relaunch = same command.
# usage (cwd experiments/red/r200): bash runcubes.sh <target.json> <tag>
t=$1; tag=$2
for p in 0 1 2 3; do
  log=out/cube_${tag}_p$p.log; [ -f $log ] && cat $log >> out/cube_${tag}_p$p.hist
  CUBEVARS=G,S0 CUBEPART=$p/4 CUBEDONE=out/cube_${tag}_p$p.hist nohup nice -n 19 timeout 36000 python3 xcnf.py $t 2 out/cube_${tag}_p$p.json > $log 2>&1 &
done
