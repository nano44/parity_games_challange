#!/usr/bin/env python3
"""L-SI box 17: write game #I of a --rand COUNT NLO NHI SEED stream (rund.py / rel.py / gap.py / tcdir.py generator) to OUT.pg, with its
start pair to OUT.start when #I is even (odd #: S3 start, no file). Usage: dumprand.py NLO NHI SEED I OUT  (K env as the checkers)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
lo, hi, seed, want = map(int, sys.argv[1:5]); out = sys.argv[5]; rng = random.Random(seed); i = 0; K = int(os.environ.get("K", "0"))
while i < want:
    g = rand_ckO(rng, lo, hi, K or rng.choice((2, 2, 3, 4)))
    if g is None: continue
    i += 1
    st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
with open(out + ".pg", "w") as f:
    f.write(f"parity {g.n - 1};\n")
    for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
if want % 2 == 0:
    with open(out + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(st[0].items())) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(st[1].items())) + "\n")
print(out, g.n)
