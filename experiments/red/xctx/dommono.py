"""L-RED box 15 (produced on Opus 5.5): mechanical check of R47 Lemma DOM-MONO on 𝒞^1P. Every Dom call (dtl_pyref dom(), the
model behind b12_pot, unmodified, wrapped) records its input (R, V, X) and X after each top step. For two calls of one phase with
the same input, the later one must have X_i ⊇ X_i of the earlier one for every step i.
Usage: DTL_ORDER=.. dommono.py random COUNT NMIN NMAX SEED | dommono.py FILES..."""
import sys, os, random, glob
sys.setrecursionlimit(100000); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X
from fixd_oneplayer import start
B = X.B


class DM(B.CH):
    def dom(self, V, R, Xs, p):
        key = (frozenset(R), frozenset(V), frozenset(Xs)); steps = []
        for top in range(self.n - 1, -1, -1):
            if top not in V or top in Xs:
                steps.append(frozenset(Xs)); continue
            Xs.add(top); self.str[top] = -1; self.Q = [top]
            self.tattr(p, Xs, R, R, self.pr[top], R)
            steps.append(frozenset(Xs))
        if not hasattr(self, "domlog"): self.domlog = []
        self.domlog.append((getattr(self, "phase", None), key, steps))


def check(g, order):
    saved = B.SE.SE; B.SE.SE = DM
    try:
        d = B.SE.run(g, order)
    finally:
        B.SE.SE = saved
    seen = {}; pairs = bad = 0
    for ph, key, steps in getattr(d, "domlog", []):
        for old in seen.get((ph, key), []):
            pairs += 1; bad += any(not (a <= b) for a, b in zip(old, steps))
        seen.setdefault((ph, key), []).append(steps)
    return pairs, bad


if __name__ == "__main__":
    order = os.environ.get("DTL_ORDER", "stable"); P = Bd = 0
    if sys.argv[1] == "random":
        cnt, nmin, nmax, seed = (int(x) for x in sys.argv[2:6]); rnd = random.Random(seed)
        src = (X.distinct(start(rnd.randint(0, 1), N, N, rnd)) for N in (rnd.randint(nmin, nmax) for _ in range(cnt)))
    else:
        src = (X.distinct(X.pg.read(f)) for f in sys.argv[1:])
    for g in src:
        if X.controller(g) is None: continue
        try:
            p, b = check(g, order)
        except RecursionError:
            continue
        P += p; Bd += b
    print("order", order, "same-input Dom call pairs", P, "DOM-MONO violations", Bd)
