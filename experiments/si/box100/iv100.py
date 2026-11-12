#!/usr/bin/env python3
"""L-SI box 100: interval decomposition of HOW3's run on the largest SCC C of D(G) (engine as trace100.py: L-RED 65 how3_232 at 59daaef2).
sigma-bar|C := Odd's choices at the gates of C's movers. An interval = a maximal run of states a..b with sigma-bar|C(t) constant (t >= t0(C));
the steps a -> ... -> b + 1 are Howard steps of the one-player game G_C[sigma-bar_a] (Odd fixed). Prints, for C:
  t0, T3, M_C, N_C, #ext gates E, #int gates, Phi_int (total int-gate flips after t0), Phi_ext (ext flips after t0, must be <= E: ONE-CROSS3),
  #intervals (= 1 + #states t > t0 with a sigma-bar|C change), max / mean interval length; Xi-only = whether every D(G) edge inside C comes
  from Xi-targets only (W-targets of C's options never in C); fvs = size of a greedy feedback vertex set of D(G)[C] (an upper bound on k).
Usage: iv100.py G.json ..."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from trace100 import trace
def fvs(nodes, adj):
    nodes = set(nodes); S = 0
    while True:
        # strip sources/sinks repeatedly, then remove the max-degree node if a cycle remains
        ch = True
        while ch:
            ch = False
            for v in list(nodes):
                if not any(w in nodes for w in adj[v]) or not any(v in adj[u] for u in nodes):
                    nodes.discard(v); ch = True
        if not nodes: return S
        v = max(nodes, key=lambda v: sum(1 for w in adj[v] if w in nodes) * sum(1 for u in nodes if v in adj[u]))
        nodes.discard(v); S += 1
for fn in sys.argv[1:]:
    G = json.load(open(fn)); G = G.get("genome", G); G.pop("_evals", None)
    seq, full, cs, comp, C, gates, rows = trace(G); T = len(seq) - 1; N = G["N"]
    big = comp[next(iter(C))]
    reach = set(); st = [big]; adjc = {}
    # t0(C): last switch of a mover outside C that is reachable from C
    adj = [sorted({y for o in G["opts"][x] for y in o[:2] if y >= 0}) for x in range(N)]
    R = set(); st = [x for x in C]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y not in R and y not in C: R.add(y); st.append(y)
            elif y not in R and y in C: R.add(y); st.append(y)
    out = R - C
    t0 = max([t for t, sw, fl in rows if any(x in out for x in sw)] or [0])
    Cg = [g for g in gates if g[0][0] in C]
    E = sum(1 for g in Cg if g[4] == "ext"); I = sum(1 for g in Cg if g[4] == "int")
    pint = sum(1 for t, sw, fl in rows if t > t0 for f in fl if f[0][0] in C and f[1] == "int")
    pext = sum(1 for t, sw, fl in rows if t > t0 for f in fl if f[0][0] in C and f[1] == "ext")
    chg = [t for t, sw, fl in rows if t > t0 and any(f[0][0] in C for f in fl)]
    cuts = [t0] + chg + [T + 1]
    L = [b - a for a, b in zip(cuts, cuts[1:])]
    xionly = all(not (o[0] >= 0 and o[0] in C) for x in C for o in G["opts"][x])
    MC = sum(len(G["opts"][x]) for x in C)
    print(os.path.basename(fn), "T3", T, "t0", t0, "N_C", len(C), "M_C", MC, "E", E, "I", I, "Phi_int", pint, "Phi_ext", pext,
          "intervals", len(L), "maxlen", max(L), "meanlen", round(sum(L) / len(L), 2), "Xi-only", xionly, "fvs<=", fvs(C, adj), flush=True)
