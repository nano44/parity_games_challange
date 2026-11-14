#!/usr/bin/env python3
"""Box 205 (L-NEW successor 69): Lemma BETA-LOC on IDEAL-CYC. At a state s and gate g = (x, j): if xt(g) is X or the Xi_sigma_s-path
from xt(g) ends at X (no Xi_sigma cycle reached), and Lambda_s(e_g) is not an odd-priority vertex other than K1, then Odd's optimal
counterstrategy takes the beta-face at g. Counters (TOTALS): prem (unit (gate, state) pairs meeting the premise), bfail (unit (gate,
state): premise met and sigma-bar(g) != beta_g; must be 0); acyc_steps (unit steps t with Xi_sigma acyclic at t-1 and t), nfail (unit
gate flips at such steps; must be 0); flips, naive (unit flips at which xt(g)'s Xi_sigma path ends at X at both t-1 and t: the naive
«flips only in the cycle's beta-basin», DEAD when > 0). Control BL_CTRL=1 drops the odd-node exclusion from the premise (bfail fires).
Usage: betaloc205.py G.json ... | betaloc205.py --rand MODE SEED COUNT [DUMP.json] (MODE k1 / k2 as box203 lam203, rand = rand191)."""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "../../.."))
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box203")); import gfc203
sys.path.insert(0, os.path.join(gfc203.ROOT, "experiments/new/box191")); import fvs202, idealcyc
CTRL = os.environ.get("BL_CTRL", "0")

def ends_x(G, s, x):
    seen = set()
    while x >= 0 and x not in seen: seen.add(x); x = G["opts"][x][s[x]][1]
    return x < 0

def run(G, c, dump=None):
    st = idealcyc.run(G, cap=20000); h = idealcyc.build(G)[0]; H, n, E, V, gates = gfc203.hist_ideal(G); K1 = V[("K", 1)]
    assert len(st) == len(H)
    for s in range(len(H)):
        for gv, (q, a, b) in gates.items():
            x, j = q; xt = G["opts"][x][j][1]; L = H[s][0][a][0]
            odd = h.prio[L] % 2 == 1 and L != K1
            if (xt < 0 or ends_x(G, st[s], xt)) and (CTRL == "1" or not odd):
                c["prem"] += 1; c["bfail"] += H[s][1][gv] != b
    for t in range(1, len(H)):
        ac = all(ends_x(G, st[t - 1], x) and ends_x(G, st[t], x) for x in range(G["N"]))
        c["acyc_steps"] += ac
        for gv, (q, a, b) in gates.items():
            if H[t - 1][1][gv] != H[t][1][gv]:
                xt = G["opts"][q[0]][q[1]][1]; c["flips"] += 1; c["nfail"] += ac
                nv = xt < 0 or (ends_x(G, st[t - 1], xt) and ends_x(G, st[t], xt))
                c["naive"] += nv
                if nv and dump and not os.path.exists(dump): json.dump(G, open(dump, "w"))

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--rand":
        mode, seed, cnt = a[1], int(a[2]), int(a[3]); dump = a[4] if len(a) > 4 else None
        rng = random.Random(seed); c = collections.Counter()
        import rand191
        os.environ["K1_MODE"] = "2" if mode == "k2" else "1"
        import k1srch202
        while c["genomes"] < cnt:
            if mode == "rand": G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
            else:
                G = k1srch202.mk(rng)
                if G is None or fvs202.kfvs(G)[0] != (2 if mode == "k2" else 1): continue
            c["genomes"] += 1; run(G, c, dump)
        print(mode, "seed", seed, "ctrl", CTRL, dict(sorted(c.items())), flush=True)
    else:
        for f in a:
            c = collections.Counter(); run(json.load(open(f)), c)
            print(os.path.basename(f), "ctrl", CTRL, dict(sorted(c.items())), flush=True)
