#!/usr/bin/env python3
"""Box 213 (L-NEW successor 75): key213's keysig on the tail (Y = V) under four readings of «SPEC run on the window game», to reconcile
key213's tower total (7,359) with REFEREE-2 40's (7,358, R2-box212-preread.md §7). Odd at sigma-bar_u (window start) or sigma-bar_s
(current); Even non-movers keep A_s (SPEC's arena; key213) or only sigma_s (H_Y as RF-B defines it; REFEREE-2). Also counts the states
where sigma-bar_s differs from sigma-bar_0 at some Odd vertex (box 212's tail clause says 0). Usage: ks213.py G.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import key213
for fn in sys.argv[1:]:
    G = json.load(open(fn)); G = G.get("genome", G); g, E, H, cls, mv = key213.history(G); n, T = g.n, len(H) - 1; res = {}; bad = 0
    for s in range(T):
        bad += any(H[s][3][o] != H[0][3][o] for o in range(n) if g.owner[o] == 1)
    for variant in ("sbar_u_A", "sbar_s_A", "sbar_u_keep", "sbar_s_keep"):
        tot = 0
        for s in range(T):
            sigma, tau, vs, tb, Is = H[s]; ns = H[s + 1][0]
            odd = H[0][3] if variant.startswith("sbar_u") else tb
            I2 = Is if variant.endswith("_A") else [(v, w) for (v, w) in Is if v in mv]
            ix, best, _, _ = key213.optimum(g, set(range(n)), sigma, I2, odd)
            tot += sum(1 for x in mv if best[ix[x]] != ix[ns[x]])
        res[variant] = tot
    print(os.path.basename(fn), "T", T, " ".join("%s %d" % kv for kv in res.items()), "sbar_changes", bad, flush=True)
