"""L-RED box 17 (produced on Opus 5.5): (G-NEXT-1P) test. For every G-transition at b (search i -> i+1) followed by a transition
(search i+1 -> i+2) at c: record the depth-0 positions where search i (the search whose tangles produce the G) learns tangles. Law: c > b only
if search i learns at >= 2 positions. Class set as neststarscan.py (b12_topchain.classgames, DIST=1); chains from L-ALG's unmodified b12_pot / b12_core.
Usage: DTL_ORDER=.. [TRIALS=3 SEED=2 NMAX=200] gnext1p.py FILES..."""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
sys.setrecursionlimit(100000); os.environ["DIST"] = "1"
import xscore as X, learnpos as LP
from b12_topchain import classgames
B = X.B; order = os.environ.get("DTL_ORDER", "stable"); cnt = collections.Counter(); ex = []
for name, g in classgames(sys.argv[1:], int(os.environ.get("TRIALS", "3")), int(os.environ.get("SEED", "2")), int(os.environ.get("NMAX", "200"))):
    C = X.controller(g)
    if C is None: continue
    saved = B.SE.SE; B.SE.SE = LP.TL
    try:
        d = B.SE.run(g, order)
    except RecursionError:
        continue
    finally:
        B.SE.SE = saved
    tl = getattr(d, "tl", []); qs = [s for s, (ph, calls) in enumerate(d.log) if ph[0] == 1 - C]
    L = [X.states(B.chain(d.log[s][1], g.n)) for s in qs]; T = []
    for i, (x, y) in enumerate(zip(L, L[1:])):
        p0 = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
        if p0 is None: continue
        t = "N" if p0 >= len(x) or p0 >= len(y) else ("G" if (x[p0][1], x[p0][2]) == (y[p0][1], y[p0][2]) else "O")
        T.append((i, p0, t))
    for k in range(len(T) - 1):
        i, b, t = T[k]
        if t != "G": continue
        i2, c, _ = T[k + 1]
        lp = sorted({pos for s2, pos in tl if s2 == qs[i]})   # search i: the search whose tangles made the G
        key = ("deeper" if c > b else "<=b", "1pos" if len(lp) <= 1 else ">=2pos")
        cnt[key] += 1
        if key == ("deeper", "1pos"): ex.append((os.path.basename(name), i, b, c, lp))
print("order", order); [print(" ", k, v) for k, v in sorted(cnt.items())]; print("  G-NEXT-1P violations:", ex[:5])
