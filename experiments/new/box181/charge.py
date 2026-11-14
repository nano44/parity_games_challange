#!/usr/bin/env python3
"""L-NEW box 181: charge every rise of cv(z) (z a mover; R(x, k) = rises of cv(xt(x, k)), box 180 RISE-EQUIV) to the FIRST mover y* on
z's chain under s_(t-1) (z included) whose option changes at step t (a rise needs one: values change only through option changes on the
chain). Reports: max over (run, z, level l) of #rises of cv(z) charged to level l (CHG-LEV), max over (run, z, y) charged to one mover
y (CHG-MOV), rises with no changed mover on the chain (NOCAUSE, must be 0), and the max rises of one cv(z). Usage: charge.py files..."""
import os, sys, json, itertools
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}; exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl)
is_lr = fl["is_lr"]; mx = {"CHG-LEV": (0,), "CHG-MOV": (0,), "R": (0,)}; nocause = 0; runs = 0; hist = Counter()
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert is_lr(G)
    except Exception: continue
    g = Gen(G); N = G["N"]; d = N // 2; starts = [tuple(G["start"])]
    if d <= 5:
        allS = list(itertools.product((0, 1), repeat=N)); starts.append(max(allS, key=lambda s: len(g.run(s)[0])))
    for st in starts:
        S, _ = g.run(st); T = len(S) - 1; runs += 1
        for z in range(N):
            cl, cm, R = Counter(), Counter(), 0
            for t in range(1, T + 1):
                a, b = g.face(S[t - 1], z, S[t - 1][z]), g.face(S[t], z, S[t][z])
                if b <= a: continue
                R += 1; chain = [z] + g.play(S[t - 1], z, S[t - 1][z]); ys = [y for y in chain if S[t][y] != S[t - 1][y]]
                if not ys: nocause += 1; continue
                y = ys[0]; cl[G["lev"][y]] += 1; cm[y] += 1
            for l, c in cl.items():
                hist[c] += 1
                if c > mx["CHG-LEV"][0]: mx["CHG-LEV"] = (c, os.path.basename(f), st, "z", z, "level", l)
            for y, c in cm.items():
                if c > mx["CHG-MOV"][0]: mx["CHG-MOV"] = (c, os.path.basename(f), st, "z", z, "mover", y)
            if R > mx["R"][0]: mx["R"] = (R, os.path.basename(f), "z", z, "d", d)
print("runs", runs, "NOCAUSE", nocause, "histogram of per-(z, level) charges", dict(sorted(hist.items())))
for k, v in mx.items(): print(k, v)
