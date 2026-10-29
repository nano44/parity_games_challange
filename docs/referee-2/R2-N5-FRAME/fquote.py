#!/usr/bin/env python3
"""REFEREE-2 own quote check for P-N5-FRAME: every «...» after [Q SPEC:a-b] (SPEC @9905dac3) and the
[R85c] quote (RESULTS @c9045f86 l. 5108-5109) must be a verbatim substring (whitespace-normalised) of the cited lines.
SHIFT=k moves every cited range by k lines (control; must fail)."""
import os, re, subprocess, sys
SHIFT = int(os.environ.get("SHIFT", "0"))
def show(rev, path):
    return subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True, check=True).stdout.split("\n")
pk = "\n".join(show("938d87967ce501058bc6d015e506403c73858034", "docs/new/P-N5-FRAME-box65.md"))
spec = show("9905dac3", "docs/new/N5-ssi-global.md")
res = show("c9045f86", "docs/RESULTS.md")
norm = lambda s: re.sub(r"\s+", " ", s).strip()
items = []
for m in re.finditer(r"\[Q SPEC:(\d+)(?:-(\d+))?\]\s*«(.*?)»", pk, re.S):
    a = int(m.group(1)); b = int(m.group(2) or a)
    items.append(("SPEC:%d-%d" % (a, b), spec, a, b, m.group(3)))
m = re.search(r"\[R85c\].*?\[Q\]\s*«(.*?)»", pk, re.S)
items.append(("RESULTS:5108-5109", res, 5108, 5109, m.group(1)))
ok = 0
for lab, src, a, b, q in items:
    text = norm(" ".join(src[a - 1 + SHIFT:b + SHIFT]))
    hit = norm(q) in text
    ok += hit
    print(("OK  " if hit else "MISS"), lab, norm(q)[:70])
print(f"quotes={len(items)} ok={ok} SHIFT={SHIFT}")
