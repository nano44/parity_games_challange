#!/usr/bin/env python3
"""L-NEW box 49 (successor 30), DATA for docs/new/N5-READER-box49.md §7: does a reader inflate |C_f(P)| (RESULTS R71's configurations at
fallback sources)? For every pair {y, z} of the longest phase's largest class, an Odd reader o -> {y, z} (start y) is appended (dress.py);
if the run is SAME, |C_f| of the dressed run (o is in Q: out-degree 2) is computed. Prints the base |C_f|, f, and the best pairs.
Usage: cfreader.py BASE.pg BASE.start OUT_PREFIX"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import dress
from dress import load, rows, phases, readstart

def cf(g, R):
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]; P = max(phases(R), key=lambda p: p[1] - p[0])
    src = [t for t in range(P[0], P[1]) if R[t]["fb"]]
    return len({tuple(R[t]["sb"][q] for q in Q) for t in src}), len(src)

base, bst, out = sys.argv[1:4]
g = load(base); E, R = rows(g, readstart(bst)); P = max(phases(R), key=lambda p: p[1] - p[0]); A = R[P[0]]
k0, f0 = cf(g, R); print(f"base |C_f| {k0} f {f0} phase {P}")
cls = {}
for v in range(g.n): cls.setdefault(A["vs"][v][0], []).append(v)
U = max(cls.values(), key=len); res = []; diff = 0
for a in range(len(U)):
    for b in range(a + 1, len(U)):
        y, z = U[a], U[b]
        dress.build(base, bst, out, [f"1:0:{y},{z}:{y}"])
        r = dress.compare(base, bst, out + ".pg", out + ".start", quiet=True)
        if not r["same"]: diff += 1; continue
        g1 = load(out + ".pg"); _, R1 = rows(g1, readstart(out + ".start")); res.append((cf(g1, R1)[0], y, z))
res.sort(reverse=True)
print(f"pairs SAME {len(res)} DIFFERENT {diff}; best (|C_f|, y, z): {res[:8]}")
