#!/usr/bin/env python3
"""PROVISIONAL implementation of Algorithm 1 of arXiv 2511.03752v1 (R. van der Heijden, "Attractors Is All You Need:
Parity Games In Polynomial Time"), following notes/L-COMP.md "M2 pseudocode" (tex:N = line in the paper's main.tex).
Not yet checked for faithfulness by the REFEREE.

Usage: avh.py game.pg [solution.sol] [--trace]
Input/output in max-parity (TARGET.md, Oink). Internally min-parity as in the paper (tex:274): rho = M - prio, M even.
Output: 'paritysol' with winner and a positional strategy for every vertex owned by its winner (strategy
construction S1/S2 is ours, see notes). Exit code 3 and message STUCK if Lemma 4's claim fails (no progress)."""
import sys, os
from collections import deque
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg

EVEN, ODD = 0, 1


class Stuck(Exception):
    pass


class Solver:
    def __init__(self, g, trace=False):
        self.g, self.trace = g, trace
        P = max(g.prio)
        M = P if P % 2 == 0 else P + 1
        self.rho = [M - p for p in g.prio]           # min-parity priorities (AM1 mapping)
        self.succ = [list(set(s)) for s in g.succ]   # mutable edge sets (P1 deletes self-loops)
        self.pred = [[] for _ in range(g.n)]
        for v in range(g.n):
            for w in self.succ[v]:
                self.pred[w].append(v)
        self.win = [None] * g.n
        self.strat = [None] * g.n
        self.stats = dict(iterations=0, A_calls=0, attractors=0, inner_iters=0)

    # Attr (tex:280-286) in the subgame `alive`; records attracting successors of player's vertices in `st`.
    def attr(self, alive, target, player, st=None):
        self.stats["attractors"] += 1
        A = set(target) & alive
        cnt = {}
        q = deque(A)
        while q:
            w = q.popleft()
            for v in self.pred[w]:
                if v not in alive or v in A:
                    continue
                if self.g.owner[v] == player:
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

    def U(self, alive, d):  # D1, tex:303
        return {v for v in alive if self.rho[v] <= d and self.rho[v] % 2 == d % 2}

    def Astar(self, alive, d):  # D2, tex:304
        O = d % 2
        res = set()
        for k in range(0, d + 1):
            if k % 2 == O:
                continue
            Uk1 = self.U(alive, k - 1) if k >= 1 else set()
            if not Uk1:
                continue
            at = self.attr(alive, Uk1, O)
            res |= {v for v in at if self.rho[v] == k}
        return res

    def Aprime(self, alive, d, A, Ast, Ud):  # D3, tex:309
        O = d % 2
        base = {v for v in A - (Ast | Ud) if self.rho[v] < d}
        return self.attr(alive, base, 1 - O)

    def A(self, alive, d):
        """D4 (tex:312-318). Returns (A, U, attractor strategy dict for O)."""
        self.stats["A_calls"] += 1
        O = d % 2
        Ud = self.U(alive, d)
        Ast = self.Astar(alive, d)
        Uk = set(Ud)
        while True:
            self.stats["inner_iters"] += 1
            st = {}
            Ak = self.attr(alive, Uk, O, st)
            Ap = self.Aprime(alive, d, Ak, Ast, Ud)
            rem = self.attr(alive, (alive - Ak) | Ap, 1 - O)
            Unext = Uk - rem
            if Unext == Uk:
                return Ak, Uk, st, Ap
            Uk = Unext

    def assign(self, alive, Aset, Uset, st, Ap, O, tag):
        """Record winner O on Aset and our strategy S1/S2 (notes, 'Strategies')."""
        for v in Aset:
            self.win[v] = O
            if self.g.owner[v] != O:
                continue
            if v in st:                                   # S1: attractor strategy
                self.strat[v] = st[v]; continue
            succ_in = [w for w in self.succ[v] if w in alive]
            c1 = [w for w in succ_in if w in Uset]
            c2 = [w for w in succ_in if w in Aset and w not in Ap]
            c3 = [w for w in succ_in if w in Aset]
            if c1:
                self.strat[v] = c1[0]
            elif c2:
                self.strat[v] = c2[0]
            elif c3:
                self.strat[v] = c3[0]
                if self.trace:
                    print(f"[{tag}] S2 fallback at v{v}", file=sys.stderr)
            else:
                self.strat[v] = None  # cannot happen if Aset is O-closed; verifier will flag it

    def preroutine(self, alive):
        """P1-P2 (notes): self-loop removal following PGSolver (Friedmann)."""
        g = self.g
        for v in list(alive):                             # P1: useless self-loops
            if v in self.succ[v] and self.rho[v] % 2 != g.owner[v] and len(self.succ[v]) > 1:
                self.succ[v].remove(v); self.pred[v].remove(v)
        for p in (EVEN, ODD):                             # P2: useful / forced self-loops
            S = {v for v in alive if v in self.succ[v] and self.rho[v] % 2 == p
                 and (g.owner[v] == p or len(self.succ[v]) == 1)}
            if not S:
                continue
            st = {}
            X = self.attr(alive, S, p, st)
            for v in X:
                self.win[v] = p
                if g.owner[v] == p:
                    self.strat[v] = v if v in S else st[v]
            alive -= X
        assert not any(v in self.succ[v] for v in alive)
        return alive

    def solve(self):
        alive = set(range(self.g.n))
        alive = self.preroutine(alive)
        while alive:                                       # tex:377
            self.stats["iterations"] += 1
            dhat = max(self.rho[v] for v in alive)        # tex:378
            O = dhat % 2                                   # tex:379 (AM2)
            opp = [self.rho[v] for v in alive if self.rho[v] % 2 != O]
            removed = False
            if opp:                                        # AM3: no O-bar priority -> A(G,dbar) = {}
                dbar = max(opp)                            # tex:380
                A, Us, st, Ap = self.A(alive, dbar)        # tex:382
                if A:
                    self.assign(alive, A, Us, st, Ap, 1 - O, f"it{self.stats['iterations']} dbar={dbar}")
                    alive = alive - A                      # tex:383-384
                    removed = True
                    if self.trace:
                        print(f"it{self.stats['iterations']}: A(G,{dbar}) -> player {1-O}: {len(A)} vertices", file=sys.stderr)
                    continue                               # tex:385-387
            A, Us, st, Ap = self.A(alive, dhat)            # tex:389
            if A:
                self.assign(alive, A, Us, st, Ap, O, f"it{self.stats['iterations']} dhat={dhat}")
                alive = alive - A                          # tex:390-391
                removed = True
                if self.trace:
                    print(f"it{self.stats['iterations']}: A(G,{dhat}) -> player {O}: {len(A)} vertices", file=sys.stderr)
            if not removed:
                raise Stuck(f"no progress with {len(alive)} vertices left (dhat={dhat})")
        return self.win, self.strat


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    g = pg.read(args[0])
    s = Solver(g, trace="--trace" in sys.argv)
    try:
        win, strat = s.solve()
    except Stuck as e:
        print(f"STUCK: {e}", file=sys.stderr)
        sys.exit(3)
    print(f"solved with {s.stats['iterations']} iterations, {s.stats['A_calls']} A-calls, "
          f"{s.stats['inner_iters']} inner iterations, {s.stats['attractors']} attractors.", file=sys.stderr)
    if len(args) > 1:
        pg.write_sol(win, args[1], strat)
    else:
        sys.stdout.write(f"paritysol {g.n};\n" + "".join(
            f"{v} {w}{'' if strat[v] is None else ' ' + str(strat[v])};\n" for v, w in enumerate(win)))


if __name__ == "__main__":
    main()
