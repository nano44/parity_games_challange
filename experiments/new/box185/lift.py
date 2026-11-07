#!/usr/bin/env python3
"""L-NEW box 185: lift an fl/mv text genome of top level m to m + 1 by adding a top pair (movers 2m+2, 2m+3) whose options are
Xi-cross-wired onto the old top pair (option 0 -> 2m+1, option 1 -> 2m), with ranks above every old rank (random order, seed) and
gates appended at random positions. Usage: lift.py in.txt out.txt seed [cross|direct|x]"""
import sys, random
L = {}
for line in open(sys.argv[1]):
    w = line.split()
    if w: L[w[0]] = [int(x) for x in w[1:]]
m = L["m"][0]; N = 2 * (m + 1); rnd = random.Random(int(sys.argv[3])); mode = sys.argv[4] if len(sys.argv) > 4 else "cross"
a, b = 2 * m, 2 * m + 1
new = {"cross": [b, a, b, a], "direct": [a, b, a, b], "x": [-1, -1, -1, -1]}[mode]
xt = L["xt"] + new
M = 2 * N; sb = sorted(L["br"]); nr = list(range(M, M + 4)); rnd.shuffle(nr); br = [sb.index(r) for r in L["br"]] + nr
bp = L["bp"] + [rnd.randint(0, 1) for _ in range(4)]
# gates: re-rank old gates with 4 new values inserted at random positions
srt = sorted(L["gate"]); old = [srt.index(g) for g in L["gate"]]; tot = M + 4; pos = sorted(rnd.sample(range(tot), 4)); rest = [i for i in range(tot) if i not in pos]
mp = {g: rest[g] for g in range(M)}; gate = [mp[g] for g in old] + pos
rnd.shuffle(gate[-4:])
open(sys.argv[2], "w").write("m %d\nxt %s\nbr %s\nbp %s\ngate %s\n" % (m + 1, " ".join(map(str, xt)), " ".join(map(str, br)),
    " ".join(map(str, bp)), " ".join(map(str, gate))))
