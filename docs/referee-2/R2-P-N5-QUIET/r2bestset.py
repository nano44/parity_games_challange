#!/usr/bin/env python3
"""REFEREE-2 succ. 33: along every Howard run on Γ3(G) (own r2acyc builder, e-order lev; Howard as in r2t3div.py), evaluate the SAME
mover choices on Γ(G) and compare, per mover, the set of ⊴-best options and the set of options strictly better than the current one.
diffbest / diffbetter: (state, mover) pairs where the sets differ (0 means: this Γ3 run is also a Howard run on Γ, with another tie rule,
so T-QUIET's bound for Γ covers its length). Usage: r2bestset.py FILES.json|SET.jsonl ..."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-P-ACYC")); import r2acyc as A
from collections import Counter
A.EORDER = "lev"
def sets(g, vj, ms):
    V = g["V"]; sig = A.mover_sig(g, ms); _, val = A.odd_opt(g, vj, sig, A.worst_start(g)); out = []
    for x in range(g["N"]):
        s = g["succ"][V[("x", x)]]; c = vj.cmp
        best = {k for k in range(len(s)) if all(c(val[s[k]], val[s[j]]) >= 0 for j in range(len(s)))}
        better = {k for k in range(len(s)) if c(val[s[k]], val[s[ms[x]]]) > 0}
        out.append((best, better))
    return out
for f in sys.argv[1:]:
    C = Counter()
    for G in ([json.loads(l) for l in open(f)] if f.endswith(".jsonl") else [json.load(open(f))]):
        g3 = A.build(G, True); v3 = A.VJ(g3); g = A.build(G, False); v = A.VJ(g); ms = list(G["start"]); C["genomes"] += 1
        while True:
            s3 = sets(g3, v3, ms); s1 = sets(g, v, ms); C["states"] += 1
            for x in range(G["N"]):
                C["pairs"] += 1; C["diffbest"] += s3[x][0] != s1[x][0]; C["diffbetter"] += s3[x][1] != s1[x][1]
            new = list(ms); ch = False; succ = g3["succ"]
            for x in range(G["N"]):
                if s3[x][1]: new[x] = max(s3[x][0], key=lambda k: succ[g3["V"][("x", x)]][k]); ch = True
            if not ch: break
            ms = new
    print(os.path.basename(f), " ".join(f"{k} {C[k]}" for k in ("genomes", "states", "pairs", "diffbest", "diffbetter")), flush=True)
