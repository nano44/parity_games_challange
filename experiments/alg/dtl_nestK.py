"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), queue item (3): per-level deficit counts in one phase of A_DTL.
For each phase (one player, no dominion in between) and each depth-0 piece index j: for every context C seen at j, k(j, C) =
number of consecutive search pairs in which piece j has context C in both, the ideal (C6) (result, V) is the same and the
actual (result, V) differs (a DEF change at C; not only first-difference pieces). Reports per phase with any DEF:
K_j = max_C k(j, C), N_j = sum_C k(j, C), c_j = #contexts at j with k >= 1, and the products prod_j max(K_j, 1) and
N_0 * N_1. Usage: DTL_ORDER=oink dtl_nestK.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_deficit as X, pg

def phases(d):
    cur = []
    for tr in d.trace:
        if cur and (tr["p"] != cur[-1]["p"] or tr["dom"] != cur[-1]["dom"]):
            yield cur; cur = []
        cur.append(tr)
    if cur: yield cur

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    best = {}
    for f in sys.argv[1:]:
        g = pg.read(f); d = X.build(g); d.run(); name = os.path.basename(f)
        for ph in phases(d):
            k = {}
            for a, b in zip(ph, ph[1:]):
                for j in range(min(len(a["pieces"]), len(b["pieces"]))):
                    (Ra, ra, Va, rha, Vha), (Rb, rb, Vb, rhb, Vhb) = a["pieces"][j], b["pieces"][j]
                    if Ra == Rb and (rha, Vha) == (rhb, Vhb) and (ra, Va) != (rb, Vb):
                        k[(j, Ra)] = k.get((j, Ra), 0) + 1
            if not k: continue
            J = max(j for j, _ in k) + 1
            K = [max([c for (jj, _), c in k.items() if jj == j] or [0]) for j in range(J)]
            N = [sum(c for (jj, _), c in k.items() if jj == j) for j in range(J)]
            C = [sum(1 for (jj, _) in k if jj == j) for j in range(J)]
            prod = 1
            for x in K: prod *= max(x, 1)
            print(f"{name} n={g.n} p={ph[0]['p']} searches={len(ph)} K={K} N={N} c={C} prodK={prod} N0*N1={N[0] * (N[1] if J > 1 else 0)} totalDEF={sum(N)}")
