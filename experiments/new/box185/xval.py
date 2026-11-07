#!/usr/bin/env python3
"""L-NEW box 185: cross-check mv.c against box150/check.py Gen (own Python simulator of RESULTS R104's IDEAL model): on each genome
(text format), over ALL starts: Tmax, per-level max moves of Xi-target movers, and REDUCE (T <= 1 + #steps moving a Xi-target).
Usage: xval.py mvbinary genome.txt ...  (prints MATCH / MISMATCH per genome)"""
import os, sys, itertools, subprocess
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def read_txt(p):
    L = {}
    for line in open(p):
        w = line.split()
        if w: L[w[0]] = [int(x) for x in w[1:]]
    m = L["m"][0]; N = 2 * (m + 1); xt = L["xt"]; lev = [v // 2 for v in range(N)]
    opts = [[[2 * (lev[x] - 1) + k if lev[x] > 0 else -1, xt[2 * x + k], 2 * x + k] for k in range(2)] for x in range(N)]
    gate = [[L["gate"][2 * x], L["gate"][2 * x + 1]] for x in range(N)]
    return m, {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": L["br"], "bp": L["bp"], "start": [0] * N}
bad = 0
for f in sys.argv[2:]:
    m, G = read_txt(f); g = Gen(G); N = G["N"]; d = m + 1
    isT = [any(G["opts"][v][k][1] == z for v in range(N) for k in range(2)) for z in range(N)]
    Tmax = 0; lm = [0] * d; viol = 0
    for st in itertools.product((0, 1), repeat=N):
        S, _ = g.run(st); T = len(S) - 1; Tmax = max(Tmax, T); c = 0
        for t in range(1, T + 1):
            mv = [x for x in range(N) if S[t][x] != S[t - 1][x]]; c += any(isT[x] for x in mv)
        viol += T > 1 + c
        for z in range(N):
            if isT[z]: lm[z // 2] = max(lm[z // 2], sum(S[t][z] != S[t - 1][z] for t in range(1, T + 1)))
    out = subprocess.run([sys.argv[1], "eval", str(m)], stdin=open(f), capture_output=True, text=True).stdout.split()
    cT = int(out[out.index("Tmax") + 1]); i = out.index("levmax"); clm = list(map(int, out[i + 1:i + 1 + d])); cv = int(out[out.index("REDUCE_viol") + 1])
    ok = (cT, clm, cv) == (Tmax, lm, viol); bad += not ok
    print("MATCH" if ok else "MISMATCH", os.path.basename(f), "py", Tmax, lm, viol, "c", cT, clm, cv)
print("TOTAL mismatches", bad)
