#!/usr/bin/env python3
"""L-RED successor 31 (R123): second span counter, independent of L-SI's win.py. Engine: L-COMP's n5b SPEC (Even side, Xi_sigma on G).
MATCHED test: mix/matc.py's (written from RESULTS R85). For each lambda-run R, each Even v and each target c of v that v leaves and
later re-enters inside R: span = transitions t -> t+1 with t_leave <= t <= t_reenter (t_leave: sigma_t(v) = c != sigma_(t+1)(v);
t_reenter: sigma_t(v) != c = sigma_(t+1)(v); first leave, last re-entry). Counts P-changes (PCH) and MATCHED ones (MAT) of Xi(c) there
(same cycle node, P differs), and SEG = the longest run of carries between MATCHED changes inside the span. Prints the top pairs by MAT and PCH, with n.  Usage: spanc.py GAME.pg START"""
import sys, os
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for p in ("experiments/n5-second", "experiments/hard-families", "experiments/harness", "experiments/red/mix"): sys.path.insert(0, os.path.join(R, p))
import n5b, pg
from matc import matched
g = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g)
N = n5b.N5(g, mode="spec"); tr = []; N.run(s0, t0, trace=tr); si = N.SG
rank = {v: r for r, v in enumerate(sorted(range(g.n), key=lambda v: (si.g.prio[v], v)))}
odd = lambda v: si.g.prio[v] % 2 == 1
U = [si.evaluate(list(st[0])) for st in tr]; T = len(U) - 1
lam = [tuple(u[v][0] for v in range(g.n)) for u in U]
runs = [0] + [k + 1 for k in range(T) if lam[k + 1] != lam[k]] + [T + 1]
def kind(x, t):
    (c, A, _), (c2, B, _) = U[t][x], U[t + 1][x]
    if c != c2 or A == B: return None
    rc = rank[c]; w = lambda v: (rank[v] - rc) if not odd(v) else -(rank[v] - rc)
    return "MAT" if matched(set(A), set(B), w, odd) else "CAR"
rows = []
for a, b in zip(runs, runs[1:]):
    for v in range(g.n):
        if g.owner[v] != 0: continue
        lv = {}; re_ = {}
        for t in range(a, b - 1):
            x, y = tr[t][0][v], tr[t + 1][0][v]
            if x != y: lv.setdefault(x, t); re_[y] = t
        for c, tl in lv.items():
            if c in re_ and re_[c] > tl:
                ks = [kind(c, t) for t in range(tl, re_[c] + 1)]; seg = cur = 0
                for k in ks:
                    if k == "MAT": cur = 0
                    if k == "CAR": cur += 1; seg = max(seg, cur)
                rows.append((ks.count("MAT"), ks.count("MAT") + ks.count("CAR"), v, c, tl, re_[c], seg))
print(f"SPANC {os.path.basename(sys.argv[1])} n {g.n} T {T} lambda-runs {len(runs) - 1} pairs {len(rows)}")
for r in sorted(rows, reverse=True)[:4]: print(f"  pair ({r[2]}, {r[3]}) span [{r[4]}, {r[5]}]: MAT {r[0]} PCH {r[1]}")
sg = max(rows, key=lambda r: r[6], default=None)
if sg: print(f"  max SEG^span {sg[6]} at pair ({sg[2]}, {sg[3]}) span [{sg[4]}, {sg[5]}] (MAT {sg[0]} PCH {sg[1]}); CARRY-SEG-S {'FAIL' if sg[6] > g.n - 1 else 'PASS'}")
mx = max(rows, default=(0, 0)); print(f"  max MAT^span {mx[0]} (/n {mx[0] / g.n:.3f}), max PCH^span {max((r[1] for r in rows), default=0)}; RESET-LIN-S {'FAIL' if mx[0] > g.n else 'PASS'}")
