#!/usr/bin/env python3
"""Box 212 (L-NEW successor 74): summary of the DATA outputs in out/ (run from experiments/new/box212). One table row per (set, rule):
units (runs, bchecked), the sum of every must-0 counter (rf212: IMP CAP CN2 CN2pi BONLY NOTIE LOCGATE LOCK2 F1 K1 K2 K3a K3b K3c K3d K3e K4
K5new L1sub L1stall L1rise L1stallempty L1lagback L2 L3 L3alpha_m L3beta_kind L3beta_m L5set L5phi NSP P1 P2 P4 P4K2 PHclosed PHval
PHimp PHout C4 DECOMP; rfd212: imp3 monofail k3fail k4fail einF l3fail phifail phivals3 p1 pclos p3), the descriptive maxima / sums, the
number of TIMEOUT lines (NOT checked), and the controls. Usage: python3 summ212.py"""
import glob, os, re, collections
M0 = ("IMP CAP CN2 CN2pi BONLY NOTIE LOCGATE LOCK2 F1 K1 K2 K3a K3b K3c K3d K3e K4 K5new L1sub L1stall L1rise L1stallempty L1lagback L2 L3 "
      "L3alpha_m L3beta_kind L3beta_m L5set L5phi NSP P1 P2 P4 P4K2 PHclosed PHval PHimp PHout C4 DECOMP").split()
M0D = "imp3 monofail k3fail k4fail einF l3fail phifail phivals3 p1 pclos p3".split()
MAXK = {"Tmax", "nsmax", "nspctP", "platmax", "tailmax", "T", "phivals", "maxlen", "tail"}
def kv(line):
    t = line.split(); d = {}
    for i in range(len(t) - 1):
        if re.fullmatch(r"[A-Za-z_0-9]+", t[i]) and re.fullmatch(r"-?\d+", t[i + 1]): d[t[i]] = int(t[i + 1])
    return d
def add(acc, d):
    for k, v in d.items(): acc[k] = max(acc[k], v) if k in MAXK else acc[k] + v
rows = collections.OrderedDict(); tmo = collections.Counter(); viol = collections.Counter()
for fn in sorted(glob.glob("out/rf212_*.out")) + sorted(glob.glob("out/rfd212_*.out")):
    if "ctrl" in fn: continue
    for line in open(fn):
        if line.startswith("VIOLATION"): viol[fn] += 1; continue
        if line.startswith("TIMEOUT"):
            r = line.split()[-1]; tmo[(os.path.basename(fn).split("_")[1], r)] += 1; continue
        m = re.search(r"\bRULE (\w+)", line) or re.search(r"\bRFD_MODE (\w+)", line)
        if not m: continue
        st = os.path.basename(fn).split("_")[1].replace(".out", "")
        key = (os.path.basename(fn).split("_")[0], st, m.group(1))
        rows.setdefault(key, collections.Counter()); add(rows[key], kv(line)); rows[key]["lines"] += 1
for (tool, st, r), c in rows.items():
    m0 = M0 if tool == "rf212" else M0D
    s0 = sum(c[k] for k in m0); hit = " ".join(f"{k} {c[k]}" for k in m0 if c[k])
    if tool == "rf212":
        d = f"runs {c['runs']} bchecked {c['bchecked']} Tmax {c['Tmax']} nsmax {c['nsmax']} nspctP {c['nspctP']} stalls {c['stalls']} plateaus {c['plateaus']} platmax {c['platmax']} plat_gt_movers {c['plat_gt_movers']} platidle {c['platidle']} platexit {c['platexit']} tailmax {c['tailmax']} tail_gt_N {c['tail_gt_N']} K5how {c['K5how']}"
    else:
        d = f"lines {c['lines']} T {c['T']} steps {c['steps']} phivals {c['phivals']} stalls {c['stalls']} plat {c['plat']} maxlen {c['maxlen']} tail {c['tail']} tail_gt_nE {c['tail_gt_nE']} k5fail {c['k5fail']} p2 {c['p2']} p4 {c['p4']} p5 {c['p5']}"
    print(f"{tool} {st} {r}: must0_sum {s0}{(' [' + hit + ']') if hit else ''} timeouts {tmo[(st, r)]} | {d}")
print("VIOLATION lines:", sum(viol.values()), dict(viol))
for fn in sorted(glob.glob("out/*ctrl*.out")):
    for line in open(fn):
        if line.strip(): print("ctrl", os.path.basename(fn), line.strip()[:300])
