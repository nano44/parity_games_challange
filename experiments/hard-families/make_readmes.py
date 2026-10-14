#!/usr/bin/env python3
"""Write <family>/README.md from results/<family>.{csv,md,png} and families.py, with a growth summary per solver:
over the last (up to) 4 finished sizes, the fitted base b in work ~ b^N and exponent k in work ~ n^k (n = vertices).
A verdict string per family is passed in VERDICTS (written by hand after reading the numbers)."""
import csv, math, os, sys, shutil, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from families import F
from verdicts import VERDICTS


def slope(xs, ys):
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx if sxx else float("nan")


def growth(rows):
    by = collections.defaultdict(list)
    for r in rows:
        if r["status"] == "ok" and r["iterations"] not in ("", None) and int(r["iterations"]) > 0:
            by[r["solver"]].append((int(r["N"]), int(r["n"]), int(r["iterations"]), r["unit"]))
    out = {}
    for s, pts in by.items():
        pts = sorted(pts)[-4:]
        if len(pts) < 3:
            continue
        b = math.exp(slope([p[0] for p in pts], [math.log(p[2]) for p in pts]))
        k = slope([math.log(p[1]) for p in pts], [math.log(p[2]) for p in pts])
        out[s] = (b, k, pts[0][0], pts[-1][0], pts[-1][2], pts[-1][3])
    return out


for fam, meta in F.items():
    res = os.path.join(HERE, "results", fam)
    if not os.path.exists(res + ".csv"):
        print("no results for", fam); continue
    rows = list(csv.DictReader(open(res + ".csv")))
    d = os.path.join(HERE, fam); os.makedirs(d, exist_ok=True)
    for ext in ("csv", "md", "png"):
        if os.path.exists(f"{res}.{ext}"):
            shutil.copy(f"{res}.{ext}", os.path.join(d, f"sweep.{ext}"))
    g = growth(rows)
    status = collections.Counter(r["status"] for r in rows)
    with open(os.path.join(d, "README.md"), "w") as f:
        f.write(f"# {fam}\n\n")
        f.write(f"**Verdict:** {VERDICTS.get(fam, '(pending)')}\n\n")
        f.write(f"- Generator source: {meta['src']}\n- Command: `{meta['gen']}` (N = family parameter)\n")
        f.write(f"- What the source says: {meta['claim']}\n- Paper: {meta['paper']}\n")
        f.write(f"- Targeted solvers: {', '.join(meta['targets'])}; contrast: {', '.join(meta['contrast'])}\n")
        f.write(f"- Agreement: every solver that finished on an instance gave the same winner on every vertex "
                f"(py-zlk, the independent Python Zielonka, included while it finished). Run statuses: "
                f"{', '.join(f'{k} {v}' for k, v in sorted(status.items()))}.\n")
        f.write("- Re-run: `experiments/hard-families/run_all.sh " + fam + "` (Oink built by scripts/setup_oink.sh).\n\n")
        f.write("## Growth over the last finished sizes\nb: fitted base of work ~ b^N; k: fitted exponent of work ~ n^k "
                "(n = vertices). An exponential family shows k rising with N and b > 1 stable; a polynomial one shows b -> 1.\n\n")
        f.write("| solver | sizes N | b (per +1 in N) | k (in n) | work at largest N |\n|---|---|---|---|---|\n")
        for s, (b, k, n0, n1, w, u) in sorted(g.items(), key=lambda x: -x[1][0]):
            f.write(f"| {s} | {n0}..{n1} | {b:.3f} | {k:.2f} | {w} {u} |\n")
        f.write("\n## Sweep table\n\n" + open(res + ".md").read().split("\n", 2)[2] + "\n")
        f.write("![sweep](sweep.png)\n")
        import glob as _g
        for extra in sorted(_g.glob(os.path.join(HERE, "results", fam + "-pgs*.md"))):
            tag = os.path.basename(extra)[:-3]
            shutil.copy(extra[:-3] + ".png", os.path.join(d, tag + ".png"))
            shutil.copy(extra[:-3] + ".csv", os.path.join(d, tag + ".csv"))
            f.write(f"\n## Targeted algorithm (ported): {tag}\n\n" + open(extra).read() + f"\n![{tag}]({tag}.png)\n")
    print("wrote", fam)
