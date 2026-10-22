#!/usr/bin/env python3
"""Plots for N1 (gauntlet step 2 growth record): per family, against n (log-log): plain VJ switch-all, N1 total Even
switches, N1 largest single phase. Input out/anneal/summary_c.csv; output docs/new/plots/n1_<family>.png and n1_all.png.
Usage: plot_n1.py [csv]"""
import sys, os, csv, collections
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..", "..", "docs", "new", "plots"); os.makedirs(OUT, exist_ok=True)
rows = [r for r in csv.DictReader(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out", "anneal", "summary_c.csv")))
        if r.get("even_iters") not in (None, "") and r["family"] != "SWEEP DONE"]
fam = collections.OrderedDict()
for r in rows: fam.setdefault(r["family"], []).append(r)
S = [("switchall_plain", "plain VJ switch-all", "#2a78d6", "o"), ("even_iters", "N1 total Even switches", "#eb6834", "s"),
     ("max_phase", "N1 largest phase", "#1baf7a", "^")]
def draw(ax, name, rs):
    for key, lab, col, mk in S:
        pts = [(int(r["n"]), int(r[key])) for r in rs if r[key].isdigit() and int(r[key]) > 0]
        if pts: ax.plot(*zip(*pts), color=col, marker=mk, markersize=5, linewidth=2, label=lab)
    ax.set_xscale("log"); ax.set_yscale("log"); ax.set_title(name, fontsize=10, color="#222222")
    ax.grid(True, which="major", color="#e6e5e0", linewidth=0.8); ax.tick_params(labelsize=8, colors="#555555")
    for s in ax.spines.values(): s.set_color("#cccccc")
k = len(fam); cols = 4; rws = (k + cols - 1) // cols
fig, axs = plt.subplots(rws, cols, figsize=(4 * cols, 3.1 * rws), squeeze=False)
for i, (name, rs) in enumerate(fam.items()):
    draw(axs[i // cols][i % cols], name, rs)
    f1, a1 = plt.subplots(figsize=(5, 3.6)); draw(a1, name, rs); a1.set_xlabel("n (vertices)", fontsize=9); a1.set_ylabel("Even switches", fontsize=9)
    a1.legend(fontsize=8, frameon=False); f1.tight_layout(); f1.savefig(os.path.join(OUT, f"n1_{name}.png"), dpi=110); plt.close(f1)
for j in range(k, rws * cols): axs[j // cols][j % cols].axis("off")
h, l = axs[0][0].get_legend_handles_labels(); fig.legend(h, l, loc="upper center", ncol=3, frameon=False, fontsize=10)
fig.supxlabel("n (vertices), log scale"); fig.supylabel("Even switches, log scale")
fig.tight_layout(rect=(0, 0, 1, 0.96)); fig.savefig(os.path.join(OUT, "n1_all.png"), dpi=100)
print("wrote", len(fam), "family plots to", os.path.relpath(OUT))
