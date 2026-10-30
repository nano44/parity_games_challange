#!/usr/bin/env python3
"""L-NEW box 83 (R3-POLY = R2 + Odd optimality = N5 inside a W-run, from ANY start pair): random search. For random games (n, out-degree
2-3, random owners and priorities) and random start pairs (sigma_0, tau_0), run N5 (n5x.step) and, inside each W-run (R89: tau fixed, no
S4c, lambda_W fixed), count WCH_F(e) = transitions of F changing W(e). Reports the max over all runs of max_e WCH_F(e), its ratio to n,
and the instance. Usage: r3rand.py N TRIALS SEED"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import step, start_pair, Engine, dual
import pg
n, trials, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rnd = random.Random(seed)
best = (0, None)
for tr in range(trials):
    owner = [rnd.randint(0, 1) for _ in range(n)]; prio = rnd.sample(range(n), n)
    succ = [sorted(rnd.sample(range(n), rnd.randint(1, 3))) for _ in range(n)]
    g = pg.Game(prio, owner, succ); E, Ed = Engine(g), Engine(dual(g))
    st = ({v: rnd.choice(succ[v]) for v in range(n) if owner[v] == 0}, {v: rnd.choice(succ[v]) for v in range(n) if owner[v] == 1})
    s, t = start_pair(g, E, Ed, st); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
    for _ in range(10 * n * n):
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
    Wc = {}
    def W(k, tau):
        if tau not in Wc: Wc[tau] = Engine(pg.Game(prio, owner, [[tau[v]] if owner[v] == 1 else succ[v] for v in range(n)]))
        return Wc[tau].evaluate(S[k])[0]
    cur = None; runs = []
    for k in range(len(S) - 1):
        ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in W(k, TAU[k])] == [x[0] for x in W(k + 1, TAU[k])]
        if not ok: cur = None; continue
        if cur is None: cur = [k, k]; runs.append(cur)
        cur[1] = k + 1
    for a, b in runs:
        ws = [W(x, TAU[a]) for x in range(a, b + 1)]
        m = max(sum(1 for i in range(b - a) if ws[i + 1][e] != ws[i][e]) for e in range(n))
        if m > best[0]: best = (m, (prio, owner, succ, st, b - a))
print(f"R3RAND n {n} trials {trials} seed {seed} max-WCH_F(e) {best[0]} ratio {best[0] / n:.2f} instance {best[1]}")
