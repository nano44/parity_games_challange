#!/usr/bin/env python3
"""REFEREE-2 40: own re-count of box 212 Addendum A (A3), kill criterion (iii), from the lane's frozen rfd212 lines (RFD_MODE spec,
read by column name from `git show COMMIT:experiments/new/box212/out/rfd212_frozen.out`) and MY OWN Ξ-feedback number (r2lv.xi_graph /
min_fvs, exhaustive to k = 3; successor 39's code, not fvs202). λ*_key := max(maxlen, tail) as the lane defines it (§6, kill212.py doc).
Usage: r2kill3.py COMMIT INSTDIR [--ctrl]   (--ctrl: λ* := T, so «λ* ≥ T/2» holds everywhere and kill (iii) must FIRE)."""
import sys, os, json, subprocess
H = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(os.environ.get("R2DIR", ""), d) for d in ("R2-P-N5-LEVEL", "R2-P-ACYC", "R2-P-N5-END", "R2-P-N5-SPLIT")]
import r2lv as L
com, inst = sys.argv[1], sys.argv[2]; ctrl = "--ctrl" in sys.argv
txt = subprocess.run(["git", "show", com + ":experiments/new/box212/out/rfd212_frozen.out"], capture_output=True, text=True, check=True).stdout
rows = {}
for l in txt.splitlines():
    t = l.split()
    if "RFD_MODE" in t and t[t.index("RFD_MODE") + 1] == "spec":
        d = {}
        for i in range(1, len(t) - 1):
            if t[i + 1].lstrip("-").isdigit() and not t[i].lstrip("-").isdigit(): d[t[i]] = int(t[i + 1])
        rows[t[0]] = d
n = half = big = bighalf = lmax = tmax = tmaxhalf = acyc = 0; ks = {}
for g in sorted(rows):
    d = rows[g]; G = json.load(open(os.path.join(inst, g))); G = G.get("genome", G)
    k, _ = L.min_fvs(L.xi_graph(G)); ks[k] = ks.get(k, 0) + 1
    if k == 0: acyc += 1; continue
    T = d["T"]; lam = T if ctrl else max(d["maxlen"], d["tail"]); h = lam >= T / 2
    n += 1; half += h; lmax = max(lmax, lam); tmax = max(tmax, T)
    if h: tmaxhalf = max(tmaxhalf, T)
    if T >= 10: big += 1; bighalf += h
print("own k distribution", dict(sorted(ks.items(), key=lambda x: (x[0] is None, x[0] or 0))))
print(f"Xi-cyclic {n} of {len(rows)} (Xi-acyclic {acyc}); lam*_key >= T/2 on {half} (largest T among them {tmaxhalf}); lam*_key < T/2 on "
      f"{n - half}; T >= 10 on {big}, of which lam*_key >= T/2 on {bighalf}; largest lam*_key {lmax}; largest T {tmax}; kill (iii) fires: {int(n > 0 and half == n)}")
print("sums over the spec rows: steps", sum(d["T"] for d in rows.values()), "stalls", sum(d["stalls"] for d in rows.values()),
      "max maxlen", max(d["maxlen"] for d in rows.values()), "max tail", max(d["tail"] for d in rows.values()),
      "must-0 sum", sum(d[c] for d in rows.values() for c in ("imp3", "monofail", "k3fail", "k4fail", "einF", "l3fail", "phifail", "phivals3", "p1", "pclos", "p3")))
