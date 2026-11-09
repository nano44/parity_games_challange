#!/usr/bin/env python3
"""L-RED 63 R229 item 6: class heights on R221 own.py (IDEAL-CYC; cap 3000). cc(v) = #steps at which class (Λ, E) of v changes.
Prints per genome: T, maxcc (max over ALL vertices, per-vertex MAXIMUM, with the vertex kind), minh (max over gates of min(cc(e_g), cc(b_g))),
minhf (the same over gates that flip at least once) with the flips there, maxflip. Usage: hgt229.py G.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r221")]
import own
print("instance N+M T maxcc kind minh minhf flips_at_minhf maxflip", flush=True)
for f in sys.argv[1:]:
    G = json.load(open(f)); G = G.get("genome", G)
    out, V, O, _ = own.run(G, 3000); T = len(out) - 1; evs = {V[("e", q)] for q in O}; n = len(out[0][1]); kind = {v: k[0] if isinstance(k, tuple) else k for k, v in V.items()}
    cls = lambda t, v: (out[t][1][v][0], frozenset(x for x in out[t][1][v][1] if x in evs))
    cc = [sum(cls(t, v) != cls(t - 1, v) for t in range(1, T + 1)) for v in range(n)]
    mv = max(range(n), key=lambda v: cc[v]); mh = mf = ff = mx = 0
    for q in O:
        g, a, b = V[("g", q)], V[("e", q)], V[("b", q)]; fl = sum(out[t][2][g] != out[t - 1][2][g] for t in range(1, T + 1)); m = min(cc[a], cc[b])
        mh = max(mh, m); mx = max(mx, fl)
        if fl and m > mf: mf, ff = m, fl
    print(os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), T, cc[mv], kind[mv], mh, mf, ff, mx, flush=True)
