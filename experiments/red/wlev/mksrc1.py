#!/usr/bin/env python3
"""L-RED R155: Lemma ONE-SOURCE test. Input: an n5b game + start, a lower source vertex SRC (its W rises many times in one W-run) and a
fixed marker MV. Priorities rescaled p -> 4p + (p % 2). Added: Even h2 (priority 0) with K1 DYNAMIC options a_j (Odd, priority 0) ->
m_j -> SRC (common suffix: SRC's play) and K0 STATIC options b_i (Odd, priority 0) -> s_i -> MV. Marker priorities: dynamic 4x + 3 (odd), static 4y + 2
(even); both fall between rescaled priorities. Start sigma(h2) = a_1. Usage: mksrc1.py IN.pg IN.start SRC MV x1,..(dyn) y1,..(static) OUT"""
import sys, re
src, sst, SRC, MV = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
XD = [int(x) for x in sys.argv[5].split(",")]; XS = [int(x) for x in sys.argv[6].split(",")] if sys.argv[6] != "-" else []; out = sys.argv[7]
rows = []
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;', line)
    if m: rows.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), [int(a) for a in m.group(4).split(",")], m.group(5) or ""])
rows.sort(); n = len(rows)
for r in rows: r[1] = 4 * r[1] + (r[1] % 2)
h = n; opts = []; nx = n + 1; extra = []
for j, x in enumerate(XD):
    a, mk = nx, nx + 1; nx += 2; opts.append(a)
    extra += [[a, 0, 1, [mk], f"da{j+1}"], [mk, 4 * x + 3, 1, [SRC], f"mda{j+1}"]]
for i, y in enumerate(XS):
    b, mk = nx, nx + 1; nx += 2; opts.append(b)
    extra += [[b, 0, 1, [mk], f"sb{i+1}"], [mk, 4 * y + 2, 1, [MV], f"msb{i+1}"]]
rows.append([h, 0, 0, opts, "h2"]); rows += extra
with open(out + ".pg", "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for r in rows: f.write(f'{r[0]} {r[1]} {r[2]} {",".join(map(str, r[3]))} "{r[4]}";\n')
st = open(sst).read().split("\n"); S = [l for l in st if l.startswith("SIGMA0")][0]; T = [l for l in st if l.startswith("TAU0")][0]
S += f" {h}:{opts[0]}"; T += "".join(f" {r[0]}:{r[3][0]}" for r in extra)
open(out + ".start", "w").write(S + "\n" + T + "\n")
