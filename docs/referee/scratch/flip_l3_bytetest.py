#!/usr/bin/env python3
"""REFEREE successor 24: byte test of P-IDEAL-FLIP line L-3. Expected = L-2 (l-new 4c2e5124, sha1 8099415b…) with exactly CHECKER C122
§5's replacements R1-R4, the old/new strings taken from the CHECKER file itself (claude/checker 80ed31a6), wrapped lines joined with
single spaces. Usage: python3 -I flip_l3_bytetest.py L2.txt C122.md [L3.txt]"""
import hashlib, re, sys
l2 = open(sys.argv[1], "rb").read().decode()
c = open(sys.argv[2]).read()
sec = c[c.index("## 5."):c.index("## DONE")]
lines = sec.split("\n")
items, cur = [], None
for ln in lines:
    m = re.match(r"  - (R[1-4])\. (.*)", ln)
    if m:
        cur = [m.group(1), m.group(2)]; items.append(cur)
    elif cur and ln.startswith("    ") and not ln.startswith("  - "):
        cur[1] += " " + ln.strip()
    else:
        cur = None
out = l2
for name, txt in items:
    m = re.fullmatch(r"«(.*)» → «(.*)»", txt)
    assert m, (name, txt)
    old, new = m.group(1), m.group(2)
    print(name, "old occurrences in L-2:", l2.count(old), "len old/new", len(old), len(new))
    assert out.count(old) == 1
    out = out.replace(old, new)
exp = out.encode()
print("replacements", [i[0] for i in items], "expected sha1", hashlib.sha1(exp).hexdigest(), "bytes", len(exp),
      "lines", exp.count(b"\n"), "(", out.count("("), ")", out.count(")"))
if len(sys.argv) > 3:
    got = open(sys.argv[3], "rb").read()
    print("L-3 sha1", hashlib.sha1(got).hexdigest(), "bytes", len(got), "EQUAL expected:", got == exp)
    if got != exp:
        import difflib
        for d in difflib.ndiff([exp.decode()], [got.decode()]):
            if d[0] in "?+-": print(d[:3000])
