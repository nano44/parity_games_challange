#!/usr/bin/env python3
"""L-RED successor 39 (R169): mk168.py for srz3c.py models (EXTTGT: sink t2 -> hp, per-gate static target hq). Original: real game from a srz3b.py MODEL_OUT json (COPIES, STATICESC, HPS0=2, UNIFORM period 2 for j >= 3):
mk167g.py graph + static gate escapes hh_i (H_i) -> hps; hs2 starts on dd_1, hps2 on dd_2. Symbol map (line A): RA_j -> MU2_j, MA_j ->
M2_j, XA_j -> X_j, GA_j -> GM2_j, A_j -> BA2_j, BB_j -> BB_j, H_j -> H_j, BA3A -> BA3_t, BBBA -> BBB_t, RA0 -> MU0; escA_j -> escj.
E1 markers (outside the model) by env E1="MU_1:key:par,..." on the model's rank scale. Usage: mk168.py MODEL.json K m2 m3 OUT.pg OUT.start"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mk167g
M = json.load(open(sys.argv[1])); K, m2, m3 = map(int, sys.argv[2:5]); D = M["D"]; JJ = M["J"]
ex = {}
MAP = {"RA": "MU2", "MA": "M2", "XA": "X", "GA": "GM2", "A": "BA2", "BB": "BB", "H": "H"}
def src(c, j):
    if j <= 2 or j <= JJ: return f"{c}{j}", 0                 # inside the model window: take the model's own symbol
    b = JJ - 1 if (JJ - 1) % 2 == j % 2 else JJ - 2           # beyond: period-2 extension from the last two modelled indices >= 3
    b = b if b >= 3 else b + 2
    return f"{c}{b}", D * (j - b) // 2
for c, real in MAP.items():
    for j in range(1, m2 + 1):
        if c in ("GA", "H") and j == 1: continue
        sym, sh = src(c, j)
        if M["present"][sym]: ex[f"{real}_{j}"] = [M["rank"][sym] + sh, 0 if M["even"][sym] else 1]
for t in range(1, m3 + 1):
    for sym, real in (("BBBA", "BBB"), ("BA3A", "BA3")):
        if M["present"][sym]: ex[f"{real}_{t}"] = [M["rank"][sym] + 1e-3 * t, 0 if M["even"][sym] else 1]
if M["present"]["RA0"]: ex["MU0"] = [M["rank"]["RA0"], 0 if M["even"]["RA0"] else 1]
for item in filter(None, os.environ.get("E1", "").split(",")):
    nm, key, par = item.split(":"); ex[nm] = [float(key), int(par)]
escj = {str(j): M["esc"][f"A{src('', j)[0] if False else (j if j <= JJ else (JJ - 1 if (JJ - 1) % 2 == j % 2 else JJ - 2))}"] for j in range(1, m2 + 1)}
gen = {"ESC": 0, "LOW": True, "HPS0": 2, "STATIC": True, "mk": {}, "explicit": ex, "escj": escj, "T2": True, "hq": M.get("hq", {})}
if M["present"].get("T2"): ex["T2"] = [M["rank"]["T2"], 0 if M["even"]["T2"] else 1]
print(f"K {K} m2 {m2} m3 {m3} n {mk167g.write(K, m2, m3, gen, sys.argv[5], sys.argv[6])}")
