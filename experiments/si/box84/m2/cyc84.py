#!/usr/bin/env python3
"""L-SI box 84 milestone 2 (ii): add a CYC option to a bit of a ladder83 / pair84 genome, so that PRIV FAILS by construction.
Bit B (by name): new option CYC with gate e-face -> y (new level-(lev B - 1) mover whose one option has beta -> TGT, dead e-face) and
beta (even, rank TOP or BOTTOM of all betas) -> c (new level-0 mover, one option beta -> B, odd small beta). So the play from CYC's gate,
when Odd keeps beta, returns to B through an EVEN-top route (beta_CYC). Gate index of CYC: above (GHI=1) or below (GHI=0) every gate of
B's level. Usage: cyc84.py IN.json B TGT TOP(1|0) GHI(1|0) OUT.json"""
import sys, json
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[1][:-5] + ".names.json"))
B, TGT, top, ghi, out = sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
ix = {n: i for i, n in enumerate(nm["movers"])}; b, tg = ix[B], ix[TGT]; N = G["N"]; M = sum(len(o) for o in G["opts"])
lb = G["lev"][b]; dummies = [i for i, n in enumerate(nm["movers"]) if n.startswith("D")]
dlow = next((i for i in dummies if G["lev"][i] == lb - 2), -1) if lb >= 2 else -1
# new movers y (level lb - 1), c (level 0)
y, c = N, N + 1; G["N"] = N + 2; G["lev"] += [lb - 1, 0]; nm["movers"] += [f"y{B}", f"c{B}"]
def add_beta(rank_top, par):
    k = len(G["br"])
    if rank_top: G["br"].append(k)
    else: G["br"] = [r + 1 for r in G["br"]] + [0]
    G["bp"].append(par); return k
G["opts"].append([[dlow, tg, add_beta(0, 1)]]); nm["opts"].append(["toTGT"])
G["opts"].append([[-1, b, add_beta(0, 1)]]); nm["opts"].append(["back"])
G["opts"][b].append([y, c, add_beta(top, 0)]); nm["opts"][b].append("CYC")
gl = [g for x in range(N) if G["lev"][x] == lb for g in G["gate"][x]]
allg = [g for o in G["gate"] for g in o]; base = max(allg) + 1
G["gate"].append([base]); G["gate"].append([base + 1])
if ghi: G["gate"][b].append(base + 2)
else:
    m = min(gl); G["gate"] = [[g + 1 if g >= m else g for g in o] for o in G["gate"]]; G["gate"][b].append(m)
G["start"] += [0, 0]
assert sorted(G["br"]) == list(range(len(G["br"]))) and sorted(g for o in G["gate"] for g in o) == list(range(len(G["br"])))
json.dump(G, open(out, "w")); json.dump(nm, open(out[:-5] + ".names.json", "w"))
