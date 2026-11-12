#!/usr/bin/env python3
"""L-RED 65 R232 (c): CONJECTURE SCC-LIN (L-SI 50 box 99 §4: «for every genome G and every SCC C of D(G), H(C) ≤ M_C», H(C) the MAXIMUM over
all start strategies of C's movers of the HOW3 run length with exits constant). For genomes whose D(G) is ONE SCC (no exits), H = max over
all mover start vectors of the HOW3 length (own engine, how3_232.how3). Enumerates all starts if their number ≤ LIMIT, else samples SAMPLES
random starts (seed). Prints M_C, H found, the argmax start, and whether H > M_C (SCC-LIN fails) / H > M_C + N.
Usage: hstart232.py G.json [LIMIT SAMPLES SEED]"""
import sys, os, json, itertools, random
from how3_232 import how3, sccs
G = json.load(open(sys.argv[1])); G.pop("_evals", None); N = G["N"]; M = sum(map(len, G["opts"]))
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 20000; smp = int(sys.argv[3]) if len(sys.argv) > 3 else 2000; rng = random.Random(int(sys.argv[4]) if len(sys.argv) > 4 else 1)
cs, comp, succ = sccs(G)
if len(cs) != 1: print(os.path.basename(sys.argv[1]), "not one SCC:", len(cs), "SCCs; sizes", sorted(map(len, cs))[-3:]); sys.exit(0)
degs = [len(o) for o in G["opts"]]; tot = 1
for d in degs: tot *= d
starts = itertools.product(*[range(d) for d in degs]) if tot <= lim else ([rng.randrange(d) for d in degs] for _ in range(smp))
best = (-1, None); hist = {}; k = 0
for st in starts:
    T = len(how3(G, start=list(st))) - 1; hist[T] = hist.get(T, 0) + 1; k += 1
    if T > best[0]: best = (T, list(st))
print(f"{os.path.basename(sys.argv[1])} N {N} M_C {M} starts {k} ({'all' if tot <= lim else 'sampled'} of {tot}) H {best[0]} S3-start T3 {len(how3(G)) - 1} "
      f"argmax {best[1]} SCC-LIN {'FAILS' if best[0] > M else 'holds'} hist {dict(sorted(hist.items()))}", flush=True)
