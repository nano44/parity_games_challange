#!/usr/bin/env python3
"""N5 SSI-GLOBAL, second independent implementation (L-COMP, gauntlet step 2; Lead 2026-10-18 20:51Z).

Written from the TEXT ONLY: docs/new/N5-ssi-global.md on claude/l-new @ 8925171 ("Exact pseudocode" section).
experiments/new/n5.py and L-SI's engine (experiments/si/) were NOT opened. The Voege-Jurdziński (VJ00) valuations and
Odd's optimal counterstrategy come from L-COMP's own port of PGSolver's evaluate_strategy
(experiments/hard-families/pgsolver_si.py, class SI; REFEREE-checked, and identical to the PGSolver d3cd624 binary in
iteration counts and solutions: experiments/hard-families/pgsolver-binary-diff.md).

Readings of the spec (each an ambiguity, reported; see README.md "Ambiguities"):
 A1 injective rank: ties between equal priorities broken by vertex index (VJ order on (priority, index), as PGSolver).
 A2 "best-reward start": PGSolver's initial_strategy_by_best_reward (successor of maximal reward; ties by the reward
    order on (priority, index)); for Odd the same on the dual game.
 A3 dual game: owners swapped, priorities + 1, same vertex ids and successor order.
 A4 Iσ = {(v,w): v Even, Ξσ(w) strictly better for Even than Ξσ(σ(v))}; Iτ likewise on the dual.
 A5 "optimal strategy" in a restricted arena = PGSolver's optimal counterstrategy (per vertex, the successor of best
    valuation for its owner; ties broken by vertex index as in PGSolver's best/nvto). The spec does not fix ties.
 A6 Step 3 uses the OLD σ (the spec: "Odd's optimal counterstrategy to σ"; σ' is not yet assigned in step 5's sense).
 A7 Fallback "classical switch-all step": every Even vertex with an improving edge switches to its best successor under
    Ξσ (PGSolver switch-all, ties by index); for Odd the same on the dual.
 A8 Iteration count = number of passes through steps 2-5 (the final pass that finds Iσ = Iτ = ∅ is not counted);
    fallback count = number of passes that took step 4.
 A9 Output: regions from Ξσ at termination (winner = parity of the cycle vertex), Even's strategy σ on its region,
    Odd's strategy = its optimal counterstrategy σ̄ to σ on its region.
Usage: n5b.py GAME.pg [OUT.sol] [--start FILE] [--mode orig|spec]   (FILE: lines 'SIGMA0 v:w ...' and 'TAU0 v:w ...', as dlm_gen.py prints)
Prints 'n5b iterations K fallbacks F evals E'."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "hard-families")); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg
from pgsolver_si import SI

sys.setrecursionlimit(1000000)
EVEN, ODD = 0, 1


def dual(g, succ=None):
    return pg.Game([p + 1 for p in g.prio], [1 - o for o in g.owner], succ if succ is not None else g.succ)


def restrict(g, allowed):
    """Same game with succ(v) := allowed[v] where allowed[v] is not None."""
    return pg.Game(g.prio, g.owner, [sorted(set(allowed[v])) if allowed[v] is not None else g.succ[v] for v in range(g.n)])


class SpecSI(SI):
    """SPEC mode (docs/new/N5-ssi-global.md SPEC S1 @ l-new c66ce20): same VJ valuations as SI.evaluate, plus Odd's choice
    taken from inside the procedure: (iv) longest path: first strict maximum over successors in increasing index; shortest
    path: BFS from the cycle node over predecessors in increasing index, first discovery sets the choice; (v) the cycle node,
    if Odd: the first successor (increasing index) through which the cycle-detecting DFS returns to it."""

    def evaluate_choice(self, strat):
        n = self.g.n
        gs = {i: set(self.succ[i]) if strat[i] == -1 else {strat[i]} for i in range(n)}
        gp = {i: set() for i in range(n)}
        for i in range(n):
            for j in gs[i]:
                gp[j].add(i)
        asc = sorted(range(n), key=lambda x: (self.reward(EVEN, self.pr[x]), x if self.reward(EVEN, self.pr[x]) % 2 == 0 else -x))
        valu = [(-1, frozenset(), 0)] * n
        choice = [-1] * n
        for v in asc:
            if valu[v][0] != -1 or v not in gs:
                continue
            seen = set()

            def process(u):
                if u in seen:
                    return False
                seen.add(u)
                for w in sorted(gs[u]):
                    if self.rel(w, v) <= 0 and (v in gs[w] or process(w)):
                        return True
                return False
            # (i) cycle-node test and (v) FIX 2 (l-new 6014db7): explicit-stack DFS from v over Gσ, successors scanned in
            # increasing index, each unvisited alive y of rank < rank(v) marked and pushed when scanned, last pushed popped
            # first; the scan stops at the first successor equal to v; choice = first vertex after v on the tree path.
            cyc = None
            stack, vis, parent, found = [v], {v}, {}, None
            while stack and found is None:
                x = stack.pop()
                for y in sorted(gs[x]):
                    if y == v:
                        found = x; break
                    if y not in vis and y in gs and self.rel(y, v) < 0:
                        vis.add(y); parent[y] = x; stack.append(y)
            if found is not None:
                cyc = found
                while cyc != v and parent.get(cyc) != v:
                    cyc = parent[cyc]
                if found == v:
                    cyc = v
            if cyc is None:
                continue
            nodes, st = set(), [v]
            while st:
                w = st.pop()
                if w in nodes:
                    continue
                nodes.add(w); st.extend(gp[w])
            hs = {w: {u for u in gs[w] if u in nodes} for w in nodes}
            hp = {w: {u for u in gp[w] if u in nodes} for w in nodes}
            paths = {u: set() for u in nodes}

            def del_other_edges(x, m):
                for y in list(hs[x]):
                    if y not in m:
                        hs[x].discard(y); hp[y].discard(x)

            def reach(start, excl):
                s_, st2 = set(), [start]
                while st2:
                    x = st2.pop()
                    if x in s_:
                        continue
                    s_.add(x); st2.extend(y for y in hp[x] if y != excl)
                return s_
            for u in sorted(nodes, key=lambda x: (self.pr[x], x), reverse=True):
                if self.rel(u, v) > 0:
                    if self.pr[u] % 2 == 0:
                        m = reach(v, u)
                        for q in nodes:
                            if q not in m:
                                paths[q].add(u)
                        del_other_edges(u, m)
                        for q in m:
                            del_other_edges(q, m)
                    else:
                        m = reach(u, v)
                        for q in m:
                            paths[q].add(u)
                        for x in m:
                            if x != u:
                                del_other_edges(x, m)
            dist = {v: 0}
            if self.pr[v] % 2 == 0:                      # longest path, first strict maximum in successor order
                cache = {v: 0}

                def get_dist(x):
                    if x in cache:
                        return cache[x]
                    best, bw = None, -1
                    for y in sorted(hs[x]):
                        dy = get_dist(y)
                        if best is None or dy > best:
                            best, bw = dy, y
                    cache[x] = 1 + best; choice[x] = bw
                    return cache[x]
                for x in nodes:
                    dist[x] = get_dist(x)
            else:                                        # BFS over predecessors, first discovery sets the choice
                from collections import deque
                q = deque([v]); disc = {v}
                while q:
                    y = q.popleft()
                    for x in sorted(hp[y]):
                        if x not in disc:
                            disc.add(x); dist[x] = dist[y] + 1; choice[x] = y; q.append(x)
            choice[v] = cyc
            for u in nodes:
                valu[u] = (v, frozenset(paths[u]), dist.get(u, 0))
            for u in nodes:
                for y in gs.pop(u):
                    if y in gp: gp[y].discard(u)
                for y in gp.pop(u):
                    if y in gs: gs[y].discard(u)
        choice = [choice[v] if self.pl[v] == ODD else -1 for v in range(n)]
        return valu, choice


MODE = "orig"   # "orig": my readings A1-A9 (Odd's optimum by best(): (valuation, index)); "spec": SPEC S1 choices


class RepeatedState(Exception):
    pass


class N5:
    def __init__(self, g, mode=None):
        self.mode = mode or MODE
        self.g, self.d = g, dual(g)
        self.SG, self.SD = SpecSI(self.g), SpecSI(self.d)
        self.evals = 0

    def ev(self, si, strat):
        self.evals += 1
        return si.evaluate(strat)

    @staticmethod
    def improving(si, strat, valu):
        """A4: for each vertex of si's Even player, the set of strictly improving successors."""
        I = {}
        for v in range(si.g.n):
            if strat[v] == -1:
                continue
            ws = [w for w in si.succ[v] if si.nvo(valu[strat[v]], valu[w]) < 0]
            if ws:
                I[v] = ws
        return I

    def opt(self, si, strat):
        """Odd's optimal counterstrategy to strat in si's game, and the valuations."""
        self.evals += 1
        if self.mode == "spec":
            return si.evaluate_choice(strat)
        valu = si.evaluate(strat)
        return valu, [si.best(valu, v) if si.pl[v] == ODD else -1 for v in range(si.g.n)]

    @staticmethod
    def counter(si, valu):
        """Optimal counterstrategy of si's Odd player (A5)."""
        return [si.best(valu, v) if si.pl[v] == ODD else -1 for v in range(si.g.n)]

    def run(self, sigma=None, tau=None, max_iter=100000, trace=None, fbtrace=None):
        g = self.g
        sigma = sigma or self.SG.initial_strategy_by_best_reward()                  # Even vertices: successor, Odd: -1
        tau = tau or self.SD.initial_strategy_by_best_reward()                      # on the dual: original Odd vertices
        it = fb = 0
        seen_states = set()                      # Lead 21:34Z: a repeated (σ, τ) state = INCOMPLETE run
        while True:
            key = (tuple(sigma), tuple(tau))          # exact, no hash collisions
            if key in seen_states:
                raise RepeatedState(f"(sigma, tau) repeated at iteration {it}")
            seen_states.add(key)
            if trace is not None:                    # box 3 hook (2026-10-24): record every state; no effect on the run
                trace.append(key)
            vs = self.ev(self.SG, sigma); vt = self.ev(self.SD, tau)
            Is, It = self.improving(self.SG, sigma, vs), self.improving(self.SD, tau, vt)
            if not Is and not It:                                                    # step 1
                break
            it += 1
            if it > max_iter:
                raise RuntimeError("iteration cap")
            # step 2: Even's optimum against fixed τ, Even restricted to A_σ, via Odd's counterstrategy on the dual arena
            allow = [None] * g.n
            for v in range(g.n):
                if g.owner[v] == EVEN:
                    allow[v] = [sigma[v]] + Is.get(v, [])
                else:
                    allow[v] = [tau[v]]
            d2 = dual(restrict(g, allow)); s2 = SpecSI(d2)
            _, c2 = self.opt(s2, [tau[v] if g.owner[v] == ODD else -1 for v in range(g.n)])
            sigma2 = [c2[v] if g.owner[v] == EVEN else -1 for v in range(g.n)]
            # step 3: Odd's optimum against σ (A6: old σ), Odd restricted to A_τ
            allow = [None] * g.n
            for v in range(g.n):
                if g.owner[v] == ODD:
                    allow[v] = [tau[v]] + It.get(v, [])
            s3 = SpecSI(restrict(g, allow))
            _, c3 = self.opt(s3, sigma)
            tau2 = [c3[v] if g.owner[v] == ODD else -1 for v in range(g.n)]
            # step 4: fallback
            isfb = sigma2 == sigma and tau2 == tau
            if fbtrace is not None:                  # box 12 hook (2026-10-26): fallback flag per transition; no effect on the run
                fbtrace.append(int(isfb))
            if isfb:
                fb += 1
                if Is:
                    sigma2 = list(sigma)
                    for v in Is:
                        sigma2[v] = self.SG.best(vs, v)
                else:
                    tau2 = list(tau)
                    for v in It:
                        tau2[v] = self.SD.best(vt, v)
            sigma, tau = sigma2, tau2                                                 # step 5
        win = [g.prio[vs[v][0]] % 2 for v in range(g.n)]                             # A9 / S5
        _, sbar = self.opt(self.SG, sigma)
        strat = [sigma[v] if g.owner[v] == EVEN else sbar[v] for v in range(g.n)]
        strat = [strat[v] if win[v] == g.owner[v] else None for v in range(g.n)]
        return win, strat, it, fb


def read_start(path, g):
    sigma = [-1] * g.n; tau = [-1] * g.n
    for line in open(path):
        parts = line.split()
        if parts and parts[0] in ("SIGMA0", "TAU0"):
            tgt = sigma if parts[0] == "SIGMA0" else tau
            for p in parts[1:]:
                a, b = map(int, p.split(":")); tgt[a] = b
    return sigma, tau


def main():
    global MODE
    if "--mode" in sys.argv:
        MODE = sys.argv[sys.argv.index("--mode") + 1]
    a = [x for x in sys.argv[1:] if not x.startswith("--") and x != MODE]
    start = sys.argv[sys.argv.index("--start") + 1] if "--start" in sys.argv else None
    a = [x for x in a if x != start]
    g = pg.read(a[0])
    s = N5(g)
    sigma, tau = read_start(start, g) if start else (None, None)
    win, strat, it, fb = s.run(sigma, tau)
    if len(a) > 1:
        pg.write_sol(win, a[1], strat)
    print(f"n5b iterations {it} fallbacks {fb} evals {s.evals}")


if __name__ == "__main__":
    main()
