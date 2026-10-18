"""q-phase depth >= 1 births and identical-chain transitions over L-ALG's class set (b12_topchain.classgames, DIST=1).
Usage: DTL_ORDER=.. [TRIALS=3 SEED=2 NMAX=200] deepclass.py FILES..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deep as D
from b12_topchain import classgames
sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable"); os.environ["DIST"] = "1"
T = [0, 0, 0, 0]; hits = []
for name, g in classgames(sys.argv[1:], int(os.environ.get("TRIALS", "3")), int(os.environ.get("SEED", "2")), int(os.environ.get("NMAX", "200"))):
    C = D.X.controller(g)
    if C is None: continue
    try:
        sc, d = D.score(g, order, C)
    except RecursionError:
        continue
    T[0] += 1; T[1] += sc[3]; T[2] += sc[0]; T[3] += sc[1]
    if sc[0] or sc[1]: hits.append((name, g.n, sc))
print("order", order, "class games", T[0], "q-transitions", T[1], "identical-chain", T[2], "q-phase depth>=1 births", T[3], "hits", hits[:8])
