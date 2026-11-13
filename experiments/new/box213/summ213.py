#!/usr/bin/env python3
"""Box 213 summary (L-NEW successor 75): one line per output file of out/ (key213_*, keymu213_*, g2_213_*, kcount213_*), summing the counters of all
genome / random lines (T and maxlen: maximum), the number of genome lines, TIMEOUT lines and whether the file ends with DONE (frozen
runners). Must-0 sums are printed as must0_sum. Run from experiments/new/box213; output pinned as out/summ213.txt."""
import os, glob, collections
MUST0 = {"key213": ("n5out", "keytau_tail"), "keymu213": ("tau3", "kp", "kpn", "muinc", "muflat", "mukappa", "unreach", "hdec"),
         "g2_213": ("g2fail", "g2e"), "kcount213": ("kviol",)}
MAXK = ("T", "maxlen", "maxsw", "maxK", "N", "M")
for f in sorted(glob.glob("out/*.out")):
    base = os.path.basename(f)
    tool = next((t for t in ("keymu213", "key213", "g2_213", "kcount213") if base.startswith(t)), None)
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
    keys = [k for k in s if k not in ("seed", "genomes", "ctrl")]
    print(base, "lines", lines, "timeouts", to, "done", int(done), "must0_sum", m0, " ".join("%s %d" % (k, s[k]) for k in keys))
