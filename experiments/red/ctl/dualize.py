#!/usr/bin/env python3
"""L-RED successor 26: the dual game G^d (owners swapped, priorities + 1, same vertex ids, successor order and labels) and the swapped
start (SIGMA0 <-> TAU0). Usage: dualize.py GAME.pg START OUT.pg OUT.start"""
import re, sys
rows = []
for line in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)(.*)$', line)
    if m: rows.append((int(m.group(1)), int(m.group(2)) + 1, 1 - int(m.group(3)), m.group(4), m.group(5)))
with open(sys.argv[3], "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for v, p, o, s, rest in rows: f.write(f"{v} {p} {o} {s}{rest}\n")
st = {l.split()[0]: l.split()[1:] for l in open(sys.argv[2]) if l.strip()}
with open(sys.argv[4], "w") as f:
    f.write("SIGMA0 " + " ".join(st.get("TAU0", [])) + "\nTAU0 " + " ".join(st.get("SIGMA0", [])) + "\n")
