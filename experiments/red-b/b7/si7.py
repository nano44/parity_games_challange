#!/usr/bin/env python3
"""L-RED-B B7: own engine for classical one-sided Voege-Jurdzinski strategy improvement with a pluggable selection rule.

Source of the definitions: O. Friedmann, arXiv 1106.0778v2 (LMCS 7(3:19) 2011), Section 3 (PDF p. 4-6): node valuation
theta = (cycle node w1, {path nodes more relevant than w1}, path length k), the orders on nodes, sets and valuations, the
optimal counterstrategy tau_sigma (Lemma 3.1), the improvement arena, improving edges, Algorithm 1.  Nothing here is copied
from another lane's engine; the valuation routine is tested against the DEFINITION by brute force over all Odd strategies
(st7.py bf).

Priorities are made injective by rank: relevance rank r(v) by (prio, vertex id).  Two vertices of equal priority have equal
parity, so every cycle keeps its winner.  Valuation key (larger = better for Even):
    (rew(w), W(P), +k if w odd else -k),  rew(w) = +(r(w)+1) for even w, -(r(w)+1) for odd w,
    W(P) = sum over u in P of +2^r(u) (u even) or -2^r(u) (u odd)        [order-isomorphic to the paper's set order].
Bit cost: W(P) is an n-bit integer; a comparison costs O(n) bit operations (TARGET.md section 3).

API: Engine(g).evaluate(sigma) -> (val, tau); val[v] = (w, W, k) of the play from v; tau[v] = Odd's choice (optimal).
     Engine.run(sigma0, rule) -> iterations, final sigma.  A rule maps (engine, sigma, val, tau, imp) to a new sigma that
     differs from sigma only by improving edges, at least one.
Usage: si7.py RULE game.pg [--start FILE|best|first|last] [--sol OUT] [--trace]"""
import sys

EVEN, ODD = 0, 1


class Game:
    def __init__(self, prio, owner, succ, names=None):
        self.n = len(prio); self.prio = list(prio); self.owner = list(owner)
        self.succ = [list(dict.fromkeys(s)) for s in succ]
        self.names = list(names) if names else [str(v) for v in range(self.n)]
        self.m = sum(len(s) for s in self.succ)
        assert all(self.succ[v] for v in range(self.n)), "dead end"


def parse_pg(text):
    rows = {}
    for line in text.replace("\n", " ").split(";"):
        line = line.strip()
        if not line or line.startswith("parity") or line.startswith("start"):
            continue
        parts = line.split(None, 3)
        v, p, o = int(parts[0]), int(parts[1]), int(parts[2])
        rest = parts[3] if len(parts) > 3 else ""
        name = None
        if '"' in rest:
            i = rest.index('"'); name = rest[i + 1:rest.rindex('"')]; rest = rest[:i]
        rows[v] = (p, o, [int(x) for x in rest.replace(" ", "").split(",") if x], name)
    ids = sorted(rows); assert ids == list(range(len(ids))), "vertex ids must be 0..n-1"
    return Game([rows[v][0] for v in ids], [rows[v][1] for v in ids], [rows[v][2] for v in ids],
                [rows[v][3] if rows[v][3] is not None else str(v) for v in ids])


def dump_pg(g):
    out = [f"parity {g.n - 1};"]
    for v in range(g.n):
        out.append(f'{v} {g.prio[v]} {g.owner[v]} {",".join(map(str, g.succ[v]))} "{g.names[v]}";')
    return "\n".join(out) + "\n"


class Engine:
    def __init__(self, g):
        self.g = g; n = self.n = g.n
        self.owner = g.owner; self.succ = g.succ
        order = sorted(range(n), key=lambda v: (g.prio[v], v))
        self.rank = [0] * n
        for r, v in enumerate(order):
            self.rank[v] = r
        self.par = [g.prio[v] & 1 for v in range(n)]
        self.rew = [(self.rank[v] + 1) if self.par[v] == 0 else -(self.rank[v] + 1) for v in range(n)]
        self.sbit = [(1 << self.rank[v]) if self.par[v] == 0 else -(1 << self.rank[v]) for v in range(n)]
        self.by_rew = sorted(range(n), key=lambda v: self.rew[v])
        self.evens = [v for v in range(n) if g.owner[v] == EVEN]
        self.evals = 0

    # ---- keys -------------------------------------------------------------------------------------------------
    def key(self, t):
        w, W, k = t
        return (self.rew[w], W, k if self.par[w] else -k)

    # ---- optimal counterstrategy and valuation ------------------------------------------------------------------
    def evaluate(self, sigma):
        """Odd's best response to sigma in the lexicographic order (cycle node, path set, length), computed in three
        stages: cycle nodes in ascending reward order; for one cycle node w, the more relevant vertices in descending
        relevance order (an even one is avoided by everybody who can avoid it, an odd one is visited by everybody who can
        reach it before w); then longest (w even) or shortest (w odd) distances to w."""
        self.evals += 1
        n, rank, owner, succ, par, sbit = self.n, self.rank, self.owner, self.succ, self.par, self.sbit
        gs = [[sigma[v]] if owner[v] == EVEN else succ[v] for v in range(n)]
        gp = [[] for _ in range(n)]
        for v in range(n):
            for y in gs[v]:
                gp[y].append(v)
        alive = [True] * n
        cyc = [-1] * n; pw = [0] * n; ln = [0] * n; tau = [-1] * n
        for w in self.by_rew:
            if not alive[w]:
                continue
            rw = rank[w]
            # is there a cycle through w whose other vertices are alive and less relevant than w?
            seen = {w}; st = [w]; found = False
            while st and not found:
                x = st.pop()
                for y in gs[x]:
                    if y == w:
                        found = True; break
                    if alive[y] and rank[y] < rw and y not in seen:
                        seen.add(y); st.append(y)
            if not found:
                continue
            R = {w}; st = [w]
            while st:
                x = st.pop()
                for y in gp[x]:
                    if alive[y] and y not in R:
                        R.add(y); st.append(y)
            hs = {x: set(y for y in gs[x] if y in R) for x in R}
            hp = {x: set(y for y in gp[x] if y in R) for x in R}

            def back(start, excl):
                S = {start}; st2 = [start]
                while st2:
                    x = st2.pop()
                    for y in hp[x]:
                        if y != excl and y not in S:
                            S.add(y); st2.append(y)
                return S

            def confine(x, S):
                for y in [y for y in hs[x] if y not in S]:
                    hs[x].discard(y); hp[y].discard(x)

            for u in sorted((x for x in R if rank[x] > rw), key=lambda x: -rank[x]):
                if par[u] == 0:
                    S = back(w, u)                      # can reach w without u
                    for q in R:
                        if q not in S:
                            pw[q] += sbit[u]
                    for q in S:
                        confine(q, S)
                    confine(u, S)
                else:
                    S = back(u, w)                      # can reach u without w
                    for q in S:
                        pw[q] += sbit[u]
                        if q != u:
                            confine(q, S)
            # distances to w in the remaining graph
            if par[w] == 1:
                dist = {w: 0}; frontier = [w]
                while frontier:
                    nxt = []
                    for x in frontier:
                        for y in hp[x]:
                            if y not in dist:
                                dist[y] = dist[x] + 1; nxt.append(y)
                    frontier = nxt
            else:
                # longest distances: the remaining graph without w's out-edges is acyclic
                dist = {w: 0}; outdeg = {x: (len(hs[x]) if x != w else 0) for x in R}
                best = {x: 0 for x in R}; queue = [w]
                while queue:
                    x = queue.pop()
                    for y in hp[x]:
                        if y == w:
                            continue
                        if dist[x] + 1 > best[y]:
                            best[y] = dist[x] + 1
                        outdeg[y] -= 1
                        if outdeg[y] == 0:
                            dist[y] = best[y]; queue.append(y)
            assert len(dist) == len(R), "valuation: a vertex of R lost its way to the cycle node"
            for x in R:
                cyc[x] = w; ln[x] = dist[x]; alive[x] = False
            for x in R:
                if owner[x] == ODD:
                    if x == w:
                        cands = [y for y in hs[x] if pw[y] == 0]
                    else:
                        cands = [y for y in hs[x] if dist[y] + 1 == dist[x]]
                    assert cands, "valuation: no consistent successor"
                    tau[x] = min(cands)
        assert not any(alive), "valuation: unassigned vertex"
        return [(cyc[v], pw[v], ln[v]) for v in range(n)], tau

    # ---- improvement ---------------------------------------------------------------------------------------------
    def improving(self, sigma, val):
        """{v: [improving targets]} for Even's vertices: targets u with Xi(sigma(v)) < Xi(u)."""
        imp = {}
        key = self.key
        kv = [key(val[v]) for v in range(self.n)]
        for v in self.evens:
            cur = kv[sigma[v]]
            better = [u for u in self.succ[v] if kv[u] > cur]
            if better:
                imp[v] = better
        return imp, kv

    def best_target(self, v, sigma, kv, tie="low"):
        """A successor of maximal valuation; the current one if it is maximal; among several maximal ones the lowest
        (tie = low) or the highest (tie = high) vertex id."""
        mx = max(kv[u] for u in self.succ[v])
        if kv[sigma[v]] == mx:
            return sigma[v]
        cands = [u for u in self.succ[v] if kv[u] == mx]
        return min(cands) if tie == "low" else max(cands)

    def run(self, sigma0, rule, maxit=10 ** 9, trace=None):
        sigma = list(sigma0); its = 0
        while True:
            val, tau = self.evaluate(sigma)
            imp, kv = self.improving(sigma, val)
            if trace is not None:
                trace(its, sigma, val, tau, imp)
            if not imp:
                return its, sigma, val, tau
            new = rule(self, sigma, val, tau, imp, kv)
            changed = [v for v in self.evens if new[v] != sigma[v]]
            assert changed and all(v in imp and new[v] in imp[v] for v in changed), "rule left the improvement arena"
            sigma = new; its += 1
            if its >= maxit:
                return its, sigma, None, None

    def regions(self, val):
        return [self.par[val[v][0]] for v in range(self.n)]       # 0 = won by Even, 1 = won by Odd

    def initial(self, how):
        g = self.g
        if how == "first":
            return [g.succ[v][0] if g.owner[v] == EVEN else -1 for v in range(g.n)]
        if how == "last":
            return [g.succ[v][-1] if g.owner[v] == EVEN else -1 for v in range(g.n)]
        if how == "best":      # successor of best reward, ties to the larger id
            return [max(g.succ[v], key=lambda u: (self.rew[u], u)) if g.owner[v] == EVEN else -1 for v in range(g.n)]
        raise ValueError(how)


# ---- rules -----------------------------------------------------------------------------------------------------------
def howard(tie="low"):
    """switch-best at every Even vertex (the locally optimizing policy, arXiv 1106.0778v2 Section 4)."""
    def rule(E, sigma, val, tau, imp, kv):
        new = list(sigma)
        for v in imp:
            new[v] = E.best_target(v, sigma, kv, tie)
        return new
    return rule


def play_vertices(E, sigma, tau, start, memo):
    """set of vertices on the play from start under (sigma, tau), as a frozenset (memoised by start)."""
    if start in memo:
        return memo[start]
    path = []; pos = {}
    x = start
    while x not in pos and x not in memo:
        pos[x] = len(path); path.append(x)
        x = sigma[x] if E.owner[x] == EVEN else tau[x]
    if x in memo:
        acc = set(memo[x])
        for y in reversed(path):
            acc = acc | {y}; memo[y] = frozenset(acc)
    else:
        i = pos[x]; cyc = frozenset(path[i:])
        for y in path[i:]:
            memo[y] = cyc
        acc = set(cyc)
        for y in reversed(path[:i]):
            acc = acc | {y}; memo[y] = frozenset(acc)
    return memo[start]


def sccs(nodes, adj):
    """Tarjan, iterative. Returns comp index per node (reverse topological: sinks get the smallest indices first)."""
    index = {}; low = {}; onst = set(); st = []; comp = {}; nc = 0; counter = 0
    for s in nodes:
        if s in index:
            continue
        work = [(s, iter(adj[s]))]; index[s] = low[s] = counter; counter += 1; st.append(s); onst.add(s)
        while work:
            v, it = work[-1]
            adv = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = counter; counter += 1; st.append(w); onst.add(w)
                    work.append((w, iter(adj[w]))); adv = True; break
                elif w in onst:
                    low[v] = min(low[v], index[w])
            if adv:
                continue
            work.pop()
            if work:
                p = work[-1][0]; low[p] = min(low[p], low[v])
            if low[v] == index[v]:
                while True:
                    w = st.pop(); onst.discard(w); comp[w] = nc
                    if w == v:
                        break
                nc += 1
    return comp, nc


def rf_dependency(E, sigma, tau, imp):
    """RF's dependency digraph on the improvable vertices (the Lead's relay of L-SI 57's wording, 2026-11-14 14:07Z):
    v depends on u != v iff u lies on the play from sigma(v) or from one of v's improving targets."""
    memo = {}
    I = set(imp)
    adj = {}
    for v in imp:
        deps = set()
        for t in [sigma[v]] + list(imp[v]):
            deps |= (play_vertices(E, sigma, tau, t, memo) & I)
        deps.discard(v)
        adj[v] = deps
    return adj


def root_first(tie="low", stats=None):
    """RF: switch-best exactly at the improvable vertices in the sink strongly connected components of the dependency
    digraph."""
    def rule(E, sigma, val, tau, imp, kv):
        adj = rf_dependency(E, sigma, tau, imp)
        comp, nc = sccs(list(imp), adj)
        sink = [True] * nc
        for v in imp:
            for u in adj[v]:
                if comp[u] != comp[v]:
                    sink[comp[v]] = False
        new = list(sigma); cnt = 0
        for v in imp:
            if sink[comp[v]]:
                new[v] = E.best_target(v, sigma, kv, tie); cnt += 1
        if stats is not None:
            stats.append((len(imp), nc, sum(sink), cnt))
        return new
    return rule


RULES = {"howard": howard, "rf": root_first}


def read_start(path, g):
    s = [-1] * g.n
    for line in open(path):
        a = line.split()
        if len(a) == 2:
            s[int(a[0])] = int(a[1])
    assert all((s[v] in g.succ[v]) == (g.owner[v] == EVEN) for v in range(g.n)), "bad start file"
    return s


def write_sol(path, E, sigma, val, tau):
    reg = E.regions(val)
    with open(path, "w") as f:
        f.write(f"paritysol {E.n - 1};\n")
        for v in range(E.n):
            s = sigma[v] if E.owner[v] == EVEN else tau[v]
            f.write(f"{v} {reg[v]} {s};\n" if E.owner[v] == reg[v] else f"{v} {reg[v]};\n")


if __name__ == "__main__":
    a = sys.argv[1:]
    rule = a[0]; g = parse_pg(open(a[1]).read()); E = Engine(g)
    start = "best"; sol = None; tie = "low"; i = 2
    while i < len(a):
        if a[i] == "--start": start = a[i + 1]; i += 2
        elif a[i] == "--sol": sol = a[i + 1]; i += 2
        elif a[i] == "--tie": tie = a[i + 1]; i += 2
        else: raise SystemExit("unknown option " + a[i])
    s0 = E.initial(start) if start in ("best", "first", "last") else read_start(start, g)
    its, sigma, val, tau = E.run(s0, RULES[rule](tie))
    reg = E.regions(val)
    print(f"{rule} tie {tie} n {g.n} m {g.m} iterations {its} evals {E.evals} even-won {reg.count(0)} odd-won {reg.count(1)}")
    if sol:
        write_sol(sol, E, sigma, val, tau)
