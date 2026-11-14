#!/bin/bash
# L-COMP box 27: certify L-SI box 71's frame CNF (m 3, tk, T 13, K 2; DIMACS sha1 f3d4b6ad...) by a COMPLETE binary split on the
# variables VARS (default 2 8 14 = frame.py x(o, X) for options 0, 1, 2: «option o has the exit as Xi-target»): cube c sets var i
# to + if bit i of c is 1, else -. All 2^k cubes together cover every assignment, so «every cube formula UNSAT» = «the CNF UNSAT».
# Each cube: dimproof.py (Glucose 4 proof of CNF + units, cube formula written next to the proof) then drup.c on that cube formula.
# Resumable: a cube with q2_c<c>.chk containing «s VERIFIED» is done. Proofs deleted after VERIFIED. Usage: PDIR=dir ./lsicubes.sh
cd "$(dirname "$0")"; P="${PDIR:?}"; VARS=(${VARS:-2 8 14}); k=${#VARS[@]}; F="$P/m3_tk_T13_T20_K2_NOIM0.cnf"
for ((c=0; c<(1<<k); c++)); do
  [ -f "$P/q2_c$c.chk" ] && grep -q "^s VERIFIED" "$P/q2_c$c.chk" && continue
  cube=""; for ((i=0;i<k;i++)); do v=${VARS[$i]}; if (( (c>>i)&1 )); then cube="$cube$v,"; else cube="$cube-$v,"; fi; done; cube=${cube%,}
  pf="$P/q2_c$c.proof"
  python3 dimproof.py "$F" "$pf" "$cube" > "$P/q2_c$c.gen" 2>&1 || { echo "cube $c dimproof failed"; continue; }
  t0=$(date +%s); { ./drup "$pf.cnf" "$pf"; echo "drup wall $(( $(date +%s) - t0 )) s"; } > "$P/q2_c$c.chk" 2>&1
  grep -q "^s VERIFIED" "$P/q2_c$c.chk" && rm -f "$pf" "$pf.cnf"
  echo "cube $c ($cube): $(grep -h 'glucose4' "$P/q2_c$c.gen" | grep -o 'UNSAT [0-9.]* s\|SAT [0-9.]* s\|bytes [0-9]*' | tr '\n' ' ') $(grep -h '^s ' "$P/q2_c$c.chk")"
done
