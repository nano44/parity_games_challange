#!/usr/bin/env python3
"""REFEREE-2 successor 39: reads the lane's frozen DATA outputs of P-N5-LEVEL §11 (experiments/new/box208/out/ at claude/l-new
1e6df499, fetched by `git show` into DIR) BY COLUMN NAME, without the lane's summ208*.py, and prints per file: rows (genome lines or
mutant / random samples), the sum of the must-0 counters, and the descriptive maxima the packet's tables quote.
Usage: r2lvdata.py DIR"""
import sys, os, re, glob
D = sys.argv[1]
LV16 = "monofail k3fail k4fail k5fail einF l3fail phifail stallnocyc nofvs rstall boundfail winstall wbeta wl3fail wmid wbound".split()
PL6 = "p1 pclos p2 p3 p4 p5".split()
RV49 = ("CN2 CN2pi BONLY NOTIE LOCGATE LOCK2 F1 DOM K1 K2 K3a K3b K3c K3d K3e K4 K5 L1sub L1stall L1rise L1stallempty L1lagback C4 L2 L3 "
        "L3alpha_m L3beta_kind L3beta_m L5set L4mover L4gate_face L4gate L4beta L4nocycle L4shape L4xi L5m L5phi P1 P2 P3 P4 P4eq_face P4K2 "
        "P5closed P5val P5howard P6 P7").split()
assert len(LV16) == 16 and len(PL6) == 6 and len(RV49) == 49, (len(LV16), len(PL6), len(RV49))
def kv(s):
    t = s.split(); out = {}
    for i in range(len(t) - 1):
        if re.fullmatch(r"-?\d+", t[i + 1]) and not re.fullmatch(r"-?\d+", t[i]): out.setdefault(t[i], int(t[i + 1]))
    return out
for fn in sorted(glob.glob(os.path.join(D, "*.out"))):
    b = os.path.basename(fn); L = [l for l in open(fn, encoding="utf-8").read().split("\n") if l.strip()]
    if b.startswith(("level208", "own208", "mut208")):
        rows = 0; z = 0; mx = {}; sm = {}
        for l in L:
            if b.startswith("mut208") or l.startswith("rand "):
                if not (l.startswith("mut ") or l.startswith("rand ")): continue
                if l.startswith("rand "):
                    hd = kv(l.split("TOTALS")[0]); left = l.split("TOTALS", 1)[1]; d = kv(left.split("MAX")[0])
                    rows += hd.get("genomes", 0); z += sum(d.get(c, 0) for c in LV16)
                    for k in ("stalls", "stallloud", "plat", "windows"): sm[k] = sm.get(k, 0) + d.get(k, 0)
                    for k, v in kv(left.split("MAX", 1)[1]).items(): mx[k] = max(mx.get(k, v), v)
                    continue
                left = l.split("TOTALS", 1)[1]; d = kv(left); rows = kv(l.split("TOTALS")[0]).get("samples", 0)
                z = sum(d.get(c, 0) for c in LV16); mx = {k: d.get(k) for k in ("stalls", "stallloud", "plat", "windows")}
                mx.update({k: v for k, v in kv(left.split("MAX", 1)[1]).items()} if "MAX" in left else {})
                break
            if " ideal " in l or l.startswith("rand ") or " g3 " in l or re.match(r"^\S+\.json ", l):
                d = kv(l.split("|")[0]); e = kv(l.split("|")[1]) if "|" in l else {}
                if not any(c in d for c in LV16): continue
                rows += d.get("samples", 1) if l.startswith("rand ") else 1
                z += sum(d.get(c, 0) for c in LV16)
                for k, v in e.items():
                    if k in ("stalls", "stallloud", "plat", "windows"): sm[k] = sm.get(k, 0) + v
                    else: mx[k] = max(mx.get(k, v), v)
        fired = "" if "ctrl" not in b else " (control)"
        print(f"{b}: rows {rows} must0sum {z}{fired} | max " + " ".join(f"{k} {v}" for k, v in sorted(mx.items())) + " | sums " +
              " ".join(f"{k} {v}" for k, v in sorted(sm.items())))
    elif b.startswith("plat208"):
        rows = 0; z = 0; pl = 0; ml = 0; mp = 0
        for l in L:
            d = kv(l)
            if not any(c in d for c in PL6): continue
            rows += d.get("genomes", d.get("samples", 1)); z += sum(d.get(c, 0) for c in PL6); pl += d.get("plateaus", 0)
            ml = max(ml, d.get("maxlen", 0)); mp = max(mp, d.get("maxpct", 0))
        print(f"{b}: rows {rows} must0sum {z} | plateaus {pl} longest {ml} maxpct {mp}")
    elif b.startswith("rv208"):
        rows = 0; z = 0; viol = 0; agg = {}
        for l in L:
            if l.startswith("VIOLATION"): viol += 1; continue
            d = kv(l)
            if "genomes" not in d: continue
            rows += d["genomes"]; z += sum(d.get(c, 0) for c in RV49)
            for k, v in d.items():
                if k in RV49: continue
                agg[k] = max(agg.get(k, 0), v) if k in ("Tmax", "platmax", "maxmvals_pct", "platpct") else agg.get(k, 0) + v
        print(f"{b}: lines {len(L)} genomes {rows} must0sum {z} VIOLATION {viol} | " + " ".join(f"{k} {v}" for k, v in sorted(agg.items())))
