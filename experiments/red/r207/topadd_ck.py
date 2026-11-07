#!/usr/bin/env python3
"""L-RED R207 TOPADD_CK: random check of Lemma TOP-ADD. Random genomes of L_d (gclimb.extend + mutations, AUX 2, WFREE) with every
lower option's Xi-target in the top level U redirected to X; compare G's run projected off U with the run of G - U (same start):
violations if the first T(G - U) projected states differ, or T(G) > T(G - U) + #two-option movers of U. Usage: topadd_ck.py d n seed"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
os.environ.setdefault("AUX", "2"); os.environ.setdefault("WFREE", "1")
import gclimb, ideal
d, n, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
base = json.load(open(os.path.join(H, "..", "r197", "lag", "max_d4_L13.json"))); viol = 0; gains = {}
for i in range(n):
    G = gclimb.extend(base, d, rng)
    for _ in range(rng.randrange(20, 200)): G = gclimb.mutate(G, rng)
    U = {v for v in range(G["N"]) if G["lev"][v] == d - 1}
    for v in range(G["N"]):
        if v not in U:
            for o in G["opts"][v]:
                if o[1] in U: o[1] = -1
    keep = [v for v in range(G["N"]) if v not in U]; mp = {v: i for i, v in enumerate(keep)}
    H2 = dict(N=len(keep), lev=[G["lev"][v] for v in keep], gate=[G["gate"][v] for v in keep], br=G["br"], bp=G["bp"],
              start=[G["start"][v] for v in keep], opts=[[[mp[o[0]] if o[0] >= 0 else -1, mp[o[1]] if o[1] >= 0 else -1, o[2]] for o in G["opts"][v]] for v in keep])
    S, _ = ideal.traj(G); S2, _ = ideal.traj(H2); T, T2 = len(S) - 1, len(S2) - 1
    proj = all(tuple(S[t][v] for v in keep) == S2[t] for t in range(T2 + 1)) if T >= T2 else False
    two = sum(1 for v in U if len(G["opts"][v]) == 2)
    if not proj or T > T2 + two: viol += 1
    gains[T - T2] = gains.get(T - T2, 0) + 1
print(f"TOPADD_CK d {d} genomes {n} seed {seed} violations {viol} gain histogram {sorted(gains.items())}")
