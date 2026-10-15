#!/usr/bin/env python3
"""psolB and psol, the partial solvers of Huth, Kuo, Piterman, arXiv 1405.0386v2, Figure 3 (archiv.tex:728-747) and
Figure 2 (archiv.tex:666-682), with the monotone attractor of Definition 3 (tex:506-521). Same conventions as psolq.py
(max-parity in/out, HKP min-parity colours inside, witness strategies, verify.py checks the output).
API: PsolB(g).run() / Psol(g).run() -> (win, strat, residual, decisions).  CLI as psolq.py."""
import sys, os
from collections import deque
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from psolq import PsolQ, pg


class PsolB(PsolQ):
    # Def. 3: MAttr_p(X, c) = mu Z. Mpred_p(Z, X, c): nodes of colour >= c attracted to X in >= 1 move; X external.
    # This is PMAttr with the permissive clause dropped; X's own nodes of colour >= c are eligible like any other.
    def mattr(self, alive, X, c, p, wit):
        self.stats["pmattr"] += 1
        Z, pushed, cnt, q = set(), set(X), {}, deque(X)
        while q:
            w = q.popleft()
            for v in self.pred[w]:
                if v not in alive or v in Z or self.c[v] < c:
                    continue
                if self.g.owner[v] == p:
                    Z.add(v)
                    if v not in wit:
                        wit[v] = w
                else:
                    if v not in cnt:
                        cnt[v] = sum(1 for x in self.succ[v] if x in alive)
                    cnt[v] -= 1
                    if cnt[v] > 0:
                        continue
                    Z.add(v)
                if v not in pushed:
                    pushed.add(v); q.append(v)
        return Z

    def run(self):  # Fig. 3 (tex:731-744): colours d descending; X = nodes of colour d; gfp; fatal -> remove Attr(MAttr(X)).
        alive = set(range(self.g.n))
        restart = True
        while restart and alive:
            restart = False
            for d in sorted({self.c[v] for v in alive}, reverse=True):
                p = d % 2
                X = {v for v in alive if self.c[v] == d}
                cache = set()
                while X and X != cache:
                    cache = X
                    wit = {}
                    W = self.mattr(alive, X, d, p, wit)
                    if X <= W:
                        st = {}
                        D = self.attr(alive, W, p, st)
                        for v in D:
                            self.win[v] = p
                            if self.g.owner[v] == p:
                                self.strat[v] = wit[v] if v in W else st[v]
                        self.decisions.append((d, p, len(W), len(D)))
                        self.stats["decisions"] += 1
                        alive = alive - D
                        restart = True
                        break
                    X = X & W
                if restart:
                    break
        return self.win, self.strat, alive, self.decisions


class Psol(PsolQ):
    def run(self):  # Fig. 2 (tex:669-677): nodes k in descending colour order; fatal singleton, or edge removal (Lemma 1).
        alive = set(range(self.g.n))
        succ = {v: set(self.succ[v]) for v in range(self.g.n)}       # psol modifies E
        restart = True
        while restart and alive:
            restart = False
            for k in sorted(alive, key=lambda v: (-self.c[v], v)):
                c, p = self.c[k], self.c[k] % 2
                wit = {}
                self.succ = [sorted(succ[v]) for v in range(self.g.n)]
                self.pred = [[] for _ in range(self.g.n)]
                for v in range(self.g.n):
                    for w in self.succ[v]:
                        self.pred[w].append(v)
                W = PsolB.mattr(self, alive, {k}, c, p, wit)
                if k in W:
                    st = {}
                    D = self.attr(alive, W, p, st)
                    for v in D:
                        self.win[v] = p
                        if self.g.owner[v] == p:
                            self.strat[v] = wit[v] if v in W else st[v]
                    self.decisions.append((c, p, len(W), len(D)))
                    self.stats["decisions"] += 1
                    alive = alive - D
                    restart = True
                    break
                rem = {w for w in succ[k] if w in W}
                if rem and len(succ[k] & alive) > len(rem):
                    succ[k] -= rem
                elif rem:
                    pass  # cannot remove every edge of k (the game would lose a successor); HKP's Lemma 1 assumes the owner has another move
        return self.win, self.strat, alive, self.decisions


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    g = pg.read(args[0])
    s = (Psol if "--psol" in sys.argv else PsolB)(g)
    win, strat, residual, _ = s.run()
    print(f"solved with {s.stats['decisions']} decisions.", file=sys.stderr)
    if residual and "--partial" not in sys.argv:
        print(f"UNDECIDED {len(residual)} of {g.n}: {sorted(residual)}", file=sys.stderr)
        sys.exit(3)
    sys.stdout.write(f"paritysol {g.n};\n" + "".join(f"{v} {win[v]}{'' if strat[v] is None else ' ' + str(strat[v])};\n"
                                                   for v in range(g.n) if win[v] is not None))
