"""switchbestexp under R2: means per N and power-law vs exponential least-squares fits on log(mean dual pivots).
Usage: fit_sbe.py CSV [CSV ...] (bench.py rows, family switchbestexp, rule r2). Prints the Lead's combined series too."""
import csv
import math
import statistics as st
import sys


def n_of(N):
    return 25 * N + 10          # switchbestexp size (pgsolver_port): n = 35, 60, ..., 560 for N = 1..22


def fit(xs, ys):
    mx, my = st.mean(xs), st.mean(ys)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    return a, b, sum((y - a - b * x) ** 2 for x, y in zip(xs, ys))


def report(label, pts):
    Ns = sorted(pts)
    ly = [math.log(pts[N]) for N in Ns]
    _, bp, sp = fit([math.log(n_of(N)) for N in Ns], ly)
    _, be, se = fit(Ns, ly)
    ratios = [pts[b] / pts[a] for a, b in zip(Ns, Ns[1:])]
    print(f"{label}: N {Ns[0]}..{Ns[-1]}: power law n^{bp:.2f} (SSR {sp:.4f}); exponential {math.exp(be):.3f}^N (SSR {se:.4f}); "
          f"better: {'power' if sp < se else 'exponential'}")
    print("  means: " + ", ".join(f"N{N}={pts[N]:.0f}" for N in Ns))
    print("  ratio per +2N: " + ", ".join(f"{r:.2f}" for r in ratios))
    up = [i for i in range(1, len(ratios)) if ratios[i] > 1.6 and ratios[i - 1] > 1.6]
    print(f"  ratio > 1.6 twice in a row: {'YES at ' + str([Ns[i + 1] for i in up]) if up else 'no'}")


rows = []
for p in sys.argv[1:]:
    with open(p) as f:
        rows += [r for r in csv.DictReader(f) if r["family"] == "switchbestexp" and r["rule"] == "r2"]
bad = [r for r in rows if r["status"] != "OK"]
by = {}
for r in rows:
    if r["status"] == "OK":
        by.setdefault(int(r["N"]), {})[int(r["seed"])] = int(r["pivots_dual"])
print(f"rows {len(rows)}, non-OK {len(bad)}")
for N in sorted(by):
    d = by[N]; v = [d[s] for s in sorted(d)]
    v5 = [d[s] for s in range(1, 6) if s in d]
    print(f"N {N:2d} n {n_of(N)}: seeds {len(v)}: mean {st.mean(v):.1f} sd {st.pstdev(v):.1f} min {min(v)} max {max(v)}; "
          f"seeds 1-5 mean {st.mean(v5):.1f} sd {st.pstdev(v5):.1f}")
mine_all = {N: st.mean(by[N].values()) for N in by if N >= 6 and N % 2 == 0}
mine5 = {N: st.mean([by[N][s] for s in range(1, 6) if s in by[N]]) for N in by if N >= 6 and N % 2 == 0}
lead = {6: 621, 8: 948, 10: 1550, 12: 2069, 14: 3014, 16: 4052}      # L-NEW (N8d §4) and L-RED (R54 §3) means
lead.update({N: mine5[N] for N in mine5 if N >= 18})
report("Lead series (L-NEW N6-12, L-RED N14-16, mine seeds 1-5 N>=18)", lead)
report("mine, seeds 1-5", mine5)
report("mine, all seeds", mine_all)
for lo in (10, 14):
    report(f"mine, all seeds, N >= {lo}", {N: v for N, v in mine_all.items() if N >= lo})
