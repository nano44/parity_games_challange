#!/usr/bin/env python3
"""L-NEW box 160, DATA: per-level counts on 2-wide degree-2 ladders (every level: exactly two degree-2 movers, no others).
b_l(s) := [key_s(m0_l) < key_s(m1_l)] (key order of the two level-l movers' current options). F_l := #steps t with b_l(s_t) != b_l(s_(t-1)).
mv_l := number of (mover, step) moves at level l. Prints per run the vectors F, mv, and the max of F_l - F_(l-1).
ALL=1: every start. Usage: flips.py genome.json ..."""
import sys, os, json, itertools
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box150", "check.py")
ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def ladder(G):
    d = max(G["lev"]) + 1
    if any(len(o) != 2 for o in G["opts"]): return None
    L = [[v for v in range(G["N"]) if G["lev"][v] == l] for l in range(d)]
    return L if all(len(x) == 2 for x in L) else None
def stats(G, st):
    g = Gen(G); L = ladder(G); d = len(L); S, AS = g.run(st); T = len(S) - 1
    B = []
    for s in S:
        key = g.keys(s); B.append([int(key[L[l][0]] < key[L[l][1]]) for l in range(d)])
    F = [sum(1 for t in range(1, T + 1) if B[t][l] != B[t - 1][l]) for l in range(d)]
    mv = [sum(1 for t in range(1, T + 1) for v in L[l] if S[t][v] != S[t - 1][v]) for l in range(d)]
    C = [sum(1 for t in range(1, T + 1) if any(S[t][v] != S[t - 1][v] for ll in range(l + 1) for v in L[ll])) for l in range(d)]
    return T, F, mv, C, S, B
if __name__ == "__main__":
    best = {}; quiet = os.environ.get("Q")
    for f in sys.argv[1:]:
        G = json.load(open(f))
        if ladder(G) is None: continue
        d = max(G["lev"]) + 1
        starts = [G["start"]] if not os.environ.get("ALL") else [list(x) for x in itertools.product([0, 1], repeat=G["N"])]
        for st in starts:
            T, F, mv, C, S, B = stats(G, st)
            inc = max([F[l] - F[l - 1] for l in range(1, d)] or [0])
            k = d; b = best.setdefault(k, dict(T=0, inc=-9, Fmax=[0]*d, mvmax=[0]*d))
            if T > b["T"]: b["T"], b["Tf"] = T, (os.path.basename(f), F, mv, C)
            if inc > b["inc"]: b["inc"], b["incf"] = inc, (os.path.basename(f), T, F, mv)
            b["Fmax"] = [max(a, c) for a, c in zip(b["Fmax"], F)]; b["mvmax"] = [max(a, c) for a, c in zip(b["mvmax"], mv)]
            if not quiet: print(f"{os.path.basename(f)} d {d} T {T} F {F} mv {mv} C {C} incF {inc}")
    for k in sorted(best): print("BEST d", k, best[k])
