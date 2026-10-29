#!/usr/bin/env python3
"""L-SI box 28 (from lay/relcheck.py, box 27): independent check of an INTER-JOINT failure (docs/si/N5-CHG-box28.md), from L-COMP's n5b (SPEC mode) ALONE (no n5x, no lwp/seglast.py code):
states from n5b's trace hook, sigma-bar = n5b's Odd counterstrategy to sigma_t, W-successor = (sigma_t, tau_t). For the given [a, b] it
checks: one phase and no fallback inside (tau constant, fbtrace 0), REL-admissibility (sigma-bar constant on RO_b, every cycle of CW_b /
CH_b a W-cycle / honest cycle at every state), maximality (REL fails at a - 1 inside the run, or a is the run start), the given transition t
is no Even vertex's last switch in [a, b], and observed GEN_W on [a, b] (two different W-plays from one vertex to the same cycle never get
the same (cycle node, P, length) valuation, P computed here from S1's rank order (Omega(v), v)).
Here: the H-sink h at t makes an intermediate switch at t and switches to its final successor before its W-chain settles.
Usage: ijcheck.py GAME.pg START a b t h"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second"))
import n5b
gp, sp, a, b, t0, h = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
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
VS = [N.ev(N.SG, [S[k][v] if g.owner[v] == n5b.EVEN else -1 for v in range(n)]) for k in range(len(tr))]
KEY = [(tuple(VS[k][v][0] for v in range(n)), tuple(T[k])) for k in range(len(tr))]   # RESULTS R38 (a) KEY: (lambda_Xi, tau)
r0 = t0
while r0 > 0 and KEY[r0 - 1] == KEY[t0] and fbt[r0 - 1] == 0: r0 -= 1
r1 = t0
while r1 + 1 < len(tr) and KEY[r1 + 1] == KEY[t0] and fbt[r1] == 0: r1 += 1
segs, e = [], r1                                  # cut the run [r0, r1] from its end into maximal REL segments (GRUN §4)
while e >= r0:
    Xe, ROe, CWe, CHe = ends(e); s0 = e
    while s0 > r0 and rel(s0 - 1, e, Xe, ROe, CWe, CHe): s0 -= 1
    segs.append((s0, e)); e = s0 - 1
print("run containing t (n5b: (lambda_Xi, tau) constant, no fallback):", (r0, r1), "| its REL segments:", segs[::-1], "| [a, b] is one of them:", (a, b) in segs)
print("|X_b|", len(X), "|RO_b|", len(RO), "|CW_b|", len(CW), "|CH_b|", len(CH))
print("REL-admissible on [a, b]:", all(rel(k, b, X, RO, CW, CH) for k in range(a, b + 1)), "| REL at a - 1:", a > 0 and rel(a - 1, b, X, RO, CW, CH))
T_ = {x for C in CW | CH for x, _ in C}
def settled(nx_rows, v, k): return all(play(nx_rows[j], v) == play(nx_rows[b], v) for j in range(k, b + 1))
def first(nx_rows, v):
    k = b
    while k > a and settled(nx_rows, v, k - 1): k -= 1
    return k
def jn(nx, v):
    p, c = play(nx, v)
    for x in (p + c)[1:]:
        if g.owner[x] == n5b.EVEN and x not in T_: return x
    return None
jW, jH = jn(WN[b], h), jn(HN[b], h)
print("h", h, "in X_b:", h in X, "| in T:", h in T_, "| sigma_k(h) for k in [a, b]:", [S[k][h] for k in range(a, b + 1)], "| y_h =", S[b][h])
print("jW(h) =", jW, "first W-settled state of jW(h):", first(WN, jW) if jW is not None else a, "| jH(h) =", jH, "first H-settled state of jH(h):", first(HN, jH) if jH is not None else a)
print("h H-unsettled at t:", not settled(HN, h, t0), "| jH(h) H-settled at t (h an H-sink):", jH is None or settled(HN, jH, t0), "| jW(h) W-unsettled at t (h not a W-sink):", jW is not None and not settled(WN, jW, t0))
print("intermediate switch at t:", S[t0][h] != S[t0 + 1][h] != S[b][h], "| L(h) =", max(k for k in range(a, b) if S[k][h] != S[k + 1][h]), "| s_h = fW(jW h) - 1 =", (first(WN, jW) if jW is not None else a) - 1)
rk = lambda v: (g.prio[v], v)
def val(path, cy):
    c = max(cy, key=rk); return (c, frozenset(x for x in path if rk(x) > rk(c)), len(path))
seen, bad = {}, 0
for k in range(a, b + 1):
    for v in range(n):
        p, cy = play(WN[k], v); key = (v, frozenset(cy), val(p, cy))
        if seen.setdefault(key, tuple(p)) != tuple(p): bad += 1
print("observed GEN_W failures on [a, b] (S1 rank order):", bad)
