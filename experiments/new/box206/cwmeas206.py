#!/usr/bin/env python3
"""Box 206 Addendum C (L-NEW successor 70): exact measures of a genome family on IDEAL-CYC: k (fvs202), N, M, b (top-block size), Dtop
(block206), D_mov := max over movers of the number of distinct classes (Lambda, E) over the run, T. Usage: cwmeas206.py G.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "box203"), os.path.join(HERE, "..", "box202")]
import block206, fvs202, gfc203
for f in sys.argv[1:]:
    G = json.load(open(f)); r = block206.census(G); H, n, E, V, gates = gfc203.hist_ideal(G)
    em = 0
    for k, v in V.items():
        if isinstance(k, tuple) and k[0] == "e": em |= E.bit[v]
    Dm = max(len({(H[t][0][V[("x", x)]][0], H[t][0][V[("x", x)]][1] & em) for t in range(len(H))}) for x in range(G["N"]))
    M = sum(len(o) for o in G["opts"])
    print(os.path.basename(f), "k", fvs202.kfvs(G)[0], "N", G["N"], "M", M, "N+M", G["N"] + M, "b", r["b"], "Dtop", r["Dtop"], "D_mov", Dm, "T", r["T"], flush=True)
