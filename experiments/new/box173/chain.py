#!/usr/bin/env python3
"""L-NEW box 173: the alternating Xi-chain genome C_m (2 levels, width m/2): movers a_1 .. a_m, a_i at level 1 (top) for i odd and
level 0 for i even (m even); every mover has degree 2: option 0 ('good') with Xi-target a_(i+1) (X for a_m), beta even of rank 2i,
option 1 ('exit') with Xi-target X, beta odd of rank 2i + 1; gates: option 0 below option 1 (good preferred by keys); both options of
a top mover W-point to a_m (level 0). Start: every mover on option 1. Mover index = i - 1.
Prints T, the step pattern (L lower / T top-only), I = number of maximal top-only runs, and checks the run moves a_m, a_(m-1), ..., a_1
one per step. Usage: chain.py m [out.json]"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]

def chain(m):
    assert m >= 2 and m % 2 == 0
    N = m; lev = [1 if (x + 1) % 2 == 1 else 0 for x in range(N)]; opts = []; gate = []; br = []; bp = []; M = 0
    for x in range(N):
        i = x + 1; xt = x + 1 if x + 1 < N else -1; wt = N - 1 if lev[x] == 1 else -1
        opts.append([[wt, xt, M], [wt, -1, M + 1]]); br += [2 * i, 2 * i + 1]; bp += [0, 1]; gate.append([M, M + 1]); M += 2
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": [1] * N}

def measure(G):
    g = Gen(G); S, _ = g.run(G["start"]); T = len(S) - 1; top = max(G["lev"])
    Mv = [[x for x in range(G["N"]) if S[t][x] != S[t - 1][x]] for t in range(1, T + 1)]
    pat = "".join("T" if all(G["lev"][x] == top for x in mv) else "L" for mv in Mv)
    I = sum(1 for t in range(T) if pat[t] == "T" and (t == 0 or pat[t - 1] == "L"))
    return T, Mv, pat, I

if __name__ == "__main__":
    m = int(sys.argv[1]); G = chain(m); T, Mv, pat, I = measure(G)
    ok = Mv == [[m - t] for t in range(1, m + 1)]
    print("C_%d N %d d %d T %d I %d lower %d pattern %s one-per-step-descending %s" % (m, G["N"], max(G["lev"]) + 1, T, I,
          pat.count("L"), pat, ok))
    if len(sys.argv) > 2: json.dump(G, open(sys.argv[2], "w"))
