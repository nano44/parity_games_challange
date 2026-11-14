#!/usr/bin/env python3
"""Box 208 (L-NEW successor 72): the DATA table of docs/new/N5-LEVEL-box208.md §7, built from out/*.out (no number typed by hand).
Per set: rows (genomes / samples), the sum of every must-0 counter (MUST0 of level208.py), and maxima or sums of the descriptive ones.
Usage: summ208.py   (run from experiments/new/box208)"""
import os, re, glob
MUST0 = ("monofail", "k3fail", "k4fail", "k5fail", "einF", "l3fail", "phifail", "stallnocyc", "nofvs", "rstall", "boundfail",
         "winstall", "wbeta", "wl3fail", "wmid", "wbound")
def kv(line):
    t = line.split(); d = {}
    for i in range(len(t) - 1):
        if re.fullmatch(r"-?\d+", t[i + 1]) and re.fullmatch(r"[A-Za-z_0-9+\-]+", t[i]) and not re.fullmatch(r"-?\d+", t[i]): d.setdefault(t[i], []).append(int(t[i + 1]))
    return d
def per_genome(fn):
    rows = [kv(l) for l in open(fn) if " monofail " in l]
    m0 = sum(sum(r.get(k, [0])) for r in rows for k in MUST0)
    g = lambda k, f: f(r[k][0] for r in rows if k in r)
    ks = sorted(set(r["k"][0] for r in rows))
    return len(rows), m0, dict(T=g("T", max), levels=g("levels", max), phivals=g("phivals", max), stalls=g("stalls", sum), stallloud=g("stallloud", sum),
                               plat=g("plat", sum), platmax=g("platmax", max), windows=g("windows", sum), wmax=g("wmax", max)), ks
def totals(fn):
    out = []
    for l in open(fn):
        if "TOTALS" not in l: continue
        d = kv(l); head = l.split("TOTALS")[0].split()
        m0 = sum(sum(d.get(k, [0])) for k in MUST0)
        n = d.get("genomes", d.get("samples", [0]))[0]
        out.append((" ".join(head[:6]), n, m0, {k: d[k][-1] for k in ("T", "levels", "phivals", "platmax", "wmax") if k in d}, {k: d[k][0] for k in ("stalls", "stallloud", "plat", "windows", "k0", "k1", "k2-3", "k4+") if k in d}))
    return out
print("| set (file in out/) | rows | sum of the 16 must-0 counters | descriptive |")
print("| --- | --- | --- | --- |")
for fn in ("level208_records.out", "level208_corpus.out", "level208_g3_records.out"):
    if not os.path.exists("out/" + fn): continue
    n, m0, d, ks = per_genome("out/" + fn)
    print("| %s | %d genomes, k in {%s} | %d | max T %d, max levels %d, max Phi values %d, stalls %d (loud %d), plateaus %d (longest %d), intervals %d (longest loud prefix %d) |"
          % (fn, n, ", ".join(str(k) for k in ks), m0, d["T"], d["levels"], d["phivals"], d["stalls"], d["stallloud"], d["plat"], d["platmax"], d["windows"], d["wmax"]))
for fn in sorted(glob.glob("out/level208_rand_*.out")) + sorted(glob.glob("out/level208_g3_rand_*.out")) + sorted(glob.glob("out/mut208_*.out")):
    for head, n, m0, mx, tt in totals(fn):
        print("| %s | %d | %d | %s; %s |" % (os.path.basename(fn), n, m0, ", ".join("max %s %d" % kv_ for kv_ in mx.items()), ", ".join("%s %d" % kv_ for kv_ in tt.items())))
for fn in sorted(glob.glob("out/level208_ctrl*.out")):
    for l in open(fn):
        d = kv(l); fired = [k for k in MUST0 if sum(d.get(k, [0])) > 0]
        name = l.split()[0] if "TOTALS" not in l else "rand k1 seed %d (%d genomes)" % (d["seed"][0], d["genomes"][0])
        print("| CONTROL %s: %s | 1 | fires: %s | |" % (os.path.basename(fn), name, ", ".join("%s %d" % (k, sum(d[k])) for k in fired) or "NOTHING"))
# second engine (run208b.sh H): L-RED's own.py through level208.py --hist; T compared with this lane's engine, genome by genome
rowsO = []
for mine, theirs in (("level208_records.out", "own208_records.out"), ("level208_corpus.out", "own208_corpus.out")):
    if not os.path.exists("out/" + theirs): continue
    n, m0, d, ks = per_genome("out/" + theirs)
    Tm = {l.split()[0]: kv(l)["T"][0] for l in open("out/" + mine) if " monofail " in l}
    To = {l.split()[0]: kv(l)["T"][0] for l in open("out/" + theirs) if " monofail " in l}
    diff = sorted(g for g in To if g in Tm and To[g] != Tm[g])
    rowsO.append("| %s | %d genomes | %d | max T %d, stalls %d (loud %d), plateaus %d (longest %d), intervals %d (longest loud prefix %d); T differs from this lane's engine on %d genomes%s |"
                 % (theirs, n, m0, d["T"], d["stalls"], d["stallloud"], d["plat"], d["platmax"], d["windows"], d["wmax"], len(diff), (" (" + ", ".join(diff[:6]) + ")") if diff else ""))
if rowsO:
    print("@@O@@")
    print("| set (file in out/) | rows | sum of the 16 must-0 counters | descriptive |")
    print("| --- | --- | --- | --- |")
    for r in rowsO: print(r)
# Addendum A: plat208.py outputs (one summary row per file)
PK = ("p1", "pclos", "p2", "p3", "p4", "p5")
rowsA = []
for fn in sorted(glob.glob("out/plat208_*.out")):
    tot = {k: 0 for k in PK}; plats = 0; mlen = 0; mpct = 0; n = 0; ctrl = 0
    for l in open(fn):
        if not l.startswith("plat"): continue
        d = kv(l); n += d.get("genomes", d.get("samples", [1]))[0]; ctrl = d["ctrl"][0]
        for k in PK: tot[k] += d[k][0]
        plats += d["plateaus"][0]; mlen = max(mlen, d["maxlen"][0]); mpct = max(mpct, d["maxpct"][0])
    rowsA.append("| %s | %d | %s | plateaus %d, longest %d steps, largest 100·(v − u)/(movers of Y + 1) = %d |" % (os.path.basename(fn), n,
                 ("CONTROL fires: " + ", ".join("%s %d" % (k, tot[k]) for k in PK if tot[k])) if ctrl else str(sum(tot.values())), plats, mlen, mpct))
if rowsA:
    print("@@A@@")
    print("| set (file in out/) | genomes | sum of p1, pclos, p2, p3, p4, p5 | descriptive |")
    print("| --- | --- | --- | --- |")
    for r in rowsA: print(r)
