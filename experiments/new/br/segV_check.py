#!/usr/bin/env python3
"""Box 11 (b): Lemma P in the V valuation along TWO-PLAYER N5 runs. V = V_{sigma,tau} (profile valuation = Even's one-player values in G_tau).
A (tau, lambda(V))-phase = maximal run of iterations with Odd's tau constant and every cycle node of V constant. Inside it Even's step is the
optimum of the honestly gated arena of G_tau; Lemma P would hold if the gate were the V-gate. Per phase: Even-moving iterations k, Lemma-P-in-V
checks (V_k(x) >= best simple path of <= k edges in G_tau to a cycle node of the phase's first V), violations, and the gate mismatch: MASKED
edges (V-improving, not honest-improving) and LURES (honest-improving, not V-improving) summed over the phase. Usage: segV_check.py game.pg [...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step, play_val
from n5 import pg, Engine, dual
TOT = [0, 0, 0, 0, 0]
for p in sys.argv[1:]:
    g = pg.read(p); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best")); V0 = [v for v in range(g.n) if g.owner[v] == 0]
    def best_paths(t, cyc):
        succT = [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)]; best = {}
        for u in cyc:
            def dfs(x, path, seen):
                for w in succT[x]:
                    if w == u:
                        P = 0
                        for v in path + [x]:
                            if E.rank[v] > E.rank[u]: P |= E.bit[v]
                        val = (u, P, len(path) + 1); key = (u, path[0] if path else x, len(path) + 1)
                        if key not in best or E.key(val) > E.key(best[key]): best[key] = val
                    elif w not in seen: dfs(w, path + [x], seen | {w})
            for x in range(g.n):
                if x != u: dfs(x, [], {x})
        return best
    key0 = None; k = 0; checks = viol = masked = lures = 0; maxk = 0; phases = 0; violphases = 0; phviol = 0
    while True:
        vs, _ = E.evaluate(tuple(s)); Is = set(E.improving(tuple(s), vs)); V = play_val(E, g, s, t); lam = tuple(V[v][0] for v in range(g.n))
        key = (tuple(t), lam)
        if key != key0:
            if key0 is not None: phases += 1; violphases += phviol > 0
            key0, k, phviol = key, 0, 0; cyc = sorted(set(lam)); best = {} if os.environ.get('FAST') == '1' else best_paths(t, cyc)
        else:
            for u in cyc:
                for x in range(g.n):
                    for L in range(1, k + 1):
                        if (u, x, L) in best:
                            checks += 1
                            if E.key(V[x]) < E.key(best[(u, x, L)]): viol += 1; phviol += 1
        Vimp = {(x, w) for x in V0 for w in g.succ[x] if w != s[x] and E.key(V[w]) > E.key(V[s[x]])}
        masked += len(Vimp - Is); lures += len(Is - Vimp)
        r = step(g, E, Ed, s, t)
        if r is None: break
        if r[0] != s: k += 1; maxk = max(maxk, k)
        s, t = r[0], r[1]
    phases += 1; violphases += phviol > 0
    print(f"{os.path.basename(p)} n={g.n} | (τ,λ(V))-phases {phases}, max Even moves in one {maxk} | Lemma-P-in-V checks {checks} violations {viol} (phases with a violation {violphases}) | masked edge-iterations {masked}, lures {lures}")
    for i, x in enumerate((checks, viol, masked, lures, maxk)): TOT[i] = TOT[i] + x if i < 4 else max(TOT[i], x)
print("TOTAL checks, violations, masked, lures, max moves:", TOT)
