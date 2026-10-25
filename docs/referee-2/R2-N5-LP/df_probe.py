#!/usr/bin/env python3
"""REFEREE-2: Lemma DF of P-N5-LP §3 as stated. On C^1O, at every in-phase S4a transition (no fallback) k -> k+1, every arena edge (y, z)
(z in {sigma_k(y)} u Is_k(y)) that is a gate edge at k+1 must have a := sigma_{k+1}(y) in R_{k+1}. Records every failure with whether y is
its own cycle node (lambda(y) = y) and whether the gate edge at k+1 is length-only (lev = -1). Own code on fb_check (SPEC run asserted =
n5.run). Usage: df_probe.py N nmin nmax seed [inst.pg ...]"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-FB"))
import fb_check as F
RC = F.RC
c = Counter(); ex = []
def scan(g, s, t, name):
    o = F.one_odd(g)
    states, fbs, E, Ed = F.run_n5(g, s, t)
    A = [F.analyse(g, E, Ed, a, b, o) for a, b in states]
    for k in range(len(fbs)):
        if fbs[k]: continue
        if not (A[k].lam == A[k + 1].lam and A[k].lamU == A[k + 1].lamU and states[k][1] == states[k + 1][1]): continue
        s0, s1 = states[k][0], states[k + 1][0]
        for y in range(g.n):
            if g.owner[y] != 0: continue
            arena = {s0[y]} | {z for (x, z) in A[k].Is if x == y}
            a = s1[y]
            for z in arena:
                if (y, z) not in A[k + 1].gl: continue
                c["DF_checks"] += 1
                if a not in A[k + 1].Rbar:
                    own = A[k + 1].lam[y] == y; lv = A[k + 1].gl[(y, z)]
                    c[f"DF_FAIL own_cycle_node={own} level={'-1' if lv == -1 else ('inf' if lv >= F.INF else '>=0')}"] += 1
                    if len(ex) < 5: ex.append((name, k, y, a, z, own, lv, A[k + 1].Xi[a], A[k + 1].Xi[z]))
                    if not own: c["DF_FAIL_not_own_cycle_node"] += 1
                else: c["DF_ok"] += 1
N, nmin, nmax, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
for i in range(N):
    rg, o = RC.rand_game(rng, rng.randint(nmin, nmax)); g = F.to_lpg(rg)
    s, t = F.start(g, rng, rng.random() < 0.6); scan(g, s, t, f"r{seed}#{i}")
for p in sys.argv[5:]:
    import pg as lpg
    g = lpg.parse("".join(l for l in open(p) if not l.lstrip().startswith("%")))
    try: F.one_odd(g)
    except AssertionError: continue
    r2 = random.Random(5)
    for r in range(5): s, t = F.start(g, r2, r > 0); scan(g, s, t, os.path.basename(p) + f"#{r}")
for k in sorted(c): print(k, c[k])
for e in ex: print("EXAMPLE", e)
