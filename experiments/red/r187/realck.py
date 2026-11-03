#!/usr/bin/env python3
"""L-RED R187 REALCK: Theorem REALIZE check (docs/red/R187-ladder.md section 1). For IDEAL genomes (files) or N random ACYC genomes
(--rand N d seed): builds the STAB+K+ESC game, runs real N5 and prints the IDEAL length, FAITHFUL (longest prefix with tau = W-face and
sigma-bar = Xi-face at every gate, W unchanged, no fallback; stabrun.py) and whether the real mover states equal the IDEAL states."""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r178"), os.path.join(H, "..", "r170"), os.path.join(H, "..", "..", "new", "box21")]
import t2, downgen
if sys.argv[1] == "--rand":
    N, d, seed = map(int, sys.argv[2:5]); rng = random.Random(seed); ok = 0; tot = 0
    for _ in range(N):
        r = t2.cmp(downgen.randacyc(d, 2, rng)); tot += 1; ok += r[3] and r[0] == r[2]
    print(f"REALCK random ACYC d {d} games {tot} equal {ok}")
else:
    for f in sys.argv[1:]:
        L, why, fa, eq = t2.cmp(json.load(open(f))); print(f"REALCK {os.path.basename(f)} IDEAL {L} {why} FAITHFUL {fa} EQUAL {eq}")
