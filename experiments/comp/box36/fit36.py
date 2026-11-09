#!/usr/bin/env python3
"""L-COMP box 36: per-gate flip record at k = 1 against N + M. Points = for each climb (cap 200 / 300 / 400) the best frozen genome
(max flips/(lamch+1); all bests have lamch 0, so ratio = flips), plus the MWR(n) family (L-RED R229, n 4/8/16) for reference.
Fits (least squares, with standard errors): (i) y = a·x, (ii) y = a + b·x, (iii) log y = log c + p·log x. DATA; climb points are
LOWER bounds on max flips at that size (heuristic search); with 3 points, the fits do not identify a growth law. Usage: fit36.py"""
import os, re, math, json
H = os.path.dirname(os.path.abspath(__file__)); CL = os.path.join(H, "out", "climb")


def best_of(log):
    b = None
    for line in open(log):
        m = re.match(r"BEST (\S+) N\+M (\d+) k 1 score \[([\d.]+), (\d+), (\d+)\]", line)
        if m:
            p = (float(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(2)), m.group(1))
            if b is None or p[:3] > b[:3]: b = p
    return b


def ls(xs, ys):
    n = len(xs); mx, my = sum(xs) / n, sum(ys) / n; sxx = sum((x - mx) ** 2 for x in xs); sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx; a = my - b * mx; res = [y - a - b * x for x, y in zip(xs, ys)]; s2 = sum(r * r for r in res) / (n - 2) if n > 2 else float("nan")
    return a, b, math.sqrt(s2 / sxx) if n > 2 else float("nan"), res


def origin(xs, ys):
    a = sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs); res = [y - a * x for x, y in zip(xs, ys)]; n = len(xs)
    se = math.sqrt(sum(r * r for r in res) / (n - 1) / sum(x * x for x in xs)) if n > 1 else float("nan")
    return a, se, res


pts = []
for tag, cap in (("A200", 200), ("C300", 300), ("B400", 400)):
    f = os.path.join(CL, f"climb{tag}.log")
    if os.path.exists(f):
        b = best_of(f); pts.append(dict(src=f"climb {tag} (cap {cap})", NM=b[3], flips=b[0], C=b[1], T3=b[2], file=b[4]))
mwr = [dict(src="MWR4_2", NM=145, flips=9.0, C=5, T3=30), dict(src="MWR8_2", NM=261, flips=17.0, C=9, T3=54), dict(src="MWR16_2", NM=493, flips=33.0, C=17, T3=102)]
for p in pts + mwr: print(json.dumps(p))
for name, P in (("climb bests", pts), ("MWR", mwr), ("climb + MWR (upper envelope check)", pts + mwr)):
    xs = [p["NM"] for p in P]; ys = [p["flips"] for p in P]
    a, se, r = origin(xs, ys); print(f"{name}: y = a·x: a = {a:.4f} ± {se:.4f}, residuals {[round(z, 2) for z in r]}")
    if len(P) >= 3:
        a2, b2, seb, r2 = ls(xs, ys); print(f"{name}: y = a + b·x: a = {a2:.2f}, b = {b2:.4f} ± {seb:.4f}, residuals {[round(z, 2) for z in r2]}")
        lc, p_, sep, r3 = ls([math.log(x) for x in xs], [math.log(y) for y in ys]); print(f"{name}: y = c·x^p: p = {p_:.3f} ± {sep:.3f}, c = {math.exp(lc):.4g}")
