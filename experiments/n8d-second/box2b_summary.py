"""Box 2b summary: mean dual (+primal) pivots per family, N and setting; fitted exponents; rand1k means. All rows must be OK."""
import csv
import glob
import math
import os
import statistics as st

R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results-2b")
SETS = ["first", "last", "rand", "relabel"]


def fit(xs, ys):
    mx, my = st.mean(xs), st.mean(ys)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return b, sum((y - my - b * (x - mx)) ** 2 for x, y in zip(xs, ys))


bad = 0
for fam in ("switchallexp", "switchbestexp"):
    tab = {}
    for s in SETS:
        p = os.path.join(R, f"{fam}.{s}.csv")
        if not os.path.exists(p):
            continue
        for r in csv.DictReader(open(p)):
            bad += r["status"] != "OK"
            tab.setdefault(s, {}).setdefault(int(r["N"]), []).append((int(r["n"]), int(r["pivots_primal"]) + int(r["pivots_dual"])))
    if not tab:
        continue
    Ns = sorted(next(iter(tab.values())))
    print(f"## {fam}: mean total pivots (primal + dual), R2 seeds 1-5")
    print("| setting | " + " | ".join(f"N {N} (n {tab[next(iter(tab))][N][0][0]})" for N in Ns) + " | power exp. | exp. base | better |")
    print("| --- |" + " --- |" * (len(Ns) + 3))
    for s in SETS:
        if s not in tab:
            continue
        m = {N: st.mean(x[1] for x in tab[s][N]) for N in Ns if N in tab[s]}
        ns = {N: tab[s][N][0][0] for N in m}
        bp, sp = fit([math.log(ns[N]) for N in m], [math.log(m[N]) for N in m])
        be, se = fit(list(m), [math.log(m[N]) for N in m])
        print(f"| {s} | " + " | ".join(f"{m[N]:.0f}" for N in Ns if N in m) +
              f" | n^{bp:.2f} (SSR {sp:.3f}) | {math.exp(be):.3f}^N (SSR {se:.3f}) | {'power' if sp < se else 'exp'} |")
    print()
print("## rand1k (first 1,000 rand10k games), R2 seeds 1-5: mean total pivots")
for s in SETS:
    p = os.path.join(R, f"rand1k.{s}.csv")
    if os.path.exists(p):
        rows = list(csv.DictReader(open(p)))
        bad += sum(r["status"] != "OK" for r in rows)
        t = [int(r["pivots_primal"]) + int(r["pivots_dual"]) for r in rows]
        print(f"- {s}: {len(rows)} runs, mean {st.mean(t):.2f}, max {max(t)}")
print(f"\nnon-OK rows: {bad}")
