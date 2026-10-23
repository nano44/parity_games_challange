"""N8d second independent implementation (L-COMP, 2026-10-23): Koh-Loho strategy iteration with tree labels over the
perfect (n, d/2)-universal tree, single-switch pivot rules R1 / R2 of docs/new/N8d-single.md §0.

Written from two sources only: arXiv 2108.13338v5 (Koh, Loho, "Beyond Value Iteration for Parity Games: Strategy
Iteration with Universal Trees", LMCS version, e-print sha256 7189eb2f...5c816c) and N8d-single.md §0 (frozen 03:21Z).
Paper references below are to v5: §2 prelim.tex, §3 strategy-iteration.tex, §4 label-setting.tex.

Paper map
- Algorithm 1 (§3, StrategyIteration)          -> run()
- admissible arc (§3: violated arc vw, v in V1)   -> admissible()
- violated / tight / loose (§2.2)               -> viol(), tighten(); loose = non-violated and mu(v) > Tighten
- Tighten (§2.2 frame), lift (§2.2), drop (§3.1) -> tighten(), lift in lfp(), drop in dijkstra()
- base nodes B(G_tau) (§3.1 Def.)               -> base_nodes()
- Algorithm 2 Dijkstra (§4), Phi_p, Phi^nu       -> dijkstra()
- Algorithm 3 LabelSetting (§4.1)               -> lfp()
- pivot R1 / R2 (N8d §0)                        -> pivot_r1(), pivot_r2()

My choices where the paper and §0 are silent (C1-C5; recorded in README.md):
C1 priorities: input is max-parity with priorities p >= 0 (TARGET.md); the paper needs pi : V -> [d] = {1..d}, d even.
   I use pi'(v) = p(v) + 2 (parity and order kept), d = smallest even number >= max pi'. The component xi_1 is then
   never read by any truncation (every pi' >= 2) and stays 0; components xi_3 .. xi_{d-1} correspond to the input's
   odd priorities 1 .. d-3. Unused priorities are kept (no compression; D2 change 1).
C2 ell = n (number of nodes of the game given to the run); M = {0, .., n-1} (§2.1, perfect universal tree).
C3 initial strategy tau_1: every Odd node takes its FIRST successor in the input file order (option --tau1 min: smallest id).
C4 dual game: owners swapped, priorities p + 1; Odd's strategy and region are read from the dual run's Even side.
C5 Even's strategy from the final mu (feasible in G, Thm 3.1): a non-violated arc to a successor with the least label
   (ties: smallest id). Odd's strategy: the same in the dual.
"""
import argparse
import heapq
import os
import random
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg  # noqa: E402

TOP = None


def tarjan(nodes, succ):
    """SCCs in completion order (a sink SCC first). succ(v) yields successors inside the node set."""
    index, low, onst, st, out = {}, {}, set(), [], []
    c = 0
    for root in nodes:
        if root in index:
            continue
        index[root] = low[root] = c; c += 1; st.append(root); onst.add(root)
        work = [(root, iter(succ(root)))]
        while work:
            v, it = work[-1]
            pushed = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = c; c += 1; st.append(w); onst.add(w)
                    work.append((w, iter(succ(w)))); pushed = True
                    break
                if w in onst and index[w] < low[v]:
                    low[v] = index[w]
            if pushed:
                continue
            work.pop()
            if work:
                u = work[-1][0]
                if low[v] < low[u]:
                    low[u] = low[v]
            if low[v] == index[v]:
                comp = []
                while True:
                    w = st.pop(); onst.discard(w); comp.append(w)
                    if w == v:
                        break
                out.append(comp)
    return out


class KL:
    def __init__(self, prio, owner, succ, tau1="first"):
        self.n = n = len(prio)
        self.owner = owner
        self.succ = [list(dict.fromkeys(s)) for s in succ]           # duplicate arcs dropped, file order kept
        self.pi = [p + 2 for p in prio]                               # C1
        mx = max(self.pi)
        self.d = mx if mx % 2 == 0 else mx + 1
        self.h = self.d // 2                                          # tree height d/2
        self.ell = n                                                  # C2
        # K[p] = number of leading components kept by the p-truncation: indices >= p+1 (p even) or >= p (p odd);
        # position j of a label holds xi_{2h-1-2j}.
        self.K = [0] * (self.d + 1)
        for p in range(1, self.d + 1):
            self.K[p] = self.h - p // 2 if p % 2 == 0 else self.h - (p - 1) // 2
        self.zeros = [(0,) * k for k in range(self.h + 1)]
        self.pred = [[] for _ in range(n)]
        for v in range(n):
            for w in self.succ[v]:
                self.pred[w].append(v)
        self.odd_nodes = [v for v in range(n) if owner[v] == 1]
        if tau1 == "first":
            self.tau = {v: self.succ[v][0] for v in self.odd_nodes}  # C3
        else:
            self.tau = {v: min(self.succ[v]) for v in self.odd_nodes}

    # ---- labels (§2.2). A label is a tuple of h ints in 0..ell-1, or TOP.
    def viol(self, mu, v, w):
        lv, lw = mu[v], mu[w]
        if lv is TOP:
            return False
        if lw is TOP:
            return True
        p = self.pi[v]; k = self.K[p]
        if p % 2 == 0:
            return lv[:k] < lw[:k]
        return lv[:k] <= lw[:k]

    def tighten(self, mu, v, w):
        """Tighten(mu, vw): the least xi in L(T) u {TOP} with vw not violated when mu(v) = xi."""
        lw = mu[w]
        if lw is TOP:
            return TOP
        p = self.pi[v]; k = self.K[p]
        if p % 2 == 0:
            return lw[:k] + self.zeros[self.h - k]
        t = list(lw[:k]); j = k - 1
        while j >= 0:
            t[j] += 1
            if t[j] < self.ell:
                break
            t[j] = 0
            j -= 1
        if j < 0:
            return TOP
        return tuple(t) + self.zeros[self.h - k]

    @staticmethod
    def le(a, b):
        return b is TOP or (a is not TOP and a <= b)

    def gsucc(self, v, tau):
        return self.succ[v] if self.owner[v] == 0 else [tau[v]]

    # ---- B(G_tau) (§3.1): v is a base node iff pi(v) even and v lies on a cycle of G_tau with top priority pi(v).
    def base_nodes(self, tau):
        B = set()
        evens = sorted({p for p in self.pi if p % 2 == 0})
        for p in evens:
            nodes = [v for v in range(self.n) if self.pi[v] <= p]
            ok = set(nodes)
            sc = lambda v: [w for w in self.gsucc(v, tau) if w in ok]
            for comp in tarjan(nodes, sc):
                cands = [v for v in comp if self.pi[v] == p]
                if not cands:
                    continue
                if len(comp) > 1:
                    B.update(cands)
                else:
                    v = comp[0]
                    if v in self.gsucc(v, tau):
                        B.add(v)
        return B

    # ---- Algorithm 2 (§4): Dijkstra for ordered trees.
    def dijkstra(self, tau, nu, B):
        n, d, h = self.n, self.d, self.h
        S = set(B)
        nu = [nu[v] if v in S else TOP for v in range(n)]
        hsucc = [[] if v in S else self.gsucc(v, tau) for v in range(n)]   # H = G_tau minus out-arcs of B
        hpred = [[] for _ in range(n)]
        for v in range(n):
            for w in hsucc[v]:
                hpred[w].append(v)
        # Phi_p for even p in [d]: topological numbering of the SCCs of H_p (sink SCC = 1), 0 iff pi(v) > p.
        phi = {}
        for p in range(2, d + 1, 2):
            nodes = [v for v in range(n) if self.pi[v] <= p]
            ok = set(nodes)
            f = [0] * n
            for i, comp in enumerate(tarjan(nodes, lambda v: [w for w in hsucc[v] if w in ok]), 1):
                for v in comp:
                    f[v] = i
            phi[p] = f
        phis = [phi[2 * h - 2 * j] for j in range(h)]   # Phi_d, Phi_{d-2}, .., Phi_2 aligned with xi_{d-1}, .., xi_1

        def key(v):
            l = nu[v]
            if l is TOP:
                return (1,)
            k = [0]
            for j in range(h):
                k.append(phis[j][v]); k.append(l[j])
            return tuple(k)

        def drop(v, u):   # drop(nu, vu) = min(nu(v), Tighten(nu, vu))
            t = self.tighten(nu, v, u)
            if self.le(t, nu[v]) and t != nu[v]:
                nu[v] = t
                return True
            return False

        for u in S:
            for v in hpred[u]:
                if v not in S:
                    drop(v, u)
        heap = [(key(v), v) for v in range(n) if v not in S]
        heapq.heapify(heap)
        while heap:
            kk, u = heapq.heappop(heap)
            if u in S or kk != key(u):
                continue
            S.add(u)
            for v in hpred[u]:
                if v not in S and drop(v, u):
                    heapq.heappush(heap, (key(v), v))
        return nu

    # ---- Algorithm 3 (§4.1): mu^{G_tau up} for the perfect tree (line 3 kept, applied in node-id order).
    def lfp(self, tau, mu):
        B = self.base_nodes(tau)
        nu = list(mu)
        for v in sorted(B):
            best = TOP
            for w in self.gsucc(v, tau):
                l = nu[v] if not self.viol(nu, v, w) else self.tighten(nu, v, w)
                if self.le(l, best):
                    best = l
            nu[v] = best
        return self.dijkstra(tau, nu, B)

    def admissible(self, mu):
        """{v: [w, ..]} for Odd nodes v with a violated arc vw (§3)."""
        out = {}
        for v in self.odd_nodes:
            ws = [w for w in self.succ[v] if self.viol(mu, v, w)]
            if ws:
                out[v] = ws
        return out

    def best_arc(self, mu, v, ws):
        """Largest Tighten(mu, vw) among admissible arcs (TOP largest); ties: smallest successor id (§0)."""
        best, bw = None, None
        for w in sorted(ws):
            t = self.tighten(mu, v, w)
            if bw is None or not self.le(t, best):
                best, bw = t, w
        return bw

    # ---- Algorithm 1 (§3).
    def run(self, rule="r1", seed=1, cap=10 ** 7, check=False):
        tau = dict(self.tau)
        mu = [self.zeros[self.h]] * self.n                   # line 2: min L(T)
        mu = self.lfp(tau, mu)                                # line 3
        if check:
            self.check_inv(tau, mu, None)
        rng = random.Random(seed) if rule == "r2" else None   # fresh generator per Algorithm 1 run (§0)
        piv = 0
        while True:
            adm = self.admissible(mu)                         # line 4
            if not adm:
                break
            if piv >= cap:
                raise RuntimeError(f"pivot cap {cap} reached")
            if rule == "r1":
                v = min(adm)
            else:
                v = rng.choice(sorted(adm))
            tau[v] = self.best_arc(mu, v, adm[v])             # line 5: one admissible arc
            old = mu
            mu = self.lfp(tau, mu)                            # line 6
            piv += 1
            if check:
                self.check_inv(tau, mu, old)
        return piv, tau, mu

    # ---- debug: invariants of Algorithm 1 and a naive least-fixed-point oracle (small games).
    def check_inv(self, tau, mu, old):
        for v in range(self.n):
            if old is not None and not self.le(old[v], mu[v]):
                raise AssertionError(f"mu decreased at {v}")
            gs = self.gsucc(v, tau)
            if mu[v] is not TOP and self.owner[v] == 0 and all(self.viol(mu, v, w) for w in gs):
                raise AssertionError(f"infeasible at Even {v}")
            if self.owner[v] == 1 and self.viol(mu, v, tau[v]):
                raise AssertionError(f"tau arc violated at {v}")
            for w in gs:
                if not self.viol(mu, v, w) and not self.le(mu[v], self.tighten(mu, v, w)):
                    raise AssertionError(f"loose arc {v}->{w}")
        if old is not None:
            nv = self.naive_lfp(tau, old)
            if nv != mu:
                raise AssertionError("label-setting differs from naive lifting")

    def naive_lfp(self, tau, mu):
        mu = list(mu)
        changed = True
        while changed:
            changed = False
            for v in range(self.n):
                if self.owner[v] == 0:
                    best = TOP
                    for w in self.succ[v]:
                        l = mu[v] if not self.viol(mu, v, w) else self.tighten(mu, v, w)
                        if self.le(l, best):
                            best = l
                else:
                    w = tau[v]
                    best = mu[v] if not self.viol(mu, v, w) else self.tighten(mu, v, w)
                if best != mu[v]:
                    mu[v] = best; changed = True
        return mu

    def even_strategy(self, mu):
        st = {}
        for v in range(self.n):
            if self.owner[v] == 0 and mu[v] is not TOP:
                cands = [w for w in self.succ[v] if not self.viol(mu, v, w)]
                st[v] = min(cands, key=lambda w: (mu[w], w))       # C5 (mu[w] finite here)
        return st


def solve(g, rule="r1", seed=1, tau1="first", check=False, cap=10 ** 7):
    """Primal and dual runs. Returns winner list, strategy list, pivots primal, pivots dual."""
    P = KL(g.prio, g.owner, g.succ, tau1)
    pp, _, mu = P.run(rule, seed, cap, check)
    D = KL([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ, tau1)     # C4
    pd, _, mud = D.run(rule, seed, cap, check)
    win = [0 if mu[v] is not TOP else 1 for v in range(g.n)]
    windual = [1 if mud[v] is not TOP else 0 for v in range(g.n)]
    if win != windual:
        raise AssertionError("primal and dual regions disagree")
    strat = [None] * g.n
    for v, w in P.even_strategy(mu).items():
        strat[v] = w
    for v, w in D.even_strategy(mud).items():
        strat[v] = w
    return win, strat, pp, pd


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("game")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--rule", choices=["r1", "r2"], default="r1")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--tau1", choices=["first", "min"], default="first")
    ap.add_argument("--check", action="store_true", help="assert Algorithm 1 invariants and compare with naive lifting")
    a = ap.parse_args()
    g = pg.read(a.game)
    t0 = time.time()
    win, strat, pp, pd = solve(g, a.rule, a.seed, a.tau1, a.check)
    dt = time.time() - t0
    if a.out:
        pg.write_sol(win, a.out, strat)
    else:
        sys.stdout.write(f"paritysol {g.n};\n" + "".join(
            f"{v} {win[v]}{'' if strat[v] is None else ' ' + str(strat[v])};\n" for v in range(g.n)))
    sys.stderr.write(f"pivots_primal {pp} pivots_dual {pd} time {dt:.3f}\n")


if __name__ == "__main__":
    main()
