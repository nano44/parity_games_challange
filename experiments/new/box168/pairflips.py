#!/usr/bin/env python3
"""L-NEW box 168 (1): clock-pair flip counts. For every level and every pair (p, q) of distinct movers of that level: flips :=
#{t in [1, T] : [key_(s_t)(p) < key_(s_t)(q)] != [key_(s_(t-1))(p) < key_(s_(t-1))(q)]}; a reader r of the pair (one level up,
options W-pointing to p and q) has W(r) = {p, q} u W(p) u W(q), so |W(r)| := that size. margin := flips - (|W(r)| + 2 log2(flips) + 2)
(> 0 means the pair is strong enough for the box 167 composition in principle). Prints per file the T, the best pair by flips and by
margin. Usage: pairflips.py file.json ..."""
import os, sys, json, math, itertools
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box167", "pmprime.py")).read().split("\nif __name__")[0])
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert "N" in G; g = Gen(G); S, _ = g.run(G["start"])
    except Exception: continue
    W = wclos(G); keys = [g.keys(s) for s in S]; T = len(S) - 1; best = None; bestm = None
    for L in sorted(set(G["lev"])):
        ms = [v for v in range(G["N"]) if G["lev"][v] == L]
        for p, q in itertools.combinations(ms, 2):
            o = [k[p] < k[q] for k in keys]; fl = sum(a != b for a, b in zip(o, o[1:])); w = len({p, q} | W[p] | W[q])
            mg = fl - (w + 2 * math.log2(fl) + 2) if fl > 0 else -w - 2
            if best is None or fl > best[0]: best = (fl, w, L, p, q)
            if bestm is None or mg > bestm[0]: bestm = (round(mg, 2), fl, w, L, p, q)
    print("%-30s N %2d T %3d | max flips %3d (|W(r)| %2d, level %d, pair %s) | best margin %6.2f (flips %d, |W| %d, level %d)" % (
        os.path.basename(f)[:30], G["N"], T, best[0], best[1], best[2], best[3:], bestm[0], bestm[1], bestm[2], bestm[3]))
