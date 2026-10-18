#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): do two staircases multiply? Disjoint union of leanT(a) and leanT(b) (copy 2's priorities
shifted up by an even amount above copy 1's), plus up to K individual cross edges (copy1 <-> copy2), hill-climbed on pinned-Oink
DTL iterations (every solution must verify). Prints improvements. Usage: prodclimb.py SEED STEPS A B K OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tcpert as T, lean as LE
seed, steps, a, b, K, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
rng = random.Random(seed); os.makedirs(out, exist_ok=True); tmp = os.path.join(out, f"p{seed}.pg")
A = LE.lean(a, T.LT); B = LE.lean(b, T.LT); sh = max(v[0] for v in A) + 2; sh += sh % 2
U = [[v[0], v[1], list(v[2]), "1:" + v[3]] for v in A] + [[v[0] + sh, v[1], [w + len(A) for w in v[2]], "2:" + v[3]] for v in B]
nA = len(A); n = len(U)
def build(E):
    V = [[x[0], x[1], list(x[2]), x[3]] for x in U]
    for u, w in E:
        if w not in V[u][2]: V[u][2].append(w)
    return V
def fit(E):
    r = T.solve(build(E), tmp)
    if not r[1]: print("NOT VERIFIED", E, r, flush=True); return -1, r
    return r[0], r
E = []; f, r = fit(E); best = f; print("start", r, "a+b+2 =", a + b + 2, flush=True)
for it in range(steps):
    F = list(E); m = rng.random()
    if F and m < 0.3: F.pop(rng.randrange(len(F)))
    elif len(F) < K:
        u = rng.randrange(n); w = rng.randrange(nA, n) if u < nA else rng.randrange(nA)
        F.append((u, w))
    else: F[rng.randrange(len(F))] = (rng.randrange(nA), rng.randrange(nA, n)) if rng.random() < .5 else (rng.randrange(nA, n), rng.randrange(nA))
    g, rr = fit(F)
    if g >= f:
        E, f = F, g
        if f > best: best = f; print(it, rr, [(U[u][3], U[w][3]) for u, w in E], flush=True)
print("done best", best)
