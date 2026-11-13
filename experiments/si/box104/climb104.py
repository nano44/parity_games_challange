#!/usr/bin/env python3
"""L-SI box 104, probe for O2 (KEY-FREE): hill climb for the number of N5 (SPEC, n5v.py mode spec) iterations from S3 on Gamma3*(G*),
on FREE genomes (MODE free: the 2M carriers in any order, priorities 6 + position) and, head to head, on R104 genomes (MODE edom:
beta = 6 + 2 br + bp, every e even and above every beta in (lev, gate) order), same shape (D levels x W movers, DEG options each),
same seed, same number of steps, same mutations except the priority move. Weak search; DATA only; nothing asymptotic.
Mutations: a Xi-target; a W-target (level >= 1); two gate indices swapped; a start option; priorities (free: two carriers swapped;
edom: two beta ranks swapped, or one beta parity flipped). A step is kept if the score does not fall.
Usage: climb104.py MODE SEED D W DEG STEPS [OUT.json]   (env LNEW, LRED as free104.py; ALG=xi scores N5'-xi instead)"""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import free104 as F
import n5v, gamma3
ALG = os.environ.get("ALG", "spec")

def genome(st):
    lev, opts, gidx, start = st["lev"], st["opts"], st["gidx"], st["start"]; N = len(lev); b = 0; o = []; gate = []
    for x in range(N):
        o.append([[wt, xt, b + k] for k, (wt, xt) in enumerate(opts[x])]); gate.append(gidx[b:b + len(opts[x])]); b += len(opts[x])
    return {"N": N, "lev": lev, "opts": o, "gate": gate, "br": st["br"], "bp": st["bp"], "start": start}

def game(st, mode):
    G = genome(st)
    if mode == "edom": return gamma3.build(G, F.PADS)[0], G
    O = F.options(G); pb = {}; pe = {}
    for i, c in enumerate(st["order"]): (pb if c < len(O) else pe)[O[c % len(O)]] = 6 + i
    return F.build_free(G, pb, pe)[0], G

def score(st, mode):
    g, _ = game(st, mode); states, fb, _ = n5v.run(g, ALG, None, cap=20000); return len(states) - 1

def init(rng, D, W, DEG):
    lev = [l for l in range(D) for _ in range(W)]; N = len(lev); by = {l: [x for x in range(N) if lev[x] == l] for l in range(D)}
    opts = [[[-1 if lev[x] == 0 else rng.choice(by[lev[x] - 1]), rng.randrange(N)] for _ in range(DEG)] for x in range(N)]; M = N * DEG
    gidx = list(range(M)); rng.shuffle(gidx); br = list(range(M)); rng.shuffle(br); order = list(range(2 * M)); rng.shuffle(order)
    return {"lev": lev, "opts": opts, "gidx": gidx, "start": [rng.randrange(DEG) for _ in range(N)], "br": br, "bp": [rng.randrange(2) for _ in range(M)], "order": order}, by

def mutate(rng, st, by, mode):
    s = json.loads(json.dumps(st)); N = len(s["lev"]); M = len(s["gidx"]); r = rng.randrange(5); x = rng.randrange(N); k = rng.randrange(len(s["opts"][x]))
    if r == 0: s["opts"][x][k][1] = -1 if rng.random() < 0.1 else rng.randrange(N)
    elif r == 1:
        if s["lev"][x] > 0: s["opts"][x][k][0] = rng.choice(by[s["lev"][x] - 1])
        else: s["opts"][x][k][1] = rng.randrange(N)
    elif r == 2: a, b = rng.sample(range(M), 2); s["gidx"][a], s["gidx"][b] = s["gidx"][b], s["gidx"][a]
    elif r == 3: s["start"][x] = rng.randrange(len(s["opts"][x]))
    elif mode == "free": a, b = rng.sample(range(2 * M), 2); s["order"][a], s["order"][b] = s["order"][b], s["order"][a]
    elif rng.random() < 0.5: a, b = rng.sample(range(M), 2); s["br"][a], s["br"][b] = s["br"][b], s["br"][a]
    else: a = rng.randrange(M); s["bp"][a] ^= 1
    return s

if __name__ == "__main__":
    mode, seed, D, W, DEG, steps = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    rng = random.Random(seed); st, by = init(rng, D, W, DEG); best = score(st, mode); s0 = best
    for i in range(steps):
        c = mutate(rng, st, by, mode); v = score(c, mode)
        if v >= best: st, best = c, v
    g, G = game(st, mode)
    print(f"CLIMB104 alg {ALG} mode {mode} seed {seed} D {D} W {W} deg {DEG} steps {steps}: N {G['N']} M {len(F.options(G))} |V| {g.n} | start score {s0} best iterations {best}", flush=True)
    if len(sys.argv) > 7: json.dump({"mode": mode, "state": st, "iterations": best}, open(sys.argv[7], "w"))
