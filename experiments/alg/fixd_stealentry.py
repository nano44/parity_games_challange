"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §28c: mechanical test of Lemma STEAL-ENTRY on dtl_pyref runs.
Every best_vertices region step (round r, top τ) records, per vertex added, how it entered (top / attractVertices via edge to z
/ attractTangle t″ with strategy s) and which tangles fired. For consecutive visits i, i+1 of the same context R in one phase
(player and dominion count fixed), each tangle t that fired at (r, τ) in visit i and is met-not-contained by the prefix
P_{i+1}(τ⁺) is a relevant steal; the lemma says some y ∈ A = t ∩ P_{i+1}(τ⁺) is (a) a prefix top, or (b) a p-vertex whose entry
strategy differs from its strategy in t. Printed: steals, case (a), case (b) only, VIOLATIONS (neither), and for case (b) the
number of distinct conflict edges (y, z) and the max number of visit pairs one conflict edge appears in.
Usage: DTL_ORDER=stable|oink fixd_stealentry.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
sys.path.insert(0, os.path.join(HERE, "..", "dtl-bench"))
import pg, dtl_pyref as P, dtl_step5stats as ST
PRE = [0]   # fired tangles at (r, τ) with a vertex that is a round-r top above τ at the next visit


class SE(P.DTL):
    def search(self, p):
        self.phase = (p, self.dominions); return P.DTL.search(self, p)

    def attractVertices(self, p, v, R, Z, Gx, maxpr):
        before = set(Z) if getattr(self, "_rec", None) is not None else None
        P.DTL.attractVertices(self, p, v, R, Z, Gx, maxpr)
        if before is not None:
            for u in Z - before: self._rec[u] = ("v", v)

    def attractTangle(self, t, p, R, Z, Gx, maxpr):
        before = set(Z) if getattr(self, "_rec", None) is not None else None
        ok = P.DTL.attractTangle(self, t, p, R, Z, Gx, maxpr)
        if ok and before is not None:
            self._fired.add(t); s = dict(self.tv[t])
            for u in Z - before: self._rec[u] = ("t", t, s[u])
        return ok

    def best_vertices(self, V, R, p):
        V.clear(); V.update(v for v in R if self.pr[v] % 2 == p)
        if not V:
            return 0
        rounds = []
        if not hasattr(self, "visits"): self.visits = []
        self.visits.append((self.phase, frozenset(R), p, rounds))
        while True:
            prevV = set(V)
            Z = set(); CurR = set(R); steps = []
            for top in range(self.n - 1, -1, -1):
                if top not in V or top in Z:
                    continue
                CurZ = {top}; self.Q = [top]; self._rec = {top: ("top",)}; self._fired = set(); pref = frozenset(Z)
                self.tattr(p, CurZ, CurR, CurR, self.pr[top], CurR)
                steps.append((top, pref, dict(self._rec), set(self._fired)))
                self._rec = None
                Z |= CurZ
            rounds.append(steps)
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
    d = SE([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], False, ins_desc=(order == "oink"))
    saved = P.TV_SORTED, P.PEARCE
    if order == "oink": P.TV_SORTED = True; P.PEARCE = True
    try:
        d.run()
    finally:
        P.TV_SORTED, P.PEARCE = saved
    return d


def analyze(d):
    by = {}
    for ph, R, p, rounds in d.visits: by.setdefault((ph, R), []).append((p, rounds))
    steals = ca = cb = viol = 0; conflict = {}; ex = None
    for key, vl in by.items():
        for i in range(len(vl) - 1):
            p, ra = vl[i]; _, rb = vl[i + 1]
            for r, steps in enumerate(ra):
                if r >= len(rb): continue
                prefb = {top: (pref, rec) for top, pref, rec, _ in rb[r]}
                tops_b = {top for top, _, _, _ in rb[r]}
                for top, _, _, fired in steps:
                    # prefix before top in visit i+1 = union of the regions of the round-r tops above top
                    Pb = set(); recb = {}
                    for t2, pref2, rec2, _ in rb[r]:
                        if t2 > top: Pb |= set(rec2); recb.update(rec2)
                    for t in fired:
                        tv = dict(d.tv[t]); A = set(tv) & Pb
                        if any(y in tops_b and y > top for y in tv): PRE[0] += 1   # case-(a) precondition (steal or not)
                        if not A or set(tv) <= Pb: continue
                        steals += 1
                        a = [y for y in A if y in tops_b and y > top]
                        b = [y for y in A if d.ow[y] == p and recb.get(y, ("?",))[0] in ("v", "t")
                             and (recb[y][1] if recb[y][0] == "v" else recb[y][2]) != tv[y] and tv[y] not in A]
                        if a: ca += 1
                        elif b:
                            cb += 1
                            for y in b:
                                z = recb[y][1] if recb[y][0] == "v" else recb[y][2]
                                conflict.setdefault((y, z), set()).add((key, i))
                        else:
                            viol += 1
                            if ex is None: ex = (key[0], len(key[1]), r, top, t, sorted(A))
    mx = max((len(s) for s in conflict.values()), default=0)
    return steals, ca, cb, viol, len(conflict), mx, ex


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    for f, g in ST.games(sys.argv[1:]):
        d = run(g, order); s, a, b, v, nc, mx, ex = analyze(d)
        print(os.path.basename(f), "steals", s, "case (a)", a, "case (b) only", b, "VIOLATIONS", v, "| conflict edges", nc,
              "max visit pairs per conflict edge", mx, "| first violation", ex, "| case-(a) precondition", PRE[0], flush=True)
        PRE[0] = 0
