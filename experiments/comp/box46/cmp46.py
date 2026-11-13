#!/usr/bin/env python3
"""L-COMP box 46 item 1: my win46 rows (out/win46_{tower,records,dead,corpus}.out) against rfd212.py's rows (L-NEW, claude/l-new 5fa64fe6
box212: N5 spec on n5v), genome by genome. Compared tuple: (T_key, #windows, W_key, stalls, tail, #plateaus, longest plateau, Φ values).
From rfd212's line: T, plat + (1 if tail > 0), max(platmax, tail), stalls, tail, plat, platmax, phivals (its window count and W are not
printed; they are formed from its plateau and tail fields by the definitions of box 212 §5: windows = plateaus + the tail).
Usage: cmp46.py RFD_FILE ...   (lines «<genome> RFD_MODE spec ...»; other modes ignored)"""
import sys, os, re, glob
H = os.path.dirname(os.path.abspath(__file__))
f = lambda l, k: int(re.search(r"(?:^| )%s (-?\d+)" % k, l).group(1))
mine = {}
for fn in sorted(glob.glob(os.path.join(H, "out", "win46_*.out"))):
    for l in open(fn):
        if " must0 " in l: mine[l.split()[0]] = (os.path.basename(fn), l)
for rf in sys.argv[1:]:
    ref = {}
    for l in open(rf):
        z = l.split()
        if len(z) > 2 and z[1] == "RFD_MODE" and z[2] == "spec": ref[z[0]] = l
    both = sorted(set(ref) & set(mine)); diff = 0; tot = dict(T=0, st=0)
    for b in both:
        m = mine[b][1]; r = ref[b]
        a = (f(m, "Tkey"), f(m, "nwin"), f(m, "Wkey"), f(m, "stalls"), f(m, "tail_len"), f(m, "plateaus"), f(m, "platmax"), f(m, "phivals"))
        c = (f(r, "T"), f(r, "plat") + (f(r, "tail") > 0), max(f(r, "platmax"), f(r, "tail")), f(r, "stalls"), f(r, "tail"), f(r, "plat"), f(r, "platmax"), f(r, "phivals"))
        tot["T"] += a[0]; tot["st"] += a[3]
        if a != c: diff += 1; print("CMP46 DIFF %s (%s): mine %s, rfd212 %s" % (b, mine[b][0], a, c))
    rsum = sum(sum(int(v) for v in re.findall(r" (?:imp3|monofail|k3fail|k4fail|einF|l3fail|phifail|phivals3|p1|pclos|p3) (\d+)", ref[b])) for b in both)
    print("CMP46 %s: genomes in both %d (mine %d, rfd212 %d) | differing in (T_key, windows, W_key, stalls, tail, plateaus, platmax, Φ values) %d | my T_key sum %d, stalls %d | rfd212's rule-free counters on them sum %d | my must0 sum %d" % (
        os.path.basename(rf), len(both), len(mine), len(ref), diff, tot["T"], tot["st"], rsum, sum(f(mine[b][1], "must0") for b in both)))
