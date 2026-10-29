#!/usr/bin/env python3
"""L-SI box 28 (docs/si/N5-CHG-box28.md §10): anatomy of P-changes and CARRIES (T33 §1.2) of one vertex inside one phase.
Prints, for the vertex with the most carries in the longest phase (or VERT=x), every P-change t -> t+1: outgoing and incoming vertices
(with E/O parity of their priority), MATCHED or CARRY, and which Even vertices switched at t. Usage: carries.py GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart, phases
from compose import matched, bits
g = load(sys.argv[1]); E, R = rows(g, readstart(sys.argv[2]) if len(sys.argv) > 2 else None, cap=20000); n = g.n
rk2v = {E.rank[v]: v for v in range(n)}; odd = lambda r: E.par[rk2v[r]] == 1
i, j = max(phases(R), key=lambda p: p[1] - p[0])
def changes(x):
    out = []
    for t in range(i, j):
        a, b = R[t]["vs"][x], R[t + 1]["vs"][x]
        if a[1] != b[1]:
            rc = E.rank[a[0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
            A, B = bits(a[1]), bits(b[1]); out.append((t, A, B, matched(A, B, w, odd)))
    return out
if os.environ.get("VERT"): x = int(os.environ["VERT"])
else: x = max(range(n), key=lambda x: (sum(1 for c in changes(x) if not c[3]), -x))
ch = changes(x); print(f"phase [{i},{j}] vertex {x} (owner {g.owner[x]}, cycle node {R[i]['vs'][x][0]}): {len(ch)} P-changes, {sum(1 for c in ch if not c[3])} carries")
lab = lambda r: f"{rk2v[r]}{'o' if odd(r) else 'e'}"
for t, A, B, m in ch:
    sw = [v for v in range(n) if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]]
    rc = E.rank[R[i]["vs"][x][0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc); dphi = sum(map(w, B)) - sum(map(w, A))
    print(f" t={t} {'MATCH' if m else 'CARRY'} dPhi={dphi:+d} out={[lab(r) for r in sorted(A - B, reverse=True)]} in={[lab(r) for r in sorted(B - A, reverse=True)]} top={lab(max(B)) if B else None} switches={sw}")
