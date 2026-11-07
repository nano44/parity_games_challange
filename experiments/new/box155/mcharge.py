#!/usr/bin/env python3
"""L-NEW box 155: check of Lemma MULTI-CHARGE on simulated IDEAL-ACYC runs (any degree): every unchained step t >= 2 (P-IDEAL-RED
CHAIN-BACK labels) has |Mv_(t-1)| >= 2; hence U <= M2 := #{t <= T-1 : |Mv_t| >= 2} and T <= N (1 + M2). Prints totals and
violations (must be 0). ALL=1: every start for N <= ALLN. Usage: mcharge.py genome.json ..."""
import sys, os, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]; labels = ns["labels"]
tot = dict(runs=0, steps=0, unch=0, M2=0, VIOL=0, BOUND=0, single_runs=0, single_maxT_over_N=0.0)
for p in sys.argv[1:]:
    G = json.load(open(p)); g = Gen(G)
    starts = [G["start"]]
    if os.environ.get("ALL") and G["N"] <= int(os.environ.get("ALLN", "8")):
        starts = [list(s) for s in itertools.product(*[range(len(o)) for o in G["opts"]])]
    for st in starts:
        S, _ = g.run(st); T = len(S) - 1; h, ch, U = labels(g, S); tot["runs"] += 1; tot["steps"] += T
        mv = [None] + [sum(1 for x in range(g.N) if S[t][x] != S[t - 1][x]) for t in range(1, T + 1)]
        M2 = sum(1 for t in range(1, T) if mv[t] >= 2); tot["M2"] += M2; tot["unch"] += U
        tot["VIOL"] += sum(1 for t in range(2, T + 1) if not ch[t] and mv[t - 1] < 2)
        tot["BOUND"] += T > g.N * (1 + M2)
        if T >= 1 and all(mv[t] == 1 for t in range(1, T + 1)):
            tot["single_runs"] += 1; tot["single_maxT_over_N"] = max(tot["single_maxT_over_N"], T / g.N)
print("MCHARGE", " ".join(f"{k} {v}" for k, v in tot.items()))
