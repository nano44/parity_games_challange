#!/usr/bin/env python3
"""L-LOWER 6: general-form test of RC-PLATEAU on records: for each capped level j >= 2 of a genome, the second mover q_(j-1) of pair
j - 1 (role, from the run) and the number of Ξ-paths from it into pair j. A capped level j with npaths > 0 refutes «a Ξ-path from
q_(j-1) into pair j forces F(j) < 2^(j+2) - 2». Usage: rcgen.py genome.txt ..."""
import sys
from sim6 import rd, run, Fprof, caps
from guard_l6 import roles, npaths
for p in sys.argv[1:]:
    D = rd(p); S, O = run(D); F = Fprof(D, O); h = caps(F); out = []
    for j in range(2, min(h + 1, D['d'])):
        r = roles(D, S, O, j - 1)
        if not r: out.append(f"j{j}:no-roles"); continue
        out.append(f"j{j}{'(capped)' if j < h else ''}:q{j-1}={r[1]} npaths={npaths(D, r[1], {2*j, 2*j+1})}")
    print(p.split('/')[-1], 'caps', h, ' '.join(out))
