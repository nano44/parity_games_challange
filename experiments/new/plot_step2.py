#!/usr/bin/env python3
"""Plots for N1 gauntlet step 2 (box 2) from the committed CSVs experiments/new/step2/*.csv -> docs/new/plots/step2_<fam>.png.
Top: Howard iterations (N1 even + odd, and plain VJ switch-all for contrast) against n, log-log. Bottom: N1 wall seconds against
n, log-log. Dashed gray: slope references n^1, n^2, n^3 through the first N1 point. Also prints the local log-log slope
(fitted exponent between consecutive sizes) of N1 iterations and seconds for the verdict lines."""
import csv, sys, os, math
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..", "..", "docs", "new", "plots")
INK, INK2, GRID, BLUE, ORANGE = "#0b0b0b", "#52514e", "#e4e3df", "#2a78d6", "#eb6834"
def num(x):
    try: return float(x)
    except ValueError: return None
for fam in sys.argv[1:]:
    rows = [r for r in csv.DictReader(open(os.path.join(HERE, "step2", fam + ".csv"))) if num(r["even_iters"]) is not None]
    if not rows: continue
    n = [num(r["n"]) for r in rows]; it = [num(r["even_iters"]) + num(r["odd_iters"]) for r in rows]
    sec = [max(num(r["secs"]), 1e-3) for r in rows]; vj = [(num(r["n"]), num(r["vj_switchall_plain"])) for r in rows if num(r["vj_switchall_plain"])]
    fig, ax = plt.subplots(2, 1, figsize=(6, 7), sharex=True)
    for a in ax:
        a.set_xscale("log"); a.set_yscale("log"); a.grid(True, which="major", color=GRID, lw=0.8)
        for s in a.spines.values(): s.set_color(GRID)
        a.tick_params(colors=INK2)
    ax[0].plot(n, it, color=BLUE, lw=2, marker="o", ms=4, label="N1 (even + odd Howard iterations)")
    if vj: ax[0].plot(*zip(*vj), color=ORANGE, lw=2, marker="s", ms=4, label="plain VJ switch-all (contrast)")
    ax[1].plot(n, sec, color=BLUE, lw=2, marker="o", ms=4, label="N1 wall seconds (bit cost)")
    for a, y in ((ax[0], it), (ax[1], sec)):
        for k in (1, 2, 3):
            a.plot([n[0], n[-1]], [y[0], y[0] * (n[-1] / n[0]) ** k], color=INK2, lw=0.8, ls="--")
            a.annotate(f"n^{k}", (n[-1], y[0] * (n[-1] / n[0]) ** k), color=INK2, fontsize=8)
        a.legend(frameon=False, fontsize=8, labelcolor=INK)
    ax[0].set_title(f"N1 on {fam} (all runs: Zielonka OK, strategies verified)", color=INK, fontsize=10)
    ax[0].set_ylabel("iterations", color=INK2); ax[1].set_ylabel("seconds", color=INK2); ax[1].set_xlabel("n (vertices)", color=INK2)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, f"step2_{fam}.png"), dpi=110); plt.close(fig)
    sl = lambda y: [round(math.log(y[i + 1] / y[i]) / math.log(n[i + 1] / n[i]), 2) if n[i + 1] > n[i] and y[i] > 0 else None for i in range(len(y) - 1)]
    print(fam, "N", rows[0]["N"], "-", rows[-1]["N"], "n", int(n[0]), "-", int(n[-1]), "iters", int(it[0]), "-", int(it[-1]),
          "| slope iters", sl(it)[-4:], "| slope secs", sl(sec)[-4:])
