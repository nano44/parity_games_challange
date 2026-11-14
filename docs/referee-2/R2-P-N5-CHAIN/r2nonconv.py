#!/usr/bin/env python3
"""REFEREE-2 successor 35: print one witness of W-1 (class (K1, ∅) is not a convex set of values over ALL vertices of Γ3): on the S3
state of the first --gen genome that has one. Own code on r2end.py. Usage: r2nonconv.py COUNT SEED KIND"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-P-N5-END"))
import r2end as R
cnt, seed, kind = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
for j in range(cnt):
    G = R.gen(rng, kind); g = R.build(G, "lev"); n, pr, ow, E, V = g["n"], g["pr"], g["ow"], g["E"], g["V"]
    od = R.Order(pr); st = R.s3(g); sig = [st[v] if ow[v] == 0 else None for v in range(n)]
    val, sbar = R.s1(pr, ow, E, sig, od); inv = {i: k for k, i in V.items()}
    evs = {V[("e", o)] for o in g["O"]}; K1 = V["K1"]
    a0 = [v for v in range(n) if val[v][0] == K1 and not (val[v][1] & evs)]
    a1 = [v for v in range(n) if val[v][0] == K1 and (val[v][1] & evs)]
    for x in a0:
        for y in a1:
            for z in a0:
                if od.cmp(val[x], val[y]) < 0 and od.cmp(val[y], val[z]) < 0:
                    nm = lambda v: f"{inv[v]} (Λ {inv[val[v][0]]}, Π {sorted(str(inv[u]) for u in val[v][1])}, k {val[v][2]})"
                    print(f"genome #{j}, S3 state:\n  {nm(x)}\n  ◁ {nm(y)}\n  ◁ {nm(z)}"); sys.exit(0)
print("none")
