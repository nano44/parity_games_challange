#!/usr/bin/env python3
"""REFEREE succ. 14: own re-check of every [Q path@commit:lines] «...» in a packet (not the lane's quotecheck.py). Whitespace normalised;
"…" separates parts that must occur in order within the cited line range. Prints PASS/FAIL per quote."""
import re, sys, subprocess
txt = open(sys.argv[1]).read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
n = bad = 0
for m in re.finditer(r"\[Q ([^@\]]+)@([0-9a-f]+):(\d+)(?:-(\d+))?\]\s*«(.*?)»", txt, re.S):
    path, com, a, b, q = m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3)), m.group(5)
    src = subprocess.run(["git", "show", "%s:%s" % (com, path)], capture_output=True, text=True).stdout.split("\n")
    seg = norm(" ".join(src[a - 1:b])); pos = 0; ok = True
    for part in [norm(p) for p in q.split("…") if norm(p)]:
        i = seg.find(part, pos)
        if i < 0: ok = False; break
        pos = i + len(part)
    n += 1; bad += not ok
    print("PASS" if ok else "FAIL", "%s@%s:%d-%d" % (path, com, a, b), norm(q)[:70])
print("QUOTES", n, "FAILED", bad)
