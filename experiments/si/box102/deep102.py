#!/usr/bin/env python3
"""L-SI box 102: DEEP3's exact quantity on HOW3 (Gamma3), engine L-RED 65 how3_232 at claude/l-red 59daaef2 (read-only, env RED).
For every flip of an INTERNAL gate g (both targets in the SCC C of its mover) at a step t >= t0(C) (box 99 §2: max f over the SCCs reachable
from C), TWO-CROSS charges it to the change of the face a that Odd leaves. Its e-depth := #e-vertices of Pi_t(a) more relevant than z, the
most relevant element of Pi_t(a) ^ Pi_(t+1)(a) (-1 if Lambda(a) changes; for a length-only change, #e-vertices of Pi_t(a)). Also checked:
'abovefail' = charged changes with an element above z that is neither an e-vertex nor K0, K3, cW (must be 0: then depth = e-depth + #core).
Per genome: nflip (internal flips after t0), histogram of e-depths, D1 / D2 = flips of e-depth > 1 / > 2, maxpg = max over gates of flips
with e-depth > 1. propfail (must 0) = charged face changes whose e-depth is neither the e-depth of the same step's change at the
face's target mover (W-target for pe, Xi-target for pbeta) nor one more (Lemma PROPAGATE); mch / mD1 = value changes at movers of
non-trivial SCCs after t0 / those with e-depth > 1 (the mover form). Usage: deep102.py inst G.json ... | deep102.py rand SEED COUNT (rand191.rgen from env LNEW)"""
import sys, os, json, random
sys.path.insert(0, os.path.join(os.environ["RED"], "experiments/red/r232"))
import how3_232 as H
PCTRL = os.environ.get("PCTRL") == "1"   # control: take the OTHER face's target in PROPAGATE (propfail must fire)
def one(G):
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
    isE = lambda u: isinstance(inv.get(u), tuple) and inv[u][0] == "e"
    core = {V[("K", 0)], V[("K", 3)], V["cW"]}
    c = dict(nflip=0, D1=0, D2=0, maxpg=0, abovefail=0, lam=0, propfail=0, mch=0, mD1=0); hist = {}
    def edep(va, vb):
        if va[0] != vb[0]: return -1, None
        D = va[1] ^ vb[1]
        if not D: return sum(1 for u in va[1] if isE(u)), None
        z = max(D, key=lambda u: rk[u]); return sum(1 for u in va[1] if isE(u) and rk[u] > rk[z]), z
    # movers of non-trivial SCCs after t0: value changes and their e-depth (mover form)
    for x in range(G["N"]):
        C = comp[x]
        if len(cs[C]) < 2: continue
        X = V[("x", x)]
        for t in range(t0[C], T):
            va, vb = full[t][0][X], full[t + 1][0][X]
            if va == vb: continue
            c["mch"] += 1; d, _ = edep(va, vb)
            if d > 1: c["mD1"] += 1
    for x in range(G["N"]):
        for k, (wt, xt, _) in enumerate(G["opts"][x]):
            C = comp[x]
            if not (wt >= 0 and xt >= 0 and comp[wt] == C and comp[xt] == C): continue
            g = V[("g", (x, k))]; pg = 0
            for t in range(t0[C], T):
                a = full[t][1][g]
                if a == full[t + 1][1][g]: continue
                c["nflip"] += 1; va, vb = full[t][0][a], full[t + 1][0][a]
                if va[0] != vb[0]: c["lam"] += 1; hist[-1] = hist.get(-1, 0) + 1; continue
                D = va[1] ^ vb[1]
                if D:
                    z = max(D, key=lambda u: rk[u]); above = [u for u in va[1] if rk[u] > rk[z]]
                else: above = list(va[1])
                c["abovefail"] += sum(1 for u in above if not isE(u) and u not in core)
                d = sum(1 for u in above if isE(u)); hist[d] = hist.get(d, 0) + 1
                # PROPAGATE: the face's change has the e-depth of its target mover's change, or one more (own e above z)
                tg = wt if (a == V[("pe", (x, k))]) != PCTRL else xt
                dt, zt = edep(full[t][0][V[("x", tg)]], full[t + 1][0][V[("x", tg)]])
                c["propfail"] += int(not (d == dt or d == dt + 1))
                if d > 1: c["D1"] += 1; pg += 1
                if d > 2: c["D2"] += 1
            c["maxpg"] = max(c["maxpg"], pg)
    return T, c, hist
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
    tot = dict(nflip=0, D1=0, D2=0, maxpg=0, abovefail=0, lam=0, propfail=0, mch=0, mD1=0); th = {}
    for nm, G in L:
        T, c, h = one(G)
        for k, v in c.items(): tot[k] = max(tot[k], v) if k == "maxpg" else tot[k] + v
        for k, v in h.items(): th[k] = th.get(k, 0) + v
        if sys.argv[1] == "inst" or c["abovefail"] or c["D2"]: print(nm, "T3", T, c, "edepth", dict(sorted(h.items())), flush=True)
    print("TOTAL genomes", len(L), " ".join("%s %d" % kv for kv in tot.items()), "edepth", dict(sorted(th.items())), flush=True)
