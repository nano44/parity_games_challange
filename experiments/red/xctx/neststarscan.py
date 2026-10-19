"""L-RED box 15 (produced on Opus 5.5): NEST* (comb/neststar.py) of q-phases over L-ALG's class set (b12_topchain.classgames,
DIST=1: in-class files as given, others forced into 𝒞_C, 3 trials). Prints the max per file and the overall top list.
Usage: DTL_ORDER=.. [TRIALS=3 SEED=2 NMAX=200] neststarscan.py FILES..."""
import sys, os
sys.setrecursionlimit(100000); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X, nestclass as NC
from comb.neststar import nest_star
from b12_topchain import classgames
os.environ["DIST"] = "1"; order = os.environ.get("DTL_ORDER", "stable"); rows = []
for name, g in classgames(sys.argv[1:], int(os.environ.get("TRIALS", "3")), int(os.environ.get("SEED", "2")), int(os.environ.get("NMAX", "200"))):
    C = X.controller(g)
    if C is None: continue
    try:
        P, _ = NC.positions(g, order, C)
    except RecursionError:
        continue
    for ph, p in P.items():
        rows.append((nest_star(tuple(p)), len(p) + 1, g.n, name))
rows.sort(reverse=True)
print("order", order, "q-phases", len(rows), "NEST* histogram", {k: sum(1 for r in rows if r[0] == k) for k in sorted({r[0] for r in rows})})
for r in rows[:15]: print("  NEST*", r[0], "S", r[1], "n", r[2], r[3])
