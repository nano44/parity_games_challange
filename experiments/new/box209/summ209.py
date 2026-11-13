#!/usr/bin/env python3
"""Box 209 (L-NEW successor 72): the DATA tables of docs/new/N5-LEVEL3-box209.md §6, built from out/*.out (no number typed by hand).
Table 1: level208.py's 16 must-0 counters on Gamma3 histories (engine n5v = N5'-xi's own run; or L-RED 65's HOW3 engine, files own3_*).
Table 2: plat209.py's must-0 counters p1, pclos, p2, p3, p4, p5, t1, t2, t3. Controls are listed with what fires.
Usage: summ209.py   (run from experiments/new/box209)"""
import os, re, glob
MUST0 = ("monofail", "k3fail", "k4fail", "k5fail", "einF", "l3fail", "phifail", "stallnocyc", "nofvs", "rstall", "boundfail",
         "winstall", "wbeta", "wl3fail", "wmid", "wbound")
PK = ("p1", "pclos", "p2", "p3", "p4", "p5", "t1", "t2", "t3")
def kv(line):
    t = line.split(); d = {}
    for i in range(len(t) - 1):
        if re.fullmatch(r"-?\d+", t[i + 1]) and re.fullmatch(r"[A-Za-z_0-9+\-]+", t[i]) and not re.fullmatch(r"-?\d+", t[i]): d.setdefault(t[i], []).append(int(t[i + 1]))
    return d
def per_genome(fn):
    rows = [kv(l) for l in open(fn) if " monofail " in l and "TOTALS" not in l]
    m0 = sum(sum(r.get(k, [0])) for r in rows for k in MUST0)
    g = lambda k, f: f(r[k][0] for r in rows if k in r)
    return len(rows), m0, dict(T=g("T", max), levels=g("levels", max), phivals=g("phivals", max), stalls=g("stalls", sum), stallloud=g("stallloud", sum),
                               plat=g("plat", sum), platmax=g("platmax", max), windows=g("windows", sum), wmax=g("wmax", max)), sorted(set(r["k"][0] for r in rows))
def Ts(fn): return {l.split()[0].replace(".hist", ""): kv(l)["T"][0] for l in open(fn) if " monofail " in l and "TOTALS" not in l}
print("| set (file in out/) | engine | rows | sum of the 16 must-0 counters | descriptive |")
print("| --- | --- | --- | --- | --- |")
for fn, eng in (("level3_records.out", "n5v"), ("level3_corpus.out", "n5v"), ("level3_dead.out", "n5v"),
                ("own3_level_records.out", "L-RED how3"), ("own3_level_corpus.out", "L-RED how3"), ("own3_level_dead.out", "L-RED how3")):
    if not os.path.exists("out/" + fn): continue
    n, m0, d, ks = per_genome("out/" + fn); extra = ""
    if fn.startswith("own3_"):
        mine = Ts("out/" + fn.replace("own3_level_", "level3_")); theirs = Ts("out/" + fn); diff = sorted(g for g in theirs if g in mine and theirs[g] != mine[g])
        extra = "; T3 differs from the n5v run on %d of %d genomes%s" % (len(diff), len([g for g in theirs if g in mine]), (" (" + ", ".join(diff[:8]) + ")") if diff else "")
    print("| %s | %s | %d genomes, k in {%s} | %d | max T3 %d, max levels %d, max Phi values %d, stalls %d (loud %d), plateaus %d (longest %d), intervals %d (longest loud prefix %d)%s |"
          % (fn, eng, n, ", ".join(str(k) for k in ks), m0, d["T"], d["levels"], d["phivals"], d["stalls"], d["stallloud"], d["plat"], d["platmax"], d["windows"], d["wmax"], extra))
for fn in sorted(glob.glob("out/level3_rand_*.out")):
    for l in open(fn):
        if "TOTALS" not in l: continue
        d = kv(l); m0 = sum(sum(d.get(k, [0])) for k in MUST0)
        print("| %s | n5v | %d | %d | %s; %s |" % (os.path.basename(fn), d.get("genomes", d.get("samples", [0]))[0], m0,
              ", ".join("max %s %d" % (k, d[k][-1]) for k in ("T", "levels", "phivals", "platmax", "wmax") if k in d),
              ", ".join("%s %d" % (k, d[k][0]) for k in ("stalls", "stallloud", "plat", "windows") if k in d)))
for fn in sorted(glob.glob("out/level3_ctrl*.out")):
    for l in open(fn):
        if " monofail " not in l: continue
        d = kv(l); fired = [k for k in MUST0 if sum(d.get(k, [0])) > 0]
        print("| CONTROL %s: %s | n5v | 1 | fires: %s | |" % (os.path.basename(fn), l.split()[0], ", ".join("%s %d" % (k, sum(d[k])) for k in fired) or "NOTHING"))
print("@@P@@")
print("| set (file in out/) | engine | genomes | sum of p1, pclos, p2, p3, p4, p5, t1, t2, t3 | descriptive |")
print("| --- | --- | --- | --- | --- |")
for fn in sorted(glob.glob("out/plat3_*.out")) + sorted(glob.glob("out/own3_plat_*.out")):
    tot = {k: 0 for k in PK}; plats = 0; mlen = 0; mpct = 0; n = 0; ctrl = 0; tail = 0; T = 0
    for l in open(fn):
        if not l.startswith("plat3"): continue
        d = kv(l); n += d.get("genomes", d.get("samples", [1]))[0]; ctrl = d["ctrl"][0]
        for k in PK: tot[k] += d[k][0]
        plats += d["plateaus"][0]; mlen = max(mlen, d["maxlen"][0]); mpct = max(mpct, d["maxpct"][0]); tail = max(tail, d["tail"][0]); T = max(T, d["T"][-1])
    print("| %s | %s | %d | %s | plateaus %d, longest %d steps, largest 100·(v − u)/(movers of Y + 1) = %d, longest tail %d, max T3 %d |" % (os.path.basename(fn),
          "L-RED how3" if "own3" in fn else "n5v", n, ("CONTROL fires: " + (", ".join("%s %d" % (k, tot[k]) for k in PK if tot[k]) or "NOTHING")) if ctrl else str(sum(tot.values())), plats, mlen, mpct, tail, T))
