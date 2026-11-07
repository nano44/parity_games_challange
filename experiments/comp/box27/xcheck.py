#!/usr/bin/env python3
"""Cross-check sim.py (mine) against L-RED's r187/ideal.py (path given in argv[1], read-only copy) on every genome file given
(all starts when N <= 10, else the stored start) and on random acyclic genomes. Prints mismatches and totals."""
import sys, os, json, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sim
sys.path.insert(0, sys.argv[1]); import ideal

def randg(rng, d, width=2, pad=0):
    N = width * d + pad
    lev = [l for l in range(d) for _ in range(width)] + [rng.randrange(d) for _ in range(pad)]
    deg = [2] * (width * d) + [1] * pad
    order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    opts = []; b = 0
    for x in range(N):
        ox = []
        for k in range(deg[x]):
            ws = [y for y in range(N) if lev[y] == lev[x] - 1]
            w = -1 if lev[x] == 0 else rng.choice(ws)
            xs = [y for y in range(N) if pos[y] > pos[x]]
            xt = rng.choice(xs + [-1, -1]) if xs else -1
            ox.append([w, xt, b]); b += 1
        opts.append(ox)
    M = b; ranks = list(range(M)); rng.shuffle(ranks); gates = list(range(M)); rng.shuffle(gates)
    gi = iter(gates); gate = [[next(gi) for _ in ox] for ox in opts]
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": ranks, "bp": [rng.randrange(2) for _ in range(M)],
            "start": [rng.randrange(len(ox)) for ox in opts]}

def cmp(G, starts):
    bad = 0
    for st in starts:
        G2 = dict(G); G2["start"] = list(st)
        A, wa = sim.run(G2); B, wb = ideal.traj(G2)
        if A != B or wa != wb: bad += 1
    return bad

def acyclic(G):
    N = G["N"]; adj = [set(o[1] for o in G["opts"][x] if o[1] >= 0) for x in range(N)]; col = [0] * N
    def dfs(v):
        col[v] = 1
        for w in adj[v]:
            if col[w] == 1 or (col[w] == 0 and not dfs(w)): return False
        col[v] = 2; return True
    return all(col[v] or dfs(v) for v in range(N))

tot = runs = skip = 0
for f in sys.argv[2:]:
    G = json.load(open(f))
    if not acyclic(G): skip += 1; continue
    starts = list(itertools.product(*[range(len(o)) for o in G["opts"]])) if G["N"] <= 10 else [G["start"]]
    b = cmp(G, starts); tot += b; runs += len(starts)
    if b: print("MISMATCH", f, b)
rng = random.Random(27)
for i in range(3000):
    G = randg(rng, rng.randrange(1, 6), rng.choice([1, 2, 3]), rng.randrange(0, 4))
    b = cmp(G, [G["start"]]); tot += b; runs += 1
    if b: print("MISMATCH random", i)
print("files skipped (Xi-cyclic)", skip, "runs", runs, "mismatches", tot)
