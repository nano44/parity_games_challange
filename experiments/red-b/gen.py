#!/usr/bin/env python3
"""Random genome generators (L-RED-B's own). A genome is the dict read by eng.build."""
import random

def rand_genome(rng, N, d=None, maxdeg=3, pX=0.25, pself=0.1, shape="rand"):
    """N movers; levels 0..d-1 with at least one mover per level; deg 1..maxdeg; Xi-targets uniform over movers (X with
    probability pX, a self-loop with probability pself); beta ranks, parities, gate indices, start uniform."""
    if d is None: d = rng.randint(1, min(N, 4))
    d = min(d, N)
    lev = list(range(d)) + [rng.randrange(d) for _ in range(N - d)]
    rng.shuffle(lev)
    bylev = {l: [x for x in range(N) if lev[x] == l] for l in range(d)}
    opts = []; M = 0
    for x in range(N):
        deg = rng.randint(1, maxdeg)
        row = []
        for k in range(deg):
            wt = -1 if lev[x] == 0 else rng.choice(bylev[lev[x] - 1])
            r = rng.random()
            if r < pX: xt = -1
            elif r < pX + pself: xt = x
            else: xt = rng.randrange(N)
            row.append([wt, xt, M]); M += 1
        opts.append(row)
    perm = list(range(M)); rng.shuffle(perm)
    gate = []; i = 0
    for x in range(N):
        gate.append([perm[i + k] for k in range(len(opts[x]))]); i += len(opts[x])
    br = list(range(M)); rng.shuffle(br)
    bp = [rng.randrange(2) for _ in range(M)]
    start = [rng.randrange(len(opts[x])) for x in range(N)]
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": start}

def shaped(rng, N, shape="mix"):
    """Random genomes of several shapes. "mix" draws a shape at random."""
    if shape == "mix": shape = rng.choice(["rand", "dense", "deep", "noX", "self", "flat", "k1"])
    if shape == "eany":
        # any shape, with an ARBITRARY order of the e-priorities (outside R104's packet order; [E-LEV] may fail)
        G = shaped(rng, N, "mix"); M = sum(len(o) for o in G["opts"])
        eo = list(range(M)); rng.shuffle(eo); G["eorder"] = eo
        return G
    if shape == "rand":  return rand_genome(rng, N, maxdeg=rng.randint(1, 3))
    if shape == "dense": return rand_genome(rng, N, maxdeg=3, pX=0.05, pself=0.05)
    if shape == "deep":  return rand_genome(rng, N, d=min(N, rng.randint(2, 6)), maxdeg=rng.randint(2, 3), pX=0.15)
    if shape == "noX":   return rand_genome(rng, N, maxdeg=rng.randint(2, 3), pX=0.0, pself=0.1)
    if shape == "self":  return rand_genome(rng, N, maxdeg=rng.randint(2, 3), pX=0.1, pself=0.4)
    if shape == "flat":  return rand_genome(rng, N, d=1, maxdeg=rng.randint(2, 4), pX=0.1)
    if shape == "k1":
        # one feedback vertex R = 0: Xi-edges go to a lower index or to R (so every Xi-cycle passes R)
        G = rand_genome(rng, N, maxdeg=rng.randint(2, 3), pX=0.1, pself=0.0)
        for x in range(N):
            for o in G["opts"][x]:
                if o[1] >= 0 and o[1] >= x and o[1] != 0: o[1] = rng.randrange(0, x) if x > 0 else 0
        return G
    raise ValueError(shape)

def all_genomes(N, M, part=0, parts=1):
    """Every genome with N movers and M options, with two reductions that change no value of Gamma(G):
    (1) the gate index enters Gamma(G) only through the vertex indices of gates and e-vertices (which are never compared:
        gates are in no set Pi and are no cycle node, e-priorities are distinct) and through the order of the e-priorities
        by (lev(owner), gate index); so only the order of the gate indices inside each level is enumerated;
    (2) an e-vertex of a level-0 option has the single successor c_W, so its value is (c_W, {}, 1) in every state and it
        is in no other vertex's set Pi (its only in-edge is from its gate, and a play through it ends in c_W, whose
        cycle node is more relevant); the order inside level 0 is therefore fixed.
    Levels: every assignment with levels 0..d-1 all inhabited. Degrees: every composition of M into N positive parts.
    W-targets, Xi-targets (X included, self-loops included), beta ranks, parities, starts: all.
    part / parts: only the outer combinations (levels, degrees, W-targets, Xi-targets) with running index = part mod parts
    (the union over part = 0..parts-1 is every genome, each once)."""
    import itertools
    def comps(m, n):
        if n == 1:
            if m >= 1: yield (m,)
            return
        for a in range(1, m - n + 2):
            for rest in comps(m - a, n - 1): yield (a,) + rest
    _ci = [0]
    for d in range(1, N + 1):
        for lev in itertools.product(range(d), repeat=N):
            if set(lev) != set(range(d)): continue
            bylev = {l: [x for x in range(N) if lev[x] == l] for l in range(d)}
            for degs in comps(M, N):
                olist = [(x, k) for x in range(N) for k in range(degs[x])]
                wchoices = [([-1] if lev[x] == 0 else bylev[lev[x] - 1]) for (x, k) in olist]
                xchoices = [[-1] + list(range(N)) for _ in olist]
                lvopts = [[i for i, (x, k) in enumerate(olist) if lev[x] == l] for l in range(d)]
                orders = [[tuple(lvopts[0])]] + [list(itertools.permutations(lvopts[l])) for l in range(1, d)]
                for wts in itertools.product(*wchoices):
                    for xts in itertools.product(*xchoices):
                        _ci[0] += 1
                        if (_ci[0] - 1) % parts != part: continue
                        for br in itertools.permutations(range(M)):
                            for bp in itertools.product((0, 1), repeat=M):
                                for od in itertools.product(*orders):
                                    gp = [0] * M; j = 0
                                    for blk in od:
                                        for i in blk: gp[i] = j; j += 1
                                    for start in itertools.product(*[range(degs[x]) for x in range(N)]):
                                        opts = []; gate = []; i = 0
                                        for x in range(N):
                                            opts.append([[wts[i + k], xts[i + k], i + k] for k in range(degs[x])])
                                            gate.append([gp[i + k] for k in range(degs[x])]); i += degs[x]
                                        yield {"N": N, "lev": list(lev), "opts": opts, "gate": gate, "br": list(br),
                                               "bp": list(bp), "start": list(start)}
