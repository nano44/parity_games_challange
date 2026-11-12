#!/usr/bin/env python3
"""Compare this engine's T_CYC with a list "file T" (one per line; inst/box208_*_T.txt are the T columns of
claude/l-new 8db300fe experiments/new/box208/out/level208_records.out and level208_corpus.out, read as data).
Usage: cmpT.py <list> <file>...   (files matched to the list by basename). DATA only."""
import sys, os, time
import eng
lst = sys.argv[1]; files = {os.path.basename(f): f for f in sys.argv[2:]}
bad = 0; tot = 0
for line in open(lst):
    name, T = line.split(); T = int(T)
    p = files.get(name)
    if p is None: print("missing", name); bad += 1; continue
    g = eng.build(eng.load(p)); h = eng.howard_run(g)
    tot += 1; ok = (len(h) - 1 == T); bad += (not ok)
    print(name, "N", g.N, "M", g.M, "T_mine", len(h) - 1, "T_listed", T, "OK" if ok else "DIFF", flush=True)
print("cmpT: files", tot, "differences", bad)
