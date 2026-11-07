#!/usr/bin/env python3
"""L-SI box 77: replay of L-LOWER 3's l3/kill genomes (claude/l-lower 4d747490; byte copies in inst/lower/) from the stored start:
own simulator (tw.Sim); with XCHK=<box150/check.py> also L-NEW's Gen (states must be identical). Prints d, T, F-profile, doubling
levels, max moves of a Xi-target of level >= 1."""
import sys, os, json, glob
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from tw import Sim, analyse, is_lr
Gen = None
if os.environ.get("XCHK"):
    ns = {"__file__": os.environ["XCHK"], "__name__": "lib"}; exec(open(os.environ["XCHK"]).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
for f in sorted(glob.glob(os.path.join(H, "inst", "lower", "*.json"))):
    G = json.load(open(f)); assert is_lr(G); sim = Sim(G); s0 = tuple(G["start"]); S = sim.run(s0)
    if Gen is not None:
        S2, _ = Gen(G).run(s0); assert [tuple(x) for x in S2] == S, f
    a = analyse(sim, S); T = a["T"]; N = G["N"]; d = N // 2
    F = [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(d)]
    mv = [sum(1 for t in range(1, T + 1) if y in a["Mv"][t]) for y in range(N)]
    Z = {G["opts"][x][k][1] for x in range(N) for k in range(2)} - {-1}
    dbl = [l for l in range(1, d) if F[l] == 2 * F[l - 1] + 2]
    mz = max((mv[z], z) for z in Z if G["lev"][z] >= 1)
    print("%s d %d T %d F %s doubling %s max moves (z in Z, lev >= 1) %d (mover %d)" % (os.path.basename(f), d, T, F, dbl, mz[0], mz[1]))
print("replay77: done" + (" (Gen cross-check on)" if Gen else ""))
# ACYC-SPLIT instance: in REC_d10_tower_mu30, re-pointing both options of mover 9 (level 4, fuel of mover 4) onto the tower pair 3
# (movers 6, 7) closes a Xi-cycle 9 -> 6 or 7 -> 4 -> 9 (mover 4's option 0 has Xi-target 9).
import copy
sys.path.insert(0, H)
from climb77 import acyclic
G = json.load(open(os.path.join(H, "inst", "lower", "REC_d10_tower_mu30.json")))
assert G["opts"][4][0][1] == 9 and G["opts"][6][0][1] == 4 and G["opts"][7][1][1] == 4 and acyclic(G)
for a_, b_ in ((6, 7), (7, 6)):
    G2 = copy.deepcopy(G); G2["opts"][9][0][1] = a_; G2["opts"][9][1][1] = b_
    assert not acyclic(G2)
    print("ACYC-SPLIT REC_d10_tower_mu30: mover 9 options -> (%d, %d) gives a Xi-cycle (9 -> %d -> 4 -> 9)" % (a_, b_, a_))
# climb record (DATA): T 45 at d 10
G = json.load(open(os.path.join(H, "inst", "climb77_d10_T45.json"))); assert is_lr(G) and acyclic(G)
S = Sim(G).run(tuple(G["start"])); T = len(S) - 1; N = G["N"]
mv = [sum(1 for t in range(1, T + 1) if S[t][y] != S[t - 1][y]) for y in range(N)]
Z = {G["opts"][x][k][1] for x in range(N) for k in range(2)} - {-1}
print("CLIMB climb77_d10_T45 d 10 T %d max moves (z in Z, lev >= 1) %d" % (T, max(mv[z] for z in Z if G["lev"][z] >= 1)))
assert T == 45
