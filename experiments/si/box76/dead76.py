#!/usr/bin/env python3
"""L-SI box 76: replay of the DEAD instances of docs/si/N5-TROPICAL-box76.md (own simulator tw.Sim; XCHK=<box150/check.py> also
replays each run with L-NEW's Gen and requires identical states). Deterministic; asserts every printed number."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from tw import Sim, analyse, is_lr
Gen = None
if os.environ.get("XCHK"):
    ns = {"__file__": os.environ["XCHK"], "__name__": "lib"}; exec(open(os.environ["XCHK"]).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]

def run(f, start):
    G = json.load(open(os.path.join(H, "inst", f))); assert is_lr(G)
    sim = Sim(G); s0 = tuple(int(c) for c in start); S = sim.run(s0)
    if Gen is not None:
        S2, _ = Gen(G).run(s0); assert [tuple(x) for x in S2] == S, "XCHK mismatch " + f
    a = analyse(sim, S); T = a["T"]; N = G["N"]
    mv = [sum(1 for t in range(1, T + 1) if y in a["Mv"][t]) for y in range(N)]
    R = [sum(1 for t in range(1, T + 1) if sim.val(S[t], y, S[t][y]) > sim.val(S[t - 1], y, S[t - 1][y])) for y in range(N)]
    F = [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(N // 2)]
    return G, sim, S, a, T, mv, R, F

# 1. SUM-COUPLE: dense_d5_l3_H10 (L-RED R214 36d340c7), start 1100110110
G, sim, S, a, T, mv, R, F = run("dense_d5_l3_H10.json", "1100110110")
x = 6; y0, y1 = G["opts"][x][0][1], G["opts"][x][1][1]
lowmax = max(mv[:6])
pis = [a["pi"][t][x] for t in range(T + 1)]
print("SUM-COUPLE dense_d5_l3_H10 start 1100110110 T %d moves %s" % (T, mv))
print("  mover 6 (level 3) moves %d at steps %s; Xi-targets of its options: %d (level %d, moves %d), %d (level %d, moves %d)"
      % (mv[x], [t for t in range(1, T + 1) if x in a["Mv"][t]], y0, G["lev"][y0], mv[y0], y1, G["lev"][y1], mv[y1]))
print("  pi(6) along the run %s; max moves over levels 0-2 = %d; increment over levels below = %d"
      % ("".join(map(str, pis)), lowmax, mv[x] - lowmax))
assert T == 10 and mv[x] == 10 and (y0, y1) == (5, 4) and mv[5] == 4 and mv[4] == 4 and lowmax == 4
assert all(pis[t] != pis[t - 1] for t in range(1, T + 1))
# strict Xi-descendants of 6
ch = {v: {G["opts"][v][k][1] for k in range(2)} - {-1} for v in range(10)}
def D(v, acc):
    for u in ch[v]:
        if u not in acc: acc.add(u); D(u, acc)
    return acc
D6 = D(x, set()); md = max(mv[u] for u in D6)
print("  strict Xi-descendants of 6: %s, max moves among them %d; moves(6) - that max = %d; moves(4) + moves(5) + 2 = %d"
      % (sorted(D6), md, mv[x] - md, mv[4] + mv[5] + 2))
assert 6 not in D6 and md == 4 and mv[x] - md == 6 and mv[4] + mv[5] + 2 == 10
print("  R(4) %d R(5) %d; ALT-MIN bound 2 + 2 min(R(5), R(4)) = %d >= moves(6) %d" % (R[4], R[5], 2 + 2 * min(R[5], R[4]), mv[x]))
assert 2 + 2 * min(R[5], R[4]) >= mv[x]

# 2. RISE-N (= L-RED R213 RISE-2D): rise_d5_R13 (L-RED 9eac6d70), start 1110110001
G, sim, S, a, T, mv, R, F = run("rise_d5_R13.json", "1110110001")
print("RISE-N rise_d5_R13 start 1110110001 T %d: R(8) = %d > N = %d (moves(8) = %d)" % (T, R[8], G["N"], mv[8]))
assert R[8] == 13 and G["N"] == 10 and T == 16

# 3. SPAWN-2: dd_d5_F14 (R113 PAIR-DOUBLE tight instance), start 1101111110
G, sim, S, a, T, mv, R, F = run("dd_d5_F14.json", "1101111110")
W = [F[j - 1] + 1 for j in range(1, 5)]
print("SPAWN-2 dd_d5_F14 start 1101111110 T %d: F %s; level-j windows (j = 1..4) %s; moves %s" % (T, F, W, mv))
assert F == [2, 3, 6, 14, 7] and F[3] == 2 * F[2] + 2 and W == [3, 4, 7, 15]
print("dead76: all assertions PASS" + (" (Gen cross-check on)" if Gen else ""))
