#!/usr/bin/env python3
"""L-COMP box 42 item 3: fits within the ONE family CL(k) (clone42.py) of Deep_3 (= Σ_C Deep_3(C), deep41 DeepInt; unit flip; total per
run) and the per-gate maximum (gmaxInt) against N + M = 285 + 7k. Input out/meas42_mine.out."""
import json, math
P = [(int(l.split()[2]), json.loads(l[l.index("{"):])) for l in open("out/meas42_mine.out")]
X = [p[0] for p in P]; Y = [p[1]["DeepInt"] for p in P]; n = len(P); mx = sum(X) / n; my = sum(Y) / n
a = sum((x - mx) * (y - my) for x, y in zip(X, Y)) / sum((x - mx) ** 2 for x in X); b = my - a * mx
res = max(abs(y - (a * x + b)) for x, y in zip(X, Y))
print("points (N+M, Deep_3):", list(zip(X, Y)))
print(f"linear fit Deep_3 = {a:.6f} (N+M) + {b:.3f}; max residual {res:.2e}  (exact rule: Deep_3 = 10 + 4k, N+M = 285 + 7k)")
Lx = [math.log(x) for x in X[1:]]; Ly = [math.log(y) for y in Y[1:]]; m = len(Lx); lx = sum(Lx) / m; ly = sum(Ly) / m
p = sum((u - lx) * (v - ly) for u, v in zip(Lx, Ly)) / sum((u - lx) ** 2 for u in Lx)
print(f"log-log slope (k >= 8; affine offset biases it above 1): {p:.3f}")
print("per-gate max deep internal flips:", sorted({q[1]['gmaxInt'] for q in P}), " dmaxInt:", sorted({q[1]['dmaxInt'] for q in P}), " T3:", sorted({q[1]['T3'] for q in P}))
