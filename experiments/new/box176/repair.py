#!/usr/bin/env python3
"""L-NEW box 176: repaired TOP-C resources. Per genome (degree <= 2, C >= 0, stored start):
 T, C, gain' (R208: T(G) - max over acyclic re-routings r of T(G^-_r), same start), m = #steps moving a top mover,
 mc = #steps moving a COUPLED top mover (a Xi-target of a coupling) = #proxy changes (R208 TOP-SPLIT proxies), pc = #distinct proxy
 tuples visited, rearm = #steps t that move a coupled top mover after which the lower part moves at t + 1 although no lower option was
 available under s_t with the OLD proxy (lower part stuck before the change), lowseg = #proxy-constant phases containing a lower step.
Usage: repair.py files..."""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
g = {"__file__": os.path.join(H, "..", "box175", "gain.py"), "__name__": "lib"}; exec(open(g["__file__"]).read().split("\nif __name__")[0], g)
Gen = g["Gen"]
def metrics(G, maxr=20000):
    tau, top, cp = g["couplings"](G); low = [x for x in range(G["N"]) if x not in top]; N = G["N"]
    gn = Gen(G); S, AS = gn.run(G["start"]); T = len(S) - 1
    best = -1; nr = 0
    for ch in itertools.product(*[[-1] + low for _ in cp]):
        nr += 1
        if nr > maxr: return None
        Hh = g["lower"](G, top, dict(zip(cp, ch)))
        if not g["acyc"](Hh["N"], Hh["opts"]): continue
        best = max(best, g["T"](Hh))
    cu = sorted(set(G["opts"][x][k][1] for x, k in cp))
    Mv = [None] + [set(x for x in range(N) if S[t][x] != S[t - 1][x]) for t in range(1, T + 1)]
    m = sum(1 for t in range(1, T + 1) if Mv[t] & top); mc = sum(1 for t in range(1, T + 1) if Mv[t] & set(cu))
    pc = len(set(tuple(S[t][u] for u in cu) for t in range(T + 1)))
    lowmv = [None] + [bool(Mv[t] - top) for t in range(1, T + 1)]
    rearm = 0
    for t in range(1, T):
        if Mv[t] & set(cu) and lowmv[t + 1]:
            # lower stuck under the old proxy: no lower mover had a non-singleton A-set at s_t with the coupled top movers as in s_(t-1)
            s_old = list(S[t]); 
            for u in cu: s_old[u] = S[t - 1][u]
            if all(len(gn.avail(tuple(s_old), x)) == 1 for x in low): rearm += 1
    ph, cur, has = 0, None, False
    for t in range(1, T + 1):
        key = tuple(S[t - 1][u] for u in cu)
        if key != cur:
            if has: ph += 1
            cur, has = key, False
        has |= lowmv[t]
    ph += has
    return dict(d=tau + 1, T=T, C=len(cp), gain=T - best, best=best, m=m, mc=mc, pc=pc, rearm=rearm, lowph=ph)
if __name__ == "__main__":
    for f in sys.argv[1:]:
        try: G = json.load(open(f)); assert "opts" in G and "start" in G and max(len(o) for o in G["opts"]) <= 2
        except Exception: continue
        try: r = metrics(G)
        except Exception: continue
        if r: print("%-30s " % os.path.basename(f)[:30] + " ".join("%s %d" % kv for kv in r.items()), flush=True)
