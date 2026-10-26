#!/usr/bin/env python3
"""Box 13 (1): growth-law fits from the scaling climbs (results/scale/*.log, END lines).
Per family (nep_fresh, nep_seed, lend_fresh, lend_seed) and n: the best value of each repeat; tables of max, max/n, max/n^2;
least-squares exponent b of log(value) = a + b log(n): (i) over the per-n maxima, (ii) per repeat index r (spread = min..max over r),
(iii) over all points. Budget doubling (dbl_*): best value per budget.
Usage: fit.py [DIR]"""
import glob
import math
import os
import re
import sys
from collections import defaultdict

D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "scale")


def best(path):
    for line in open(path):
        m = re.match(r"END steps (\d+) best \((-?\d+), (-?\d+)\) n (\d+)", line)
        if m:
            return int(m.group(2)), int(m.group(1))
    return None, None


def lsq(pts):
    pts = [(math.log(n), math.log(v)) for n, v in pts if v and v > 0]
    if len(pts) < 2:
        return float("nan")
    mx = sum(x for x, _ in pts) / len(pts); my = sum(y for _, y in pts) / len(pts)
    sxx = sum((x - mx) ** 2 for x, _ in pts)
    return sum((x - mx) * (y - my) for x, y in pts) / sxx if sxx else float("nan")


fam = defaultdict(lambda: defaultdict(dict)); dbl = defaultdict(dict); steps = {}
for p in glob.glob(os.path.join(D, "*.log")):
    b = os.path.basename(p)[:-4]
    v, st = best(p)
    m = re.match(r"(nep|lend)_(fresh|seed)_n(\d+)_r(\d+)$", b)
    if m:
        fam[f"{m.group(1)}_{m.group(2)}"][int(m.group(3))][int(m.group(4))] = v; steps[b] = st; continue
    m = re.match(r"dbl_(nep|lend)_n(\d+)_b(\d+)$", b)
    if m:
        dbl[f"{m.group(1)} n {m.group(2)}"][int(m.group(3))] = (v, st)
for f in sorted(fam):
    print(f"== {f}  (value = {'max N_ep in one phase' if f.startswith('nep') else 'max len(E) over |D_E| >= 2 epochs'}; budget 15 s x n)")
    print("| n | repeats (best each) | max | max/n | max/n^2 | steps (r1/r2/r3) |")
    print("| --- | --- | --- | --- | --- | --- |")
    mx = []
    for n in sorted(fam[f]):
        rs = fam[f][n]; vals = [rs[r] for r in sorted(rs) if rs[r] is not None]
        if not vals:
            continue
        M = max(vals); mx.append((n, M))
        stp = "/".join(str(steps.get(f"{f}_n{n}_r{r}")) for r in sorted(rs))
        print(f"| {n} | {', '.join(str(rs[r]) for r in sorted(rs))} | {M} | {M / n:.3f} | {M / n / n:.4f} | {stp} |")
    per_r = []
    for r in (1, 2, 3):
        pts = [(n, fam[f][n].get(r)) for n in fam[f] if fam[f][n].get(r)]
        per_r.append(lsq(pts))
    allp = [(n, v) for n in fam[f] for v in fam[f][n].values() if v]
    good = [x for x in per_r if x == x]
    print(f"exponent b (log max = a + b log n): over per-n maxima {lsq(mx):.2f}; per repeat {', '.join(f'{x:.2f}' for x in per_r)}"
          f" (spread {min(good):.2f}..{max(good):.2f}); all points {lsq(allp):.2f}" if good else "exponent: n/a")
    print()
for k in sorted(dbl):
    print(f"== budget doubling, {k}: " + ", ".join(f"{b} s -> {dbl[k][b][0]} ({dbl[k][b][1]} steps)" for b in sorted(dbl[k])))
