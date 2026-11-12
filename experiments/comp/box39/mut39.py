#!/usr/bin/env python3
"""L-COMP box 39: the move set of box38/climb38.py (canon, rerank, NM, flat, unflat, low, mutate), copied verbatim except that mutate
takes an optional list `kinds` of move numbers (0-8; 6 = add option, 8 = add mover) and the size cap CAP is a module variable."""
import json
CAP = 10 ** 9


def canon(G):
    """b := option order; br/bp re-indexed accordingly; gate kept (a permutation over options)."""
    G = json.loads(json.dumps(G)); br, bp = [], []; i = 0
    for x in range(G["N"]):
        for o in G["opts"][x]:
            br.append(G["br"][o[2]]); bp.append(G["bp"][o[2]]); o[2] = i; i += 1
    G["br"], G["bp"] = br, bp; return G


def rerank(vals):
    order = sorted(range(len(vals)), key=lambda i: vals[i]); r = [0] * len(vals)
    for j, i in enumerate(order): r[i] = j
    return r


def NM(G): return G["N"] + sum(len(o) for o in G["opts"])


def flat(G):
    """options as dicts in option order (x, wt, xt, gate, br, bp), plus mover data."""
    O = []
    for x in range(G["N"]):
        for k, (wt, xt, b) in enumerate(G["opts"][x]):
            O.append(dict(x=x, wt=wt, xt=xt, gate=G["gate"][x][k], br=G["br"][b], bp=G["bp"][b], st=(G["start"][x] == k)))
    return O


def unflat(N, lev, O):
    gr = rerank([o["gate"] for o in O]); brr = rerank([o["br"] for o in O])
    G = {"N": N, "lev": list(lev), "opts": [[] for _ in range(N)], "gate": [[] for _ in range(N)], "br": [], "bp": [], "start": [0] * N}
    for i, o in enumerate(sorted(range(len(O)), key=lambda i: (O[i]["x"], i))):
        q = O[o]; x = q["x"]; k = len(G["opts"][x])
        G["opts"][x].append([q["wt"], q["xt"], i]); G["gate"][x].append(gr[o]); G["br"].append(brr[o]); G["bp"].append(q["bp"])
        if q["st"]: G["start"][x] = k
    return G


def low(G, lev, x): return [y for y in range(G["N"]) if lev[y] == lev[x] - 1]


def mutate(G, rng, kinds=None):
    N, lev = G["N"], G["lev"]; O = flat(G); M = len(O); r = rng.randrange(9) if kinds is None else rng.choice(kinds)
    if r == 0:
        rng.choice(O)["xt"] = rng.randrange(-1, N)
    elif r == 1:
        c = [o for o in O if lev[o["x"]] >= 1]
        if not c: return None
        o = rng.choice(c); o["wt"] = rng.choice(low(G, lev, o["x"]))
    elif r == 2:
        a, b = rng.sample(O, 2); a["gate"], b["gate"] = b["gate"], a["gate"]
    elif r == 3:
        a, b = rng.sample(O, 2); a["br"], b["br"] = b["br"], a["br"]
    elif r == 4:
        rng.choice(O)["bp"] ^= 1
    elif r == 5:
        x = rng.randrange(N); mine = [o for o in O if o["x"] == x]
        if len(mine) < 2: return None
        for o in mine: o["st"] = False
        rng.choice(mine)["st"] = True
    elif r == 6:
        if NM(G) + 1 > CAP: return None
        x = rng.randrange(N)
        O.append(dict(x=x, wt=(rng.choice(low(G, lev, x)) if lev[x] else -1), xt=rng.randrange(-1, N), gate=rng.uniform(-1, M), br=rng.uniform(-1, M),
                      bp=rng.randrange(2), st=False))
    elif r == 7:
        x = rng.randrange(N); mine = [i for i, o in enumerate(O) if o["x"] == x]
        if len(mine) < 2: return None
        i = rng.choice(mine); was = O[i]["st"]; del O[i]
        if was: rng.choice([o for o in O if o["x"] == x])["st"] = True
    else:
        if NM(G) + 2 > CAP: return None
        l = rng.choice(sorted(set(lev)) + [max(lev) + 1]); p = max([y + 1 for y in range(N) if lev[y] <= l], default=0)
        sh = lambda y: y + (y >= p) if y >= 0 else y
        for o in O: o["x"] = sh(o["x"]); o["wt"] = sh(o["wt"]); o["xt"] = sh(o["xt"])
        lev = lev[:p] + [l] + lev[p:]; N += 1
        G2 = {"N": N}; lw = [y for y in range(N) if lev[y] == l - 1]
        O.append(dict(x=p, wt=(rng.choice(lw) if l else -1), xt=rng.randrange(-1, N), gate=rng.uniform(-1, M), br=rng.uniform(-1, M), bp=rng.randrange(2), st=True))
        if rng.random() < 0.5:   # let an existing option point at the new mover (else it is unreachable by Xi)
            rng.choice(O[:-1])["xt"] = p
    return unflat(N, lev, O)


