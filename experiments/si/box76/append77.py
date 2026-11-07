#!/usr/bin/env python3
"""L-SI box 77: PASS-FREEZE instance. Appends to an L^R_d genome (FILE, start START) a top pair (movers 2d, 2d+1, level d, W-targets
2d-2+k by R110's wiring) whose four options have Xi-target X, fresh beta ranks above all others, the start option even and the other
odd (each new mover prefers its start option forever), fresh gates, start split (0, 1). Nobody targets the new movers and keys of levels
< d do not read level d, so levels 0..d-1 run exactly as before; the new pair never moves and F(d) = F(d-1) (Lemma PASS-FREEZE).
Writes OUT (stored start = START + 01) and prints both profiles."""
import sys, os, json, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from tw import Sim, analyse, is_lr
f, start, out = sys.argv[1], sys.argv[2], sys.argv[3]
G = json.load(open(f)); N = G["N"]; d = N // 2
def prof(G, st):
    sim = Sim(G); S = sim.run(tuple(st)); a = analyse(sim, S); T = a["T"]; dd = G["N"] // 2
    return T, [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(dd)], \
        [sum(1 for t in range(1, T + 1) if y in a["Mv"][t]) for y in range(G["N"])], S
st = [int(c) for c in start]
T0, F0, mv0, S0 = prof(G, st)
H2 = copy.deepcopy(G); M = len(H2["br"]); r0 = max(H2["br"]) + 1; g0 = max(max(g) for g in H2["gate"]) + 1
H2["N"] = N + 2; H2["lev"] = H2["lev"] + [d, d]; newst = st + [0, 1]
for i, x in enumerate((N, N + 1)):
    H2["opts"].append([[2 * (d - 1) + k, -1, M + 2 * i + k] for k in range(2)])
    H2["gate"].append([g0 + 2 * i, g0 + 2 * i + 1])
    for k in range(2):
        H2["br"].append(r0 + 2 * i + k); H2["bp"].append(0 if k == newst[x] else 1)
H2["start"] = newst
assert is_lr(H2)
T1, F1, mv1, S1 = prof(H2, newst)
print("base  %s start %s: T %d F %s" % (os.path.basename(f), start, T0, F0))
print("frozen top pair: T %d F %s moves of new pair %d %d; lower states identical: %s" % (T1, F1, mv1[N], mv1[N + 1], [s[:N] for s in S1] == S0))
assert T1 == T0 and F1[:d] == F0 and mv1[N] == mv1[N + 1] == 0 and F1[d] == F0[d - 1] and [s[:N] for s in S1] == S0
json.dump(H2, open(out, "w")); print("written", out)
