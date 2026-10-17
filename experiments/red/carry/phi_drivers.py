#!/usr/bin/env python3
"""L-RED (Opus 5.5): classify the drivers of one depth-0 piece change, live, in A_DTL (tracer exact vs Oink), the way L-ALG's
dtl_mirror.py does on C6. Args: GAME.pg SEARCH PIECE. For the change between searches SEARCH-1 and SEARCH at depth-0 piece
PIECE (same context): r0 = first pruning round whose survivor set differs; a driver is a tangle born in SEARCH-1 whose
disabling (all else equal, from the same round-(r0-1) set) undoes the round-r0 survivor set; for each driver: its top h
(max priority, then index), h's death round at that piece in SEARCH-1 (dead before r0 / alive), the rescued vertices
(survive r0 with the driver, not without) and whether all rescued vertices have priority > pr(h) (a CAP carry).
Also counted (L-ALG 38f10e4): a SUFFICIENT singleton, i.e. C alone (every other new tangle disabled) reproduces round r0,
when the round without any new tangle differs; its rescued set is taken against the no-new-tangle round."""
import sys, os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rd", os.path.join(HERE, "redundancy.py"))
rd = importlib.util.module_from_spec(spec); spec.loader.exec_module(rd)
path, SR, PC = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
born = []


class B(rd.RD):
    def __init__(self, *a, **k):
        super().__init__(*a, **k); self.calls = {}; self.d0 = 0; self.rep = None

    def search(self, p):
        self.d0 = 0
        return super().search(p)

    def search_rec(self, R, p, depth):
        self._depth = depth
        return super().search_rec(R, p, depth)

    def extractTangles(self, top, R):
        b = len(self.tv); r = super().extractTangles(top, R)
        for t in range(b, len(self.tv)): born.append(len(self.searches) - 1)
        return r

    def rounds(self, R, p, disabled):
        cur = {v for v in R if self.pr[v] % 2 == p}; out = [frozenset(cur)]
        while cur:
            nx, _ = self.one_round(cur, R, p, disabled)
            if nx == cur: break
            cur = nx; out.append(frozenset(cur))
        return out

    def best_vertices(self, V, R, p):
        if getattr(self, "_depth", 0) == 0:
            si = len(self.searches) - 1
            if self.d0 == PC and si in (SR - 1, SR):
                alive = {t for t in range(len(self.tv)) if self.tpr[t] != -1 and self.tpr[t] % 2 == p}
                self.calls[si] = (frozenset(R), alive, self.rounds(R, p, set()))
                if si == SR:
                    old = {t for t in alive if born[t] < SR - 1}; new = alive - old
                    ra, rb = self.calls[SR - 1][2], self.calls[SR][2]
                    pick = lambda L, r: L[r] if r < len(L) else frozenset()
                    r0 = next(r for r in range(1, max(len(ra), len(rb)) + 1) if pick(ra, r) != pick(rb, r))
                    prev = rb[r0 - 1]; target = pick(rb, r0)
                    out = []
                    none, _ = self.one_round(set(prev), R, p, set(new))   # every new tangle disabled
                    for C in sorted(new):
                        without, _ = self.one_round(set(prev), R, p, {C})
                        alone, _ = self.one_round(set(prev), R, p, set(new) - {C})
                        nec, suf = without != target, alone == target and none != target
                        if not (nec or suf): continue
                        if not nec: without = none                        # sufficient singleton (L-ALG 38f10e4): rescued vs no new tangle
                        vs = [w for w, _ in self.tv[C]]; h = max(vs, key=lambda v: (self.pr[v], v))
                        death = next((r for r in range(1, len(ra)) if h not in ra[r]), None)
                        st = "dead_before_r0" if death is not None and death < r0 else ("alive_pruned_at_r0" if death == r0 else "alive_survives_r0")
                        resc = set(target) - set(without)
                        cap = bool(resc) and all(self.pr[u] > self.pr[h] for u in resc)
                        out.append((C, self.idx[h], self.pr[h], st, sorted(self.idx[u] for u in resc), sorted(self.pr[u] for u in resc), cap,
                                    "necessary" if nec else "sufficient_only"))
                    self.rep = dict(r0=r0, same_context=self.calls[SR - 1][0] == R, drivers=out,
                                    deaths_prev={self.idx[v]: next((r for r in range(1, len(ra)) if v not in ra[r]), "end") for v in ra[0]},
                                    deaths_now={self.idx[v]: next((r for r in range(1, len(rb)) if v not in rb[r]), "end") for v in rb[0]})
            self.d0 += 1
        return super().best_vertices(V, R, p)


d = rd.run.__globals__["ff"].pg.read(path)
from stdsort import oink_order
idx = oink_order(d.prio); newi = {v: i for i, v in enumerate(idx)}
b = B([d.prio[v] for v in idx], [d.owner[v] for v in idx], [[newi[w] for w in d.succ[v]] for v in idx], False, ins_desc=True)
b.idx = idx
rd.dtl_py.TV_SORTED = True; rd.dtl_py.PEARCE = True
sys.setrecursionlimit(100000); b.run()
print(b.rep)
