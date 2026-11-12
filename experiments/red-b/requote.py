#!/usr/bin/env python3
"""Re-quote check (L-RED-B): every «...» on a [Q] line of box 208 par. 1 and A1 must occur verbatim in the named landed
entry of trunk docs/RESULTS.md (the whole entry: its title line and its body up to the next "### "), or, for the two
packet-level quotes, in the landed packet text. Usage: requote.py <box208.md> <RESULTS.md> <repo root>. Prints one line
per quote: FOUND-IN-ENTRY / FOUND-ELSEWHERE (which entries) / NOT-FOUND, and a summary."""
import re, sys
box = open(sys.argv[1], encoding="utf-8").read().splitlines()
res = open(sys.argv[2], encoding="utf-8").read()
root = sys.argv[3]
# split RESULTS into entries
ents = {}
for m in re.finditer(r"^### (R\d+) .*?(?=^### |\Z)", res, re.M | re.S):
    ents[m.group(1)] = m.group(0)
def norm(s): return re.sub(r"\s+", " ", s)
nents = {k: norm(v) for k, v in ents.items()}
# join wrapped [Q] items: a [Q] item starts at a line beginning "- [Q]" and continues on following lines starting with two spaces
items = []; cur = None
for l in box:
    if l.startswith("- [Q]"):
        if cur: items.append(cur)
        cur = l
    elif cur is not None and l.startswith("  ") and not l.startswith("  -"):
        cur += " " + l.strip()
    else:
        if cur: items.append(cur)
        cur = None
if cur: items.append(cur)
tot = bad = 0
for it in items:
    m = re.match(r"- \[Q\] (R\d+)", it)
    ent = m.group(1) if m else None
    for q in re.findall(r"«([^»]*)»", it):
        parts = [p.strip() for p in q.split("…") if p.strip()]
        for p in parts:
            tot += 1; p2 = norm(p)
            if ent and p2 in nents.get(ent, ""): print("FOUND-IN-ENTRY", ent, "|", p2[:90])
            else:
                where = [k for k, v in nents.items() if p2 in v]
                if where: print("FOUND-ELSEWHERE", ent, "->", ",".join(where[:6]), "|", p2[:90])
                else: bad += 1; print("NOT-FOUND", ent, "|", p2[:120])
print("requote: [Q] items %d, quoted strings %d, not found in RESULTS %d" % (len(items), tot, bad))
