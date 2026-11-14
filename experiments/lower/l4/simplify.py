#!/usr/bin/env python3
"""L-LOWER 4: greedy core extraction for a doubling tower. Keeps the property P: F(1..H) = 2F(l-1)+2 exact (from the run's own F(0))
and F(H) unchanged. Moves tried, in order, until none applies: (a) truncate the top level (pointers into it re-targeted to X);
(b) re-target one option to X; (c) make a mover static (both options to X, start option preferred by parity/rank unchanged? no:
only (a), (b)). Usage: simplify.py in.json H out.json"""
import sys, os, json, copy
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run
from trace import keys
def Fs(G):
    S = run(G, G["start"]); d = G["N"] // 2
    O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(d)] for k in (keys(G, s) for s in S)]
    return [sum(O[t][l] != O[t-1][l] for t in range(1, len(S))) for l in range(d)], len(S) - 1
G = json.load(open(sys.argv[1])); H = int(sys.argv[2])
F0, T0 = Fs(G); target = F0[:H + 1]
def ok(G):
    try: F, T = Fs(G)
    except Exception: return False
    return F[:H + 1] == target
def truncate(G):
    N = G["N"] - 2; G2 = copy.deepcopy(G); G2["N"] = N; G2["lev"] = G["lev"][:N]
    G2["opts"] = [[[o[0], o[1] if o[1] < N else -1, o[2]] for o in G["opts"][x]] for x in range(N)]
    used = sorted(o[2] for x in range(N) for o in G2["opts"][x])
    G2["gate"] = G["gate"][:N]; G2["start"] = G["start"][:N]
    # keep beta table indices (br/bp indexed by beta id); drop unused ids by remapping
    rm = {b: i for i, b in enumerate(used)}
    order = sorted(used, key=lambda b: G["br"][b]); rank = {b: r for r, b in enumerate(order)}
    G2["br"] = [rank[b] for b in used]; G2["bp"] = [G["bp"][b] for b in used]
    for x in range(N):
        for o in G2["opts"][x]: o[2] = rm[o[2]]
    return G2
changed = True
while changed:
    changed = False
    while G["N"] > 2 * (H + 1):
        G2 = truncate(G)
        if ok(G2): G = G2; changed = True; print("truncated to d", G["N"] // 2, flush=True)
        else: break
    for x in range(G["N"]):
        for k in range(2):
            if G["opts"][x][k][1] >= 0:
                G2 = copy.deepcopy(G); G2["opts"][x][k][1] = -1
                if ok(G2): G = G2; changed = True
F, T = Fs(G)
json.dump(G, open(sys.argv[3], "w"))
print("d", G["N"] // 2, "T", T, "F", F, "mover targets:", sum(1 for x in range(G["N"]) for o in G["opts"][x] if o[1] >= 0))
