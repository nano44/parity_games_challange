"""Compare kl2.py results with L-NEW's experiments/new/kl/results/*.csv.
  analyze.py rand    : rand10k: R1 per instance (exact), R2 seed 1 per instance (exact if draws agree), R2 seeds 1-3 spread
  analyze.py family F..: per family and size: R1 exact; R2 seed-1 exact; R2 seeds 1-10 mean / sd / min / max (primal, dual)
                         + L-NEW's r2 (seed 1) and r2seeds rows; local growth exponents of the R2 mean total pivots vs n."""
import csv
import math
import os
import statistics as stt
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LN = os.path.join(ROOT, "experiments", "new", "kl", "results")


SEEDF = ["family", "N", "n", "seed", "pivots", "pivots_dual", "verify", "oink"]


def rows(p, fields=None):
    with open(p) as f:
        first = f.readline(); f.seek(0)
        if fields and not first.startswith("family"):
            return list(csv.DictReader(f, fieldnames=fields))
        return list(csv.DictReader(f))


def rand():
    mine = rows(os.path.join(HERE, "out", "rand10k.kl2.csv"))
    th = {}
    for rule in ("r1", "r2"):
        for r in rows(os.path.join(LN, f"rand10k.{rule}.csv")):
            th[(r["file"], rule)] = (int(r["iterations"]), int(r["iterations_dual"]))
    bad = [r for r in mine if r["status"] != "OK"]
    eq = {"r1": [0, 0], "r2s1": [0, 0]}
    diffs = []
    per = {}
    for r in mine:
        if r["status"] != "OK":
            continue
        pp, pd = int(r["pivots_primal"]), int(r["pivots_dual"])
        per.setdefault(r["file"], {})[(r["rule"], r["seed"])] = (pp, pd)
        key = "r1" if r["rule"] == "r1" else ("r2s1" if r["seed"] == "1" else None)
        if key:
            t = th[(r["file"], r["rule"])]
            eq[key][1] += 1
            if (pp, pd) == t:
                eq[key][0] += 1
            else:
                diffs.append((key, r["file"], (pp, pd), t))
    print(f"rows {len(mine)}, non-OK {len(bad)}")
    for b in bad[:10]:
        print("  NON-OK", b)
    for k, (a, b) in eq.items():
        print(f"{k}: {a}/{b} instances equal to L-NEW (primal and dual)")
    for d in diffs[:20]:
        print("  DIFF", d)
    s = [sum(v[("r2", str(x))]) for v in per.values() for x in (1, 2, 3) if ("r2", str(x)) in v]
    s1 = [sum(v[("r1", "")]) for v in per.values() if ("r1", "") in v]
    print(f"total pivots (primal+dual): R1 mean {stt.mean(s1):.2f} max {max(s1)}; R2 seeds 1-3 mean {stt.mean(s):.2f} max {max(s)}")
    nb = {}
    for f, v in per.items():
        n = int(f.split("_n")[1].split("_")[0])
        for x in (1, 2, 3):
            if ("r2", str(x)) in v:
                nb.setdefault(min(n // 20, 5), []).append(sum(v[("r2", str(x))]))
    for b in sorted(nb):
        print(f"  n in [{20 * b},{20 * b + 19}]: R2 mean {stt.mean(nb[b]):.2f} max {max(nb[b])} ({len(nb[b])} runs)")


def family(f):
    p = os.path.join(HERE, "results", f"{f}.kl2.csv")
    mine = rows(p)
    t1 = {r["N"]: r for r in rows(os.path.join(LN, f"{f}.r1.csv"))} if os.path.exists(os.path.join(LN, f"{f}.r1.csv")) else {}
    t2 = {r["N"]: r for r in rows(os.path.join(LN, f"{f}.r2.csv"))} if os.path.exists(os.path.join(LN, f"{f}.r2.csv")) else {}
    ts = {}
    for name in ("growing.r2seeds.csv", "sbe.r2seeds.csv"):
        for r in rows(os.path.join(LN, name), SEEDF):
            if r["family"] == f:
                ts.setdefault(r["N"], set()).add((int(r["seed"]), int(r["pivots"]), int(r["pivots_dual"])))
    by = {}
    for r in mine:
        by.setdefault(r["N"], []).append(r)
    print(f"## {f}")
    print("| N | n | ref | status | R1 mine | R1 L-NEW | R2s1 mine | R2s1 L-NEW | R2 s1-10 primal mean (sd) [min,max] | dual mean (sd) [min,max] | L-NEW r2seeds |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    pts = []
    for N in sorted(by, key=int):
        rs = by[N]
        st = sorted({r["status"] for r in rs})
        r1 = [r for r in rs if r["rule"] == "r1"]
        r2 = [r for r in rs if r["rule"] == "r2" and r["status"] == "OK"]
        m1 = f"{r1[0]['pivots_primal']}/{r1[0]['pivots_dual']}" if r1 and r1[0]["status"] == "OK" else (r1[0]["status"] if r1 else "-")
        l1 = f"{t1[N]['iterations']}/{t1[N]['iterations_dual']}" if N in t1 else "-"
        s1 = [r for r in r2 if r["seed"] == "1"]
        m2 = f"{s1[0]['pivots_primal']}/{s1[0]['pivots_dual']}" if s1 else "-"
        l2 = f"{t2[N]['iterations']}/{t2[N]['iterations_dual']}" if N in t2 else "-"
        if r1 and N in t1 and m1 != l1:
            m1 = "**" + m1 + "**"
        if s1 and N in t2 and m2 != l2:
            m2 = "**" + m2 + "**"

        def desc(xs):
            if not xs:
                return "-"
            sd = stt.pstdev(xs) if len(xs) > 1 else 0.0
            return f"{stt.mean(xs):.1f} ({sd:.1f}) [{min(xs)},{max(xs)}]"
        pp = [int(r["pivots_primal"]) for r in r2]
        pd = [int(r["pivots_dual"]) for r in r2]
        ls = "; ".join(f"s{s}:{a}/{b}" for s, a, b in sorted(ts.get(N, ())))
        n = int(rs[0]["n"])
        print(f"| {N} | {n} | {rs[0]['ref']} | {','.join(st)} | {m1} | {l1} | {m2} | {l2} | {desc(pp)} | {desc(pd)} | {ls or '-'} |")
        if pp:
            pts.append((n, stt.mean([a + b for a, b in zip(pp, pd)])))
    if len(pts) >= 2:
        ex = []
        for (n0, y0), (n1, y1) in zip(pts, pts[1:]):
            if y0 > 0 and y1 > 0 and n1 > n0:
                ex.append(f"{math.log(y1 / y0) / math.log(n1 / n0):.2f}")
        print(f"\nlocal exponents d log(mean R2 total pivots) / d log n between consecutive sizes: {', '.join(ex) or '-'}\n")


if __name__ == "__main__":
    if sys.argv[1] == "rand":
        rand()
    else:
        for f in sys.argv[2:]:
            family(f)
