#!/usr/bin/env python3
"""L-NEW box 60: SBC_G, the greedy one-player decomposition of N5-SF's distinct-sigma sequence. Segment [a, b]: sbar* := sbar(sigma^(a))
(S1's reply at the segment start) and the segment extends while F(sigma^(j)) == N5's step (n5x.step) on G* = G cut to sbar* from
(sigma^(j), sbar*), restricted to Even. SBC_G := #segments - 1. A boundary at j: F(sigma^(j)) differs from the frozen-reply step.
Also: per Odd u, Gflips(u) := #boundaries j at which sbar changes at u (sbar(sigma^(j+1)) vs the segment's sbar*), and the longest
segment SEGMAX. Prints one SBCG line. Usage: sbcg.py GAME.pg"""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54"))
import n5sf, n5x, pg
from n5x import load, Engine, dual
g = load(sys.argv[1]); n = g.n; m = sum(len(set(s)) for s in g.succ)
E, T = n5sf.trace(g)
seq = [T[0]]
for x in T[1:]:
    if x.get("cycle"): break
    if x["s"] != seq[-1]["s"]: seq.append(x)
def mk(a):
    sstar = [seq[a]["sb"][u] if g.owner[u] == 1 else -1 for u in range(n)]
    succ = [[sstar[u]] if g.owner[u] == 1 else list(g.succ[u]) for u in range(n)]
    gs = pg.Game(list(g.prio), list(g.owner), succ); return gs, Engine(gs), Engine(dual(gs)), sstar
a = 0; cur = mk(0); bounds = []; gfl = collections.Counter(); seg = 0
for j in range(len(seq) - 1):
    gs, Es, Eds, sstar = cur
    r = n5x.step(gs, Es, Eds, list(seq[j]["s"]), sstar)
    ok = r is not None and all(r[0][v] == seq[j + 1]["s"][v] for v in range(n) if g.owner[v] == 0)
    if not ok:
        bounds.append(j); seg = max(seg, j - a)
        for u in range(n):
            if g.owner[u] == 1 and seq[j]["sb"][u] != sstar[u]: gfl[u] += 1
        a = j; cur = mk(a)
        gs, Es, Eds, sstar = cur
        r = n5x.step(gs, Es, Eds, list(seq[j]["s"]), sstar)
        assert r is not None and all(r[0][v] == seq[j + 1]["s"][v] for v in range(n) if g.owner[v] == 0), ("ONE-PLAYER fails at", j)
seg = max(seg, len(seq) - 1 - a)
sbc = sum(1 for j in range(len(seq) - 1) if seq[j]["sb"] != seq[j + 1]["sb"])
bound = (n + m + 1) * (n * n - n + 1)
print(f"SBCG {os.path.basename(sys.argv[1])} n {n} m {m} orbit {len(seq)} SBC {sbc} SBC_G {len(bounds)} SEGMAX {seg} "
      f"maxGflips {max(gfl.values(), default=0)} {'PASS' if seg < bound else 'SEG_V'}", flush=True)
