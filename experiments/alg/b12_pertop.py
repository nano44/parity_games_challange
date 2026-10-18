"""L-ALG succ. 10 (box 12, produced on Opus 5.5), GAP-A-M §30: tangles LEARNED per (phase, top) on the one-player class 𝒞^1P.
A phase's searches are ≤ (tangles learned in it) + 2, so a polynomial bound per (phase, top) would give GAP-A on 𝒞^1P directly.
Printed per game set: max searches per phase, max tangles learned per phase, max per (phase, top), and the game reaching it.
Same class set as b12_topchain.py. Usage: DTL_ORDER=stable|oink TRIALS=k SEED=s NMAX=n b12_pertop.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
sys.path.insert(0, os.path.join(HERE, "..", "dtl-bench"))
import dtl_pyref as P
from b12_topchain import classgames


class PT(P.DTL):
    def search(self, p):
        self.phase = (p, self.dominions)
        if not hasattr(self, "births"): self.births = []; self.nsearch = {}
        self.nsearch[self.phase] = self.nsearch.get(self.phase, 0) + 1
        return P.DTL.search(self, p)

    def extractTangles(self, top, R):
        k = len(self.tv); r = P.DTL.extractTangles(self, top, R)
        for t in range(k, len(self.tv)):
            self.births.append((self.phase, max(v for v, _ in self.tv[t]), frozenset(v for v, _ in self.tv[t])))
        return r


def run(g, order):
    if order == "oink":
        from stdsort import oink_order
        idx = oink_order(g.prio)
    else:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v))
    new = {v: i for i, v in enumerate(idx)}
    d = PT([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], False, ins_desc=(order == "oink"))
    saved = P.TV_SORTED, P.PEARCE
    if order == "oink": P.TV_SORTED = True; P.PEARCE = True
    try:
        d.run()
    finally:
        P.TV_SORTED, P.PEARCE = saved
    return d


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    trials, seed, nmax = int(os.environ.get("TRIALS", "2")), int(os.environ.get("SEED", "1")), int(os.environ.get("NMAX", "120"))
    best = {"search": (0,), "learn": (0,), "top": (0,)}
    for name, g in classgames(sys.argv[1:], trials, seed, nmax):
        d = run(g, order); per = {}; pt = {}
        for ph, top, _ in getattr(d, "births", []):
            per[ph] = per.get(ph, 0) + 1; pt[(ph, top)] = pt.get((ph, top), 0) + 1
        for key, val in (("search", max(getattr(d, "nsearch", {0: 0}).values())), ("learn", max(per.values(), default=0)),
                         ("top", max(pt.values(), default=0))):
            if val > best[key][0]: best[key] = (val, g.n, name)
        if os.environ.get("VERBOSE"): print(name, g.n, best, flush=True)
    print("order", order, "| max searches/phase", best["search"], "| max learned/phase", best["learn"], "| max learned per (phase, top)", best["top"])
