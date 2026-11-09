"""Genome normalisation helpers shared by shrink34.py and shrink34_moves.py (copied verbatim from shrink34.py)."""

def size(G): return G["N"] + sum(len(o) for o in G["opts"])

def normalise(N, lev, opts, gate, br, bp, start):
    """opts[x] = list of [wt, xt, oldb]; gate[x][k] old gate value; br, bp dicts oldb -> value."""
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]
    gr = {q: r for r, q in enumerate(sorted(O, key=lambda q: gate[q[0]][q[1]]))}
    brr = {q: r for r, q in enumerate(sorted(O, key=lambda q: br[opts[q[0]][q[1]][2]]))}
    newopts = []; newgate = []; nbr = []; nbp = []; b = 0
    for x in range(N):
        oo = []; gg = []
        for k in range(len(opts[x])):
            wt, xt, ob = opts[x][k]; oo.append([wt, xt, b]); gg.append(gr[(x, k)]); nbr.append(brr[(x, k)]); nbp.append(bp[ob]); b += 1
        newopts.append(oo); newgate.append(gg)
    return {"N": N, "lev": lev, "opts": newopts, "gate": newgate, "br": nbr, "bp": nbp, "start": start}

def unpack(G):
    br = {o[2]: G["br"][o[2]] for oo in G["opts"] for o in oo}; bp = {o[2]: G["bp"][o[2]] for oo in G["opts"] for o in oo}
    return [list(map(list, oo)) for oo in G["opts"]], [list(g) for g in G["gate"]], br, bp

