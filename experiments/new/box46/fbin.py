#!/usr/bin/env python3
"""Box 46 DATA: list the gaps between consecutive W-honest states of a phase that contain an in-phase fallback at a NON-honest state
(f_in of Corollary HON', docs/new/N5-REC1-box46.md §1a), with LEV (levels.level, G_tau frame) at both ends when n <= NMAX.
Usage: fbin.py STARTS SEED --list FILE [--nmax N]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import levels as L, hon
from levels import load, step, start_pair, Engine, dual, Unknown
def run(g, start, nm, nmax):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 4000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t); w = hon.wvals(g, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), hon=(tuple(vs) == tuple(w)), xi=vs, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        a, b = i, j; i = j + 1; H = [k for k in range(a, b + 1) if rows[k]["hon"]]; tau = rows[a]["t"]
        for h0, h1 in zip(H, H[1:]):
            fk = [k for k in range(h0 + 1, h1) if rows[k]["fb"]]
            if not fk: continue
            lv = "n/a"
            if g.n <= nmax:
                frame = [[tau[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
                try: lv = (L.level(E, g, frame, rows[h0]["xi"], (), 10 ** 7), L.level(E, g, frame, rows[h1]["xi"], (), 10 ** 7))
                except Unknown: lv = "unknown"
            print(f"{nm} n {g.n} start {'S3' if start is None else 'random'} phase [{a},{b}] gap {h0}->{h1} fallbacks at {fk} LEV {lv}")
if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 40
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
    for l in open(a[3]):
        if not l.strip() or l.startswith("#"): continue
        nm = l.split()[0]; g = load(os.path.join(R0, nm))
        if g.n > 64: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: run(g, st, nm, nmax)
            except RecursionError: pass
