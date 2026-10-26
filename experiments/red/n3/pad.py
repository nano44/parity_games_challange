#!/usr/bin/env python3
"""Pad a game with K new vertices (random owner/priority, edges into the old game and among themselves); old vertices keep their edges
plus, with probability P, one extra edge to a new vertex. Start pair extended at random. Usage: pad.py GAME START K SEED OUT [P]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x, pg
g = n3x.load(sys.argv[1]); st = n3x.readstart(sys.argv[2]); K = int(sys.argv[3]); rng = random.Random(int(sys.argv[4])); out = sys.argv[5]
P = float(sys.argv[6]) if len(sys.argv) > 6 else 0.1
n = g.n; N = n + K
prio = list(g.prio) + [rng.randrange(max(g.prio) + 10) for _ in range(K)]
owner = list(g.owner) + [rng.randrange(2) for _ in range(K)]
succ = [list(s) for s in g.succ] + [sorted(set(rng.randrange(N) for _ in range(rng.choice([1, 2])))) for _ in range(K)]
for v in range(n):
    if g.owner[v] == 0 and rng.random() < P: succ[v] = sorted(set(succ[v] + [rng.randrange(n, N)]))
h = pg.Game(prio, owner, succ); pg.write(h, out)
s0, t0 = dict(st[0]), dict(st[1])
for v in range(n, N):
    (s0 if owner[v] == 0 else t0)[v] = rng.choice(succ[v])
open(out[:-3] + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in s0.items()) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in t0.items()) + "\n")
