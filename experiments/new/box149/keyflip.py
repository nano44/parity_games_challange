#!/usr/bin/env python3
"""L-NEW box 149 KEYFLIP: check of Lemma KEYFLIP (deg 2, any IDEAL-ACYC genome): moves(x) <= 1 + KF_x, where KF_x = number of steps t
with KP(x) under the keys of s_(t-1) != KP(x) under the keys of s_t (box 147 stat.py features). Prints movers checked, violations
(must be 0), total moves and total key flips per genome. Usage: keyflip.py genome.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(HERE, "..", "box147", "stat.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split('\nif __name__')[0], ns); analyse = ns["analyse"]
for p in sys.argv[1:]:
    G = json.load(open(p)); R = analyse(G); S, FS = R["S"], R["FS"]; n = G["N"]; T = len(S) - 1; bad = mt = kt = 0
    for x in range(n):
        mv = sum(1 for t in range(1, T + 1) if S[t][x] != S[t - 1][x]); kf = sum(1 for t in range(1, T + 1) if FS[t - 1]["KP"][x] != FS[t]["KP"][x])
        bad += mv > 1 + kf; mt += mv; kt += kf
    print(f"KEYFLIP {os.path.basename(p)} N {n} STEPS {T} MOVES {mt} KFLIPS {kt} VIOL {bad}")
