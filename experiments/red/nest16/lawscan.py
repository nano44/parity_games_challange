"""L-RED box 16 (produced on Opus 5.5): DATA laws on q-phases of 𝒞^1P (chains from L-ALG's unmodified b12_pot.run/chain +
b12_core.states via xscore; class set b12_topchain.classgames DIST=1 as neststarscan.py). Per transition at depth-0 position b:
type G (same (rank, V), piece grew) or O ((rank, V) rose) or N (chain length change at b).
  G-NEXT : a G at b is followed by a transition at a position <= b (or ends the phase).
  G-ADJ  : at a G at b, the first stable position after b in the new chain is b + 1 (when one exists).
  O-SEG  : the segment after an O at b > min(P) (deeper than the shallowest position that rises in the phase) (positions > b up to the next <= b) has NEST* <= 1.
  W      : for every position c with window NEST* (1 + NEST* of elements > c between c's first and last occurrence) >= 2, the window
           contains no position < c.
Usage: DTL_ORDER=.. [TRIALS=3 SEED=2 NMAX=200] lawscan.py FILES..."""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
sys.setrecursionlimit(100000); os.environ["DIST"] = "1"
import xscore as X, starclimb as SC
from comb.neststar import nest_star
from b12_topchain import classgames
B = X.B; order = os.environ.get("DTL_ORDER", "stable"); cnt = collections.Counter(); ex = {}; nph = 0; hist = collections.Counter()


def bad(law, name, info):
    cnt[law + " viol"] += 1; ex.setdefault(law, []).append((name, info))


for name, g in classgames(sys.argv[1:], int(os.environ.get("TRIALS", "3")), int(os.environ.get("SEED", "2")), int(os.environ.get("NMAX", "200"))):
    C = X.controller(g)
    if C is None: continue
    name = os.path.basename(name)
    try:
        d = B.run(g, order)
    except RecursionError:
        continue
    phases = {}
    for ph, calls in getattr(d, "log", []): phases.setdefault(ph, []).append(X.states(B.chain(calls, g.n)))
    for ph, L in phases.items():
        if ph[0] != 1 - C: continue
        nph += 1; T = []; ST = max(r for ch in L for _, r, _, _ in ch) if L else 0
        for x, y in zip(L, L[1:]):
            p0 = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
            if p0 is None: continue
            t = "N" if p0 >= len(x) or p0 >= len(y) else ("G" if (x[p0][1], x[p0][2]) == (y[p0][1], y[p0][2]) else "O")
            pool = next((j for j in range(p0 + 1, len(y)) if y[j][1] == g.n + 2), None)
            T.append((p0, t, pool))
        P = [b for b, _, _ in T]; hist[nest_star(tuple(P))] += 1
        for i, (b, t, pool) in enumerate(T):
            seg = []
            for p in P[i + 1:]:
                if p <= b: break
                seg.append(p)
            if t == "G":
                cnt["G"] += 1
                if seg: bad("G-NEXT", name, (ph, i, b, P))
                if pool is not None:
                    cnt["G with pool"] += 1
                    if pool != b + 1: bad("G-ADJ", name, (ph, i, b, pool))
            if t == "O" and b > min(P):
                cnt["O b>minP"] += 1
                if nest_star(tuple(seg)) >= 2: bad("O-SEG", name, (ph, i, b, P))
        for c in set(P):
            if SC.wnest(P, c) >= 2:
                cnt["W windows"] += 1
                i0 = P.index(c); i1 = len(P) - 1 - P[::-1].index(c)
                if any(x < c for x in P[i0:i1 + 1]): bad("W", name, (ph, c, P))
print("order", order, "q-phases", nph, "NEST* histogram", dict(sorted(hist.items())))
for k in sorted(cnt): print(" ", k, cnt[k])
for k, v in ex.items(): print(" ", k, "first:", v[:3])
