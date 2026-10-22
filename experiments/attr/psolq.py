#!/usr/bin/env python3
"""psolQ, the partial solver of Huth, Kuo, Piterman, "Fatal Attractors in Parity Games: Building Blocks for Partial
Solvers", arXiv 1405.0386v2, Figure 5 (archiv.tex:970-997) with Definition 6 (tex:942-948). Line labels Q1-Q7, L1-L2,
P1-P2, S in notes/L-ATTR.md "psolQ pseudocode". Definition fixed in docs/attr/A1-statement.md D3.

Input/output max-parity (TARGET.md, Oink, PGSolver format). Internally MIN-parity as in HKP (tex:366-367):
colour c(v) = M - pr(v), M = max pr rounded up to even (order reversed, parity kept; same map as experiments/m2/avh.py).

Usage: psolq.py game.pg [solution.sol] [--partial] [--trace]
Writes 'paritysol' with winner and a positional strategy for every vertex the solver decides. Vertices psolQ leaves
undecided: without --partial the run prints 'UNDECIDED k of n' and exits 3 (so compare.py reports 'error', like avh.py's
STUCK); with --partial their lines are omitted. Python API: PsolQ(g).run() -> (win, strat, residual, decisions)."""
import sys, os
from collections import deque
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg


class PsolQ:
    def __init__(self, g, trace=False):
        self.g, self.trace = g, trace
        P = max(g.prio)
        M = P if P % 2 == 0 else P + 1
        self.c = [M - p for p in g.prio]                 # HKP colours (min-parity)
        self.succ = [sorted(set(s)) for s in g.succ]
        self.pred = [[] for _ in range(g.n)]
        for v in range(g.n):
            for w in self.succ[v]:
                self.pred[w].append(v)
        self.win = [None] * g.n
        self.strat = [None] * g.n
        self.decisions = []                               # (b, player, |W|, |Attr(W)|)
        self.stats = dict(layered=0, pmattr=0, decisions=0)

    # Def. 1 (tex:407-418): standard attractor of player p to X inside the subgame `alive`; X included.
    def attr(self, alive, X, p, st=None):
        A = set(X) & alive
        cnt, q = {}, deque(A)
        while q:
            w = q.popleft()
            for v in self.pred[w]:
                if v not in alive or v in A:
                    continue
                if self.g.owner[v] == p:
                    A.add(v); q.append(v)
                    if st is not None:
                        st[v] = w
                else:
                    if v not in cnt:
                        cnt[v] = sum(1 for x in self.succ[v] if x in alive)
                    cnt[v] -= 1
                    if cnt[v] == 0:
                        A.add(v); q.append(v)
        return A

    # P1-P2 (Def. 6): PMAttr_p(T, d) = mu Z. PMpred_p(Z, T, d) inside `alive`; the target T is external (tex:532-535):
    # a node of T is in the result only if attracted to T in >= 1 move. Eligible nodes: c(v) >= d or v in T.
    # wit records, for p's nodes, the successor in Z u T that witnessed the entry (first entry kept: S in the notebook).
    def pmattr(self, alive, T, d, p, wit):
        self.stats["pmattr"] += 1
        Z = set()
        pushed = set(T)
        cnt, q = {}, deque(T)
        while q:
            w = q.popleft()
            for v in self.pred[w]:
                if v not in alive or v in Z:
                    continue
                if not (self.c[v] >= d or v in T):
                    continue
                if self.g.owner[v] == p:
                    Z.add(v)
                    if v not in wit:
                        wit[v] = w
                else:
                    if v not in cnt:
                        cnt[v] = sum(1 for x in self.succ[v] if x in alive)   # every w in Z u T is popped exactly once
                    cnt[v] -= 1
                    if cnt[v] > 0:
                        continue
                    Z.add(v)
                if v not in pushed:
                    pushed.add(v); q.append(v)
        return Z

    # L1-L2 (Fig. 5, tex:970-977). Pre-condition: all nodes of X have parity p.
    def layered_attr(self, alive, p, X, wit):
        self.stats["layered"] += 1
        A = set()
        b = max(self.c[v] for v in X)
        d = p
        while d <= b:
            Y = {v for v in X if self.c[v] <= d}
            A = self.pmattr(alive, A | Y, d, p, wit)
            d += 2
        return A

    # Q1-Q7 (Fig. 5, tex:985-997). The recursion "return psolQ(G \ Attr(W))" is the restart of the colour loop.
    def run(self):
        alive = set(range(self.g.n))
        restart = True
        while restart and alive:
            restart = False
            for b in sorted({self.c[v] for v in alive}):                        # Q1 (D3a: colours of the current G)
                p = b % 2
                X = {v for v in alive if self.c[v] <= b and self.c[v] % 2 == p}  # Q2
                cache = set()
                while X and X != cache:                                           # Q3
                    cache = X
                    wit = {}
                    W = self.layered_attr(alive, p, X, wit)                       # Q4
                    if X <= W:                                                    # Q5: fatal (Def. 7)
                        st = {}
                        D = self.attr(alive, W, p, st)
                        for v in D:
                            self.win[v] = p
                            if self.g.owner[v] == p:
                                self.strat[v] = wit[v] if v in W else st[v]      # S
                        self.decisions.append((b, p, len(W), len(D)))
                        self.stats["decisions"] += 1
                        if self.trace:
                            print(f"b={b} player {p}: fatal layered attractor |W|={len(W)}, removed |Attr(W)|={len(D)}", file=sys.stderr)
                        alive = alive - D
                        restart = True
                        break
                    X = X & W                                                     # Q6
                if restart:
                    break
        return self.win, self.strat, alive, self.decisions                        # Q7: alive = residual game


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    g = pg.read(args[0])
    s = PsolQ(g, trace="--trace" in sys.argv)
    win, strat, residual, _ = s.run()
    print(f"solved with {s.stats['decisions']} decisions, {s.stats['layered']} layered attractors, "
          f"{s.stats['pmattr']} permissive attractors.", file=sys.stderr)
    if residual and "--partial" not in sys.argv:
        print(f"UNDECIDED {len(residual)} of {g.n}: {sorted(residual)}", file=sys.stderr)
        sys.exit(3)
    lines = [f"paritysol {g.n};\n"] + [f"{v} {win[v]}{'' if strat[v] is None else ' ' + str(strat[v])};\n"
                                       for v in range(g.n) if win[v] is not None]
    if len(args) > 1:
        open(args[1], "w").write("".join(lines))
    else:
        sys.stdout.write("".join(lines))


if __name__ == "__main__":
    main()
