#!/usr/bin/env python3
"""L-RED 69 R241 §7: sums of the NULL-switch runs (out/null/): kt241 json rows, generated TOTAL rows, climbs; and the B5 instance replay.
Usage: nullsumm241.py OUTDIR/null   (env none; reads only files)"""
import sys, os, re, glob
D = sys.argv[1]; tot = dict(runs=0, must0=0, nullsw=0, nullxi=0, T=0, xs=0, xd=0)
for f in sorted(glob.glob(os.path.join(D, "kt_*_null.out"))):
    r = dict(runs=0, must0=0, nullsw=0, nullxi=0, T=0, xs=0, xd=0)
    for l in open(f):
        if ": std" not in l: continue
        a = l.split(": ", 1)[1].split(" | ")[0]; r["runs"] += 1; r["must0"] += sum(int(v) for v in re.findall(r" (\d+)", " " + a))
        for k in ("nullsw", "nullxi"): r[k] += int(re.search(k + r" (\d+)", l).group(1))
        r["T"] += int(re.search(r"\| T (\d+)", l).group(1)); m = re.search(r"xdiff (\d+)", l)
        if m: r["xs"] += 1; r["xd"] += int(m.group(1))
    print(f"NULL241 {os.path.basename(f)}: " + " ".join(f"{k} {v}" for k, v in r.items())); [tot.__setitem__(k, tot[k] + r[k]) for k in r]
for l in open(os.path.join(D, "kt_randnull.out")):
    if not l.startswith("#"): continue
    m0 = sum(int(v) for v in re.findall(r" (\d+)", " " + l.split("genomes", 1)[1].split(" | ")[0].split(" ", 2)[2]))
    g = int(re.search(r"genomes (\d+)", l).group(1)); ns = int(re.search(r"nullsw (\d+)", l).group(1)); nx = int(re.search(r"nullxi (\d+)", l).group(1))
    T = int(re.search(r"\| T (\d+)", l).group(1)); xs, xd = map(int, re.search(r"sampled (\d+) xdiff (\d+)", l).groups())
    print(f"NULL241 {l.split()[0]}: runs {g} must0 {m0} nullsw {ns} nullxi {nx} T {T} xs {xs} xd {xd}")
    for k, v in (("runs", g), ("must0", m0), ("nullsw", ns), ("nullxi", nx), ("T", T), ("xs", xs), ("xd", xd)): tot[k] += v
print("NULL241 TOTAL runs: " + " ".join(f"{k} {v}" for k, v in tot.items()))
ev = 0; cand = 0
for f in sorted(glob.glob(os.path.join(D, "climb*.log"))):
    last = {}
    for l in open(f):
        m = re.match(r"CLIMB241 (\w+) END evals (\d+) best \((\d+), (\d+)", l)
        if m: last[m.group(1)] = (int(m.group(2)), int(m.group(4)))
        cand += int("CANDIDATE" in l)
    for t, (e, b) in last.items(): ev += e; print(f"NULL241 climb {t}: evals {e} best objective {b} (nullsw = objective // 1000)")
print(f"NULL241 climbs: evals {ev} candidates {cand}")
