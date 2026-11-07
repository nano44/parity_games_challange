#!/bin/bash
# L-COMP box 27: parallel form of lsicubes.sh (same cubes, same commands; Lead 09:35Z: 3 cubes at a time). Per-cube lock dir
# q2_c<c>.lock (mkdir is atomic); a cube whose .gen is still being written by a running dimproof (e.g. an orphan from the serial
# driver) is waited for, then checked. Usage: PDIR=dir PAR=3 ./lsicubes_par.sh [cube ids in order]
cd "$(dirname "$0")"; export P="${PDIR:?}"; export VARS="${VARS:-2 8 14}"
one() { c=$1; V=($VARS); k=${#V[@]}; F="$P/m3_tk_T13_T20_K2_NOIM0.cnf"; pf="$P/q2_c$c.proof"
  [ -f "$P/q2_c$c.chk" ] && grep -q "^s VERIFIED" "$P/q2_c$c.chk" && return 0
  mkdir "$P/q2_c$c.lock" 2>/dev/null || return 0
  cube=""; for ((i=0;i<k;i++)); do v=${V[$i]}; if (( (c>>i)&1 )); then cube="$cube$v,"; else cube="$cube-$v,"; fi; done; cube=${cube%,}
  while pgrep -f "dimproof.py $F $pf " >/dev/null; do sleep 60; done
  if ! grep -q "UNSAT" "$P/q2_c$c.gen" 2>/dev/null || [ ! -f "$pf" ]; then python3 dimproof.py "$F" "$pf" "$cube" > "$P/q2_c$c.gen" 2>&1; fi
  t0=$(date +%s); { ./drup "$pf.cnf" "$pf"; echo "drup wall $(( $(date +%s) - t0 )) s"; } > "$P/q2_c$c.chk" 2>&1
  grep -q "^s VERIFIED" "$P/q2_c$c.chk" && rm -f "$pf" "$pf.cnf"
  rmdir "$P/q2_c$c.lock"
  echo "cube $c ($cube): $(grep -o 'glucose4 [A-Z]* [0-9.]* s\|bytes [0-9]*' "$P/q2_c$c.gen" | tr '\n' ' ') $(grep -h '^s ' "$P/q2_c$c.chk")"; }
export -f one
for c in "${@:-1 2 3 4 5 6 7 0}"; do echo $c; done | xargs -P "${PAR:-3}" -I{} bash -c 'one {}'
