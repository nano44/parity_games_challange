#!/usr/bin/env python3
"""Hill-climb on abs3 (gate problem, c1 = c2): score = W-changing steps, then steps. Usage: climb3.py N STEPS SEED"""
import random, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from abs3 import run, better
n, STEPS, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rnd = random.Random(seed); R = 4 * n + 12
def ok(I):
    G, rho, pp, th, t1, t2 = I
    allp = list(pp[:n]) + [th] + sorted(pp[n:])
    if len(set(allp)) != len(allp): return False
    if not better((t2[0], t2[1]), (t1[0], t1[1]), pp, th % 2): return False
    if any(pp[v] <= th for v in t1[0] | t2[0]): return False
    if run(G, rho, pp, th, t1, t2, cap=0)[3] in ("EXIT", "NOOPT"): pass
    return all(rho[x] in G[x] for x in range(n))
def rand():
    while True:
        G = [sorted(set(rnd.sample([y for y in range(n + 2) if y != x], rnd.randint(1, 3)))) for x in range(n)]
        pv = rnd.sample(range(2, R), n + 5); th = pv[n]
        pp = pv[:n] + pv[n + 1:]          # virtual tail vertices are indices n.. (n+3) of pp
        vv = [n + k for k in range(4)]
        t1 = (frozenset(v for v in vv[:2] if pp[v] > th), rnd.randint(1, 4)); t2 = (frozenset(v for v in vv[2:] if pp[v] > th), rnd.randint(1, 4))
        rho = [rnd.choice(G[x]) for x in range(n)]
        I = (G, rho, pp, th, t1, t2)
        if ok(I): return I
def mut(I):
    G, rho, pp, th, t1, t2 = I; G = [list(e) for e in G]; rho = list(rho); pp = list(pp)
    k = rnd.randrange(7); x = rnd.randrange(n)
    if k == 0:
        y = rnd.choice([y for y in range(n + 2) if y != x])
        if y in G[x] and len(G[x]) > 1 and rho[x] != y: G[x].remove(y)
        elif y not in G[x] and len(G[x]) < 4: G[x].append(y); G[x].sort()
    elif k == 1: rho[x] = rnd.choice(G[x])
    elif k == 2: pp[rnd.randrange(len(pp))] = rnd.randrange(2, R)
    elif k == 3: th = rnd.randrange(2, R)
    elif k == 4:
        vv = [n + q for q in range(4)]; t1 = (frozenset(v for v in vv[:2] if pp[v] > th and rnd.random() < 0.7), rnd.randint(1, 4))
    elif k == 5:
        vv = [n + q for q in range(4)]; t2 = (frozenset(v for v in vv[2:] if pp[v] > th and rnd.random() < 0.7), rnd.randint(1, 4))
    else:
        y = rnd.randrange(n); pp[x], pp[y] = pp[y], pp[x]
    t1 = (frozenset(v for v in t1[0] if pp[v] > th), t1[1]); t2 = (frozenset(v for v in t2[0] if pp[v] > th), t2[1])
    return (G, rho, pp, th, t1, t2)
def enc(I): G, rho, pp, th, t1, t2 = I; return json.dumps([G, rho, pp, th, [sorted(t1[0]), t1[1]], [sorted(t2[0]), t2[1]]])
def score(I):
    w, s, tc, why = run(*I); return ((tc, w) if os.environ.get("BYTC") else (w, s)), why, tc
cur = None
while cur is None:
    I = rand(); cur = (score(I)[0], I)
best = cur
for it in range(STEPS):
    J = mut(cur[1])
    if not ok(J): continue
    sc, why, tc = score(J)
    if sc >= cur[0]: cur = (sc, J)
    if sc > best[0]: best = (sc, J); print(it, "best", sc, why, "trapchanges", tc, enc(J), flush=True)
    if rnd.random() < 0.0005: cur = best
print("FINAL", best[0], enc(best[1]))
