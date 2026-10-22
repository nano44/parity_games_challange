#!/usr/bin/env python3
"""REFEREE-2 (Fable 5.1) own mechanical check of docs/new/N5-phase-bound-box10.md (packet P-N5-1P, trunk 26905f0).
Written from the definitions only (VJ00 BRICS RS-00-48 section 4 play values and order; the spec's rank/p' injectivity);
does not import n5.py, si.py or any L-NEW script.

One-player game H: every Odd vertex has out-degree 1, so a strategy rho (one successor per vertex) fixes every play.
  value(rho, x) = (c, P, l): c = most relevant vertex of the cycle the play from x ends in, P = vertices before c more
  relevant than c, l = number of edges from x to c.  Order (better for Even): reward(c) = p'(c) if even else -p'(c);
  then P by the most relevant vertex of the symmetric difference (even in the bigger set, or odd in the smaller set, is
  better); then l (longer better iff c odd).
Switch-best: rho_{k+1} = a pointwise-optimal strategy of the arena {rho_k(x)} u I_k(x).  The arena optimum is computed
  (a) as the pointwise maximum over ALL plays of the arena (DFS over simple paths), then realised by the argmax rule
      rho*(x) = argmax_z best(z) and VERIFIED to attain the maximum at every vertex (this is fact (F1)); and
  (b) for small arenas also by brute force over every strategy of the arena (cross-check of (a)).
Checks on every run: (F1), (F2), the phase structure (Theorem PH), Lemma P at every in-phase step of every phase, the
  "lambda-changing or flat" property of improving edges after n-1 in-phase steps, and the N5 fallback situation.
Usage: sb1p.py random N_GAMES NMAX [seed] [tiebreak]     |  sb1p.py inst game.pg [game.pg.start] [tiebreak]
  tiebreak in keep|change|rand|first (which optimal arena strategy is taken when several attain the maximum)."""
import sys, random, itertools, time

BUDGET = 3_000_000   # DFS node budget per enumeration (Lemma P path tables and play enumeration); exceeded -> SKIPPED


class Game:
    def __init__(self, prio, owner, succ):
        self.n = n = len(prio)
        self.prio, self.owner = list(prio), list(owner)
        self.succ = [sorted(set(s)) for s in succ]
        for v in range(n):
            assert self.succ[v], f"vertex {v} without successor"
            if self.owner[v] == 1:
                assert len(self.succ[v]) == 1, f"Odd vertex {v} has out-degree {len(self.succ[v])}: not one-player"
        order = sorted(range(n), key=lambda v: (self.prio[v], v))
        self.rank = [0] * n
        for r, v in enumerate(order):
            self.rank[v] = r
        self.par = [p % 2 for p in self.prio]
        self.pp = [2 * self.rank[v] + self.par[v] for v in range(n)]
        self.rew = [self.pp[v] if self.par[v] == 0 else -self.pp[v] for v in range(n)]
        self.m = sum(len(s) for s in self.succ)
        self.sumdeg1 = sum(len(s) - 1 for s in self.succ)

    # ---- values and order ----------------------------------------------------------------------------------
    def value(self, rho, x):
        seq, pos, v = [], {}, x
        while v not in pos:
            pos[v] = len(seq); seq.append(v); v = rho[v]
        cyc = seq[pos[v]:]
        c = max(cyc, key=lambda u: self.rank[u])
        k = pos[c]
        P = frozenset(u for u in seq[:k] if self.rank[u] > self.rank[c])
        return (c, P, k)

    def omega(self, rho):
        return [self.value(rho, x) for x in range(self.n)]

    def setcmp(self, A, B):
        """-1 if A < B (B better for Even), 0 if equal, +1 if A > B; by the most relevant vertex of the difference."""
        if A == B:
            return 0
        t = max(A ^ B, key=lambda u: self.rank[u])
        if t in B:
            return -1 if self.par[t] == 0 else 1
        return 1 if self.par[t] == 0 else -1

    def setkey(self, P):
        return sum((1 << self.rank[u]) if self.par[u] == 0 else -(1 << self.rank[u]) for u in P)

    def key(self, val):
        c, P, l = val
        return (self.rew[c], self.setkey(P), l if self.par[c] == 1 else -l)

    def cmp(self, a, b):
        """Direct comparison without the weight encoding (used to self-test key())."""
        ca, Pa, la = a; cb, Pb, lb = b
        if ca != cb:
            return -1 if self.rew[ca] < self.rew[cb] else 1
        s = self.setcmp(Pa, Pb)
        if s:
            return s
        if la == lb:
            return 0
        if self.par[ca] == 1:
            return -1 if la < lb else 1
        return -1 if la > lb else 1

    def prefix(self, x, val):
        """x (+) (c, P, l) := (c, P u {x if x more relevant than c}, l + 1)."""
        c, P, l = val
        return (c, P | {x} if self.rank[x] > self.rank[c] else P, l + 1)

    def improving(self, rho, Om):
        I = {}
        for x in range(self.n):
            if self.owner[x] == 0:
                kc = self.key(Om[rho[x]])
                zs = [z for z in self.succ[x] if z != rho[x] and self.key(Om[z]) > kc]
                if zs:
                    I[x] = zs
        return I

    # ---- arena optimum ----------------------------------------------------------------------------------------
    def best_plays(self, opts):
        """Pointwise maximum over all plays of the arena opts (DFS over simple paths from each vertex)."""
        n = self.n
        best = [None] * n
        nodes = 0
        for x in range(n):
            seq, pos = [x], {x: 0}
            # iterative DFS: stack of (vertex, iterator over its options)
            stack = [iter(opts[x])]
            while stack:
                nodes += 1
                if nodes > BUDGET:
                    return None
                it = stack[-1]
                z = next(it, None)
                if z is None:
                    stack.pop(); v = seq.pop(); del pos[v]
                    continue
                if z in pos:   # play closes
                    cyc = seq[pos[z]:]
                    c = max(cyc, key=lambda u: self.rank[u]); k = pos[c]
                    val = (c, frozenset(u for u in seq[:k] if self.rank[u] > self.rank[c]), k)
                    if best[x] is None or self.key(val) > self.key(best[x]):
                        best[x] = val
                else:
                    pos[z] = len(seq); seq.append(z); stack.append(iter(opts[z]))
        return best

    def brute_opt(self, opts, cap=200_000):
        """Brute force over every strategy of the arena: pointwise max of values, and whether one strategy attains it."""
        total = 1
        for o in opts:
            total *= len(o)
            if total > cap:
                return None
        pmax = [None] * self.n
        vals = []
        for rho in itertools.product(*opts):
            Om = self.omega(rho)
            vals.append((rho, Om))
            for x in range(self.n):
                if pmax[x] is None or self.key(Om[x]) > self.key(pmax[x]):
                    pmax[x] = Om[x]
        attained = [rho for rho, Om in vals if all(self.key(Om[x]) == self.key(pmax[x]) for x in range(self.n))]
        return pmax, attained, total


def read_pg(path):
    prio, owner, succ = {}, {}, {}
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("%") or line.startswith("parity") or line.startswith("start"):
            continue
        line = line.rstrip(";")
        if '"' in line:
            line = line[:line.index('"')]
        parts = line.split()
        v, p, o = int(parts[0]), int(parts[1]), int(parts[2])
        prio[v], owner[v] = p, o
        succ[v] = [int(t) for t in parts[3].split(",")]
    n = len(prio)
    assert sorted(prio) == list(range(n))
    return Game([prio[v] for v in range(n)], [owner[v] for v in range(n)], [succ[v] for v in range(n)])


def read_start(path, g):
    rho = None
    for line in open(path):
        if line.startswith("SIGMA0"):
            rho = [None] * g.n
            for tok in line.split()[1:]:
                v, w = map(int, tok.split(":")); rho[v] = w
    for v in range(g.n):
        if rho[v] is None:
            assert g.owner[v] == 1 or len(g.succ[v]) == 1, f"no start for Even vertex {v}"
            rho[v] = g.succ[v][0]
    return rho


class Stats:
    def __init__(self):
        self.d = {}
        self.viol = []
    def inc(self, k, by=1):
        self.d[k] = self.d.get(k, 0) + by
    def mx(self, k, val):
        self.d[k] = max(self.d.get(k, 0), val)
    def bad(self, msg):
        self.viol.append(msg); self.inc("VIOLATIONS")


def arena_opts(g, rho, I):
    return [([rho[x]] + I[x]) if (g.owner[x] == 0 and x in I) else [rho[x]] for x in range(g.n)]


def choose(g, rho, opts, best, tb, rng):
    """The dual of VJ00's counter-strategy rule: rho*(x) = an argmax over x's options of best(z)."""
    new = []
    for x in range(g.n):
        mk = max(g.key(best[z]) for z in opts[x])
        cands = [z for z in opts[x] if g.key(best[z]) == mk]
        if tb == "keep":
            z = rho[x] if rho[x] in cands else min(cands)
        elif tb == "change":
            others = [z for z in cands if z != rho[x]]
            z = max(others) if others else rho[x]
        elif tb == "first":
            z = min(cands)
        else:
            z = rng.choice(cands)
        new.append(z)
    return new


def switch_best_run(g, rho0, tb, rng, st, cap=10 ** 5):
    """Returns the list of strategies rho_0, rho_1, ... and per-step kinds; applies the N5 fallback when the arena
    optimum returns rho unchanged (checks that this is the value-flat situation and that I = {} afterwards)."""
    rho = list(rho0)
    seq, kinds = [rho], []
    Om = g.omega(rho)
    while len(seq) < cap:
        I = g.improving(rho, Om)
        if not I:
            break
        opts = arena_opts(g, rho, I)
        best = g.best_plays(opts)
        if best is None:
            st.inc("SKIPPED_best_plays_budget"); return seq, kinds, "budget"
        # (F2): rho is in the arena, so the arena maximum dominates Om
        for x in range(g.n):
            if g.key(best[x]) < g.key(Om[x]):
                st.bad(f"(F2) fails at x={x}")
        # brute-force cross-check of the pointwise maximum and of its attainability
        bf = g.brute_opt(opts)
        if bf is not None:
            pmax, attained, total = bf
            st.inc("bruteforce_arenas"); st.inc("bruteforce_strategies", total)
            if any(g.key(pmax[x]) != g.key(best[x]) for x in range(g.n)):
                st.bad("brute-force pointwise max differs from play enumeration")
            if not attained:
                st.bad("(F1) FAILS: no arena strategy attains the pointwise maximum")
        # value-flat situation (every arena strategy has rho's values): Corollary 2's claims, whatever the tie-break does
        if all(g.key(best[x]) == g.key(Om[x]) for x in range(g.n)):
            st.inc("flat_situations")
            for x, zs in I.items():
                if Om[x][0] != x:
                    st.bad(f"flat situation: improving edge at x={x} which is not its own cycle node")
                for z in zs:
                    hat = list(rho); hat[x] = z
                    if g.omega(hat) != Om:
                        st.bad(f"flat situation: single switch ({x},{z}) is not value-flat")
            fb = list(rho)
            for x, zs in I.items():
                fb[x] = max(zs, key=lambda z: (g.key(Om[z]), z))
            Om3 = g.omega(fb)
            if Om3 != Om or g.improving(fb, Om3):
                st.bad("flat situation: the S4c fallback changes values or leaves improving edges")
        new = choose(g, rho, opts, best, tb, rng)
        Om2 = g.omega(new)
        st.inc("F1_argmax_checks")
        if any(g.key(Om2[x]) != g.key(best[x]) for x in range(g.n)):
            st.bad("(F1) argmax strategy does not attain the pointwise maximum")
            # fall back to a brute-force maximiser if one exists
            if bf is not None and bf[1]:
                new = list(bf[1][0]); Om2 = g.omega(new)
        if new == rho:
            # N5 fallback situation (S4c): the optimum returned rho although I != {}
            st.inc("fallback_events")
            for x, zs in I.items():
                # every improving edge must be a flat cycle-closer at an own cycle node (Corollary 2's claim)
                if Om[x][0] != x:
                    st.bad(f"fallback: improving edge at x={x} which is not its own cycle node")
                for z in zs:
                    hat = list(rho); hat[x] = z
                    if g.omega(hat) != Om:
                        st.bad(f"fallback: single switch ({x},{z}) is not value-flat")
            fb = list(rho)
            for x, zs in I.items():
                fb[x] = max(zs, key=lambda z: (g.key(Om[z]), z))
            Om3 = g.omega(fb)
            if Om3 != Om:
                st.bad("fallback: values changed")
            if g.improving(fb, Om3):
                st.bad("fallback: improving edges remain after the fallback")
            seq.append(fb); kinds.append("fallback")
            rho, Om = fb, Om3
            continue
        lam_change = any(Om2[x][0] != Om[x][0] for x in range(g.n))
        kinds.append("lambda" if lam_change else ("vc" if Om2 != Om else "flat"))
        seq.append(new)
        rho, Om = new, Om2
    return seq, kinds, "ok"


def path_table(g, x, u, kmax):
    """best[k] = best value(r) over simple paths r from x to u with exactly k edges (None if none), k <= kmax."""
    best = [None] * (kmax + 1)
    if x == u:
        best[0] = (u, frozenset(), 0)
    seq, pos = [x], {x: 0}
    stack = [iter(g.succ[x])]
    nodes = 0
    while stack:
        nodes += 1
        if nodes > BUDGET:
            return None
        z = next(stack[-1], None)
        if z is None:
            stack.pop(); v = seq.pop(); del pos[v]; continue
        if z in pos or len(seq) > kmax:
            continue
        if z == u:
            L = len(seq)
            P = frozenset(w for w in seq if g.rank[w] > g.rank[u])
            val = (u, P, L)
            if best[L] is None or g.key(val) > g.key(best[L]):
                best[L] = val
            continue   # a simple path ends at u (u is the last vertex)
        pos[z] = len(seq); seq.append(z); stack.append(iter(g.succ[z]))
    return best


def check_run(g, seq, kinds, st, lemmaP=True):
    n = g.n
    Oms = [g.omega(r) for r in seq]
    lams = [[o[0] for o in Om] for Om in Oms]
    # phases: maximal runs of consecutive steps with lambda unchanged (steps of kind 'lambda' separate phases)
    steps = len(kinds)
    st.inc("runs"); st.inc("steps", steps)
    st.inc("lambda_steps", kinds.count("lambda")); st.inc("flat_steps", kinds.count("flat"))
    st.inc("vc_steps", kinds.count("vc")); st.inc("fallback_steps", kinds.count("fallback"))
    # (F2) along the run
    for k in range(steps):
        for x in range(n):
            if g.key(Oms[k + 1][x]) < g.key(Oms[k][x]):
                st.bad(f"(F2) run step {k} x={x}")
        if kinds[k] == "lambda":
            for x in range(n):
                if lams[k + 1][x] != lams[k][x] and g.rew[lams[k + 1][x]] <= g.rew[lams[k][x]]:
                    st.bad(f"lambda not rising at step {k} x={x}")
    # phase boundaries
    phases = []   # (start index into seq, end index): strategies seq[a..b] with in-phase steps a..b-1
    a = 0
    for k in range(steps):
        if kinds[k] == "lambda":
            phases.append((a, k)); a = k + 1
    phases.append((a, steps))
    st.mx("max_phases_per_run", len(phases))
    if len(phases) > n * (n - 1) + 1:
        st.bad("more than n(n-1)+1 phases")
    for (a, b) in phases:
        K = b - a
        ks = kinds[a:b]
        vc = sum(1 for k in ks if k == "vc"); fl = sum(1 for k in ks if k in ("flat", "fallback"))
        st.inc("phases"); st.mx("max_inphase_steps", K); st.mx("max_vc_per_phase", vc); st.mx("max_flat_per_phase", fl)
        st.mx("max_vc_minus_n_plus_1", vc - (n - 1))
        if vc > n - 1:
            st.bad(f"phase with {vc} value-changing steps > n-1 = {n - 1}")
        if fl > g.sumdeg1:
            st.bad(f"phase with {fl} flat steps > sum(deg-1) = {g.sumdeg1}")
        for j, k in enumerate(ks):
            if j >= n - 1 and k == "vc":
                st.bad(f"value-changing in-phase step at index {j} >= n-1")
        # after n-1 in-phase steps (and in the fallback situation): every improving edge is lambda-changing or flat at an
        # own cycle node
        for j in range(K + 1):
            if j < n - 1:
                continue
            rho, Om = seq[a + j], Oms[a + j]
            for x, zs in g.improving(rho, Om).items():
                for z in zs:
                    hat = list(rho); hat[x] = z
                    v = g.value(hat, x)
                    st.inc("edge_checks_after_n-1")
                    if g.rew[v[0]] > g.rew[Om[x][0]]:
                        continue  # lambda-changing
                    if g.omega(hat) == Om and Om[x][0] == x:
                        continue  # flat at an own cycle node
                    st.bad(f"improving edge ({x},{z}) at in-phase index {j} neither lambda-changing nor flat")
        if not lemmaP:
            continue
        # Lemma P: cycle nodes of rho_0 (phase start); for every in-phase k, x and u: Om_k(x) >= best path value <= k edges
        U = sorted(set(lams[a]))
        kmax = min(K, n - 1)
        skipped = False
        for u in U:
            if lams[a][u] != u:
                st.bad(f"cycle node {u} is not its own cycle node")
            for x in range(n):
                tab = path_table(g, x, u, kmax)
                if tab is None:
                    skipped = True; break
                bestk = None
                for k in range(K + 1):
                    if k <= kmax and tab[k] is not None and (bestk is None or g.key(tab[k]) > g.key(bestk)):
                        bestk = tab[k]
                    if bestk is None:
                        continue
                    st.inc("lemmaP_checks")
                    if g.key(Oms[a + k][x]) < g.key(bestk):
                        st.bad(f"LEMMA P FAILS: phase start {a}, k={k}, x={x}, u={u}: Om={Oms[a + k][x]} < path {bestk}")
            if skipped:
                break
        if skipped:
            st.inc("lemmaP_phases_SKIPPED_budget")
        else:
            st.inc("lemmaP_phases_checked")


def rand_game(rng, n, dmax=3, p_even=0.75, prange=None):
    prio = [rng.randrange(0, prange or n) for _ in range(n)]
    owner = [0 if rng.random() < p_even else 1 for _ in range(n)]
    succ = [rng.sample(range(n), rng.randint(1, min(dmax, n))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    return Game(prio, owner, succ)


def selftest(rng):
    # key() agrees with the direct comparator on random values
    for _ in range(3000):
        g = rand_game(rng, rng.randint(2, 12))
        vs = []
        for _ in range(2):
            rho = [rng.choice(g.succ[x]) for x in range(g.n)]
            vs += g.omega(rho)
        a, b = rng.choice(vs), rng.choice(vs)
        ka, kb = g.key(a), g.key(b)
        s = (ka > kb) - (ka < kb)
        assert s == g.cmp(a, b), (a, b)
    # (V2) prefix monotonicity, on values whose sets avoid x, or with different cycle nodes
    cnt = 0
    for _ in range(3000):
        g = rand_game(rng, rng.randint(2, 10))
        rho = [rng.choice(g.succ[x]) for x in range(g.n)]
        rho2 = [rng.choice(g.succ[x]) for x in range(g.n)]
        Om, Om2 = g.omega(rho), g.omega(rho2)
        x = rng.randrange(g.n); a, b = rng.choice(Om), rng.choice(Om2)
        if a[0] != b[0] or (x not in a[1] and x not in b[1]):
            s = g.cmp(a, b); s2 = g.cmp(g.prefix(x, a), g.prefix(x, b))
            assert s == s2, (x, a, b); cnt += 1
    print(f"selftest ok (key vs direct comparator 3000; (V2) prefix monotonicity {cnt} pairs)")


def main():
    mode = sys.argv[1]
    st = Stats()
    t0 = time.time()
    if mode == "random":
        N, nmax = int(sys.argv[2]), int(sys.argv[3])
        seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
        tb = sys.argv[5] if len(sys.argv) > 5 else "keep"
        rng = random.Random(seed)
        selftest(rng)
        for i in range(N):
            n = rng.randint(2, nmax)
            g = rand_game(rng, n, dmax=rng.choice([2, 3, 4]), p_even=rng.choice([0.6, 0.8, 1.0]),
                          prange=rng.choice([n, 2 * n, 3]))
            st.inc("games")
            for start in range(2):
                rho0 = [rng.choice(g.succ[x]) for x in range(g.n)]
                seq, kinds, status = switch_best_run(g, rho0, tb, rng, st)
                if status == "ok":
                    check_run(g, seq, kinds, st)
    else:
        g = read_pg(sys.argv[2])
        tb = "keep"; rho0 = None
        for arg in sys.argv[3:]:
            if arg.endswith(".start"):
                rho0 = read_start(arg, g)
            else:
                tb = arg
        rng = random.Random(7)
        if rho0 is None:
            rho0 = [g.succ[x][0] for x in range(g.n)]
        seq, kinds, status = switch_best_run(g, rho0, tb, rng, st)
        print(f"{sys.argv[2]}: n={g.n} m={g.m} status={status} steps={len(kinds)} kinds={''.join(k[0] for k in kinds)}")
        if status == "ok":
            check_run(g, seq, kinds, st, lemmaP=True)
            # per-phase summary
            a = 0; ph = []
            for k, kd in enumerate(kinds):
                if kd == "lambda":
                    ph.append((a, k)); a = k + 1
            ph.append((a, len(kinds)))
            print("phases (in-phase steps, value-changing, flat):",
                  [(b - a, kinds[a:b].count("vc"), kinds[a:b].count("flat") + kinds[a:b].count("fallback")) for a, b in ph])
    for k in sorted(st.d):
        print(f"  {k} = {st.d[k]}")
    for v in st.viol[:20]:
        print("  VIOLATION:", v)
    print(f"RESULT violations={len(st.viol)} secs={time.time() - t0:.1f}")


if __name__ == "__main__":
    main()
