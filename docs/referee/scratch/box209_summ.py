#!/usr/bin/env python3
"""REFEREE s33: summary of box209_logs/*.out (box209_replay.py outputs): one markdown row per set; numbers parsed, not read by eye.
usage: box209_summ.py [md]"""
import sys, os, re, glob
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "box209_logs"); rows = []; tot = 0; totg = 0; tots = 0
def kv(line):
    t = line.split(":", 1)[1].split(); return {t[i]: int(t[i + 1]) for i in range(0, len(t), 2)}
for f in sorted(glob.glob(os.path.join(d, "*.out"))):
    b = os.path.basename(f)
    if b in ("quotes.out", "mut.out", "summ.out") or b.startswith("lean_"): continue
    L = open(f).read().split("\n"); m = [l for l in L if l.startswith("MUST-0:")]; r = [l for l in L if l.startswith("RECORDS:")]
    if not m or not r: rows.append("| %s | NO SUMMARY (unfinished or failed) | | | | | | | | | |" % b); continue
    M, R = kv(m[0]), kv(r[0]); assert len(M) == 30, (b, len(M))
    ctrl = ", ".join("%s %s" % (k, format(R[k], ",")) for k in ("c_k4", "c_k5", "ch1", "ch2", "ch3", "ch4", "ch4c", "ch5", "c_Y", "c_l3v") if k in R)
    rows.append("| %s | %s | %s | %d | %d | %d | %d (longest %d) | %d | %d | %d / %d | %s |" % (b, format(R["genomes"], ","), format(R["states"], ","), R["maxT"], sum(M.values()),
                R["stalls"], R["plateaus"], R["maxplat"], R["maxtail"], R["n_p4case3"], R["n_alpha"], R["n_beta"], ctrl))
    tot += sum(M.values()); totg += R["genomes"]; tots += R["states"]
print("| log | genomes | states | max T3 | sum of the 30 must-0 counters | stalls (reference T3) | plateaus checked, three references | longest tail | (P4) case (3) gates | states with (α) / (β), three references | controls |")
print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for r in rows: print(r)
print("| all | %s | %s | | %d | | | | | | |" % (format(totg, ","), format(tots, ","), tot))
