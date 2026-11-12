#!/usr/bin/env python3
"""L-SI P-N5-GATE line L-3 = line L-2 (docs/si/P-N5-GATE-line-L2.txt, sha1 c0f2007d…) with fixes entry 3 applied. REFEREE 31's §5
strings (R-1..R-7, D-1..D-5b, G-a..G-c) are PARSED from the byte copy ref_R-P-N5-GATE_a401ce0e.md (sha1 asserted), never retyped; they are
applied in the report's table order, each old asserted exactly once in the current text; then the EXTRA replacements below (REFEREE-2's
line items and the lane's own, each old asserted once). Prints L-3 (one line). Usage: mkL3.py ROOT"""
import hashlib, os, re, sys
ROOT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
raw = open(os.path.join(ROOT, "docs/si/P-N5-GATE-line-L2.txt"), "rb").read()
assert hashlib.sha1(raw).hexdigest() == "c0f2007d84afab1e00ef41e24ba8f5f064468cc5"
rr = open(os.path.join(HERE, "ref_R-P-N5-GATE_a401ce0e.md"), "rb").read()
assert hashlib.sha1(rr).hexdigest() == "8c24800e21109d2dec4b1525bcef3445db7f7720"
sec = rr.decode("utf-8").split("## 5. Line L-2")[1].split("\n## ")[0]
ROWS = []
for l in sec.split("\n"):
    m = re.match(r"\| ((?:R|D|G)-[0-9a-z]+)[^|]*\| «(.*?)» \| «(.*?)»", l)
    if m: ROWS.append((m.group(1), m.group(2), m.group(3)))
assert [r[0] for r in ROWS] == ["R-1", "R-2", "R-3", "R-4", "R-5", "R-6", "R-7", "D-1", "D-2", "D-3", "D-4", "D-5a", "D-5b",
                                "G-a", "G-b", "G-c"], [r[0] for r in ROWS]
# EXTRA: REFEREE-2 37's line items and lane items, (id, old, new); filled when REFEREE-2's report is on origin.
EXTRA = []
def apply(L, rows):
    for i, a, b in rows:
        assert L.count(a) == 1, (i, L.count(a), a[:60])
        L = L.replace(a, b)
    return L
L = apply(raw.decode("utf-8"), ROWS)
L = apply(L, EXTRA)
assert "|" not in L and L.count("\n") == 1 and L.endswith("\n")
sys.stdout.write(L)
