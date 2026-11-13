#!/usr/bin/env python3
"""L-COMP box 46 item 2: Ξ-CYCLIC variants of box 212's tower genomes (Ξ-acyclic, O1's domain): one option is ADDED to one mover x, with
Ξ-target x itself (a Ξ self-loop, so R104's Ξ-graph gets a cycle), W-target = the W-target of x's first option, not the start; its gate
index and β rank are the lowest or the highest of the genome (rerank keeps them distinct), its β parity 0 or 1. Movers tried: the first
mover of every 4th level (levels 0, 4, 8, ...). Output: inst/xtower/<tower>_x<x>_g<lo|hi>_b<lo|hi>_p<0|1>.json. Usage: mkx46.py TOWER.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box39")]
from mut39 import flat, unflat, canon
D = os.path.join(H, "inst", "xtower"); os.makedirs(D, exist_ok=True)
for fn in sys.argv[1:]:
    G = json.load(open(fn)); G = canon(G.get("genome", G)); N, lev = G["N"], G["lev"]; base = os.path.basename(fn).split("_")[0]
    firsts = sorted({min(x for x in range(N) if lev[x] == l) for l in set(lev)})[::4]
    for x in firsts:
        for gp in ("lo", "hi"):
            for bp_ in ("lo", "hi"):
                for par in (0, 1):
                    O = flat(G); M = len(O); wt = next(o["wt"] for o in O if o["x"] == x)
                    O.append(dict(x=x, wt=wt, xt=x, gate=(-1 if gp == "lo" else M + 1), br=(-1 if bp_ == "lo" else M + 1), bp=par, st=False))
                    H2 = unflat(N, lev, O); out = os.path.join(D, "%s_x%d_g%s_b%s_p%d.json" % (base, x, gp, bp_, par)); json.dump(H2, open(out, "w"), sort_keys=True)
    print(fn, "levels", len(firsts), "variants", 8 * len(firsts))
