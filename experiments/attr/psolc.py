#!/usr/bin/env python3
"""psolC, the partial solver of Huth, Kuo, Piterman, "Static analysis of parity games: alternating reachability under
parity", Imperial College DTR 2015/4 (DTR15-4.pdf, sha256 a7b61fe3...9cd6; LNCS 9560 pp. 159-177), Figure 5 (p.9) with
Wr_p(G, X) computed on the game graph G^p_X of Definition 2 (p.5) by Theorem 1 (p.6). Line map: docs/attr/psolC-impl.md.

Conventions: input/output max-parity (TARGET.md, PGSolver format); inside, DTR's MIN-parity colours c = M - pr with M = max pr
rounded up to even (order reversed, parity kept; same map as psolq.py/avh.py). Player 0 = Even, player 1 = Odd.
psolC gives winning regions only; its strategies need memory (DTR Thm 3). Positional strategies for every decided vertex
(TARGET section 5, D2 change 5) are produced by solving the decided subgame with the harness Zielonka (`strat="zlk"`),
or with Oink (`strat="oink"`), or not at all (`strat=None`); this is a verification aid, not part of psolC.

Usage: psolc.py game.pg [solution.sol] [--partial] [--trace] [--oink] [--no-strat]
Exit 3 'UNDECIDED k of n' if the residual game is non-empty and --partial is not given.
API: PsolC(g).run() -> (win, strat, residual, decisions); decisions = list of (player, |gfp X|, |Attr|)."""
import sys, os, subprocess, tempfile
from collections import deque
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, zielonka

BOT = None  # the colour record "bottom" of Definition 2


class PsolC:
    def __init__(self, g, trace=False, strat="zlk", exclude_start=False):
        self.g, self.trace, self.strat_mode = g, trace, strat
        self.exclude_start = exclude_start   # variant A1 (docs/attr/psolC-impl.md): minimum without c(v_0); NOT DTR Def. 1
        P = max(g.prio)
        M = P if P % 2 == 0 else P + 1
        self.c = [M - p for p in g.prio]                       # DTR colours (min-parity)
        self.succ = [sorted(set(s)) for s in g.succ]
        self.pred = [[] for _ in range(g.n)]
        for v in range(g.n):
            for w in self.succ[v]:
                self.pred[w].append(v)
        self.win = [None] * g.n
        self.strat = [None] * g.n
        self.decisions = []
        self.stats = dict(wr=0, fixpoints=0, decisions=0, product_nodes=0)

    # Standard attractor of player p to X in the subgame `alive` (DTR p.4: Attr_p[G, X]); X included.
    def attr(self, alive, X, p):
        A = set(X) & alive
        cnt, q = {}, deque(A)
        while q:
            w = q.popleft()
            for v in self.pred[w]:
                if v not in alive or v in A:
                    continue
                if self.g.owner[v] == p:
                    A.add(v); q.append(v)
                else:
                    if v not in cnt:
                        cnt[v] = sum(1 for x in self.succ[v] if x in alive)
                    cnt[v] -= 1
                    if cnt[v] == 0:
                        A.add(v); q.append(v)
        return A

    # Wr_p(G, X) ∩ X by Theorem 1 on G^p_X (Definition 2), restricted to the part of G^p_X reachable from X x {⊥}
    # (Fig. 5 caption). Nodes (v, l), l in C(G) ∪ {⊥}. Edges (1):
    #   ((v, ⊥), (v', min(c(v), c(v'))))  for (v, v') in E;
    #   ((v, l), (v', min(l, c(v'))))     for (v, v') in E, l in C(G), and (v not in X or l%2 != p).
    # Target Z = X x {l : l%2 = p}; W = {v : (v, ⊥) in Attr_p(G^p_X, Z)}. Returns W ∩ X (only X matters in Fig. 5).
    def wr_in_X(self, alive, X, p):
        self.stats["wr"] += 1
        g, c = self.g, self.c
        start = [(x, BOT) for x in X]
        nodes = set(start)
        out = {}
        q = deque(start)
        while q:                                                # forward closure from X x {⊥}
            v, l = q.popleft()
            if l is not BOT and v in X and l % 2 == p:
                out[(v, l)] = []                                # target: dead end in G^p_X
                continue
            succs = []
            for w in self.succ[v]:
                if w not in alive:
                    continue
                if l is BOT:
                    nl = c[w] if self.exclude_start else min(c[v], c[w])   # edge (1), first line: min(c(v), c(v'))
                else:
                    nl = min(l, c[w])                                         # edge (1), second line
                node = (w, nl)
                succs.append(node)
                if node not in nodes:
                    nodes.add(node); q.append(node)
            out[(v, l)] = succs
        self.stats["product_nodes"] += len(nodes)
        pred = {n: [] for n in nodes}
        for n, ss in out.items():
            for s in ss:
                pred[s].append(n)
        A = {n for n in nodes if n[1] is not BOT and n[0] in X and n[1] % 2 == p}   # Z ∩ reachable part
        cnt, q = {}, deque(A)
        while q:                                                # attractor of Z for player p in the reachable part
            w = q.popleft()
            for n in pred[w]:
                if n in A:
                    continue
                if g.owner[n[0]] == p:
                    A.add(n); q.append(n)
                else:
                    if n not in cnt:
                        cnt[n] = len(out[n])
                    cnt[n] -= 1
                    if cnt[n] == 0:
                        A.add(n); q.append(n)
        return {x for x in X if (x, BOT) in A}

    # fixedpoint(G, X, p) of Fig. 5: W = V; repeat { X = X ∩ W; W = X ∩ Wr_p(G, X) } until X ⊆ W; return X.
    def fixedpoint(self, alive, X, p):
        self.stats["fixpoints"] += 1
        X = set(X)
        while True:
            if not X:
                return X
            W = self.wr_in_X(alive, X, p)
            if self.trace:
                print(f"  fixedpoint p={p}: X={sorted(X)} -> X ∩ Wr={sorted(W)}", file=sys.stderr)
            if X <= W:
                return X
            X = X & W

    # tryPlayer(G, p) of Fig. 5: X = fixedpoint(G, {v : c(v)%2 = p}, p); return Attr_p[G, X] if X != {} else {}.
    def try_player(self, alive, p):
        X = self.fixedpoint(alive, {v for v in alive if self.c[v] % 2 == p}, p)
        if not X:
            return set(), set()
        return self.attr(alive, X, p), X

    # psolC(G) of Fig. 5: W = tryPlayer(G, 0); if W != {} recurse on G \ W; else W = tryPlayer(G, 1); if W != {} recurse;
    # else return G. The recursion is the restart of the loop below (player 0 tried first after every removal).
    def run(self):
        alive = set(range(self.g.n))
        while alive:
            removed = False
            for p in (0, 1):
                D, X = self.try_player(alive, p)
                if D:
                    for v in D:
                        self.win[v] = p
                    self.decisions.append((p, len(X), len(D)))
                    self.stats["decisions"] += 1
                    if self.trace:
                        print(f"player {p}: gfp X={sorted(X)}, removed Attr |{len(D)}|", file=sys.stderr)
                    if self.strat_mode:
                        self.positional_strategies(alive, D, p)
                    alive = alive - D
                    removed = True
                    break
            if not removed:
                break
        return self.win, self.strat, alive, self.decisions

    def positional_strategies(self, alive, D, p):
        """Verification aid (D2 change 5): a positional winning strategy for p on the decided region D, obtained by
        solving the subgame induced by D (within `alive`) with the harness Zielonka or with Oink. Asserts that the
        subgame solver agrees that p wins all of D (a soundness cross-check of the decision)."""
        Dl = sorted(D)
        idx = {v: i for i, v in enumerate(Dl)}
        succ = [[idx[w] for w in self.succ[v] if w in D] for v in Dl]
        assert all(succ), "decided region is not closed under its own edges"
        sub = pg.Game([self.g.prio[v] for v in Dl], [self.g.owner[v] for v in Dl], succ)
        if self.strat_mode == "oink":
            w, s = oink_solve(sub)
        else:
            w, s = zielonka.solve_with_strategy(sub)
        assert all(x == p for x in w), "subgame solver disagrees: decided region is not won entirely by its player"
        for i, v in enumerate(Dl):
            if self.g.owner[v] == p:
                self.strat[v] = Dl[s[i]]


def oink_solve(sub):
    oink = os.path.join(HERE, "..", "..", "tools", "oink", "build", "oink")
    with tempfile.TemporaryDirectory() as td:
        gp, sp = os.path.join(td, "g.pg"), os.path.join(td, "g.sol")
        pg.write(sub, gp)
        subprocess.run([oink, "--tl", "-w", "1", gp, sp], check=True, capture_output=True)
        text = open(sp).read()
    import verify
    return pg.read_sol(text, sub.n), verify.read_strategy(text, sub.n)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    g = pg.read(args[0])
    mode = None if "--no-strat" in sys.argv else ("oink" if "--oink" in sys.argv else "zlk")
    s = PsolC(g, trace="--trace" in sys.argv, strat=mode, exclude_start="--exclude-start" in sys.argv)
    win, strat, residual, _ = s.run()
    print(f"solved with {s.stats['decisions']} decisions, {s.stats['fixpoints']} fixpoints, {s.stats['wr']} Wr computations, "
          f"{s.stats['product_nodes']} product nodes.", file=sys.stderr)
    if residual and "--partial" not in sys.argv:
        print(f"UNDECIDED {len(residual)} of {g.n}: {sorted(residual)[:20]}", file=sys.stderr)
        sys.exit(3)
    lines = [f"paritysol {g.n};\n"] + [f"{v} {win[v]}{'' if strat[v] is None else ' ' + str(strat[v])};\n"
                                       for v in range(g.n) if win[v] is not None]
    if len(args) > 1:
        open(args[1], "w").write("".join(lines))
    else:
        sys.stdout.write("".join(lines))


if __name__ == "__main__":
    main()
