#!/usr/bin/env python3
# P-N5-ASC line L-3 generator (L-NEW successor 63). From the repo root: python3 experiments/new/box193/mkl3_193.py C135_COPY
# C135_COPY = git show 0942e8be:docs/checker/C135.md (byte-for-byte). Applies C135 §5 R1-R4 to L-2; asserts sha1 0012d671.
import sys, re, hashlib
c = open(sys.argv[1], encoding="utf-8").read().split("\n")
i = c.index("## 5. The L-3 (exact wording)")
items, cur = [], None
for ln in c[i+1:]:
    if ln.startswith("- "):
        if cur is not None: items.append(cur)
        cur = ln[2:]
    elif ln.startswith("  ") and cur is not None: cur += " " + ln.strip()
    else:
        if cur is not None: items.append(cur); cur = None
        if ln.startswith("## "): break
reps = []
for it in items:
    m = re.match(r"(R\d) \(E-\d\): «(.*)» → «(.*)»$", it)
    if m: reps.append(m.groups())
assert [r[0] for r in reps] == ["R1", "R2", "R3", "R4"], reps
L = open("docs/new/P-N5-ASC-line-L2.txt", encoding="utf-8").read()
for tag, old, new in reps:
    assert L.count(old) == 1, (tag, L.count(old)); L = L.replace(old, new)
    print(tag, "old once, applied")
h = hashlib.sha1(L.encode()).hexdigest(); print("sha1", h, len(L.encode()), "bytes")
assert h == "0012d6710983ec339be8f5d4e051a205cc9207ba"
assert L.count("\n") == 1 and L.endswith("\n") and "|" not in L and L.count("(") == L.count(")") == 122
open("docs/new/P-N5-ASC-line-L3.txt", "w", encoding="utf-8").write(L)
