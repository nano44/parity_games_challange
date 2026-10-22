"""L-RED box 16 (produced on Opus 5.5): segstat over L-ALG's class set (b12_topchain.classgames, DIST=1, as neststarscan.py).
Also counts (G-NEXT) violations: a case-G transition at b followed by a transition at a position > b.
Usage: DTL_ORDER=.. [TRIALS=3 SEED=2 NMAX=200] segscan.py FILES..."""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
sys.setrecursionlimit(100000); os.environ["DIST"] = "1"
import xscore as X, segstat as S
from b12_topchain import classgames
order = os.environ.get("DTL_ORDER", "stable"); H = collections.Counter(); ex = {}; nph = 0
for name, g in classgames(sys.argv[1:], int(os.environ.get("TRIALS", "3")), int(os.environ.get("SEED", "2")), int(os.environ.get("NMAX", "200"))):
    C = X.controller(g)
    if C is None: continue
    try:
        for ph, T in S.trans(g, order, C):
            nph += 1
            for b, t, s in S.segs(T):
                H[(t, s)] += 1
                if (t == "G" and s > 0) or s >= 2: ex.setdefault((t, s), []).append((os.path.basename(name), b))
    except RecursionError:
        pass
print("order", order, "q-phases", nph)
for k in sorted(H): print(k, H[k], ex.get(k, [])[:5])
