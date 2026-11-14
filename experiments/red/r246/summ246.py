#!/usr/bin/env python3
"""L-RED 71 R246: tables for docs/red/R246-scheme-tie.md, computed from out/*.out (nothing typed by hand).
Usage: summ246.py   (run in experiments/red/r246; prints markdown)"""
import re, os, glob
HERE = os.path.dirname(os.path.abspath(__file__))
def rows(fn, tag):
    out = []
    p = os.path.join(HERE, "out", fn)
    if not os.path.exists(p): return out
    for line in open(p):
        if not line.startswith(tag): continue
        t = line.split(); d = {"name": t[1]}
        for i in range(2, len(t) - 1):
            if re.fullmatch(r"-?\d+", t[i + 1]) and not re.fullmatch(r"-?\d+", t[i]): d[t[i]] = int(t[i + 1])
            elif t[i] in ("eng", "mode", "emode", "seed", "end"): d[t[i]] = t[i + 1]
        out.append(d)
    return out
kof = lambda name: int(re.search(r"G_(\d+)_", name).group(1))
cs = rows("census_s.out", "TIE246") + rows("k10.out", "TIE246"); cv = rows("census_v.out", "TIE246")
def pick(L, kind, mode): return {kof(r["name"]): r for r in L if kind in r["name"] and r["mode"] == mode}
print("### Table A: tie census of N5 (mode spec) on Gamma3(G_k), R104's priorities (file pg/G_k_r104.pg = L-RED-B's G_k_g3.pg)")
print("| k | n | iterations | fallbacks | choice | S4a ties met | at movers | path / cycle | iterations with a tie | most ties in one iteration | refuse | refuse_strict | S4b steps / ties | fallback ties | engine v equal |")
print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
A = pick(cs, "r104", "spec"); Av = pick(cv, "r104", "spec")
keys = ("its", "fb", "a_steps", "choice", "tie", "ptie", "ctie", "tie_mov", "tie_its", "tie_max", "refuse", "refuse_strict", "b_steps", "bchoice", "btie", "fbtie", "opt_bad")
for k in sorted(A):
    r = A[k]; eq = ("yes" if all(Av[k][x] == r[x] for x in keys) else "NO") if k in Av else "not run"
    print(f"| {k} | {r['n']} | {r['its']} | {r['fb']} | {r['choice']} | {r['tie']} | {r['tie_mov']} | {r['ptie']} / {r['ctie']} | {r['tie_its']} | {r['tie_max']} | {r['refuse']} | {r['refuse_strict']} | {r['b_steps']} / {r['btie']} | {r['fbtie']} | {eq} |")
for mode in ("spec", "xi"):
    print(f"\n### Table B ({mode}): the scheme on Gamma3^top(G_k), mode {mode} (file pg/G_k_top.pg)")
    print("| k | n | iterations | 2^k + 2 | fallbacks | choice | S4a ties met | path / cycle | refuse | refuse_strict | S4b steps / ties | fallback ties | opt_bad | engine v equal |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    B = pick(cs, "top", mode); Bv = pick(cv, "top", mode)
    for k in sorted(B):
        r = B[k]; eq = ("yes" if all(Bv[k][x] == r[x] for x in keys) else "NO") if k in Bv else "not run"
        print(f"| {k} | {r['n']} | {r['its']} | {2 ** k + 2} | {r['fb']} | {r['choice']} | {r['tie']} | {r['ptie']} / {r['ctie']} | {r['refuse']} | {r['refuse_strict']} | {r['b_steps']} / {r['btie']} | {r['fbtie']} | {r['opt_bad']} | {eq} |")
print("\n### Table C: third engine (L-COMP n5b --mode spec), iterations / fallbacks")
for fn in ("n5b.out", "k10.out"):
    p = os.path.join(HERE, "out", fn)
    if os.path.exists(p):
        for line in open(p):
            if line.startswith("N5B"): print("- " + line.strip())
print("\n### Table D: winners against Oink (zchk246)")
for r in rows("zchk.out", "ZCHK246"): print(f"- {r['name']} mode {r['mode']}: its {r['its']} wrong_zlk {r['wrong_zlk']} wrong_tl {r['wrong_tl']}")
print("\n### Table E: mover states against the IDEAL key run (trace246)")
for line in open(os.path.join(HERE, "out", "trace.out")) if os.path.exists(os.path.join(HERE, "out", "trace.out")) else []:
    if line.startswith("TRACE246 G_"):
        t = line.split(); d = dict(zip(t[2::2], t[3::2])); m = re.search(r"fb_at (\[[^\]]*\]) F (\d+) nonmover (\d+) L (\d+) end (\w+) ideal_mism (\d+) model_avail2_sum (\d+)", line)
        print(f"- {t[1]} emode {d['emode']} mode {d['mode']}: its {d['its']} fb_at {m.group(1)} F {m.group(2)} nonmover {m.group(3)} L {m.group(4)} end {m.group(5)} ideal_mism {m.group(6)} model_avail2_sum {m.group(7)}")
print("\n### Table F: Lemma TOP on other genomes (rand246)")
tot = {}
for line in open(os.path.join(HERE, "out", "rand.out")) if os.path.exists(os.path.join(HERE, "out", "rand.out")) else []:
    if line.startswith("RAND246"):
        print("- " + line.strip()); t = line.split(); d = dict(zip(t[1::2], t[2::2]))
        g = "ctrl" + d["ctrl"]
        for x in ("genomes", "sumL", "mism", "earlyfb", "tie_pre", "tie_post", "xidiff", "r104tie", "r104mism"): tot.setdefault(g, {}).setdefault(x, 0); tot[g][x] += int(d[x])
for g in sorted(tot): print(f"- TOTAL {g}: " + " ".join(f"{k} {v}" for k, v in tot[g].items()))
print("\n### Table G: control of the tie counter (TIE246_CTRL=1: P-sets ignored)")
for r in rows("ctrl.out", "TIE246"): print(f"- {r['name']} ctrl 1: tie {r['tie']} (path {r['ptie']}), refuse {r['refuse']}, refuse_strict {r['refuse_strict']}")
