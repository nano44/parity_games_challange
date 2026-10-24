#!/usr/bin/env python3
"""Box 31 (a): abstract model of a W-flat run in a U1 piece after the kappa_w-freeze (assumptions in docs/new/N5-U1T-box31.md §3).
Layered tight DAG: level 0 = {o}; a vertex at level d has its tied successors at level d-1. Honest value A(x) = mid(x) ∪ A(sigma x),
compared by the top-ranked vertex of the symmetric difference (even rank-parity: the larger set is better). One step:
arena(v) = {sigma v} ∪ {z tied: A(z) > A(sigma v)};  sigma' = the tie-break choice in the arena:
  mode bfs (c_w even): lexmin root-first index sequence (BFS over predecessors, increasing index);  mode idx (c_w odd): min index.
Runs to the fixpoint; reports switches per vertex. Usage: cascade.py climb L W seed iters mode"""
import sys, random, os
FIT = os.environ.get("FIT", "sw")

def better(E, a, b):                         # a > b ?  sets of mid vertices; E[x] = (rank, parity)
    d = a ^ b
    if not d: return False
    t = max(d, key=lambda x: E[x][0])
    return (t in a) == (E[t][1] == 0)

def run(inst, mode, cap=10000):
    lev, D, mid, E, idx, s = inst            # lev[v]; D[v] tied succs; mid set; E ranks; idx[v] tie-break index; s start
    s = dict(s); V = sorted(lev, key=lambda v: lev[v]); sw = {v: 0 for v in V}; steps = 0
    while steps < cap:
        A = {}
        for v in V: A[v] = frozenset() if lev[v] == 0 else ((frozenset([v]) if v in mid else frozenset()) | A[s[v]])
        ar = {v: [s[v]] + [z for z in D[v] if z != s[v] and better(E, A[z], A[s[v]])] for v in V if lev[v] > 0}
        ns = {}; key = {}
        for v in V:
            if lev[v] == 0: key[v] = (); continue
            if mode == "idx": ns[v] = min(ar[v], key=lambda z: idx[z])
            else: ns[v] = min(ar[v], key=lambda z: key[z]); key[v] = key[ns[v]] + (idx[v],)
        ch = [v for v in ns if ns[v] != s[v]]
        if not ch: break
        for v in ch: sw[v] += 1
        s.update(ns); steps += 1
    return steps, sw

def rand_inst(rng, L, W):
    lev = {0: 0}; v = 1; layers = [[0]]
    for d in range(1, L + 1):
        layers.append(list(range(v, v + W))); 
        for x in layers[-1]: lev[x] = d
        v += W
    D = {x: sorted(rng.sample(layers[lev[x] - 1], min(len(layers[lev[x] - 1]), rng.randint(1, 3)))) for x in lev if lev[x] > 0}
    mid = {x for x in lev if lev[x] > 0 and rng.random() < 0.6}
    ranks = list(range(len(lev))); rng.shuffle(ranks); E = {x: (ranks[x], rng.randrange(2)) for x in lev}
    perm = list(range(len(lev))); rng.shuffle(perm); idx = {x: perm[x] for x in lev}
    s = {x: rng.choice(D[x]) for x in D}
    return [lev, D, mid, E, idx, s]

def mutate(rng, inst):
    lev, D, mid, E, idx, s = inst; lev = dict(lev); D = {k: list(v) for k, v in D.items()}; mid = set(mid); E = dict(E); idx = dict(idx); s = dict(s)
    xs = [x for x in lev if lev[x] > 0]; r = rng.random(); x = rng.choice(xs)
    layer = [y for y in lev if lev[y] == lev[x] - 1]
    if r < 0.2: D[x] = sorted(rng.sample(layer, min(len(layer), rng.randint(1, 3)))); s[x] = rng.choice(D[x])
    elif r < 0.35: mid ^= {x}
    elif r < 0.55: y = rng.choice(list(lev)); E[x], E[y] = (E[y][0], E[x][1]), (E[x][0], E[y][1])
    elif r < 0.65: E[x] = (E[x][0], 1 - E[x][1])
    elif r < 0.85: y = rng.choice(list(lev)); idx[x], idx[y] = idx[y], idx[x]
    else: s[x] = rng.choice(D[x])
    return [lev, D, mid, E, idx, s]

if __name__ == "__main__":
    _, L, W, seed, iters, mode = sys.argv[1:7]; L, W, seed, iters = int(L), int(W), int(seed), int(iters)
    rng = random.Random(seed); best = None; bf = -1
    for it in range(iters):
        cand = rand_inst(rng, L, W) if best is None or rng.random() < 0.05 else mutate(rng, best)
        steps, sw = run(cand, mode); f = (steps * 1000 + max(sw.values())) if FIT == "steps" else (max(sw.values()) * 1000 + steps)
        if f >= bf: bf, best = f, cand
    steps, sw = run(best, mode)
    print(f"L {L} W {W} mode {mode}: max switches/vertex {max(sw.values())}, steps {steps}, per level max",
          [max(sw[x] for x in best[0] if best[0][x] == d) for d in range(1, L + 1)])
