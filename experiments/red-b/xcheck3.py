#!/usr/bin/env python3
"""Validation of eng3.py: (1) best_reply3's values equal the pointwise minimum over ALL positional Odd strategies (brute3)
at every state of HOW3 on small random genomes; (2) PAD (c) of P-N5-REACH par. 5: for every vertex of Gamma, the Gamma3 value
has the cycle node and P-set of the Gamma value under the transported pair (eng.py's IDEAL-CYC run is NOT the same run, so (2)
is checked at the start state only, with Odd's choices transported). Usage: xcheck3.py SEED COUNT [Nmax]."""
import sys, random, eng, eng3, gen
seed, cnt = int(sys.argv[1]), int(sys.argv[2]); Nmax = int(sys.argv[3]) if len(sys.argv) > 3 else 4
rng = random.Random(seed); bad = 0; states = 0; padbad = 0; Tmax = 0
for i in range(cnt):
    G = gen.shaped(rng, rng.randint(1, Nmax), "mix"); G.pop("eorder", None)
    g = eng3.build3(G)
    if g.M + 1 > 11: continue
    h = eng3.how3_run(g, tie="rand", rng=rng)
    Tmax = max(Tmax, len(h) - 1)
    for st in h:
        states += 1
        if eng3.brute3(g, st["sig"]) != st["val"]: bad += 1
    # PAD (c) at the start state: Gamma under the same mover choice and the transported Odd choice
    g0 = eng.build(G); st = h[0]
    nx0 = [0] * g0.n
    for v in range(g0.n):
        if g0.owner[v] == 1:
            w = st["sbar"][v]
            nx0[v] = g.succ[w][0] if v != g0.K[2] else (g0.K[1] if w == g.r else g0.K[2])
        elif v < g0.N: nx0[v] = g0.succ[v][st["sig"][v]]
        else: nx0[v] = g0.succ[v][0]
    # gamma's frozen K0 -> K3, K1 -> K1 equal the transported ones; beta -> xt or K0 (via pb_g)
    val0, lam0, pim0, kk0 = eng.play_values(g0, nx0)
    for v in range(g0.n):
        if lam0[v] != st["lam"][v]: padbad += 1; continue
        # P-sets as vertex sets
        s0 = {u for u in range(g0.n) if pim0[v] >> g0.rank[u] & 1}
        s3 = {u for u in range(g.n) if st["pim"][v] >> g.rank[u] & 1}
        if s0 != s3: padbad += 1
print("xcheck3 seed", seed, "genomes", cnt, "states", states, "valfail", bad, "padfail", padbad, "Tmax", Tmax)
