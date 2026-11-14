#!/usr/bin/env python3
"""N12 engine (L-NEW, 2026-11-14): settle-and-recurse on the parity-induced mean-payoff game.

Core: ReduceGame of P. Ohlmann, "A symmetric recursive algorithm for mean-payoff games", arXiv 2603.07555v1, Section 5
Algorithm 1, with Section 6.1 (initial F), 6.2 (fix many vertices at once), 6.4 (remembered potentials), 6.5 (lazy; flag only).
Lane additions (docs/new/N12-proposal.md): (R) the test Reduced is Section 2's definition on EVERY vertex (the pseudocode's test on
N and P only is unsound; flag --literal reproduces it); (P) reduced-trap peeling at every call; (D) side choice by a work-balanced
dovetail of the two sides at every call (policy duet), or a fixed policy.

Game: Even = Max, Odd = Min; every edge leaving v has weight (-1)^p * (n+1)^p, p = compressed priority of v (order and parity
preserved).  Exact Python integers; maxbits records the largest bit length of a potential.

Output: winning regions and positional strategies (paritysol with --sol).  Counters: calls (ReduceGame invocations, abandoned
dovetail branches included), settles, rounds (potential reductions), cuts, peels, depth, work (vertex + edge visits), maxbits.

usage: n12.py [--no61] [--no62] [--no64] [--nopeel] [--lazy] [--literal] [--policy duet|small|large|sup|inf|Sbig|Ssmall|Hbig|Hsmall|top|topx|flipK] [--sol FILE] game.pg
"""
import sys

sys.setrecursionlimit(1000000)


def read_pg(path):
    owner, pr, succ = {}, {}, {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('parity') or line.startswith('start'):
                continue
            parts = line.rstrip(';').split()
            v = int(parts[0]); pr[v] = int(parts[1]); owner[v] = int(parts[2])
            succ[v] = [int(x) for x in parts[3].split(',')]
    ids = sorted(owner)
    idx = {v: i for i, v in enumerate(ids)}
    return len(ids), [owner[v] for v in ids], [pr[v] for v in ids], [sorted(set(idx[u] for u in succ[v])) for v in ids], ids


def compress(pr):
    """order- and parity-preserving compression to the least priorities (TARGET.md section 1)."""
    out, cur = {}, -1
    for p in sorted(set(pr)):
        cur += 1
        if cur % 2 != p % 2:
            cur += 1
        out[p] = cur
    return [out[p] for p in pr]


class Stats:
    def __init__(self):
        self.calls = 0; self.settles = 0; self.rounds = 0; self.cuts = 0; self.depth = 0; self.work = 0; self.maxbits = 0
        self.settled_vertices = 0; self.peels = 0


class Solver:
    def __init__(self, n, owner, pr, succ, opt61=True, opt62=True, opt64=True, peel=True, policy='duet', lazy=False,
                 literal=False):
        self.n = n; self.owner = owner; self.succ = succ
        self.pred = [[] for _ in range(n)]
        for v in range(n):
            for u in succ[v]:
                self.pred[u].append(v)
        self.cpr = compress(pr)
        B = n + 1
        self.w0 = [(B ** p) if p % 2 == 0 else -(B ** p) for p in self.cpr]
        self.wbits = max(abs(x).bit_length() for x in self.w0)
        self.opt61 = opt61; self.opt62 = opt62; self.opt64 = opt64; self.peel = peel
        self.policy = policy; self.lazy = lazy; self.literal = literal
        self.st = Stats()

    # ---------- zones and the reduced test (Section 2 definitions; real frame, Min = Odd = owner 1) ----------
    def zones(self, X, phi):
        owner, succ, w0, st = self.owner, self.succ, self.w0, self.st
        N, P = set(), set()
        zero = {}
        for v in X:
            base = w0[v] - phi[v]
            neg = pos = False; allneg = allpos = True; zs = []
            for u in succ[v]:
                if u in X:
                    w = base + phi[u]
                    if w < 0: neg = True; allpos = False
                    elif w > 0: pos = True; allneg = False
                    else: allneg = allpos = False; zs.append(u)
            st.work += 1 + len(succ[v])
            if owner[v] == 1:
                if neg: N.add(v)
                elif allpos: P.add(v)
                else: zero[v] = zs
            else:
                if pos: P.add(v)
                elif allneg: N.add(v)
                else: zero[v] = zs
        # ZN: Min can force a < 0 edge before a > 0 one = Min-attractor of N inside Z along weight-0 edges
        ZN = set(N)
        cnt = {v: len(zs) for v, zs in zero.items() if owner[v] == 0}
        zpred = {}
        for v, zs in zero.items():
            for u in zs:
                zpred.setdefault(u, []).append(v)
        Q = list(N)
        while Q:
            u = Q.pop()
            for v in zpred.get(u, ()):
                if v in ZN: continue
                if owner[v] == 1:
                    ZN.add(v); Q.append(v)
                else:
                    cnt[v] -= 1
                    if cnt[v] == 0:
                        ZN.add(v); Q.append(v)
        return N, P, ZN, X - ZN

    def reduced(self, X, phi, N, P, ZN, ZP):
        """Section 2: a vertex of ZN is reduced if Min can force to immediately see a <= 0 edge towards ZN (dually for ZP).
        self.literal: the pseudocode's Reduced (Section 5), which tests N and P only."""
        owner, succ, w0, literal = self.owner, self.succ, self.w0, self.literal
        for v in (N if literal else ZN):
            base = w0[v] - phi[v]
            if owner[v] == 1:
                if not any((u in ZN) and base + phi[u] <= 0 for u in succ[v] if u in X): return False
            else:
                if not all((u in ZN) and (literal or base + phi[u] <= 0) for u in succ[v] if u in X): return False
        for v in (P if literal else ZP):
            base = w0[v] - phi[v]
            if owner[v] == 0:
                if not any((u in ZP) and base + phi[u] >= 0 for u in succ[v] if u in X): return False
            else:
                if not all((u in ZP) and (literal or base + phi[u] >= 0) for u in succ[v] if u in X): return False
        return True

    # ---------- main recursion (generators: every `yield` is a scheduling point for the dovetail) ----------
    def reduce(self, X, phi, depth=0):
        """X: set of vertices (a sinkless subgame); phi: dict, absolute potential on X.
        Returns (minus, plus, phi') with G[X] reduced under phi'; minus = ZN (Odd wins), plus = ZP (Even wins)."""
        st = self.st
        st.calls += 1
        if depth > st.depth: st.depth = depth
        while True:
            N, P, ZN, ZP = self.zones(X, phi)
            if self.reduced(X, phi, N, P, ZN, ZP):
                return ZN, ZP, phi
            if self.peel:
                for s, Zs in ((1, ZP), (-1, ZN)):
                    if not Zs: continue
                    R = self.reduced_trap(X, phi, s, Zs)
                    if R:
                        st.peels += 1
                        res = yield from self.cut_and_glue(X, phi, s, R, {v: 0 for v in R}, depth)
                        return res[1], res[2], res[3]
            pol = self.policy
            if pol == 'duet':
                res = yield from self.duet(X, phi, N, P, depth)
            else:
                if pol.startswith('flip'):      # adversarial probes: Sbig with the choice flipped at depth < K (flipK) 
                    a = self.init_sizes(X, phi, 1, N); b = self.init_sizes(X, phi, -1, P)
                    s = 1 if a[0] >= b[0] else -1
                    if depth < int(pol[4:]): s = -s
                elif pol in ('top', 'topx'):    # side by the parity of the largest priority present in X
                    pmax = max(self.cpr[v] for v in X)
                    s = 1 if pmax % 2 == 1 else -1
                    if pol == 'topx': s = -s
                elif pol in ('Sbig', 'Ssmall', 'Hsmall', 'Hbig'):
                    a = self.init_sizes(X, phi, 1, N); b = self.init_sizes(X, phi, -1, P)
                    k = 0 if pol[0] == 'S' else 1
                    if pol in ('Sbig', 'Hbig'): s = 1 if a[k] >= b[k] else -1
                    else: s = 1 if a[k] <= b[k] else -1
                elif pol == 'small': s = 1 if len(N) <= len(P) else -1
                elif pol == 'large': s = 1 if len(N) >= len(P) else -1
                elif pol == 'sup': s = 1
                else: s = -1
                res = yield from self.settle(X, phi, s, N if s == 1 else P, depth)
            if res[0] == 'tail':
                phi = res[1]
                st.rounds += 1
                continue
            return res[1], res[2], res[3]

    def init_sizes(self, X, phi, s, eN):
        """(|F0|, |H0|): size of the initial F of side s (Section 6.1) and of H after the first BacktrackAllPaths."""
        owner, succ, pred, w0, st = self.owner, self.succ, self.pred, self.w0, self.st
        emin_owner = 1 if s == 1 else 0
        def ew(v, u):
            return s * (w0[v] + phi[u] - phi[v])
        A = set()
        for v in X:
            if v in eN: continue
            ws = [ew(v, u) for u in succ[v] if u in X]
            st.work += 1 + len(succ[v])
            if owner[v] != emin_owner:
                if any(w > 0 for w in ws): A.add(v)
            elif all(w > 0 for w in ws): A.add(v)
        cnt = {}
        Q = list(A)
        while Q:
            u = Q.pop()
            for v in pred[u]:
                if v not in X or v in A or v in eN: continue
                if owner[v] != emin_owner:
                    A.add(v); Q.append(v)
                elif ew(v, u) == 0:
                    if v not in cnt:
                        cnt[v] = sum(1 for x in succ[v] if x in X and ew(v, x) == 0)
                    cnt[v] -= 1
                    if cnt[v] == 0:
                        A.add(v); Q.append(v)
        F0 = len(X) - len(A)
        # backtrack: vertices of A all of whose successors are settled
        H = set(A); esc = {}; Q = []
        for v in A:
            c = sum(1 for u in succ[v] if u in H)
            esc[v] = c
            if c == 0: Q.append(v)
        while Q:
            v = Q.pop()
            if v not in H: continue
            H.discard(v)
            for x in pred[v]:
                if x in H:
                    esc[x] -= 1
                    if esc[x] == 0: Q.append(x)
        return F0, len(H)

    def duet(self, X, phi, N, P, depth):
        """run the sup side (s = +1) and the inf side (s = -1) in lockstep, balanced by work; the first to finish wins."""
        st = self.st
        g = [self.settle(X, phi, 1, N, depth), self.settle(X, phi, -1, P, depth)]
        w = [0, 0]
        while True:
            i = 0 if w[0] <= w[1] else 1
            before = st.work
            try:
                next(g[i])
            except StopIteration as e:
                g[1 - i].close()
                return e.value
            w[i] += st.work - before
            yield

    def reduced_trap(self, X, phi, s, Zs):
        """largest R inside Zs (ZP if s = 1, ZN if s = -1) such that every eMax vertex of R has an edge of effective weight >= 0
        into R and every eMin vertex of R has all its edges (inside X) of effective weight >= 0 and into R: a dominion of eMax."""
        owner, succ, pred, w0, st = self.owner, self.succ, self.pred, self.w0, self.st
        emin_owner = 1 if s == 1 else 0
        R = set(Zs)
        cnt = {}
        Q = []
        for v in Zs:
            base = w0[v] - phi[v]
            st.work += 1 + len(succ[v])
            if owner[v] == emin_owner:
                if any((u not in R) or s * (base + phi[u]) < 0 for u in succ[v] if u in X):
                    Q.append(v)
            else:
                c = sum(1 for u in succ[v] if u in R and s * (base + phi[u]) >= 0)
                cnt[v] = c
                if c == 0: Q.append(v)
        for v in Q: R.discard(v)
        while Q:
            u = Q.pop()
            for v in pred[u]:
                if v not in R: continue
                if owner[v] == emin_owner:
                    R.discard(v); Q.append(v)
                elif s * (w0[v] - phi[v] + phi[u]) >= 0:
                    cnt[v] -= 1
                    if cnt[v] == 0:
                        R.discard(v); Q.append(v)
        return R

    def cut_and_glue(self, X, phi, s, T, ephiT, depth):
        """T: a trap for eMin, positively reduced (effective frame) by phi + s * ephiT.  Attract for eMax (AttractMaxAndReduce),
        recurse on the rest, glue the potentials (Lemma 4)."""
        owner, succ, pred, w0, st = self.owner, self.succ, self.pred, self.w0, self.st
        emin_owner = 1 if s == 1 else 0

        def ew(v, u):
            return s * (w0[v] + phi[u] - phi[v])

        A = set(T)
        ephiA = dict(ephiT)
        cntm = {}
        Q = list(T)
        while Q:
            u = Q.pop()
            for v in pred[u]:
                if v not in X or v in A: continue
                st.work += 1
                if owner[v] != emin_owner:
                    ephiA[v] = max(ew(v, x) + ephiA[x] for x in succ[v] if x in A)
                    A.add(v); Q.append(v)
                else:
                    if v not in cntm:
                        cntm[v] = sum(1 for x in succ[v] if x in X)
                    cntm[v] -= 1
                    if cntm[v] == 0:
                        ephiA[v] = min(ew(v, x) + ephiA[x] for x in succ[v] if x in X)
                        A.add(v); Q.append(v)
        Gp = X - A
        if Gp:
            yield
            Gm2, Gp2, phi2 = yield from self.reduce(Gp, {v: phi[v] for v in Gp}, depth + 1)
            delta = None
            for v in Gp:
                e2 = s * (phi2[v] - phi[v])
                for u in succ[v]:
                    if u in A:
                        d = -ew(v, u) - ephiA[u] + e2
                        if delta is None or d > delta: delta = d
            if delta is None: delta = 0
        else:
            Gm2, Gp2, phi2, delta = set(), set(), {}, 0
        newphi = dict(phi2)
        for v in A:
            newphi[v] = phi[v] + s * (ephiA[v] + delta)
        self.note_bits(newphi)
        if s == 1:
            return ('done', Gm2, Gp2 | A, newphi)
        return ('done', Gm2 | A, Gp2, newphi)

    def note_bits(self, phi):
        st = self.st
        mb = max((abs(x).bit_length() for x in phi.values()), default=0)
        if mb > st.maxbits: st.maxbits = mb

    def settle(self, X, phi, s, eN, depth):
        """one computation of supSigma_N (s = +1) or infSigma_P (s = -1, the same code in the effective frame)."""
        owner, succ, pred, w0, st = self.owner, self.succ, self.pred, self.w0, self.st
        emin_owner = 1 if s == 1 else 0

        def ew(v, u):
            return s * (w0[v] + phi[u] - phi[v])

        # --- initial F: Section 6.1 (vertices from which eMin reaches eN before any > 0 edge) or eN ---
        if self.opt61:
            A = set()
            for v in X:          # effective P: eMax with some > 0 edge, eMin with all edges > 0
                if v in eN: continue
                ws = [ew(v, u) for u in succ[v] if u in X]
                st.work += 1 + len(succ[v])
                if owner[v] != emin_owner:
                    if any(w > 0 for w in ws): A.add(v)
                else:
                    if all(w > 0 for w in ws): A.add(v)
            cnt = {}
            Q = list(A)
            while Q:
                u = Q.pop()
                for v in pred[u]:
                    if v not in X or v in A or v in eN: continue
                    st.work += 1
                    if owner[v] != emin_owner:
                        A.add(v); Q.append(v)
                    elif ew(v, u) == 0:
                        if v not in cnt:
                            cnt[v] = sum(1 for x in succ[v] if x in X and ew(v, x) == 0)
                        cnt[v] -= 1
                        if cnt[v] == 0:
                            A.add(v); Q.append(v)
            F = X - A
        else:
            F = set(eN)
        sup = {v: 0 for v in F}
        phipred = None

        def lazy_exit():
            for v in eN:
                neg = False; allneg = True
                for u in succ[v]:
                    if u in X:
                        if ew(v, u) + sup.get(u, 0) - sup.get(v, 0) < 0: neg = True
                        else: allneg = False
                if owner[v] == emin_owner:
                    if not neg: return True
                elif not allneg: return True
            return False

        first = True
        while True:
            if self.lazy and not first and lazy_exit():
                return ('tail', {v: phi[v] + s * sup.get(v, 0) for v in X})
            first = False
            # --- BacktrackAllPaths ---
            esc = {}
            Q = []
            for v in X:
                if v in F: continue
                c = 0
                for u in succ[v]:
                    if u in X and u not in F: c += 1
                st.work += 1 + len(succ[v])
                esc[v] = c
                if c == 0: Q.append(v)
            while Q:
                v = Q.pop()
                vals = [ew(v, u) + sup[u] for u in succ[v] if u in X]
                val = min(vals) if owner[v] == emin_owner else max(vals)
                assert val >= 0, 'supSigma < 0 in backtracking'
                sup[v] = val; F.add(v)
                for x in pred[v]:
                    if x in X and x not in F:
                        esc[x] -= 1
                        if esc[x] == 0: Q.append(x)
            H = X - F
            if not H:
                newphi = {v: phi[v] + s * sup[v] for v in X}
                self.note_bits(newphi)
                return ('tail', newphi)
            yield
            # --- recursive call on H (Section 6.4: start from the previous potential of H) ---
            if self.opt64 and phipred is not None:
                start = {v: phipred[v] for v in H}
            else:
                start = {v: phi[v] for v in H}
            Hm, Hp, phiH = yield from self.reduce(H, start, depth + 1)
            phipred = phiH
            eHp = Hp if s == 1 else Hm
            if eHp:
                # case a: escapes of eMin from eH+ to F (Lemma 5a / 8a)
                m = None; arg = None
                for v in eHp:
                    if owner[v] != emin_owner: continue
                    eph = s * (phiH[v] - phi[v])
                    for u in succ[v]:
                        if u in F:
                            val = ew(v, u) + sup[u] - eph
                            if m is None or val < m:
                                m = val; arg = (v, u)
                if arg is None:
                    st.cuts += 1
                    res = yield from self.cut_and_glue(X, phi, s, eHp, {v: s * (phiH[v] - phi[v]) for v in eHp}, depth)
                    return res
                R, case_a = eHp, True
            else:
                # case b: eH+ empty, eH- = H nonempty: best escape of eMax from H to F (Lemma 5b / 8b)
                m = None; arg = None
                for v in H:
                    if owner[v] == emin_owner: continue
                    eph = s * (phiH[v] - phi[v])
                    for u in succ[v]:
                        if u in F:
                            val = ew(v, u) + sup[u] - eph
                            if m is None or val > m:
                                m = val; arg = (v, u)
                assert arg is not None, 'Lemma 5b: no eMax escape from H- to F'
                R, case_a = H, False
            st.settles += 1
            if self.opt62:
                S = self.good_set(X, phi, s, F, sup, R, phiH, m, case_a)
                assert arg[0] in S
                for v in S:
                    sup[v] = m + s * (phiH[v] - phi[v])
                    assert sup[v] >= 0
                F |= S
                st.settled_vertices += len(S)
            else:
                v, u = arg
                sup[v] = ew(v, u) + sup[u]
                assert sup[v] >= 0
                F.add(v)
                st.settled_vertices += 1

    def good_set(self, X, phi, s, F, sup, R, phiH, m, case_a):
        """Lemma 8.  R = eH+ (case a) or eH- (case b).  Good escape: an edge v -> u, v in R, u in F, with
        ew(v, u) + sup[u] - ephiH(v) <= m (a) / >= m (b).  S: the vertices of R from which the escaping player (eMin in a, eMax in b)
        can force a good escape before any edge of phiH-modified weight > 0 (a) / < 0 (b) or any edge leaving R otherwise."""
        owner, succ, w0, st = self.owner, self.succ, self.w0, self.st
        emin_owner = 1 if s == 1 else 0
        mover = emin_owner if case_a else 1 - emin_owner
        S = set()
        cnt = {}
        Q = []
        okin = {}
        for v in R:
            eph = s * (phiH[v] - phi[v])
            hasgood = False; bad = False; ins = []
            for u in succ[v]:
                if u not in X: continue
                if u in F:
                    val = s * (w0[v] + phi[u] - phi[v]) + sup[u] - eph
                    if (val <= m) if case_a else (val >= m): hasgood = True
                    else: bad = True
                elif u in R:
                    wm = s * (w0[v] + phiH[u] - phiH[v])
                    if (wm <= 0) if case_a else (wm >= 0): ins.append(u)
                    else: bad = True
                else:
                    bad = True
            st.work += 1 + len(succ[v])
            okin[v] = ins
            if owner[v] == mover:
                if hasgood: S.add(v); Q.append(v)
            elif bad:
                cnt[v] = -1
            else:
                cnt[v] = len(ins)
                if cnt[v] == 0:
                    S.add(v); Q.append(v)
        ipred = {}
        for v, ins in okin.items():
            for u in ins:
                ipred.setdefault(u, []).append(v)
        while Q:
            u = Q.pop()
            for v in ipred.get(u, ()):
                if v in S: continue
                if owner[v] == mover:
                    S.add(v); Q.append(v)
                elif cnt[v] > 0:
                    cnt[v] -= 1
                    if cnt[v] == 0:
                        S.add(v); Q.append(v)
        return S

    # ---------- top level ----------
    def solve(self):
        n = self.n
        X = set(range(n))
        g = self.reduce(X, {v: 0 for v in X})
        while True:
            try:
                next(g)
            except StopIteration as e:
                minus, plus, phi = e.value
                break
        self.phi = phi
        if not self.literal:
            N, P, ZN, ZP = self.zones(X, phi)
            assert self.reduced(X, phi, N, P, ZN, ZP), 'final potential is not reducing'
            assert ZN == minus and ZP == plus, 'zones differ from returned regions'
        strat = [-1] * n
        for v in range(n):
            base = self.w0[v] - phi[v]
            if self.owner[v] == 0 and v in plus:
                c = [u for u in self.succ[v] if u in plus and base + phi[u] >= 0]
                strat[v] = min(c) if c else -1
            elif self.owner[v] == 1 and v in minus:
                c = [u for u in self.succ[v] if u in minus and base + phi[u] <= 0]
                strat[v] = min(c) if c else -1
        return plus, minus, strat


def main():
    args = sys.argv[1:]
    kw = {}
    sol = None; path = None
    i = 0
    while i < len(args):
        a = args[i]
        if a == '--no61': kw['opt61'] = False
        elif a == '--no62': kw['opt62'] = False
        elif a == '--no64': kw['opt64'] = False
        elif a == '--nopeel': kw['peel'] = False
        elif a == '--lazy': kw['lazy'] = True
        elif a == '--literal': kw['literal'] = True
        elif a == '--policy': i += 1; kw['policy'] = args[i]
        elif a == '--sol': i += 1; sol = args[i]
        else: path = a
        i += 1
    n, owner, pr, succ, ids = read_pg(path)
    S = Solver(n, owner, pr, succ, **kw)
    plus, minus, strat = S.solve()
    st = S.st
    m = sum(len(x) for x in succ)
    print('n %d m %d d %d calls %d settles %d settled %d rounds %d cuts %d peels %d depth %d work %d maxbits %d wbits %d WE %d' % (
        n, m, len(set(pr)), st.calls, st.settles, st.settled_vertices, st.rounds, st.cuts, st.peels, st.depth, st.work, st.maxbits,
        S.wbits, len(plus)))
    if sol:
        with open(sol, 'w') as f:
            f.write('paritysol %d;\n' % (max(ids)))
            for v in range(n):
                win = 0 if v in plus else 1
                if strat[v] >= 0:
                    f.write('%d %d %d;\n' % (ids[v], win, ids[strat[v]]))
                else:
                    f.write('%d %d;\n' % (ids[v], win))


if __name__ == '__main__':
    main()
