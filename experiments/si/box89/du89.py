#!/usr/bin/env python3
"""L-SI box 89: D_U at each real bit's waiting hub. For bit B_l (names file, option SET) let e_S be its SET e-vertex, w = succ(e_S)
(the W-target's vertex in Gamma), r = rank(e_S). D_U,I(w) := #distinct pi_r(E_t(w)) over a maximal interval I with every cycle node
constant (pi_r = e-vertices at least as relevant as e_S; E_t(w) = e-vertices on the play from w at state t, sigma_t / Odd's best
response). Prints per genome: T, N + M, and per bit l: max over I of D_U,I(w_l) and the number of intervals.
Usage: du89.py BOX81DIR GENOME.json ..."""
import sys, os, json
B81 = sys.argv[1]; sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
def du(G, nm, cap=3000):
    N = G["N"]; h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=cap); _, _, _, V = gamma3.build(G, set())
    ev = {V[("e", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}; rank = lambda v: (h.prio[v], v)
    bits = sorted((int(n[1:]), x) for x, n in enumerate(nm["movers"]) if n[0] == "B" and n[1:].isdigit())
    rows = []
    for s in st:
        cur = list(s0)
        for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); rows.append((cur, sb, tuple(vs[v][0] for v in range(h.n))))
    res = {}
    for l, x in bits:
        eS = V[("e", (x, nm["opts"][x].index("SET")))]; r0 = rank(eS); w = h.succ[eS][0]
        best = 0; cur_set = set(); nI = 1
        for t, (cur, sb, lam) in enumerate(rows):
            if t and lam != rows[t - 1][2]: best = max(best, len(cur_set)); cur_set = set(); nI += 1
            nxt = lambda v: cur[v] if h.owner[v] == 0 else sb[v]; v = w; seen = set(); out = []
            while v not in seen:
                seen.add(v)
                if v in ev and rank(v) >= r0: out.append(rank(v))
                v = nxt(v)
            cur_set.add(tuple(sorted(out)))
        res[l] = (max(best, len(cur_set)), nI)
    return len(st) - 1, N + sum(len(o) for o in G["opts"]), res
if __name__ == "__main__":
    for f in sys.argv[2:]:
        G = json.load(open(f)); nm = json.load(open(f[:-5] + ".names.json")); T, NM, res = du(G, nm)
        print(os.path.basename(f), "T", T, "N+M", NM, " ".join(f"w{l}:{d}/I{i}" for l, (d, i) in sorted(res.items())))
