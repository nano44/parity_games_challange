#!/usr/bin/env python3
"""L-NEW box 50: disjoint union of parity games (vertex ids shifted; priorities kept, so the rank order interleaves the components).
Usage: dunion.py OUT.pg A.pg B.pg ..."""
import sys
out, ins = sys.argv[1], sys.argv[2:]; lines = []; off = 0
for f in ins:
    rows = [l.strip().rstrip(";") for l in open(f) if l.strip() and not l.startswith("parity")]
    k = 0
    for l in rows:
        p = l.split(); v, pr, ow, su = int(p[0]), int(p[1]), int(p[2]), p[3]
        lines.append("%d %d %d %s;" % (v + off, pr, ow, ",".join(str(int(x) + off) for x in su.split(",")))); k = max(k, v + 1)
    off += k
open(out, "w").write("parity %d;\n" % (off - 1) + "\n".join(lines) + "\n")
