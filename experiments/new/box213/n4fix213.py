#!/usr/bin/env python3
"""Box 213 N-4 (REFEREE-2 40, claude/referee-2 8e075239, R2-box212-preread.md §9; Lead 03:57Z): the notebook's «187 notbest moves on 12
genomes» is wrong. This script reads experiments/new/box213/out/arena213_frozen.out, prints the true per-genome list, and (with --apply)
replaces the two wrong passages in notes/L-NEW.md (the BOX 213 section and the dead-end entry) by text generated from the file.
Usage (repository root): python3 experiments/new/box213/n4fix213.py [--apply]"""
import sys, re
F = "experiments/new/box213/out/arena213_frozen.out"; NB = "notes/L-NEW.md"
rows = []
for line in open(F):
    t = line.split()
    if len(t) < 3 or "notbest" not in t: continue
    d = dict(zip(t[1::2], map(int, t[2::2]))); rows.append((t[0][:-5] if t[0].endswith(".json") else t[0], d))
pos = sorted(((n, d["notbest"]) for n, d in rows if d["notbest"] > 0), key=lambda r: (-r[1], r[0]))
tot = sum(d["notbest"] for _, d in rows); mv = sum(d["moved"] for _, d in rows)
lst = ", ".join("%s %d" % r for r in pos)
txt = ("notbest %d of %d moves on %d of %d genomes (from %s by n4fix213.py; CORRECTED per REFEREE-2 40 N-4, Lead 03:57Z; the earlier «on 12 "
       "genomes» list summed to 84): %s" % (tot, mv, len(pos), len(rows), F, lst))
print(txt)
assert tot == 187 and mv == 6107, (tot, mv)
if "--apply" in sys.argv:
    s = open(NB).read()
    a = re.compile(r"notbest 187 on 12 genomes \(W86_n77 16,.*?CFI3_n48 1\)", re.S)
    b = re.compile(r"187 of 6,107 mover moves go to a non-best gate, on 12 genomes \(W86_n77 16,.*?CFI3_n48 1\)", re.S)
    assert len(a.findall(s)) == 1 and len(b.findall(s)) == 1
    s = a.sub(lambda m: txt, s); s = b.sub(lambda m: "a non-best gate: " + txt, s)
    open(NB, "w").write(s); print("applied to", NB)
