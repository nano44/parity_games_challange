#!/usr/bin/env python3
"""REFEREE-2 succ. 15 (§C): count STAU-1 case (ii) on my inputs: states with Isigma = {}, Itau != {}, tau value-optimal in H', SPEC's S4b
output != tau (N5 moves to SPEC's tau', N5^tau keeps tau in S4b^tau and Odd falls back), over the states of both runs; and whether the two
successor states differ. Usage: is0_count.py random N nmin nmax seed kind k | files list runs"""
import sys, os, random
import stau_check as S
a = sys.argv[1:]; c = {"states": 0, "IS0_DIV": 0, "IS0_DIV_diff_next": 0}
def visit(g, s, t):
    for keep in (False, True):
        states, _, _ = S.run(g, s, t, S.Stats(), "x", keep)
        for sg, tu in states:
            A = S.step(g, list(sg), list(tu), False); B = S.step(g, list(sg), list(tu), True)
            if A is None: continue
            c["states"] += 1; i = A[3]
            if not i["Is"] and i["It"] and i["tau_opt"] and list(i["s4b_spec"]) != list(tu):
                c["IS0_DIV"] += 1
                if (A[0], A[1]) != (B[0], B[1]): c["IS0_DIV_diff_next"] += 1
if a[0] == "random":
    N, lo, hi, seed = map(int, a[1:5]); kind = a[5]; k = int(a[6]); rng = random.Random(seed)
    for _ in range(N):
        g = S.DC.rand_game(rng, rng.randint(lo, hi), kind)
        for r in range(k + 1):
            s, t = S.starts(g, r, rng); visit(g, s, t)
else:
    rng = random.Random(7)
    for p in [l.strip() for l in open(a[1]) if l.strip()]:
        g = S.pg.read(os.path.join(S.DC.ROOT, p))
        if g.n > 64: continue
        for r in range(int(a[2])):
            s, t = S.starts(g, r, rng); visit(g, s, t)
print("MODE", " ".join(a), c)
