#!/usr/bin/env python3
"""REFEREE-2 41: sum the TOTAL / INFO lines of r2unit217.py outputs (chunks of a corpus sweep). Usage: sum217.py FILES..."""
import sys, re
from collections import defaultdict
tot = defaultdict(int); info = defaultdict(int); mx = defaultdict(int); fired = set(); files = 0; unfinished = []; skipped = 0; lv = defaultdict(int); bc = set()
for fn in sys.argv[1:]:
    txt = open(fn).read()
    if "\nFIRED " not in "\n" + txt: unfinished.append(fn); continue
    files += 1
    for l in txt.splitlines():
        if l.startswith("TOTAL "):
            t = l.split(": ", 1)[1].split()
            for k, v in zip(t[0::2], t[1::2]): tot[k] += int(v)
        elif l.startswith("INFO "):
            m = re.search(r"full_by_level (\S*) bridge_len_const (.*)$", l)
            for it in (m.group(1).split(",") if m and m.group(1) else []):
                a, b = it.split(":"); lv[int(a)] += int(b)
            if m: bc |= set(re.findall(r"-?\d+", m.group(2)))
            t = l[5:].split(" full_by_level")[0].split()
            for k, v in zip(t[0::2], t[1::2]):
                if k in ("k", "maxT", "maxsw", "Thoward_max"): mx[k] = max(mx[k], int(v))
                else: info[k] += int(v)
        elif l.startswith("FIRED "):
            f, _, s = l[6:].partition(" | files skipped as Ξ-cyclic ")
            if f.strip() != "none": fired |= set(f.split())
            skipped += int(s or 0)
print(f"SUM over {files} finished files (unfinished: {len(unfinished)}): " + " ".join(f"{k} {v}" for k, v in tot.items()))
print("INFO " + " ".join(f"{k} {v}" for k, v in info.items()) + " " + " ".join(f"{k} {v}" for k, v in mx.items())
      + " full_by_level " + ",".join(f"{a}:{b}" for a, b in sorted(lv.items())) + f" bridge_len_const {sorted(bc)}")
print("FIRED " + (" ".join(sorted(fired)) or "none") + f" | files skipped as Ξ-cyclic {skipped}")
