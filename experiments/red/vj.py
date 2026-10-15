#!/usr/bin/env python3
"""L-RED's independent Voege-Jurdzinski valuation and single-switch strategy improvement (MSF / LSF).

Written from the definitions in Friedmann, LMCS 7(3:19) 2011, arXiv 1106.0778, section 3 (pp. 4-6):
  play from v under positional (sigma, tau):  v1 ... vk (w1 ... wl)^omega, w1 the most relevant node of the cycle;
  node valuation  theta = (w1, {v_i > w1 : 1 <= i <= k}, k)   (path component INCLUDES v1 = v itself);
  set order: M < N  iff  max(M delta N) is in (N cap V_even) cup (M cap V_odd);
  (u,M,e) < (v,N,f) iff u <_rew v, or u = v and M < N, or u = v, M = N and (e < f and u odd, or e > f and u even);
  rew(v) = Omega(v) if even else -Omega(v);  Xi_sigma(v) = min over tau (Lemma 3.1, VJ00: a single optimal tau exists).
Priorities are made injective exactly as L-SI's engine does (S2.md: p'(v) = 2 rank(v) + parity, rank by (Omega(v), v)),
since that tie-break is part of the candidate's definition.  Everything else is written independently of si.py:
  evaluate()      Odd's optimal counterstrategy by the VJ construction (best cycle node first, then path bits in decreasing
                  relevance, then length), own code;
  evaluate_bf()   brute force over ALL positional counterstrategies tau (pointwise min), for validation on small games;
  msf()/lsf()     S2.md rule: one improving edge of maximal (minimal) level, ties smallest v then smallest w.
Usage: vj.py RULE game.pg [--start best|first|last|spec:v:w,...] [--trace]"""
import sys, os, itertools
sys.setrecursionlimit(1 << 20)
EVEN, ODD = 0, 1


def read_pg(path):
    prio, owner, succ, rows = {}, {}, {}, []
    for line in open(path):
        line = line.strip().rstrip(";")
        if not line or line.startswith("parity") or line.startswith("%") or line.startswith("start"):
            continue
        parts = line.split('"')[0].split()
        v, p, o = int(parts[0]), int(parts[1]), int(parts[2])
        prio[v], owner[v], succ[v] = p, o, sorted({int(x) for x in parts[3].split(",")})
    n = len(prio)
    assert sorted(prio) == list(range(n)), "vertex ids must be 0..n-1"
    return [prio[v] for v in range(n)], [owner[v] for v in range(n)], [succ[v] for v in range(n)]


class VJ:
    def __init__(self, prio, owner, succ):
        self.n = n = len(prio); self.prio = list(prio); self.owner = list(owner); self.succ = [list(s) for s in succ]
        order = sorted(range(n), key=lambda v: (prio[v], v))
        self.rank = [0] * n
        for r, v in enumerate(order):
            self.rank[v] = r
        self.par = [prio[v] & 1 for v in range(n)]
        self.pp = [2 * self.rank[v] + self.par[v] for v in range(n)]          # injective priority
        self.rew = [self.pp[v] if self.par[v] == EVEN else -self.pp[v] for v in range(n)]
        self.rankpar = [0] * n
        for v in range(n):
            self.rankpar[self.rank[v]] = self.par[v]
        self.pred = [[] for _ in range(n)]
        for v in range(n):
            for w in self.succ[v]:
                self.pred[w].append(v)
        self.cache = {}; self.evals = 0

    # ---- orders ----------------------------------------------------------------------------------------------
    def setkey(self, M):
        """M: bitmask over ranks. Larger key = better for Even; equals the set order of 1106.0778 p.4."""
        k = 0; r = 0
        while M:
            if M & 1:
                k += (1 << r) if self.rankpar[r] == EVEN else -(1 << r)
            M >>= 1; r += 1
        return k

    def key(self, th):
        c, M, k = th
        return (self.rew[c], self.setkey(M), k if self.par[c] == ODD else -k)

    def better(self, a, b):
        return self.key(a) > self.key(b)

    def level(self, a, b):
        """S2.md: (3, max rank of the cycle nodes) if they differ; (2, rank of max(M delta N)); else (1, 0)."""
        if a[0] != b[0]:
            return (3, max(self.rank[a[0]], self.rank[b[0]]))
        if a[1] != b[1]:
            return (2, (a[1] ^ b[1]).bit_length() - 1)
        return (1, 0)

    # ---- play valuation under fixed (sigma, tau) ---------------------------------------------------------------
    def play_value(self, sigma, tau, v):
        nxt = lambda u: sigma[u] if self.owner[u] == EVEN else tau[u]
        pos = {}; path = []; u = v
        while u not in pos:
            pos[u] = len(path); path.append(u); u = nxt(u)
        cyc = path[pos[u]:]; c = max(cyc, key=lambda x: self.rank[x])
        k = path.index(c)
        M = 0
        for x in path[:k]:
            if self.rank[x] > self.rank[c]:
                M |= 1 << self.rank[x]
        return (c, M, k)

    def evaluate_bf(self, sigma):
        """Pointwise minimum over all positional tau (exponential; validation only)."""
        oddv = [v for v in range(self.n) if self.owner[v] == ODD]
        best = [None] * self.n
        for choice in itertools.product(*[self.succ[v] for v in oddv]):
            tau = [None] * self.n
            for v, w in zip(oddv, choice):
                tau[v] = w
            for v in range(self.n):
                th = self.play_value(sigma, tau, v)
                if best[v] is None or self.key(th) < self.key(best[v]):
                    best[v] = th
        return best

    # ---- Odd's optimal counterstrategy (VJ00 construction, own code) -------------------------------------------
    def evaluate(self, sigma):
        key = tuple(sigma)
        if key in self.cache:
            return self.cache[key]
        self.evals += 1
        n, rank = self.n, self.rank
        out = [([sigma[v]] if self.owner[v] == EVEN else list(self.succ[v])) for v in range(n)]
        alive = set(range(n)); val = [None] * n; tau = [None] * n
        while alive:
            # Odd's best available cycle node: minimal reward among alive w lying on a cycle of alive vertices below w
            w = None
            for cand in sorted(alive, key=lambda x: self.rew[x]):
                rc = rank[cand]; seen = {cand}; st = [cand]; ok = False
                while st and not ok:
                    x = st.pop()
                    for y in out[x]:
                        if y == cand:
                            ok = True; break
                        if y in alive and rank[y] < rc and y not in seen:
                            seen.add(y); st.append(y)
                if ok:
                    w = cand; break
            assert w is not None
            # region R: alive vertices that can reach w
            R = {w}; st = [w]
            while st:
                x = st.pop()
                for y in self.pred[x]:
                    if y in alive and y not in R and x in out[y]:
                        R.add(y); st.append(y)
            # H: allowed edges inside R, w is a sink (the path ends at the first visit of w)
            H = {x: ([] if x == w else [y for y in out[x] if y in R]) for x in R}
            Hp = {x: [] for x in R}
            for x in R:
                for y in H[x]:
                    Hp[y].append(x)

            def can_reach(target, avoid):
                """vertices of R with an H-path to target not passing through avoid (target itself included)"""
                S = {target}; st = [target]
                while st:
                    x = st.pop()
                    for y in Hp[x]:
                        if y != avoid and y not in S:
                            S.add(y); st.append(y)
                return S

            def keep_only(x, allowed):
                for y in H[x]:
                    if y not in allowed:
                        Hp[y].remove(x)
                H[x] = [y for y in H[x] if y in allowed]

            bits = {x: 0 for x in R}
            for u in sorted((x for x in R if rank[x] > rank[w]), key=lambda x: -rank[x]):
                if self.par[u] == EVEN:                # Odd avoids u wherever it can
                    A = can_reach(w, u)
                    for q in R:
                        if q in A:
                            keep_only(q, A)
                        else:
                            bits[q] |= 1 << rank[u]
                    keep_only(u, A)                    # u's own path to w leaves u at once
                else:                                  # Odd goes through u wherever it can
                    B = can_reach(u, w)
                    for q in B:
                        bits[q] |= 1 << rank[u]
                        if q != u:
                            keep_only(q, B)
            # lengths: w odd -> Odd wants the shortest path; w even -> the longest (H is then acyclic, see notes)
            dist = {w: 0}
            if self.par[w] == ODD:
                layer = [w]
                while layer:
                    nl = []
                    for x in layer:
                        for y in Hp[x]:
                            if y not in dist:
                                dist[y] = dist[x] + 1; tau[y] = x; nl.append(y)
                    layer = nl
            else:
                state = {}
                def longest(x):
                    if x in dist:
                        return dist[x]
                    if state.get(x) == 1:
                        raise RuntimeError("cycle in the restricted graph (should not happen for an even cycle node)")
                    state[x] = 1; best = (-1, None)
                    for y in H[x]:
                        d = longest(y)
                        if d > best[0]:
                            best = (d, y)
                    dist[x] = best[0] + 1; tau[x] = best[1]; state[x] = 2
                    return dist[x]
                for x in R:
                    longest(x)
            assert all(x in dist for x in R)
            # tau at w (if Odd's): close a cycle through w using vertices below w
            if self.owner[w] == ODD:
                par = {w: None}; st = [w]; closing = None
                while st and closing is None:
                    x = st.pop()
                    for y in out[x]:
                        if y == w:
                            closing = x; break
                        if y in alive and rank[y] < rank[w] and y not in par:
                            par[y] = x; st.append(y)
                x = closing
                while par[x] is not None and par[x] != w:
                    x = par[x]
                tau[w] = x if par[x] == w else closing
            for x in R:
                val[x] = (w, bits[x], dist[x])
                if self.owner[x] == EVEN:
                    tau[x] = None
            alive -= R
        res = (val, tau)
        self.cache[key] = res
        return res

    # ---- rules -------------------------------------------------------------------------------------------------
    def improving(self, sigma, val):
        return [(v, w) for v in range(self.n) if self.owner[v] == EVEN
                for w in self.succ[v] if w != sigma[v] and self.better(val[w], val[sigma[v]])]

    def pick(self, sigma, val, imp, most=True):
        best = None
        for v, w in imp:
            lv = self.level(val[sigma[v]], val[w])
            k = ((lv[0], lv[1]) if most else (-lv[0], -lv[1]), -v, -w)
            if best is None or k > best[0]:
                best = (k, v, w, lv)
        return best[1], best[2], best[3]

    def pick_most_improved(self, sigma, val, imp):
        """S7 (docs/si/candidates/S7.md): switch the improving edge maximising |{x : Xi_{sigma[e]}(x) > Xi_sigma(x)}|; ties: the
        largest new valuation at v; then the smallest (v, w). Returns (v, w, count, index_tie_used)."""
        best = None
        for v, w in imp:
            s2 = list(sigma); s2[v] = w; val2, _ = self.evaluate(tuple(s2))
            cnt = sum(1 for x in range(self.n) if self.key(val2[x]) > self.key(val[x]))
            k = (cnt, self.key(val2[v]))
            if best is None or k > best[0] or (k == best[0] and (v, w) < best[1]):
                tie = best is not None and k == best[0]
                best = (k, (v, w), tie or (best[2] if best else False))
        return best[1][0], best[1][1], best[0][0], best[2]

    def initial(self, kind):
        n = self.n
        if kind == "best":          # PGSolver best-reward start as L-SI uses it (stratimpralgs.ml:85-87 via si.py)
            def rk(w):
                r = self.prio[w] if self.prio[w] % 2 == 0 else -self.prio[w]
                return (r, w if r % 2 == 0 else -w)
            return tuple(-1 if self.owner[v] == ODD else max(self.succ[v], key=rk) for v in range(n))
        if kind == "first":
            return tuple(-1 if self.owner[v] == ODD else self.succ[v][0] for v in range(n))
        if kind == "last":
            return tuple(-1 if self.owner[v] == ODD else self.succ[v][-1] for v in range(n))
        if kind.startswith("spec:"):
            st = [-1 if self.owner[v] == ODD else self.succ[v][0] for v in range(n)]
            for tok in kind[5:].replace(",", " ").split():
                v, w = map(int, tok.split(":")); st[v] = w
            return tuple(st)
        raise ValueError(kind)

    def on_play(self, sigma, tau, val, v, w):
        """cycle-creating in the corrected sense: v lies on Odd's play from w before the first visit of w's cycle node"""
        x = val[w][0]; u = w; seen = set()
        while u != x and u not in seen:
            if u == v:
                return True
            seen.add(u); u = sigma[u] if self.owner[u] == EVEN else tau[u]
        return False

    def run(self, rule, start, trace=False, cap=None, hook=None):
        sigma = start; it = 0; stats = {"cyc": 0, "escape": 0, "cycnode_change": 0}
        while True:
            val, tau = self.evaluate(sigma); imp = self.improving(sigma, val)
            if not imp:
                return sigma, it, stats
            if rule == "most-improved":
                v, w, cnt, tie = self.pick_most_improved(sigma, val, imp); lv = ("count", cnt); stats["index_ties"] = stats.get("index_ties", 0) + tie
            else:
                v, w, lv = self.pick(sigma, val, imp, most=(rule == "msf"))
            new = list(sigma); new[v] = w; new = tuple(new)
            cyc = self.on_play(sigma, tau, val, v, w)
            val2, _ = self.evaluate(new)
            changed = any(val[u][0] != val2[u][0] for u in range(self.n))
            stats["cyc"] += cyc; stats["cycnode_change"] += changed; stats["escape"] += (cyc and not changed)
            if trace:
                print(f"it {it}: switch {v}->{w} level {lv} {'CYC' if cyc else 'nocyc'} {'cycnode-change' if changed else ''} "
                      f"#imp {len(imp)}", file=sys.stderr)
            if hook:
                hook(it, sigma, val, tau, v, w, lv, cyc, changed)
            sigma = new; it += 1
            if cap and it > cap:
                raise RuntimeError("cap")

    def regions(self, sigma):
        val, tau = self.evaluate(sigma)
        win = [self.par[val[v][0]] for v in range(self.n)]
        strat = [None] * self.n
        for v in range(self.n):
            if self.owner[v] == EVEN and win[v] == EVEN:
                strat[v] = sigma[v]
            elif self.owner[v] == ODD and win[v] == ODD:
                strat[v] = tau[v]
        return win, strat


if __name__ == "__main__":
    args = sys.argv[1:]
    start = "best"; trace = False
    if "--start" in args:
        i = args.index("--start"); start = args[i + 1]; del args[i:i + 2]
    if "--trace" in args:
        trace = True; args.remove("--trace")
    rule, path = args[0], args[1]
    e = VJ(*read_pg(path))
    sigma, it, stats = e.run(rule, e.initial(start), trace)
    win, strat = e.regions(sigma)
    print(f"solved with {it} iterations, {e.evals} evaluations; cycle-creating {stats['cyc']}, escapes {stats['escape']}, "
          f"cycle-node changes {stats['cycnode_change']}", file=sys.stderr)
    print(f"paritysol {e.n};\n" + "".join(f"{v} {w}{'' if strat[v] is None else ' ' + str(strat[v])};\n" for v, w in enumerate(win)), end="")
