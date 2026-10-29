#!/usr/bin/env python3
"""L-NEW box 61: (a) iteration count I of N5-SF (two-sided, SPEC S3 start) with I/n^3 and I/(n^2 (n+m)); (b) Lemma-candidate COARSE:
every greedy one-player segment [a, b] of sbcg.py that ends at a boundary contains a transition j in [a, b) at which some vertex's COARSE
key changes. Coarse key of v at state j: (cycle node of Xi_j(v), most relevant vertex of its path set). Counts: C = #transitions with a
coarse change anywhere; segments without one (VIOL). Usage: coarse.py GAME.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54"))
import n5sf, n5x, pg
from n5x import load, Engine, dual
g = load(sys.argv[1]); n = g.n; m = sum(len(set(s)) for s in g.succ)
E, T = n5sf.trace(g); I = len(T) - 1 - (1 if T[-1].get("cycle") else 0)
seq = [T[0]]
for x in T[1:]:
    if x.get("cycle"): break
    if x["s"] != seq[-1]["s"]: seq.append(x)
def key(val):
    x = val[1]; return (val[0], max((v for v in range(n) if E.bit[v] & x), key=lambda v: E.rank[v]) if x else -1)
vals = [E.evaluate(tuple(st["s"]))[0] for st in seq]
keys = [[key(vv) for vv in vl] for vl in vals]
ch = [keys[j] != keys[j + 1] for j in range(len(seq) - 1)]
INF = 10 ** 9
def vdepth(x, y):
    """0 if the cycle node changes; else 1 + #common path vertices more relevant than d = max(P xor P'); INF if equal."""
    if x[0] != y[0]: return 0
    dd = x[1] ^ y[1]
    if not dd and x[2] == y[2]: return INF
    if not dd: return n + 1
    d = max((v for v in range(n) if E.bit[v] & dd), key=lambda v: E.rank[v])
    return 1 + sum(1 for v in range(n) if E.bit[v] & x[1] & y[1] and E.rank[v] > E.rank[d])
dep = [min(vdepth(vals[j][v], vals[j + 1][v]) for v in range(n)) for j in range(len(seq) - 1)]
def mk(a):
    sstar = [seq[a]["sb"][u] if g.owner[u] == 1 else -1 for u in range(n)]
    succ = [[sstar[u]] if g.owner[u] == 1 else list(g.succ[u]) for u in range(n)]
    gs = pg.Game(list(g.prio), list(g.owner), succ); return gs, Engine(gs), Engine(dual(gs)), sstar
a = 0; cur = mk(0); nb = 0; viol = 0; first = None; DEPTH = 0
for j in range(len(seq) - 1):
    gs, Es, Eds, sstar = cur
    r = n5x.step(gs, Es, Eds, list(seq[j]["s"]), sstar)
    if not (r is not None and all(r[0][v] == seq[j + 1]["s"][v] for v in range(n) if g.owner[v] == 0)):
        nb += 1; DEPTH = max(DEPTH, min(dep[a:j + 1]))
        if not any(ch[a:j]):
            viol += 1; first = first if first is not None else (a, j)
        a = j; cur = mk(a)
print(f"COARSE {os.path.basename(sys.argv[1])} n {n} m {m} I {I} I/n3 {I / n**3:.5f} I/n2nm {I / (n * n * (n + m)):.6f} SBC_G {nb} "
      f"DEPTH {DEPTH} C {sum(ch)} viol {viol} first {first} {'PASS' if viol == 0 else 'FAIL'}", flush=True)
