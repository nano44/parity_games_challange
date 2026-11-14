#!/usr/bin/env python3
"""Box 207 Addendum C (L-NEW successor 71): where the gate flips of an IDEAL-CYC run sit, relative to the feedback vertex R (fvs202; first
in index order). Unit: gate flips (pairs (step t, gate g) with σ̄_(t−1)(g) ≠ σ̄_t(g)). Split by WHERE: «in» = class(R) does not change at t
(inside an R-window), «end» = it does; and by KIND of g at t − 1 and at t: BB = both face plays (e_g's and β_g's) pass R, B1 = exactly one
does, N = neither (by Lemma PAID, a gate at its e-face of kind N is a chained gate). Scope: every gate. Output: counts per (where, kind at
t − 1 > kind at t); inN := in-window flips with kind N at t − 1 or t (descriptive). Usage: wkind207.py G.json ..."""
import sys, os, json, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE] + [os.path.join(HERE, "..", d) for d in ("box203", "box202", "box191")]
import gfc203, idealcyc, rlocal207
for f in sys.argv[1:]:
    G = json.load(open(f)); H, n, E, V, gates = gfc203.hist_ideal(G); ST = idealcyc.run(G); h, s0, movers, inv = idealcyc.build(G)
    R = rlocal207.fvsets(G)[0]; r = V[("x", R)]
    em = 0
    for k, v in V.items():
        if isinstance(k, tuple) and k[0] == "e": em |= E.bit[v]
    def kinds(t):
        s = list(s0)
        for x in range(G["N"]): s[movers[x]] = V[("g", (x, ST[t][x]))]
        fn = lambda v: s[v] if h.owner[v] == 0 else H[t][1][v]
        def hit(v):
            seen = set()
            while v not in seen:
                if v == r: return 1
                seen.add(v); v = fn(v)
            return 0
        return {g: ("N", "B1", "BB")[hit(a) + hit(b)] for g, (q, a, b) in gates.items()}
    c = collections.Counter(); prev = kinds(0); inN = 0; tot = 0
    for t in range(1, len(H)):
        cur = kinds(t)
        same = (H[t][0][r][0], H[t][0][r][1] & em) == (H[t - 1][0][r][0], H[t - 1][0][r][1] & em)
        for g in gates:
            if H[t][1][g] != H[t - 1][1][g]:
                c[("in" if same else "end") + ":" + prev[g] + ">" + cur[g]] += 1; tot += 1
                if same and "N" in (prev[g], cur[g]): inN += 1
        prev = cur
    print(os.path.basename(f), "R", R, "flips", tot, "in", sum(v for k, v in c.items() if k.startswith("in")), "inN", inN,
          " ".join("%s %d" % kv for kv in sorted(c.items())), flush=True)
