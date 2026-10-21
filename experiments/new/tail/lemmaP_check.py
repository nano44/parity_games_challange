#!/usr/bin/env python3
"""Box 10 (ii): computer check of Lemma P (phase progress) for switch-best on ONE-PLAYER games (Odd out-degree 1), VJ00 valuations (L-SI's
engine, read-only). Lemma P: within a lambda-phase (no vertex changes its cycle node during steps 1..k), for every vertex x, every cycle
node u of rho_0 and every SIMPLE path r from x to u with at most k edges: Omega_k(x) >= value(r) := (u, P(r), |r|), P(r) = vertices of r
(u excluded) more relevant than u. Corollary checked too: a lambda-phase has at most n steps. Random games + random starts; DFS over simple
paths (n <= nmax small). Usage: lemmaP_check.py games seed nmax"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine
from phase_trace import sbstep
INST = sys.argv[1] == "inst"
if INST: games, seed, nmax = len(sys.argv) - 2, 0, 0
else: games, seed, nmax = map(int, sys.argv[1:4])
rng = random.Random(seed)
viol = 0; checks = 0; maxphase = (0, 0); runs = 0; stuckflat = 0
for gi in range(games):
    if INST:
        path = sys.argv[2 + gi]; g = pg.read(path); n = g.n; owner, succ = g.owner, g.succ
        s0 = [g.succ[v][0] if owner[v] == 0 else -1 for v in range(n)]
        if os.path.exists(path + ".start"):
            for tok in open(path + ".start").readline().split()[1:]: a, b = map(int, tok.split(":")); s0[a] = b
        print("instance", os.path.basename(path), "n", n, flush=True)
    else:
        n = rng.randint(3, nmax); owner = [0 if rng.random() < 0.75 else 1 for _ in range(n)]; pr = rng.sample(range(2 * n), n)
        succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
        g = pg.Game(pr, owner, succ)
    E = Engine(g)
    rank = E.rank
    def value_of_path(path, u):   # path = [x, ..., last before u]; path set = bitmask over ranks of the vertices more relevant than u
        P = 0
        for v in path:
            if rank[v] > rank[u]: P |= E.bit[v]
        return (u, P, len(path))
    for rep in range(1 if INST else 2):
        s = list(s0) if INST else [rng.choice(succ[v]) if owner[v] == 0 else -1 for v in range(n)]; runs += 1
        vs0, _ = E.evaluate(tuple(s)); lam0 = tuple(vs0[v][0] for v in range(n)); cycnodes = sorted(set(lam0))
        # all simple paths from x to u, by length: paths[u][x][L] = list of P-values (as values) -- enumerate via DFS
        best = {}   # (u, x, L) -> best value of a simple path with exactly L edges
        def dfs(x, path, seen, u=None):
                if u is None: u = dfs_u[0]
                if x == u and path:
                    val = value_of_path(path, u); key = (u, path[0], len(path))
                    if key not in best or E.key(val) > E.key(best[key]): best[key] = val
                    return
                if x == u and not path: pass
                for w in g.succ[x]:
                    if w == u:
                        val = value_of_path(path + [x], u); key = (u, path[0] if path else x, len(path) + 1)
                        if key not in best or E.key(val) > E.key(best[key]): best[key] = val
                    elif w not in seen: dfs(w, path + [x], seen | {w}, u)
        dfs_u = [None]
        for u in cycnodes:
            dfs_u[0] = u
            for x in range(n):
                if x != u: dfs(x, [], {x}, u)
        k = 0; cur = list(s); inphase = True
        while True:
            vs, _ = E.evaluate(tuple(cur)); lam = tuple(vs[v][0] for v in range(n))
            if lam != lam0:      # new phase: restart the table from the current strategy (every phase is checked)
                lam0 = lam; cycnodes = sorted(set(lam0)); best = {}; k = 0
                for u in cycnodes:
                    dfs_u[0] = u
                    for x in range(n):
                        if x != u: dfs(x, [], {x}, u)
            if inphase:
                maxphase = max(maxphase, (k, n)) if k > maxphase[0] else maxphase
                if k > n: print("PHASE LONGER THAN n:", n, k, g.prio, g.owner, g.succ, s); viol += 1
                for u in cycnodes:
                    for x in range(n):
                        for L in range(1, k + 1):
                            if (u, x, L) in best:
                                checks += 1
                                if E.key(vs[x]) < E.key(best[(u, x, L)]):
                                    viol += 1; print("VIOLATION", dict(n=n, k=k, x=x, u=u, L=L, omega=vs[x], path_value=best[(u, x, L)], prio=g.prio, owner=g.owner, succ=g.succ, start=s))
            ns, _, _ = sbstep(g, E, cur)
            if ns is None: break
            if ns == cur: stuckflat += 1; break
            cur = ns; k += 1
print(f"games={games} runs={runs} nmax={nmax} Lemma-P checks={checks} violations={viol}; longest phase {maxphase[0]} steps at n={maxphase[1]}; runs stopped by a no-change step {stuckflat}")
