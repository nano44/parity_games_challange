#!/usr/bin/env python3
"""Box 214 Step A (L-NEW successor 75): does lev(xt) track the mirror level d - 1 - l? mean deviation against 200 shuffles of the target levels (seed 1), and corr(l, lev(xt)), on the five towers (box212/inst). Usage: python3 mirror214.py (any directory)."""
import os; os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box212", "inst"))
import json, sys, random, statistics
def load(f):
    G = json.load(open(f)); return G.get("genome", G)
rng = random.Random(1)
for f in ["DBL4_d20_F30.json", "RECF4_d20_F60.json", "H5_d20_F62.json", "H6_d24_F126.json", "HIT7_d28_F254.json"]:
    G = load(f); lev = G["lev"]; d = max(lev) + 1
    pairs = [(lev[x], lev[xt]) for x in range(G["N"]) for (wt, xt, b) in G["opts"][x] if xt >= 0]
    dev = statistics.mean(abs(lt - (d - 1 - l)) for l, lt in pairs)
    # baseline: same multiset of target levels, randomly permuted among sources
    tl = [lt for _, lt in pairs]; base = []
    for _ in range(200):
        rng.shuffle(tl); base.append(statistics.mean(abs(t - (d - 1 - l)) for (l, _), t in zip(pairs, tl)))
    corr = statistics.correlation([l for l, _ in pairs], [lt for _, lt in pairs])
    print(f, "d", d, "Xi-edges", len(pairs), "mean|lev(xt) - (d-1-l)|", round(dev, 2), "shuffled baseline", round(statistics.mean(base), 2), "+-", round(statistics.pstdev(base), 2), "corr(l, lev(xt))", round(corr, 3))
