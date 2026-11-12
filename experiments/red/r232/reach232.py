#!/usr/bin/env python3
"""L-RED 65 R232 (vs L-SI 50 box 99 SCC-RED §1): on Gamma3(G) (r230/elev230.build = L-NEW gamma3 at l-new fcba92fc via env LNEW), the
set of movers reachable from each mover x over ALL edges of Gamma3 (an over-approximation of every positional pair's play), versus the
set reachable in D(G) (x -> W-target, x -> Xi-target, movers only). reachfail = movers x whose Gamma3-reachable movers are not all
D(G)-reachable from x (must be 0 for §1). Also lists the non-mover vertices with an edge INTO a mover. Usage: reach232.py G.json ..."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r230"))
from elev230 import build
def dreach(G):
    N = G["N"]; adj = [{y for o in G["opts"][x] for y in (o[0], o[1]) if y >= 0} for x in range(N)]; R = []
    for x in range(N):
        seen = set(); st = list(adj[x])
        while st:
            y = st.pop()
            if y not in seen: seen.add(y); st.extend(adj[y])
        R.append(seen)
    return R
def g3reach(G):
    gm, sig, tau, V, O = build(G); N = G["N"]; n = gm.n; R = []
    into = sorted({u for u in range(n) if u >= N for w in gm.succ[u] if w < N})
    for x in range(N):
        seen = set(); st = [w for w in gm.succ[x]]
        while st:
            u = st.pop()
            if u not in seen: seen.add(u); st.extend(gm.succ[u])
        R.append({u for u in seen if u < N})
    inv = {v: k for k, v in V.items()}
    return R, [inv.get(u, u) for u in into]
if __name__ == "__main__":
    tot = dict(genomes=0, movers=0, reachfail=0, selfdiff=0)
    for f in sys.argv[1:]:
        G = json.load(open(f)); G.pop("_evals", None)
        if not (isinstance(G, dict) and "opts" in G): continue
        D = dreach(G); R3, into = g3reach(G); bad = [x for x in range(G["N"]) if not R3[x] <= (D[x] | {x})]
        sd = sum(1 for x in range(G["N"]) if (x in R3[x]) != (x in D[x]))
        tot["genomes"] += 1; tot["movers"] += G["N"]; tot["reachfail"] += len(bad); tot["selfdiff"] += sd
        if bad or sd: print(os.path.basename(f), "reachfail movers", bad[:10], "selfdiff", sd, "non-movers with an edge into a mover:", into[:12])
    print("TOTAL", tot)
