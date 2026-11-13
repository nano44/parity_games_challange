#!/usr/bin/env python3
"""Box 212 Addendum A (L-NEW successor 74): kill criterion (iii) of the approved BOX 212 text («if on every Ξ-cyclic genome of the sets
λ*_key ≥ F/2, the reduction carries no information»), evaluated on the frozen rfd212 lines (out/rfd212_frozen.out, RFD_MODE spec = N5
itself on Γ3 up to its first fallback, reference T). Per genome: k = fvs202.kfvs's Ξ-feedback number (k = 0: Ξ-acyclic, skipped),
T = T_key (steps before the first fallback; F is T_key plus a constant), λ*_key = max(longest plateau, tail). Prints one line per
Ξ-cyclic genome and a summary line. Run from experiments/new/box212."""
import sys, os, re, json, glob
sys.path.insert(0, "../box208"); import level208, fvs202
rows = {}
for l in open("out/rfd212_frozen.out"):
    t = l.split()
    if "RFD_MODE" not in t or t[t.index("RFD_MODE") + 1] != "spec": continue
    rows[t[0]] = {t[i]: int(t[i + 1]) for i in range(len(t) - 1) if re.fullmatch(r"-?\d+", t[i + 1])}
paths = {}
for f in sorted(glob.glob("../box20*/inst/*.json") + glob.glob("../box202/*.json") + glob.glob("../box191/inst/*.json")):
    paths.setdefault(os.path.basename(f), f)
n = half = big = bighalf = 0; lmax = 0; tmax_half = 0; tmax = 0
for g, d in sorted(rows.items()):
    G = json.load(open(paths[g])); G = G.get("genome", G); k = fvs202.kfvs(G)[0]
    if k == 0: continue
    lam, T = max(d["maxlen"], d["tail"]), d["T"]; h = lam >= T / 2
    n += 1; half += h; lmax = max(lam, lmax); tmax = max(tmax, T)
    if h: tmax_half = max(tmax_half, T)
    if T >= 10: big += 1; bighalf += h
    print(g, "k", k, "T", T, "lam", lam, "lam>=T/2", int(h))
print(f"Xi-cyclic {n} of {len(rows)}; lam*_key >= T/2 on {half} (largest T among them {tmax_half}); lam*_key < T/2 on {n - half}; "
      f"T >= 10 on {big}, of which lam*_key >= T/2 on {bighalf}; largest lam*_key {lmax}; largest T {tmax}; kill (iii) fires: {int(half == n)}")
