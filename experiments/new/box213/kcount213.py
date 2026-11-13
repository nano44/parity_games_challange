#!/usr/bin/env python3
"""Box 213 KEY-TAU (iii) DATA (L-NEW successor 75): what KEY-TAU's count measures. N5 (box190 n5v.step mode spec) from S3 on Gamma3(G) up
to its first fallback. Per genome:
  T        steps before the first fallback
  sumsw    total mover switches; maxsw: the largest number of switches of ONE mover
  maxK     max over movers of |K(x)| = the number of tau-paths of x to c_W in the W-graph (x -> wt over all options; wt < 0 = c_W),
           counted by dynamic programming (capped at 10**18; 0 if the W-graph has a cycle through x: not seen on Gamma3, W3-ALL)
  slack    max over movers of |K(x)| - 1 - (switches of x)  (KEY-TAU (iii) says it is >= 0: must-0 counter kviol counts movers with < 0)
  N, M     movers, options
Usage: kcount213.py G.json ... | kcount213.py --rand SEED COUNT MODE"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box208"))
import level208
import n5v, eg195, gamma3, n5x
KEYS = ("kviol", "T", "sumsw", "maxsw", "maxK", "N", "M")
MAXK = ("T", "maxsw", "maxK", "N", "M")
def paths(G):
    N = G["N"]; memo = {}; onstack = set()
    def f(x):
        if x in memo: return memo[x]
        if x in onstack: return 0
        onstack.add(x); s = 0
        for (w, _, _) in G["opts"][x]: s += 1 if w < 0 else f(w)
        onstack.discard(x); memo[x] = min(s, 10 ** 18); return memo[x]
    return [f(x) for x in range(N)]
def one(G):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); mv = [V[("x", x)] for x in range(G["N"])]
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); sw = [0] * len(mv); T = 0
    while T <= 20000:
        res = n5v.step(g, E, Ed, sigma, tau, "spec")
        if res is None or res[4]: break
        for i, x in enumerate(mv): sw[i] += res[0][x] != sigma[x]
        sigma, tau = list(res[0]), list(res[1]); T += 1
    K = paths(G); c = collections.Counter()
    c["T"] = T; c["sumsw"] = sum(sw); c["maxsw"] = max(sw) if sw else 0; c["maxK"] = max(K) if K else 0
    c["kviol"] = sum(1 for i in range(len(mv)) if K[i] - 1 - sw[i] < 0); c["N"] = G["N"]; c["M"] = sum(len(o) for o in G["opts"])
    return c
def fmt(c): return " ".join("%s %d" % (k, c[k]) for k in KEYS)
if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--rand":
        seed, cnt, mode = int(a[1]), int(a[2]), a[3]; rng = random.Random(seed); k = 0; tot = collections.Counter()
        while k < cnt:
            G = eg195.gen(rng, mode)
            if G is None or G["N"] < 2: continue
            k += 1; cc = one(G)
            for key in KEYS: tot[key] = max(tot[key], cc[key]) if key in MAXK else tot[key] + cc[key]
        print("rand", mode, "seed", seed, "genomes", k, fmt(tot), flush=True)
    else:
        for fn in a:
            G = json.load(open(fn)); G = G.get("genome", G); print(os.path.basename(fn), fmt(one(G)), flush=True)
