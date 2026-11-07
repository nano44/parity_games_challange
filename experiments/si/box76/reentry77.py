#!/usr/bin/env python3
"""L-SI box 77: RE-ENTRY of fuel chains. For a genome FILE and each level l: D_l := movers of levels <= l; U_l := Xi-targets of upward
options (target level > source level) of movers in D_l; reports the movers of D_l that are Xi-reachable from U_l (static Xi-graph,
all options), with one witness path."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from tw import is_lr
for f in sys.argv[1:]:
    G = json.load(open(f)); assert is_lr(G); N = G["N"]; d = N // 2; lev = G["lev"]
    ch = {x: [G["opts"][x][k][1] for k in range(2) if G["opts"][x][k][1] >= 0] for x in range(N)}
    def path(a, b, seen=None):
        if a == b: return [a]
        seen = seen or set(); seen.add(a)
        for y in ch[a]:
            if y not in seen:
                p = path(y, b, seen)
                if p: return [a] + p
        return None
    print(os.path.basename(f))
    for l in range(0, d - 1):
        D = [x for x in range(N) if lev[x] <= l]
        U = sorted({G["opts"][x][k][1] for x in D for k in range(2) if G["opts"][x][k][1] >= 0 and lev[G["opts"][x][k][1]] > lev[x]})
        U = [y for y in U if lev[y] > l]
        re = [(u, z, path(u, z)) for u in U for z in D if path(u, z)]
        wit = min(re, key=lambda r: len(r[2])) if re else None
        print("  l %d: U_l above l %s; movers of D_l reachable from U_l: %s; witness %s" % (l, U, sorted({z for _, z, _ in re}), wit))
