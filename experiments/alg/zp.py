#!/usr/bin/env python3
"""C3: ZP = Zielonka's recursion with psolC (NE(0)) pruning at every call (docs/alg/candidates/C3.md).
API: solve(g) -> (win, strat, calls, pruned_total). Strategies: Zielonka's on the residual parts, psolC regions via
zlk on the region (verification aid; oracle extraction is pointless for a complete solver: ZP itself is the oracle, and
solving the region with ZP restricted to one edge per vertex is what zlk_strategy does more cheaply).
CLI: zp.py game.pg [out.sol] [--plain] (--plain: Zielonka without pruning, same code path, for call-count comparison)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, ne, zielonka
sys.setrecursionlimit(100000)


class ZP:
    def __init__(self, g, prune=True):
        self.g = g; self.prune = prune
        self.succ = [sorted(set(s)) for s in g.succ]
        self.pred = [[] for _ in range(g.n)]
        for v in range(g.n):
            for w in self.succ[v]:
                self.pred[w].append(v)
        self.calls = 0; self.pruned = 0; self.psolc_decisions = 0
        self.strat = {}

    def attr(self, alive, target, p, strat=None):
        return zielonka.attractor(self.g, alive, target, p, strat)

    def psolc(self, alive):
        """psolC on the subgame alive: returns (D0, D1, residual)."""
        A = sorted(alive); idx = {v: i for i, v in enumerate(A)}
        succ = [[idx[w] for w in self.succ[v] if w in alive] for v in A]
        st = ne.Stats()
        win, dec = ne.ne(len(A), [self.g.prio[v] for v in A], [self.g.owner[v] for v in A], succ, 0, st)
        D = [set(), set()]
        for i, v in enumerate(A):
            if win[i] is not None:
                D[win[i]].add(v)
        self.psolc_decisions += len(dec)
        return D[0], D[1], alive - D[0] - D[1]

    def solve_sub(self, alive):
        self.calls += 1
        if not alive:
            return set(), set()
        if self.prune:
            D0, D1, R = self.psolc(alive)
            self.pruned += len(D0) + len(D1)
        else:
            D0, D1, R = set(), set(), set(alive)
        if not R:
            return D0, D1
        g = self.g
        d = max(g.prio[v] for v in R); p = d % 2; q = 1 - p
        top = {v for v in R if g.prio[v] == d}
        sA = {}
        T = self.attr(R, top, p, sA)
        W = self.solve_sub(R - T)
        if not W[q]:
            self.strat.update(sA)
            for v in top:
                if g.owner[v] == p:
                    self.strat[v] = next(w for w in self.succ[v] if w in R)
            res = [None, None]; res[p] = set(R); res[q] = set()
        else:
            sB = {}
            B = self.attr(R, W[q], q, sB)
            self.strat.update(sB)
            W2 = self.solve_sub(R - B)
            res = [None, None]; res[p] = W2[p]; res[q] = W2[q] | B
        return D0 | res[0], D1 | res[1]

    def run(self):
        W0, W1 = self.solve_sub(set(range(self.g.n)))
        win = [0 if v in W0 else 1 for v in range(self.g.n)]
        return win


def solve(g, prune=True, strat=True):
    z = ZP(g, prune)
    win = z.run()
    st = [None] * g.n
    if strat:
        for p in (0, 1):
            D = {v for v in range(g.n) if win[v] == p}
            if D:
                sd = ne.zlk_strategy(g, D, p)
                for v, w in sd.items():
                    st[v] = w
    return win, st, z.calls, z.pruned


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    g = pg.read(args[0])
    win, st, calls, pruned = solve(g, prune="--plain" not in sys.argv)
    print(f"ZP: {calls} recursive calls, {pruned} vertices pruned by psolC", file=sys.stderr)
    text = f"paritysol {g.n};\n" + "".join(f"{v} {w}{'' if st[v] is None else ' ' + str(st[v])};\n" for v, w in enumerate(win))
    if len(args) > 1:
        open(args[1], "w").write(text)
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
