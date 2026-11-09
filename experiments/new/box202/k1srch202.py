#!/usr/bin/env python3
"""Box 202 (L-NEW successor 67): random search for CONJECTURE K1-FLIP on genomes with Xi-feedback number k = 1.
Generator: eg195.gen(rng, 'acyc') (Xi-edges to smaller index only), then pick a mover f and redirect a random fraction of options
(x, j) with x < f, or x = f, to Xi-target f (edges INTO f from below, or a self-loop): every Xi-cycle then passes f, so k <= 1;
genomes with k != 1 (fvs202.kfvs) are skipped. Optionally (K1_MODE=2) a second such vertex f2 (then k <= 2; for comparison).
Per genome: T3, C, R (fvs202.run), per-gate flips and face-Lambda changes (as gflip202). Counters (totals over the sample):
  k1fail : gates with flips(g) > 2*lamch(g) + 1                                   [CONJECTURE K1-FLIP, k = 1]
  k1c2fail: gates with flips(g) > 2*(lamch(g) + 1)                               [CONJECTURE K1-FLIP(2)]
  maxflip, maxT3/N: maxima. Control K1_CTRL=1: lamch := -1 (k1fail fires on every flipping gate).
Usage: k1srch202.py SEED COUNT  (ROOT default from this file's place). Freezes the first k1fail genome to k1fail_<seed>.json."""
import sys, os, json, random, collections
ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import eg195, gamma3, n5v, n5x, fvs202
MODE = os.environ.get("K1_MODE", "1"); CTRL = os.environ.get("K1_CTRL", "0"); bad2 = []

def mk(rng):
    G = eg195.gen(rng, "acyc"); N = G["N"]
    if N < 2: return None
    fs = rng.sample(range(N), 2 if MODE == "2" else 1); p = rng.choice([0.2, 0.4, 0.7])
    for f in fs:
        for x in range(N):
            if x <= f:
                for o in G["opts"][x]:
                    if rng.random() < p: o[1] = f
    return G

def census(G):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: kk for kk, v in V.items()}
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); H = []
    while len(H) <= 3000:
        vs, tb = E.evaluate(tuple(sigma)); H.append((tuple(sigma), vs, tb)); res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        sigma, tau = res[0], res[1]
    T = len(H) - 1; gates = [v for v in range(n) if isinstance(name[v], tuple) and name[v][0] == "g"]
    bad = 0; mf = 0; bad2.clear()
    for q in gates:
        pe, pb = V[("pe", name[q][1])], V[("pbeta", name[q][1])]
        fl = sum(H[t - 1][2][q] != H[t][2][q] for t in range(1, T + 1))
        lc = sum((H[t - 1][1][pe][0] != H[t][1][pe][0]) or (H[t - 1][1][pb][0] != H[t][1][pb][0]) for t in range(1, T + 1))
        if CTRL == "1": lc = -1
        mf = max(mf, fl); bad += fl > 2 * lc + 1; bad2.append(fl > 2 * (lc + 1))
    return T, bad, mf

if __name__ == "__main__":
    seed, cnt = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); c = collections.Counter(); froze = False
    while c["genomes"] < cnt:
        G = mk(rng)
        if G is None: continue
        k = fvs202.kfvs(G)[0]
        if k != (2 if MODE == "2" else 1): c["skipped"] += 1; continue
        T, bad, mf = census(G); c["genomes"] += 1; c["k1fail"] += bad; c["k1c2fail"] += sum(bad2); c["maxflip"] = max(c["maxflip"], mf)
        c["maxT3"] = max(c["maxT3"], T); c["maxT3perN"] = max(c["maxT3perN"], round(T / G["N"], 2))
        if bad and not froze:
            json.dump(G, open(f"k1fail_{seed}.json", "w")); froze = True
        if c["genomes"] % 200 == 0: print(dict(c), flush=True)
    print("FINAL", "mode", MODE, "ctrl", CTRL, dict(c), flush=True)
