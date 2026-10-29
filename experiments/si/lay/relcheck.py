#!/usr/bin/env python3
"""L-SI box 27: independent check of a SEG-LAST failure, from L-COMP's n5b (SPEC mode) ALONE (no n5x, no lwp/seglast.py code):
states from n5b's trace hook, sigma-bar = n5b's Odd counterstrategy to sigma_t, W-successor = (sigma_t, tau_t). For the given [a, b] it
checks: one phase and no fallback inside (tau constant, fbtrace 0), REL-admissibility (sigma-bar constant on RO_b, every cycle of CW_b /
CH_b a W-cycle / honest cycle at every state), maximality (REL fails at a - 1 inside the run, or a is the run start), the given transition t
is no Even vertex's last switch in [a, b], and observed GEN_W on [a, b] (two different W-plays from one vertex to the same cycle never get
the same (cycle node, P, length) valuation, P computed here from S1's rank order (Omega(v), v)).
Usage: relcheck.py GAME.pg START a b t"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second"))
import n5b
gp, sp, a, b, t0 = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:6])
g = n5b.pg.read(gp); N = n5b.N5(g); N.mode = "spec"; n = g.n
sig0, tau0 = n5b.read_start(sp, g); tr, fbt = [], []
N.run(sig0, tau0, trace=tr, fbtrace=fbt)
EV = [v for v in range(n) if g.owner[v] == n5b.EVEN]; OD = [v for v in range(n) if g.owner[v] == n5b.ODD]
S = [list(s) for s, _ in tr]; T = [list(x) for _, x in tr]
SB = [N.opt(N.SG, [S[k][v] if g.owner[v] == n5b.EVEN else -1 for v in range(n)])[1] for k in range(len(tr))]
WN = [[S[k][v] if g.owner[v] == n5b.EVEN else T[k][v] for v in range(n)] for k in range(len(tr))]
HN = [[S[k][v] if g.owner[v] == n5b.EVEN else SB[k][v] for v in range(n)] for k in range(len(tr))]
def play(nx, v):
    path, pos, x = [], {}, v
    while x not in pos: pos[x] = len(path); path.append(x); x = nx[x]
    return path[:pos[x]], path[pos[x]:]
def cyc(nx, v): return frozenset((x, nx[x]) for x in play(nx, v)[1])
def iscyc(nx, C): return all(nx[x] == y for x, y in C)
def rel(k, B, Xb, RO, CW, CH): return all(SB[k][u] == SB[B][u] for u in RO) and all(iscyc(WN[k], C) for C in CW) and all(iscyc(HN[k], C) for C in CH)
def ends(B):
    Q = [v for v in EV if len(set(g.succ[v])) >= 2]; X, st = set(), list(Q)
    while st:
        x = st.pop()
        if x in X: continue
        X.add(x); p1, c1 = play(WN[B], x); p2, c2 = play(HN[B], x); st.extend(y for y in p1 + c1 + p2 + c2 if g.owner[y] == n5b.EVEN)
    RO = {y for v in X for y in sum(play(HN[B], v), []) if g.owner[y] == n5b.ODD}
    return X, RO, {cyc(WN[B], v) for v in X}, {cyc(HN[B], v) for v in X}
print("n", n, "states", len(tr), "fallback flags", fbt)
print("tau constant on [a, b]:", all(T[k] == T[a] for k in range(a, b + 1)), "| no fallback at transitions a..b-1:", all(fbt[k] == 0 for k in range(a, b)))
print("phase/run boundary before a: tau_(a-1) == tau_a:", a > 0 and T[a - 1] == T[a], "| fallback at a-1:", a > 0 and fbt[a - 1] == 1)
X, RO, CW, CH = ends(b)
print("|X_b|", len(X), "|RO_b|", len(RO), "|CW_b|", len(CW), "|CH_b|", len(CH))
print("REL-admissible on [a, b]:", all(rel(k, b, X, RO, CW, CH) for k in range(a, b + 1)), "| REL at a - 1:", a > 0 and rel(a - 1, b, X, RO, CW, CH))
sw = [v for v in EV if S[t0][v] != S[t0 + 1][v]]
later = {v: [k for k in range(t0 + 1, b) if S[k][v] != S[k + 1][v]] for v in sw}
print(f"switchers at t = {t0}:", [(v, S[t0][v], S[t0 + 1][v], "switches again at", later[v]) for v in sw])
print("SEG-LAST fails at t:", bool(sw) and all(later[v] for v in sw))
rk = lambda v: (g.prio[v], v)
def val(path, cy):
    c = max(cy, key=rk); return (c, frozenset(x for x in path if rk(x) > rk(c)), len(path))
seen, bad = {}, 0
for k in range(a, b + 1):
    for v in range(n):
        p, cy = play(WN[k], v); key = (v, frozenset(cy), val(p, cy))
        if seen.setdefault(key, tuple(p)) != tuple(p): bad += 1
print("observed GEN_W failures on [a, b] (S1 rank order):", bad)
