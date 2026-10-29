#!/usr/bin/env python3
"""REFEREE-2 succ. 19 (Opus 5.5, D15): own verbatim check of every [Q path@commit:lines] «...» in a packet. For each tag: git show
commit:path, join the tagged lines (whitespace runs normalised) and require the quote to be a substring of THOSE lines. Control
SHIFT=k shifts every line range by k (must report mismatches). Usage: qcheck.py packet [rev]   (rev: read the packet at git rev)"""
import sys, re, subprocess, os
SHIFT = int(os.environ.get("SHIFT", "0"))
pk = sys.argv[1]
txt = subprocess.run(["git", "show", f"{sys.argv[2]}:{pk}"], capture_output=True, text=True, check=True).stdout if len(sys.argv) > 2 else open(pk).read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
tags = re.findall(r"\[Q ([^@\]]+)@([0-9a-f]+):(\d+)(?:-(\d+))?\]\s*«(.*?)»", txt, re.S)
ok = 0; cache = {}
for path, com, a, b, q in tags:
    a = int(a) + SHIFT; b = (int(b) if b else int(a) - SHIFT) + SHIFT
    key = (com, path)
    if key not in cache: cache[key] = subprocess.run(["git", "show", f"{com}:{path}"], capture_output=True, text=True, check=True).stdout.split("\n")
    seg = norm(" ".join(cache[key][a - 1:b]))
    hit = norm(q) in seg
    ok += hit
    print(("OK   " if hit else "MISS ") + f"{path}@{com}:{a}-{b} | {norm(q)[:90]}")
print(f"tags {len(tags)} ok {ok} miss {len(tags) - ok} SHIFT {SHIFT}")
