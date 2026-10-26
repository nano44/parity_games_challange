#!/usr/bin/env python3
"""Box 48 DATA: shape of the fallback-free returns (no in-phase fallback source in [s_i, s_{i+1})): U := the vertices of Q whose sigma-bar changes
somewhere in [s_i, s_{i+1}]; histogram of |U|, of |Q|, of the max |D| over the stretch, and of |D_C| (DC) of the returning configuration. Usage: r0shape.py STARTS SEED --list FILE [--nmax N]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
from multi import load, step, start_pair, Engine, dual
H = {}
def inc(k): H[k] = H.get(k, 0) + 1
def run(g, start, nm, cap=5000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append((tuple(x[0] for x in vs), tuple(t), tuple(sb[q] for q in Q), r[4] if r else 0, sum(1 for q in Q if sb[q] != t[q])))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1][:2] == rows[i][:2]: j += 1
        st = {}; nc2 = set()
        for k in range(i, j + 1):
            if k == i or rows[k][2] != rows[k - 1][2]: st.setdefault(rows[k][2], []).append(k)
            if rows[k][4] >= 2: nc2.add(rows[k][2])
        inc(("NCONF2_phase", len(nc2)))
        for cf, ss in st.items():
            for a, b in zip(ss, ss[1:]):
                if any(rows[k][3] for k in range(a, b)): continue
                U = {qi for k in range(a, b) for qi in range(len(Q)) if rows[k][2][qi] != rows[k + 1][2][qi]}
                inc(("U", len(U))); inc(("Q", len(Q))); inc(("DC", rows[a][4])); inc(("Dmax", max(rows[k][4] for k in range(a, b + 1))))
        i = j + 1
a = sys.argv[1:]; nmax = 34
if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
K = int(a[0]); RNG = random.Random(int(a[1])); R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[3]) if l.strip() and not l.startswith("#")]
for nm, g in gs:
    if g.n > nmax: continue
    for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
        try: run(g, st, nm)
        except RecursionError: pass
for k in sorted(H): print(k, H[k])
