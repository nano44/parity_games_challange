#!/usr/bin/env python3
"""L-SI box 105 (D2/D3 probe): FREE genomes on the ladder shape of RESULTS R110 (L-RED's R197 convention: movers 2l and 2l + 1 on
level l, l < d, degree 2, option k of a mover of level l >= 1 W-points to mover 2(l - 1) + k). Free parameters: the Xi-targets (a
mover or X), the gate indices (a permutation), the 2M carriers' order and parities (priority 6 + 2 * rank + parity), the start.
MODE free: all of them; MODE edom: R104's priorities (every e even above every beta, in (lev, gate) order; beta = 6 + 2 * rank +
parity), i.e. only the beta ranks and parities are free. Score: L* of KEY(G*) (key105.key_run). Random restarts + hill climb.
Usage: ladder105.py MODE d SEED RESTARTS STEPS [OUT.json]"""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import key105 as K
F = K.F

def genome(st, d):
    N = 2 * d; lev = [x // 2 for x in range(N)]; opts = []; b = 0
    for x in range(N):
        o = []
        for k in range(2): o.append([-1 if lev[x] == 0 else 2 * (lev[x] - 1) + k, st["xt"][b], b]); b += 1
        opts.append(o)
    M = 2 * N
    return {"N": N, "lev": lev, "opts": opts, "gate": [st["gate"][2 * x:2 * x + 2] for x in range(N)], "br": list(range(M)), "bp": [0] * M, "start": st["start"]}

def prios(st, G, mode):
    O = F.options(G); M = len(O)
    if mode == "free":
        pb = {q: 6 + 2 * st["rank"][i] + st["par"][i] for i, q in enumerate(O)}; pe = {q: 6 + 2 * st["rank"][M + i] + st["par"][M + i] for i, q in enumerate(O)}
    else:
        br = sorted(range(M), key=lambda i: st["rank"][i]); pb = {O[i]: 6 + 2 * r + st["par"][i] for r, i in enumerate(br)}
        eo = sorted(O, key=lambda q: (G["lev"][q[0]], G["gate"][q[0]][q[1]])); pe = {q: 6 + 2 * M + 2 * i for i, q in enumerate(eo)}
    return pb, pe

def score(st, d, mode):
    G = genome(st, d); pb, pe = prios(st, G, mode); states, c, *_ = K.key_run(G, pb, pe); return len(states) - 1

def init(rng, d):
    N = 2 * d; M = 2 * N; g = list(range(M)); rng.shuffle(g); r = list(range(2 * M)); rng.shuffle(r)
    return {"xt": [rng.choice([-1] + list(range(N))) for _ in range(M)], "gate": g, "rank": r, "par": [rng.randrange(2) for _ in range(2 * M)], "start": [rng.randrange(2) for _ in range(N)]}

def mutate(rng, st, d):
    N = 2 * d; M = 2 * N; t = json.loads(json.dumps(st)); m = rng.randrange(5)
    if m == 0: t["xt"][rng.randrange(M)] = rng.choice([-1] + list(range(N)))
    elif m == 1: i, j = rng.sample(range(M), 2); t["gate"][i], t["gate"][j] = t["gate"][j], t["gate"][i]
    elif m == 2: i, j = rng.sample(range(2 * M), 2); t["rank"][i], t["rank"][j] = t["rank"][j], t["rank"][i]
    elif m == 3: i = rng.randrange(2 * M); t["par"][i] ^= 1
    else: i = rng.randrange(N); t["start"][i] ^= 1
    return t

if __name__ == "__main__":
    mode, d, seed, restarts, steps = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]); rng = random.Random(seed)
    best = -1; bst = None; hist = []
    for r in range(restarts):
        st = init(rng, d); sc = score(st, d, mode)
        for _ in range(steps):
            t = mutate(rng, st, d); s2 = score(t, d, mode)
            if s2 >= sc: st, sc = t, s2
        hist.append(sc)
        if sc > best: best, bst = sc, st
    print(f"LADDER105 mode {mode} d {d} seed {seed} restarts {restarts} steps {steps}: best L* {best} | per restart {sorted(hist, reverse=True)}", flush=True)
    if len(sys.argv) > 6: json.dump({"mode": mode, "d": d, "state": bst, "L": best}, open(sys.argv[6], "w"))
