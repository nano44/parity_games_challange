#!/usr/bin/env python3
"""box 80, second-instance test of L-LOWER's DOMINANCE-FREEZE observation (Lead 15:14Z). For a genome (stored start) and level j:
a FAILING j-window is one in which some member of the pair j does not move exactly once. For each failing window and each member x
that does not move in it, the DECIDER at each state of the window (s_(a-1) .. s_(e-1)) is the option (owner mover, option index) of
largest rank in the symmetric difference of the two option paths of x (path of (x, k): (x, k) followed by the current options along
its Xi-chain); its sign decides pi(x) (R104: values compare by the largest-rank beta of the symmetric difference). Reports, per failing
window, the deciders seen, whether the decider is the same at every state, and whether its owner moved in the window ('parked' if not)."""
import json, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box76"))
from sim80 import Sim
from check80 import windows
G = json.load(open(sys.argv[1])); j = int(sys.argv[2]); sim = Sim(G); S = sim.run()
F, dbl, W = windows(sim, S); N = sim.N
rank = lambda x, k: G["br"][G["opts"][x][k][2]]
def path(s, x, k):
    out = [(x, k)]; y = sim.xt[x][k]
    while y >= 0: out.append((y, s[y])); y = sim.xt[y][s[y]]
    return set(out)
def decider(s, x):
    d = path(s, x, 0) ^ path(s, x, 1); return max(d, key=lambda o: rank(*o))
fail = 0; summ = collections.Counter(); per = []
for i, (a, e, m) in enumerate(W[j]):
    for x in (2 * j, 2 * j + 1):
        mv = sum(1 for t in range(a, e + 1) if S[t][x] != S[t - 1][x])
        if mv == 1: continue
        ds = [decider(S[t], x) for t in range(a - 1, e)]
        uniq = sorted(set(ds)); own = {o[0] for o in uniq}
        parked = all(all(S[t][o] == S[a - 1][o] for t in range(a - 1, e + 1)) for o in own)
        summ[(x, tuple(uniq), parked)] += 1; per.append(i)
    if any(sum(1 for t in range(a, e + 1) if S[t][x] != S[t - 1][x]) != 1 for x in (2 * j, 2 * j + 1)): fail += 1
print("%s level %d: %d of %d j-windows failing" % (os.path.basename(sys.argv[1]), j, fail, len(W[j])))
for (x, uniq, parked), n in sorted(summ.items(), key=lambda kv: -kv[1]):
    print("  member %d: decider(s) %s (owner level(s) %s, rank(s) %s) %s : %d (window, member)" % (
        x, uniq, [o[0] // 2 for o in uniq], [rank(*o) for o in uniq], "PARKED owner" if parked else "owner moves", n))
