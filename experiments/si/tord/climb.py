#!/usr/bin/env python3
"""Hill-climb on abs2 instances: score = W-changing steps (ties: total steps). Usage: climb.py N STEPS SEED [same|oe|ee|oo]"""
import random, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from abs2 import run, paths
def rew(p): return p if p % 2 == 0 else -p
n, STEPS, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); mode = sys.argv[4] if len(sys.argv) > 4 else "any"
rnd = random.Random(seed)
def ok(I):
    G, rho, pp, th1, c1, th2, c2 = I
    if len(set(pp) | {th1, th2}) != n + (1 if th1 == th2 else 2): return False
    if mode == "same" and th1 != th2: return False
    if mode in ("ee", "oo", "oe") and th1 == th2: return False
    if th1 != th2 and rew(th2) <= rew(th1): return False
    if mode == "oe" and not (th1 % 2 == 1 and th2 % 2 == 0): return False
    if mode == "ee" and not (th1 % 2 == 0 and th2 % 2 == 0): return False
    if mode == "oo" and not (th1 % 2 == 1 and th2 % 2 == 1): return False
    return all(rho[x] in G[x] for x in range(n)) and all(p is not None for p in paths(rho, n).values())
def rand():
    while True:
        G = [sorted(set(rnd.sample([y for y in range(n + 1) if y != x], rnd.randint(1, 3)))) for x in range(n)]
        pv = rnd.sample(range(2, 4 * n + 8), n + 2); th1, th2 = pv[n], pv[n + 1]
        if mode == "same": th2 = th1
        rho = [rnd.choice(G[x]) for x in range(n)]
        I = (G, rho, pv[:n], th1, th1 % 2, th2, th2 % 2)
        if ok(I): return I
def mut(I):
    G, rho, pp, th1, c1, th2, c2 = I; G = [list(e) for e in G]; rho = list(rho); pp = list(pp)
    k = rnd.randrange(6); x = rnd.randrange(n)
    if k == 0:
        y = rnd.choice([y for y in range(n + 1) if y != x])
        if y in G[x] and len(G[x]) > 1 and rho[x] != y: G[x].remove(y)
        elif y not in G[x] and len(G[x]) < 4: G[x].append(y); G[x].sort()
    elif k == 1: rho[x] = rnd.choice(G[x])
    elif k == 2: pp[x] = rnd.randrange(2, 4 * n + 8)
    elif k == 3: th1 = rnd.randrange(2, 4 * n + 8); c1 = th1 % 2
    elif k == 4: th2 = rnd.randrange(2, 4 * n + 8); c2 = th2 % 2
    else:
        y = rnd.randrange(n); pp[x], pp[y] = pp[y], pp[x]
    if mode == "same": th2, c2 = th1, c1
    return (G, rho, pp, th1, c1, th2, c2)
def score(I):
    w, s, why, h = run(*I); return ((s, w) if os.environ.get("BYSTEPS") else (w, s)), why
cur = None
while cur is None:
    I = rand(); cur = (score(I)[0], I)
best = cur
for it in range(STEPS):
    J = mut(cur[1])
    if not ok(J): continue
    sc, why = score(J)
    if sc >= cur[0]: cur = (sc, J)
    if sc > best[0]:
        best = (sc, J); print(it, "best", sc, why, json.dumps(J), flush=True)
    if rnd.random() < 0.0005: cur = best
print("FINAL", best[0], json.dumps(best[1]))
