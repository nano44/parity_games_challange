#!/usr/bin/env python3
"""Box 18: aggregate nm.py / inv.py logs. Usage: agg.py nm|inv LOG ..."""
import json, sys
kind = sys.argv[1]; rows = []; err = 0
for f in sys.argv[2:]:
    for l in open(f):
        if l.startswith("ERROR"): err += 1; continue
        p = l.split(" ", 7)
        if p[0] == ("NM" if kind == "nm" else "INV"):
            rest = l.split(" ", 7)[7] if kind == "nm" else None
            if kind == "nm": rows.append((p[1], p[2], int(p[4]), json.loads(p[7])))
            else:
                a, b = p[7].split("} {", 1); rows.append((p[1], p[2], int(p[4]), json.loads(a + "}"), json.loads("{" + b)))
print("instances", len(rows), "errors", err)
if kind == "nm":
    for k in ("pch_max", "nm_max", "nm_over_n_max", "ft_max", "ftnm_max", "reset_max", "resetnm_max", "gate_nm_max", "gate_ftnm_max"):
        b = max(rows, key=lambda r: r[3][k]); print(f"  {k}: {b[3][k]} ({b[0]} {b[1]} n {b[2]})")
    top = sorted(rows, key=lambda r: -r[3]["nm_over_n_max"])[:5]; print("  top NM/n:", [(r[0].split('/')[-1], r[1], r[2], r[3]["nm_max"], r[3]["pch_max"]) for r in top])
else:
    keys = sorted({k for r in rows for k in r[3]})
    for k in keys:
        tot = sum(r[3].get(k, 0) for r in rows); inst = [r for r in rows if r[3].get(k, 0)]
        print(f"  {k}: total {tot} in {len(inst)} instances" + (f"; first {inst[0][0]} {inst[0][1]} n {inst[0][2]}: {inst[0][4].get(k)}" if inst and k not in ('lip_checks', 'pchanges') else ""))
