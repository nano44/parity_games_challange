#!/usr/bin/env python3
"""L-SI box 53 §6: own-cycle-node sbar-flips (XCN) per W-run. xcn.py GAME.pg [START]: XCN_TR (most XCN transitions in one W-run), XCN_V (most at one vertex), XCN_RUN_ALL (whole run). xcnrs.py SEED COUNT N DMAX BIAS: random search for the most XCN transitions in one W-run."""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "new", "box21"))
from n5x import step, start_pair, Engine, dual
import pg
seed, cnt, N, D, B = map(int, sys.argv[1:6]); rng = random.Random(seed); best = (0, None)
for i in range(cnt):
    n = N; own = [rng.randint(0, 1) for _ in range(n)]; pr = [rng.randint(0, n) for _ in range(n)]
    if B: own[0] = 1; pr[0] = (max(pr) + 1) | 1
    succ = [rng.sample(range(n), rng.randint(1, D)) for _ in range(n)]; g = pg.Game(pr, own, succ)
    E, Ed = Engine(g), Engine(dual(g))
    st = ({v: rng.choice(succ[v]) for v in range(n) if own[v] == 0}, {v: rng.choice(succ[v]) for v in range(n) if own[v] == 1})
    s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
    while len(S) < 300:
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
    EV = [E.evaluate(x) for x in S]; Wc = {}
    def Wv(k, tau):
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(pr), list(own), [[tau[v]] if own[v] == 1 else succ[v] for v in range(n)]))
        return Wc[tau].evaluate(S[k])[0]
    run = 0
    for k in range(len(S) - 1):
        ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
        if not ok: run = 0; continue
        if any(EV[k][1][o] != EV[k + 1][1][o] and (EV[k][0][o][0] == o or EV[k + 1][0][o][0] == o) for o in range(n) if own[o] == 1):
            run += 1
            if run > best[0]: best = (run, (pr, own, succ, st))
print("XCNRS seed", seed, "n", N, "best", best[0], best[1] if best[0] >= 3 else "")
