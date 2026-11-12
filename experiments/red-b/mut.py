#!/usr/bin/env python3
"""Mutation operators on genomes (L-RED-B's own). Each returns a NEW valid genome dict or None."""
import copy, random

def M_of(G): return sum(len(o) for o in G["opts"])

def normalize(G):
    """Re-index beta-ids as 0..M-1 in (x, k) order; ranks and gate indices compressed to bijections, order kept."""
    opts = G["opts"]; N = G["N"]
    olist = [(x, k) for x in range(N) for k in range(len(opts[x]))]
    br = [G["br"][opts[x][k][2]] for (x, k) in olist]; bp = [G["bp"][opts[x][k][2]] for (x, k) in olist]
    order = sorted(range(len(olist)), key=lambda i: br[i]); nbr = [0] * len(olist)
    for r, i in enumerate(order): nbr[i] = r
    gi = [G["gate"][x][k] for (x, k) in olist]
    order = sorted(range(len(olist)), key=lambda i: gi[i]); ngi = [0] * len(olist)
    for r, i in enumerate(order): ngi[i] = r
    nopts = []; ngate = []; i = 0
    for x in range(N):
        nopts.append([[opts[x][k][0], opts[x][k][1], i + k] for k in range(len(opts[x]))])
        ngate.append([ngi[i + k] for k in range(len(opts[x]))]); i += len(opts[x])
    return {"N": N, "lev": list(G["lev"]), "opts": nopts, "gate": ngate, "br": nbr, "bp": bp, "start": list(G["start"])}

def mutate(G, rng, Ncap=10**9, Mcap=10**9):
    G = copy.deepcopy(G); N = G["N"]; lev = G["lev"]; opts = G["opts"]; M = M_of(G)
    bylev = {}
    for x in range(N): bylev.setdefault(lev[x], []).append(x)
    op = rng.choice(["xt", "xt", "xt", "wt", "brswap", "brswap", "bp", "gswap", "start", "addopt", "delopt", "addmover",
                     "delmover", "xtX", "brmove"])
    x = rng.randrange(N); k = rng.randrange(len(opts[x]))
    if op == "xt":
        opts[x][k][1] = rng.randrange(N)
    elif op == "xtX":
        opts[x][k][1] = -1
    elif op == "wt":
        if lev[x] == 0: return None
        opts[x][k][0] = rng.choice(bylev[lev[x] - 1])
    elif op == "brswap":
        a, b = rng.randrange(M), rng.randrange(M); G["br"][a], G["br"][b] = G["br"][b], G["br"][a]
    elif op == "brmove":
        # move one beta to a random rank, shifting the others
        a = rng.randrange(M); r = rng.randrange(M); old = G["br"][a]
        for i in range(M):
            if old < G["br"][i] <= r: G["br"][i] -= 1
            elif r <= G["br"][i] < old: G["br"][i] += 1
        G["br"][a] = r
    elif op == "bp":
        a = rng.randrange(M); G["bp"][a] ^= 1
    elif op == "gswap":
        x2 = rng.randrange(N); k2 = rng.randrange(len(opts[x2]))
        G["gate"][x][k], G["gate"][x2][k2] = G["gate"][x2][k2], G["gate"][x][k]
    elif op == "start":
        G["start"][x] = rng.randrange(len(opts[x]))
    elif op == "addopt":
        if M >= Mcap: return None
        wt = -1 if lev[x] == 0 else rng.choice(bylev[lev[x] - 1])
        xt = rng.choice([-1] + list(range(N)))
        opts[x].append([wt, xt, M]); G["gate"][x].append(M + rng.random() - 0.5)
        G["br"].append(rng.randrange(M + 1) - 0.5); G["bp"].append(rng.randrange(2))
    elif op == "delopt":
        if len(opts[x]) == 1: return None
        del opts[x][k]; del G["gate"][x][k]
        if G["start"][x] == k: G["start"][x] = 0
        elif G["start"][x] > k: G["start"][x] -= 1
    elif op == "addmover":
        if N >= Ncap or M >= Mcap: return None
        l = rng.randint(0, max(lev) + 1)
        if l > 0 and (l - 1) not in bylev: return None
        wt = -1 if l == 0 else rng.choice(bylev[l - 1])
        lev.append(l); opts.append([[wt, rng.choice([-1] + list(range(N + 1))), M]])
        G["gate"].append([M + rng.random() - 0.5]); G["br"].append(rng.randrange(M + 1) - 0.5); G["bp"].append(rng.randrange(2))
        G["start"].append(0); G["N"] = N + 1
    elif op == "delmover":
        if N == 1: return None
        # x may be removed only if no W-target points to it, or another mover of its level can take over
        others = [y for y in bylev[lev[x]] if y != x]
        users = [(y, j) for y in range(N) for j in range(len(opts[y])) if opts[y][j][0] == x]
        if users and not others: return None
        if not others and any(lev[y] > lev[x] for y in range(N)): return None
        for (y, j) in users: opts[y][j][0] = rng.choice(others)
        for y in range(N):
            for o in opts[y]:
                if o[1] == x: o[1] = -1
        del lev[x]; del opts[x]; del G["gate"][x]; del G["start"][x]; G["N"] = N - 1
        for y in range(N - 1):
            for o in opts[y]:
                if o[0] > x: o[0] -= 1
                if o[1] > x: o[1] -= 1
    return normalize(G)
