"""L-ALG (produced on Opus 5.5, 2026-10-16): DATA for GAP-A-M.md Lemma D2: at every stable piece, every region of the
last sptl pass lies in Dom(V*, R) united with the previously removed X. Usage: dtl_sptldom.py [G.pg ...] (+ 800 random)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, pg, gen
cnt = {"stable_pieces": 0, "viol": 0}
ex = []
class SD(D.DTL):
    def sptl(self, V, R, p):
        changes = False; self._regs = []
        for top in range(self.n - 1, -1, -1):
            if top not in V or top not in R: continue
            Z = {top}; self.str[top] = -1; self.Q = [top]
            self.tattr(p, Z, R, R, self.pr[top], R)
            self._regs.append(set(Z))
            closed = (self.str[top] != -1) if self.ow[top] == p else not any(w in R for w in self.outs[top])
            if closed and top not in self.W:
                self.W.add(top)
                before = len(self.tv)
                if self.extractTangles(top, Z): changes = True
        return changes
    def dom(self, V, R, X, p):
        regs = getattr(self, "_regs", None)
        Xb = set(X)
        super().dom(V, R, X, p)
        if regs is not None:
            cnt["stable_pieces"] += 1
            U = set().union(*regs) if regs else set()
            added = X - Xb
            if not U <= added | Xb:
                cnt["viol"] += 1
                if len(ex) < 3: ex.append((sorted(V), sorted(U - added - Xb)))
            self._regs = None
rnd = gen.Rng("sptldom"); games = [pg.read(f) for f in sys.argv[1:]]
for i in range(800):
    n = rnd.randint(6, 28); games.append(gen.random_game(n, rnd.randint(2, n+1), 1, rnd.randint(1, 3), rnd.next64()))
sys.setrecursionlimit(100000)
for g in games:
    idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
    d = SD([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx]); d.tkeys = []; d.run()
print(cnt, ex)
