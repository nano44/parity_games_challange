#!/usr/bin/env python3
"""L-RED R187 DOWNGEN: random fastcyc genomes of the DOWN class (every Xi-target is a mover of strictly lower level, or 'X');
the class STAB+K can realise (tau-stability by lengths, docs/red/R187 section 2). Usage (lib): randdown(d, deg, rng, W), mutdown(G, rng)."""
import json, random
def randdown(d, deg, rng, W=2, px=0.2):
    N = W * d; lev = [i // W for i in range(N)]; opts = []; b = 0
    for v in range(N):
        o = []
        for k in range(deg):
            wt = -1 if lev[v] == 0 else rng.choice([u for u in range(N) if lev[u] == lev[v] - 1])
            low = [u for u in range(N) if lev[u] < lev[v]]
            xt = -1 if (not low or rng.random() < px) else rng.choice(low)
            o.append([wt, xt, b]); b += 1
        opts.append(o)
    M = b; br = list(range(M)); rng.shuffle(br); gates = list(range(N * deg)); rng.shuffle(gates)
    return dict(N=N, lev=lev, opts=opts, gate=[gates[v * deg:(v + 1) * deg] for v in range(N)], br=br,
                bp=[rng.randint(0, 1) for _ in range(M)], start=[rng.randrange(deg) for _ in range(N)], deg=deg, cyc=True)
def mutdown(G, rng):
    H = json.loads(json.dumps(G)); N = H["N"]; deg = H["deg"]; r = rng.random(); lev = H["lev"]
    v = rng.randrange(N); k = rng.randrange(deg)
    if r < 0.3:
        low = [u for u in range(N) if lev[u] < lev[v]]; H["opts"][v][k][1] = rng.choice(low + [-1]) if low else -1
    elif r < 0.45:
        if lev[v] > 0: H["opts"][v][k][0] = rng.choice([u for u in range(N) if lev[u] == lev[v] - 1])
    elif r < 0.6:
        M = len(H["br"]); a, b = rng.randrange(M), rng.randrange(M); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
    elif r < 0.7: H["bp"][rng.randrange(len(H["bp"]))] ^= 1
    elif r < 0.88:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(deg), rng.randrange(deg)
        H["gate"][a][ka], H["gate"][b][kb] = H["gate"][b][kb], H["gate"][a][ka]
    else: H["start"][rng.randrange(N)] = rng.randrange(deg)
    return H
def randacyc(d, deg, rng, W=2, px=0.15):
    """ACYC class: Xi-targets of any level, but every X-edge v -> xt goes forward in a random order pi (G_X acyclic)."""
    N = W * d; lev = [i // W for i in range(N)]; pi = list(range(N)); rng.shuffle(pi); opts = []; b = 0
    for v in range(N):
        o = []
        for k in range(deg):
            wt = -1 if lev[v] == 0 else rng.choice([u for u in range(N) if lev[u] == lev[v] - 1])
            fw = [u for u in range(N) if pi[u] > pi[v]]
            o.append([wt, -1 if (not fw or rng.random() < px) else rng.choice(fw), b]); b += 1
        opts.append(o)
    M = b; br = list(range(M)); rng.shuffle(br); gates = list(range(N * deg)); rng.shuffle(gates)
    return dict(N=N, lev=lev, opts=opts, gate=[gates[v * deg:(v + 1) * deg] for v in range(N)], br=br, pi=pi,
                bp=[rng.randint(0, 1) for _ in range(M)], start=[rng.randrange(deg) for _ in range(N)], deg=deg, cyc=True)
def mutacyc(G, rng):
    H = json.loads(json.dumps(G)); N = H["N"]; deg = H["deg"]; lev = H["lev"]; pi = H["pi"]; r = rng.random()
    v = rng.randrange(N); k = rng.randrange(deg)
    if r < 0.3:
        fw = [u for u in range(N) if pi[u] > pi[v]]; H["opts"][v][k][1] = rng.choice(fw + [-1]) if fw else -1
    elif r < 0.4:
        a, b = rng.randrange(N), rng.randrange(N); pi[a], pi[b] = pi[b], pi[a]
        if any(o[1] >= 0 and pi[o[1]] <= pi[u] for u in range(N) for o in H["opts"][u]): return mutacyc(G, rng)
    elif r < 0.5:
        if lev[v] > 0: H["opts"][v][k][0] = rng.choice([u for u in range(N) if lev[u] == lev[v] - 1])
    elif r < 0.62:
        M = len(H["br"]); a, b = rng.randrange(M), rng.randrange(M); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
    elif r < 0.7: H["bp"][rng.randrange(len(H["bp"]))] ^= 1
    elif r < 0.88:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(deg), rng.randrange(deg)
        H["gate"][a][ka], H["gate"][b][kb] = H["gate"][b][kb], H["gate"][a][ka]
    else: H["start"][rng.randrange(N)] = rng.randrange(deg)
    return H
