#!/usr/bin/env python3
"""L-NEW box 147 POLYW: the linear UNST potentials PHI_p(s) = sum_{x unstable} (pi(x)+1)^p (poly levels n^(p+1)) and the exact
DECREMENT energy sum 2^pi(x); per run (DOWN test: strict fall at unchained, no rise at chained steps) and on the all-start graph for
n <= 12 (allstart.py labels). Prints violation counts per p. Usage: polyw.py genome.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "weights.py"); ns = {"__file__": P}; exec(open(P).read().split('\nif __name__')[0], ns)
Q = os.path.join(HERE, "stat.py"); nq = {"__file__": Q}; exec(open(Q).read().split('\nif __name__')[0], nq)
PS = [1, 2, 3, 4, 6, 8]
tot = {p: [0, 0] for p in PS + ["2^pi"]}
for g in sys.argv[1:]:
    G = json.load(open(g)); n = G["N"]; R = nq["analyse"](G); pos = R["pos"]
    W = {p: [(pos[x] + 1) ** p for x in range(n)] for p in PS}; W["2^pi"] = [2 ** pos[x] for x in range(n)]
    run = {}
    for p, w in W.items():
        bad = 0
        for t, ch in R["lab"].items():
            dphi = sum(w[x] * (R["FS"][t]["UNST"][x] - R["FS"][t - 1]["UNST"][x]) for x in range(n))
            bad += (not ch and not dphi < 0) or (ch and dphi > 0)
        run[p] = bad; tot[p][0] += bad
    alls = {}
    if n <= 12:
        pos2, FS, lab = ns["graph"](G)
        for p, w in W.items(): alls[p] = ns["check"](w, FS, lab); tot[p][1] += alls[p]
    print(os.path.basename(g), "n", n, "RUN", " ".join(f"p{p}:{run[p]}" for p in W), "| ALLSTART", " ".join(f"p{p}:{alls[p]}" for p in alls), flush=True)
print("TOTAL (run, allstart):", " ".join(f"p{p}:{v[0]},{v[1]}" for p, v in tot.items()))
