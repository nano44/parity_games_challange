#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): hill climb toward first differences at search_rec depth >= 1 (ctxfit.py rule, L-ALG
tools UNMODIFIED). Fitness (lexicographic): e* at depth >= 1, distinct first-difference contexts (max over phases),
transitions. Mutations: one priority, one owner, add an edge, remove an edge (keeping a successor), add a vertex.
Equal-fitness moves are accepted (plateau walk). Usage: deepclimb.py SEED.pg RNGSEED STEPS NMAX OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ctxfit as CF, pg
src, seed, steps, nmax, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed); os.makedirs(out, exist_ok=True)
def fit(g):
    try: tr, cx, deep = CF.summary(CF.run(g)); return (deep, cx, tr)
    except RecursionError: return (-1, 0, 0)
def mutate(g):
    pr, ow, su = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = len(pr); k = rng.randrange(5 if n < nmax else 4)
    v = rng.randrange(n)
    if k == 0: pr[v] = rng.randint(0, max(pr) + 2)
    elif k == 1: ow[v] ^= 1
    elif k == 2: w = rng.randrange(n); su[v] = sorted(set(su[v] + [w]))
    elif k == 3:
        if len(su[v]) > 1: su[v].remove(rng.choice(su[v]))
    else:
        pr.append(rng.randint(0, max(pr) + 2)); ow.append(rng.randint(0, 1)); su.append(sorted(set(rng.randrange(n + 1) for _ in range(2))))
        u = rng.randrange(n); su[u] = sorted(set(su[u] + [n]))
    return pg.Game(pr, ow, su)
g = pg.read(src); f = fit(g); best = f; print("start", f, flush=True)
for it in range(steps):
    h = mutate(g); fh = fit(h)
    if fh >= f:
        g, f = h, fh
        if f > best:
            best = f; p = os.path.join(out, f"dc_s{seed}_it{it}_n{g.n}_deep{f[0]}_cx{f[1]}_tr{f[2]}.pg"); pg.write(g, p); print(it, f, p, flush=True)
print("done best", best)
