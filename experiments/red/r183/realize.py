#!/usr/bin/env python3
"""L-RED R183 REALIZE: R178 IDEAL genome (json, fastcyc format) -> real parity game G (gate -> {W-target, beta}; beta -> X-target),
written with the genome's sigma start and tau = W-faces as START. Prints the IDEAL run (abs177.simulate, faces fixed by fiat) and the
real N5 run's FL runs (fvch.analyse). Usage: realize.py genome.json out_prefix"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r177"), os.path.join(H, "..", "r178")]
import abs177 as A, pg, fvch, chain
def conv(G):   # copy of r178/fastver2.conv (that file runs a script at import)
    N = G["N"]; deg = G["deg"]
    return dict(levels=[l + 1 for l in G["lev"]], opts=[[["W" if o[0] < 0 else o[0], "X" if o[1] < 0 else o[1]] for o in G["opts"][v]] for v in range(N)],
                perm=list(range(N)) + [N + G["gate"][v][k] for v in range(N) for k in range(deg)], brank=G["br"], bpar=G["bp"],
                start=G["start"], bper=True)
G = json.load(open(sys.argv[1])); gen = conv(G); out = sys.argv[2]
n, prio, owner, sW, sX, idx = A.build(gen)
succ = [sorted(set(sW[v]) | set(sX[v])) for v in range(n)]
g = pg.Game(prio, owner, succ); chain.write(g, out + ".pg")
N = len(gen["levels"]); sig = {}
for i in range(N): sig[idx[("x", i)]] = idx[("g", i, gen["start"][i])]
for v in range(n):
    if owner[v] == 0 and v not in sig: sig[v] = succ[v][0]
with open(out + ".start", "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{sig[v]}" for v in sorted(sig)) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{sW[v][0]}" for v in range(n) if owner[v] == 1) + "\n")
s, fl, why, _ = A.simulate(gen)
from n5x import readstart
R = fvch.analyse(g, readstart(out + ".start"))
print("IDEAL steps", s, "FL", fl, why, "| REAL n", n, "K", R["K"], "FL runs", [(r["a"], r["b"], r["L"], r["FVCH"], r["SBCH"]) for r in R["runs"]])
