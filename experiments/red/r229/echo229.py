#!/usr/bin/env python3
"""L-RED 63 R229 item 7: BOX 94's echo claim S(g_Q) = S(v) ∪ (S(v) + 1) (S(x) = steps at which x's VJ value changes), per level, on
R221 own.py. Names from the generator's names JSON (genm90 / gennest: «v», «Q», level prefix l<j>_). Prints per level |S(v)|, |S(g_Q)|,
echo (1 if equal), and the two set differences' sizes. Usage: echo229.py G.json NAMES.json"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r221")]
import own
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[2])); out, V, O, _ = own.run(G, 3000); T = len(out) - 1
S = lambda x: {t for t in range(1, T + 1) if out[t][1][x] != out[t - 1][1][x]}
res = []
for j in range(1, 10):
    p = "" if j == 1 else f"l{j}_"
    if p + "Q" not in nm: break
    Q = nm[p + "Q"]; v = nm[p + "v"]; gQ = V[("g", (Q, 0))]
    Sv, Sg = S(v), S(gQ); E = Sv | {t + 1 for t in Sv if t + 1 <= T}
    res.append(f"L{j} |S(v)| {len(Sv)} |S(gQ)| {len(Sg)} echo {int(Sg == E)} gQ-E {len(Sg - E)} E-gQ {len(E - Sg)}")
print(os.path.basename(sys.argv[1]), "T", T, "; ".join(res))
