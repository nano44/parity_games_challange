#!/usr/bin/env python3
"""Box 215 summary (L-NEW successor 75; copy of box 213's summ213.py with box 215's tool): one line per output file of out/ (keyside215_*), summing the counters of all
genome / random lines (T and maxlen: maximum), the number of genome lines, TIMEOUT lines and whether the file ends with DONE (frozen
runners). Must-0 sums are printed as must0_sum. Run from experiments/new/box215; output pinned as out/summ215.txt."""
import os, glob, collections
MUST0 = {"keyside215": ("lkp", "pkf", "pkfa", "kflip", "casc", "ftt", "ladder")}
MAXK = ("T", "maxF", "maxmoves")
for f in sorted(glob.glob("out/*.out")):
    base = os.path.basename(f)
    tool = next((t for t in ("keyside215",) if base.startswith(t)), None)
    if tool is None: continue
    s = collections.Counter(); lines = 0; to = 0; done = False
    for ln in open(f):
        t = ln.split()
        if not t: continue
        if t[0] == "DONE": done = True; continue
        if t[0] == "TIMEOUT": to += 1; continue
        lines += 1; i = 1
        while i + 1 < len(t):
            try: v = int(t[i + 1])
            except ValueError: i += 1; continue
            k = t[i]; s[k] = max(s[k], v) if k in MAXK else s[k] + v; i += 2
    m0 = sum(s[k] for k in MUST0[tool])
    keys = [k for k in s if k not in ("seed", "genomes", "ctrl", "cyconly")]
    print(base, "lines", lines, "timeouts", to, "done", int(done), "must0_sum", m0, " ".join("%s %d" % (k, s[k]) for k in keys))
