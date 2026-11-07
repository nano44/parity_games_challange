#!/bin/bash
# L-COMP box 28: regression (a) of cnf2.py: T^R(3) = 8 re-derived with cnf2 (SYM=1): T >= 8 SAT (model decoded -> log/d3cnf2/L8.json,
# replayed by sim.py), T >= 9 UNSAT on all 16 P-TR3 cubes (CUBE = start bits of movers 2..5, cube c bit i -> mover 2+i); CaDiCaL 1.9.5.
# Resumable (a cube with a RESULT line is skipped). Times comparable with P-TR3 §3 (cnf.py) only when the machine is not oversubscribed.
cd "$(dirname "$0")"; mkdir -p log/d3cnf2
[ -f log/d3cnf2/L8.log ] && grep -q RESULT log/d3cnf2/L8.log || SYM=1 python3 cnf2.py 3 8 log/d3cnf2/L8.json > log/d3cnf2/L8.log 2>&1
for c in $(seq 0 15); do f=log/d3cnf2/L9_c$c.log; grep -q RESULT $f 2>/dev/null && continue
  CUBE=$(python3 -c "print(','.join(f'{x}:{($c>>i)&1}' for i,x in enumerate(range(2,6))))")
  SYM=1 CUBE=$CUBE python3 cnf2.py 3 9 log/d3cnf2/L9_c$c.json > $f 2>&1; done
echo "d3cnf2 done $(date -u +%FT%TZ)" >> log/d3cnf2/done
