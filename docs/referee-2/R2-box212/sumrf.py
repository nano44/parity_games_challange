#!/usr/bin/env python3
"""REFEREE-2 40: sum the TOTAL lines of r2rf.py outputs per configuration directory (out/<cfg>/*.out). Prints per cfg: files, files
with a TOTAL line, timeouts / errors (exit ≠ 0), runs, rule-free FAILS sum, and chosen descriptive records (max for *max / rec_W /
rec_tail_max / rec_nsp_max, else sum). Usage: sumrf.py OUTDIR"""
import sys, os, glob, re
MAXK = lambda k: k.endswith("max") or k in ("rec_Wmax", "rec_tail_max", "rec_nsp_max", "rec_Tmax", "rec_platmax", "rec_plat_len_max")
SHOW = ["rec_Tmax", "rec_Wmax", "rec_nsp_max", "rec_platexit", "rec_restrict_steps", "rec_restrict_idle", "rec_restrict_diff", "rec_tail_gt_N",
        "rec_how_k5fail", "rec_how_domfail", "rec_how_p3fail", "rec_how_p6fail", "rec_how_p7fail", "rec_how_l4mapfail", "rec_how_quietnfail", "rec_how_c4fail"]
for d in sorted(glob.glob(os.path.join(sys.argv[1], "*"))):
    files = sorted(glob.glob(d + "/*.out")); tot = {}; nt = 0; bad = []; fails = 0; runs = 0; nonzero = {}
    for f in files:
        txt = open(f).read(); m = re.search(r"^exit (\d+)", txt, re.M)
        if m and m.group(1) != "0": bad.append((os.path.basename(f), m.group(1)))
        tl = [l for l in txt.splitlines() if l.startswith("TOTAL")]
        if not tl: continue
        nt += 1; l = tl[-1]
        fails += int(re.search(r"FAILS (\d+)", l).group(1)); runs += int(re.search(r"runs (\d+)", l).group(1))
        head = l.split("|")[1].split()
        for k, v in zip(head[::2], head[1::2]):
            if int(v): nonzero[k] = nonzero.get(k, 0) + int(v)
        for k, v in re.findall(r"(rec_\w+|capped) (\d+)", l):
            v = int(v); tot[k] = max(tot.get(k, 0), v) if MAXK(k) else tot.get(k, 0) + v
    print(f"{os.path.basename(d)}: files {len(files)} with_TOTAL {nt} runs {runs} capped {tot.get('capped', 0)} rulefree_FAILS {fails}"
          + (f" nonzero {nonzero}" if nonzero else "") + (f" exit!=0 {bad}" if bad else "") + " | " + " ".join(f"{k[4:]} {tot.get(k, 0)}" for k in SHOW))
