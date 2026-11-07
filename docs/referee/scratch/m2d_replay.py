"""REFEREE successor 25: replay of P-M2D-DEAD's instances with t3r_sim.py (successor 24's own IDEAL simulator; no L-LOWER code).
Prints: membership (in_LR with d), ISO, Z, per-step states and movers, moves(z) for z in Z of level >= 1, max, and the table string."""
import json, sys, itertools
sys.path.insert(0, __import__("os").path.dirname(__file__))
import t3r_sim as ts
for f in sys.argv[1:]:
    G = json.load(open(f)); N = G["N"]; d = N // 2
    S = ts.run(G); T = len(S) - 1
    Mv = [None] + [[x for x in range(N) if S[t][x] != S[t - 1][x]] for t in range(1, T + 1)]
    Z = sorted({G["opts"][x][k][1] for x in range(N) for k in range(2) if G["opts"][x][k][1] >= 0})
    iso = all(G["opts"][x][k][1] not in (0, 1) for x in range(N) for k in range(2))
    mv = {z: sum(1 for t in range(1, T + 1) if z in Mv[t]) for z in Z if G["lev"][z] >= 1}
    zmax = max(mv, key=mv.get)
    src = [(x, k) for x in range(N) for k in range(2) if G["opts"][x][k][1] == zmax]
    print(f.split("/")[-1], "N", N, "d", d, "even N", N % 2 == 0, "in_LR(d)", ts.in_LR(G, d), "ISO", iso, "start", "".join(map(str, G["start"])))
    print("  T", T, "Z", Z, "mu-candidate z", zmax, "lev", G["lev"][zmax], "moves", mv[zmax], "2d", 2 * d, "options with Xi-target z", src)
    print("  steps moving z:", [t for t in range(1, T + 1) if zmax in Mv[t]])
    print("  table:", "; ".join("%d %s%s" % (t, "".join(map(str, S[t])), (" " + str(Mv[t]).replace(" ", "")) if t else "") for t in range(T + 1)))
