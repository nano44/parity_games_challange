#!/usr/bin/env python3
"""L-RED 65 R232 (c): ONE-CROSS3 on HOW3 (Gamma3), own engine, and its SCC corollary for SCC-LIN.
(1) ONE-CROSS3: gate g with a face (pe_g or pbeta_g) of constant value over the whole run: sigma-bar(g) changes <= 1 time, only toward the
    constant face. Must-0: xfail, dfail, tie.
(2) SCC corollary: for an SCC C of D(G) and t0(C) := max f(C') over SCCs reachable from C, a gate of a mover of C whose W-target or
    Xi-target is not in C (or is X / -1) changes sigma-bar at most once on states >= t0(C). Must-0: sfail. Descriptive: internal gates
    (both targets in C) with >= 2 changes after t0 (the only ones that can flip repeatedly).
Usage: oc3_232.py G.json ..."""
import sys, os, json
from how3_232 import how3, sccs
tot = dict(genomes=0, gates=0, const=0, xfail=0, dfail=0, tie=0, outgates=0, sfail=0, internal_multi=0)
for fn in sys.argv[1:]:
    G = json.load(open(fn)); G.pop("_evals", None); full = []; seq = how3(G, full=full); N = G["N"]; T = len(seq) - 1
    cs, comp, succ = sccs(G); K = len(cs); f = [0] * K
    for t in range(1, T + 1):
        for x in range(N):
            if seq[t][x] != seq[t - 1][x]: f[comp[x]] = t
    reach = []
    for c in range(K):
        r = set()
        for d in succ[c]: r |= {d} | reach[d]
        reach.append(r)
    t0 = [max((f[d] for d in reach[c]), default=0) for c in range(K)]
    V = full[0][2]; c_ = dict(gates=0, const=0, xfail=0, dfail=0, tie=0, outgates=0, sfail=0, internal_multi=0)
    for x in range(N):
        for k, (wt, xt, _) in enumerate(G["opts"][x]):
            g, pe, pb = V[("g", (x, k))], V[("pe", (x, k))], V[("pb", (x, k))] if ("pb", (x, k)) in V else None
            pb = V[("pbeta", (x, k))]
            ve = [fu[0][pe] for fu in full]; vb = [fu[0][pb] for fu in full]; ch = [fu[1][g] for fu in full]
            c_["gates"] += 1; c_["tie"] += sum(1 for a, b in zip(ve, vb) if a == b)
            fl = [(ch[i], ch[i + 1]) for i in range(T) if ch[i] != ch[i + 1]]
            const = [a for a, vs in ((pe, ve), (pb, vb)) if all(v == vs[0] for v in vs)]
            if const:
                c_["const"] += 1; c_["xfail"] += len(fl) >= 2
                if len(const) == 1 and any(a == const[0] for a, _ in fl): c_["dfail"] += 1
            C = comp[x]; inside = lambda y: y >= 0 and comp[y] == C
            fl0 = [i for i in range(0 if os.environ.get("OC_CTRL") == "1" else t0[C], T) if ch[i] != ch[i + 1]]   # OC_CTRL=1: from state 0 (control)
            if not (inside(wt) and inside(xt)):
                c_["outgates"] += 1; c_["sfail"] += len(fl0) >= 2
            elif len(fl0) >= 2: c_["internal_multi"] += 1
    for k, v in c_.items(): tot[k] += v
    tot["genomes"] += 1; print(os.path.basename(fn), "T3", T, c_, flush=True)
print("TOTAL", tot, flush=True)
