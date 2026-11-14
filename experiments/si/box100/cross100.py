#!/usr/bin/env python3
"""L-SI box 100: Lemma TWO-CROSS counters on HOW3 (Gamma3), engine L-RED 65 how3_232 at 59daaef2 (read-only), every gate of every mover,
whole run (states 0..T3). For gate g with faces pe, pbeta: flips = #steps t -> t+1 with sigma-bar(g) changing; ch_e, ch_b = #steps at which
Omega(pe), Omega(pbeta) change. Must-0 (unit gate-step or gate): unm = flips away from face a at a step where Omega(a) does NOT change
(gate-steps); sumf = gates with flips > ch_e + ch_b; minf = gates with flips > 2 min(ch_e, ch_b) + 1; tie = gate-states with equal faces
(NO-TIE3). Descriptive: qflip = flips away from face a at which Lambda(a) does NOT change (quiet flips), qint = those at
internal gates (both targets in the mover's SCC); dmax = max depth of the change of Omega(a) charged to a flip away from a
(depth(): -1 Lambda change; else #Pi elements above the most relevant difference; |Pi| for a length-only change); deep = flips
charged to a change of depth > CMAX (env CMAX; counted only when set); gates with flips >= 2; tight = gates with flips >= 2 and flips = 2 min + 1.
CTRL=1 (control): charge each flip to the face Odd moves TO instead (the claim then is false: unm must fire).
Usage: cross100.py inst G.json ... | cross100.py rand SEED COUNT (rand191.rgen from env LNEW)"""
import sys, os, json, random
R = os.environ["RED"]; sys.path.insert(0, os.path.join(R, "experiments/red/r232"))
import how3_232 as H
CTRL = os.environ.get("CTRL") == "1"
CMAX = int(os.environ["CMAX"]) if "CMAX" in os.environ else None
def depth(a, b, rk):
    # depth of the change a -> b of a value (Lambda, Pi, len): -1 if Lambda changes; else the number of elements of Pi_a (= of Pi_b) more
    # relevant than the most relevant element of Pi_a ^ Pi_b; if Pi_a = Pi_b (length-only change): |Pi_a| (deeper than every Pi change)
    if a[0] != b[0]: return -1
    D = a[1] ^ b[1]
    if not D: return len(a[1])
    z = max(D, key=lambda u: rk[u]); return sum(1 for u in a[1] if rk[u] > rk[z])
def one(G):
    cs, cp, _ = H.sccs(G); comp = dict(enumerate(cp)); rk = H.own.VJ(H.build(G)[0].prio).rk
    full = []; seq = H.how3(G, full=full); T = len(seq) - 1; V = full[0][2]; c = dict(dmax=-1, deep=0, qflip=0, qint=0, gates=0, unm=0, sumf=0, minf=0, tie=0, multi=0, tight=0, maxfl=0)
    for x in range(G["N"]):
        for k in range(len(G["opts"][x])):
            g, pe, pb = V[("g", (x, k))], V[("pe", (x, k))], V[("pbeta", (x, k))]
            ve = [f[0][pe] for f in full]; vb = [f[0][pb] for f in full]; ch = [f[1][g] for f in full]
            c["gates"] += 1; c["tie"] += sum(1 for a, b in zip(ve, vb) if a == b)
            che = sum(1 for t in range(T) if ve[t] != ve[t + 1]); chb = sum(1 for t in range(T) if vb[t] != vb[t + 1])
            fl = 0
            for t in range(T):
                if ch[t] != ch[t + 1]:
                    fl += 1; a = ch[t + 1] if CTRL else ch[t]
                    va = ve if a == pe else vb
                    c["unm"] += va[t] == va[t + 1]
                    d = depth(va[t], va[t + 1], rk); c["dmax"] = max(c["dmax"], d)
                    if CMAX is not None and d > CMAX: c["deep"] += 1
                    if va[t][0] == va[t + 1][0]: c["qflip"] += 1; c["qint"] += int(all(y >= 0 and comp.get(y) == comp.get(x) for y in G["opts"][x][k][:2]))
            c["sumf"] += fl > che + chb; c["minf"] += fl > 2 * min(che, chb) + 1
            if fl >= 2: c["multi"] += 1; c["tight"] += fl == 2 * min(che, chb) + 1
            c["maxfl"] = max(c["maxfl"], fl)
    return T, c
if __name__ == "__main__":
    if sys.argv[1] == "inst":
        L = []
        for f in sys.argv[2:]:
            G = json.load(open(f)); G = G.get("genome", G); G.pop("_evals", None); L.append((os.path.basename(f), G))
    else:
        sys.path[:0] = [os.path.join(os.environ["LNEW"], p) for p in ("experiments/new/box191", "experiments/new")]
        import rand191
        rng = random.Random(int(sys.argv[2])); L = []
        for i in range(int(sys.argv[3])):
            d, w, D = rng.randint(1, 5), rng.randint(1, 3), rng.randint(2, 3); L.append(("r%d" % i, rand191.rgen(rng, d, w, D)))
    tot = {}; n = 0
    for nm, G in L:
        T, c = one(G); n += 1
        for k, v in c.items(): tot[k] = max(tot.get(k, -1), v) if k in ("maxfl", "dmax") else tot.get(k, 0) + v
        if sys.argv[1] == "inst" or c["unm"] or c["sumf"] or c["minf"]: print(nm, "T3", T, c, flush=True)
    print("TOTAL genomes", n, " ".join("%s %d" % kv for kv in tot.items()), flush=True)
