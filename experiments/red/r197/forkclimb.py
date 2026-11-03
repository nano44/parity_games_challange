#!/usr/bin/env python3
"""L-RED R197 FORKCLIMB: hill-climb width-2 W-ladders (option k of a level-l >= 1 mover has W-target 2(l-1) + (k mod 2), r190 format)
whose Xi-graph is a FORK ladder: the two options of a mover with Xi-targets (k mod 2 picks the side) point to the TWO movers of one
other level (each mover's options split over both sides), so consecutive single wakes can alternate sides (R196 escape shape).
MODE=down: Xi of level l -> level l-1 (level 0 -> exit); MODE=up: Xi of level l -> level l+1 (top -> exit); MODE=mix: per mover,
Xi-level free among levels with a pi-later pair (acyclic by pi = level order or its reverse per mode). Degree D: options k >= 2 get
Xi-target exit or a side (mutable). Mutations: gates, beta ranks / parities, start, side bijection per mover.
MODE=free: r190/delclimb ladders (Xi free, pi mutable). Score SCORE=L (default), FMAX (max_l F_l, sum F, L), JUMP (max_l F_l - F_(l-1), sum F, L), U (box 144 CHAIN-BACK unchained steps), F (sum of carries F_l), TOP (moves of the top level).
Usage: forkclimb.py d D iters seed out.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178"), os.path.join(H, "..", "r190")]
import ideal, delclimb
MODE = os.environ.get("MODE", "down"); SC = os.environ.get("SCORE", "L")
def xlev(l, d):
    if MODE == "down": return l - 1
    if MODE == "up": return l + 1 if l + 1 < d else -1
def rand(d, D, rng):
    if MODE == "free": return delclimb.rand(d, 2, D, rng)
    N = 2 * d; lev = [v // 2 for v in range(N)]
    pi = [ (N - 1 - v) if MODE == "down" else v for v in range(N)]
    opts = []
    for v in range(N):
        l = lev[v]; xl = xlev(l, d); flip = rng.randint(0, 1); o = []
        for k in range(D):
            wt = -1 if l == 0 else 2 * (l - 1) + (k % 2)
            if xl < 0: xt = -1
            elif k < 2: xt = 2 * xl + ((k + flip) % 2)
            else: xt = rng.choice([2 * xl, 2 * xl + 1, -1])
            o.append([wt, xt, D * v + k])
        opts.append(o)
    M = N * D; g = list(range(M)); rng.shuffle(g); b = list(range(M)); rng.shuffle(b)
    return dict(N=N, lev=lev, opts=opts, deg=D, pi=pi, gate=[g[D * v:D * v + D] for v in range(N)], br=b,
                bp=[rng.randint(0, 1) for _ in range(M)], start=[rng.randrange(D) for _ in range(N)], mode=MODE)
def mutate(G, rng):
    if MODE == "free": return delclimb.mutate(G, rng)
    H = json.loads(json.dumps(G)); N = H["N"]; D = H["deg"]; M = N * D; r = rng.random(); v = rng.randrange(N)
    if r < 0.1:
        o = H["opts"][v]
        if o[0][1] >= 0: o[0][1], o[1][1] = o[1][1], o[0][1]
        else: return G
    elif r < 0.15 and D > 2:
        k = rng.randrange(2, D); xl = xlev(H["lev"][v], max(H["lev"]) + 1)
        if xl < 0: return G
        H["opts"][v][k][1] = rng.choice([2 * xl, 2 * xl + 1, -1])
    elif r < 0.4: a, b = rng.randrange(M), rng.randrange(M); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
    elif r < 0.5: H["bp"][rng.randrange(M)] ^= 1
    elif r < 0.85:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(D), rng.randrange(D); H["gate"][a][ka], H["gate"][b][kb] = H["gate"][b][kb], H["gate"][a][ka]
    else: H["start"][v] = rng.randrange(D)
    return H
def score(G):
    if SC == "U":
        os.environ["SCORE"] = "U"; L, U, per = delclimb.stats(G, 2); os.environ["SCORE"] = SC; return (U, L)
    S, why = ideal.traj(G, cap=20000)
    if SC == "L": return (len(S) - 1,)
    import anal
    L, why, F, Mv, Dl, lagn, off = anal.run(G, 2)
    if SC == "F": return (sum(F), L)
    if SC == "TOP": return (Mv[-1], L)
    if SC == "FMAX": return (max(F), sum(F), L)
    if SC == "JUMP": return (max(F[l] - F[l - 1] for l in range(1, len(F))), sum(F), L)
if __name__ == "__main__":
    sys.path.insert(0, H)
    d, D, it, seed = map(int, sys.argv[1:5]); out = sys.argv[5]; rng = random.Random(seed)
    G = rand(d, D, rng)
    if os.environ.get("SEEDG"):   # start from a given genome, adding (d - its depth) new levels at the BOTTOM (W-targets of the old level 0)
        G0 = json.load(open(os.environ["SEEDG"])); add = d - (max(G0["lev"]) + 1); N0 = G0["N"]; M0 = sum(len(o) for o in G0["opts"]); D0 = len(G0["opts"][0])
        H2 = dict(N=N0 + 2 * add, lev=[l for l in range(add) for _ in (0, 1)] + [l + add for l in G0["lev"]], deg=D0)
        sh = 2 * add; opts = []
        for l in range(add):
            for i in (0, 1): opts.append([[-1 if l == 0 else 2 * (l - 1) + k % 2, rng.choice(list(range(sh + N0)) + [-1]) if False else -1, 0] for k in range(D0)])
        for v in range(N0):
            opts.append([[(o[0] + sh) if o[0] >= 0 else 2 * (add - 1) + k % 2, (o[1] + sh) if o[1] >= 0 else -1, 0] for k, o in enumerate(G0["opts"][v])])
        b = 0
        for o in opts:
            for x in o: x[2] = b; b += 1
        M = b; Mn = M - M0
        H2["opts"] = opts; H2["gate"] = [[M0 + D0 * v + k for k in range(D0)] for v in range(sh)] + [list(g) for g in G0["gate"]]
        H2["br"] = list(range(Mn)) + [r + Mn for r in G0["br"]]; H2["bp"] = [rng.randint(0, 1) for _ in range(Mn)] + list(G0["bp"])
        H2["start"] = [rng.randrange(D0) for _ in range(sh)] + list(G0["start"])
        pos = {u: i for i, u in enumerate(G0.get("xorder") or sorted(range(N0), key=lambda u: G0["pi"][u]))}
        H2["pi"] = [N0 + i for i in range(sh)] + [pos[v] for v in range(N0)]
        G = H2
    sc = score(G); best = (sc, G)
    for i in range(it):
        if i % 20000 == 0 and i: G = json.loads(json.dumps(best[1])); sc = best[0]
        H2 = mutate(G, rng); s2 = score(H2)
        if s2 >= sc: G, sc = H2, s2
        if sc > best[0]: best = (sc, json.loads(json.dumps(G))); json.dump(G, open(out, "w"))
    json.dump(best[1], open(out, "w"))
    print(f"FORKCLIMB MODE {MODE} SCORE {SC} d {d} D {D} seed {seed} best {best[0]}")
