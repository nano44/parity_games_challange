#!/usr/bin/env python3
"""L-RED successor 26 (STEP 2 (A), T37 §3 (H1) route): Friedmann's H_n (L-COMP's experiments/friedmann-hn/hn.py, mode fig, read only)
with the sink x lifted from priority 1 to a HIGH odd priority X, so that every gate vertex (d1_i, d2_i, d3_i, e_i, y_i, g_i <= 8n+2)
ranks below the cycle node of the exit plays (x) and GATE-SHUT's (H1) fails at every gate. Variants (argument WHERE):
  gate : X = 8n+3, every priority >= 8n+3 shifted by +2 (x just above the gates, below the lane, c, s, r, k, f, h)
  lane : X just above the lane a/t and c (below s, r, k, f, h)
  top  : X above everything (all path sets empty; lengths only)
Writes GAME.pg and GAME.start (SIGMA0 = iota_{H_n}, TAU0 = the S3 tau of the new game).
Usage: hnh1.py N WHERE OUT.pg OUT.start"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "friedmann-hn")); sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second"))
import hn, n5b
n, where = int(sys.argv[1]), sys.argv[2]
g, ix = hn.build(n, "fig")
pr = list(g.prio); x = ix["x"]
where = where.rstrip("E")
if where == "gate":
    cut = 8 * n + 3
elif where == "lane":
    cut = 20 * n + 1               # c = 20n (odd vertex c has even priority 20n); s = 20n+2: x goes to 20n+1 after shifting
else:
    cut = max(pr) + 1
pr = [p + 2 if p >= cut else p for p in pr]
pr[x] = cut if cut % 2 == 1 else cut + 1
if "E" in sys.argv[2:3][0][-1:]: pr[x] += 1      # WHERE ending in E: the sink gets the EVEN priority just above (Even-won sink)
assert len(set(pr)) == len(pr)
lab = g.labels or [str(v) for v in range(g.n)]
with open(sys.argv[3], "w") as f:
    f.write(f"parity {g.n - 1};\n")
    for v in range(g.n):
        f.write(f"{v} {pr[v]} {g.owner[v]} {','.join(str(w) for w in g.succ[v])} \"{lab[v]}\";\n")
g2 = n5b.pg.read(sys.argv[3]); N = n5b.N5(g2)
t0 = N.SD.initial_strategy_by_best_reward(); s = hn.iota(n, ix)
with open(sys.argv[4], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(s.items())) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{t0[v]}" for v in range(g2.n) if g2.owner[v] == 1) + "\n")
print(f"n {g.n} x priority {pr[x]} (max {max(pr)})")
