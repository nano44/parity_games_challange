"""L-ALG (produced on Opus 5.5, 2026-10-16): counter for conjecture (CU), GAP-A-M.md §9 ((CU) is FALSE: instances/dtl_cu_viol_n24.pg). (CU) said: in every sptl pass, a top blocked by W
(it extracted earlier in the same search) whose region is closed has, as its SCC, a stored tangle or a set with no escapes
(a dominion), as long as the search has found no dominion yet. Usage: dtl_wblock.py [G.pg ...] (+ 600 seeded random games)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, pg, gen
cnt = {"passes": 0, "blocked_closed": 0, "blocked_new_scc": 0, "final_pass_blocked_new": 0}
ex = []
def sccs_from(d, top, Z):
    p = d.pr[top] % 2; st, ow = d.str, d.ow
    def succ(v):
        if ow[v] == p:
            s_ = st[v]; return [s_] if s_ != -1 and s_ in Z else []
        return [w for w in d.outs[v] if w in Z]
    # Tarjan from top (same as dtl_pyref non-Pearce)
    index, low, on, stack, cnt_, out = {}, {}, set(), [], 0, []
    index[top] = low[top] = 0; cnt_ = 1; stack.append(top); on.add(top); work = [(top, iter(succ(top)))]
    while work:
        v, it = work[-1]; pushed = False
        for w in it:
            if w not in index:
                index[w] = low[w] = cnt_; cnt_ += 1; stack.append(w); on.add(w); work.append((w, iter(succ(w)))); pushed = True; break
            elif w in on: low[v] = min(low[v], index[w])
        if pushed: continue
        work.pop()
        if work: low[work[-1][0]] = min(low[work[-1][0]], low[v])
        if low[v] == index[v]:
            C = []
            while True:
                w = stack.pop(); on.discard(w); C.append(w)
                if w == v: break
            out.append(C)
    res = []
    for C in out:
        if len(C) == 1:
            v = C[0]
            if not (st[v] == v or (st[v] == -1 and v in d.outs[v])): continue
        res.append(sorted(C))
    return res
class WB(D.DTL):
    def search(self, p):
        self._dom_at_search = self.dominions
        return super().search(p)

    def sptl(self, V, R, p):
        changes = False; blocked_new = 0
        for top in range(self.n - 1, -1, -1):
            if top not in V or top not in R: continue
            Z = {top}; self.str[top] = -1; self.Q = [top]
            self.tattr(p, Z, R, R, self.pr[top], R)
            closed = (self.str[top] != -1) if self.ow[top] == p else not any(w in R for w in self.outs[top])
            if closed and top in self.W and self.dominions == self._dom_at_search:
                # (CU) is claimed only while the search has found no dominion: after a dominion everything learned in the
                # search is solved or deleted at its end (search(), 1023-1040).
                cnt["blocked_closed"] += 1
                for C in sccs_from(self, top, Z):
                    Cs = set(C)
                    esc = [w for v in C if self.ow[v] != p for w in self.outs[v] if w in self.G and w not in Cs]
                    if not esc:
                        cnt["blocked_dominion"] = cnt.get("blocked_dominion", 0) + 1; continue
                    if C not in self.tkeys:
                        cnt["blocked_new_scc"] += 1; blocked_new += 1
                        if len(ex) < 3: ex.append((top, C))
            if closed and top not in self.W:
                self.W.add(top)
                if self.extractTangles(top, Z): changes = True
        cnt["passes"] += 1
        if not changes and blocked_new: cnt["final_pass_blocked_new"] += 1
        return changes
rnd = gen.Rng("wblock"); games = [pg.read(f) for f in sys.argv[1:]]
for i in range(600):
    n = rnd.randint(8, 26); games.append(gen.random_game(n, rnd.randint(2, n+1), 1, rnd.randint(1, 3), rnd.next64()))
sys.setrecursionlimit(100000)
for g in games:
    idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
    d = WB([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx]); d.run()
print(cnt, ex[:2])
