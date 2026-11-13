#!/usr/bin/env python3
"""Box 213 G-2 (L-NEW successor 75): on every genome with an acyclic Xi-graph (R104's x -> xt, the beta-targets), N5's run on Gamma3(G)
from S3 up to its first fallback is ONE class-frozen window: no vertex lags against the last state (b' = 0), and every class is
(reward of a cycle node, {}) for non-e vertices. Engine: key213.history (read-only import). Per genome:
  g2fail   (must 0; unit genomes): Xi-acyclic and b' > 0 (some vertex lags at some state)
  g2e      (must 0; unit (state, vertex other than an e-vertex or its pe pad)): Xi-acyclic and the class's e-set is non-empty
           [R122 BETA-ACYC's no-e-vertex clause, read on Gamma3: the pad pe_g -> e_g is e_g's own entry]
  CONTROL  lagcyc (unit genomes): Xi-CYCLIC and b' > 0 (must be > 0 on some genome of a set with Xi-cyclic genomes)
Usage: g2_213.py G.json ... | g2_213.py --rand SEED COUNT MODE"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import key213, eg195
def xacyc(G):
    adj = {x: [xt for (_, xt, _) in G["opts"][x] if xt >= 0] for x in range(G["N"])}; col = {}
    def dfs(x):
        col[x] = 1
        for y in adj[x]:
            if col.get(y) == 1 or (y not in col and not dfs(y)): return False
        col[x] = 2; return True
    return int(all(x in col or dfs(x) for x in adj))
def one(G):
    g, E, H, cls, mv = key213.history(G); n, T = g.n, len(H) - 1; c = collections.Counter(); a = xacyc(G); c["xacyc"] = a; c["T"] = T
    import gamma3
    _, _, _, V = gamma3.build(G, eg195.PADS); ev = set(v for k, v in V.items() if isinstance(k, tuple) and k[0] in ("e", "pe"))
    bp = next(t for t in range(T + 1) if all(cls[t][x] == cls[T][x] for x in range(n)))
    if a:
        c["g2fail"] = int(bp > 0); c["g2e"] = sum(1 for t in range(T + 1) for v in range(n) if v not in ev and cls[t][v][1] != 0)
    else: c["lagcyc"] = int(bp > 0)
    return c
KEYS = ("g2fail", "g2e", "lagcyc", "xacyc", "T")
if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--rand":
        seed, cnt, mode = int(a[1]), int(a[2]), a[3]; rng = random.Random(seed); k = 0; tot = collections.Counter()
        while k < cnt:
            G = eg195.gen(rng, mode)
            if G is None or G["N"] < 2: continue
            k += 1; c = one(G)
            for key in KEYS: tot[key] = max(tot[key], c[key]) if key == "T" else tot[key] + c[key]
        print("rand", mode, "seed", seed, "genomes", k, " ".join("%s %d" % (key, tot[key]) for key in KEYS), flush=True)
    else:
        for fn in a:
            G = json.load(open(fn)); G = G.get("genome", G); c = one(G)
            print(os.path.basename(fn), " ".join("%s %d" % (key, c[key]) for key in KEYS), flush=True)
