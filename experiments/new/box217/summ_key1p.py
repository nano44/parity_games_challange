#!/usr/bin/env python3
"""Packet P-N5-KEY1P: sums of the must-0 counters over the pinned outputs out/key1p_*.out (one line per file) for docs/new/P-N5-KEY1P.md
§10 and experiments/new/check.sh. A file without its last line DONE is reported MISSING. Run from experiments/new/box217."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(HERE, "out")
NAMES = ["ideq", "l0", "a1mu", "a1v", "a2", "a3", "a4h", "a4x", "mism", "nofb"]
FILES = ["key1p_towers_n5.out", "key1p_rec.out", "key1p_rec_n5.out", "key1p_mut.out", "key1p_mut_n5.out", "key1p_rand.out", "key1p_lift.out"]
tot_all = 0
for f in FILES:
    p = os.path.join(O, f)
    if not os.path.exists(p) or open(p).read().rstrip().split("\n")[-1] != "DONE": print(f"{f} MISSING"); continue
    gen = steps = 0; c = {n: 0 for n in NAMES}; has = set(); maxT = 0
    for l in open(p):
        if " | " not in l: continue
        head, tail = l.split(" | ", 1)
        m = re.search(r"\bgenomes (\d+)\b", head); gen += int(m.group(1)) if m else 1
        m = re.search(r"\bsumT (\d+)\b", head) or re.search(r"\bT (\d+)\b", head); steps += int(m.group(1))
        m = re.search(r"\bmaxT (\d+)\b", head) or re.search(r"\bT (\d+)\b", head); maxT = max(maxT, int(m.group(1)))
        for n in NAMES:
            m = re.search(rf"\b{n} (\d+)\b", tail)
            if m: c[n] += int(m.group(1)); has.add(n)
    s = sum(c.values()); tot_all += s
    print(f"{f} genomes {gen} steps {steps} maxT {maxT} must0_sum {s} " + " ".join(f"{n} {c[n]}" if n in has else f"{n} -" for n in NAMES))
print(f"all files must0_sum {tot_all}")
