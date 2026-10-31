#!/usr/bin/env python3
"""L-RED R158: re-run a fbsearch.py genome (JSON) with a longer E2 chain: extra BA2_i copy the last BA2's rank/parity (rank + tiny).
Prints |F| (longest W-run), iterations, n. Usage: fbscale.py K m GENOME.json m2 [OUTPREFIX]"""
import sys, os, json
K, m, GJ, m2 = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]); OUT = sys.argv[5] if len(sys.argv) > 5 else None
sys.argv = [sys.argv[0], str(K), str(m), str(m2), "0", "0"]
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import fbsearch as F
gen = json.load(open(GJ)); mk = {k: (tuple(v) if v else None) for k, v in gen["mk"].items()}
old = sorted(int(k.split("_")[1]) for k in mk if k.startswith("BA2_")); last = mk[f"BA2_{old[-1]}"]
for i in range(1, m2 + 1):
    if f"BA2_{i}" not in mk: mk[f"BA2_{i}"] = None if last is None else (last[0] + 1e-6 * i, last[1])
for k in list(mk):
    if k.startswith("BA2_") and int(k.split("_")[1]) > m2: del mk[k]
gen["mk"] = mk
g, s0, t0, order = F.build(gen)
tr, fb = F.xcn.trace(g, s0, t0, cap=50000); runs, W = F.xcn.wruns(g, tr, fb)
print(f"m2 {m2} n {g.n} iters {len(tr) - 1} fallbacks {sum(fb)} wruns {len(runs)} |F| {max(len(r) for r in runs) - 1}")
if OUT:
    with open(OUT + ".pg", "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f'{v} {g.prio[v]} {g.owner[v]} {",".join(map(str, g.succ[v]))} "{order[v]}";\n')
    with open(OUT + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(g.n) if g.owner[v] == 0) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{t0[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
