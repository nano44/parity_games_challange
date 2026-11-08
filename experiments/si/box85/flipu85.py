#!/usr/bin/env python3
"""L-SI box 85: machine check of Lemma FLIP-U (docs/si/box85-twocopies.md §2): Lemma FLIP (L-RED R222 §4) with D_E replaced by D_U,
the number of distinct U-PROJECTIONS (e-vertices at least as relevant as e_S) of the e-sets of w and of the other gates g_o on the
interval. Unit: (mover B, SET-type option S = (w, Xi-target B, any beta parity), maximal interval I with every cycle node constant and
Lambda(B) in {K1, K2}). Runner: box81/ref idealcyc. Prints per genome: units, max (flips - boundU), max (flips - boundE), max flips,
and the number of units where boundU < boundE (the sharpening bites). Usage: flipu85.py BOX81DIR GENOME.json ..."""
import sys, os, json
B81 = sys.argv[1]; sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
def measure(G):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=3000)
    _, _, _, V = gamma3.build(G, set()); N = G["N"]; ev = {V[("e", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}
    K12 = {V[("K", 1)], V[("K", 2)]}; rank = lambda v: (h.prio[v], v)
    units = [(x, k) for x in range(N) for k, o in enumerate(G["opts"][x]) if o[1] == x]
    rows = []
    for s in st:
        cur = list(s0)
        for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); lam = tuple(vs[v][0] for v in range(h.n)); nxt = lambda v: cur[v] if h.owner[v] == 0 else sb[v]
        memo = {}
        def es(v):
            if v in memo: return memo[v]
            seen = set(); out = set(); u = v
            while u not in seen: seen.add(u); out |= {u} if u in ev else set(); u = nxt(u)
            memo[v] = frozenset(out); return memo[v]
        info = {}
        for (x, k) in units:
            eS = V[("e", (x, k))]; w = h.succ[eS][0]
            info[(x, k)] = (s[x] == k, es(w), tuple(es(V[("g", (x, k2))]) for k2 in range(len(G["opts"][x])) if k2 != k))
        rows.append((lam, info))
    res = dict(units=0, exU=None, exE=None, maxfl=0, bites=0); t0 = 0
    for t in range(1, len(rows) + 1):
        if t < len(rows) and rows[t][0] == rows[t - 1][0]: continue
        seg = rows[t0:t]; t0 = t
        for (x, k) in units:
            if seg[0][0][movers[x]] not in K12: continue
            r0 = rank(V[("e", (x, k))]); U = lambda X: frozenset(v for v in X if rank(v) >= r0)
            fl = sum(seg[i][1][(x, k)][0] != seg[i - 1][1][(x, k)][0] for i in range(1, len(seg))); no = len(seg[0][1][(x, k)][2])
            bE = 1 + (len({r[1][(x, k)][1] for r in seg}) - 1) + sum(len({r[1][(x, k)][2][j] for r in seg}) - 1 for j in range(no))
            bU = 1 + (len({U(r[1][(x, k)][1]) for r in seg}) - 1) + sum(len({U(r[1][(x, k)][2][j]) for r in seg}) - 1 for j in range(no))
            res["units"] += 1; res["maxfl"] = max(res["maxfl"], fl); res["bites"] += bU < bE
            res["exU"] = fl - bU if res["exU"] is None else max(res["exU"], fl - bU); res["exE"] = fl - bE if res["exE"] is None else max(res["exE"], fl - bE)
    return res
if __name__ == "__main__":
    for f in sys.argv[2:]:
        r = measure(json.load(open(f))); print(os.path.basename(f), " ".join(f"{k} {v}" for k, v in r.items()), flush=True)
