#!/usr/bin/env python3
"""L-RED R212: lift an E_m genome (fk text) to E_(m+1). Modes: top (new level m+1, random options, Xi-targets X or any upper mover),
bot (new level 1 inserted above level 0; old levels shift up; new movers random). Ranks of the old options keep their order and are
interleaved at random with the new ones; same for gates. Usage: extend.py in.txt mode seed out.txt"""
import sys, random
def rd(p):
    L = {}
    for line in open(p):
        w = line.split()
        if w: L[w[0]] = [int(x) for x in w[1:]]
    return L
L = rd(sys.argv[1]); mode, seed, out = sys.argv[2], int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
m = L["m"][0]; N = 2 * (m + 1); N2 = N + 2; M2 = 2 * N2
# mover map old -> new
mp = {v: v for v in range(N)} if mode == "top" else {v: (v if v < 2 else v + 2) for v in range(N)}
new = [N, N + 1] if mode == "top" else [2, 3]
xt = [-1] * (2 * N2); br = [None] * M2; bp = [0] * M2; gate = [None] * M2
for v in range(N):
    for k in range(2):
        o = 2 * v + k; no = 2 * mp[v] + k
        xt[no] = mp[L["xt"][o]] if L["xt"][o] >= 0 else -1
        br[no] = ("o", L["br"][o]); bp[no] = L["bp"][o]; gate[no] = ("o", L["gate"][o])
# acyclicity: new movers' targets must not reach back; for top: targets among old upper movers (old graph acyclic, no edge into new)
# for bot: same (no old option targets the new movers)
for v in new:
    for k in range(2):
        cand = [mp[u] for u in range(2, N)] + [-1, -1]
        xt[2 * v + k] = rng.choice(cand); br[2 * v + k] = ("n", rng.random()); bp[2 * v + k] = rng.randint(0, 1); gate[2 * v + k] = ("n", rng.random())
def rerank(arr, oldvals):
    olds = sorted(i for i in range(M2) if arr[i][0] == "o"); news = [i for i in range(M2) if arr[i][0] == "n"]
    seq = sorted(olds, key=lambda i: arr[i][1])  # old order
    pos = list(range(M2)); rng.shuffle(pos); slots_new = set(rng.sample(range(M2), len(news)))
    res = [None] * M2; it_old = iter(seq); nl = sorted(news, key=lambda i: arr[i][1]); it_new = iter(nl)
    for r in range(M2):
        i = next(it_new) if r in slots_new else next(it_old); res[i] = r
    return res
brn = rerank(br, None); gn = rerank(gate, None)
# level 0 must realise both bits
while len({int(gn[a] < gn[2 + c]) for a in range(2) for c in range(2)}) < 2: gn = rerank(gate, None)
open(out, "w").write("m %d\nxt %s\nbr %s\nbp %s\ngate %s\n" % (m + 1, " ".join(map(str, xt)), " ".join(map(str, brn)), " ".join(map(str, bp)), " ".join(map(str, gn))))
