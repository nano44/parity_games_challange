#!/usr/bin/env python3
"""L-SI box 76: ALT-MIN check and rise counts. For every mover x (deg 2) of every corpus run (tw.py corpus/simulator):
R(x) := #{t : cv_(s_t)(x) > cv_(s_(t-1))(x)} (rises of the current value), R_k(x) := #{t : v_(s_t)(x, k) > v_(s_(t-1))(x, k)},
PF_x := pi changes; P0/P1 := pi changes to 0 / to 1.
Checks (violation counters; lane-proved statements of docs/si/N5-TROPICAL-box76.md): TO_k: P_k > R_k; ALT: PF > 2 min(R_0, R_1) + 1;
RMV: moves(x) > R(x); MOVEALT: moves(x) > 2 + 2 min(R_0, R_1).
DATA: per d, max R(x) (all; Xi-targets), max of R(x) - moves(x), max PF; witnesses."""
import sys, os, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tw import load_corpus, is_lr, Sim, analyse
C = collections.Counter(MONO_VIOL=0, ALT=0, TO_k=0, RMV=0, MOVEALT=0); R = collections.defaultdict(lambda: [-99, None])
def upd(k, v, w):
    if v > R[k][0]: R[k] = [v, w]
for path, G in load_corpus():
    if not is_lr(G): continue
    sim = Sim(G); N = G["N"]; d = N // 2
    Z = {G["opts"][x][k][1] for x in range(N) for k in range(2)} - {-1}
    for s0 in (itertools.product((0, 1), repeat=N) if N <= 10 else [tuple(G["start"])]):
        S = sim.run(s0); a = analyse(sim, S); T = a["T"]; C["runs"] += 1
        V = [[(sim.val(S[t], x, 0), sim.val(S[t], x, 1)) for x in range(N)] for t in range(T + 1)]
        for x in range(N):
            mv = sum(1 for t in range(1, T + 1) if x in a["Mv"][t])
            Rk = [sum(1 for t in range(1, T + 1) if V[t][x][k] > V[t - 1][x][k]) for k in range(2)]
            Rc = sum(1 for t in range(1, T + 1) if V[t][x][S[t][x]] > V[t - 1][x][S[t - 1][x]])
            dec = sum(1 for t in range(1, T + 1) for k in range(2) if V[t][x][k] < V[t - 1][x][k])
            if dec: C["MONO_VIOL"] += 1
            P = [sum(1 for t in range(1, T + 1) if a["pi"][t][x] != a["pi"][t - 1][x] and a["pi"][t][x] == k) for k in range(2)]
            PF = P[0] + P[1]
            C["TO_k"] += (P[0] > Rk[0]) + (P[1] > Rk[1]); C["ALT"] += PF > 2 * min(Rk) + 1
            C["RMV"] += mv > Rc; C["MOVEALT"] += mv > 2 + 2 * min(Rk); C["movers"] += 1
            w = (path, "".join(map(str, s0)), x, G["lev"][x], x in Z, "mv", mv, "R", Rc, "Rk", Rk, "PF", PF, "T", T)
            upd((d, "R"), Rc, w); upd((d, "R-mv"), Rc - mv, w); upd((d, "minRk"), min(Rk), w)
            if x in Z: upd((d, "Z:R"), Rc, w)
            upd((d, "mv-2minRk"), mv - 2 * min(Rk), w)
print("INFO", " ".join("%s %d" % kv for kv in sorted(C.items())))
for k in sorted(R): print(k, R[k][0], R[k][1])
