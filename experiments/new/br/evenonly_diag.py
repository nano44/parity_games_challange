#!/usr/bin/env python3
"""Box 11 (b) test bed: EVEN-ONLY runs of N5 (Odd never moves, so tau is fixed and every iteration is Even's optimum in G_tau over the honestly
gated arena). Per iteration: V-improving edges (V = profile valuation V_{sigma,tau} in G_tau, one-player for Even) that are NOT honest-improving
(masked by the gate), honest-improving edges that are NOT V-improving (lures), honest-improving edges not taken (stalls), and whether the
Lemma-P statement holds in the V valuation (after k moves, V_k(x) >= best simple path of <= k edges in G_tau to any cycle node of V_0) and in
the honest valuation. Asserts the run is Even-only. Usage: evenonly_diag.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step, play_val
from n5 import pg, Engine, dual
g = pg.read(sys.argv[1]); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
V0 = [v for v in range(g.n) if g.owner[v] == 0]
succT = [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)]
def best_paths(cyc):
    best = {}
    for u in cyc:
        def dfs(x, path, seen):
            for w in succT[x]:
                if w == u:
                    P = 0
                    for v in path + [x]:
                        if E.rank[v] > E.rank[u]: P |= E.bit[v]
                    val = (u, P, len(path) + 1); key = (u, path[0] if path else x, len(path) + 1)
                    if key not in best or E.key(val) > E.key(best[key]): best[key] = val
                elif w not in seen and len(path) < g.n: dfs(w, path + [x], seen | {w})
        for x in range(g.n):
            if x != u: dfs(x, [], {x})
    return best
V = play_val(E, g, s, t); lam0 = tuple(V[v][0] for v in range(g.n)); cyc = sorted(set(lam0)); best = best_paths(cyc)
k = 0; totm = totl = tots = 0; violV = violX = 0; checks = 0
while True:
    vs, sbar = E.evaluate(tuple(s)); Is = set(E.improving(tuple(s), vs)); V = play_val(E, g, s, t)
    Vimp = {(x, w) for x in V0 for w in g.succ[x] if w != s[x] and E.key(V[w]) > E.key(V[s[x]])}
    masked = Vimp - Is; lures = Is - Vimp
    lam = tuple(V[v][0] for v in range(g.n))
    if lam == lam0:
        for u in cyc:
            for x in range(g.n):
                for L in range(1, k + 1):
                    if (u, x, L) in best:
                        checks += 1
                        if E.key(V[x]) < E.key(best[(u, x, L)]): violV += 1
                        if E.key(vs[x]) < E.key(best[(u, x, L)]): violX += 1
    r = step(g, E, Ed, s, t)
    if r is None: break
    assert r[1] == t, "Odd moved: not an Even-only run"
    stalls = sorted({x for (x, w) in Is if r[0][x] == s[x]})
    totm += len(masked); totl += len(lures); tots += len(stalls)
    print(f"it {k}: moves {sum(1 for x in V0 if r[0][x] != s[x])} | V-improving {len(Vimp)}, honest-improving {len(Is)}, masked (V not honest) {len(masked)}, lures (honest not V) {len(lures)}, stalled {stalls} {'fb' if r[2] else ''} | λ(V) changed: {lam != lam0}")
    s = r[0]; k += 1
print(f"{os.path.basename(sys.argv[1])} n={g.n} iterations={k} Even-only OK; totals masked {totm}, lures {totl}, stalls {tots}; Lemma-P-in-V checks {checks} violations {violV}; in honest Ξσ violations {violX}")
