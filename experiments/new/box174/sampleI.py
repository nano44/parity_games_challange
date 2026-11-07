#!/usr/bin/env python3
"""L-NEW box 174: random sampling of L^R_d genomes (all starts) for the largest I (maximal top-only runs). Usage: sampleI.py d n seed"""
import os, sys, json, random, itertools
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
sys.path.insert(0, os.path.join(H, "..", "box162")); fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}
exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl); rand_lr = fl["rand_lr"]
d, n, seed = map(int, sys.argv[1:4]); rng = random.Random(seed); best = (-1,)
for it in range(n):
    G = rand_lr(d, rng, iso=False); g = Gen(G); top = d - 1
    for st in itertools.product((0, 1), repeat=2 * d):
        S, _ = g.run(st)
        k = "".join("L" if any(S[t][v] != S[t - 1][v] and G["lev"][v] < top for v in range(G["N"])) else "T" for t in range(1, len(S)))
        I = sum(1 for i, c in enumerate(k) if c == "T" and (i == 0 or k[i - 1] == "L"))
        if (I, len(k)) > best[:2]:
            best = (I, len(k), k); G["start"] = list(st); json.dump(G, open(os.path.join(H, "out", "sampleI_d%d_s%d.json" % (d, seed)), "w"))
            print(it, best, flush=True)
print("DONE", best)
