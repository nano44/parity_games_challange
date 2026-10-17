#!/usr/bin/env python3
"""Summary of the gauntlet-step-2 run (compare.py CSV): status counts, agreement, and log-log slopes of wall-clock and
iterations against n for the named solver.  Usage: g10k_summary.py out/g10k_s7.csv s7"""
import sys, csv, math, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
rows = list(csv.DictReader(open(sys.argv[1]))); solver = sys.argv[2]
mine = [r for r in rows if r.get("solver") == solver]
st = collections.Counter(r["status"] for r in mine)
print("rows for", solver, len(mine), dict(st))
# n per game from the file name (gen.py corpus names record n) or manifest
import re
def n_of(r):
    try: return int(r["n"])
    except (KeyError, ValueError): m = re.search(r"_n(\d+)_", r.get("game", "")); return int(m.group(1)) if m else None
def it_of(r):
    try: return float(r["iterations"])
    except (KeyError, ValueError, TypeError): return None
pts = [(n_of(r), float(r["wall_s"]), it_of(r)) for r in mine if r["status"] == "ok" and n_of(r)]
pts = [p for p in pts if p[0] and p[0] > 1 and p[1] > 0]
def slope(xs, ys):
    xs = [math.log(x) for x in xs]; ys = [math.log(y) for y in ys]; mx = sum(xs) / len(xs); my = sum(ys) / len(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
big = [p for p in pts if p[0] >= 50]
print("ok games with n:", len(pts), "; wall-clock slope vs n (all):", round(slope([p[0] for p in pts], [p[1] for p in pts]), 2), "; (n >= 50):", round(slope([p[0] for p in big], [p[1] for p in big]), 2) if len(big) > 5 else "-")
it = [p for p in pts if p[2] is not None and p[2] > 0]
if it: print("iterations slope vs n:", round(slope([p[0] for p in it], [p[2] for p in it]), 2), "; max iterations", max(p[2] for p in it), "at n =", max(it, key=lambda p: p[2])[0])
bins = collections.defaultdict(list)
for n, t, k in pts: bins[(n - 1) // 25].append((t, k))
print("| n range | games | mean secs | max secs | mean iters | max iters |"); print("|---|---|---|---|---|---|")
for b in sorted(bins):
    v = bins[b]; ks = [k for _, k in v if k is not None]
    print(f"| {25*b+1}-{25*b+25} | {len(v)} | {sum(t for t,_ in v)/len(v):.3f} | {max(t for t,_ in v):.2f} | {sum(ks)/len(ks) if ks else 0:.1f} | {max(ks) if ks else 0:.0f} |")
