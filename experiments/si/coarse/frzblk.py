#!/usr/bin/env python3
"""L-SI box 9: DATA for the bridge to L-NEW box 34 (docs/si/N5-C-box9.md §7). In a phase (λ_Ξ and τ constant) of an o-cyclic 𝒞^1O
game, for each ℓ >= 0 with a FREEZE window (n consecutive (h) states with r <= ℓ, docs/new/N5-REL-box34.md §3) ending at F, take the
maximal runs I of consecutive (h) states after F with r = ℓ (L-NEW's r = ℓ intervals; w may change). Inside I:
  (MONO-I) fallback levels non-increasing and <= ℓ;  (TOP) #fallbacks at level ℓ <= n_E;
  (PL-I) per level M < ℓ: N_M <= n_E(1 + D_M), D_M = #intervals between consecutive level-M fallbacks with a COARSE_M change;
  counts: fallbacks, evictions (R -> F tails), (L1) re-entries into R at S4a steps of vertices evicted at a fallback of I, D_M.
Own engine path (mono.states, asserted equal to n5.run). Usage: frzblk.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rfinv import *
from collections import Counter

def scan_f(g, name):
    E, out = states(g); n = g.n; o = odd_choice(g); assert o is not None, f"{name}: not one-Odd-choice"
    nE = sum(1 for v in range(n) if g.owner[v] == 0); C = Counter(); ex = []
    for a in out:
        a["ph"] = (tuple(x[0] for x in a["Xi"]), a["t"])
        _, W = wvals(g, a["s"], a["t"]); a["W"] = W; a["R"] = reach(g, a["s"], a["t"], o)
        a["h"] = (not oncycle(g, a["s"], a["sb"], o)) and (not oncycle(g, a["s"], a["t"], o)) and a["Xi"][o][0] == W[o][0]
        a["r"] = lev(a["Xi"][o], W[o]) if a["h"] else None
        a["gl"] = [(y, z, lev(a["Xi"][a["s"][y]], a["Xi"][z])) for y, z in a["Is"]]
        a["M"] = max([l for *_, l in a["gl"]] or [-3])
    K = len(out)
    for l in range(0, n):
        F = None
        for s in range(0, K - n + 1):
            if all(out[k]["h"] and out[k]["r"] <= l and out[k]["ph"] == out[s]["ph"] for k in range(s, s + n)): F = s + n - 1; break
        if F is None: continue
        t = F
        while t < K:
            if not (out[t]["h"] and out[t]["r"] == l and out[t]["ph"] == out[F]["ph"]): t += 1; continue
            I = [t]
            while I[-1] + 1 < K and out[I[-1] + 1]["h"] and out[I[-1] + 1]["r"] == l and out[I[-1] + 1]["ph"] == out[F]["ph"]: I.append(I[-1] + 1)
            t = I[-1] + 1
            fbs = [k for k in I[:-1] if out[k]["fb"]]
            if not fbs: continue
            C["blocks"] += 1; C["fb"] += len(fbs)
            lv = [out[k]["M"] for k in fbs]
            if any(m > l for m in lv) or any(y > x for x, y in zip(lv, lv[1:])): C["mono_viol"] += 1; ex.append((name, "MONO-I", l, lv))
            if lv.count(l) > nE: C["top_viol"] += 1; ex.append((name, "TOP", l, lv.count(l)))
            ev = set(); L1 = 0
            for k in I[:-1]:
                a, b = out[k], out[k + 1]
                if a["fb"]:
                    e = {y for y, z, lg in a["gl"] if y in a["R"] and y not in b["R"]}; ev |= e; C["evict"] += len(e)
                else:
                    L1 += sum(1 for y in ev if y not in a["R"] and y in b["R"])
            C["L1"] += L1; C["max_L1"] = max(C["max_L1"], L1); C["max_fb"] = max(C["max_fb"], len(fbs))
            for M in sorted(set(lv)):
                bl = [k for k in fbs if out[k]["M"] == M]; D = 0
                for k1, k2 in zip(bl, bl[1:]):
                    if any(any(coarse(out[u + 1]["Xi"][v], M) != coarse(out[u]["Xi"][v], M) for v in range(n)) for u in range(k1 + 1, k2)): D += 1
                C["D"] += D; C["lvl_blocks"] += 1
                if len(bl) > nE * (1 + D): C["pl_viol"] += 1; ex.append((name, "PL-I", l, M, len(bl), D))
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan_f(load(p), os.path.basename(p)); X += e
        for k, v in c.items(): T[k] = max(T[k], v) if k.startswith("max") else T[k] + v
    print("TOTAL", dict(T))
    for e in X[:20]: print("  ", e)
