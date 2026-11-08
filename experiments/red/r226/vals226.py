#!/usr/bin/env python3
"""L-RED 60 R226: print, per step, the value (Lambda | Pi e-sequence in play order) of the named movers. Usage: vals226.py G.json x0 x9 ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221")]
import own
G = json.load(open(sys.argv[1])); N = G['N']; xs = [int(a[1:]) for a in sys.argv[2:]]
out, V, O, ow = own.run(G); n, prio, o_, succ, _, _ = own.build(G); inv = {v: k for k, v in V.items()}; evs = {V[("e", q)] for q in O}
lab = lambda e: "e%d.%d" % inv[e][1]
for t, (s, vals, tau) in enumerate(out):
    nxt = lambda u: (s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0])); row = []
    for x in xs:
        seq = []; seen = set(); u = x
        while u not in seen:
            seen.add(u)
            if u in evs and u in vals[x][1]: seq.append(lab(u))
            u = nxt(u)
        l = inv.get(vals[x][0]); row.append("x%d=%s:%s" % (x, l if isinstance(l, str) else l, ",".join(seq)))
    print("%2d" % t, "  ".join(row))
