#!/usr/bin/env python3
"""Box 47: check every “…” quote of a fixes file against source files at a git revision: whitespace normalised, then substring test.
Prints, per quote, the source file(s) and line(s) where it occurs; exit 1 if any quote occurs in none.
Usage: quotecheck.py FIXES.md REV SRC1 [SRC2 ...]   (run from the repository root)"""
import sys, re, subprocess
fx, rev, srcs = sys.argv[1], sys.argv[2], sys.argv[3:]
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
S = {}
for f in srcs:
    S[f] = norm_with_lines(subprocess.run(["git", "show", f"{rev}:{f}"], capture_output=True, text=True, check=True).stdout)
quotes = re.findall(r"“(.+?)”", re.sub(r"\s+", " ", open(fx).read()))
bad = 0
for q in quotes:
    hits = []
    for f, (t, lines) in S.items():
        i = t.find(q)
        while i >= 0:
            hits.append(f"{f.split('/')[-1]} l. {lines[i]}" + (f"-{lines[i + len(q) - 1]}" if lines[i + len(q) - 1] != lines[i] else ""))
            i = t.find(q, i + 1)
    if not hits: bad += 1
    print(("OK   " if hits else "MISS ") + q[:70] + (" …" if len(q) > 70 else "") + " | " + ("; ".join(hits[:3]) + (" …" if len(hits) > 3 else "") if hits else "-"))
print(f"{len(quotes)} quotes, {len(quotes) - bad} found, {bad} missing")
sys.exit(1 if bad else 0)
