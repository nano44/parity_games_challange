#!/usr/bin/env python3
"""L-NEW box 143: print a run of a 2-wide ladder genome: per state t the sigma bits per level, L_l per level, B_x per mover
(0/1/= on a tie), and the movers of step t. Usage: trace.py genome.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box139", "paths.py")).read().split("def vx(G):")[0]
ns = {"__file__": os.path.join(HERE, "..", "box139", "paths.py")}; exec(src, ns); run = ns["run"]; fc = ns["fc"]
G = json.load(open(sys.argv[1])); S, CUR, KEY, why = run(G, cap=5000); N = G["N"]; d = N // 2; opts = G["opts"]
print("opts (W-target, Xi-target):", [[(o[0], o[1]) for o in opts[v]] for v in range(N)], "xorder", G.get("xorder"))
for t in range(len(S)):
    val, idx, _, M = fc.values(G, list(S[t])); F = [[val(N + idx[(v, k)]) for k in range(2)] for v in range(N)]
    K = KEY[min(t, len(KEY) - 1)]
    Ls = "".join("u" if K[2 * l] < K[2 * l + 1] else "v" for l in range(d))
    Bs = " ".join("".join(("0" if F[v][0] > F[v][1] else "1" if F[v][1] > F[v][0] else "=") for v in (2 * l, 2 * l + 1)) for l in range(d))
    sg = " ".join("".join(str(S[t][v]) for v in (2 * l, 2 * l + 1)) for l in range(d))
    mv = [v for v in range(N) if t > 0 and S[t][v] != S[t - 1][v]]
    print(f"t {t:3d} sigma {sg}  L {Ls}  B {Bs}  movers {mv}")
