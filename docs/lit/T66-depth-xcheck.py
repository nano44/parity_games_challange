#!/usr/bin/env python3
"""T66 (L-LIT): independent re-count of T66-depth-check.py's 'lmcs' rows, without experiments/si/si.py.

Own code for everything but the game table (imported from T66-depth-check.py, function lmcs = Table 4 of arXiv 1106.0778 v2):
  - values (cycle node, set Pi as a bitmask over relevance ranks, length) of a positional pair, by one pass over the functional graph;
  - Odd's optimal counterstrategy by BRUTE FORCE over all 2^N choices at the N Odd vertices e_i (the only Odd vertices with a choice):
    the choice vector whose value vector is pointwise minimal (asserted to exist and to be unique);
  - Howard's step: every Even vertex moves to a best successor (ties: largest index) if that is strictly better than its current one.
Order (VJ00 / Friedmann 1106.0778 section 3): reward of the cycle node (p' if even, -p' if odd; p' = 2*rank + parity, rank by
(priority, index)); then Pi by the most relevant vertex of the symmetric difference (in the better set iff it is even); then length
(shorter is better iff the cycle node is even).
Prints the same counters as T66-depth-check.py: T, C, flips, deep (> CMAX), dmax, unm, flips of the busiest gate.
Run from the repository root:  python3 -I docs/lit/T66-depth-xcheck.py NMIN NMAX [CMAX]
"""
import importlib.util, itertools, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("t66", os.path.join(HERE, "T66-depth-check.py"))
t66 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t66)


class Own:
    def __init__(self, g):
        self.n = n = g.n
        self.owner, self.succ, self.prio = g.owner, [sorted(set(s)) for s in g.succ], g.prio
        order = sorted(range(n), key=lambda v: (g.prio[v], v))
        self.rank = [0] * n
        for r, v in enumerate(order):
            self.rank[v] = r
        self.even = [g.prio[v] % 2 == 0 for v in range(n)]
        self.evenrank = [False] * n                           # parity of the vertex of a given rank
        for v in range(n):
            self.evenrank[self.rank[v]] = self.even[v]

    def values(self, nxt):
        """nxt[v] = the successor of v under the positional pair. Returns val[v] = (cycle node, Pi mask, length)."""
        n, rank = self.n, self.rank
        val = [None] * n
        state = [0] * n                                       # 0 new, 1 on stack, 2 done
        for s in range(n):
            if state[s]:
                continue
            path = []
            v = s
            while state[v] == 0:
                state[v] = 1; path.append(v); v = nxt[v]
            if state[v] == 1:                                 # closed a new cycle at v
                i = path.index(v)
                cyc = path[i:]
                top = max(cyc, key=lambda u: rank[u])
                j = cyc.index(top)
                rot = cyc[j:] + cyc[:j]                       # top first, then the cycle in play order
                val[top] = (top, 0, 0); state[top] = 2
                for u in reversed(rot[1:]):                   # walk backwards from the vertex just before top
                    w = nxt[u]
                    c, pm, ln = val[w]
                    val[u] = (c, pm | ((1 << rank[u]) if rank[u] > rank[c] else 0), ln + 1); state[u] = 2
                path = path[:i]
            for u in reversed(path):
                c, pm, ln = val[nxt[u]]
                val[u] = (c, pm | ((1 << rank[u]) if rank[u] > rank[c] else 0), ln + 1); state[u] = 2
        return val

    def better(self, a, b):
        """True iff value a is strictly better for Even than value b."""
        if a[0] != b[0]:
            ra = (2 * self.rank[a[0]] + (0 if self.even[a[0]] else 1)) * (1 if self.even[a[0]] else -1)
            rb = (2 * self.rank[b[0]] + (0 if self.even[b[0]] else 1)) * (1 if self.even[b[0]] else -1)
            return ra > rb
        x = a[1] ^ b[1]
        if x:
            z = x.bit_length() - 1
            return bool((a[1] >> z) & 1) == self.evenrank[z]
        if a[2] == b[2]:
            return False
        return (a[2] < b[2]) == self.even[a[0]]

    def evaluate(self, strat, gates):
        """Brute force: all choice vectors of Odd at the gates; return (val, tau) with val pointwise minimal."""
        base = [strat[v] if self.owner[v] == 0 else self.succ[v][0] for v in range(self.n)]
        cands = []
        for choice in itertools.product(*[self.succ[g] for g in gates]):
            nxt = list(base)
            for g, w in zip(gates, choice):
                nxt[g] = w
            cands.append((self.values(nxt), choice))
        low = list(cands[0][0])                               # pointwise minimum over all counterstrategies
        for val, _ in cands[1:]:
            for v in range(self.n):
                if self.better(low[v], val[v]):
                    low[v] = val[v]
        opt = [c for c in cands if all(c[0][v] == low[v] for v in range(self.n))]
        assert opt, "no counterstrategy attains the pointwise minimum"
        assert len(opt) == 1, "the optimal counterstrategy is not unique"
        return opt[0][0], dict(zip(gates, opt[0][1]))


def depth(a, b):
    if a[0] != b[0]:
        return -1
    x = a[1] ^ b[1]
    if x == 0:
        return bin(a[1]).count("1")
    return bin(a[1] >> x.bit_length()).count("1")


def run(n, cmax):
    g, strat, names = t66.lmcs(n)
    eng = Own(g)
    gates = [v for v in range(g.n) if g.owner[v] == 1 and len(eng.succ[v]) >= 2]
    strat = list(strat)
    val, tau = eng.evaluate(strat, gates)
    T = C = flips = deep = unm = 0
    dmax = -1
    per = {}
    while True:
        new = list(strat)
        for v in range(g.n):
            if g.owner[v] == 0:
                b = eng.succ[v][0]
                for w in eng.succ[v][1:]:                     # ascending index: among equal best values the largest index wins
                    if not eng.better(val[b], val[w]):
                        b = w
                if eng.better(val[b], val[strat[v]]):
                    new[v] = b
        if new == strat:
            break
        nval, ntau = eng.evaluate(new, gates)
        T += 1
        if any(val[v][0] != nval[v][0] for v in range(g.n)):
            C += 1
        for q in gates:
            if tau[q] != ntau[q]:
                a = tau[q]
                flips += 1; per[q] = per.get(q, 0) + 1
                if not eng.better(nval[a], val[a]):
                    unm += 1
                d = depth(val[a], nval[a]); dmax = max(dmax, d)
                if d > cmax:
                    deep += 1
        strat, val, tau = new, nval, ntau
    bq = max(per.items(), key=lambda kv: kv[1]) if per else (None, 0)
    print(f"own  N {n} n {g.n} T {T} C {C} gates {len(gates)} flips {flips} deep(>{cmax}) {deep} dmax {dmax} unm {unm} "
          f"busiest {names[bq[0]] if bq[0] is not None else '-'} {bq[1]}")


if __name__ == "__main__":
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    cmax = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    for n in range(lo, hi + 1):
        run(n, cmax)
