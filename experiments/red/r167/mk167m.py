#!/usr/bin/env python3
"""L-RED successor 39 (R167): build a real game (mk167g.py graph) from a srz3.py MODEL_OUT json (UNIFORM, period 2 from j = 3 on),
extended to any m2: rank(c_j) = rank(c_b) + D (j - b) / 2 with b = 3 (j odd) or 4 (j even). Symbol map: R_j -> MU2_j (rider dd_j),
M_j -> M2_j (mdd_j), X_j -> X_j (x_j), A_j -> BA2_j (aa_j), G_j -> GM2_j (gg_j), BB_j -> BB_j, BBB -> BBB_t (all t, +tiny), BA3 -> BA3_t,
R0 -> MU0; esc_j -> escj. E1 markers (outside the model): env E1="MU_1:key:par,MU_2:key:par,GM_2:key:par" (keys on the model's scale;
default: all inert, below every model symbol is not needed). Drivers start LOW (dd_1 / dd_0) unless HIGH=1.
Usage: mk167m.py MODEL.json K m2 m3 OUT.pg OUT.start"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mk167g
M = json.load(open(sys.argv[1])); K, m2, m3 = map(int, sys.argv[2:5]); D = M["D"]
ex = {}
def put(name, sym, shift=0.0):
    if M["present"][sym] and sym != "T": ex[name] = [M["rank"][sym] + shift, 0 if M["even"][sym] else 1]
MAP = {"R": "MU2", "M": "M2", "X": "X", "A": "BA2", "G": "GM2", "BB": "BB"}
for c, real in MAP.items():
    for j in range(1, m2 + 1):
        if j <= 2: sym, sh = f"{c}{j}", 0
        else: b = 3 if j % 2 else 4; sym, sh = f"{c}{b}", D * (j - b) // 2
        if c == "G" and j == 1: continue
        if M["present"][sym]: ex[f"{real}_{j}"] = [M["rank"][sym] + sh, 0 if M["even"][sym] else 1]
for t in range(1, m3 + 1): put(f"BBB_{t}", "BBB", 1e-3 * t); put(f"BA3_{t}", "BA3", 1e-3 * t)
put("MU0", "R0")
for item in filter(None, os.environ.get("E1", "").split(",")):
    nm, key, par = item.split(":"); ex[nm] = [float(key), int(par)]
escj = {}
for j in range(1, m2 + 1):
    escj[str(j)] = M["esc"][str(j)] if j <= 2 else M["esc"][str(3 if j % 2 else 4)]
gen = {"ESC": 0, "LOW": os.environ.get("HIGH") != "1", "MID": os.environ.get("MID") == "1", "mk": {}, "explicit": ex, "escj": escj}
print(f"K {K} m2 {m2} m3 {m3} n {mk167g.write(K, m2, m3, gen, sys.argv[5], sys.argv[6])}")
