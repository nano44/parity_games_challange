#!/usr/bin/env python3
"""L-LOWER 12: independent (sim6, Python big integers) count of room.c's score: caps, T, o(h-1) changes among core steps (pairs
0..h-1 move) and the adjacent pairs, plus N + M = 6d. Usage: adj.py GENOME [h]"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run, Fprof, caps
for p in sys.argv[1:]:
    if p.isdigit(): continue
    D = rd(p); S, O = run(D); F = Fprof(D, O); h = caps(F) if len(sys.argv) < 3 or not sys.argv[-1].isdigit() else int(sys.argv[-1])
    keep = [0] + [t for t in range(1, len(S)) if S[t][:2 * h] != S[t - 1][:2 * h]]
    ch = [i for i in range(1, len(keep)) if O[keep[i]][h - 1] != O[keep[i - 1]][h - 1]]
    adj = sum(1 for a, b in zip(ch, ch[1:]) if b == a + 1)
    print(f'{os.path.basename(p)}: d {D["d"]} N+M {6 * D["d"]} caps {caps(F)} T {len(S) - 1} core steps {len(keep) - 1} o({h - 1}) changes {len(ch)} adjacent {adj} share {adj / max(len(ch), 1):.3f}')
