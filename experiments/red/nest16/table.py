"""L-RED box 16 (produced on Opus 5.5): per instance and order: n, S (q-phase searches), |P| (chain-changing transitions),
I = S - 1 - |P| (chain-keeping), NEST*; plus every (G-NEXT) / (G-ADJ) violation with its transition index. Chains from L-ALG's
unmodified b12_pot.run / chain + b12_core.states (via xscore). Usage: table.py G.pg ..."""
import sys, os, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
import xscore as X
from comb.neststar import nest_star
B = X.B; sys.setrecursionlimit(100000)
for f in sys.argv[1:]:
    sha = hashlib.sha1(open(f, "rb").read()).hexdigest()
    g = X.distinct(X.pg.read(f)); C = X.controller(g)
    for order in ("stable", "oink"):
        d = B.run(g, order); L = [X.states(B.chain(c, g.n)) for ph, c in d.log if ph[0] == 1 - C]
        S = len(L); P = []; T = []; viol = []
        for i, (x, y) in enumerate(zip(L, L[1:])):
            p0 = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
            if p0 is None: continue
            t = "N" if p0 >= len(x) or p0 >= len(y) else ("G" if (x[p0][1], x[p0][2]) == (y[p0][1], y[p0][2]) else "O")
            pool = next((j for j in range(p0 + 1, len(y)) if y[j][1] == g.n + 2), None)
            T.append((i, p0, t, pool)); P.append(p0)
        for k, (i, p0, t, pool) in enumerate(T):
            if t != "G": continue
            if k + 1 < len(T) and T[k + 1][1] > p0: viol.append(f"G-NEXT: search {i}->{i+1}, transition #{k}, G at {p0}, next at {T[k+1][1]}")
            if pool is not None and pool != p0 + 1: viol.append(f"G-ADJ: search {i}->{i+1}, transition #{k}, G at {p0}, stable piece at {pool}")
        print(f"{os.path.basename(f)} sha1 {sha[:12]} {order}: n {g.n} S {S} |P| {len(P)} I {S - 1 - len(P)} NEST* {nest_star(tuple(P))}")
        for v in viol: print("   ", v)
