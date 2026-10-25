#!/usr/bin/env python3
"""REFEREE-2: find the smallest random C^1O game whose SPEC run FROM THE S3 (best-reward) START violates Lemma DF as stated; write it
as a .pg (pgsolver format). Usage: df_find.py seed out.pg"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-FB"))
import fb_check as F
RC = F.RC
seed, out = int(sys.argv[1]), sys.argv[2]; rng = random.Random(seed); best = None
for i in range(20000):
    rg, o = RC.rand_game(rng, rng.randint(4, 10)); g = F.to_lpg(rg); F.one_odd(g)
    s, t = F.start(g, rng, False)
    states, fbs, E, Ed = F.run_n5(g, s, t)
    A = [F.analyse(g, E, Ed, a, b, o) for a, b in states]
    for k in range(len(fbs)):
        if fbs[k] or not (A[k].lam == A[k + 1].lam and A[k].lamU == A[k + 1].lamU and states[k][1] == states[k + 1][1]): continue
        for y in range(g.n):
            if g.owner[y] != 0: continue
            arena = {states[k][0][y]} | {z for (x, z) in A[k].Is if x == y}
            a = states[k + 1][0][y]
            for z in arena:
                if (y, z) in A[k + 1].gl and a not in A[k + 1].Rbar:
                    if best is None or g.n < best[0].n: best = (g, k, y, a, z, o)
    if best and best[0].n <= 5: break
g, k, y, a, z, o = best
with open(out, "w") as f:
    f.write(f"parity {g.n - 1};\n")
    for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
print("n", g.n, "o", o, "transition", k, "y", y, "a = sigma_{k+1}(y)", a, "z", z)
