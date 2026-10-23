#!/usr/bin/env python3
"""N8d §4 growth table: per hard family, R2 pivots (primal + dual) and seconds against n from the seed-1 bench CSVs
(results/<family>.r2.csv), plus multi-seed means where recorded (results/*r2seeds.csv); fitted log-log slope d(log pivots)/d(log n) over
the last two sizes and over the whole range. Prints markdown."""
import csv, math, os, glob
from collections import defaultdict
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
fams = ["tc", "tc+", "switchallexp", "switchbestexp", "counter_qpt", "counter_m", "counter_rr", "counter_dp", "counter_core", "counter_ortl",
        "counter_rob", "counter_symsi", "recursiveladder"]


def slope(pts):
    pts = [(n, p) for n, p in pts if p > 0]
    if len(pts) < 2: return "-", "-"
    (n0, p0), (n1, p1), (na, pa) = pts[-2], pts[-1], pts[0]
    loc = math.log(p1 / p0) / math.log(n1 / n0) if n1 != n0 else float("nan")
    tot = math.log(p1 / pa) / math.log(n1 / na) if n1 != na else float("nan")
    return f"{loc:.2f}", f"{tot:.2f}"


print("| family | seed-1 bench: n → pivots (primal+dual), seconds | slope last / whole (pivots) | slope last / whole (seconds) | multi-seed means (n: mean primal+dual) |")
print("| --- | --- | --- | --- | --- |")
seeds = defaultdict(lambda: defaultdict(list))
for f in glob.glob(os.path.join(R, "*r2seeds.csv")):
    for r in csv.DictReader(open(f)):
        try: seeds[r["family"]][int(r["n"])].append(int(r["pivots"]) + int(r["pivots_dual"]))
        except (ValueError, KeyError): pass
for fam in fams:
    p = os.path.join(R, f"{fam}.r2.csv")
    if not os.path.exists(p): continue
    rows = sorted(csv.DictReader(open(p)), key=lambda r: int(r["n"]))
    pts = [(int(r["n"]), int(r["iterations"]) + int(r["iterations_dual"])) for r in rows]
    sec = [(int(r["n"]), float(r["secs"]) or 0.05) for r in rows]
    cells = "; ".join(f"{n}: {pv} ({s:g} s)" for (n, pv), (_, s) in zip(pts, sec))
    ms = seeds.get(fam, {})
    mcell = "; ".join(f"{n}: {sum(v) / len(v):.0f} (k={len(v)})" for n, v in sorted(ms.items())) or "-"
    lp, wp = slope(pts); ls, ws = slope(sec)
    print(f"| {fam} | {cells} | {lp} / {wp} | {ls} / {ws} | {mcell} |")
