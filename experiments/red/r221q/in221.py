#!/usr/bin/env python3
"""L-RED 56 R221: IN check (box 194 §7): max over vertices v and maximal stretches with constant class (Lambda, E) of the number of
distinct values Omega_t(v) in the stretch (own implementation). Usage: in221.py G.json ..."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
for f in sys.argv[1:]:
    G = json.load(open(f)); out, V, O, _ = own.run(G); n = len(out[0][1]); evs = {V[("e", q)] for q in O}; best = (0, None)
    for v in range(n):
        t = 0
        while t < len(out):
            c = (out[t][1][v][0], frozenset(u for u in out[t][1][v][1] if u in evs)); u = t
            while u + 1 < len(out) and (out[u + 1][1][v][0], frozenset(x for x in out[u + 1][1][v][1] if x in evs)) == c: u += 1
            d = len({out[i][1][v] for i in range(t, u + 1)})
            if d > best[0]: best = (d, v)
            t = u + 1
    print(f.split('/')[-1], "N", G["N"], "max distinct values in one constant-class stretch", best[0], "at vertex", best[1], flush=True)
