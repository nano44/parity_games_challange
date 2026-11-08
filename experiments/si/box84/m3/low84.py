#!/usr/bin/env python3
"""L-SI box 84 milestone 3 (i), smallest test: on a pair84 genome (MIRROR, MUP=1) add a level-1 mirror M1 (copy of B1's rule: UP ->
M2, SET with continuation -> M2, an RS2 lane of length LM1 exiting to B2, mirror e above e_B1) and give B2 an option LOW (beta -> M1,
dead e-face): B2's lower-reading hub. M1 never passes B2 (PRIV holds for LOW) iff M1's lane exits avoid B2 (EXIT=M2) — with EXIT=B2 the
LOW route returns to B2 (PRIV fails). Usage: low84.py IN.json LM1 EXIT(M2|B2) LOWTOP(1|0) OUT.json"""
import sys, json
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[1][:-5] + ".names.json"))
LM1, EXIT, lowtop, out = int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), sys.argv[5]
ix = {n: i for i, n in enumerate(nm["movers"])}
def mv(name, lev):
    G["N"] += 1; G["lev"].append(lev); G["opts"].append([]); G["gate"].append([]); G["start"].append(0); nm["movers"].append(name); nm["opts"].append([]); ix[name] = G["N"] - 1; return ix[name]
nb = [len(G["br"])]
def beta(rank, par):           # rank: 'top' or 'bot'
    k = len(G["br"])
    if rank == "top": G["br"].append(k)
    else: G["br"] = [r + 1 for r in G["br"]] + [0]
    G["bp"].append(par); return k
gates = []
def opt(x, wt, xt, rank, par, label, gate_hi=False):
    k = beta(rank, par); G["opts"][x].append([wt, xt, k]); nm["opts"][x].append(label); gates.append((x, len(G["opts"][x]) - 1, gate_hi))
D0 = ix["D0"]; M2, B2 = ix["M2"], ix["B2"]
M1 = mv("M1", 1); w = mv("wm1", 0); opt(w, -1, M2, "bot", 1, "cont")
opt(M1, D0, M2, "bot", 1, "UP")
d = mv("dm1", 0); opt(d, -1, -1, "top", 0, "bonus")
a = [mv(f"am1_{j}", 0) for j in range(LM1)]; b = [mv(f"bm1_{j}", 0) for j in range(LM1)]
for j in range(LM1):
    opt(a[j], -1, b[j], "top", 0, "lane"); opt(b[j], -1, ix[EXIT], "bot", 1, "exit"); opt(b[j], -1, b[j - 1] if j else d, "bot", 1, "chain")
    opt(M1, D0, a[j], "bot", 0, f"lane{j}")
opt(M1, w, M1, "bot", 0, "SET", gate_hi=True)
opt(B2, ix["D1"], M1, "top" if lowtop else "bot", 0, "LOW")
# gate indices: new gates get fresh indices; M1's SET above every level-1 gate (mirror e above e_B1), others at the end
allg = sorted(g for o in G["gate"] for g in o); nxt = (allg[-1] + 1) if allg else 0
for (x, k, hi) in gates:
    G["gate"][x].append(nxt); nxt += 1
assert sorted(G["br"]) == list(range(len(G["br"]))) and sorted(g for o in G["gate"] for g in o) == list(range(len(G["br"])))
json.dump(G, open(out, "w")); json.dump(nm, open(out[:-5] + ".names.json", "w"))
