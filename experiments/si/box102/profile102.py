#!/usr/bin/env python3
"""L-SI box 102 profile: every flip charged to depth > 3 (all gates, whole run), with gate kind (int / ext), before / after t0(C), the face
Odd leaves, z and the common Pi elements above z (core K0 / K3 shown as K0 / K3). Engine as deep102.py (env RED). Usage: profile102.py G.json ..."""
import sys, os, json
sys.path.insert(0, os.path.join(os.environ["RED"], "experiments/red/r232"))
import how3_232 as H
CM = 3
for fn in sys.argv[1:]:
    G = json.load(open(fn)); G = G.get("genome", G); G.pop("_evals", None)
    full = []; seq = H.how3(G, full=full); T = len(seq) - 1; V = full[0][2]
    gm = H.build(G)[0]; inv = {v: k for k, v in V.items()}; rk = H.own.VJ(gm.prio).rk
    cs, comp, succ = H.sccs(G); K = len(cs); f = [0] * K
    for t in range(1, T + 1):
        for x in range(G["N"]):
            if seq[t][x] != seq[t - 1][x]: f[comp[x]] = t
    reach = []
    for c in range(K):
        r = set()
        for d in succ[c]: r |= {d} | reach[d]
        reach.append(r)
    t0 = [max((f[d] for d in reach[c]), default=0) for c in range(K)]
    def kind(x, k):
        wt, xt, _ = G["opts"][x][k]; C = comp[x]
        return "int" if (wt >= 0 and xt >= 0 and comp[wt] == C and comp[xt] == C) else "ext"
    rows = []; edep = {}
    for x in range(G["N"]):
        for k in range(len(G["opts"][x])):
            g, pe, pb = V[("g", (x, k))], V[("pe", (x, k))], V[("pbeta", (x, k))]
            for t in range(T):
                a = full[t][1][g]
                if a == full[t + 1][1][g]: continue
                va, vb = full[t][0][a], full[t + 1][0][a]
                if va[0] != vb[0]: continue
                D = va[1] ^ vb[1]
                if not D: d = len(va[1]); z = None; above = sorted(va[1], key=lambda u: -rk[u])
                else:
                    z = max(D, key=lambda u: rk[u]); above = sorted([u for u in va[1] if rk[u] > rk[z]], key=lambda u: -rk[u]); d = len(above)
                ne = sum(1 for u in above if inv[u][0] == "e")
                edep[ne] = edep.get(ne, 0) + 1
                if d > CM:
                    rows.append((t, (x, k), kind(x, k), "after" if t >= t0[comp[x]] else "before", "pe" if a == pe else "pb",
                                 inv.get(z, "LEN") if z is not None else "LEN", [inv[u] if inv[u][0] != "K" else inv[u][0] + str(inv[u][1]) for u in above]))
    print("==", os.path.basename(fn), "T3", T, "deep", len(rows), "e-depth histogram (all quiet charged changes):", dict(sorted(edep.items())))
    for r in rows[:30]: print("  t%d gate%s %s %s leave %s z=%s above=%s" % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
