"""REFEREE successor 26: own VJ engine for the P-N5-XICYC review (no lane code imported).
Values (L, P, k): L cycle node, P frozenset of vertices on the path before L that are more relevant than L, k path length.
Relevance: (prio, index) (SPEC S1 rank); parity = prio % 2; reward(L) = +rel if even, -rel if odd (only the order matters).
Odd's optimal counterstrategy: local improvement for Odd in the one-player game (VJ local = global, R36 (c) P1 on G^d), then
optionally cross-checked by brute force over all Odd positional strategies (small games).
Game: prio list, owner list (0 Even, 1 Odd), succ list of lists."""
import itertools

class VJ:
    def __init__(self, prio, owner, succ):
        self.prio, self.owner, self.succ, self.n = prio, owner, succ, len(prio)
        self.rel = [(prio[v], v) for v in range(self.n)]
        order = sorted(range(self.n), key=lambda v: self.rel[v]); self.rk = [0] * self.n
        for i, v in enumerate(order): self.rk[v] = i
    def even(self, v): return self.prio[v] % 2 == 0
    def reward(self, v): return self.rk[v] if self.even(v) else -self.rk[v] - 1
    def cmp(self, A, B):
        """>0 iff A better for Even than B, 0 equal, <0 worse."""
        if A[0] != B[0]: return 1 if self.reward(A[0]) > self.reward(B[0]) else -1
        d = A[1] ^ B[1]
        if d:
            m = max(d, key=lambda v: self.rk[v]); good = self.even(m)
            return (1 if good else -1) if m in A[1] else (-1 if good else 1)
        if A[2] == B[2]: return 0
        if self.even(A[0]): return 1 if A[2] < B[2] else -1
        return 1 if A[2] > B[2] else -1
    def ext(self, v, A):
        L, P, k = A
        return (L, P | {v} if self.rk[v] > self.rk[L] else P, k + 1)
    def values(self, strat):
        """strat[v] = chosen successor for every vertex. Returns list of values."""
        n = self.n; val = [None] * n
        for v0 in range(n):
            if val[v0] is not None: continue
            path = []; pos = {}; v = v0
            while v not in pos and val[v] is None:
                pos[v] = len(path); path.append(v); v = strat[v]
            if val[v] is None:  # new cycle starting at pos[v]
                cyc = path[pos[v]:]; L = max(cyc, key=lambda u: self.rk[u]); i = cyc.index(L)
                val[L] = (L, frozenset(), 0)
                # walk the cycle backwards from L
                j = (i - 1) % len(cyc)
                while cyc[j] != L:
                    u = cyc[j]; val[u] = self.ext(u, val[strat[u]]); j = (j - 1) % len(cyc)
                path = path[:pos[v]]
            for u in reversed(path): val[u] = self.ext(u, val[strat[u]])
        return val
    def best_reply(self, sigma, tau0=None):
        """sigma: dict/list of Even choices (every Even vertex). Odd local improvement to a pointwise optimum."""
        n = self.n; st = [None] * n
        for v in range(n):
            st[v] = sigma[v] if self.owner[v] == 0 else (tau0[v] if tau0 else self.succ[v][0])
        while True:
            val = self.values(st); ch = False
            for v in range(n):
                if self.owner[v] != 1: continue
                cur = val[st[v]]; b = st[v]
                for w in self.succ[v]:
                    if self.cmp(val[w], val[b]) < 0: b = w
                if b != st[v] and self.cmp(val[b], cur) < 0: st[v] = b; ch = True
            if not ch: return st, val
    def brute(self, sigma):
        odd = [v for v in range(self.n) if self.owner[v] == 1]; best = None
        for ch in itertools.product(*[self.succ[v] for v in odd]):
            st = [sigma[v] if self.owner[v] == 0 else None for v in range(self.n)]
            for v, w in zip(odd, ch): st[v] = w
            val = self.values(st)
            if best is None: best = list(val)
            else:
                for v in range(self.n):
                    if self.cmp(val[v], best[v]) < 0: best[v] = val[v]
        return best

def opt_choices(E, st, val):
    """Odd choices consistent with the optimal values: u with ext(v, val[u]) == val[v] or (v is its own cycle node and
    u closes a cycle with the same value) -- used only as a diagnostic for rule-independence of R-steps."""
    out = {}
    for v in range(E.n):
        if E.owner[v] != 1: continue
        s = set()
        for u in E.succ[v]:
            if val[v][0] != v and E.cmp(E.ext(v, val[u]), val[v]) == 0 and v not in val[u][1] and not reaches(st, u, v, val): s.add(u)
            elif val[v][0] == v:
                t = list(st); t[v] = u
                if E.cmp(E.values(t)[v], val[v]) == 0: s.add(u)
        out[v] = s
    return out

def reaches(st, u, v, val):
    seen = set(); w = u
    while w not in seen:
        if w == v: return True
        seen.add(w); w = st[w]
    return False
