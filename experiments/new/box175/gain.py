#!/usr/bin/env python3
"""L-NEW box 175: gain'(G) := T(G) - max over acyclic re-routings of the couplings (each coupling = a lower option whose Xi-target is a
top mover; re-routed to X or to a lower mover, keeping the Xi-graph acyclic) of T(G - top), G - top = the genome without its top-level
movers, same start on the rest (L-RED R208 definition as relayed by the Lead 2026-11-06 01:27Z). C := number of couplings.
Usage: gain.py files...  (prints C, T(G), best re-routed T(G - top), gain')"""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]

def acyc(N, opts):
    adj = [[o[1] for o in opts[x] if o[1] >= 0] for x in range(N)]; col = [0] * N
    def dfs(v):
        col[v] = 1
        for w in adj[v]:
            if col[w] == 1 or (col[w] == 0 and not dfs(w)): return False
        col[v] = 2; return True
    return all(col[v] or dfs(v) for v in range(N))

def couplings(G):
    tau = max(G["lev"]); top = set(x for x in range(G["N"]) if G["lev"][x] == tau)
    return tau, top, [(x, k) for x in range(G["N"]) if x not in top for k, o in enumerate(G["opts"][x]) if o[1] in top]

def T(G, start=None):
    S, _ = Gen(G).run(start if start is not None else G["start"]); return len(S) - 1

def lower(G, top, rer):
    keep = [x for x in range(G["N"]) if x not in top]; idx = {v: i for i, v in enumerate(keep)}; opts = []
    for x in keep:
        oo = []
        for k, o in enumerate(G["opts"][x]):
            xt = rer.get((x, k), o[1]); oo.append([o[0] if o[0] < 0 else idx[o[0]], xt if xt < 0 else idx[xt], o[2]])
        opts.append(oo)
    return {"N": len(keep), "lev": [G["lev"][v] for v in keep], "opts": opts, "gate": [G["gate"][v] for v in keep], "br": G["br"],
            "bp": G["bp"], "start": [G["start"][v] for v in keep]}

def gainp(G, maxC=2):
    tau, top, cp = couplings(G)
    if len(cp) > maxC: return None
    low = [x for x in range(G["N"]) if x not in top]; best = -1; arg = None
    for choice in itertools.product(*[[-1] + low for _ in cp]):
        rer = dict(zip(cp, choice)); H_ = lower(G, top, rer)
        if not acyc(H_["N"], H_["opts"]): continue
        t = T(H_)
        if t > best: best, arg = t, choice
    return len(cp), T(G), best, T(G) - best, arg

if __name__ == "__main__":
    for f in sys.argv[1:]:
        try: G = json.load(open(f)); assert "opts" in G and "start" in G and max(len(o) for o in G["opts"]) <= 2
        except Exception: continue
        try: r = gainp(G)
        except Exception: continue
        if r: print("%-34s C %d T %3d bestlow %3d gain' %d reroute %s" % (os.path.basename(f)[:34], *r), flush=True)
