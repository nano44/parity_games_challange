#!/usr/bin/env python3
"""REFEREE-2: build o-acyclic C^1O games whose X part is a given one-player game (all its vertices keep their ids 0..|X|-1) and
whose Y part is random: o (Odd, exits into X), plus Even vertices with edges into Y, into X and to o; o lies on no cycle because Y
has no edge from X. Writes game.pg and game.start (X start from the given .start, Y random).  Usage: compose.py in.pg in.start out_prefix seed nY"""
import sys, random
inp, instart, out, seed, nY = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
rng = random.Random(seed)
rows = {}
for line in open(inp):
    line = line.strip().rstrip(";")
    if not line or line.startswith("parity"): continue
    p = line.split(); rows[int(p[0])] = (int(p[1]), int(p[2]), [int(t) for t in p[3].split(",")])
nX = len(rows); n = nX + nY
prio = [rows[v][0] for v in range(nX)]; owner = [rows[v][1] for v in range(nX)]; succ = [rows[v][2] for v in range(nX)]
o = nX
yv = list(range(nX + 1, n))
for v in range(nX, n):
    prio.append(rng.randrange(max(prio) + 3)); owner.append(1 if v == o else 0)
    if v == o:
        succ.append(sorted(set(rng.sample(range(nX), rng.choice((2, 3))))))
    else:
        cands = set(rng.sample(range(nX), rng.choice((0, 1, 1)))) | ({o} if rng.random() < 0.7 else set())
        if yv and rng.random() < 0.6: cands.add(rng.choice(yv))
        if not cands: cands = {o}
        succ.append(sorted(cands))
with open(out + ".pg", "w") as f:
    f.write(f"parity {n - 1};\n")
    for v in range(n): f.write(f"{v} {prio[v]} {owner[v]} {','.join(map(str, succ[v]))};\n")
sig = {}
for tok in open(instart).readline().split()[1:]:
    a, b = map(int, tok.split(":")); sig[a] = b
for v in yv: sig[v] = rng.choice(succ[v])
with open(out + ".start", "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(sig.items())) + "\n")
    f.write(f"TAU0 {o}:{rng.choice(succ[o])}\n")
print(out, "n", n, "o", o, "exits", succ[o])
