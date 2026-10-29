#!/usr/bin/env python3
"""L-NEW box 53 (successor 32): integer features of an N5 state for ranking-function synthesis (Lead 13:47Z, BOX 53). All features are
integers of polynomial range (no 2^rank weights). For a valuation (c, P, l) of S1 (P a mask of ranks) and a vertex v:
  cr  = rew(c) = +-p'(c)                        (cycle-node reward; Even-better is larger)
  ps  = sum_{r in P} s(r)(r + 1)                 (signed rank-sum; s(r) = +1 if rank r has even priority, -1 if odd)
  pc  = sum_{r in P} s(r)                        (signed count)
  tp  = s(r*)(r* + 1), r* = max P (0 if P empty) (signed top)
  pp  = sum_{r in P, s(r) = +1} (r + 1);  pn = sum_{r in P, s(r) = -1} (r + 1)
  ln  = l if c odd else -l                       (S1's length component, oriented so that larger is better for Even)
Frames: X (Xi = val(sigma, sigma-bar), G), W (val(sigma, tau), G), T (Xi_tau = tau's valuation on G^d; larger = better for ODD).
UNIFORM features: for each frame and component, the sum over all vertices (21), plus |Is|, |It|, |D| (3). PER-VERTEX features: each
(frame, component, v) separately (21 n). PER-RANK features: per frame N_r (vertices whose path set holds rank r), r < n, sum cr, sum ln; plus |Is|, |It|, |D|.
EDGE BITS (index 6), and index 7 = uniform + moments + edge bits: [sigma(v) = w] / [tau(v) = w] for every edge (v, w) at a vertex with >= 2 successors (T42 section 3's state encoding).
Usage: imported (states(g, start) -> list of (uniform, per-vertex, fb, per-rank, moments, uniform+moments, edge bits))."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, load, readstart, Dset
from n5x import Engine, dual
COMP = ("cr", "ps", "pc", "tp", "pp", "pn", "ln")
NAMES = [f + "_" + c for f in "XWT" for c in COMP] + ["nIs", "nIt", "nD"]
MNAMES = [f + "_" + c for f in "XWT" for c in ("m0", "m1", "m2", "m3", "m4", "cr", "ln")] + ["nIs", "nIt", "nD"]

def comp(E, val):
    c, mask, l = val; ps = pc = pp = pn = 0; top = -1; r = 0; m = mask
    while m:
        if m & 1:
            s = 1 if E.rankpar[r] == 0 else -1; ps += s * (r + 1); pc += s; top = r
            if s > 0: pp += r + 1
            else: pn += r + 1
        m >>= 1; r += 1
    tp = 0 if top < 0 else (1 if E.rankpar[top] == 0 else -1) * (top + 1)
    return (E.rew[c], ps, pc, tp, pp, pn, l if E.par[c] == 1 else -l)

def states(g, start=None, cap=20000):
    E, R = rows(g, start, cap=cap); Ed = Engine(dual(g)); out = []
    for A in R:
        vt, _ = Ed.evaluate(tuple(A["t"]))
        It = Ed.improving(tuple(A["t"]), vt); Is = E.improving(tuple(A["s"]), A["vs"])
        per = []
        for frame, E_, V in (("X", E, A["vs"]), ("W", E, A["W"]), ("T", Ed, vt)):
            cs = [comp(E_, V[v]) for v in range(g.n)]
            per.append(cs)
        uni = [sum(cs[v][k] for v in range(g.n)) for cs in per for k in range(7)] + [len(Is), len(It), len(Dset(g, A))]
        pv = [cs[v][k] for cs in per for k in range(7) for v in range(g.n)]
        rk = []                              # PER-RANK features: per frame, N_r = #{v : rank r in P(v)} for every r, plus sum cr and sum ln
        for (frame, E_, V), cs in zip((("X", E, A["vs"]), ("W", E, A["W"]), ("T", Ed, vt)), per):
            N = [0] * g.n
            for v in range(g.n):
                m = V[v][1]; r = 0
                while m:
                    if m & 1: N[r] += 1
                    m >>= 1; r += 1
            rk += N + [sum(c[0] for c in cs), sum(c[6] for c in cs)]
        mom = []                             # MOMENT features: per frame sum_r (r+1)^j N_r, j = 0..4, plus sum cr, sum ln; plus the 3 counts
        for f in range(3):
            N = rk[f * (g.n + 2): f * (g.n + 2) + g.n]
            mom += [sum((r + 1) ** j * N[r] for r in range(g.n)) for j in range(5)] + rk[f * (g.n + 2) + g.n: (f + 1) * (g.n + 2)]
        eb = [int((A["s"] if g.owner[v] == 0 else A["t"])[v] == w) for v in range(g.n) if len(set(g.succ[v])) >= 2 for w in sorted(set(g.succ[v]))]
        out.append((uni, pv, A["fb"], rk + uni[-3:], mom + uni[-3:], uni + mom, eb, uni + mom + eb))
    return out
