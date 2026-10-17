"""L-ALG (produced on Opus 5.5, 2026-10-16). Measurement-only prototype of the ideal-pruning variant (C6 idea): best_vertices' survivor set uses U_hat instead of
the consumed union U; everything else (sptl, Dom, cut, recursion) is dtl_pyref's code (docs/alg/candidates/C6-DTLhat.md).
Usage: dtl_c6proto.py [G.pg ...]   (plus 1,500 seeded random games; prints DTL vs C6 counts and correctness)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, dtl_ideal as I, pg, gen, zielonka, verify

class C6(D.DTL):
    def best_vertices(self, V, R, p):
        V.clear(); V.update(v for v in R if self.pr[v] % 2 == p)
        if not V:
            return 0
        tl = [t for t in range(len(self.tv)) if I.alive(self, t, p)]
        while True:
            prevV = set(V)
            Uh = I.ideal_union(self, p, V, R, tl)
            S = I.survivors(self, p, V, R, Uh, tl)
            if S == V:
                return 1
            V.clear(); V.update(S)
            if not V:
                V.update(prevV); return -1

def run(cls, g):
    idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
    d = cls([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx])
    win, st = d.run()
    W = [None]*g.n; Sx = [None]*g.n
    for i, v in enumerate(idx):
        W[v] = win[i]; Sx[v] = idx[st[i]] if st[i] is not None and st[i] != -1 else None
    return d, W, Sx

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    bad = 0; diff = 0; tot = [0, 0, 0, 0]
    rnd = gen.Rng("c6")
    games = [(f, pg.read(f)) for f in sys.argv[1:]]
    for i in range(1500):
        n = rnd.randint(3, 20); games.append((f"r{i}", gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())))
    for name, g in games:
        ref = zielonka.solve(g)
        d6, W6, S6 = run(C6, g); d0, W0, S0 = run(D.DTL, g)
        ok = W6 == list(ref) and not verify.check(g, W6, S6)
        if None in W6 or not ok:
            bad += 1; print("C6 WRONG/INCOMPLETE", name)
        if (d6.iterations, d6.tangles) != (d0.iterations, d0.tangles):
            diff += 1
        if not name.startswith("r"):
            print(name.split("/")[-1], "DTL it/tangles", d0.iterations, d0.tangles, "| C6", d6.iterations, d6.tangles)
    print("games", len(games), "C6 wrong/incomplete", bad, "games where counts differ", diff)
