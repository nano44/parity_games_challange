#!/usr/bin/env python3
"""L-RED successor 27: mkr (R106) moved into an EVEN-winning region. Priority classes of mkr.py: structural (LO <= p < HP), loops (odd
p < LO), z (Z), pivots h, h' (HP, HQ), markers (p > Z). New order, bottom to top: structural (same relative order) < z (now EVEN) <
loops (EVEN, order reversed, so Even's preference among loops is kept and every loop beats z) < h, h' < markers (same order and
parity). Owners, edges, labels, start unchanged. Usage: ewin.py MKR.pg OUT.pg"""
import re, sys
rows = []
for line in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(".*")?;?\s*$', line.strip().rstrip(';') + ';') if line[0].isdigit() else None
    m = re.match(r'(\d+) (\d+) ([01]) ([\d,]+) ?(".*")?;', line.strip())
    if m: rows.append([int(m.group(1)), int(m.group(2)), m.group(3), m.group(4), m.group(5) or ""])
lab = {r[0]: r[4].strip('"') for r in rows}
Z = next(r[1] for r in rows if lab[r[0]] == "z")
piv = {r[1] for r in rows if lab[r[0]] in ("h", "hp")}
loops = sorted(r[1] for r in rows if r[1] % 2 == 1 and r[1] < min(piv) and r[1] < Z and lab[r[0]] != "z" and r[1] < 10 ** 9 and
               any(lab[r[0]].startswith(x) for x in ("T", "L", "C1", "Cp0", "Tp")) and str(r[0]) in r[3].split(","))
cls = {}
for r in rows:
    p = r[1]
    if lab[r[0]] == "z": cls[r[0]] = (1, 0)
    elif p in loops: cls[r[0]] = (2, -p)
    elif p in piv: cls[r[0]] = (3, p)
    elif p > Z: cls[r[0]] = (4, p)
    else: cls[r[0]] = (0, p)
order = sorted(rows, key=lambda r: cls[r[0]]); x = 0; newp = {}
for r in order:
    c = cls[r[0]][0]
    want = {1: 0, 2: 0}.get(c, r[1] % 2)
    x += 1
    while x % 2 != want: x += 1
    newp[r[0]] = x
with open(sys.argv[2], "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for r in rows: f.write(f"{r[0]} {newp[r[0]]} {r[2]} {r[3]} {r[4]};\n")
print("loops", len(loops))
