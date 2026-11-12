#!/usr/bin/env python3
"""L-COMP box 43 items 2-3: fits within each family (out/meas43_mine.out, out/meas43_cross.out, out/meas43_tail_mine.out,
out/meas43_tail_cross.out). Per family: Deep_3 (mine: DeepInt) against k and against N + M: least-squares line, maximum residual,
log-log slope; per-gate maximum (gmaxInt), dmaxInt and T3 by size; agreement of the two engines on T3, whole-run deep and dmax.
Usage: fit43.py"""
import os, re, json, ast, math
H = os.path.dirname(os.path.abspath(__file__))
def mine(fn):
    d = {}
    for l in open(os.path.join(H, "out", fn)):
        if "{" not in l: continue
        w = l.split(); r = json.loads(l[l.index("{"):]); r["NM"] = int(w[2]); d[w[0]] = r
    return d
def cross(fn):
    d = {}
    p = os.path.join(H, "out", fn)
    if not os.path.exists(p): return d
    for l in open(p):
        if "{" not in l: continue
        w = l.split(); r = ast.literal_eval(l[l.index("{"):]); r["T3"] = int(w[2]); d[w[0]] = r
    return d
def line(xs, ys):
    n = len(xs); mx, my = sum(xs) / n, sum(ys) / n; b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs); a = my - b * mx
    return a, b, max(abs(a + b * x - y) for x, y in zip(xs, ys))
def report(tag, rows, key, M, C):
    rows = sorted(rows, key=lambda r: r[0])
    ks = [r[0] for r in rows]; nm = [M[r[1]]["NM"] for r in rows]; y = [M[r[1]][key] for r in rows]
    a, b, res = line(ks, y); a2, b2, res2 = line(nm, y)
    ll = line([math.log(v) for v in nm[1:]], [math.log(v) for v in y[1:]])[1] if len(nm) > 2 and all(v > 0 for v in y[1:]) else float("nan")
    ag = [(M[r[1]]["T3"], M[r[1]]["deep"], M[r[1]]["dmax"]) == (C[r[1]]["T3"], C[r[1]]["deep"], C[r[1]]["dmax"]) for r in rows if r[1] in C]
    print("%s: sizes N+M %s | %s %s | = %.4g + %.6g k (max residual %.3g) = %.4g + %.6g (N+M) (max residual %.3g); log-log slope (k > 0 points) %.3f | per-gate max %s | dmaxInt %s | T3 %s | whole-run deep (mine) %s | two engines agree on (T3, whole-run deep, dmax): %d of %d"
          % (tag, nm, key, y, a, b, res, a2, b2, res2, ll, sorted(set(M[r[1]]["gmaxInt"] for r in rows)), sorted(set(M[r[1]]["dmaxInt"] for r in rows)), sorted(set(M[r[1]]["T3"] for r in rows)),
             [M[r[1]]["deep"] for r in rows], sum(ag), len(ag)))
M = mine("meas43_mine.out"); C = cross("meas43_cross.out")
for X in ("D18", "D10", "D80"):
    rows = [(0, "DHIB26_k0.json")] + [(int(re.search(r"_k(\d+)", f).group(1)), f) for f in M if f.startswith(X + "_k")]
    report(X + "(k)", rows, "DeepInt", M, C)
p = os.path.join(H, "out", "meas43_tail_mine.out")
if os.path.exists(p):
    M = mine("meas43_tail_mine.out"); C = cross("meas43_tail_cross.out")
    rows = [(int(re.search(r"TMWR(\d+)", f).group(1)), f) for f in M if f.startswith("TMWR")]
    if len(rows) >= 2: report("TMWR(n) = TAIL_2(MWR(n)), per-gate max", rows, "gmaxInt", M, C); report("TMWR(n), Deep_3", rows, "DeepInt", M, C)
    for f in sorted(M):
        r = M[f]; c = C.get(f)
        print("   %-14s N+M %4d T3 %3d Deep_3 %4d per-gate max %3d dmaxInt %2d whole-run deep %4d qflip %4d | cross100: %s" % (f, r["NM"], r["T3"], r["DeepInt"], r["gmaxInt"], r["dmaxInt"], r["deep"], r["qflip"],
              "T3 %d deep %d dmax %d qflip %d maxfl %d" % (c["T3"], c["deep"], c["dmax"], c["qflip"], c["maxfl"]) if c else "-"))
