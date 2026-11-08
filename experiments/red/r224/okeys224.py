#!/usr/bin/env python3
"""L-RED 58 R224: test of Lemma STRETCH's premise «o(l) at a state is a function of the states of pairs 0..l only» (L10 §1a) with
L-LOWER's own okeys (sim6; env LOW). For every state s of the run and every level l, R random re-draws of every mover of pairs > l;
counter: (state, l, draw) with o_l changed (unit: draw; scope: the stored run). Also F(0..H-2) of a target file (changes of o_l along
the target, with pairs > H-2 held at the state the target starts from). Usage: okeys224.py GENOME R SEED [TARGET H]"""
import sys, os, random
LOW = os.environ["LOW"]; sys.path[:0] = [os.path.join(LOW, "experiments/lower/l6")]
from sim6 import rd, run, okeys
D = rd(sys.argv[1]); R = int(sys.argv[2]); rng = random.Random(int(sys.argv[3])); S, O = run(D); n2 = len(S[0]); d = n2 // 2
bad = 0; tot = 0
for s in S:
    o = okeys(D, tuple(s))
    for l in range(d):
        for _ in range(R):
            s2 = list(s[:2 * (l + 1)]) + [rng.randrange(2) for _ in range(n2 - 2 * (l + 1))]
            tot += 1; bad += okeys(D, tuple(s2))[l] != o[l]
print(f"OKEYS224 states {len(S)} levels {d} draws {tot} o_l changed {bad}")
if len(sys.argv) > 4:
    H = int(sys.argv[5]); rows = [l.split() for l in open(sys.argv[4]) if l[0].isdigit()]
    tail = list(S[0][2 * (H - 1):]); F = [0] * (H - 1); prev = None
    for r in rows:
        o = okeys(D, tuple(int(c) for c in r[1]) + tuple(tail))
        if prev is not None: F = [F[l] + (o[l] != prev[l]) for l in range(H - 1)]
        prev = o
    print(f"OKEYS224 target {os.path.basename(sys.argv[4])} steps {len(rows) - 1} F(0..{H-2}) {F}")
