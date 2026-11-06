#!/bin/bash
# L-RED R214 exact scan: for mover z (even; sigma_l covers z+1), smallest r with UNSAT. Usage: scan.sh MODE d H z r0 cap   (MODE NT|ANY|T)
# cwd experiments/red/r213. Logs ../r214/out/scan_<MODE>_d<d>_z<z>.log; resumable (skips r already answered in the log).
MODE=$1; d=$2; H=$3; z=$4; r=$5; cap=${6:-7200}; log=../r214/out/scan_${MODE}_d${d}_z${z}.log
while true; do
  if grep -q "r $r: UNSAT" "$log" 2>/dev/null; then echo "DONE z $z max $((r-1))" >> "$log"; break; fi
  if grep -q "r $r: SAT" "$log" 2>/dev/null; then r=$((r+1)); continue; fi
  case $MODE in NT) E="MOVENT=1";; ANY) E="MOVEANY=1";; T) E="";; esac
  env $E timeout $cap python3 move.py $d $H $z $r ../r214/out/${MODE}_d${d}_z${z}_r${r}.json >> "$log" 2>&1
  rc=$?; [ $rc -eq 124 ] && { echo "TIMEOUT z $z r $r cap $cap" >> "$log"; break; }
  grep -q "r $r: SAT" "$log" && r=$((r+1)) || { grep -q "r $r: UNSAT" "$log" || { echo "ERROR rc $rc" >> "$log"; break; }; }
done
