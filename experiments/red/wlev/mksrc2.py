#!/usr/bin/env python3
"""L-RED R156: k-SOURCE test. Like mksrc1.py (priorities p -> 4p + (p % 2)), with several dynamic classes: class c has options
d<c>a<j> (Odd, prio 0) -> m (odd prio 4x + 3) -> SRC_c; static options sb<i> -> (even prio 4y + 2) -> MV. Even h2 (prio 0), start on
the first option. Env EVEN=1 (R157): dynamic markers even, 4x + 2.
Usage: mksrc2.py IN.pg IN.start MV "SRC1:x,x,..;SRC2:x,.." y,y,..|- OUT"""
import sys, re, os
EVEN = os.environ.get("EVEN") == "1"          # R157: even dynamic markers 4x + 2
src, sst, MV, CL, YS, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
classes = [(int(a.split(":")[0]), [int(x) for x in a.split(":")[1].split(",")]) for a in CL.split(";")]
XS = [int(y) for y in YS.split(",")] if YS != "-" else []
rows = []
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if m: rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), [int(a) for a in m.group(4).split(",")], m.group(5) or ""])
rows.sort(); n = len(rows)
for r in rows: r[1] = 4 * r[1] + (r[1] % 2)
h = n; opts = []; nx = n + 1; extra = []
for c, (S, xs) in enumerate(classes, 1):
    for j, x in enumerate(xs, 1):
        a, mk = nx, nx + 1; nx += 2; opts.append(a)
        extra += [[a, 0, 1, [mk], f"d{c}a{j}"], [mk, 4 * x + (2 if EVEN else 3), 1, [S], f"md{c}a{j}"]]
for i, y in enumerate(XS, 1):
    b, mk = nx, nx + 1; nx += 2; opts.append(b)
    extra += [[b, 0, 1, [mk], f"sb{i}"], [mk, 4 * y + 2, 1, [MV], f"msb{i}"]]
rows.append([h, 0, 0, opts, "h2"]); rows += extra
with open(out + ".pg", "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for r in rows: f.write(f'{r[0]} {r[1]} {r[2]} {",".join(map(str, r[3]))} "{r[4]}";\n')
st = open(sst).read().split("\n"); S0 = [l for l in st if l.startswith("SIGMA0")][0]; T0 = [l for l in st if l.startswith("TAU0")][0]
S0 += f" {h}:{opts[0]}"; T0 += "".join(f" {r[0]}:{r[3][0]}" for r in extra)
open(out + ".start", "w").write(S0 + "\n" + T0 + "\n")
