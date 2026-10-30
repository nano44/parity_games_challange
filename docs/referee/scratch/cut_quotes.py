#!/usr/bin/env python3
"""REFEREE succ. 19: own check of the [Q path@commit:lines] «...» quotes of a packet (fragments split at '…', whitespace-normalised)."""
import re, subprocess, sys
txt = subprocess.run(["git", "show", sys.argv[1]], capture_output=True, text=True).stdout
norm = lambda s: re.sub(r"\s+", " ", s).strip()
pat = re.compile(r"\[Q ([^@\]]+)@([0-9a-f]+):(\d+)(?:-(\d+))?\]\s*«(.*?)»", re.S)
ok = bad = 0
for m in pat.finditer(txt):
    path, c, a, b, q = m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3)), m.group(5)
    src = subprocess.run(["git", "show", "%s:%s" % (c, path)], capture_output=True, text=True).stdout.split("\n")
    seg = norm(" ".join(src[a - 1:b]))
    frs = [norm(f) for f in q.split("…") if norm(f)]
    good = all(f in seg for f in frs)
    ok += good; bad += not good
    print("OK " if good else "BAD", path, c, a, b, len(frs))
print("quotes", ok + bad, "ok", ok, "bad", bad)
