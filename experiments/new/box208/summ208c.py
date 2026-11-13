#!/usr/bin/env python3
"""Box 208 Addendum B (L-NEW successor 72): the DATA table of rv208.py's outputs (out/rv208_*.out), no number typed by hand.
Usage: summ208c.py   (run from experiments/new/box208)"""
import os, re, glob
MUST0 = ("CN2", "CN2pi", "BONLY", "NOTIE", "LOCGATE", "LOCK2", "F1", "DOM", "K1", "K2", "K3a", "K3b", "K3c", "K3d", "K3e", "K4", "K5",
         "L1sub", "L1stall", "L1rise", "L1stallempty", "L1lagback", "C4", "L2", "L3", "L3alpha_m", "L3beta_kind", "L3beta_m", "L5set",
         "L4mover", "L4gate_face", "L4gate", "L4beta", "L4nocycle", "L4shape", "L4xi", "L5m", "L5phi",
         "P1", "P2", "P3", "P4", "P4eq_face", "P4K2", "P5closed", "P5val", "P5howard", "P6", "P7")
SUM = ("genomes", "Tsum", "lagstates", "stalls", "nonstalls", "betaonly", "plateaus", "plat_gt_movers", "P4eq", "K2tested"); MAX = ("Tmax", "platmax", "platpct")
def kv(line):
    t = line.split(); return {t[i]: int(t[i + 1]) for i in range(len(t) - 1) if re.fullmatch(r"-?\d+", t[i + 1]) and re.fullmatch(r"[A-Za-z_0-9]+", t[i]) and not t[i].isdigit()}
print("| set (file in out/) | lines | genomes | sum of the 49 must-0 counters | VIOLATION lines | descriptive |")
print("| --- | --- | --- | --- | --- | --- |")
for fn in sorted(glob.glob("out/rv208_*.out")):
    if "xcheck" in fn:
        ls = [l for l in open(fn) if l.strip()]; ok = sum(1 for l in ls if l.rstrip().endswith("OK"))
        print("| %s | %d | %d | builder, run length, states and values equal to box191 idealcyc / si.Engine on %d of %d files | | max T %d |" % (
              os.path.basename(fn), len(ls), ok, ok, len(ls), max(kv(l).get("T", 0) for l in ls)))
        continue
    tot = {}; viol = 0; n = 0; fired = {}
    for l in open(fn):
        if "VIOLATION" in l: viol += 1; continue
        d = kv(l)
        if "genomes" not in d: continue
        n += 1
        for k in SUM: tot[k] = tot.get(k, 0) + d.get(k, 0)
        for k in MAX: tot[k] = max(tot.get(k, 0), d.get(k, 0))
        for k in MUST0:
            if d.get(k, 0): fired[k] = fired.get(k, 0) + d[k]
    ctrl = "ctrl" in fn
    print("| %s | %d | %d | %s | %d | max T %d, sum T %d, (b, t) pairs with a lagging vertex %d, stalls %d, non-stalls %d, case (β) only %d, plateaus %d (longest %d; longer than the movers of Y: %d), equal-class gates met %d, (K2) pairs %d |" % (
          os.path.basename(fn), n, tot["genomes"], ("CONTROL fires: " + (", ".join("%s %d" % kv_ for kv_ in sorted(fired.items())) or "NOTHING")) if ctrl else str(sum(fired.values())),
          viol, tot["Tmax"], tot["Tsum"], tot["lagstates"], tot["stalls"], tot["nonstalls"], tot["betaonly"], tot["plateaus"], tot["platmax"], tot["plat_gt_movers"], tot["P4eq"], tot["K2tested"]))
