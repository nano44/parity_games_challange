#!/bin/bash
# L-COMP box 27: query 2 cube C (BASE = its 3 literals; C 0 = -2,-8,-14, C 4 = -2,-8,14) split further on vars 20, 26 (frame.py
# x(3, X), x(4, X)): 4 sub-cubes whose union is cube C (all sign patterns). Usage: PDIR=dir C=0 BASE=-2,-8,-14 PAR=2 ./subcubes0.sh Same commands as lsicubes_par.sh (dimproof.py streaming, then drup.c). Resumable. PAR=2.
cd "$(dirname "$0")"; export P="${PDIR:?}"; F="$P/m3_tk_T13_T20_K2_NOIM0.cnf"; export F; export C="${C:-0}" BASE="${BASE:--2,-8,-14}"
sub() { s=$1; a=$(( s & 1 ? 20 : -20 )); b=$(( s & 2 ? 26 : -26 )); cube="$BASE,$a,$b"; pf="$P/q2_c${C}s$s.proof"
  [ -f "$P/q2_c${C}s$s.chk" ] && grep -q "^s VERIFIED" "$P/q2_c${C}s$s.chk" && return 0
  if ! grep -q UNSAT "$P/q2_c${C}s$s.gen" 2>/dev/null || [ ! -f "$pf" ]; then python3 dimproof.py "$F" "$pf" "$cube" > "$P/q2_c${C}s$s.gen" 2>&1; fi
  t0=$(date +%s); { ./drup "$pf.cnf" "$pf"; echo "drup wall $(( $(date +%s) - t0 )) s"; } > "$P/q2_c${C}s$s.chk" 2>&1
  grep -q "^s VERIFIED" "$P/q2_c${C}s$s.chk" && rm -f "$pf" "$pf.cnf"
  echo "cube $C sub $s ($cube): $(grep -o 'glucose4 [A-Z]* [0-9.]* s\|bytes [0-9]*' "$P/q2_c${C}s$s.gen" | tr '\n' ' ') $(grep -h '^s ' "$P/q2_c${C}s$s.chk")"; }
export -f sub
seq 0 3 | xargs -P "${PAR:-2}" -I{} bash -c 'sub {}'
