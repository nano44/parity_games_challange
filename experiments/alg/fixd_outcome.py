"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §28d: what changes at the first differing depth-0 best_vertices call of
consecutive searches s, s+1 of a phase (dtl_pyref, instrumented). For each search the depth-0 calls are listed in order with
(R, result, final V). At the first index j where they differ:
  CTX     the depth-0 call outcomes agree up to j but R_j differs: the difference arose BETWEEN depth-0 calls (a deeper
          search_rec call, a threshold or Dom attractor, or sptl);
  -1->ST  result -1 in s, stable in s+1;     ST->-1  the reverse;
  PV-GROW / PV-SHRINK / PV-OTHER   both -1, prevV ⊂ / ⊃ / incomparable (PV-SHRINK is the §27d mechanism: a later emptying
          round with a smaller last nonempty V; the emptying round itself is not recorded here);
  VS-GROW / VS-SHRINK / VS-OTHER   both stable, V* ⊂ / ⊃ / incomparable;
  SAME    same (R, result, V): the difference is inside the call (regions) or deeper / later; then j is the first index whose
          NEXT context differs, if any (RECUT-LATER).
Also counted: whether the chain below j is re-cut (some later depth-0 context differs). Usage: DTL_ORDER=stable|oink fixd_outcome.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
sys.path.insert(0, os.path.join(HERE, "..", "dtl-bench"))
import pg, dtl_pyref as P, dtl_step5stats as ST


class OC(P.DTL):
    def search(self, p):
        self.phase = (p, self.dominions); self.calls = []
        r = P.DTL.search(self, p)
        if not hasattr(self, "log"): self.log = []
        self.log.append((self.phase, self.calls)); return r

    def search_rec(self, R, p, depth):
        old = getattr(self, "_dep", 0); self._dep = depth
        try:
            return P.DTL.search_rec(self, R, p, depth)
        finally:
            self._dep = old

    def best_vertices(self, V, R, p):
        Rk = frozenset(R)
        res = P.DTL.best_vertices(self, V, R, p)
        if getattr(self, "_dep", 0) == 0 and hasattr(self, "calls"):
            self.calls.append((Rk, res, frozenset(V)))
        return res


def run(g, order):
    if order == "oink":
        from stdsort import oink_order
        idx = oink_order(g.prio)
    else:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v))
    new = {v: i for i, v in enumerate(idx)}
    d = OC([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], False, ins_desc=(order == "oink"))
    saved = P.TV_SORTED, P.PEARCE
    if order == "oink": P.TV_SORTED = True; P.PEARCE = True
    try:
        d.run()
    finally:
        P.TV_SORTED, P.PEARCE = saved
    return d


def classify(a, b):
    for j in range(min(len(a), len(b))):
        (Ra, ra, Va), (Rb, rb, Vb) = a[j], b[j]
        if Ra != Rb: return "CTX", j
        if (ra, Va) == (rb, Vb): continue
        if ra == -1 and rb == 1: return "-1->ST", j
        if ra == 1 and rb == -1: return "ST->-1", j
        if ra == -1:
            return ("PV-GROW" if Va < Vb else "PV-SHRINK" if Vb < Va else "PV-OTHER"), j
        return ("VS-GROW" if Va < Vb else "VS-SHRINK" if Vb < Va else "VS-OTHER"), j
    return "SAME", None


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable"); tot = {}; recut = {}
    for f, g in ST.games(sys.argv[1:]):
        d = run(g, order)
        log = getattr(d, "log", [])
        for (pa, ca), (pb, cb) in zip(log, log[1:]):
            if pa != pb: continue                      # a phase boundary: not consecutive searches of one phase
            k, j = classify(ca, cb); tot[k] = tot.get(k, 0) + 1
            if j is not None:
                rc = any(x[0] != y[0] for x, y in zip(ca[j + 1:], cb[j + 1:])) or len(ca) != len(cb)
                recut[(k, rc)] = recut.get((k, rc), 0) + 1
    print("order", order, "| first differing depth-0 outcome:", dict(sorted(tot.items())))
    print("with the chain below re-cut (True) or not:", dict(sorted(recut.items(), key=str)))
