#!/usr/bin/env python3
"""L-RED R177 FASTABS: fast simulator of the idealised FL dynamics (abs177.py with bper=True, Xi-graph acyclic, all plays to one
terminal T below every beta). Xi(face (v,k)) = signed weight of the betas on the Xi-play (bit = beta rank, sign = parity); with
distinct betas per option two faces never tie. kappa(face) = key(W-target) + (gate index,). Step: avail = current + faces with
larger Xi; sigma' = lex-min tree, levels bottom-up. Equivalence with abs177 (the si.py engine) is checked by verify(); see
docs/red/R177-tiebreak.md. Usage: fastabs.py d deg iters restarts seed [W]  (ladder width W, default 2)"""
import sys, random, json, os
FB = os.environ.get("FB") == "1"

def simulate(G, cap=100000):
    N, lev, opts, gate, br, bp, start = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"], G["start"]
    order = sorted(range(N), key=lambda v: lev[v])
    xorder = G["xorder"]      # topological: xt of v is later in xorder
    s = list(start); steps = 0
    while steps < cap:
        X = [0] * N
        def face(v, k):
            wt, xt, b = opts[v][k]
            return (1 << br[b] if bp[b] == 0 else -(1 << br[b])) + (0 if xt < 0 else X[xt])
        for v in reversed(xorder): X[v] = face(v, s[v])
        avail = [[k for k in range(len(opts[v])) if k == s[v] or face(v, k) > X[v]] for v in range(N)]
        if all(len(a) == 1 for a in avail): return steps, "opt"
        key = [None] * N; ns = list(s)
        for v in order:
            best = None
            for k in avail[v]:
                wt = opts[v][k][0]
                kk = ((gate[v][k],) if wt < 0 else key[wt] + (gate[v][k],))
                if best is None or kk < best[0]: best = (kk, k)
            key[v] = best[0]; ns[v] = best[1]
        if ns == s:
            if not FB: return steps, "stuck"
            # S4c fallback: every Even v with an improving face switches to its best-Xi face (ties impossible: distinct betas)
            ns = [max(avail[v], key=lambda k: face(v, k)) for v in range(N)]
        s = ns; steps += 1
    return steps, "cap"

def randG(d, deg, rng, W=2):
    N = W * d; lev = [i // W for i in range(N)]
    xorder = list(range(N)); rng.shuffle(xorder); pos = {v: i for i, v in enumerate(xorder)}
    opts = []; b = 0
    for v in range(N):
        o = []
        for k in range(deg):
            wt = -1 if lev[v] == 0 else rng.choice([u for u in range(N) if lev[u] == lev[v] - 1])
            later = [u for u in range(N) if pos[u] > pos[v]]
            xt = rng.choice(later + [-1]) if later else -1
            o.append([wt, xt, b]); b += 1
        opts.append(o)
    M = b; br = list(range(M)); rng.shuffle(br); gates = list(range(N * deg)); rng.shuffle(gates)
    return dict(N=N, lev=lev, opts=opts, gate=[gates[v * deg:(v + 1) * deg] for v in range(N)], br=br,
                bp=[rng.randint(0, 1) for _ in range(M)], start=[rng.randrange(deg) for _ in range(N)], xorder=xorder, deg=deg)

def mutate(G, rng):
    H = json.loads(json.dumps(G)); N = H["N"]; deg = H["deg"]; pos = {v: i for i, v in enumerate(H["xorder"])}; r = rng.random()
    if r < 0.3:
        v = rng.randrange(N); k = rng.randrange(deg); later = [u for u in range(N) if pos[u] > pos[v]]
        H["opts"][v][k][1] = rng.choice(later + [-1]) if later else -1
    elif r < 0.45:
        v = rng.randrange(N); k = rng.randrange(deg)
        if H["lev"][v] > 0: H["opts"][v][k][0] = rng.choice([u for u in range(N) if H["lev"][u] == H["lev"][v] - 1])
    elif r < 0.6:
        M = len(H["br"]); a, b = rng.randrange(M), rng.randrange(M); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
    elif r < 0.7:
        H["bp"][rng.randrange(len(H["bp"]))] ^= 1
    elif r < 0.85:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(deg), rng.randrange(deg)
        H["gate"][a][ka], H["gate"][b][kb] = H["gate"][b][kb], H["gate"][a][ka]
    elif r < 0.95:
        H["start"][rng.randrange(N)] = rng.randrange(deg)
    else:   # move a vertex in xorder (keep xt constraints valid by resetting violators)
        xo = H["xorder"]; i, j = rng.randrange(N), rng.randrange(N); v = xo.pop(i); xo.insert(j, v); pos = {u: t for t, u in enumerate(xo)}
        for u in range(N):
            for o in H["opts"][u]:
                if o[1] >= 0 and pos[o[1]] <= pos[u]: o[1] = -1
    return H

if __name__ == "__main__":
    d, deg, iters, rs, seed = (int(a) for a in sys.argv[1:6]); W = int(sys.argv[6]) if len(sys.argv) > 6 else 2
    rng = random.Random(seed); gb, gbs = None, -1
    for r in range(rs):
        G = randG(d, deg, rng, W); bs = simulate(G)[0]
        for it in range(iters):
            H = mutate(G, rng); hs = simulate(H)[0]
            if hs >= bs: G, bs = H, hs
        if bs > gbs: gb, gbs = G, bs; json.dump(gb, open(os.environ.get("OUT", "/dev/null"), "w"))
        print("RESTART", r, bs, "BEST", gbs, flush=True)
    print("FASTABS d", d, "deg", deg, "W", W, "best", gbs)
