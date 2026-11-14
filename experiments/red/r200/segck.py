#!/usr/bin/env python3
"""L-RED R202 SEGCK: empirical check of L-NEW box 158 SEG-CAP on IDEAL-ACYC runs (r187/ideal.py): on a 2-wide degree-2 ladder with
d levels (R197 convention), each segment (nonempty steps before / between / after the level-0 steps) has length <= T*(d-1), with the
exact maxima T*(1..4) = 2, 4, 8, 13 (R188 / R197 / R202 validation). Inputs: given genome files, plus random ladders (acyclic Xi, random
ranks / parities / gates / starts). Usage: segck.py count seed [genome.json ...]"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
TS = {1: 2, 2: 4, 3: 8, 4: 13}
def segs(G):
    S, why = ideal.traj(G); lev = G["lev"]
    z = [u for u in range(1, len(S)) if any(S[u][v] != S[u - 1][v] for v in range(G["N"]) if lev[v] == 0)]
    cuts = [0] + z + [len(S)]; return len(S) - 1, z, [cuts[i + 1] - cuts[i] - 1 for i in range(len(cuts) - 1)]
def rnd(R, d):
    N = 2 * d; lev = [v // 2 for v in range(N)]; perm = list(range(N)); R.shuffle(perm); pos = {v: i for i, v in enumerate(perm)}
    g = list(range(2 * N)); R.shuffle(g); rk = list(range(2 * N)); R.shuffle(rk); opts = []
    for v in range(N):
        later = [u for u in range(N) if pos[u] > pos[v]]
        opts.append([[(2 * (lev[v] - 1) + k) if lev[v] > 0 else -1, R.choice([-1] + later), 2 * v + k] for k in (0, 1)])
    return dict(N=N, lev=lev, deg=2, opts=opts, gate=[[g[2 * v], g[2 * v + 1]] for v in range(N)], br=rk, bp=[R.randint(0, 1) for _ in range(2 * N)],
                start=[R.randint(0, 1) for _ in range(N)])
cnt, seed = int(sys.argv[1]), int(sys.argv[2]); R = random.Random(seed); viol = 0; n = 0; best = {}
gens = [(f, json.load(open(f))) for f in sys.argv[3:]] + [(f"rand{i}", rnd(R, R.choice([2, 3, 4, 5]))) for i in range(cnt)]
for name, G in gens:
    d = max(G["lev"]) + 1
    if d - 1 not in TS: continue
    L, z, sg = segs(G); n += 1; cap = TS[d - 1]
    best[d] = max(best.get(d, 0), max(sg))
    if max(sg) > cap or len(z) > 2: viol += 1; print("VIOLATION", name, "d", d, "L", L, "level-0 steps", z, "segments", sg, "cap", cap)
print(f"SEGCK runs {n} violations {viol} max segment by d {dict(sorted(best.items()))} (caps T*(d-1) {TS})")
