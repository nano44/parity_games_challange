"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §28: (TOP-CHAIN) "the tangles learned in one phase with the same top
vertex (the highest-priority vertex of the tangle) form a ⊆-chain". With it, a phase learns at most n tangles per top,
so <= n^2 tangles and, every non-final search learning one, <= n^2 + n + 1 searches per phase. Model: dtl_pyref (order datum
from DTL_ORDER: stable | oink), tangles recorded in creation order with the phase they were born in.
Printed per game: phases, tangles, max tangles with one top in one phase, and the number of (phase, top) groups that are NOT
chains, with the first crossing pair. Usage: DTL_ORDER=oink|stable fixd_topchain.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_pyref as P, dtl_step5stats as ST


class TC(P.DTL):
    def search(self, p):
        self.cur_phase = (p, self.dominions)          # a phase of p ends with a dominion-finding search (R5 (g))
        k = len(self.tv); r = P.DTL.search(self, p)
        if not hasattr(self, "born"): self.born = {}
        for t in range(k, len(self.tv)): self.born[t] = self.cur_phase
        return r


def run(g, order):
    if order == "oink":
        from stdsort import oink_order
        idx = oink_order(g.prio)
    else:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v))
    new = {v: i for i, v in enumerate(idx)}
    d = TC([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], False, ins_desc=(order == "oink"))
    saved = P.TV_SORTED, P.PEARCE
    if order == "oink": P.TV_SORTED = True; P.PEARCE = True
    try:
        d.run()
    finally:
        P.TV_SORTED, P.PEARCE = saved
    return d, idx


def analyze(g, order):
    d, idx = run(g, order)
    groups = {}
    for t, tv in enumerate(d.tv):
        vs = frozenset(v for v, _ in tv); top = max(vs)     # vertices are indexed in priority order: max index = top
        groups.setdefault((d.born.get(t), top), []).append(vs)
    bad = 0; first = None; mx = 0
    for key, L in groups.items():
        mx = max(mx, len(L))
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                a, b = L[i], L[j]
                if not (a <= b or b <= a):
                    bad += 1
                    if first is None: first = (sorted(idx[v] for v in a), sorted(idx[v] for v in b))
                    break
            else:
                continue
            break
    return len(d.tv), len(groups), mx, bad, first


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    for f, g in ST.games(sys.argv[1:]):
        nt, ng, mx, bad, first = analyze(g, order)
        print(os.path.basename(f), "tangles", nt, "(phase, top) groups", ng, "max per group", mx, "NON-CHAIN groups", bad,
              "first crossing", first, flush=True)
