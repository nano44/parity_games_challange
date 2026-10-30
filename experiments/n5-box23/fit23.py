#!/usr/bin/env python3
"""Box 23 (c): table and fits of climb results. Reads climbs/*.log END lines (fit = (max R*_F, sum R*_F, |F| of that run)); per n
keeps the best R*_F over seeds/families given by --glob; fits R* = c n^b (least squares on logs) and R* = a n + d.
Usage: fit23.py [--glob 'climbs/rs_fresh_*.log']"""
import argparse, glob, math, re
ap = argparse.ArgumentParser(); ap.add_argument("--glob", default="climbs/rs_*.log"); a = ap.parse_args()
best = {}
for f in sorted(glob.glob(a.glob)):
    m = None
    for line in open(f):
        m = re.match(r"END steps (\d+) best \((-?\d+), (\d+), (\d+)\) n (\d+) secs (\d+)", line) or m
    if not m or not m.group(1).isdigit():
        continue
    steps, rs, _, F, n, secs = (int(m.group(i)) for i in (1, 2, 3, 4, 5, 6))
    print(f"{f}: n {n} R* {rs} |F| {F} R*/n {rs / n:.2f} steps {steps} secs {secs}")
    if n not in best or rs > best[n][0]:
        best[n] = (rs, F, f)
ns = sorted(best); print("BEST per n:", {n: best[n][:2] for n in ns})
pts = [(n, best[n][0]) for n in ns if best[n][0] > 0]
if len(pts) >= 2:
    X = [math.log(n) for n, _ in pts]; Y = [math.log(r) for _, r in pts]; k = len(pts); mx, my = sum(X) / k, sum(Y) / k
    b = sum((x - mx) * (y - my) for x, y in zip(X, Y)) / sum((x - mx) ** 2 for x in X); c = math.exp(my - b * mx)
    X2 = [n for n, _ in pts]; Y2 = [r for _, r in pts]; mx2, my2 = sum(X2) / k, sum(Y2) / k
    a2 = sum((x - mx2) * (y - my2) for x, y in zip(X2, Y2)) / sum((x - mx2) ** 2 for x in X2)
    print(f"FIT power R* = {c:.3f} n^{b:.3f};  linear R* = {a2:.3f} n + {my2 - a2 * mx2:.2f}  (points {k})")
