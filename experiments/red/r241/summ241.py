#!/usr/bin/env python3
"""L-RED 69 R241: sums of the kt241 outputs (every number in docs/red/R241-keytau.md comes from this script's output, out/summ241.txt).
Groups of counters: TAU = KEY-TAU (i)-(iii) + premises; GATE = box 215 as stated (gate keys); EKEY = box 215 with e-index keys.
Usage: summ241.py OUTDIR"""
import sys, os, re, glob
TAU = ("std", "tau3", "w3", "lenvar", "kp", "kpf", "kpa", "unreach", "mukappa", "muinc", "muflat", "mulen", "kviol", "nomove")
GATE = ("eord", "kpg", "lkp", "pkf", "pkfa", "kflip", "kflipm", "casc", "ftt", "ladder")
EKEY = tuple(k + "_e" for k in GATE[1:])

def counters(part):
    return {k: int(v) for k, v in re.findall(r"(\w+) (\d+)", part)}

def grp(c, ks):
    s = sum(c.get(k, 0) for k in ks); nz = {k: c[k] for k in ks if c.get(k, 0)}
    return f"{s}" + (f" {nz}" if nz else "")

D = sys.argv[1]
print("== per-file runs (json; one row per genome)")
for f in sorted(glob.glob(os.path.join(D, "kt_*.out"))):
    if os.path.basename(f).startswith("kt_rand"): continue
    rows = [l for l in open(f) if l.startswith("KT241") and ": std" in l]; to = [l for l in open(f) if "TIMEOUT" in l]
    tot = {}; T = sw = cyc = xs = xd = 0; ekrows = 0
    for l in rows:
        c = counters(l.split(": ", 1)[1].split(" | ")[0])
        for k, v in c.items(): tot[k] = tot.get(k, 0) + v
        ekrows += int("kpg_e" in l)
        T += int(re.search(r"\| T (\d+)", l).group(1)); sw += int(re.search(r"switches (\d+)", l).group(1)); cyc += int(re.search(r"cycuse (\d+)", l).group(1))
        m = re.search(r"xdiff (\d+)", l)
        if m: xs += 1; xd += int(m.group(1))
    print(f"{os.path.basename(f)}: genomes {len(rows)} timeouts {len(to)} | TAU {grp(tot, TAU)} | GATE {grp(tot, GATE)} | EKEY {grp(tot, EKEY)} (rows with e-key counters {ekrows})"
          f" | sum T {T} switches {sw} cycuse {cyc} | n5v sampled {xs} xdiff {xd}")
print("== generated sets (kt_rand.out; one TOTAL row per set)")
G = 0; Tt = 0
for f in sorted(glob.glob(os.path.join(D, "kt_rand*.out"))):
    print(f"-- {os.path.basename(f)}")
    for l in open(f):
        if not l.startswith("#"): continue
        tag = l.split()[0]; c = counters(l.split("genomes", 1)[1].split(" | ")[0]); g = int(re.search(r"genomes (\d+)", l).group(1))
        T = int(re.search(r"\| T (\d+)", l).group(1)); xs, xd = map(int, re.search(r"sampled (\d+) xdiff (\d+)", l).groups())
        mT = int(re.search(r"max T (\d+)", l).group(1)); lad = int(re.search(r"ladders (\d+)", l).group(1))
        print(f"{tag}: genomes {g} | TAU {grp(c, TAU)} | GATE {grp(c, GATE)} | EKEY {grp(c, EKEY)} | sum T {T} max T {mT} ladders {lad} | n5v sampled {xs} xdiff {xd}")
        if not ("ctrl" in tag): G += g; Tt += T
print(f"generated sets without controls: genomes {G} sum T {Tt}")
