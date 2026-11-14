#!/usr/bin/env python3
"""Box 210 (L-NEW successor 72): the DATA tables of docs/new/N5-GENLEVEL-box210.md §5, built from out/*.out (no number typed by hand).
Usage: summ210.py   (run from experiments/new/box210)"""
import os, re
MUST0 = ("F1", "K1", "K3", "K4", "K5", "L1", "L3", "L3m", "L4", "L4c", "L5", "P1", "P2", "P3", "P4w")
def kv(line):
    t = line.split(); return {t[i]: int(t[i + 1]) for i in range(len(t) - 1) if re.fullmatch(r"-?\d+", t[i + 1]) and re.fullmatch(r"[A-Za-z_][A-Za-z_0-9]*", t[i])}
print("| game (out/gen210_families.out) | n (split) | H | sum of the 15 must-0 counters | T | non-stall steps | stalls | plateaus (longest) | tail | Odd flips inside Y on plateaus | Odd flips at steps with no class change |")
print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for l in open("out/gen210_families.out"):
    if not l.startswith("gen210 pg"): continue
    d = kv(l); print("| %s | %d | %d | %d | %d | %d | %d | %d (%d) | %d | %d | %d |" % (l.split()[2], d["n"], d["Hsize"], sum(d[k] for k in MUST0), d["Tmax"], d["nonstalls"], d["stalls"], d["plateaus"], d["platmax"], d["tailmax"], d["oddflipY"], d["oddflipQ"]))
print("@@R@@")
print("| set | games | sum of the 15 must-0 counters | descriptive |")
print("| --- | --- | --- | --- |")
for fn in ("out/gen210_rand.out", "out/gen210_ctrl.out"):
    for l in open(fn):
        if not l.startswith("gen210 rand"): continue
        d = kv(l); t = l.split(); ctrl = d["ctrl"]; fired = ", ".join("%s %d" % (k, d[k]) for k in MUST0 if d[k])
        name = "seed %d: %d vertices, priorities 1..%d, out-degree 1..%d, top priority %s, H %s" % (d["seed"], d["n0"], d["d"], d["deg"], "even" if d["evtop"] else "odd", t[t.index("H") + 1])
        print("| %s%s | %d | %s | max T %d, sum T %d, vertices of H %d, non-stall steps %d, stalls %d, plateaus %d (longest %d), longest tail %d, Odd flips inside Y %d, at class-quiet steps %d, capped %d |" % (
              ("CONTROL GEN_CTRL=%d, " % ctrl) if ctrl else "", name, d["games"], ("fires: " + (fired or "NOTHING")) if ctrl else str(sum(d[k] for k in MUST0)),
              d["Tmax"], d["Tsum"], d["Hsize"], d["nonstalls"], d["stalls"], d["plateaus"], d["platmax"], d["tailmax"], d["oddflipY"], d["oddflipQ"], d["capped"]))
print("@@B@@")
print("| run (every reference state b; counts add up over b) | games | sum of the 15 must-0 counters | descriptive |")
print("| --- | --- | --- | --- |")
for l in list(open("out/gen210_allb.out")) + list(open("out/climb210.out")):
    d = kv(l); t = l.split()
    if l.startswith("gen210 pg"): name = t[2]
    elif l.startswith("gen210 rand"): name = "random, seed %d: %d vertices, priorities 1..%d, out-degree 1..%d, top priority even" % (d["seed"], d["n0"], d["d"], d["deg"])
    elif l.startswith("climb210"): name = "hill-climb, seed %d, %d games visited, %d vertices, priorities 1..%d (longest run found: T %d)%s" % (d["seed"], d["iters"], d["n0"], d["d"], d["bestT"], "" if d["seed"] == 2121 else "; b = T only")
    else: continue
    print("| %s | %d | %d | max T %d, non-stall (b, t) pairs %d, stalls %d, plateaus %d (longest %d), longest tail %d, Odd flips inside Y %d |" % (name, d["games"], sum(d[k] for k in MUST0), d["Tmax"], d["nonstalls"], d["stalls"], d["plateaus"], d["platmax"], d["tailmax"], d["oddflipY"]))
print("@@N@@")
print("| N5 run (out/n5lev210.out) | games | iterations (max, sum) | fallbacks | K1 + K3 + K4 + L1 + L3 + L3m | K5 | L4 | L4c | P3 | stalls |")
print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for l in open("out/n5lev210.out"):
    if not l.startswith("n5lev"): continue
    d = kv(l); t = l.split(); name = t[2] if t[1] == "pg" else "random, seed %d: %d vertices, priorities 1..%d" % (d["seed"], d["n0"], d["d"])
    print("| %s | %d | %d, %d | %d | %d | %d | %d | %d | %d | %d |" % (name, d["games"], d["Tmax"], d["Tsum"], d["fallbacks"], sum(d[k] for k in ("K1", "K3", "K4", "L1", "L3", "L3m")), d["K5"], d["L4"], d["L4c"], d["P3"], d["stalls"]))
ls = [l for l in open("out/gen210_xcheck.out") if l.strip()]
print("@@X@@"); print("xcheck: %d of %d files OK (values of every vertex at every state equal to si.Engine's on the split game)" % (sum(1 for l in ls if l.rstrip().endswith("OK")), len(ls)))
print("@@S@@")
for l in open("out/scale210.out"):
    t = l.split(); print("- %s (T %s, Λ-loud %s): %s" % (t[1], t[3], t[5], " ".join(t[7:])))
