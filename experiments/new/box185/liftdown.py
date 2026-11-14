#!/usr/bin/env python3
"""L-NEW box 185: lift an fl/mv text genome of top level m to m + 1 by adding a NEW level 0 below (old mover v -> v + 2, old Xi-targets
shifted; the old level-0 options now W-point to the new movers 0, 1 by the R197 convention). New level-0 options: Xi-target X or a random
old mover (acyclic automatically: nothing points down to a new mover unless chosen), ranks inserted at random, gates inserted at random.
Usage: liftdown.py in.txt out.txt seed"""
import sys, random
L = {}
for line in open(sys.argv[1]):
    w = line.split()
    if w: L[w[0]] = [int(x) for x in w[1:]]
m = L["m"][0]; N = 2 * (m + 1); M = 2 * N; rnd = random.Random(int(sys.argv[3]))
xt = [rnd.choice([-1, -1] + list(range(2, N + 2))) for _ in range(4)] + [(t + 2 if t >= 0 else -1) for t in L["xt"]]
sb = sorted(L["br"]); old = [sb.index(r) for r in L["br"]]; tot = M + 4
pos = sorted(rnd.sample(range(tot), 4)); rest = [i for i in range(tot) if i not in pos]
br = pos[:] ; rnd.shuffle(br); br = br + [rest[r] for r in old]
bp = [rnd.randint(0, 1) for _ in range(4)] + L["bp"]
sg = sorted(L["gate"]); og = [sg.index(g) for g in L["gate"]]
gp = sorted(rnd.sample(range(tot), 4)); grest = [i for i in range(tot) if i not in gp]; rnd.shuffle(gp)
gate = gp + [grest[g] for g in og]
open(sys.argv[2], "w").write("m %d\nxt %s\nbr %s\nbp %s\ngate %s\n" % (m + 1, " ".join(map(str, xt)), " ".join(map(str, br)),
    " ".join(map(str, bp)), " ".join(map(str, gate))))
