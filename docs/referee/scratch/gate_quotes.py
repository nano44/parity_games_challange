#!/usr/bin/env python3
"""REFEREE s31: every «...» quote in P-N5-GATE line L-2, located in trunk docs/RESULTS.md (whole file and by entry).
Usage: gate_quotes.py L2.txt RESULTS.md. Quotes nested «a «b» c» are taken outermost; whitespace runs normalised to one space."""
import re, sys
line = open(sys.argv[1], encoding="utf-8").read()
res = open(sys.argv[2], encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s)
R = norm(res)
# entries by heading
heads = [(m.start(), m.group(1)) for m in re.finditer(r"^### (R\d+|DE\d+)", res, re.M)]
def entry_of(pos_raw):
    e = None
    for p, h in heads:
        if p <= pos_raw: e = h
    return e
# outermost quotes
qs, depth, start = [], 0, None
for i, ch in enumerate(line):
    if ch == "«":
        if depth == 0: start = i + 1
        depth += 1
    elif ch == "»":
        depth -= 1
        if depth == 0: qs.append(line[start:i])
print("quotes:", len(qs), "unbalanced depth at end:", depth)
for q in qs:
    nq = norm(q)
    n = R.count(nq)
    # locate raw position via regex tolerant of whitespace
    pat = re.escape(q).replace(r"\ ", r"\s+")
    ents = sorted({entry_of(m.start()) for m in re.finditer(pat, res)})
    print(f"[{n}] {','.join(e or '-' for e in ents) or 'NOT FOUND'} :: {q[:110]}")
