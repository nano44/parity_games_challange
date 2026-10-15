#!/usr/bin/env python3
"""L-SI strategy-improvement engine (own implementation; cross-checked against experiments/hard-families/pgsolver_si.py).

Valuations: Voege-Jurdzinski discrete valuations as in Friedmann, LMCS 7(3:19) 2011 (arXiv 1106.0778) section 3:
  theta(v) = (cycle node w, {path nodes more relevant than w}, path length), ordered by (reward of w, path set in the
  relevance-lexicographic reward order, length: shorter is worse for Even at odd cycles, longer is worse at even cycles).
Priorities are made injective by rank: p'(v) = 2*rank(v) + (pr(v) mod 2) with rank by (pr(v), v); this preserves every
cycle's winner, so the game is unchanged.  Bit cost: a valuation key is (int, int of n bits, int); comparisons cost O(n) bits.
Rules (improvement policies, Friedmann Def. section 3: pick edges in the arena A_{G,sigma}, at least one strictly improving):
  switch-all   locally optimizing policy (VJ00; PGSolver 'switchall' tie-breaks reproduced)
  rar          Random-Action-Removal = Kalai/MSW Random-Facet with fresh randomness (Zwick arXiv 2607.06334 Fig. 1)
  random-edge  one uniformly random improving edge (baseline, B10)
  msf / lsf    single switch: the improving edge whose valuation difference sits at the most / least relevant position
  steepest     single switch maximizing the re-evaluated valuation of the switched vertex
  switch-all-start-sub   S4: start from the optimum of the subgame V minus Attr(top priority), then switch-all
Output: regions and positional strategies for both players (Odd's = the optimal counterstrategy), checked by harness/verify.py.
Usage: si.py RULE game.pg [out.sol] [--seed S] [--start best|last|random]   (prints 'solved with K iterations.' to stderr)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg

sys.setrecursionlimit(10 ** 6)
EVEN, ODD = 0, 1


class Engine:
    def __init__(self, g):
        self.g = g
        n = self.n = g.n
        self.owner = g.owner
        self.succ = [sorted(set(s)) for s in g.succ]
        self.pred = [[] for _ in range(n)]
        for v in range(n):
            for w in self.succ[v]:
                self.pred[w].append(v)
        order = sorted(range(n), key=lambda v: (g.prio[v], v))
        self.rank = [0] * n
        for r, v in enumerate(order):
            self.rank[v] = r
        self.par = [g.prio[v] % 2 for v in range(n)]           # parity of the vertex (= parity of p')
        self.pp = [2 * self.rank[v] + self.par[v] for v in range(n)]   # injective priority p'
        self.rew = [self.pp[v] if self.par[v] == 0 else -self.pp[v] for v in range(n)]
        self.bit = [1 << self.rank[v] for v in range(n)]      # path component: bitmask over ranks
        self.rankpar = [0] * n
        for v in range(n):
            self.rankpar[self.rank[v]] = self.par[v]
        self.evals = 0
        self.cache = {}
        self.wcache = {0: 0}

    def weight(self, mask):
        """Signed weight of a path set: +2^r for even ranks, -2^r for odd ranks. M < N in Friedmann's set order iff
        weight(M) < weight(N) (the highest differing rank dominates the lower ones)."""
        w = self.wcache.get(mask)
        if w is None:
            w = 0; m = mask; r = 0
            while m:
                if m & 1:
                    w += (1 << r) if self.rankpar[r] == 0 else -(1 << r)
                m >>= 1; r += 1
            self.wcache[mask] = w
        return w

    # ---- valuation keys: larger = better for Even -------------------------------------------------------------
    def key(self, val):
        w, path, ln = val
        return (self.rew[w], self.weight(path), ln if self.par[w] == 1 else -ln)

    def extend(self, u, val):
        """Valuation of u when u steps to a vertex with valuation val (u on the path, added if more relevant)."""
        w, path, ln = val
        return (w, path | (self.bit[u] if self.rank[u] > self.rank[w] else 0), ln + 1)

    # ---- optimal counterstrategy valuation (VJ00; the structure of Friedmann section 3) -------------------------
    def evaluate(self, strat):
        """strat: tuple, strat[v] = successor for Even's v, -1 for Odd's. Returns (val, tau): val[v] = (cycle node,
        signed path weight, length); tau[v] = Odd's optimal counterstrategy choice (None for Even's vertices)."""
        key = tuple(strat)
        if key in self.cache:
            return self.cache[key]
        self.evals += 1
        n, rank = self.n, self.rank
        gs = [([strat[v]] if self.owner[v] == EVEN else self.succ[v]) for v in range(n)]
        gp = [[] for _ in range(n)]
        for v in range(n):
            for w in gs[v]:
                gp[w].append(v)
        alive = [True] * n
        val = [None] * n
        tau_full = [None] * n
        for v in sorted(range(n), key=lambda x: self.rew[x]):       # Odd's preferred cycle nodes first
            if not alive[v]:
                continue
            # cycle through v using only less relevant alive vertices?
            rv = rank[v]
            seen = {v}; st = [v]; found = False
            while st and not found:
                x = st.pop()
                for y in gs[x]:
                    if y == v:
                        found = True; break
                    if alive[y] and rank[y] < rv and y not in seen:
                        seen.add(y); st.append(y)
            if not found:
                continue
            # R: alive vertices reaching v
            R = {v}; st = [v]
            while st:
                x = st.pop()
                for y in gp[x]:
                    if alive[y] and y not in R:
                        R.add(y); st.append(y)
            hs = {x: [y for y in gs[x] if y in R] for x in R}
            hp = {x: [y for y in gp[x] if y in R] for x in R}
            path = {x: 0 for x in R}

            def reach(start, excl):
                s = {start}; st2 = [start]
                while st2:
                    x = st2.pop()
                    for y in hp[x]:
                        if y != excl and y not in s:
                            s.add(y); st2.append(y)
                return s

            def restrict(x, M):
                keep = [y for y in hs[x] if y in M]
                for y in hs[x]:
                    if y not in M:
                        hp[y].remove(x)
                hs[x] = keep
            for u in sorted((x for x in R if rank[x] > rv), key=lambda x: -rank[x]):
                if self.par[u] == 0:                 # Even likes u: Odd avoids it where it can
                    M = reach(v, u)
                    for q in R:
                        if q not in M:
                            path[q] |= self.bit[u]
                    restrict(u, M)
                    for q in M:
                        restrict(q, M)
                else:                                # Odd likes u: whoever can reach u (without v) goes there
                    M = reach(u, v)
                    for q in M:
                        path[q] |= self.bit[u]
                        if q != u:
                            restrict(q, M)
            dist = {}
            tau = {}
            if self.par[v] == 0:                     # even cycle: Odd takes the longest path (restricted graph is a DAG + v)
                state = {}
                def longest(x):
                    if x == v:
                        return 0
                    if x in state:
                        if state[x] is None:
                            raise RuntimeError("cycle in restricted graph")
                        return state[x]
                    state[x] = None
                    best, arg = -1, None
                    for y in hs[x]:
                        d = longest(y)
                        if d > best:
                            best, arg = d, y
                    state[x] = best + 1
                    tau[x] = arg
                    return best + 1
                for x in R:
                    dist[x] = longest(x)
            else:                                    # odd cycle: shortest path (BFS over preds from v)
                dist[v] = 0; layer = [v]
                while layer:
                    nxt = []
                    for x in layer:
                        for y in hp[x]:
                            if y not in dist:
                                dist[y] = dist[x] + 1; tau[y] = x; nxt.append(y)
                    layer = nxt
            # v itself: Odd's choice closes the cycle through less relevant vertices
            if self.owner[v] == ODD:
                # find successor y of v on a cycle back to v through ranks < rv (first found in DFS)
                par = {v: None}; st = [v]; cyc = None
                while st and cyc is None:
                    x = st.pop()
                    for y in gs[x]:
                        if y == v:
                            cyc = x; break
                        if alive[y] and rank[y] < rv and y not in par:
                            par[y] = x; st.append(y)
                x = cyc
                while par[x] is not v and par[x] is not None:
                    x = par[x]
                tau[v] = x if x != v else cyc
            for x in R:
                val[x] = (v, path[x], dist[x])
                alive[x] = False
                if self.owner[x] == ODD:
                    tau_full[x] = tau[x]          # Odd's optimal counterstrategy: the restricted-graph choice
        res = (val, tau_full)
        self.cache[key] = res
        return res

    # ---- helpers ----------------------------------------------------------------------------------------------
    def cycle_creating(self, strat, v, w):
        """True iff v lies on Odd's (sigma, tau)-play from w, INCLUDING the cycle the play ends in (play notion; the switch
        v -> w would then close a cycle through v under the current counterstrategy).  Correction by L-RED (2026-10-15):
        the earlier test looked only at the path SET of Xi(w), which omits vertices less relevant than the cycle node; a
        second slip (stopping at the cycle node) missed v on the final cycle after the cycle node."""
        _, tau = self.evaluate(strat)
        x = w; seen = set()
        while x not in seen:
            if x == v:
                return True
            seen.add(x)
            x = strat[x] if self.owner[x] == EVEN else tau[x]
        return False

    def improving(self, strat, val):
        out = []
        for v in range(self.n):
            if self.owner[v] == EVEN:
                kc = self.key(val[strat[v]])
                for w in self.succ[v]:
                    if w != strat[v] and self.key(val[w]) > kc:
                        out.append((v, w))
        return out

    def best_succ(self, v, val, cands=None):
        """PGSolver tie-break: max by (valuation, index)."""
        return max(cands if cands is not None else self.succ[v], key=lambda w: (self.key(val[w]), w))

    def initial(self, kind, rng=None):
        n = self.n
        if kind == "best":      # stratimpralgs.ml:85-87 initial_strategy_by_best_reward (ties: max index via <=)
            def rewcmp(w):
                r = self.g.prio[w] if self.g.prio[w] % 2 == 0 else -self.g.prio[w]
                return (r, w if r % 2 == 0 else -w)
            return tuple(-1 if self.owner[v] == ODD else max(self.succ[v], key=rewcmp) for v in range(n))
        if kind == "last":
            return tuple(-1 if self.owner[v] == ODD else max(self.succ[v]) for v in range(n))
        if kind == "first":
            return tuple(-1 if self.owner[v] == ODD else min(self.succ[v]) for v in range(n))
        if kind == "random":
            return tuple(-1 if self.owner[v] == ODD else rng.choice(self.succ[v]) for v in range(n))
        if kind.startswith("spec:"):      # "spec:v:w v:w ..." explicit start for Even's vertices (others: first successor)
            st = [-1 if self.owner[v] == ODD else self.succ[v][0] for v in range(n)]
            for tok in kind[5:].split():
                v, w = map(int, tok.split(":")); st[v] = w
            return tuple(st)
        raise ValueError(kind)

    def regions(self, strat):
        val, tau = self.evaluate(strat)
        win = [self.par[val[v][0]] for v in range(self.n)]
        ws = [None] * self.n
        for v in range(self.n):
            if self.owner[v] == EVEN and win[v] == EVEN:
                ws[v] = strat[v]
            elif self.owner[v] == ODD and win[v] == ODD:
                ws[v] = tau[v]
        return win, ws

    # ---- improvement rules: each maps (strat, val) -> new strat, given a non-empty improving set ----------------
    def rule_switch_all(self, strat, val, imp, rng):
        new = list(strat)
        for v in range(self.n):
            if self.owner[v] == EVEN:
                b = self.best_succ(v, val)
                if self.key(val[b]) > self.key(val[strat[v]]):
                    new[v] = b
        return tuple(new)

    def rule_random_edge(self, strat, val, imp, rng):
        v, w = rng.choice(imp)
        new = list(strat); new[v] = w
        return tuple(new)

    def _level(self, a, b):
        """Relevance level at which valuations a, b first differ: (3, max rank of the two cycle nodes) if the cycle
        nodes differ, (2, rank of the most relevant vertex in the symmetric difference of the path sets), (1, 0) if
        only the lengths differ."""
        if a[0] != b[0]:
            return (3, max(self.rank[a[0]], self.rank[b[0]]))
        if a[1] != b[1]:
            return (2, (a[1] ^ b[1]).bit_length() - 1)
        return (1, 0)

    def rule_single_level(self, strat, val, imp, rng, most=True):
        best, arg = None, None
        for v, w in imp:
            lv = self._level(val[strat[v]], val[w])
            k = (lv if most else (-lv[0], -lv[1]), -v, -w)
            if best is None or k > best:
                best, arg = k, (v, w)
        new = list(strat); new[arg[0]] = arg[1]
        return tuple(new)

    def rule_msfa(self, strat, val, imp, rng):
        """MSF-A: most significant first among the improving edges (v, w) whose target path does not pass through v
        (v not on Odd's play from w before its cycle node: the switch closes no cycle through v; play notion); if there is none, plain MSF."""
        acyc = [(v, w) for v, w in imp if not self.cycle_creating(strat, v, w)]
        return self.rule_single_level(strat, val, acyc if acyc else imp, rng, True)

    def rule_msfc(self, strat, val, imp, rng):
        """MSF-C: the opposite preference: cycle-creating improving edges first (highest level), else plain MSF."""
        cyc = [(v, w) for v, w in imp if self.cycle_creating(strat, v, w)]
        return self.rule_single_level(strat, val, cyc if cyc else imp, rng, True)

    def rule_steepest(self, strat, val, imp, rng):
        best, arg = None, None
        for v, w in imp:
            s = list(strat); s[v] = w; s = tuple(s)
            val2, _ = self.evaluate(s)
            k = (self.key(val2[v]), -v, -w)
            if best is None or k > best:
                best, arg = k, s
        return arg

    def rule_most_improved(self, strat, val, imp, rng):
        best, arg = None, None
        for v, w in imp:
            s = list(strat); s[v] = w; s = tuple(s)
            val2, _ = self.evaluate(s)
            cnt = sum(1 for x in range(self.n) if self.key(val2[x]) > self.key(val[x]))
            k = (cnt, -v, -w)
            if best is None or k > best:
                best, arg = k, s
        return arg

    # ---- generic driver ---------------------------------------------------------------------------------------
    def run(self, rule, start, rng=None, max_iter=None):
        strat = start
        it = 0
        while True:
            val, _ = self.evaluate(strat)
            imp = self.improving(strat, val)
            if not imp:
                return strat, it
            it += 1
            if max_iter and it > max_iter:
                raise RuntimeError("iteration cap")
            strat = rule(strat, val, imp, rng)

    # ---- Random-Action-Removal (Zwick 2607.06334, Fig. 1), fresh randomness per call ----------------------------
    def rar(self, start, rng):
        self.rar_switches = 0
        F = [set(self.succ[v]) if self.owner[v] == EVEN else set() for v in range(self.n)]
        return self._rar(F, start, rng)

    def _rar(self, F, a, rng):
        B = [(v, w) for v in range(self.n) if self.owner[v] == EVEN for w in F[v] if w != a[v]]
        if not B:
            return a
        v, r = rng.choice(B)
        F[v].discard(r)
        b = self._rar(F, a, rng)
        F[v].add(r)
        val, _ = self.evaluate(b)
        if self.key(val[r]) > self.key(val[b[v]]):      # edge b -> c=b[r] directed away from b: r improves b
            c = list(b); c[v] = r; c = tuple(c)
            self.rar_switches += 1
            return self._rar(F, c, rng)
        return b


def attractor(g, alive, target, player):
    attr = set(target); q = list(attr); cnt = {}
    while q:
        w = q.pop()
        for v in g.pred[w]:
            if v not in alive or v in attr:
                continue
            if g.owner[v] == player:
                attr.add(v); q.append(v)
            else:
                if v not in cnt:
                    cnt[v] = sum(1 for x in set(g.succ[v]) if x in alive)
                cnt[v] -= 1
                if cnt[v] == 0:
                    attr.add(v); q.append(v)
    return attr


def subgame(g, keep):
    keep = sorted(keep); idx = {v: i for i, v in enumerate(keep)}
    return pg.Game([g.prio[v] for v in keep], [g.owner[v] for v in keep],
                   [[idx[w] for w in g.succ[v] if w in idx] for v in keep]), keep


def solve_S4(g, counter, rule_name="switch-all", rng=None):
    """S4: start strategy = optimum of the subgame V \\ Attr_p(top priority), extended by best-reward on the attractor;
    then run the given rule.  Returns Even's final strategy; counter[0] accumulates iterations over the recursion."""
    if g.n == 0:
        return ()
    e = Engine(g)
    p = max(g.prio); top = {v for v in range(g.n) if g.prio[v] == p}
    A = attractor(g, set(range(g.n)), top, p % 2)
    rest = [v for v in range(g.n) if v not in A]
    start = list(e.initial("best"))
    if rest:
        sub, keep = subgame(g, rest)
        s_sub = solve_S4(sub, counter, rule_name, rng)
        for i, v in enumerate(keep):
            if g.owner[v] == EVEN:
                start[v] = keep[s_sub[i]]
    rule = RULES[rule_name](e)
    strat, it = e.run(rule, tuple(start), rng)
    counter[0] += it
    return strat


RULES = {
    "switch-all": lambda e: e.rule_switch_all,
    "random-edge": lambda e: e.rule_random_edge,
    "msf": lambda e: (lambda s, v, i, r: e.rule_single_level(s, v, i, r, True)),
    "lsf": lambda e: (lambda s, v, i, r: e.rule_single_level(s, v, i, r, False)),
    "msfa": lambda e: e.rule_msfa,
    "msfc": lambda e: e.rule_msfc,
    "steepest": lambda e: e.rule_steepest,
    "most-improved": lambda e: e.rule_most_improved,
}


def solve(g, rule_name, seed=0, start="best"):
    """Returns (win, strategies, iterations, evaluations)."""
    rng = random.Random(seed)
    e = Engine(g)
    if rule_name == "rar":
        strat = e.rar(e.initial(start, rng), rng)
        it = e.rar_switches
    elif rule_name.startswith("S4"):
        counter = [0]
        inner = rule_name[3:] if len(rule_name) > 3 else "switch-all"
        strat = solve_S4(g, counter, inner, rng)
        it = counter[0]
    else:
        strat, it = e.run(RULES[rule_name](e), e.initial(start, rng), rng)
    win, ws = e.regions(strat)
    return win, ws, it, e.evals


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    seed = int(args[args.index("--seed") + 1]) if "--seed" in args else 0
    start = args[args.index("--start") + 1] if "--start" in args else "best"
    pos = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] not in ("--seed", "--start"))]
    rule, path = pos[0], pos[1]
    g = pg.read(path)
    win, ws, it, ev = solve(g, rule, seed, start)
    print(f"solved with {it} iterations, {ev} evaluations.", file=sys.stderr)
    if len(pos) > 2:
        pg.write_sol(win, pos[2], ws)
    else:
        sys.stdout.write(f"paritysol {g.n};\n" + "".join(f"{v} {w}{'' if ws[v] is None else ' ' + str(ws[v])};\n" for v, w in enumerate(win)))
