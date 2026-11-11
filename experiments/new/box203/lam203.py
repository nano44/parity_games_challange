#!/usr/bin/env python3
"""Box 203 part 2 (L-NEW successor 68): Lemma (k+1)-LAMBDA on IDEAL-CYC. At every state, the cycle nodes Lambda_t(v) over all vertices v
other than c_W, c_X and the e-vertices whose successor is c_W take at most k + 1 values, k := the Xi-feedback number (box202 fvs202.kfvs).
Counters per genome: maxL (max over states of #distinct such Lambda), lfail (states with maxL > k + 1; must be 0; genomes with k > 12
are skipped for lfail). Control LAM_CTRL=1: the bound is k (fires where some state has k + 1 values).
Usage: lam203.py G.json ... | lam203.py --rand MODE SEED COUNT (MODE k1 / k2 as asc203, rand = rand191.rgen d 1-6, w 1-3, degree 2-3)."""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gfc203
sys.path.insert(0, os.path.join(gfc203.ROOT, "experiments/new/box191"))
import fvs202
CTRL = os.environ.get("LAM_CTRL", "0")

def lam(G):
    H, n, E, V, gates = gfc203.hist_ideal(G); k = fvs202.kfvs(G)[0]
    excl = {V["cW"], V["cX"]} | {V[("e", q)] for (q, a, b) in gates.values() if G["opts"][q[0]][q[1]][0] < 0}
    mL = 0; bad = 0
    for vs, sb in H:
        L = len({vs[v][0] for v in range(n) if v not in excl}); mL = max(mL, L)
        if isinstance(k, int) and L > k + (0 if CTRL == "1" else 1): bad += 1
    return dict(k=k, maxL=mL, lfail=bad, T=len(H) - 1)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--rand":
        mode, seed, cnt = a[1], int(a[2]), int(a[3]); rng = random.Random(seed); c = collections.Counter()
        import rand191
        os.environ["K1_MODE"] = "2" if mode == "k2" else "1"
        import k1srch202
        while c["genomes"] < cnt:
            if mode == "rand": G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
            else:
                G = k1srch202.mk(rng)
                if G is None or fvs202.kfvs(G)[0] != (2 if mode == "k2" else 1): continue
            r = lam(G); c["genomes"] += 1; c["lfail"] += r["lfail"]; c["maxL"] = max(c["maxL"], r["maxL"])
        print(mode, "seed", seed, "ctrl", CTRL, dict(c), flush=True)
    else:
        for f in a:
            r = lam(json.load(open(f))); print(os.path.basename(f), "ctrl", CTRL, " ".join(f"{k} {v}" for k, v in r.items()), flush=True)
