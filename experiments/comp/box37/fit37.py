#!/usr/bin/env python3
"""L-COMP box 37: fits on gen37(n) (meas37 output files). For each counter y in (Qf = flips at gate (Q, 0), per-gate; C; T3) against
x = N + M: (a) exact integer-linear check y = a*n + b over all rows (a, b from the two smallest n; reports the max residual);
(b) log-log least squares y ~ c * x^p on ALL rows and on the upper half (n >= median), p with its standard error.
Usage: fit37.py file1 [file2 ...] (rows must agree across files where n coincides; disagreements are printed)."""
import sys, math, re
rows = {}
for f in sys.argv[1:]:
    for line in open(f):
        z = line.split()
        if len(z) < 10 or z[1] != "n": continue
        d = dict(zip(z[1::2], z[2::2])); n = int(d["n"]); v = {k: int(d[k]) for k in ("N+M", "T3", "C", "Qf", "maxflip")}
        if n in rows and rows[n] != v: print("DISAGREE", f, n, rows[n], v)
        rows.setdefault(n, v)
ns = sorted(rows); print("distinct sizes:", len(ns), "n =", ns)
def ls(xs, ys):
    X = [math.log(x) for x in xs]; Y = [math.log(y) for y in ys]; k = len(X); mx, my = sum(X) / k, sum(Y) / k
    sxx = sum((x - mx) ** 2 for x in X); p = sum((x - mx) * (y - my) for x, y in zip(X, Y)) / sxx; c = my - p * mx
    res = [y - (c + p * x) for x, y in zip(X, Y)]; se = math.sqrt(sum(r * r for r in res) / max(k - 2, 1) / sxx); return p, se
for key in ("Qf", "maxflip", "C", "T3", "N+M"):
    y = [rows[n][key] for n in ns]; a = y[1] - y[0]; a = (y[1] - y[0]) / (ns[1] - ns[0]); b = y[0] - a * ns[0]
    mr = max(abs(yy - (a * n + b)) for n, yy in zip(ns, y)); print(f"{key:8s} = {a:g}*n + {b:g}  max residual {mr:g}")
x = [rows[n]["N+M"] for n in ns]
for key in ("Qf", "maxflip", "C", "T3"):
    y = [rows[n][key] for n in ns]; p, se = ls(x, y); h = len(ns) // 2; p2, se2 = ls(x[h:], y[h:])
    print(f"{key:8s} vs N+M: p = {p:.3f} +- {se:.3f} (all {len(ns)}), p = {p2:.3f} +- {se2:.3f} (upper {len(ns) - h}); ratio at max n {y[-1] / x[-1]:.4f}")
