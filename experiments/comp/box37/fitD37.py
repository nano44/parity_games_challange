#!/usr/bin/env python3
"""L-COMP box 37 (3): fit of the mover class height D_mov (L-NEW box 204; IDEAL-CYC; ideal37 value = the definition) against N + M.
Set: every BEST line of out/climb37_*.log (each frozen climb best; D_mov from its ideal37 re-run), envelope = max D_mov per distinct N + M.
Also the gen37(n) family (D_mov = 4n + 3 measured in out/xhgt37.out for n 2-8; formula on 22 sizes is NOT re-measured here).
Prints: number of points and distinct sizes, envelope table, log-log p +- SE on the envelope, linear fit D = a (N + M) + b with max
residual, max ratio D/(N + M) with its genome. Usage: fitD37.py"""
import glob, json, math, re, os
H = os.path.dirname(os.path.abspath(__file__)); pts = []
for f in sorted(glob.glob(os.path.join(H, "out", "climb37_*.log"))):
    for line in open(f):
        if not line.startswith("BEST "): continue
        name = line.split()[1]; fm = json.loads(line[line.index("{"):line.index("} ideal37") + 1]); hi = json.loads(line[line.index("ideal37 ") + 8:line.index(" agree")])
        pts.append((fm["NM"], hi["Dmov"], fm["Dmov"], name))
print("points", len(pts), "fast37 != ideal37:", sum(a != b for _, a, b, _ in pts))
env = {}
for nm, d, _, name in pts:
    if nm not in env or d > env[nm][0]: env[nm] = (d, name)
xs = sorted(env); print("distinct sizes", len(xs), "range", xs[0], "-", xs[-1])
def ls(X, Y):
    k = len(X); mx, my = sum(X) / k, sum(Y) / k; sxx = sum((x - mx) ** 2 for x in X)
    p = sum((x - mx) * (y - my) for x, y in zip(X, Y)) / sxx; c = my - p * mx; res = [y - (c + p * x) for x, y in zip(X, Y)]
    return p, c, math.sqrt(sum(r * r for r in res) / max(k - 2, 1) / sxx), max(abs(r) for r in res)
Y = [env[x][0] for x in xs]
p, c, se, _ = ls([math.log(x) for x in xs], [math.log(y) for y in Y]); print(f"envelope log-log: p = {p:.3f} +- {se:.3f}")
a, b, sea, mr = ls(xs, Y); print(f"envelope linear: D_mov = {a:.4f}*(N+M) + {b:.2f} (slope SE {sea:.4f}), max residual {mr:.2f}")
# bins of size for a readable table: max per 50-wide bin
bins = {}
for x in xs:
    k = x // 50 * 50
    if k not in bins or env[x][0] > bins[k][1]: bins[k] = (x, env[x][0], env[x][1])
print("max D_mov per 50-wide size bin (N+M, D_mov, ratio, genome):")
for k in sorted(bins): x, d, nm = bins[k]; print(f"  [{k},{k+50}) {x} {d} {d / x:.4f} {nm}")
r = max(pts, key=lambda t: t[1] / t[0]); print("max ratio", round(r[1] / r[0], 4), r)
print("gen37(n) for comparison: D_mov = 4n + 3, N + M = 29n + 29 -> ratio -> 4/29 = 0.1379")
