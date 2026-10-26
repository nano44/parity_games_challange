#!/usr/bin/env python3
"""REFEREE-2 succ. 17: own check of «…» quotes tagged [Q path@commit:a-b] (or :a) in a packet. Whitespace runs normalised; "…" inside a
quote separates parts, each part must occur inside lines a..b of `git show commit:path`. Usage: qtags.py packet_file"""
import sys, re, subprocess
txt = open(sys.argv[1]).read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
pat = re.compile(r"\[Q ([^@\]]+)@([0-9a-f]+):(\d+)(?:-(\d+))?\]\s*«(.*?)»", re.S)
n = bad = 0
for m in pat.finditer(txt):
    path, c, a, b, q = m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3)), m.group(5)
    src = subprocess.run(["git", "show", f"{c}:{path}"], capture_output=True, text=True).stdout.split("\n")
    win = norm(" ".join(src[a - 1:b]))
    parts = [norm(p) for p in q.split("…") if norm(p)]
    miss = [p for p in parts if p not in win]
    n += 1; bad += bool(miss)
    print(("OK   " if not miss else "MISS ") + f"{path}@{c}:{a}-{b} | " + norm(q)[:90] + (f"  MISSING: {miss}" if miss else ""))
print(f"tagged quotes {n} ok {n - bad} missing {bad}")
untagged = len(re.findall("«", txt)) - n
print(f"«-quotes without a [Q] tag right before them: {untagged}")
