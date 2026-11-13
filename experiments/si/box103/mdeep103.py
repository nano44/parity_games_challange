#!/usr/bin/env python3
"""L-SI box 103: MOVER-DEEP3 by Xi-feedback number. HOW3 on Gamma3 (engine L-RED 65 how3_232 at claude/l-red 59daaef2, env RED). For each
non-trivial SCC C of D(G): k := size of a greedy feedback vertex set of D(G)[C] (an upper bound; = 1 exact when it returns 1); for t >= t0(C),
every value change of a mover y in C at fixed Lambda, with e-depth := #e-vertices of Pi_t(y) above z (z = most relevant element of the Pi
difference). Counters per k-class (k = 1, k >= 2): ch (changes at fixed Lambda), lenonly (Pi unchanged: length-only; NOT in md / maxed, bounded
by n3 per (Lambda, Pi) plateau), md1 / md2 (Pi-changes of e-depth > 1 / > 2), maxed (max e-depth of a Pi-change); each Pi-change is also classed lossy (some e-vertex of Pi_t lost), gain (E grows
by inclusion only) or esame (E unchanged; z not an e-vertex), with *_d1 = those of e-depth > 1; lostE (must 0, R125 (k) E-MON3 via E-DOM: the change's z is an e-vertex that is LOST, i.e. z in Pi_t \\ Pi_(t+1)).
Usage: mdeep103.py inst G.json ... | mdeep103.py rand SEED COUNT (rand191.rgen, env LNEW)"""
import sys, os, json, random
sys.path.insert(0, os.path.join(os.environ["RED"], "experiments/red/r232"))
import how3_232 as H
def fvs(nodes, adj):
    nodes = set(nodes); S = 0
    while True:
        ch = True
        while ch:
            ch = False
            for v in list(nodes):
                if not any(w in nodes for w in adj[v]) or not any(v in adj[u] for u in nodes):
                    nodes.discard(v); ch = True
        if not nodes: return S
        v = max(nodes, key=lambda v: sum(1 for w in adj[v] if w in nodes) * sum(1 for u in nodes if v in adj[u]))
        nodes.discard(v); S += 1
def one(G, tot):
    full = []; seq = H.how3(G, full=full); T = len(seq) - 1; V = full[0][2]; N = G["N"]
    gm = H.build(G)[0]; inv = {v: k for k, v in V.items()}; rk = H.own.VJ(gm.prio).rk
    isE = lambda u: isinstance(inv.get(u), tuple) and inv[u][0] == "e"
    cs, comp, succ = H.sccs(G); K = len(cs); f = [0] * K
    adj = [sorted({y for o in G["opts"][x] for y in o[:2] if y >= 0}) for x in range(N)]
    for t in range(1, T + 1):
        for x in range(N):
            if seq[t][x] != seq[t - 1][x]: f[comp[x]] = t
    reach = []
    for c in range(K):
        r = set()
        for d in succ[c]: r |= {d} | reach[d]
        reach.append(r)
    t0 = [max((f[d] for d in reach[c]), default=0) for c in range(K)]
    for c in range(K):
        if len(cs[c]) < 2 and not any(cs[c][0] in adj[cs[c][0]] for _ in [0]): continue
        k = fvs(cs[c], adj); cls = "k1" if k == 1 else "k2+"; tot[cls]["sccs"] += 1
        for y in cs[c]:
            X = V[("x", y)]
            for t in range(t0[c], T):
                va, vb = full[t][0][X], full[t + 1][0][X]
                if va == vb or va[0] != vb[0]: continue
                tot[cls]["ch"] += 1; D = va[1] ^ vb[1]
                if D:
                    z = max(D, key=lambda u: rk[u]); d = sum(1 for u in va[1] if isE(u) and rk[u] > rk[z])
                    Ea = {u for u in va[1] if isE(u)}; Eb = {u for u in vb[1] if isE(u)}
                    kind = "lossy" if Ea - Eb else ("gain" if Eb - Ea else "esame")
                    tot[cls][kind] += 1
                    if d > 1: tot[cls][kind + "_d1"] += 1
                    if isE(z) and z in va[1]: tot[cls]["lostE"] += 1
                else:
                    tot[cls]["lenonly"] += 1; continue
                tot[cls]["md1"] += d > 1; tot[cls]["md2"] += d > 2; tot[cls]["maxed"] = max(tot[cls]["maxed"], d)
    return T
if __name__ == "__main__":
    if sys.argv[1] == "inst":
        L = []
        for fn in sys.argv[2:]:
            G = json.load(open(fn)); G = G.get("genome", G); G.pop("_evals", None); L.append((os.path.basename(fn), G))
    else:
        sys.path[:0] = [os.path.join(os.environ["LNEW"], p) for p in ("experiments/new/box191", "experiments/new")]
        import rand191
        rng = random.Random(int(sys.argv[2])); L = []
        for i in range(int(sys.argv[3])):
            d, w, D = rng.randint(1, 5), rng.randint(1, 3), rng.randint(2, 3); L.append(("r%d" % i, rand191.rgen(rng, d, w, D)))
    TOT = {c: dict(sccs=0, ch=0, lenonly=0, lossy=0, lossy_d1=0, gain=0, gain_d1=0, esame=0, esame_d1=0, md1=0, md2=0, maxed=-1, lostE=0) for c in ("k1", "k2+")}
    for nm, G in L:
        tot = {c: dict(sccs=0, ch=0, lenonly=0, lossy=0, lossy_d1=0, gain=0, gain_d1=0, esame=0, esame_d1=0, md1=0, md2=0, maxed=-1, lostE=0) for c in ("k1", "k2+")}
        T = one(G, tot)
        for c in tot:
            for kk, v in tot[c].items(): TOT[c][kk] = max(TOT[c][kk], v) if kk == "maxed" else TOT[c][kk] + v
        if sys.argv[1] == "inst": print(nm, "T3", T, tot, flush=True)
    print("TOTAL genomes", len(L), TOT, flush=True)
