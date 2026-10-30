#!/usr/bin/env python3
"""L-NEW box 90 (CONJECTURE BIP-REL-1, strict): random search. Random games (n, out-degree 1-3, random owners / priorities) and random
start pairs; run N5 (box21/n5x.step); in every W-run (R89) and every frozen stretch (sigmabar constant), count STRICT releases of each Even
edge (late adoption of (y, z) blocked at an earlier state of the same frozen stretch). Prints the first instance with 2 strict releases of
one edge, and the max SB_F / n seen (SB_F = transitions of a W-run where sigmabar changes). Usage: relrand.py N TRIALS SEED"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import step, start_pair, Engine, dual
import pg
N, trials, seed = map(int, sys.argv[1:4]); rnd = random.Random(seed); best = 0; sbmax = (0, None); found = 0
for tr in range(trials):
    owner = [rnd.randint(0, 1) for _ in range(N)]; prio = rnd.sample(range(N), N)
    succ = [sorted(rnd.sample(range(N), rnd.randint(1, 3))) for _ in range(N)]
    g = pg.Game(prio, owner, succ); E, Ed = Engine(g), Engine(dual(g))
    st = ({v: rnd.choice(succ[v]) for v in range(N) if owner[v] == 0}, {v: rnd.choice(succ[v]) for v in range(N) if owner[v] == 1})
    s, t = start_pair(g, E, Ed, st); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
    for _ in range(20 * N * N):
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
    Wc = {}
    def W(k, tau):
        if tau not in Wc: Wc[tau] = Engine(pg.Game(prio, owner, [[tau[v]] if owner[v] == 1 else succ[v] for v in range(N)]))
        return Wc[tau].evaluate(S[k])[0]
    EV = [E.evaluate(x) for x in S]; runs = []; cur = None
    for k in range(len(S) - 1):
        ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in W(k, TAU[k])] == [x[0] for x in W(k + 1, TAU[k])]
        if not ok: cur = None; continue
        if cur is None: cur = [k, k]; runs.append(cur)
        cur[1] = k + 1
    for a, b in runs:
        sb = sum(1 for q in range(a, b) if EV[q + 1][1] != EV[q][1])
        if sb / N > sbmax[0]: sbmax = (sb / N, sb)
        blocked = set(); fz = Counter()
        for q in range(a, b):
            if q > a and EV[q][1] != EV[q - 1][1]: blocked = set(); fz = Counter()
            Wq = W(q, TAU[a]); Is = set(E.improving(S[q], EV[q][0]))
            for y in range(N):
                if owner[y]: continue
                z = S[q + 1][y]
                if z != S[q][y] and (y, z) in blocked and EV[q + 1][1] == EV[q][1]:
                    fz[(y, z)] += 1
                    if fz[(y, z)] > best: best = fz[(y, z)]
                    if fz[(y, z)] >= 2 and not found:
                        found = 1; print("STRICT-DOUBLE", (y, z), "prio", prio, "owner", owner, "succ", succ, "start", st, "run", (a, b), flush=True)
            for y in range(N):
                if owner[y]: continue
                for z in succ[y]:
                    if z != S[q][y] and E.key(Wq[z]) > E.key(Wq[S[q][y]]) and (y, z) not in Is: blocked.add((y, z))
print(f"RELRAND n {N} trials {trials} seed {seed} max-strict-per-edge {best} max SB_F/n {sbmax[0]:.2f} ({sbmax[1]})")
