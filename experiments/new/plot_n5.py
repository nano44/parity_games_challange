#!/usr/bin/env python3
"""N5 growth plots from the committed CSVs experiments/new/n5/<family>.csv -> docs/new/plots/n5_<family>.png.
Top: N5 iterations and fallbacks against n (log-log; dashed n^1, n^2 references through the first point). Bottom: wall seconds per
iteration against n (log-log), the measured cost of one iteration (2 valuations + up to 2 one-player optima, Python).
Also prints, per family: iterations per N, fallbacks per N, fallback fraction at the largest N, local slopes (last 3) of
iterations and of seconds/iteration in n. Usage: plot_n5.py fam ..."""
import csv, sys, os, math
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..", "..", "docs", "new", "plots")
INK, INK2, GRID, BLUE, ORANGE = "#0b0b0b", "#52514e", "#e4e3df", "#2a78d6", "#eb6834"
for fam in sys.argv[1:]:
    rows = [r for r in csv.DictReader(open(os.path.join(HERE, "n5", fam + ".csv"))) if r["n5_iterations"]]
    N = [int(r["N"]) for r in rows]; n = [float(r["n"]) for r in rows]; it = [max(int(r["n5_iterations"]), 1) for r in rows]
    fb = [int(r["fallback"]) for r in rows]; spi = [max(float(r["secs"]), 1e-3) / it[i] for i, r in enumerate(rows)]
    sl = lambda y: [round(math.log(y[i + 1] / y[i]) / math.log(n[i + 1] / n[i]), 2) for i in range(len(y) - 1) if n[i + 1] > n[i] and y[i] > 0][-3:]
    print(f"{fam}: N {N[0]}..{N[-1]}, n {int(n[0])}..{int(n[-1])}; iterations per N {it}; fallbacks per N {fb}; fallback fraction at "
          f"largest N {fb[-1]}/{it[-1]} = {fb[-1] / it[-1]:.2f}; slope iterations {sl(it)}; slope secs/iteration {sl(spi)}")
    fig, ax = plt.subplots(2, 1, figsize=(6, 7), sharex=True)
    for a in ax:
        a.set_xscale("log"); a.set_yscale("log"); a.grid(True, color=GRID, lw=0.8)
        for s in a.spines.values(): s.set_color(GRID)
        a.tick_params(colors=INK2)
    ax[0].plot(n, it, color=BLUE, lw=2, marker="o", ms=4, label="N5 iterations")
    fbp = [(n[i], fb[i]) for i in range(len(n)) if fb[i] > 0]
    if fbp: ax[0].plot(*zip(*fbp), color=ORANGE, lw=2, marker="s", ms=4, label="fallback steps (classical switch-all)")
    for k in (1, 2):
        ax[0].plot([n[0], n[-1]], [it[0], it[0] * (n[-1] / n[0]) ** k], color=INK2, lw=0.8, ls="--")
        ax[0].annotate(f"n^{k}", (n[-1], it[0] * (n[-1] / n[0]) ** k), color=INK2, fontsize=8)
    ax[1].plot(n, spi, color=BLUE, lw=2, marker="o", ms=4, label="wall seconds per iteration (Python)")
    for a in ax: a.legend(frameon=False, fontsize=8, labelcolor=INK)
    ax[0].set_title(f"N5 on {fam} (every row: regions = Oink zlk/tl, strategies verified)", color=INK, fontsize=10)
    ax[0].set_ylabel("iterations", color=INK2); ax[1].set_ylabel("seconds / iteration", color=INK2); ax[1].set_xlabel("n (vertices)", color=INK2)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, f"n5_{fam}.png"), dpi=110); plt.close(fig)
