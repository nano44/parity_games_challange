#!/usr/bin/env python3
"""Box 190: iterations of N5'-xi (both implementations agree) vs n on every family run (out/xcheck.txt N ranges; n from the fam_ files)."""
import os, re, glob
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); fig, ax = plt.subplots(figsize=(8, 5))
for f in sorted(glob.glob(os.path.join(HERE, "out", "fam_*.txt")) + glob.glob(os.path.join(HERE, "out", "pgs_*.txt"))):
    xs, ys = [], []
    for l in open(f):
        m = re.search(r" n (\d+) \| spec \d+ \| xi (\d+)", l)
        if m: xs.append(int(m.group(1))); ys.append(int(m.group(2)))
    if xs: ax.plot(xs, ys, marker=".", label=os.path.basename(f)[4:-4].lstrip("_"))
ax.set_xlabel("n (vertices)"); ax.set_ylabel("N5'-xi iterations"); ax.set_xscale("log"); ax.legend(fontsize=7, ncol=2)
ax.set_title("N5'-xi iterations on the hard families (CANDIDATE; DATA)"); fig.tight_layout()
fig.savefig(os.path.join(HERE, "out", "xi_growth.png"), dpi=110); print("wrote out/xi_growth.png")
