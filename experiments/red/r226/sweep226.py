#!/usr/bin/env python3
"""L-RED 60 R226: depth-2 sweep. G0 = union(CX4, CX4, gmode); every single Xi-rewire of a copy-B option to a copy-A mover
(and A -> B); print the top results by (T, maxD). Usage: sweep226.py CX4.json OUT.txt"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compose226 import *
A = json.load(open(sys.argv[1])); res = []
for gm in ("above", "below", "inter"):
    G0 = union(A, A, gm); m0 = measure(G0); res.append((m0["T"], m0["maxD"], gm, "base", m0))
    NA = A["N"]
    for (src, dst) in ((range(NA, 2 * NA), range(NA)), (range(NA), range(NA, 2 * NA))):
        for x in src:
            for k in range(len(G0["opts"][x])):
                for y in list(dst):
                    G = rewire(G0, x, k, 1, y)
                    try: m = measure(G)
                    except AssertionError: continue
                    res.append((m["T"], m["maxD"], gm, (x, k, y), m))
res.sort(key=lambda r: (r[0], r[1]), reverse=True)
with open(sys.argv[2], "w") as f:
    for r in res[:60]: print(r, file=f)
    import collections; print("T histogram", sorted(collections.Counter(r[0] for r in res).items()), file=f)
print("done", len(res))
