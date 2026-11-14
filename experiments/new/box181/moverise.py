#!/usr/bin/env python3
"""L-NEW box 181: (MOVE-RISE) does every move of z at step t strictly raise cv(z) (cv_(s_t)(z) > cv_(s_(t-1))(z))? (MOVES) max moves(z)
against 2d. (INNER) max flips of a lower level's pair inside a gap BOUNDED BY RISES AT BOTH ENDS (r_i, r_(i+1)] of cv(z), levels below
lev(z). L^R_d files, stored start + arg-max start (d <= 5). Usage: moverise.py files..."""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}; exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl)
is_lr = fl["is_lr"]; C = dict(runs=0, moves=0, MOVE_NORISE=0, MOVES_gt_2d=0); mxm = (0,); inner = (0,)
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert is_lr(G)
    except Exception: continue
    g = Gen(G); N = G["N"]; d = N // 2; starts = [tuple(G["start"])]
    if d <= 5:
        allS = list(itertools.product((0, 1), repeat=N)); starts.append(max(allS, key=lambda s: len(g.run(s)[0])))
    for st in starts:
        S, _ = g.run(st); T = len(S) - 1; C["runs"] += 1; K = [g.keys(s) for s in S]
        flip = [[int((K[t][2 * l] < K[t][2 * l + 1]) != (K[t - 1][2 * l] < K[t - 1][2 * l + 1])) for l in range(d)] for t in range(1, T + 1)]
        for z in range(N):
            cv = [g.face(s, z, s[z]) for s in S]; m = 0
            for t in range(1, T + 1):
                if S[t][z] != S[t - 1][z]:
                    m += 1; C["moves"] += 1; C["MOVE_NORISE"] += cv[t] <= cv[t - 1]
            C["MOVES_gt_2d"] += m > 2 * d
            if m > mxm[0]: mxm = (m, os.path.basename(f), "mover", z, "d", d)
            rises = [t for t in range(1, T + 1) if cv[t] > cv[t - 1]]
            for a, b in zip(rises, rises[1:]):
                for l in range(G["lev"][z]):
                    F = sum(flip[t - 1][l] for t in range(a + 1, b + 1))
                    if F > inner[0]: inner = (F, os.path.basename(f), st, "z", z, "gap", (a, b), "level", l)
print(" ".join("%s %d" % kv for kv in C.items())); print("max moves", mxm); print("max inner-gap flips of one lower level", inner)
