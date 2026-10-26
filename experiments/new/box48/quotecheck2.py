#!/usr/bin/env python3
"""Box 48: as box47/quotecheck.py, but each source is REV:FILE (sources at different revisions, e.g. two referee branches).
Every “…” quote of FIXES.md (whitespace normalised) must occur in some source; prints file:line hits; exit 1 if any quote is missing.
Usage: quotecheck2.py FIXES.md REV1:FILE1 [REV2:FILE2 ...]   (run from the repository root)"""
import sys, re, subprocess
fx, srcs = sys.argv[1], sys.argv[2:]
def norm_with_lines(text):
    out, lines, ln, prev_space = [], [], 1, True
    for ch in text:
        if ch == "\n": ln += 1
        if ch.isspace():
            if not prev_space: out.append(" "); lines.append(ln)
            prev_space = True
        else:
            out.append(ch); lines.append(ln); prev_space = False
    return "".join(out), lines
S = {s: norm_with_lines(subprocess.run(["git", "show", s], capture_output=True, text=True, check=True).stdout) for s in srcs}
quotes = re.findall(r"“(.+?)”", re.sub(r"\s+", " ", open(fx).read()))
bad = 0
for q in quotes:
    hits = []
    for s, (t, lines) in S.items():
        i = t.find(q)
        while i >= 0:
            hits.append(f"{s}:{lines[i]}-{lines[i + len(q) - 1]}"); i = t.find(q, i + 1)
    print(("OK   " if hits else "MISS ") + " ".join(hits[:3]) + " | " + q[:90])
    bad += not hits
print(f"quotes {len(quotes)} missing {bad}")
sys.exit(1 if bad else 0)
