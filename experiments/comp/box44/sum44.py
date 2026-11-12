#!/usr/bin/env python3
"""L-COMP box 44: totals of the counter rows written by wchk44.py / free44.py / lev44.py (one line per file).
Usage: sum44.py FILE..."""
import sys, re, os
for fn in sys.argv[1:]:
    rows = [l for l in open(fn) if " | " in l and re.search(r"\| (s3fail|sum) ", l)]; tot = {}; mx = {}; fz = 0; fzn = 0
    if not rows: continue
    for l in rows:
        parts = l.split(" | ")
        cpart = next(p for p in parts if re.match(r"(s3fail|sum) ", p))
        if cpart.startswith("sum "): cpart = parts[parts.index(cpart) + 1]
        kv = cpart.split()
        for i in range(0, len(kv), 2): tot[kv[i]] = tot.get(kv[i], 0) + int(kv[i + 1])
        for k, pat in (("T", r"\| T(?:3\*)? (\d+) iterations"), ("T3", r"\| T3 (\d+) Ttot"), ("iterations", r"iterations (\d+) "), ("Ttot", r" Ttot (\d+) "), ("|W|", r"\|W\| (\d+) "), ("|V|", r"\|V\| (\d+) "), ("platmax", r"platmax (\d+)"), ("stalls", r"stalls (\d+)"), ("plateaus", r" plateaus (\d+)"), ("q", r" q (\d+) "), ("tail_len", r"tail_len (\d+)"), ("ties", r"myHoward T \d+ ties (\d+)")):
            m = re.search(pat, l)
            if m:
                v = int(m.group(1)); a = mx.setdefault(k, [0, 0]); a[0] = max(a[0], v); a[1] += v
        m = re.search(r"frozendiff (\d)", l)
        if m: fzn += 1; fz += int(m.group(1))
        m = re.search(r"T3/bound ([0-9.e+-]+)", l)
        if m: a = mx.setdefault("T3/bound", [0.0, 0.0]); a[0] = max(a[0], float(m.group(1)))
    nz = {k: v for k, v in tot.items() if v}
    print("%s: rows %d | must-0 sum %d%s | %s%s" % (os.path.basename(fn), len(rows), sum(v for k, v in tot.items() if k != "tdiff"), (" NONZERO " + str(nz)) if nz else "",
          " ".join("max %s %s sum %s" % (k, ("%.3e" % a[0]) if isinstance(a[0], float) else a[0], "-" if isinstance(a[0], float) else a[1]) for k, a in mx.items()),
          (" | rows differing from the frozen (T, iterations, |W|): %d of %d" % (fz, fzn)) if fzn else ""))
