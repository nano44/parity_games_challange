#!/usr/bin/env python3
"""L-NEW box 181: key flips per level BETWEEN consecutive rises of one option's value, on L^R_d runs (box150 simulator).
For option (x, k) with rise steps r_1 < ... < r_R, the gaps are (0, r_1], (r_1, r_2], ..., (r_R, T]. In each gap, F_l := #steps at which
the key order of the level-l pair (2l, 2l+1) flips (P-IDEAL-KEYS / R111 notation). Reports, per level l, the max over all options and gaps
of F_l in one gap, and the max of sum_l F_l in one gap; also the same restricted to levels below lev(x) (the lemma's form: «each lower
level contributes O(1) flips between two rises»). Usage: gapflips.py files..."""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}; exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl)
is_lr = fl["is_lr"]
best = {}; maxsum = (0,); maxsum_low = (0,); runs = 0
def upd(key, val, where):
    if val > best.get(key, (-1,))[0]: best[key] = (val,) + where
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert is_lr(G)
    except Exception: continue
    g = Gen(G); d = G["N"] // 2
    starts = [tuple(G["start"])]
    if d <= 5:
        allS = list(itertools.product((0, 1), repeat=2 * d)); starts.append(max(allS, key=lambda s: len(g.run(s)[0])))
    for st in starts:
        S, _ = g.run(st); T = len(S) - 1; runs += 1; K = [g.keys(s) for s in S]
        flip = [[int((K[t][2 * l] < K[t][2 * l + 1]) != (K[t - 1][2 * l] < K[t - 1][2 * l + 1])) for l in range(d)] for t in range(1, T + 1)]
        for x in range(2 * d):
            for k in (0, 1):
                v = [g.face(s, x, k) for s in S]; rises = [t for t in range(1, T + 1) if v[t] > v[t - 1]]
                cuts = [0] + rises + ([T] if not rises or rises[-1] != T else [])
                for a, b in zip(cuts, cuts[1:]):
                    F = [sum(flip[t - 1][l] for t in range(a + 1, b + 1)) for l in range(d)]
                    for l in range(d): upd(("F", l), F[l], (os.path.basename(f), st, (x, k), (a, b)))
                    low = sum(F[l] for l in range(x // 2)); tot = sum(F)
                    if tot > maxsum[0]: maxsum = (tot, os.path.basename(f), (x, k), (a, b), F)
                    if low > maxsum_low[0]: maxsum_low = (low, os.path.basename(f), (x, k), (a, b), F, "lev", x // 2)
                    upd(("lowmax", x // 2), max([F[l] for l in range(x // 2)] or [0]), (os.path.basename(f), (x, k), (a, b)))
print("runs", runs)
for key in sorted(best): print(key, best[key][0], best[key][1:])
print("max total flips in one gap:", maxsum)
print("max lower-level flips in one gap:", maxsum_low)
