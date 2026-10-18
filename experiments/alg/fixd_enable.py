"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §28f: compounding condition (b) of §29. For consecutive searches s, s+1 of
a phase, let j be the depth-0 position of the first differing depth-0 call (as in fixd_outcome.py; for "CTX" transitions the
first index whose R differs, minus one). The ENABLING tangles are those born in search s that fire in a region step of the
depth-0 call at position j in search s+1. For each, its birth position: the depth-0 position whose subtree held the birth (the
depth-0 call itself, or a deeper call made after it), and the birth depth. Condition (b) needs births BELOW j (position > j).
Printed: counts of enabling births by (position relative to j: "<j" / "=j" / ">j") and depth (0 / >0), and transitions with no
enabling tangle at j. Usage: DTL_ORDER=stable|oink fixd_enable.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
sys.path.insert(0, os.path.join(HERE, "..", "dtl-bench"))
import pg, dtl_pyref as P, dtl_step5stats as ST


class EN(P.DTL):
    def search(self, p):
        self.phase = (p, self.dominions); self.sidx = getattr(self, "sidx", -1) + 1; self.calls = []; self.pos = -1
        if not hasattr(self, "log"): self.log = []; self.birth = {}
        r = P.DTL.search(self, p); self.log.append((self.phase, self.calls)); return r

    def search_rec(self, R, p, depth):
        old = getattr(self, "_dep", 0); self._dep = depth
        try:
            return P.DTL.search_rec(self, R, p, depth)
        finally:
            self._dep = old

    def attractTangle(self, t, p, R, Z, Gx, maxpr):
        ok = P.DTL.attractTangle(self, t, p, R, Z, Gx, maxpr)
        if ok and getattr(self, "_inreg", False): self._fired.add(t)
        return ok

    def extractTangles(self, top, R):
        k = len(self.tv); r = P.DTL.extractTangles(self, top, R)
        for t in range(k, len(self.tv)): self.birth[t] = (self.sidx, self.pos, getattr(self, "_dep", 0))
        return r

    def best_vertices(self, V, R, p):
        dep = getattr(self, "_dep", 0)
        if dep == 0: self.pos += 1
        Rk = frozenset(R); self._fired = set(); self._inreg = True
        # region steps fire tangles; the threshold loop also calls attractTangle (Gx = R): exclude it by toggling below
        res = self._bv(V, R, p)
        self._inreg = False
        if dep == 0: self.calls.append((Rk, res, frozenset(V), frozenset(self._fired)))
        return res

    def _bv(self, V, R, p):
        V.clear(); V.update(v for v in R if self.pr[v] % 2 == p)
        if not V:
            return 0
        while True:
            prevV = set(V)
            Z = set(); CurR = set(R)
            for top in range(self.n - 1, -1, -1):
                if top not in V or top in Z:
                    continue
                CurZ = {top}; self.Q = [top]; self._inreg = True
                self.tattr(p, CurZ, CurR, CurR, self.pr[top], CurR)
                self._inreg = False
                Z |= CurZ
            cand = [v for v in sorted(V, reverse=True) if not self.attracts(p, v, Z, R)]
            if not cand:
                return 1
            for t in [0] + [q for q in self.prios if q > 0 and q <= self.maxpr]:
                self.Q = sorted(Z)
                self.tattr(p, Z, R, R, t, None)
                keep = []
                for i, u in enumerate(cand):
                    if self.pr[u] <= t:
                        keep += cand[i:]; break
                    if not self.attracts(p, u, Z, R):
                        keep.append(u)
                cand = keep
            V -= set(cand)
            if not cand:
                return 1
            if not V:
                V.clear(); V.update(prevV)
                return -1


def run(g, order):
    if order == "oink":
        from stdsort import oink_order
        idx = oink_order(g.prio)
    else:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v))
    new = {v: i for i, v in enumerate(idx)}
    d = EN([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], False, ins_desc=(order == "oink"))
    saved = P.TV_SORTED, P.PEARCE
    if order == "oink": P.TV_SORTED = True; P.PEARCE = True
    try:
        d.run()
    finally:
        P.TV_SORTED, P.PEARCE = saved
    return d


def first_j(a, b):
    for j in range(min(len(a), len(b))):
        if a[j][0] != b[j][0]: return j - 1          # outcomes agreed; the difference arose after call j-1
        if a[j][1:3] != b[j][1:3]: return j
    return None


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable"); tot = {}; none_ = 0; trans = 0
    for f, g in ST.games(sys.argv[1:]):
        d = run(g, order); log = getattr(d, "log", [])
        for s in range(len(log) - 1):
            (pa, ca), (pb, cb) = log[s], log[s + 1]
            if pa != pb: continue
            j = first_j(ca, cb)
            if j is None or j < 0: continue
            trans += 1
            fired = cb[j][3]; en = [t for t in fired if d.birth.get(t, (None,))[0] == s]
            if not en: none_ += 1
            for t in en:
                _, bp, bd = d.birth[t]
                k = ("<j" if bp < j else "=j" if bp == j else ">j", "depth0" if bd == 0 else "deeper")
                tot[k] = tot.get(k, 0) + 1
    print("order", order, "transitions", trans, "with no enabling tangle firing at R_j", none_, "| enabling births:", dict(sorted(tot.items())))
