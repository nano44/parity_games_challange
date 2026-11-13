#!/usr/bin/env python3
"""L-SI box 97: HYPOTHESIS [STD3] measured on N5'-xi's run from S3 on Gamma3(G) (L-NEW gamma3 / n5v / n5x / eg195 at the pins of
box91/pins.txt), up to and including the first fallback's source state T3.
Standard state (R117 P-N5-REACH §3, as R122's frozen frame): sigma = R104's start transported through the pads at every Even vertex that
is not a mover (K0 -> pA, K1 -> s, K3 -> K2, beta_g -> xt(g) if a mover else pb_g; pads, e, c's have one successor) and tau = pe_g at
every gate, K2 -> K2.
Counters (unit state; must be 0): nstd = states j <= T3 with sigma off the movers or tau not standard; s0 = genomes whose state 0 is not
standard [S3-START]; nfb = genomes with no fallback before the cap; nhow = transitions j -> j+1 (j < T3) where some mover moves to a
successor that is not a ⊴-best one for state j's values [Howard step]. Records: genomes, cyclic (Xi-cyclic genomes), states (sum T3 + 1).
Control CTRL=post: the run continues 3 iterations past the first fallback (outside [STD3]); nstd then counts non-standard states there.
Usage: std97.py inst G.json ... | std97.py rand SEED COUNT  (ROOT = archive of l-new fcba92fc, as for box91/mult91.py)"""
import sys, os, json, random
R = os.environ["ROOT"]; os.environ.setdefault("EG195_ROOT", R)
sys.path[:0] = [os.path.join(R, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import eg195, gamma3, n5v, n5x, rand191
CTRL = os.environ.get("CTRL", "")

def one(G, cap=20000):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0)
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    N, opts = G["N"], G["opts"]; movers = set(range(N))
    want = {V[("K", 0)]: V["pA"], V[("K", 1)]: V["s"], V[("K", 3)]: V[("K", 2)]}
    for x in range(N):
        for k, (wt, xt, b) in enumerate(opts[x]):
            want[V[("b", (x, k))]] = xt if xt >= 0 else V[("pb", (x, k))]
    wtau = {V[("K", 2)]: V[("K", 2)]}
    for x in range(N):
        for k in range(len(opts[x])): wtau[V[("g", (x, k))]] = V[("pe", (x, k))]
    std = lambda s, t: all(s[v] == w for v, w in want.items()) and all(t[v] == w for v, w in wtau.items())
    c = dict(nstd=0, s0=0, nfb=0, nhow=0, states=0); post = 0
    if not std(sigma, tau): c["s0"] = 1
    for j in range(cap + 1):
        c["states"] += 1
        if not std(sigma, tau): c["nstd"] += 1
        vs, _ = E.evaluate(tuple(sigma))
        res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None: break
        if res[4]:
            post = post + 1 if CTRL == "post" else 99
            if post > 3: break
        for x in (movers if not post else ()):
            if res[0][x] != sigma[x]:
                best = max(E.key(vs[w]) for w in g.succ[x])
                if E.key(vs[res[0][x]]) != best: c["nhow"] += 1
        sigma, tau = list(res[0]), list(res[1])
    else:
        c["nfb"] = 1
    return c

if __name__ == "__main__":
    K = ("nstd", "s0", "nfb", "nhow", "states")
    if sys.argv[1] == "inst":
        L = [(os.path.basename(f), json.load(open(f))) for f in sys.argv[2:]]
    else:
        rng = random.Random(int(sys.argv[2])); L = []
        for i in range(int(sys.argv[3])):
            d, w, D = rng.randint(1, 5), rng.randint(1, 3), rng.randint(2, 3)
            L.append(("r%d" % i, rand191.rgen(rng, d, w, D)))
    tot = dict.fromkeys(K, 0); gen = cyc = 0
    print("name cyclic N+M " + " ".join(K), flush=True)
    for nm, G in L:
        G = G.get("genome", G); c = one(G); cy = not eg195.acyclic(G); gen += 1; cyc += cy
        for k in K: tot[k] += c[k]
        if sys.argv[1] == "inst" or any(c[k] for k in K[:4]):
            print(nm, int(cy), G["N"] + sum(len(o) for o in G["opts"]), " ".join(str(c[k]) for k in K), flush=True)
    print("TOTAL genomes %d cyclic %d " % (gen, cyc) + " ".join("%s %d" % (k, tot[k]) for k in K), flush=True)
