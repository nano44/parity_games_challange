#!/usr/bin/env python3
"""Box 190: IDEAL-model analogues of the N5' variants (R104's IDEAL step with ONE rule changed), and a hill-climber for long runs.
  spec: R104's step (least root-first key among A_s(x)); xi: the Xi-best option of A_s(x) (= the Xi-best option of x);
  idx : the largest gate index in A_s(x);  seq: R104's s' applied at the least-index mover where it differs.
Usage: idealv.py climb MODE D SEEDS ITERS   (genomes: 2-wide degree-2 ladders as in R110's L^R_d, Xi-acyclic by a random order)"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(HERE, "..", "box189")]
from reachcheck import chainB, better, acyclic

def val(G, s, x, k):   # Xi-value as a signed integer (R105 ENC: sum of +-2^rank), larger = better for Even
    return sum((1 << G["br"][b]) * (1 if G["bp"][b] == 0 else -1) for b in chainB(G, s, x, k))
def traj(G, mode, cap=100000):
    N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]; s = list(G["start"]); T = 0
    order = sorted(range(N), key=lambda x: lev[x])
    while T < cap:
        A = [[k for k in range(len(opts[x])) if k == s[x] or better(G, s, x, k, s[x])] for x in range(N)]
        if all(len(a) == 1 for a in A): return T
        ns = list(s)
        if mode in ("spec", "seq"):
            key = [None] * N
            for x in order:
                key[x], ns[x] = min(((gate[x][k],) if opts[x][k][0] < 0 else key[opts[x][k][0]] + (gate[x][k],), k) for k in A[x])
            if mode == "seq":
                ch = [x for x in range(N) if ns[x] != s[x]]; ns = list(s)
                if ch: ns[ch[0]] = (lambda x: min(((gate[x][k],) if opts[x][k][0] < 0 else key[opts[x][k][0]] + (gate[x][k],), k) for k in A[x])[1])(ch[0])
        elif mode == "xi":
            for x in range(N): ns[x] = max(A[x], key=lambda k: val(G, s, x, k))
        elif mode == "idx":
            for x in range(N): ns[x] = max(A[x], key=lambda k: gate[x][k])
        if ns == s: return T
        s = ns; T += 1
    return T

def rgen(rng, d):
    N = 2 * d; lev = [x // 2 for x in range(N)]; order = list(range(N)); rng.shuffle(order); pos = {x: i for i, x in enumerate(order)}
    opts = []
    for x in range(N):
        o = []
        for k in range(2):
            wt = 2 * (lev[x] - 1) + k if lev[x] > 0 else -1
            later = [y for y in range(N) if pos[y] > pos[x]]
            o.append([wt, rng.choice(later) if later and rng.random() < 0.8 else -1, 2 * x + k])
        opts.append(o)
    M = 2 * N; gl = list(range(M)); rng.shuffle(gl); br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": [gl[2 * x:2 * x + 2] for x in range(N)], "br": br,
            "bp": [rng.randint(0, 1) for _ in range(M)], "start": [rng.randint(0, 1) for _ in range(N)]}
def mutate(rng, G):
    G = json.loads(json.dumps(G)); N = G["N"]; M = 2 * N; r = rng.random()
    if r < 0.3:
        x = rng.randrange(N); k = rng.randrange(2); G["opts"][x][k][1] = rng.choice(list(range(N)) + [-1])
    elif r < 0.5: i, j = rng.randrange(M), rng.randrange(M); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.65: G["bp"][rng.randrange(M)] ^= 1
    elif r < 0.85:
        flat = [g for p in G["gate"] for g in p]; i, j = rng.randrange(M), rng.randrange(M); flat[i], flat[j] = flat[j], flat[i]
        G["gate"] = [flat[2 * x:2 * x + 2] for x in range(N)]
    else: G["start"][rng.randrange(N)] ^= 1
    return G if acyclic(G) else None
def climb(mode, d, seed, iters):
    rng = random.Random(seed); G = rgen(rng, d)
    while not acyclic(G): G = rgen(rng, d)
    best = traj(G, mode)
    for _ in range(iters):
        H = mutate(rng, G)
        if H is None: continue
        t = traj(H, mode)
        if t >= best: G, best = H, t
    return best, G
if __name__ == "__main__":
    mode, d, seeds, iters = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]); res = []
    for sd in range(1, seeds + 1):
        b, G = climb(mode, d, sd, iters); res.append(b)
        os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
        json.dump(G, open(os.path.join(HERE, "out", f"climb_{mode}_d{d}_s{sd}.json"), "w"))
    print(f"CLIMB mode {mode} d {d} seeds {seeds} iters {iters}: best T per seed {res}, max {max(res)}", flush=True)
