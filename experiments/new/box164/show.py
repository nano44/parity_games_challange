#!/usr/bin/env python3
"""print a run with per-move records (x, old->new, decisive beta (rank, parity), on which chain). Usage: show.py file.json"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "rec.py")).read().split("\nif __name__")[0])
G = json.load(open(sys.argv[1])); g = Gen(G); S, _ = g.run(G["start"])
print("N", g.N, "T", len(S) - 1, "lev", g.lev)
for t in range(1, len(S)):
    a, b = S[t - 1], S[t]; out = []
    for x in range(g.N):
        if a[x] != b[x]:
            P, Q = chain(g, a, x, b[x]), chain(g, a, x, a[x]); m = decisive(g, P, Q)
            out.append("x%d(l%d) %d->%d dec beta%d r%d p%d %s" % (x, g.lev[x], a[x], b[x], m, g.br[m], g.bp[m], "new" if m in P else "old"))
    print("t %2d %s -> %s : %s" % (t, "".join(map(str, a)), "".join(map(str, b)), "; ".join(out)))
