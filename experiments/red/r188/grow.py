#!/usr/bin/env python3
"""L-RED R188 GROW: climb in IDEAL-ACYC (r187 ideal.traj = real run by REALIZE) from a seed genome, optionally adding a new TOP level of
W movers (options -> the old top-level movers, free Xi-targets kept acyclic). Score = run length T (accept >=). Writes OUT at every
improvement. Usage: grow.py seed.json addtop(0/1) iters seed OUT"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal, rel, downgen
G = json.load(open(sys.argv[1])); add, iters, seed, out = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed); N = G["N"]; deg = G["deg"]
if "pi" not in G:
    xo = G.get("xorder") or list(range(N)); G["pi"] = [0] * N
    for i, v in enumerate(xo): G["pi"][v] = i
G.pop("xorder", None)
if add:
    W = sum(1 for l in G["lev"] if l == max(G["lev"])); top = [v for v in range(N) if G["lev"][v] == max(G["lev"])]
    M = sum(len(o) for o in G["opts"]); nb = len(G["br"])
    for i in range(W):
        v = N + i; G["lev"].append(max(G["lev"]) + (1 if i == 0 else 0) if i == 0 else G["lev"][N]); G["pi"].append(-1 - i)
        G["opts"].append([[top[k % len(top)], -1, nb + deg * i + k] for k in range(deg)])
        G["gate"].append([M + deg * i + k for k in range(deg)]); G["start"].append(rng.randrange(deg))
    G["br"] += [nb + j for j in range(W * deg)]; G["bp"] += [rng.randint(0, 1) for _ in range(W * deg)]
    G["N"] = N = N + W
    mn = min(G["pi"]); G["pi"] = [p - mn for p in G["pi"]]   # new movers first in pi: they may read anyone
    G["lev"][N - W:] = [max(G["lev"][:N - W]) + 1] * W
def score(H):
    S, why = ideal.traj(H, cap=3000); return len(S) - 1
best = score(G); print("start", best, flush=True); json.dump(G, open(out, "w"))
for it in range(iters):
    H = downgen.mutacyc(G, rng); s = score(H)
    if s >= best:
        if s > best: print("it", it, s, flush=True); json.dump(H, open(out, "w"))
        G, best = H, s
S, _ = ideal.traj(G); print("BEST", best, rel.stats(G, S))
