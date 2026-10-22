#!/usr/bin/env python3
"""Box 10: abstract gated switch-best on CDAG_n (pure combinatorics, Odd-CDAG semantics = Even-CDAG of cdag.py). State tau: tau[v] in 0..v-1.
Improving (y,w): Pfull(w) better than Pfull(tau[y]) (min of symmetric difference lies in the better set; Pfull(0) = {}). Gate rules:
  up1 : (y,w) masked iff y < n and Pfull(tau[y+1]) is STRICTLY WORSE than Pfull(tau[y]) (what exploit e[y,w] -> y+1 realises; variants.py up1)
  upall: masked iff some z > y whose path avoids y has Pfull(tau[z]) strictly worse than Pfull(tau[y])
  none : no masks (switch-best)
Step = arena optimum over {tau[y]} + open improving edges, computed bottom-up with NEW values (one-player optimum in the arena).
Reports max steps over ALL starts (n! strategies) and the start achieving it. Usage: abstractgate.py n rule"""
import sys, itertools
n = int(sys.argv[1]); rule = sys.argv[2]
def pfull(tau, v):
    P = frozenset(); 
    while v: P = P | {v}; v = tau[v]
    return P
def better(P, Q):  # P strictly better for the improver than Q
    d = P ^ Q; return bool(d) and min(d) in P
def pathavoids(tau, z, y):
    v = z
    while v:
        if v == y: return False
        v = tau[v]
    return True
def stepf(tau):
    imp = [(y, w) for y in range(1, n + 1) for w in range(y) if w != tau[y] and better(pfull(tau, w), pfull(tau, tau[y]))]
    if not imp: return None
    opn = []
    for (y, w) in imp:
        cur = pfull(tau, tau[y])
        if rule == "up1": masked = y < n and better(cur, pfull(tau, tau[y + 1]))
        elif rule == "upall": masked = any(pathavoids(tau, z, y) and better(cur, pfull(tau, tau[z])) for z in range(y + 1, n + 1))
        else: masked = False
        if not masked: opn.append((y, w))
    arena = {y: {tau[y]} | {w for (x, w) in opn if x == y} for y in range(1, n + 1)}
    new = list(tau); val = {0: frozenset()}
    for y in range(1, n + 1):      # bottom-up: targets < y already have new values
        bestw = max(arena[y], key=lambda w: (val[w], ) if False else 0)  # placeholder
        bw = None
        for w in sorted(arena[y]):
            if bw is None or better(val[w], val[bw]): bw = w
        new[y] = bw; val[y] = val[bw] | {y}
    if new == tau: return "stuck"
    return new
best = (0, None); stuck = 0
for start in itertools.product(*[range(v) for v in range(1, n + 1)]):
    tau = [0] + list(start); k = 0
    while True:
        r = stepf(tau)
        if r is None: break
        if r == "stuck": stuck += 1; break
        tau = r; k += 1
    if k > best[0]: best = (k, start)
print(f"n={n} rule={rule} starts={len(list(itertools.product(*[range(v) for v in range(1, n + 1)])))} max steps={best[0]} at start tau(1..n)={best[1]}; runs stuck (all improving edges masked, not optimal) {stuck}")
