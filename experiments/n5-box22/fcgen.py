#!/usr/bin/env python3
"""L-COMP box 22: fcN = PGSolver switchbestexp N (hard-families/pgsolver_port.py, byte-identical to the d3cd624 binary) minus the N edges
CycleNode1(i) -> CycleAccessDistributer (descriptions "f<i>" -> "c"), nothing else (L-RED R115's definition; L-RED's sbev.py NOT used).
Output in pgsolver_port's format (PGSolver output_game). Usage: fcgen.py N > fcN.pg"""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hard-families"))
import pgsolver_port as P
N = int(sys.argv[1]); lines = P.switchbestexp(N).splitlines(); rows = {}
pat = re.compile(r'^(\d+) (\d+) ([01]) ([\d,]+) "([^"]*)";$')
for l in lines[1:]:
    m = pat.match(l); rows[int(m.group(1))] = [int(m.group(2)), int(m.group(3)), [int(x) for x in m.group(4).split(",")], m.group(5)]
c = [v for v, r in rows.items() if r[3] == "c"]; assert len(c) == 1; c = c[0]; dropped = 0
for i in range(N):
    f = [v for v, r in rows.items() if r[3] == f"f{i}"]; assert len(f) == 1
    assert c in rows[f[0]][2] and len(rows[f[0]][2]) > 1; rows[f[0]][2].remove(c); dropped += 1
assert dropped == N
sys.stdout.write(lines[0] + "\n" + "".join(f'{v} {r[0]} {r[1]} {",".join(map(str, r[2]))} "{r[3]}";\n' for v, r in sorted(rows.items())))
