#!/usr/bin/env python3
"""L-NEW box 50: independent recomputation of Xi at one transition t -> t+1: walk the (sigma_t, sigma-bar_t)-play from every vertex (no use of
Engine.evaluate's valuations; sigma-bar taken from the run) and read (cycle node, path set of ranks > the cycle node's, length) by S1;
prints, for every vertex whose value changes, the classification (LEN / P-change) and whether it equals fbcarry.py's. Usage: fbwalk.py GAME START t"""
import sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root")); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import rows, load, readstart
from fbcarry import kind
g = load(sys.argv[1]); E, R = rows(g, readstart(sys.argv[2])); t = int(sys.argv[3]); n = g.n
def walk(k):
    nx = [R[k]["s"][v] if g.owner[v] == 0 else R[k]["sb"][v] for v in range(n)]; out = []
    for v in range(n):
        seq, seen, x = [], {}, v
        while x not in seen: seen[x] = len(seq); seq.append(x); x = nx[x]
        cyc = seq[seen[x]:]; c = max(cyc, key=lambda u: E.rank[u]); pre = seq[:seq.index(c)]
        out.append((c, frozenset(E.rank[u] for u in pre if E.rank[u] > E.rank[c]), len(pre)))
    return out
A, B = walk(t), walk(t + 1); ok = True
for v in range(n):
    a, b = A[v], B[v]; mine = "NONE" if a == b else ("LEN" if (a[0] == b[0] and a[1] == b[1]) else "P")
    k = kind(E, R[t]["vs"][v], R[t + 1]["vs"][v]); kk = "P" if k in ("MAT", "CAR") else k
    ok &= (mine == kk)
    if mine != "NONE": print(v, mine, k)
print("fb flag", R[t]["fb"], "switched", [v for v in range(n) if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]], "AGREE" if ok else "DISAGREE")
