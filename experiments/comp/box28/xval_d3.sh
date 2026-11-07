#!/bin/bash
# L-COMP box 28: cross-validation of frup against box27/drup.c on the 16 P-TR3 d 3 L 9 cube proofs. Per cube: DIMACS by mkdimacs.py
# (sha1 must equal P-TR3 §4), Glucose 4 proof streamed by box27/dimproof.py (sha1 must equal P-TR3 §4), then frup and drup on the same
# files (wall times), proof deleted after both. Resumable: log/xval_d3/c<c>.done. Usage: PDIR=dir ./xval_d3.sh [cubes]
cd "$(dirname "$0")"; P="${PDIR:?}"; mkdir -p "$P" log/xval_d3
for c in ${@:-9 10 5 2 13 6 14 1 15 3 0 7 8 11 12 4}; do
  O=log/xval_d3/c$c; [ -f $O.done ] && continue
  python3 mkdimacs.py 3 9 $c "$P" > $O.cnf.txt 2>&1; F="$P/d3_L9_c$c.cnf"; pf="$P/d3_L9_c$c.proof"
  python3 ../box27/dimproof.py "$F" "$pf" > $O.gen 2>&1
  t0=$(date +%s.%N); ./frup "$F" "$pf" > $O.frup 2>&1; echo "frup exit $? wall $(echo "$(date +%s.%N) - $t0" | bc) s" >> $O.frup
  t0=$(date +%s.%N); ../box27/drup "$F" "$pf" > $O.drup 2>&1; echo "drup exit $? wall $(echo "$(date +%s.%N) - $t0" | bc) s" >> $O.drup
  rm -f "$pf"; date -u +%FT%TZ > $O.done
  echo "cube $c: $(grep -o 'sha1 [0-9a-f]*' $O.cnf.txt) | $(grep -o 'UNSAT [0-9.]* s\|sha1 [0-9a-f]*$\|bytes [0-9]*' $O.gen | tr '\n' ' ') | frup: $(grep -h '^s \|wall' $O.frup | tr '\n' ' ') | drup: $(grep -h '^s \|wall' $O.drup | tr '\n' ' ')" >> log/xval_d3.txt
done
