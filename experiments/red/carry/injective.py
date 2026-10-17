#!/usr/bin/env python3
"""L-RED: rewrite a .pg game with INJECTIVE priorities, preserving the order (priority, then the given tie order) and
parity. Tie order: 'stable' = vertex id, 'oink' = Oink's std::sort reindexing (L-ALG stdsort.oink_order via LALG_DIR).
Usage: injective.py IN.pg OUT.pg [stable|oink]"""
import sys, os, re
rows = []
for line in open(sys.argv[1]):
    m = re.match(r"^(\d+)\s+(\d+)\s+([01])\s+([\d,]+)", line.strip())
    if m: rows.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4)))
rows.sort(); pr = [r[1] for r in rows]
mode = sys.argv[3] if len(sys.argv) > 3 else "stable"
if mode == "oink":
    sys.path.insert(0, os.path.join(os.environ["LALG_DIR"], "experiments", "dtl-bench")); from stdsort import oink_order
    order = oink_order(pr)
else:
    order = sorted(range(len(pr)), key=lambda v: (pr[v], v))
new, last = {}, -1
for v in order:
    q = last + 1
    if q % 2 != pr[v] % 2: q += 1
    new[v] = q; last = q
with open(sys.argv[2], "w") as f:
    f.write(f"parity {len(rows) - 1};\n")
    for v, p, o, s in rows: f.write(f"{v} {new[v]} {o} {s};\n")
