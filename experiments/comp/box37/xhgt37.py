#!/usr/bin/env python3
"""L-COMP box 37: cross-check of MY D_mov / T / D_face / D_minface / maxflip (ideal37.py) against L-NEW's IDEAL-CYC engine
(box203 gfc203.hist_ideal, as used by box204 k1eq204.py; checkout of claude/l-new 3a492186 at env LNEW, read only).
L-NEW side: class(v, t) = (H[t][0][v][0], H[t][0][v][1] & emask) exactly as k1eq204.run's cl; D^tot = number of distinct classes;
D_mov = max over V[("x", x)]; flips from H[t][1] at V[("g", q)]. Per genome: both rows and MATCH/MISMATCH (also per-mover D^tot).
Usage: LNEW=<dir> xhgt37.py G.json ..."""
import sys, os, json
H0 = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H0)
import ideal37
L = os.environ["LNEW"]; sys.path[:0] = [os.path.join(L, "experiments/new", d) for d in ("box203", "box191", "box189", "box190")]
import gfc203
def theirs(G):
    H, n, E, V, gates = gfc203.hist_ideal(G); T = len(H) - 1; emask = 0
    for k, v in V.items():
        if isinstance(k, tuple) and k[0] == "e": emask |= E.bit[v]
    cl = lambda v, t: (H[t][0][v][0], H[t][0][v][1] & emask)
    D = lambda v: len({cl(v, t) for t in range(T + 1)})
    Dall = {x: D(V[("x", x)]) for x in range(G["N"])}
    df = dmin = 0; mf = 0
    for gv, (q, a, b) in gates.items():
        da, db = D(a), D(b); df = max(df, da, db); dmin = max(dmin, min(da, db))
        mf = max(mf, sum(H[t - 1][1][gv] != H[t][1][gv] for t in range(1, T + 1)))
    return dict(T=T, Dmov=max(Dall.values()), Dface=df, Dminface=dmin, maxflip=mf), Dall
bad = 0
for f in sys.argv[1:]:
    G = json.load(open(f)); m = ideal37.heights(G); Dm = m.pop("Dall"); t, Dt = theirs(G)
    keys = ("T", "Dmov", "Dface", "Dminface", "maxflip"); ok = all(m[k] == t[k] for k in keys) and Dm == Dt
    nmov = sum(Dm[x] != Dt[x] for x in Dm); bad += not ok
    print(os.path.basename(f), "N+M", G["N"] + sum(map(len, G["opts"])), "MINE", {k: m[k] for k in keys}, "LNEW", t,
          "per-mover D^tot mismatches", nmov, "MATCH" if ok else "MISMATCH", flush=True)
print("genomes", len(sys.argv) - 1, "mismatching genomes", bad)
