#!/usr/bin/env python3
"""L-RED R207 GCLIMB: hill-climb genomes of L_d (RESULTS R109): levels 0..d-1, movers 2l, 2l+1 of degree 2 on every level l, plus
A auxiliary movers of degree 1 per level (env AUX, default 0; AUX=0 and WFREE=0 = the R197 ladder 𝓛^R_d). W-target of an option of a
level-l >= 1 mover: any mover of level l-1 (WFREE=1) or the R197 convention 2(l-1)+k (WFREE=0, two-option movers only; aux movers
W-point to any level-(l-1) mover). Xi-targets: movers later in pi, or the exit X (-1); pi mutable (acyclic by construction).
Score: SCORE=T (default; run length; FL = (max pair flips of the two-option pairs, T); FTOP = (top pair flips, T))
(T = run length from the stored start, r187/ideal.py). Seeds: SEED=<genome> (same d: continue; smaller d: add levels on top,
new movers at random pi positions); aux movers are added to a seed if it has fewer.
Usage: gclimb.py d iters seed out.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
# MAXLEV: option-local mutations only on movers of level <= MAXLEV (default all)
AUX = int(os.environ.get("AUX", "0")); MAXLEV = int(os.environ.get("MAXLEV", "99")); WFREE = os.environ.get("WFREE", "0") == "1"
def norm(G):
    """renumber: gates 0..M-1 and ranks 0..M-1 order-preserving, beta ids in mover/option order"""
    N = G["N"]; flat = [(v, k) for v in range(N) for k in range(len(G["opts"][v]))]
    g = sorted(flat, key=lambda vk: G["gate"][vk[0]][vk[1]]); gi = {vk: i for i, vk in enumerate(g)}
    r = sorted(flat, key=lambda vk: G["br"][G["opts"][vk[0]][vk[1]][2]]); ri = {vk: i for i, vk in enumerate(r)}
    bp = [G["bp"][G["opts"][v][k][2]] for (v, k) in flat]
    opts = []; b = 0
    for v in range(N):
        o = []
        for k in range(len(G["opts"][v])): o.append([G["opts"][v][k][0], G["opts"][v][k][1], b]); b += 1
        opts.append(o)
    return dict(N=N, lev=list(G["lev"]), deg=2, opts=opts, gate=[[gi[(v, k)] for k in range(len(G["opts"][v]))] for v in range(N)],
                br=[ri[vk] for vk in flat], bp=bp, start=list(G["start"]), pi=list(G["pi"]))
def getpi(G):
    if "pi" in G: return list(G["pi"])
    pos = {u: i for i, u in enumerate(G["xorder"])}; return [pos[v] for v in range(G["N"])]
def wchoices(G, v, k):
    l = G["lev"][v]
    if l == 0: return [-1]
    if not WFREE and len(G["opts"][v]) == 2 and v < 2 * (max(G["lev"]) + 1): return [2 * (l - 1) + k]
    return [u for u in range(G["N"]) if G["lev"][u] == l - 1]
def extend(G0, d, rng):
    """add levels on top up to d and AUX aux movers per level; new options get gates / ranks at the top (renormalised by norm)"""
    G = json.loads(json.dumps(G0)); G["pi"] = getpi(G); d0 = max(G["lev"]) + 1
    N0 = G["N"]; nd2 = 2 * d0
    # current layout: movers 0..2d0-1 two-option, then aux; rebuild as two-option movers 0..2d-1 then aux
    two = list(range(nd2)); aux = [v for v in range(N0) if v >= nd2]
    newtwo = list(range(nd2, 2 * d)); naux_old = len(aux)
    mp = {v: v for v in two}
    for i, v in enumerate(aux): mp[v] = 2 * d + i
    N = 2 * d + naux_old; lev = [0] * N; opts = [None] * N; gate = [None] * N; start = [0] * N; pi = [0] * N
    big = 10 ** 6; br = list(G["br"]); bp = list(G["bp"]); nb = len(br)
    for v in range(N0):
        u = mp[v]; lev[u] = G["lev"][v]; start[u] = G["start"][v]; gate[u] = list(G["gate"][v]); pi[u] = G["pi"][v]
        opts[u] = [[mp[w] if w >= 0 else -1, mp[x] if x >= 0 else -1, b] for (w, x, b) in G["opts"][v]]
    for i, u in enumerate(newtwo):
        lev[u] = u // 2; start[u] = rng.randrange(2); pi[u] = rng.random() * (N0 + 1) - 0.5; gate[u] = [big + rng.random() * big for _ in range(2)]
        opts[u] = [[2 * (lev[u] - 1) + k, -1, nb + k] for k in range(2)]; nb += 2; br += [big + rng.random(), big + rng.random()]; bp += [rng.randint(0, 1), rng.randint(0, 1)]
    for l in range(d):
        have = sum(1 for u in range(N) if opts[u] is not None and u >= 2 * d and lev[u] == l)
        for _ in range(AUX - have):
            u = N; N += 1; lev.append(l); start.append(0); pi.append(rng.random() * N0); gate.append([big + rng.random() * big])
            opts.append([[-1 if l == 0 else rng.choice([w for w in range(2 * d) if lev[w] == l - 1]), -1, nb]]); nb += 1
            br.append(big + rng.random()); bp.append(rng.randint(0, 1))
    order = sorted(range(N), key=lambda u: pi[u]); pi = [0] * N
    for i, u in enumerate(order): pi[u] = i
    for u in range(N):   # repair Xi-targets violating pi
        for o in opts[u]:
            if o[1] >= 0 and pi[o[1]] <= pi[u]: o[1] = -1
    # beta ids are global indices into br/bp
    return norm(dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=start, pi=pi))
def lift(G0):
    """RESULTS R109 LIFT: raise every level by one; new level-0 movers A = 0, B = 1 with two options each (Xi-target X, no W-target,
    four new ranks above all others, all even, the larger of each mover on its option 0; four new gates above all others; start 0);
    every option of an old level-0 mover gets W-target A. Old two-option movers 2l, 2l+1 -> 2l+2, 2l+3; aux movers after them."""
    G = json.loads(json.dumps(G0)); pi0 = getpi(G); d0 = max(G["lev"]) + 1; N0 = G["N"]; nd2 = 2 * d0
    mp = {v: v + 2 if v < nd2 else v + 2 for v in range(N0)}
    N = N0 + 2; lev = [0, 0] + [0] * N0; opts = [None] * N; gate = [None] * N; start = [0] * N; pi = [0] * N
    M0 = sum(len(o) for o in G["opts"]); br = list(G["br"]) + [M0 + 3, M0 + 2, M0 + 1, M0]; bp = list(G["bp"]) + [0, 0, 0, 0]
    gm = max(g for gg in G["gate"] for g in gg) + 1
    nb = len(G["br"])
    opts[0] = [[-1, -1, nb], [-1, -1, nb + 1]]; opts[1] = [[-1, -1, nb + 2], [-1, -1, nb + 3]]
    gate[0] = [gm, gm + 1]; gate[1] = [gm + 2, gm + 3]; pi[0], pi[1] = N0, N0 + 1
    for v in range(N0):
        u = mp[v]; lev[u] = G["lev"][v] + 1; start[u] = G["start"][v]; gate[u] = list(G["gate"][v]); pi[u] = pi0[v]
        opts[u] = [[mp[w] if w >= 0 else 0, mp[x] if x >= 0 else -1, b] for (w, x, b) in G["opts"][v]]
    return norm(dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=start, pi=pi))
def mutate(G, rng):
    H2 = json.loads(json.dumps(G)); N = H2["N"]; pi = H2["pi"]; r = rng.random()
    low = [u for u in range(N) if H2["lev"][u] <= MAXLEV]; v = rng.choice(low); k = rng.randrange(len(H2["opts"][v]))
    M = sum(len(o) for o in H2["opts"]); lowb = [o[2] for u in low for o in H2["opts"][u]]
    if r < 0.30: H2["opts"][v][k][1] = rng.choice([u for u in range(N) if pi[u] > pi[v]] + [-1])
    elif r < 0.38:
        a, b = rng.randrange(N), rng.randrange(N); pi[a], pi[b] = pi[b], pi[a]
        if any(xt >= 0 and pi[xt] <= pi[u] for u in range(N) for (_, xt, _) in H2["opts"][u]): return G
    elif r < 0.43:
        c = wchoices(H2, v, k)
        if len(c) < 2: return G
        H2["opts"][v][k][0] = rng.choice(c)
    elif r < 0.6: a, b = rng.choice(lowb), rng.randrange(M); H2["br"][a], H2["br"][b] = H2["br"][b], H2["br"][a]
    elif r < 0.68: H2["bp"][rng.choice(lowb)] ^= 1
    elif r < 0.9:
        a, b = v, rng.randrange(N); ka, kb = rng.randrange(len(H2["opts"][a])), rng.randrange(len(H2["opts"][b]))
        H2["gate"][a][ka], H2["gate"][b][kb] = H2["gate"][b][kb], H2["gate"][a][ka]
    else:
        v = rng.choice([u for u in range(N) if len(H2["opts"][u]) == 2]); H2["start"][v] ^= 1
    return H2
SC = os.environ.get("SCORE", "T")
def score(G):
    S = ideal.traj(G, cap=100000)[0]
    if SC == "T": return (len(S) - 1,)
    import diag
    K = [diag.keys(G, s) for s in S]; d = max(G["lev"]) + 1; F = []
    for l in range(d):
        o = [k[2 * l] < k[2 * l + 1] for k in K]; F.append(sum(a != b for a, b in zip(o, o[1:])))
    if SC == "FL": return (max(F), len(S) - 1)        # max pair flips (two-option pairs), then T
    if SC == "FTOP": return (F[-1], len(S) - 1)       # top pair flips, then T
if __name__ == "__main__":
    d, it, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); out = sys.argv[4]; rng = random.Random(seed)
    G0 = json.load(open(os.environ["SEED"]))
    if os.environ.get("LIFT") == "1": G0 = lift(G0)
    G = extend(G0, d, rng)
    sc = score(G); best = (sc, G); stale = 0
    for i in range(it):
        H2 = mutate(G, rng); s2 = score(H2)
        if s2 >= sc: G, sc = H2, s2
        if sc > best[0]: best = (sc, json.loads(json.dumps(G))); json.dump(G, open(out, "w")); stale = 0
        stale += 1
        if stale > 15000: G = json.loads(json.dumps(best[1])); sc = best[0]; stale = 0
    json.dump(best[1], open(out, "w"))
    print(f"GCLIMB d {d} AUX {AUX} WFREE {int(WFREE)} seed {seed} best {best[0]}")
